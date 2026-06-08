#!/usr/bin/env python3
"""Overlay SSSOM mappings onto already-generated LinkML schema YAMLs.

This is the "overlay-only" path: it does NOT re-parse upstream XSDs. Use it
when an ``*.sssom.tsv`` file in ``--mappings-dir`` has been edited and the
new mappings need to be pushed into the schema YAMLs without regenerating
them from scratch.

For each YAML file in ``--schema-dir`` the script:

1. Loads classes, enums, and types.
2. For every class / enum / type whose unsuffixed local name appears as a
    subject in one of the SSSOM TSVs (subject CURIE prefix ``calm:``), merges the
   predicate-mapped CURIEs into the matching mapping slot
   (``exact_mappings``, ``close_mappings``, ``broad_mappings``,
   ``narrow_mappings``, ``related_mappings``). Existing entries are
   preserved; duplicates are dropped.
3. Adds any referenced object-side prefixes to the YAML's ``prefixes`` block
   (URIs come from each TSV's ``#curie_map:`` metadata).
4. Writes the YAML back using the canonical formatter helpers from
    ``calm_to_linkml.py`` so overlay output keeps the same readability/layout
    conventions as a freshly-generated file.

Usage::

    python scripts/apply_sssom_overlay.py \\
        --schema-dir src/calm/schema \\
        --mappings-dir src/calm/mappings

The script is idempotent: running it twice on a clean tree produces no
further changes.
"""
from __future__ import annotations

import argparse
import sys
from collections import OrderedDict
from pathlib import Path

import yaml

# Reuse canonical YAML formatter helpers from calm_to_linkml.py so overlaid
# files keep the same shape as a fresh generator run (block scalars,
# indented list items, blank lines between entries, and double-blank
# separators between top-level blocks).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from calm_to_linkml import _emit_scalar, _emit_section  # noqa: E402


# SKOS predicate -> LinkML mapping slot.
SSSOM_PREDICATE_TO_LINKML_SLOT: dict[str, str] = {
    "skos:exactMatch":   "exact_mappings",
    "skos:closeMatch":   "close_mappings",
    "skos:broadMatch":   "broad_mappings",
    "skos:narrowMatch":  "narrow_mappings",
    "skos:relatedMatch": "related_mappings",
}

# Subject-side CURIE prefix recognised on TSV rows.
_MYSCHEMA_SUBJECT_PREFIXES = (
    "calm:",
)

# Prefixes that are intrinsic to LinkML / SSSOM and need not be declared on
# every schema YAML.
_SSSOM_BUILTIN_PREFIXES = {
    "sssom", "owl", "rdf", "rdfs", "skos", "semapv", "linkml",
}

# Prefixes that are subject-side aliases of the schema itself; declaring
# them on the schemas would be redundant with the existing default.
_MYSCHEMA_OWN_PREFIXES = {
    "calm",
}

# Top-level blocks whose second-level entries should be separated by blank
# lines for readability. ``prefixes`` is intentionally excluded: its entries
# are a compact CURIE table and read better packed together, matching
# calm_to_linkml.build_schema_text (which emits prefixes without separators).
_ENTRY_BLANK_BLOCKS = {
    "subsets",
    "types",
    "enums",
    "slots",
    "classes",
}

# Top-level keys that begin a fresh double-blank-separated block. Every other
# key (scalar header fields such as id/name/title/description/license/see_also/
# source/version, and the default_prefix/default_range scalars that trail the
# prefixes block) attaches to the current block with a single newline. This
# mirrors the block grouping in calm_to_linkml.build_schema_text so overlaid
# files keep the same top-level shape as a fresh generator run instead of
# exploding every header field onto its own double-blank-separated block.
_BLOCK_LEADING_KEYS = {
    "prefixes",
    "imports",
    "subsets",
    "types",
    "enums",
    "slots",
    "classes",
}


# ---------------------------------------------------------------------------
# Canonical layout of mapping slots inside a class / enum / type body
# ---------------------------------------------------------------------------
#
# schema_to_linkml.py emits class / enum / type bodies in this canonical
# order (see VersionEmitter.emit_*):
#
#   description, abstract, is_a, tree_root, mixins, mixin,
#   class_uri / enum_uri / uri,
#   exact_mappings, aliases, in_subset,
#   permissible_values / attributes / slots, ...
#
# New mapping slots are inserted just AFTER the latest preceding
# already-present mapping slot, or just BEFORE the first post-mapping anchor
# that already exists.

_POST_MAPPING_ANCHORS_CLASS = (
    "aliases", "in_subset", "attributes", "slots", "slot_usage",
    "rules", "comments", "annotations",
)
_POST_MAPPING_ANCHORS_ENUM = (
    "aliases", "in_subset", "permissible_values",
)
_POST_MAPPING_ANCHORS_TYPE = (
    "aliases", "in_subset", "pattern", "annotations",
)
_POST_MAPPING_ANCHORS_SLOT = (
    "aliases", "in_subset", "annotations",
)

