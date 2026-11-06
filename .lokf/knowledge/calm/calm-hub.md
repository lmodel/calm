---
type: CalmNode
id: https://w3id.org/lmodel/calm/knowledge/calm/calm-hub
title: CALM Hub API
description: "CALM Hub's API as a node of CALM's own architecture: the registry service for architectures, patterns and standards, built with Quarkus, and a typed concept of this bundle."
resource: calm/architecture/calm-3.json
isPartOf:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-own-architecture
unique_id: calm-hub
node_type: service
details:
  detailed_architecture: calm-hub-detail.architecture.json
sources:
  - id: calm-3.json
    resource: calm/architecture/calm-3.json
    title: node calm-hub
  - id: finos-readme.md
    resource: README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: d95a3bbe6ff777d89d63481ca96a508e9575f7d8
status: draft
---

# CALM Hub API

`calm-3.json` describes CALM Hub's API as a node of type `service`. The node has a REST interface and a detailed architecture of its own.[^calm-3.json] Its code is `calm-hub/` in FINOS's tree.[^finos-readme.md]

[^calm-3.json]: calm/architecture/calm-3.json, node calm-hub
[^finos-readme.md]: README.md
