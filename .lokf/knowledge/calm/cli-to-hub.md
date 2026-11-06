---
type: CalmRelationship
id: https://w3id.org/lmodel/calm/knowledge/calm/cli-to-hub
title: CLI to CALM Hub
description: The connection from the CALM CLI to CALM Hub's REST interface over HTTPS, as a relationship of CALM's own architecture and a typed concept of this bundle.
resource: calm/architecture/calm-3.json
isPartOf:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-own-architecture
references:
  - https://w3id.org/lmodel/calm/knowledge/calm/calm-cli
  - https://w3id.org/lmodel/calm/knowledge/calm/calm-hub
unique_id: cli-to-hub
protocol: HTTPS
relationship_type:
  connects:
    source_end:
      node: calm-cli
    destination_end:
      node: calm-hub
      interfaces:
        - calm-hub-rest-api
sources:
  - id: calm-3.json
    resource: calm/architecture/calm-3.json
    title: relationship cli-to-hub
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: d95a3bbe6ff777d89d63481ca96a508e9575f7d8
status: draft
---

# CLI to CALM Hub

`calm-3.json` describes the relationship `cli-to-hub` as a connection over HTTPS. It runs from `calm-cli` to the `calm-hub-rest-api` interface of `calm-hub`.[^calm-3.json]

[^calm-3.json]: calm/architecture/calm-3.json, relationship cli-to-hub
