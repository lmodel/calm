---
type: Explanation
id: https://w3id.org/lmodel/calm/knowledge/explanations/modelling-choices
genre: explanation
title: How the model keeps CALM's form
description: "The modelling choices that keep CALM's documents valid as they are: CALM's keys as aliases, four slots renamed apart from LOKF, open and closed classes as CALM has them, CALM's descriptions, and references as strings."
resource: .linkml/docs/about.md
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: How the model keeps CALM's form
  - id: docs-index.md
    resource: .linkml/docs/index.md
    title: Validating a CALM document
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:26:22Z"
  revision: 7c036d453c485cf0e0a265f4c500d78a9018f82e
status: draft
---

# How the model keeps CALM's form

A slot carries CALM's key as its alias. Six slots list the key under `aliases` instead: five hold CALM's `source`, `destination`, `target`, `unit` and `type`, of which LOKF defines all but `destination` with another meaning, and one holds `$schema`, which gen-python would make an attribute's name.[^about.md] No slot is an identifier. gen-python names an identifier's type after its alias, and `unique-id` is no Python name.[^about.md] `linkml-validate`, the example runner and the dataclasses read slot names, so they cannot read a CALM document.[^docs-index.md]

[^about.md]: .linkml/docs/about.md, How the model keeps CALM's form
[^docs-index.md]: .linkml/docs/index.md, Validating a CALM document
