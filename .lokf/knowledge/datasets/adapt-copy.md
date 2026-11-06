---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy (.lokf/calm.yaml)
description: "`.lokf/calm.yaml`, the copy `lokf adapt` writes from the schema so that this bundle and a host's can type concepts with `CalmNode`, `CalmRelationship`, `CalmFlow` and `CalmControlRequirement`."
resource: .lokf/calm.yaml
derivedFrom:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: project.justfile
    resource: .linkml/project.justfile
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: Knowledge Trust Ladder (KTL)
  - resource: .lokf/calm.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: fc39abe0456914e91fdf07617dbe0bcb2a336d0f
status: draft
---

# The schema's adapt copy (.lokf/calm.yaml)

`just lokf-adapt` writes the copy, and `just lokf-adapt-check` fails when it is stale.[^project.justfile] The copy roots four classes on LOKF's `Concept` and folds `name` and `description` into LOKF's `title` and `description`.[^linkml-readme.md] A release attaches it as `schema-<tag>-calm.yaml`.[^linkml-readme.md]

[^project.justfile]: .linkml/project.justfile
[^linkml-readme.md]: .linkml/README.md, Knowledge Trust Ladder (KTL)