# Relative order of the five mapping slots within a body.
_MAPPING_SLOT_ORDER = (
    "exact_mappings",
    "close_mappings",
    "broad_mappings",
    "narrow_mappings",
    "related_mappings",
)


# ---------------------------------------------------------------------------
# SSSOM TSV parsing
# ---------------------------------------------------------------------------


def _parse_sssom_metadata(path: Path) -> dict:
    """Parse the leading ``#`` metadata block of an SSSOM TSV as YAML."""
    buf: list[str] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("#"):
                break
            buf.append(line[1:])
    if not buf:
        return {}
    try:
        meta = yaml.safe_load("".join(buf))
    except yaml.YAMLError:
        return {}
    return meta if isinstance(meta, dict) else {}


def _parse_sssom_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    """Return ``(header, rows)`` from the TSV body (skipping metadata)."""
    header: list[str] | None = None
    rows: list[list[str]] = []
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\r\n")
            if not line or line.startswith("#"):
                continue
            fields = line.split("\t")
            if header is None:
                header = fields
                continue
            rows.append(fields)
    return (header or []), rows


def _strip_named_prefix(curie: str) -> str | None:
    """Return the local name if ``curie`` is an schena-subject CURIE, else None."""
    for px in _MYSCHEMA_SUBJECT_PREFIXES:
        if curie.startswith(px):
            return curie[len(px):]
    return None


# ---------------------------------------------------------------------------
# Mapping index
# ---------------------------------------------------------------------------


class MappingIndex:
    """subject_local_name -> mapping_slot -> ordered list of object CURIEs."""

    def __init__(self) -> None:
        self.by_name: dict[str, dict[str, list[str]]] = {}
        self.prefix_uris: dict[str, str] = {}

    def add(self, name: str, slot: str, obj_curie: str) -> None:
        slot_map = self.by_name.setdefault(name, {})
        existing = slot_map.setdefault(slot, [])
        if obj_curie not in existing:
            existing.append(obj_curie)

    def used_prefixes_for(self, name: str) -> set[str]:
        out: set[str] = set()
        for curies in self.by_name.get(name, {}).values():
            for c in curies:
                if ":" in c:
                    out.add(c.split(":", 1)[0])
        return out


def load_mappings(mappings_dir: Path) -> MappingIndex:
    """Load every ``*.sssom.tsv`` under ``mappings_dir`` into one index."""
    idx = MappingIndex()
    for tsv in sorted(mappings_dir.glob("*.sssom.tsv")):
        meta = _parse_sssom_metadata(tsv)
        curie_map = meta.get("curie_map") or {}
        if isinstance(curie_map, dict):
            for px, uri in curie_map.items():
                if px in _SSSOM_BUILTIN_PREFIXES:
                    continue
                idx.prefix_uris.setdefault(px, uri)

        header, rows = _parse_sssom_rows(tsv)
        if not header:
            continue
        col = {name: i for i, name in enumerate(header)}
        try:
            si = col["subject_id"]
            pi = col["predicate_id"]
            oi = col["object_id"]
        except KeyError as missing:
            print(
                f"WARN: {tsv.name} missing required column "
                f"{missing.args[0]!r}; skipping file",
                file=sys.stderr,
            )
            continue
        for row in rows:
            if len(row) <= max(si, pi, oi):
                continue
            subject = row[si].strip()
            predicate = row[pi].strip()
            obj = row[oi].strip()
            local = _strip_named_prefix(subject)
            if local is None:
                continue
            slot = SSSOM_PREDICATE_TO_LINKML_SLOT.get(predicate)
            if slot is None or not obj:
                continue
            idx.add(local, slot, obj)
    return idx


# ---------------------------------------------------------------------------
# YAML overlay
# ---------------------------------------------------------------------------


def _to_ordered(value):
    """Recursively convert plain dicts to OrderedDicts (preserving order)."""
    if isinstance(value, dict):
        return OrderedDict((k, _to_ordered(v)) for k, v in value.items())
    if isinstance(value, list):
        return [_to_ordered(v) for v in value]
    return value


