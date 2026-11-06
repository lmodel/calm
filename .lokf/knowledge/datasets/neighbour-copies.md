---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbour copies
description: The released adapt copies of 33 other lmodel schemas in `.linkml/tests/neighbours/`, each pinned by checksum, that `tests/test_schema_rules.py` checks this copy's names against.
resource: .linkml/tests/neighbours
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: .linkml/tests/test_schema_rules.py
    title: NEIGHBOURS
  - resource: .linkml/tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
status: draft
---

# Neighbour copies

Each neighbour is the schema asset of a release, checked against its `.sha256` and its build-provenance attestation, and pinned by checksum in `NEIGHBOURS`.[^test_schema_rules.py] The test lists each key the copy shares with a neighbour, so a new shared key fails it.[^test_schema_rules.py]

[^test_schema_rules.py]: .linkml/tests/test_schema_rules.py, NEIGHBOURS
