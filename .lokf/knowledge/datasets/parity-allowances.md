---
type: Dataset
id: https://w3id.org/lmodel/calm/knowledge/datasets/parity-allowances
genre: reference
title: Parity allowances
description: "`.linkml/parity/`: the probes whose verdicts the parity tests check, and the definitions allowed to differ in shape from CALM's files, each with its kind and reason."
resource: .linkml/parity
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-meta-files
sources:
  - id: probes.yaml
    resource: .linkml/parity/probes.yaml
  - id: structural.yaml
    resource: .linkml/parity/structural.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:08:58Z"
  revision: 978a861246a227e8e26439074bd579f7e2c4b5f7
status: draft
---

# Parity allowances

`probes.yaml` lists values to validate against one definition of each set. It says where the generated set may be wider or narrower, and why.[^probes.yaml] `structural.yaml` lists the six definitions whose shape differs. Each is an equivalent form, a gap of LinkML's or a fault of CALM's.[^structural.yaml]

[^probes.yaml]: .linkml/parity/probes.yaml
[^structural.yaml]: .linkml/parity/structural.yaml
