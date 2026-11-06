---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/example-data
genre: reference
title: Example data
description: The examples and counter-examples under `.linkml/tests/data/problem/`, written with CALM's keys, which `tests/test_data.py` checks against both CALM's files and the generated ones.
resource: .linkml/tests/data/problem
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: test_data.py
    resource: .linkml/tests/test_data.py
    title: the docstring
  - resource: .linkml/tests/data/problem
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
status: draft
---

# Example data

Each file's name starts with the class it exemplifies. A valid example must pass both sets, and a counter-example must fail both.[^test_data.py] They sit under `problem/` because linkml-validate and the example runner read slot names, not CALM's keys.[^test_data.py]

[^test_data.py]: .linkml/tests/test_data.py, the docstring
