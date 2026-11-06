---
type: Reference
id: https://w3id.org/lmodel/calm/knowledge/references/finos-architecture-as-code
genre: reference
title: FINOS Architecture as Code (finos/architecture-as-code)
description: FINOS's monorepo of CALM's tools (the CLI, CALM Hub, the widgets, the docs site), of which this repository is a fork, kept unchanged at the repository's root.
resource: README.md
sources:
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: What it models
  - id: finos-readme.md
    resource: README.md
  - id: upstream_tree.tsv
    resource: .linkml/tests/upstream_tree.tsv
sameAs:
  - https://github.com/finos/architecture-as-code
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: 0fc4649a3d68bc6418150b66f67430843c858fd1
status: draft
---

# FINOS Architecture as Code (finos/architecture-as-code)

This repository is a fork of finos/architecture-as-code, and FINOS's tree sits unchanged at its root.[^linkml-readme.md] FINOS's README says the tools take the schema from the npm package of calm-schema.[^finos-readme.md] `.linkml/tests/upstream_tree.tsv` lists every file of the merged commit with its hash.[^upstream_tree.tsv]

[^linkml-readme.md]: .linkml/README.md, What it models
[^finos-readme.md]: README.md
[^upstream_tree.tsv]: .linkml/tests/upstream_tree.tsv
