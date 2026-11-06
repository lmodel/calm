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
  at: "2026-11-06T08:08:58Z"
  revision: fa096d644ebd722b932d0ca644b337a63d35f759
status: draft
---

# Neighbour copies

Each neighbour is the schema asset of a release, checked against its `.sha256` and its build-provenance attestation, and pinned by checksum in `NEIGHBOURS`.[^test_schema_rules.py] A key the copy shares with a neighbour is listed, so a new one fails the test.[^test_schema_rules.py]

[^test_schema_rules.py]: .linkml/tests/test_schema_rules.py, NEIGHBOURS
