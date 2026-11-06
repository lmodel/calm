# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Added

- **A schema of CALM 1.3**, one module per file of calm-schema's v1.3 release, with `Calm` classes that keep CALM's keys as aliases and CALM's descriptions word for word.
- **CALM's JSON Schema files, generated from the schema**, in `meta/` at CALM's addresses, which `scripts/calm_meta.py` writes.
- **A JSON-LD context with CALM's keys**, `meta/calm.context.jsonld`, so a CALM document expands to RDF under the schema's IRIs without renaming.
- **Parity tests** that hold `meta/` to CALM's own files: every address CALM's files name, the same verdict on each CALM document in FINOS's tree and calm-schema's release and on their mutations, and each remaining difference listed with its reason in `parity/`.
- **A weekly watch** of calm-schema's tags and FINOS's main, against calm-schema's v1.3 files under `upstream/` and a list of every file of FINOS's merged commit.
- **`.lokf/schema/calm.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-calm.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the adapt copy, as KTL's main branch lays them out. The knowledge release workflow and the sidecar preflight carry KTL #325's change to read that folder until a KTL release does, and the next sync replaces them.
- **The schema project moved from `linkml/` to `.linkml/`**, the sidecar layout, and `linkml_schema` at the root links to the schema's folder.
- **The schema follows calm-schema's v1.3 release.** The converter read CALM 1.2 from the monorepo's `calm/release/`, which FINOS has since moved to calm-schema.
- **Pin linkml and linkml-runtime at 1.12.1.** PyPI publishing and the docs preview stay off.

### Removed

- **The converter, its overlay, the patched generators and the twelve SSSOM sets.** Every SSSOM row was marked `semapv:LLMBasedMatching`, and none stated a mapping CALM makes. `git show 7d5c4f33` holds what went.

## [0.0.0] - 2026-11-06

### Added

- **The baseline**: this fork's merge of FINOS's tree, which the `v0.0.0` tag marks.
