"""Compares the JSON Schema files the model gives with the files CALM publishes.

tests/test_parity.py runs three tiers over these helpers:

1. Addresses. Every file compiles, every reference resolves, and every $id, every
   definition and every pointer a published $ref names exists in the generated set.
2. Verdicts. Each CALM document in FINOS's tree and in upstream/, each of its
   mutations, and each probe in parity/probes.yaml gets the same verdict from both
   sets, or the difference parity/probes.yaml expects.
3. Structure. The definitions that differ in shape once both sides are normalised
   are the ones parity/structural.yaml lists, each with its reason.
"""

from __future__ import annotations

import copy
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

import jsonschema
import referencing
import yaml
from jsonschema_specifications import REGISTRY as SPECIFICATIONS
from referencing.jsonschema import DRAFT202012

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT.parent
PUBLISHED = ROOT / "upstream" / "calm-schema" / "v1.3" / "schema"
GENERATED = ROOT / "meta"
PARITY = ROOT / "parity"
META_BASE = "https://calm.finos.org/release/1.3/meta/"
RELEASE_PREFIX = "https://calm.finos.org/release/"

# Where a document's $schema sends it: the file it names, and the pointer in that
# file a document of its kind validates against.
TARGETS = {
    "calm.json": "core.json",
    "core.json": "core.json",
    "calm-timeline.json": "timeline.json",
    "timeline.json": "timeline.json",
    "flow.json": "flow.json#/defs/flow",
    "control-requirement.json": "control-requirement.json",
    "evidence.json": "evidence.json",
}
DECORATOR = "decorators.json#/defs/decorator"
SKIPPED_DIRS = {
    "node_modules",
    ".git",
    ".linkml",
    "dist",
    "build",
    ".venv",
    ".lokf",
    "website",
}


def load_files(folder: Path) -> dict[str, dict]:
    return {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(folder.glob("*.json"))
        if path.name != "package.json"
    }


@lru_cache(maxsize=1)
def published() -> dict[str, dict]:
    return load_files(PUBLISHED)


@lru_cache(maxsize=1)
def generated() -> dict[str, dict]:
    """The generated set, built fresh from the model rather than read from meta/."""
    spec = importlib.util.spec_from_file_location(
        "calm_meta_for_parity", ROOT / "scripts" / "calm_meta.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    files = module.Shaper().build()
    for name in module.COPIED:
        files[name] = json.loads((module.UPSTREAM / name).read_text(encoding="utf-8"))
    return files


def registry(files: dict[str, dict]) -> referencing.Registry:
    resources = [
        (doc["$id"], DRAFT202012.create_resource(doc)) for doc in files.values()
    ]
    return SPECIFICATIONS.with_resources(resources)


@lru_cache(maxsize=2)
def _registry(which: str) -> referencing.Registry:
    return registry(published() if which == "published" else generated())


def validator(which: str, target: str) -> jsonschema.Draft202012Validator:
    """A validator for one pointer of one set, such as core.json#/defs/node."""
    return jsonschema.Draft202012Validator(
        {"$ref": META_BASE + target}, registry=_registry(which)
    )


def verdict(which: str, target: str, instance) -> bool:
    return validator(which, target).is_valid(instance)


# ---- tier 1 ------------------------------------------------------------------


def _refs(node, base: str):
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str):
            yield (
                ref
                if "://" in ref
                else (base + ref if ref.startswith("#") else META_BASE + ref)
            )
        for value in node.values():
            yield from _refs(value, base)
    elif isinstance(node, list):
        for item in node:
            yield from _refs(item, base)


def contract(files: dict[str, dict]) -> set[str]:
    """Every $id, every top-level definition and every pointer a $ref names."""
    pointers = set()
    for doc in files.values():
        pointers.add(doc["$id"])
        for key in doc.get("defs", {}):
            pointers.add(f"{doc['$id']}#/defs/{key}")
        for ref in _refs(doc, doc["$id"]):
            if ref.startswith(META_BASE):
                pointers.add(ref)
    return pointers


def resolves(files: dict[str, dict], pointer: str) -> bool:
    try:
        registry(files).resolver().lookup(pointer)
    except referencing.exceptions.Unresolvable:
        return False
    return True


# ---- tier 2 ------------------------------------------------------------------


def _target_of(obj: dict) -> str | None:
    schema = obj.get("$schema")
    if not isinstance(schema, str) or not schema.startswith("https://calm.finos.org/"):
        return None
    if schema.endswith(".decorator.standard.json"):
        return DECORATOR
    if schema.startswith(RELEASE_PREFIX):
        return TARGETS.get(schema.rsplit("/", 1)[-1])
    if schema.endswith(".pattern.json"):
        return "core.json"
    return None


def _documents_in(node, found: list):
    if isinstance(node, dict):
        target = _target_of(node)
        if target:
            found.append((target, node))
            return
        for value in node.values():
            _documents_in(value, found)
    elif isinstance(node, list):
        for item in node:
            _documents_in(item, found)


@lru_cache(maxsize=1)
def corpus() -> list[tuple[str, str, object]]:
    """Each CALM document in FINOS's tree and upstream/: where it is, its target and
    the document, found by its $schema at any depth of a JSON file."""
    paths = []
    for path in sorted(TREE.rglob("*.json")):
        parts = set(path.relative_to(TREE).parts[:-1])
        if parts & SKIPPED_DIRS:
            continue
        paths.append(path)
    paths += sorted((ROOT / "upstream").rglob("*.json"))
    out = []
    for path in paths:
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        found: list = []
        _documents_in(doc, found)
        where = str(path.relative_to(TREE))
        out += [(f"{where}#{i}", target, d) for i, (target, d) in enumerate(found)]
    return out


def _items(node, key):
    value = node.get(key) if isinstance(node, dict) else None
    return (
        [item for item in value if isinstance(item, dict)]
        if isinstance(value, list)
        else []
    )


def _nodes(doc):
    return _items(doc, "nodes") + _items(doc, "moments")


def _relationships(doc):
    return [
        r
        for r in _items(doc, "relationships")
        if isinstance(r.get("relationship-type"), dict)
    ]


def _flows(doc):
    return _items(doc, "flows") + (
        [doc] if isinstance(doc.get("transitions"), list) else []
    )


def _control_details(doc):
    holders = [doc] + _nodes(doc) + _relationships(doc) + _flows(doc)
    details = []
    for holder in holders:
        controls = holder.get("controls")
        if isinstance(controls, dict):
            for control in controls.values():
                details += _items(control, "requirements")
    return details


# Each mutation: a name, where it applies, and the change. Applied to the first such
# object that the schemas themselves check, so each mutant differs from its source in
# one place. An object found elsewhere, such as a node inside a pattern's prefixItems,
# is left alone: no schema checks it, so a mutation there tests nothing.
MUTATIONS = (
    ("node without unique-id", _nodes, lambda o: o.pop("unique-id", None)),
    ("node name not a string", _nodes, lambda o: o.update(name=5)),
    ("node details with an extra key", _nodes, lambda o: o.update(details={"x": 1})),
    ("node node-type not a string", _nodes, lambda o: o.update({"node-type": 5})),
    (
        "relationship without its type",
        _relationships,
        lambda o: o.pop("relationship-type"),
    ),
    (
        "relationship with a misspelt protocol",
        _relationships,
        lambda o: o.update(protocol="HTTPX"),
    ),
    (
        "relationship of two kinds",
        _relationships,
        lambda o: o["relationship-type"].update(
            interacts={"actor": "a", "nodes": ["b"]},
            connects={"source": {"node": "a"}, "destination": {"node": "b"}},
        ),
    ),
    ("flow with an extra key", _flows, lambda o: o.update(x=1)),
    ("flow with no transitions", _flows, lambda o: o.update(transitions=[])),
    (
        "control detail with both configurations",
        _control_details,
        lambda o: o.update({"config-url": "u", "config": {}}),
    ),
    (
        "control detail with neither configuration",
        _control_details,
        lambda o: (o.pop("config-url", None), o.pop("config", None)),
    ),
)


def mutants(document) -> list[tuple[str, object]]:
    out = []
    if not isinstance(document, dict):
        return out
    for name, find, change in MUTATIONS:
        mutant = copy.deepcopy(document)
        found = find(mutant)
        if found:
            change(found[0])
            out.append((name, mutant))
    return out


@lru_cache(maxsize=1)
def probes() -> list[dict]:
    return yaml.safe_load((PARITY / "probes.yaml").read_text(encoding="utf-8"))[
        "probes"
    ]


def relation(target: str, instance) -> str:
    """same, wider (generated accepts, published refuses) or narrower."""
    ours = verdict("generated", target, instance)
    theirs = verdict("published", target, instance)
    if ours == theirs:
        return "same"
    return "wider" if ours else "narrower"


# ---- tier 3 ------------------------------------------------------------------

ANNOTATIONS = {"description", "title", "examples", "$comment", "default"}


def normalise(node, base: str):
    """A schema stripped of what does not change a verdict, in one form for both sides."""
    if isinstance(node, list):
        return [normalise(item, base) for item in node]
    if not isinstance(node, dict):
        return node
    out = {}
    for key, value in node.items():
        if key in ANNOTATIONS:
            continue
        if key == "additionalProperties" and value is True:
            continue
        if key == "$ref":
            out[key] = (
                value
                if "://" in value
                else (base + value if value.startswith("#") else META_BASE + value)
            )
            continue
        if key == "required":
            out[key] = sorted(value)
            continue
        if key == "patternProperties" and len(value) == 1:
            out["additionalProperties"] = normalise(next(iter(value.values())), base)
            continue
        if key == "properties":
            props = {}
            for name, schema in value.items():
                if schema is False:
                    out.setdefault("not_required", []).append(name)
                else:
                    props[name] = normalise(schema, base)
            if props:
                out[key] = props
            continue
        if key == "not" and set(value) == {"required"}:
            out.setdefault("not_required", []).extend(value["required"])
            continue
        if key in ("oneOf", "anyOf", "allOf"):
            out[key] = [_branch(normalise(b, base)) for b in value]
            continue
        out[key] = normalise(value, base)
    if "enum" in out and out.get("type") == "string":
        del out["type"]
    if "not_required" in out:
        out["not_required"] = sorted(set(out["not_required"]))
    if out.get("properties") == {}:
        del out["properties"]
    return out


def _branch(node):
    """A branch's properties that only repeat a key it requires say nothing."""
    props = node.get("properties")
    if props and all(v in ({}, {"type": "array", "items": {}}) for v in props.values()):
        del node["properties"]
    return node


def definitions(files: dict[str, dict]) -> dict[str, dict]:
    """Each file's root, without its defs, and each definition, by pointer."""
    out = {}
    for doc in files.values():
        base = doc["$id"]
        root = {k: v for k, v in doc.items() if k not in ("defs", "$schema", "$id")}
        out[base] = normalise(root, base)
        for key, schema in doc.get("defs", {}).items():
            out[f"{base}#/defs/{key}"] = normalise(schema, base)
    return out


def descriptions(node, path="") -> dict[str, str]:
    """Every description, by its path, with a patternProperties map read as
    additionalProperties, as the model writes it."""
    out = {}
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "description" and isinstance(value, str):
                out[path] = value
            elif (
                key == "patternProperties"
                and isinstance(value, dict)
                and len(value) == 1
            ):
                out |= descriptions(
                    next(iter(value.values())), f"{path}/additionalProperties"
                )
            else:
                out |= descriptions(value, f"{path}/{key}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            out |= descriptions(item, f"{path}/{i}")
    return out
