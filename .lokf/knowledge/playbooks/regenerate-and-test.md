---
type: Playbook
id: https://w3id.org/lmodel/calm/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "The steps after an edit to the schema: lint, regenerate the project, CALM's files, the docs and the adapt copy, then run the tests from `.linkml/`."
resource: .linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: Before opening a pull request
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: 6ffb90861f44ee8a4e580c28d24e2155547c76c3
status: draft
---

# Regenerate and test after a schema change

From `.linkml/`, run `just gen-project`, `just gen-calm`, `just gen-doc` and `just lokf-adapt`, and commit the output.[^contributing.md] Then run `just lint` and `just test`.[^contributing.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, Before opening a pull request
