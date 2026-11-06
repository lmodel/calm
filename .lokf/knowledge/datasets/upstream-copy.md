---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/upstream-copy
genre: reference
title: Pinned copy of calm-schema v1.3
description: calm-schema's files at the tag v1.3, unchanged under `.linkml/upstream/calm-schema/v1.3/`, each pinned by its git object hash in `scripts/upstream_pins.tsv`.
resource: .linkml/upstream/calm-schema/v1.3
isPartOf:
  - https://w3id.org/lmodel/calm/knowledge/references/calm-schema
sources:
  - id: upstream_pins.tsv
    resource: .linkml/scripts/upstream_pins.tsv
  - id: test_upstream.py
    resource: .linkml/tests/test_upstream.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: 3f1ca0dfb5c90cacc7ec5dc39d3f039fcd690cb6
status: draft
---

# Pinned copy of calm-schema v1.3

The copy holds the eleven schema files, the release's licence, notice and changelog, and the deployment decorator standard with its examples.[^upstream_pins.tsv] `tests/test_upstream.py` holds every file to its hash.[^test_upstream.py]

[^upstream_pins.tsv]: .linkml/scripts/upstream_pins.tsv
[^test_upstream.py]: .linkml/tests/test_upstream.py, the docstring
