---
type: Explanation
id: https://w3id.org/lmodel/calm/knowledge/explanations/differences-from-calm
genre: explanation
title: Where the model differs from CALM's files
description: "The differences the parity tests allow between the generated files and CALM's: metadata and decorator data are wider, a controls map is narrower, and three faults of CALM's own files are not repeated."
resource: .linkml/docs/about.md
about:
  - https://w3id.org/lmodel/calm/knowledge/datasets/parity-allowances
sources:
  - id: about.md
    resource: .linkml/docs/about.md
    title: Where the model differs from CALM's files
  - resource: .linkml/parity
generated:
  by: process:ktl-librarian
  at: "2026-11-06T08:26:22Z"
  revision: 7c036d453c485cf0e0a265f4c500d78a9018f82e
status: draft
---

# Where the model differs from CALM's files

`metadata` accepts any value, and a decorator's `data` may be empty, because LinkML cannot state CALM's rules there.[^about.md] A controls map holds a control under every key, where CALM leaves a key outside its pattern unchecked.[^about.md] CALM's own files hold three faults:

- `core.json` misplaces `additionalProperties`.
- `units.json` closes an empty root.
- CALM's cron pattern refuses its own examples.[^about.md]

[^about.md]: .linkml/docs/about.md, Where the model differs from CALM's files
