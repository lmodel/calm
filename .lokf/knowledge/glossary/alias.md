---
type: GlossaryTerm
id: https://w3id.org/lmodel/calm/knowledge/glossary/alias
genre: reference
title: Alias (of a slot)
description: In this schema, the CALM key a slot carries when its name differs, such as `unique-id` for `unique_id`; scripts/calm_meta.py writes CALM's files with the aliases as keys.
resource: .linkml/src/calm/schema/calm.yaml
sources:
  - id: calm.yaml
    resource: .linkml/src/calm/schema/calm.yaml
    title: comments
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:26:22Z"
  revision: 7c036d453c485cf0e0a265f4c500d78a9018f82e
status: draft
---

# Alias (of a slot)

A slot whose name differs from CALM's key carries the key as its alias.[^calm.yaml] Six slots list CALM's key under `aliases` instead, so that only CALM's files carry it. Five hold CALM's `source`, `destination`, `target`, `unit` and `type`, of which LOKF defines all but `destination` with another meaning, and one holds `$schema`.[^calm.yaml]

[^calm.yaml]: .linkml/src/calm/schema/calm.yaml, comments
