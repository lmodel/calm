---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
genre: reference
title: The CALM LinkML schema
description: "The LinkML model of CALM 1.3 in `.linkml/src/calm/schema/`: one module per file of CALM's, `Calm` classes that keep CALM's keys as aliases, and the umbrella `calm.yaml` with `CalmArchitecture` as its root."
resource: .linkml/src/calm/schema/calm.yaml
derivedFrom:
  - https://w3id.org/lmodel/calm/knowledge/references/calm-schema
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: How the modules fit together
  - id: linkml-readme.md
    resource: .linkml/README.md
    title: Repository Structure
  - resource: .linkml/src/calm/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
status: draft
---

# The CALM LinkML schema

The umbrella `calm.yaml` imports nine modules, and each renders one of CALM's files.[^about.md] A slot keeps CALM's key as its alias. Where CALM describes an element, the description is CALM's own words.[^about.md] `linkml_schema` at the repository's root is a link to this folder.[^linkml-readme.md]

[^about.md]: .linkml/docs/about.md, How the modules fit together
[^linkml-readme.md]: .linkml/README.md, Repository Structure
