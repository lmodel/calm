---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/calm-meta-files
genre: reference
title: CALM's JSON Schema files, generated
description: The eleven files in `.linkml/meta/`, at CALM's own addresses, and the JSON-LD context beside them with CALM's keys, which `scripts/calm_meta.py` writes from the LinkML schema; the parity tests hold the files to CALM's own.
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
  at: "2026-11-06T20:27:22Z"
status: draft
---

# CALM's JSON Schema files, generated

`scripts/calm_meta.py` runs gen-json-schema once and shapes its output into CALM's layout.[^calm_meta.py] `calm.json` and `calm-timeline.json` are copies of CALM's files, because they define nothing.[^calm_meta.py] `just gen-calm` writes the folder, and `just check-calm` fails when it is stale.[^project.justfile]

`calm.context.jsonld`, beside the eleven files, is a JSON-LD context keyed by CALM's keys, written from the slots' aliases and IRIs, so that a CALM document expands to RDF under the schema's IRIs without renaming.[^calm_meta.py]

[^calm_meta.py]: .linkml/scripts/calm_meta.py, the docstring
[^project.justfile]: .linkml/project.justfile
