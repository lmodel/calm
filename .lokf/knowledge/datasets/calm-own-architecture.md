---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/calm-own-architecture
genre: reference
title: CALM's own architecture
description: "FINOS's CALM description of its own tools, in `calm/architecture/` of FINOS's tree: three moments of one architecture and a timeline, from which this bundle's typed CALM concepts are taken."
resource: calm/architecture
isPartOf:
  - https://w3id.org/lmodel/calm/knowledge/datasets/finos-tree
sources:
  - id: calm.timeline.json
    resource: calm/architecture/calm.timeline.json
  - id: calm-3.json
    resource: calm/architecture/calm-3.json
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: d95a3bbe6ff777d89d63481ca96a508e9575f7d8
status: draft
---

# CALM's own architecture

`calm-3.json` is the current moment, and `calm.timeline.json` lists `calm-1`, `calm-2` and `calm-3`.[^calm.timeline.json] The concepts under `calm/` in this bundle each take one node, relationship or flow of `calm-3.json`.[^calm-3.json]

[^calm.timeline.json]: calm/architecture/calm.timeline.json
[^calm-3.json]: calm/architecture/calm-3.json