def _insert_mapping_slot(
    body: OrderedDict,
    slot: str,
    curies: list[str],
    post_anchors: tuple[str, ...],
) -> None:
    """Place ``slot`` at its canonical position within ``body``.

    Insertion rules:

    * If ``slot`` already exists, its value is replaced in place.
    * Otherwise insert just after the latest preceding mapping slot already
      in ``body``; failing that, just before the next succeeding mapping
      slot; failing that, just before the first post-mapping anchor that
      already exists; failing that, append.
    """
    if slot in body:
        body[slot] = curies
        return

    target_after: str | None = None
    slot_idx = _MAPPING_SLOT_ORDER.index(slot)
    for s in _MAPPING_SLOT_ORDER[:slot_idx]:
        if s in body:
            target_after = s

    target_before: str | None = None
    if target_after is None:
        for s in _MAPPING_SLOT_ORDER[slot_idx + 1:]:
            if s in body:
                target_before = s
                break
        if target_before is None:
            for k in post_anchors:
                if k in body:
                    target_before = k
                    break

    rebuilt: OrderedDict = OrderedDict()
    inserted = False
    if target_after is not None:
        for k, v in body.items():
            rebuilt[k] = v
            if k == target_after and not inserted:
                rebuilt[slot] = curies
                inserted = True
    elif target_before is not None:
        for k, v in body.items():
            if k == target_before and not inserted:
                rebuilt[slot] = curies
                inserted = True
            rebuilt[k] = v
    if not inserted:
        rebuilt = OrderedDict(body)
        rebuilt[slot] = curies

    body.clear()
    body.update(rebuilt)


def _merge_mappings(
    body: OrderedDict,
    slot_map: dict[str, list[str]],
    post_anchors: tuple[str, ...],
) -> tuple[bool, int]:
    """Merge ``slot_map`` into ``body``. Returns ``(touched, links_added)``."""
    touched = False
    links_added = 0
    # Apply slots in canonical order so the YAML diff is stable across runs.
    for slot in _MAPPING_SLOT_ORDER:
        curies = slot_map.get(slot)
        if not curies:
            continue
        existing = body.get(slot)
        if existing is None:
            _insert_mapping_slot(body, slot, list(curies), post_anchors)
            links_added += len(curies)
            touched = True
        else:
            new_list = list(existing)
            added_here = 0
            for c in curies:
                if c not in new_list:
                    new_list.append(c)
                    added_here += 1
            if added_here:
                body[slot] = new_list
                links_added += added_here
                touched = True
    return touched, links_added


def _ensure_prefixes(
    data: OrderedDict,
    needed: set[str],
    prefix_uris: dict[str, str],
) -> bool:
    """Add referenced prefixes to ``data['prefixes']``. Returns changed flag."""
    changed = False
    prefixes = data.get("prefixes")
    if not isinstance(prefixes, dict):
        prefixes = OrderedDict()
        data["prefixes"] = prefixes
    for px in sorted(needed):
        if px in _SSSOM_BUILTIN_PREFIXES or px in _MYSCHEMA_OWN_PREFIXES:
            continue
        if px in prefixes:
            continue
        uri = prefix_uris.get(px)
        if uri is None:
            print(
                f"WARN: prefix {px!r} referenced by a mapping but no URI "
                f"found in any sssom curie_map; declare it manually.",
                file=sys.stderr,
            )
            continue
        prefixes[px] = uri
        changed = True
    return changed


def _render_schema_body(data: OrderedDict) -> str:
    """Render a full schema body using build_schema.py layout conventions.

    Rules:
    * Lists remain indented (handled by build_schema's dumper).
    * Long strings are emitted as folded/literal block scalars when needed.
    * For key dictionary blocks (prefixes/subsets/types/enums/slots/classes),
      insert a blank line between second-level entries.
    * Consecutive scalar/header entries (id, name, ..., version and the
      default_prefix/default_range scalars) are packed together; each
      structural block (see ``_BLOCK_LEADING_KEYS``) is separated from the
      previous one by double blank lines.
    """
    blocks: list[str] = []
    current: list[str] = []
    for key, value in data.items():
        if isinstance(value, (dict, list)):
            rendered = _emit_section(
                key,
                value,
                blank_between_entries=(
                    isinstance(value, dict) and key in _ENTRY_BLANK_BLOCKS
                ),
            )
        else:
            rendered = _emit_scalar(key, value)

        if not rendered:
            continue

        if key in _BLOCK_LEADING_KEYS and current:
            blocks.append("\n".join(current))
            current = []
        current.append(rendered.rstrip("\n"))

    if current:
        blocks.append("\n".join(current))

    if not blocks:
        return ""
    return "\n\n\n".join(blocks) + "\n"


# ---------------------------------------------------------------------------
# Whole-file overlay
# ---------------------------------------------------------------------------


