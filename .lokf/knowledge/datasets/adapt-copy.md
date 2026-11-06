---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/schema/calm.yaml`, the copy `lokf adapt` writes from the schema so that this bundle and a host's can type concepts with `CalmNode`, `CalmRelationship`, `CalmFlow` and `CalmControlRequirement`."
resource: .lokf/schema/calm.yaml
derivedFrom:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: project.justfile
    resource: .linkml/project.justfile
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: Knowledge Trust Ladder (KTL)
  - resource: .lokf/schema/calm.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T16:04:28Z"
  revision: 002eb3d51bc2faf8f9ffab1dfe82bf3a7b50841c
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes the copy, and `just lokf-adapt-check` fails when it is stale.[^project.justfile] The copy roots four classes on LOKF's `Concept` and folds `name` and `description` into LOKF's `title` and `description`.[^linkml-readme.md] A release attaches it as `schema-<tag>-calm.yaml`.[^linkml-readme.md]

[^project.justfile]: .linkml/project.justfile
[^linkml-readme.md]: .linkml/README.md, Knowledge Trust Ladder (KTL)
