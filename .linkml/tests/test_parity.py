"""Holds the JSON Schema files the model gives to the files CALM 1.3 publishes.

tests/calm_parity.py says what each tier compares. meta/ holds the generated files, and a
test holds it to what scripts/calm_meta.py writes now.
"""

import json
import re
import subprocess
import sys

import jsonschema
import pytest
import yaml

import calm_parity as parity

FILES = [
    "calm.json",
    "calm-timeline.json",
    "control.json",
    "control-requirement.json",
    "core.json",
    "decorators.json",
    "evidence.json",
    "flow.json",
    "interface.json",
    "timeline.json",
    "units.json",
]


def test_meta_is_what_the_model_gives():
    result = subprocess.run(
        [sys.executable, str(parity.ROOT / "scripts" / "calm_meta.py"), "--check"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr


def test_both_sets_hold_the_eleven_files():
    assert sorted(parity.published()) == sorted(FILES)
    assert sorted(parity.generated()) == sorted(FILES)
    on_disk = {
        p.name: json.loads(p.read_text()) for p in parity.GENERATED.glob("*.json")
    }
    assert on_disk == parity.generated()


# ---- tier 1: addresses ---------------------------------------------------------


@pytest.mark.parametrize("name", FILES)
def test_each_generated_file_is_draft_2020_12(name):
    doc = parity.generated()[name]
    assert doc["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert doc["$id"] == parity.META_BASE + name
    jsonschema.Draft202012Validator.check_schema(doc)


def test_every_generated_reference_resolves():
    files = parity.generated()
    unresolved = sorted(
        p for p in parity.contract(files) if not parity.resolves(files, p)
    )
    assert not unresolved


def test_every_published_address_exists():
    """Each $id, each definition and each pointer a published $ref names."""
    missing = sorted(
        p
        for p in parity.contract(parity.published())
        if not parity.resolves(parity.generated(), p)
    )
    assert not missing


def test_the_generated_set_adds_no_definition():
    published = parity.contract(parity.published())
    added = sorted(p for p in parity.contract(parity.generated()) if p not in published)
    assert not added


# ---- tier 2: verdicts ----------------------------------------------------------


def test_the_corpus_is_found():
    """FINOS's tree and upstream/ hold architectures, timelines, flows, control
    requirements and decorators."""
    targets = {target for _, target, _ in parity.corpus()}
    assert targets == {
        "core.json",
        "timeline.json",
        "flow.json#/defs/flow",
        "control-requirement.json",
        parity.DECORATOR,
    }
    assert len(parity.corpus()) >= 150


def test_every_corpus_document_gets_the_same_verdict():
    differing = [
        (where, target)
        for where, target, doc in parity.corpus()
        if parity.relation(target, doc) != "same"
    ]
    assert not differing


def test_every_mutant_gets_the_same_verdict():
    differing = []
    count = 0
    for where, target, doc in parity.corpus():
        for name, mutant in parity.mutants(doc):
            count += 1
            if parity.relation(target, mutant) != "same":
                differing.append((where, name))
    assert count >= 500
    assert not differing


def test_the_mutants_are_refused():
    """A mutation of a valid document is refused by CALM's files, so the verdicts
    above compare a refusal, not two acceptances."""
    accepted = set()
    for where, target, doc in parity.corpus():
        if not parity.verdict("published", target, doc):
            continue
        for name, mutant in parity.mutants(doc):
            if parity.verdict("published", target, mutant):
                accepted.add(name)
    assert not accepted


@pytest.mark.parametrize(
    "probe", parity.probes(), ids=lambda p: f"{p['pointer']} {json.dumps(p['value'])}"
)
def test_each_probe_gets_the_expected_verdicts(probe):
    assert parity.relation(probe["pointer"], probe["value"]) == probe["expect"]
    assert ("reason" in probe) == (probe["expect"] != "same")


# ---- tier 3: structure ---------------------------------------------------------


def _listed():
    data = yaml.safe_load((parity.PARITY / "structural.yaml").read_text())
    return data["differences"]


def test_only_the_listed_definitions_differ_in_shape():
    published = parity.definitions(parity.published())
    generated = parity.definitions(parity.generated())
    differing = {
        pointer.removeprefix(parity.META_BASE)
        for pointer, schema in published.items()
        if generated.get(pointer) != schema
    }
    assert differing == set(_listed())


def test_each_listed_difference_has_a_kind_and_a_reason():
    for pointer, entry in _listed().items():
        assert entry["kind"] in {"equivalent-form", "model-gap", "upstream-fault"}, (
            pointer
        )
        assert entry["reason"].strip(), pointer


def test_every_description_calm_gives_is_kept_word_for_word():
    for name, doc in parity.published().items():
        theirs = parity.descriptions(doc)
        ours = parity.descriptions(parity.generated()[name])
        changed = sorted(
            path for path, text in theirs.items() if ours.get(path) != text
        )
        assert not changed, name


def test_calm_refuses_its_own_cron_examples():
    """A fault of CALM 1.3, recorded so a fixed release shows: the pattern allows
    no asterisk, and each example has one."""
    cron = parity.published()["units.json"]["defs"]["cron-expression"]
    assert cron["examples"]
    assert not any(re.search(cron["pattern"], e) for e in cron["examples"])
