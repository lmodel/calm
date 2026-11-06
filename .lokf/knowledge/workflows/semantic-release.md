---
type: Service
id: https://w3id.org/lmodel/calm/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The release workflow: it previews each pull request's release and, on a push to main, promotes the changelog, tags and publishes the release behind the `release` Environment."
resource: .github/workflows/semantic-release.yml
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: e7660611c637d033fcb16e8de895531804ff8e35
status: draft
---

# Semantic release (semantic-release.yml)

The baseline tag sits on the merge of FINOS's tree, so FINOS's older commits do not count.[^semantic-release.yml]

[^semantic-release.yml]: .github/workflows/semantic-release.yml