def overlay_file(schema_path: Path, mappings: MappingIndex) -> tuple[int, int]:
    """Overlay mappings onto one schema YAML in place.

    Returns ``(elements_updated, links_added)``. The file is rewritten only
    when at least one element was modified or a new prefix was declared.
    """
    text = schema_path.read_text(encoding="utf-8")
    # Preserve the original ``---`` + leading ``#`` comment block verbatim;
    # build_schema.py owns the header and we don't want to rewrite it.
    # Consume all leading ``---``, ``#``-comment, and blank lines; stop as
    # soon as we see the first non-comment, non-separator content line.
    header_lines: list[str] = []
    for raw in text.splitlines(keepends=True):
        stripped = raw.rstrip("\n\r")
        if stripped == "---" or stripped.startswith("#"):
            header_lines.append(raw)
        elif stripped == "":
            # Blank line: include it only while still in the header block
            # (i.e., before we have seen any YAML content key).
            header_lines.append(raw)
        else:
            break
    header = "".join(header_lines)

    data = yaml.safe_load(text)
    if data is None:
        data = OrderedDict()
    data = _to_ordered(data)

    elements_updated = 0
    links_added = 0
    used_prefixes: set[str] = set()

    for collection_key, post_anchors in (
        ("classes", _POST_MAPPING_ANCHORS_CLASS),
        ("slots",   _POST_MAPPING_ANCHORS_SLOT),
        ("enums",   _POST_MAPPING_ANCHORS_ENUM),
        ("types",   _POST_MAPPING_ANCHORS_TYPE),
    ):
        collection = data.get(collection_key)
        if not isinstance(collection, dict):
            continue
        for name, body in collection.items():
            if not isinstance(body, OrderedDict):
                continue
            slot_map = mappings.by_name.get(name)
            if not slot_map:
                continue
            touched, n_added = _merge_mappings(body, slot_map, post_anchors)
            if touched:
                elements_updated += 1
                links_added += n_added
                used_prefixes |= mappings.used_prefixes_for(name)

    prefixes_changed = _ensure_prefixes(data, used_prefixes, mappings.prefix_uris)

    if elements_updated or prefixes_changed:
        if not header:
            header = (
                "---\n"
                "# Auto-generated by scripts/build_schema.py\n"
                "# Overlaid by scripts/apply_sssom_overlay.py\n"
                "# DO NOT EDIT BY HAND - re-run the scripts to regenerate.\n"
                "\n"
            )
        # Render with build_schema helpers so overlay output retains the
        # same readability conventions as generated schemas.
        body_yaml = _render_schema_body(data)
        out = header + body_yaml
        schema_path.write_text(out, encoding="utf-8")
    return elements_updated, links_added


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    repo_root = here.parent
    default_schema_dir = (
        repo_root / "src" / "calm" / "schema"
    )
    default_mappings_dir = (
        repo_root / "src" / "calm" / "mappings"
    )

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument(
        "--schema-dir", type=Path, default=default_schema_dir,
        help="directory containing LinkML schema YAML files",
    )
    p.add_argument(
        "--mappings-dir", type=Path, default=default_mappings_dir,
        help="directory containing *.sssom.tsv mapping files",
    )
    args = p.parse_args(argv)

    if not args.schema_dir.is_dir():
        print(f"ERROR: schema-dir {args.schema_dir} is not a directory",
              file=sys.stderr)
        return 1
    if not args.mappings_dir.is_dir():
        print(f"ERROR: mappings-dir {args.mappings_dir} is not a directory",
              file=sys.stderr)
        return 1

    mappings = load_mappings(args.mappings_dir)
    if not mappings.by_name:
        print(
            f"No schema-subject mappings loaded from {args.mappings_dir} "
            "(expected *.sssom.tsv rows with subject prefix "
            f"{_MYSCHEMA_SUBJECT_PREFIXES[0]!r}); nothing to do.",
            file=sys.stderr,
        )
        return 0

    n_subjects = len(mappings.by_name)
    n_links = sum(
        len(curies)
        for slot_map in mappings.by_name.values()
        for curies in slot_map.values()
    )
    referenced_prefixes = sorted({
        c.split(":", 1)[0]
        for slot_map in mappings.by_name.values()
        for curies in slot_map.values()
        for c in curies
        if ":" in c
    })
    print(
        f"Loaded {n_links} mappings across {n_subjects} schema subjects "
        f"(object prefixes: {', '.join(referenced_prefixes) or '-'})"
    )

    schemas = sorted(args.schema_dir.glob("*.yaml"))
    if not schemas:
        print(f"No YAML schemas in {args.schema_dir}", file=sys.stderr)
        return 1

    files_changed = 0
    total_elements = 0
    total_links = 0
    for path in schemas:
        elements, links = overlay_file(path, mappings)
        if elements:
            files_changed += 1
            total_elements += elements
            total_links += links
            print(f"  {path.name}: +{links} links across {elements} elements")

    if total_links:
        print(
            f"\nOverlay complete: {total_links} new mappings applied to "
            f"{total_elements} elements across {files_changed} files"
        )
    else:
        print(
            "\nOverlay complete: schemas already in sync with SSSOM files "
            "- no changes needed"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
