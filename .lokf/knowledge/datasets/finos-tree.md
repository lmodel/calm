---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/finos-tree
genre: reference
title: FINOS's tree
description: Every file of FINOS's architecture-as-code at the merged commit, kept unchanged beside `.linkml/`, which `tests/upstream_tree.tsv` lists by hash and the parity tests read for CALM documents.
resource: .linkml/tests/upstream_tree.tsv
isPartOf:
  - https://w3id.org/lmodel/calm/knowledge/references/finos-architecture-as-code
sources:
  - id: test_upstream.py
    resource: .linkml/tests/test_upstream.py
    title: the docstring
  - id: project.justfile
    resource: .linkml/project.justfile
  - id: calm_parity.py
    resource: .linkml/tests/calm_parity.py
    title: corpus
  - resource: .linkml/tests/upstream_tree.tsv
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
status: draft
---

# FINOS's tree

`tests/upstream_tree.tsv` lists each file of FINOS's merged commit with its git object hash, and `tests/test_upstream.py` fails on any change.[^test_upstream.py] `just pin-finos-tree <commit>` rewrites the list after a merge.[^project.justfile] The parity tests find each CALM document in the tree by its `$schema`.[^calm_parity.py]

[^test_upstream.py]: .linkml/tests/test_upstream.py, the docstring
[^project.justfile]: .linkml/project.justfile
[^calm_parity.py]: .linkml/tests/calm_parity.py, corpus
