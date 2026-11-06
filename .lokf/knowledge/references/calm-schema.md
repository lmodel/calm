---
type: Reference
id: https://w3id.org/lmodel/calm/knowledge/references/calm-schema
genre: reference
title: CALM Meta Schema (finos/calm-schema)
description: FINOS's calm-schema repository, which publishes CALM's eleven JSON Schema files by release; release 1.3 is the edition this schema renders, served at CALM's release addresses.
resource: .linkml/upstream/calm-schema/v1.3
sources:
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: What it models
  - id: upstream_pins.tsv
    resource: .linkml/scripts/upstream_pins.tsv
  - id: about.md
    resource: .linkml/docs/about.md
    title: Where it comes from
sameAs:
  - https://github.com/finos/calm-schema
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:13:55Z"
  revision: 3f1ca0dfb5c90cacc7ec5dc39d3f039fcd690cb6
status: draft
---

# CALM Meta Schema (finos/calm-schema)

FINOS publishes CALM's schema in finos/calm-schema, and serves each release at the address in its files' `$id`.[^linkml-readme.md] This project pins the tag v1.3, commit `47e2a41a0e1e5e9fe639b30ce2adae8c4abc5b6d`. It holds that release's files unchanged under `.linkml/upstream/calm-schema/v1.3/`.[^upstream_pins.tsv] FINOS moved the schema there from architecture-as-code in October 2026.[^about.md]

[^linkml-readme.md]: .linkml/README.md, What it models
[^upstream_pins.tsv]: .linkml/scripts/upstream_pins.tsv
[^about.md]: .linkml/docs/about.md, Where it comes from
