---
type: Playbook
id: https://w3id.org/lmodel/calm/knowledge/playbooks/take-a-new-calm-release
genre: how-to
title: Take a new release of CALM or FINOS's tree
description: "What to do when the weekly watch reports a calm-schema release or a move of FINOS's main: refresh `.linkml/upstream/` and the pins, or merge FINOS's tree and rewrite its list."
resource: .linkml/CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/calm/knowledge/references/calm-schema
  - https://w3id.org/lmodel/calm/knowledge/references/finos-architecture-as-code
sources:
  - id: contributing.md
    resource: .linkml/CONTRIBUTING.md
    title: Taking a new release of CALM or FINOS's tree
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
  revision: ebc3ad962ccfabb0ed9a8bb1753974ea69ba7894
status: draft
---

# Take a new release of CALM or FINOS's tree

For a CALM release, copy its files into `.linkml/upstream/` with their hashes, move the pins in the watch and the headers, and regenerate.[^contributing.md] For FINOS's tree, merge `upstream/main`, run `just pin-finos-tree <commit>`, move `FINOS_COMMIT`, and merge with a merge commit.[^contributing.md]

[^contributing.md]: .linkml/CONTRIBUTING.md, Taking a new release of CALM or FINOS's tree
