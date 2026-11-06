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
  at: "2026-11-06T08:13:55Z"
  revision: 10de4ed9c1a6200cd505674bb14225b20a3469c6
status: draft
---

# Documentation site

The site takes its home page from `.linkml/README.md`, its docs from `.linkml/docs/` and its schema pages from gen-doc.[^site.config.mjs] It redirects the old mkdocs site's addresses under `/elements/` to `/schema/`.[^site.config.mjs]

[^site.config.mjs]: website/site.config.mjs
