"""Unit checks of scripts/calm_meta.py's helpers, apart from the files it writes.

tests/test_parity.py holds the files themselves to CALM's. These hold the small
functions the build routes names and types through, on inputs the schema does not
have today, so a change to the schema cannot pass them by.
"""

import importlib.util

import pytest

import calm_parity as parity


def _build():
    spec = importlib.util.spec_from_file_location(
        "calm_meta_for_units", parity.ROOT / "scripts" / "calm_meta.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BUILD = _build()


@pytest.mark.parametrize(
    ("name", "key"),
    [
        ("CalmNodeInterface", "node-interface"),
        ("CalmControlRequirement", "control-requirement"),
        ("CalmNode", "node"),
        ("Decision", "decision"),
    ],
)
def test_kebab_gives_calms_definition_key(name, key):
    assert BUILD.kebab(name) == key


@pytest.mark.parametrize(
    ("module", "file"),
    [
        ("calm", "core.json"),
        ("calm_core", "core.json"),
        ("calm_control_requirement", "control-requirement.json"),
        ("calm_units", "units.json"),
    ],
)
def test_module_file_names_the_file_a_module_renders(module, file):
    assert BUILD.module_file(module) == file


@pytest.mark.parametrize(
    ("base", "expected"),
    [
        # The one base the schema has today, and the bases a later type could take.
        ("str", {"type": "string"}),
        ("int", {"type": "integer"}),
        ("Decimal", {"type": "number"}),
        ("float", {"type": "number"}),
        ("Bool", {"type": "boolean"}),
        ("XSDDate", {"type": "string", "format": "date"}),
        ("XSDDateTime", {"type": "string", "format": "date-time"}),
        ("URI", {"type": "string", "format": "uri"}),
        # A base the generator's table lacks is a string, as the generator writes it.
        ("NCName", {"type": "string"}),
        (None, {"type": "string"}),
    ],
)
def test_json_type_is_the_generators_type_for_a_base(base, expected):
    """A type based on int once came out as `"type": "int"`, which is no JSON Schema
    type; the build now reads the generator's own table."""
    assert BUILD.json_type(base) == expected
