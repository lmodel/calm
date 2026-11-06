---
type: CalmFlow
id: https://w3id.org/lmodel/calm/knowledge/calm/publish-architecture
title: Publish Architecture
description: The flow in which a user publishes a CALM architecture to CALM Hub through the CLI, in three transitions, as a flow of CALM's own architecture and a typed concept of this bundle.
resource: calm/architecture/calm-3.json
isPartOf:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-own-architecture
references:
  - https://w3id.org/lmodel/calm/knowledge/calm/cli-to-hub
unique_id: flow-publish-architecture
transitions:
  - relationship_unique_id: user-interacts-with-cli
    sequence_number: 1
    description: The user invokes the CLI to publish an architecture.
  - relationship_unique_id: cli-to-hub
    sequence_number: 2
    description: The CLI sends the architecture to CALM Hub's API over HTTPS.
  - relationship_unique_id: hub-to-db
    sequence_number: 3
    description: CALM Hub's API stores the architecture in MongoDB.
sources:
  - id: calm-3.json
    resource: calm/architecture/calm-3.json
    title: flow flow-publish-architecture
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: d95a3bbe6ff777d89d63481ca96a508e9575f7d8
status: draft
---

# Publish Architecture

`calm-3.json` describes the flow `flow-publish-architecture` in three transitions:

1. The user invokes the CLI.
2. The CLI sends the architecture to CALM Hub's API.
3. The API stores it in MongoDB.[^calm-3.json]

[^calm-3.json]: calm/architecture/calm-3.json, flow flow-publish-architecture
