---
type: Playbook
id: https://w3id.org/lmodel/calm/knowledge/playbooks/release
genre: how-to
title: Release the schema
description: "How a release is cut: typed commits, an `## [Unreleased]` changelog section, semantic-release from the `v0.0.0` baseline on the merge of FINOS's tree, and the knowledge release's assets."
resource: .linkml/CONTRIBUTING.md
references:
  - https://w3id.org/lmodel/calm/knowledge/workflows/semantic-release
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: Releasing (maintainers)
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
  revision: ebc3ad962ccfabb0ed9a8bb1753974ea69ba7894
status: draft
---

# Release the schema

Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and FINOS's commits in a merge count too.[^contributing.md] On merge, semantic-release promotes the changelog section, tags `vX.Y.Z` and publishes the GitHub Release.[^contributing.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, Releasing (maintainers)
