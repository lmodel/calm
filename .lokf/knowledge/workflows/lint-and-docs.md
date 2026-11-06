---
type: Service
id: https://w3id.org/lmodel/calm/knowledge/workflows/lint-and-docs
genre: reference
title: Lint and docs (lint-and-docs.yaml)
description: "Static checks of this project's files, never FINOS's: ShellCheck, actionlint on the project's workflows, word budgets, markdownlint, lychee and codespell."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: e7660611c637d033fcb16e8de895531804ff8e35
status: draft
---

# Lint and docs (lint-and-docs.yaml)

Each job reads only this project's paths, and the word budgets are 1,000 for CONTRIBUTING.md and 900 for SECURITY.md.[^lint-and-docs.yaml]

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml
