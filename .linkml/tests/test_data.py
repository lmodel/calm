"""Checks each example against CALM's form of the schema.

An example is a CALM document or part of one, with CALM's keys, such as unique-id.
linkml-validate and the example runner read keys by slot name (unique_id), so they
cannot read one; the examples sit under tests/data/problem/, where the runner does
not look, and this test validates them against the files scripts/calm_meta.py gives,
and against CALM's own, by the definition the class's exact mapping names.
`tests/data/problem/valid/<Class>-<anything>.yaml` must pass both, and
`tests/data/problem/invalid/<Class>-<anything>.yaml` must fail both.
"""

import importlib.util
from functools import lru_cache
from pathlib import Path

import pytest
import yaml

import calm_parity as parity

DATA = Path(__file__).parent / "data" / "problem"
VALID = sorted((DATA / "valid").glob("*.yaml"))
INVALID = sorted((DATA / "invalid").glob("*.yaml"))


@lru_cache(maxsize=1)
def _shaper():
    spec = importlib.util.spec_from_file_location(
        "calm_meta_for_data", parity.ROOT / "scripts" / "calm_meta.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Shaper()


def _target(path: Path) -> str:
    cls = path.stem.split("-")[0]
    file, key = _shaper().published(cls)
    return file if key is None else f"{file}#/defs/{key}"


def _load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_example(path):
    target, data = _target(path), _load(path)
    assert parity.verdict("generated", target, data)
    assert parity.verdict("published", target, data)


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_example(path):
    target, data = _target(path), _load(path)
    assert not parity.verdict("generated", target, data)
    assert not parity.verdict("published", target, data)


def test_every_published_class_has_an_example():
    named = {p.stem.split("-")[0] for p in VALID}
    published = {
        name
        for name in _shaper().sv.all_classes()
        if _shaper().published(name) is not None
    }
    assert published <= named


def test_examples_the_schema_gives_validate():
    """The examples a class or type states, which the build copies into CALM's files."""
    shaper = _shaper()
    for name in shaper.sv.all_classes():
        for example in shaper.sv.get_class(name).examples or []:
            file, key = shaper.published(name)
            target = file if key is None else f"{file}#/defs/{key}"
            assert parity.verdict("generated", target, dict(example.object._items())), (
                name
            )
