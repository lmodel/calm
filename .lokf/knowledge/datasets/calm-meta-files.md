---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/calm-meta-files
genre: reference
title: CALM's JSON Schema files, generated
description: The eleven files in `.linkml/meta/`, at CALM's own addresses, which `scripts/calm_meta.py` writes from the LinkML schema and the parity tests hold to CALM's own files.
resource: .linkml/meta
derivedFrom:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: calm_meta.py
    resource: .linkml/scripts/calm_meta.py
    title: the docstring
  - id: project.justfile
    resource: .linkml/project.justfile
  - resource: .linkml/meta
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: 4b78000fe91d8f08e2bbb0695f0192248496ca4f
status: draft
---

# CALM's JSON Schema files, generated

`scripts/calm_meta.py` runs gen-json-schema once and shapes its output into CALM's layout.[^calm_meta.py] `calm.json` and `calm-timeline.json` are copies of CALM's files, because they define nothing.[^calm_meta.py] `just gen-calm` writes the folder, and `just check-calm` fails when it is stale.[^project.justfile]

[^calm_meta.py]: .linkml/scripts/calm_meta.py, the docstring
[^project.justfile]: .linkml/project.justfile
