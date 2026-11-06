---
type: Explanation
id: https://w3id.org/lmodel/calm/knowledge/explanations/how-meta-is-generated
genre: explanation
title: How CALM's files are generated from the model
description: "How `scripts/calm_meta.py` turns gen-json-schema's single document into CALM's eleven files: routing by module, keys from exact mappings, five repairs of linkml 1.12.1 and four rules for what LinkML cannot state."
resource: .linkml/scripts/calm_meta.py
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-meta-files
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: How CALM's files are generated
  - id: calm_meta.py
    resource: .linkml/scripts/calm_meta.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
status: draft
---

# How CALM's files are generated from the model

The script runs the generator once and makes each module its file. It writes a class with no counterpart in CALM's files inline, where it is used.[^about.md] It repairs five faults of linkml 1.12.1's generator and states four things LinkML cannot, each named in its docstring.[^calm_meta.py] The `--split`, `--draft` and `--def-name-style` options proposed for gen-json-schema would do most of its routing.[^about.md]

[^about.md]: .linkml/docs/about.md, How CALM's files are generated
[^calm_meta.py]: .linkml/scripts/calm_meta.py, the docstring
