---
type: Service
id: https://w3id.org/lmodel/calm/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The test workflow: on each pull request and push to main it installs from `.linkml/uv.lock`, lints the schema, runs `just test` on Python 3.10 to 3.14, and checks CALM's files and the adapt copy."
resource: .github/workflows/main.yaml
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: fc39abe0456914e91fdf07617dbe0bcb2a336d0f
status: draft
---

# Build and test (main.yaml)

The workflow runs in `.linkml/`. It lints on Python 3.13 only, and checks `meta/` and the adapt copy there too.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml
