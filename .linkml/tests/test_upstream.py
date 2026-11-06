"""Holds FINOS's tree, the pinned copy of CALM 1.3 and the schema headers to the pins.

FINOS's architecture-as-code tree sits beside .linkml/, unchanged, and upstream/ holds
calm-schema's v1.3 files. These tests show that both match their pins byte for byte,
and that the schema, the build and the watch name one edition.
"""

import hashlib
import importlib.util
from functools import lru_cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
TREE = ROOT.parent
SCHEMA_DIR = ROOT / "src" / "calm" / "schema"
UPSTREAM = ROOT / "upstream"
MANIFEST = Path(__file__).parent / "upstream_tree.tsv"


def _module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _watch():
    return _module("watch_pins", ROOT / "scripts" / "check_upstream_release.py")


def _blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _header(module):
    return yaml.safe_load((SCHEMA_DIR / f"{module}.yaml").read_text(encoding="utf-8"))


def test_finos_tree_is_the_merged_commit():
    """Every file FINOS's merged commit holds is here, byte for byte."""
    differing = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        sha, path = line.split("\t", 1)
        local = TREE / path
        if not local.is_file() or _blob_sha(local) != sha:
            differing.append(path)
    assert not differing


def test_upstream_holds_the_pinned_files_alone():
    pins = {pin["local"]: pin["sha"] for pin in _watch().pins()}
    found = {
        str(path.relative_to(UPSTREAM)): _blob_sha(path)
        for path in UPSTREAM.rglob("*")
        if path.is_file()
    }
    assert found == pins


def test_the_pins_agree():
    """The schema headers, the build and the watch name one edition and one commit."""
    edition = _watch().EDITION
    umbrella = _header("calm")
    assert umbrella["version"] == edition["version"]
    assert umbrella["annotations"]["upstream_tag"] == edition["tag"]
    assert umbrella["annotations"]["upstream_commit"] == edition["commit"]
    assert umbrella["annotations"]["upstream_license"] == "Apache-2.0"
    assert edition["commit"] in umbrella["source"]
    for path in SCHEMA_DIR.glob("calm_*.yaml"):
        header = _header(path.stem)
        assert header["version"] == edition["version"], path.name
        assert edition["commit"] in header["source"], path.name
        assert header["prefixes"]["calm_meta"] == (
            f"https://calm.finos.org/release/{edition['version']}/meta/"
        ), path.name
    build = _module("calm_meta_pins", ROOT / "scripts" / "calm_meta.py")
    assert build.META_BASE == umbrella["prefixes"]["calm_meta"]
    assert (
        build.UPSTREAM == UPSTREAM / "calm-schema" / f"v{edition['version']}" / "schema"
    )


def test_each_module_renders_a_published_file():
    """Module calm_<name> renders <name>.json, whose title it carries."""
    published = UPSTREAM / "calm-schema" / f"v{_watch().EDITION['version']}" / "schema"
    for path in SCHEMA_DIR.glob("calm_*.yaml"):
        stem = path.stem.removeprefix("calm_").replace("_", "-")
        doc = yaml.safe_load((published / f"{stem}.json").read_text(encoding="utf-8"))
        assert _header(path.stem)["title"] == doc["title"], path.name
