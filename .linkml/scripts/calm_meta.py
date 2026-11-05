#!/usr/bin/env python3
"""Write CALM's JSON Schema files from the LinkML model.

gen-json-schema writes one document with every definition under ``$defs``. CALM
publishes eleven files, each with its definitions under ``defs`` and its own ``$id``.
This script runs the generator once and shapes its output into CALM's layout:

- Each module of the schema becomes the file it renders (``calm_core`` gives
  ``core.json``), and the umbrella's ``CalmArchitecture`` is the root of
  ``core.json``. A class whose exact mapping names a whole file is that file's root.
- A definition takes the key its exact mapping names (``CalmNode`` maps to
  ``core.json#/defs/node``). A class or enum with no published counterpart is
  written inline wherever it is used, as CALM writes it.
- ``$schema`` is draft 2020-12, ``$id`` is CALM's address, and the keys are CALM's,
  which the slots carry as aliases.

linkml 1.12.1's generator needs five repairs here, each a fault of the generator:
the conditions of ``exactly_one_of`` and ``all_of`` name slots rather than their
aliases; a slot that is not required still admits ``null`` through an enum or an
``extra_slots`` range, despite ``--no-include-null``; ``linkml:Any`` excludes arrays;
``list_elements_unique`` writes no ``uniqueItems``; and ``ifabsent`` writes no
``default``.

Four things LinkML cannot state are written from the model by rule: an enum that a
slot only ever offers beside a free string is published open, as CALM's
``node-type-definition`` is; each type with an exact mapping becomes a definition;
``NAMED_ARRAYS`` hoists the one array CALM names, ``option-type``; and a slot that
lists one key under ``aliases`` takes it as its key here alone. That keeps ``$schema``
out of gen-python's attribute names, and ``source``, ``target``, ``unit`` and
``type`` out of the JSON-LD keys a composite with LOKF shares.

calm.json and calm-timeline.json declare CALM's vocabulary beside JSON Schema's and
define nothing, so they are copied from upstream/ unchanged. Usage::

    python scripts/calm_meta.py [--output DIR] [--check]
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "src" / "calm" / "schema"
SCHEMA = SCHEMA_DIR / "calm.yaml"
UPSTREAM = ROOT / "upstream" / "calm-schema" / "v1.3" / "schema"
OUTPUT = ROOT / "meta"

META_BASE = "https://calm.finos.org/release/1.3/meta/"
DRAFT = "https://json-schema.org/draft/2020-12/schema"
TOP_CLASS = "CalmArchitecture"
UMBRELLA = "calm"
COPIED = ("calm.json", "calm-timeline.json")

# CALM names one array, the options of a relationship, as a definition of its own.
NAMED_ARRAYS = {("CalmRelationshipType", "options"): ("core.json", "option-type")}

# The order CALM's files give their keys, so a diff against them reads easily.
KEY_ORDER = (
    "$schema",
    "$id",
    "title",
    "description",
    "type",
    "enum",
    "const",
    "pattern",
    "format",
    "minimum",
    "minItems",
    "uniqueItems",
    "items",
    "properties",
    "required",
    "default",
    "additionalProperties",
    "anyOf",
    "oneOf",
    "allOf",
    "not",
    "examples",
    "defs",
)
CONDITIONALS = ("allOf", "anyOf", "oneOf", "not", "if", "then", "else")


def kebab(name: str) -> str:
    """CalmNodeInterface -> node-interface."""
    if name.startswith("Calm"):
        name = name[len("Calm") :]
    return re.sub(r"(?<!^)(?=[A-Z])", "-", name).lower()


def module_file(module: str) -> str:
    """The file a module renders: calm_control_requirement -> control-requirement.json."""
    if module == UMBRELLA:
        return "core.json"
    return module[len("calm_") :].replace("_", "-") + ".json"


def _walk(node, visit):
    """Call visit on every dict in a JSON tree, children first."""
    if isinstance(node, dict):
        for value in node.values():
            _walk(value, visit)
        visit(node)
    elif isinstance(node, list):
        for item in node:
            _walk(item, visit)


# Maps whose keys are names, not keywords, and keep the order they were built in.
NAME_MAPS = ("properties", "defs", "patternProperties")


def _ordered(node, names=False):
    """A copy with each schema's keywords in CALM's order, the rest after them."""
    if isinstance(node, dict):
        if names:
            keys = list(node)
        else:
            keys = [k for k in KEY_ORDER if k in node]
            keys += sorted(k for k in node if k not in KEY_ORDER)
        return {k: _ordered(node[k], names=not names and k in NAME_MAPS) for k in keys}
    if isinstance(node, list):
        return [_ordered(item) for item in node]
    return node


class Shaper:
    """Turns the generator's single document into CALM's files."""

    def __init__(self, schema: Path = SCHEMA):
        self.sv = SchemaView(str(schema))
        gen = JsonSchemaGenerator(
            str(schema),
            preserve_names=True,
            include_null=False,
            title_from="title",
            mergeimports=True,
            top_class=TOP_CLASS,
        )
        self.defs = json.loads(gen.serialize())["$defs"]
        self.module_of = self.sv.element_by_schema_map()
        self.raw = {
            path.stem: yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in SCHEMA_DIR.glob("calm*.yaml")
        }

    # ---- where each element is published ------------------------------------

    def published(self, name: str) -> tuple[str, str | None] | None:
        """The file and definition key an element's exact mapping names, the key None
        for a file's root, or None when CALM has no counterpart."""
        element = self.sv.get_element(name)
        for curie in element.exact_mappings or []:
            uri = self.sv.expand_curie(curie)
            if uri.startswith(META_BASE):
                file, _, pointer = uri[len(META_BASE) :].partition("#")
                if file != module_file(self.module_of[name]):
                    raise ValueError(
                        f"{name} maps to {file} but sits in another module"
                    )
                return file, pointer.rsplit("/", 1)[-1] if pointer else None
        return None

    # ---- repairs of the generator's output ----------------------------------

    def _aliases(self, cls: str) -> dict[str, str]:
        """Each slot's key in CALM's files: its alias, or else the one key it lists
        under aliases, which keeps the key out of every other generated form."""
        out = {}
        for s in self.sv.class_induced_slots(cls):
            if s.alias:
                out[s.name] = s.alias
            elif s.aliases:
                if len(s.aliases) != 1:
                    raise ValueError(f"{cls}.{s.name} lists {len(s.aliases)} aliases")
                out[s.name] = s.aliases[0]
        return out

    def repair_class(self, cls: str, schema: dict) -> None:
        aliases = self._aliases(cls)

        def rename(node):
            if isinstance(node, dict):
                if "properties" in node:
                    node["properties"] = {
                        aliases.get(k, k): v for k, v in node["properties"].items()
                    }
                if "required" in node:
                    node["required"] = [aliases.get(k, k) for k in node["required"]]
                for key in CONDITIONALS:
                    if key in node:
                        rename(node[key])
            elif isinstance(node, list):
                for item in node:
                    rename(item)

        rename(schema)
        properties = schema.get("properties", {})
        order = [aliases.get(s.name, s.name) for s in self.sv.class_induced_slots(cls)]
        schema["properties"] = properties = {
            k: properties[k] for k in sorted(properties, key=order.index)
        }
        for slot in self.sv.class_induced_slots(cls):
            prop = properties.get(aliases.get(slot.name, slot.name))
            if prop is None:
                continue
            if slot.list_elements_unique:
                prop["uniqueItems"] = True
            if slot.ifabsent:
                match = re.fullmatch(r"string\((.*)\)", slot.ifabsent)
                if match:
                    prop["default"] = match.group(1)
        examples = (self.raw[self.module_of[cls]]["classes"][cls] or {}).get("examples")
        if examples:
            schema["examples"] = [example["object"] for example in examples]
        if schema.get("title") == cls:
            del schema["title"]

    @staticmethod
    def drop_null(tree) -> None:
        """Remove the null branch an optional enum or extra_slots range keeps."""

        def visit(node):
            branches = node.get("anyOf")
            if branches and {"type": "null"} in branches:
                kept = [b for b in branches if b != {"type": "null"}]
                del node["anyOf"]
                if len(kept) == 1:
                    for key, value in kept[0].items():
                        node.setdefault(key, value)
                else:
                    node["anyOf"] = kept

        _walk(tree, visit)

    # ---- rules for what LinkML cannot state ---------------------------------

    def open_enums(self, defs: dict) -> set[str]:
        """Enums a slot only ever offers beside a free string, published open."""
        enums = set(self.sv.all_enums())

        def opened_enum(node) -> str | None:
            branches = node.get("anyOf") or []
            refs = [b["$ref"].removeprefix("#/$defs/") for b in branches if "$ref" in b]
            if len(branches) == 2 and {"type": "string"} in branches and refs:
                return refs[0] if refs[0] in enums else None
            return None

        open_uses: set[str] = set()
        closed_uses: set[str] = set()

        def survey(node):
            enum = opened_enum(node)
            if enum:
                open_uses.add(enum)
            elif node.get("$ref", "").removeprefix("#/$defs/") in enums:
                closed_uses.add(node["$ref"].removeprefix("#/$defs/"))

        def survey_all(node):
            if isinstance(node, dict):
                survey(node)
                branches = node.get("anyOf") if opened_enum(node) else None
                for key, value in node.items():
                    if value is not branches:
                        survey_all(value)
            elif isinstance(node, list):
                for item in node:
                    survey_all(item)

        survey_all(defs)
        mixed = open_uses & closed_uses
        if mixed:
            raise ValueError(f"enums offered both open and closed: {sorted(mixed)}")

        def visit(node):
            enum = opened_enum(node)
            if enum:
                del node["anyOf"]
                node["$ref"] = f"#/$defs/{enum}"

        _walk(defs, visit)
        for enum in open_uses:
            schema = defs[enum]
            values = schema.pop("enum")
            schema.pop("type", None)
            schema["anyOf"] = [{"enum": values}, {"type": "string"}]
        return open_uses

    def type_defs(self) -> dict[str, dict]:
        """Each type with an exact mapping, as a definition."""
        out = {}
        for module, doc in self.raw.items():
            for name, spec in (doc.get("types") or {}).items():
                if self.published(name) is None:
                    continue
                typeof = self.sv.induced_type(name).base
                out[name] = {
                    "type": {"str": "string"}.get(typeof, typeof),
                    "title": spec.get("title"),
                    "description": spec.get("description"),
                    "pattern": spec.get("pattern"),
                    "examples": [e["value"] for e in spec.get("examples", [])],
                }
                out[name] = {k: v for k, v in out[name].items() if v}
        return out

    # ---- assembly -----------------------------------------------------------

    def build(self) -> dict[str, dict]:
        defs = copy.deepcopy(self.defs)
        for name, schema in defs.items():
            if name in self.sv.all_classes():
                if self.sv.get_class(name).class_uri == "linkml:Any":
                    defs[name] = {"description": schema["description"]}
                else:
                    self.repair_class(name, schema)
            elif schema.get("title") == name:
                del schema["title"]
        self.drop_null(defs)
        self.open_enums(defs)
        defs |= self.type_defs()

        places: dict[str, tuple[str, str | None]] = {}
        for name in defs:
            found = self.published(name)
            if found:
                places[name] = found
        for (cls, slot), (file, key) in NAMED_ARRAYS.items():
            prop = defs[cls]["properties"][slot]
            hoisted = {k: v for k, v in prop.items() if k != "description"}
            name = f"_array_{key}"
            defs[name] = hoisted
            places[name] = (file, key)
            defs[cls]["properties"][slot] = {
                "description": prop.get("description"),
                "$ref": f"#/$defs/{name}",
            }

        inline = set(defs) - set(places)

        def expand(node):
            if isinstance(node, dict):
                target = node.get("$ref", "").removeprefix("#/$defs/")
                if target in inline:
                    body = copy.deepcopy(defs[target])
                    body.pop("description", None) if "description" in node else None
                    node.pop("$ref")
                    for key, value in body.items():
                        node.setdefault(key, value)
                for value in list(node.values()):
                    expand(value)
            elif isinstance(node, list):
                for item in node:
                    expand(item)

        for _ in range(len(inline) + 1):
            expand(defs)

        declared = [
            name
            for doc in self.raw.values()
            for kind in ("classes", "enums", "types")
            for name in doc.get(kind) or {}
        ]
        declared += [name for name in places if name not in declared]

        files: dict[str, dict] = {}
        for name, (file, key) in sorted(
            places.items(), key=lambda item: declared.index(item[0])
        ):
            module = self.sv.schema_map[self.module_of.get(name, UMBRELLA)]
            doc = files.setdefault(
                file,
                {
                    "$schema": DRAFT,
                    "$id": META_BASE + file,
                    "title": module.title,
                    "description": " ".join(module.description.split()),
                },
            )
            if key is None:
                body = {k: v for k, v in defs[name].items() if k != "description"}
                doc.update(body)
            else:
                doc.setdefault("defs", {})[key] = defs[name]
        for file, doc in files.items():
            if file == "core.json":
                core = self.sv.schema_map["calm_core"]
                doc["title"] = core.title
                doc["description"] = " ".join(core.description.split())

        def rewrite(node, file):
            if isinstance(node, dict):
                ref = node.get("$ref", "")
                if ref.startswith("#/$defs/"):
                    target_file, key = places[ref.removeprefix("#/$defs/")]
                    pointer = "" if key is None else f"#/defs/{key}"
                    node["$ref"] = (
                        pointer if target_file == file else target_file + pointer
                    )
                for value in node.values():
                    rewrite(value, file)
            elif isinstance(node, list):
                for item in node:
                    rewrite(item, file)

        out = {}
        for file, doc in files.items():
            rewrite(doc, file)
            out[file] = _ordered(doc)
        return out


def render(doc: dict) -> str:
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def write(output: Path, check: bool) -> int:
    files = {name: render(doc) for name, doc in Shaper().build().items()}
    files |= {name: (UPSTREAM / name).read_text(encoding="utf-8") for name in COPIED}
    stale = []
    for name, text in sorted(files.items()):
        path = output / name
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current != text:
            stale.append(name)
            if not check:
                output.mkdir(parents=True, exist_ok=True)
                path.write_text(text, encoding="utf-8")
    extra = sorted(p.name for p in output.glob("*.json") if p.name not in files)
    if check:
        for name in stale + extra:
            print(
                f"{output.name}/{name} differs from what the model gives",
                file=sys.stderr,
            )
        return 1 if stale or extra else 0
    for name in extra:
        (output / name).unlink()
    print(f"Wrote {len(stale)} of {len(files)} files to {output}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument(
        "--check", action="store_true", help="Write nothing; exit 1 on drift"
    )
    args = parser.parse_args(argv)
    return write(args.output, args.check)


if __name__ == "__main__":
    sys.exit(main())
