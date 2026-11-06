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
  at: "2026-11-06T08:08:58Z"
  revision: e3049d37e117aca6a92dff91576f333fdcfa802d
status: draft
---

# Alias (of a slot)

A slot whose name differs from CALM's key carries the key as its alias.[^calm.yaml] Six slots list CALM's key under `aliases` instead, so that only CALM's files carry it. Five hold a key LOKF defines with another meaning, and one holds `$schema`.[^calm.yaml]

[^calm.yaml]: .linkml/src/calm/schema/calm.yaml, comments
