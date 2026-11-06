---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What the LinkML generators write from the schema: `.linkml/project/` (JSON Schema, OWL, SHACL, ShEx, Java, TypeScript and more), the Python datamodel and `docs/schema/calm.yaml`. None is edited by hand."
resource: .linkml/project
derivedFrom:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: What this project is
  - id: docs-index.md
    resource: .linkml/docs/index.md
    title: Validating a CALM document
  - resource: .linkml/project
  - resource: .linkml/src/calm/datamodel
  - resource: .linkml/docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: e3049d37e117aca6a92dff91576f333fdcfa802d
status: draft
---

# Generated artefacts

`just gen-project` writes `project/` and the datamodel, and `just gen-doc` the schema pages and the merged schema under `docs/schema/`.[^contributing.md] The JSON Schema in `project/` keeps slot names; CALM's form is in `meta/`.[^docs-index.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, What this project is
[^docs-index.md]: .linkml/docs/index.md, Validating a CALM document
