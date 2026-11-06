---
type: Service
id: https://w3id.org/lmodel/calm/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: The knowledge website on GitHub Pages, built from `website/` with a page per concept, the docs pages, the changelog and the schema's pages.
resource: website/site.config.mjs
dependsOn:
  - https://w3id.org/lmodel/calm/knowledge/workflows/knowledge-website
sources:
  - id: site.config.mjs
    resource: website/site.config.mjs
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
  revision: ebc3ad962ccfabb0ed9a8bb1753974ea69ba7894
status: draft
---

# Documentation site

The site takes its home page from `.linkml/README.md`, its docs from `.linkml/docs/` and its schema pages from gen-doc.[^site.config.mjs] It redirects the old mkdocs site's addresses under `/elements/` to `/schema/`.[^site.config.mjs]

[^site.config.mjs]: website/site.config.mjs
