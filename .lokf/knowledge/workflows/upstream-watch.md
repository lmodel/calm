---
type: Service
id: https://w3id.org/lmodel/calm/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: The weekly check that `.linkml/scripts/check_upstream_release.py` runs against calm-schema and FINOS's main; a failing check opens or updates an issue.
resource: .github/workflows/upstream-watch.yaml
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: check_upstream_release.py
    resource: .linkml/scripts/check_upstream_release.py
    title: the docstring
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: f8c8b6c2c38e5ee52b86f31e9184e171ec290441
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday.[^upstream-watch.yaml] A new calm-schema tag, a moved pin, a changed pinned file or a changed licence fails it; unreleased schema work and a newer FINOS tree are reported for information.[^check_upstream_release.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^check_upstream_release.py]: .linkml/scripts/check_upstream_release.py, the docstring
