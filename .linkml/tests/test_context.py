"""Holds meta/calm.context.jsonld, the JSON-LD context with CALM's keys, to CALM's
files and to the schema.

The context the generators write keys an aliased slot by its alias with the hyphen
made an underscore, so a CALM document's `unique-id` does not expand through it.
scripts/calm_meta.py writes this one from the slots' keys in CALM's files, and
test_parity.py's check of `meta/` covers its text. These tests hold its meaning:
every key CALM's files name is a term, each term is its slot's IRI, and an example
architecture expands to RDF under those IRIs.
"""

import json
from functools import lru_cache

import rdflib
import yaml
from linkml_runtime.utils.schemaview import SchemaView
from rdflib.namespace import RDF, XSD

import calm_parity as parity

CONTEXT = parity.GENERATED / "calm.context.jsonld"
CALM = rdflib.Namespace("https://w3id.org/lmodel/calm/")
SCHEMA = rdflib.Namespace("http://schema.org/")
EXAMPLE = (
    parity.ROOT
    / "tests"
    / "data"
    / "problem"
    / "valid"
    / "CalmArchitecture-order-system.yaml"
)

# Keys of CALM's files that are not CALM data: JSON Schema's own keyword on a
# document, and the keyword core.json misplaces inside properties.
NOT_DATA = {"$schema", "additionalProperties"}


@lru_cache(maxsize=1)
def context() -> dict:
    return json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"]


def terms() -> dict[str, dict]:
    return {k: v for k, v in context().items() if isinstance(v, dict)}


def _keys(node, found: set[str]) -> None:
    """Every property key a published file names, at any depth."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "properties" and isinstance(value, dict):
                found.update(value)
            _keys(value, found)
    elif isinstance(node, list):
        for item in node:
            _keys(item, found)


def test_every_key_of_calms_files_is_a_term():
    keys: set[str] = set()
    for doc in parity.published().values():
        _keys(doc, keys)
    assert keys - NOT_DATA <= set(terms())


def test_each_term_is_its_slots_iri_and_nothing_else_is_a_term():
    sv = SchemaView(str(parity.ROOT / "src" / "calm" / "schema" / "calm.yaml"))
    expected = {}
    for cls in sv.all_classes():
        for slot in sv.class_induced_slots(cls):
            key = slot.alias or (slot.aliases[0] if slot.aliases else slot.name)
            if key != "$schema":
                expected[key] = sv.get_uri(slot, expand=False)
    assert {k: v["@id"] for k, v in terms().items()} == expected


def test_prefixes_are_the_schemas():
    prefixes = {k: v for k, v in context().items() if isinstance(v, str)}
    assert prefixes == {
        "calm": "https://w3id.org/lmodel/calm/",
        "schema": "http://schema.org/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
    }
    assert context()["@version"] == 1.1


def test_an_architecture_expands_to_rdf_under_the_schemas_iris():
    doc = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    graph = rdflib.Graph().parse(
        data=json.dumps({"@context": context(), **doc}), format="json-ld"
    )
    ids = {str(o) for o in graph.objects(None, CALM.unique_id)}
    assert {n["unique-id"] for n in doc["nodes"]} <= ids
    assert (None, SCHEMA.name, rdflib.Literal("Order Service")) in graph
    assert (None, CALM.source_end, None) in graph
    # Typed values carry their datatype, and free-form values stay one JSON literal.
    sequence = next(graph.objects(None, CALM.sequence_number))
    assert sequence.datatype == XSD.integer
    metadata = next(graph.objects(None, CALM.metadata))
    assert metadata.datatype == RDF.JSON
    # A controls map is an index map: each control is a node under calm:controls.
    control = next(graph.objects(None, CALM.controls))
    assert (control, CALM.requirements, None) in graph
