---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/calm/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: calm Knowledge Bundle
description: FINOS CALM 1.3 (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/calm/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# calm Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for calm. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website on GitHub Pages, built from `website/` with a page per concept, the docs pages, the changelog and the schema's pages.

# References

* [CALM Meta Schema (finos/calm-schema)](references/calm-schema.md) - FINOS's calm-schema repository, which publishes CALM's eleven JSON Schema files by release; release 1.3 is the edition this schema renders, served at CALM's release addresses.
* [FINOS Architecture as Code (finos/architecture-as-code)](references/finos-architecture-as-code.md) - FINOS's monorepo of CALM's tools (the CLI, CALM Hub, the widgets, the docs site), of which this repository is a fork, kept unchanged at the repository's root.

# Datasets

* [The CALM LinkML schema](datasets/calm-linkml-schema.md) - The LinkML model of CALM 1.3 in `.linkml/src/calm/schema/`: one module per file of CALM's, `Calm` classes that keep CALM's keys as aliases, and the umbrella `calm.yaml` with `CalmArchitecture` as its root.
* [CALM's JSON Schema files, generated](datasets/calm-meta-files.md) - The eleven files in `.linkml/meta/`, at CALM's own addresses, and the JSON-LD context beside them with CALM's keys, which `scripts/calm_meta.py` writes from the LinkML schema; the parity tests hold the files to CALM's own.
* [Pinned copy of calm-schema v1.3](datasets/upstream-copy.md) - calm-schema's files at the tag v1.3, unchanged under `.linkml/upstream/calm-schema/v1.3/`, each pinned by its git object hash in `scripts/upstream_pins.tsv`.
* [FINOS's tree](datasets/finos-tree.md) - Every file of FINOS's architecture-as-code at the merged commit, kept unchanged beside `.linkml/`, which `tests/upstream_tree.tsv` lists by hash and the parity tests read for CALM documents.
* [The schema's adapt copy (.lokf/calm.yaml)](datasets/adapt-copy.md) - `.lokf/calm.yaml`, the copy `lokf adapt` writes from the schema so that this bundle and a host's can type concepts with `CalmNode`, `CalmRelationship`, `CalmFlow` and `CalmControlRequirement`.
* [Parity allowances](datasets/parity-allowances.md) - `.linkml/parity/`: the probes whose verdicts the parity tests check, and the definitions allowed to differ in shape from CALM's files, each with its kind and reason.
* [Example data](datasets/example-data.md) - The examples and counter-examples under `.linkml/tests/data/problem/`, written with CALM's keys, which `tests/test_data.py` checks against both CALM's files and the generated ones.
* [Neighbour copies](datasets/neighbour-copies.md) - The released adapt copies of 33 other lmodel schemas in `.linkml/tests/neighbours/`, each pinned by checksum, that `tests/test_schema_rules.py` checks this copy's names against.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators write from the schema: `.linkml/project/` (JSON Schema, OWL, SHACL, ShEx, Java, TypeScript and more), the Python datamodel and `docs/schema/calm.yaml`. None is edited by hand.
* [CALM's own architecture](datasets/calm-own-architecture.md) - FINOS's CALM description of its own tools, in `calm/architecture/` of FINOS's tree: three moments of one architecture and a timeline, from which this bundle's typed CALM concepts are taken.

# Calm

* [CALM CLI](calm/calm-cli.md) - The CALM CLI as a node of CALM's own architecture: a service for validation, generation, visualisation and documentation, and a typed concept of this bundle.
* [CALM Hub API](calm/calm-hub.md) - CALM Hub's API as a node of CALM's own architecture: the registry service for architectures, patterns and standards, built with Quarkus, and a typed concept of this bundle.
* [CLI to CALM Hub](calm/cli-to-hub.md) - The connection from the CALM CLI to CALM Hub's REST interface over HTTPS, as a relationship of CALM's own architecture and a typed concept of this bundle.
* [Publish Architecture](calm/publish-architecture.md) - The flow in which a user publishes a CALM architecture to CALM Hub through the CLI, in three transitions, as a flow of CALM's own architecture and a typed concept of this bundle.
* [Access Control (CR-001)](calm/cr-001-access-control.md) - The control requirement CALM's own `control-requirement.json` gives as its example, `CR-001`, and a typed concept of this bundle.

# Explanations

* [How the fork is laid out](explanations/fork-layout.md) - Why this repository keeps FINOS's tree unchanged at its root and puts the schema project in `.linkml/`, the bundle in `.lokf/` and the site in `website/`, and what links and pointers it adds.
* [How CALM's files are generated from the model](explanations/how-meta-is-generated.md) - How `scripts/calm_meta.py` turns gen-json-schema's single document into CALM's eleven files: routing by module, keys from exact mappings, five repairs of linkml 1.12.1 and four rules for what LinkML cannot state.
* [Where the model differs from CALM's files](explanations/differences-from-calm.md) - The differences the parity tests allow between the generated files and CALM's: metadata and decorator data are wider, a controls map is narrower, and three faults of CALM's own files are not repeated.
* [How the model keeps CALM's form](explanations/modelling-choices.md) - The modelling choices that keep CALM's documents valid as they are: CALM's keys as aliases, four slots renamed apart from LOKF, open and closed classes as CALM has them, CALM's descriptions, and references as strings.
* [What the model leaves out](explanations/what-is-left-out.md) - What this schema does not model: CALM's decorator standards beyond the decorator itself, the constraints a pattern states, and FINOS's tools.

# Glossary

* [CALM](glossary/calm.md) - The Common Architecture Language Model: FINOS's JSON Schema vocabulary for describing a software architecture as data, which this schema models at release 1.3.
* [Pattern (CALM)](glossary/pattern.md) - A CALM pattern: a JSON Schema whose `$schema` is CALM's and which constrains the architectures that follow it. It validates here as an architecture.
* [Decorator (CALM)](glossary/decorator.md) - A CALM decorator: supplementary information about elements of one or more architectures, kept apart from them, which `CalmDecorator` models.
* [Alias (of a slot)](glossary/alias.md) - In this schema, the CALM key a slot carries when its name differs, such as `unique-id` for `unique_id`; scripts/calm_meta.py writes CALM's files with the aliases as keys.

# Playbooks

* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - The steps after an edit to the schema: lint, regenerate the project, CALM's files, the docs and the adapt copy, then run the tests from `.linkml/`.
* [Take a new release of CALM or FINOS's tree](playbooks/take-a-new-calm-release.md) - What to do when the weekly watch reports a calm-schema release or a move of FINOS's main: refresh `.linkml/upstream/` and the pins, or merge FINOS's tree and rewrite its list.
* [Release the schema](playbooks/release.md) - How a release is cut: typed commits, an `## [Unreleased]` changelog section, semantic-release from the `v0.0.0` baseline on the merge of FINOS's tree, and the knowledge release's assets.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons. FINOS's other files are its tools and stay outside the map.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI assistance in this repository: the person who submits a change is its author, FINOS's files stay FINOS's, an element says what CALM's files say, and AI co-authorship in commits is discouraged.
* [Licence and attribution](policies/license-and-attribution.md) - Which licence applies where: this project's files under Apache 2.0, FINOS's tree and CALM under FINOS's Apache 2.0 terms, CALM's descriptions kept word for word, and the bundle under CC BY 4.0.
* [Security policy](policies/security-policy.md) - How to report a vulnerability privately, what this repository releases, and what holds each surface that executes here: the workflows, the scheduled librarian and the release.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The test workflow: on each pull request and push to main it installs from `.linkml/uv.lock`, lints the schema, runs `just test` on Python 3.10 to 3.14, and checks CALM's files and the adapt copy.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - Static checks of this project's files, never FINOS's: ShellCheck, actionlint on the project's workflows, word budgets, markdownlint, lychee and codespell.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `.linkml/scripts/check_upstream_release.py` runs against calm-schema and FINOS's main; a failing check opens or updates an issue.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The release workflow: it previews each pull request's release and, on a push to main, promotes the changelog, tags and publishes the release behind the `release` Environment.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The scheduled run of the ktl-librarian skill, from the KTL v0.61.0 templates; inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is true.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on every pull request that touches `.lokf/`: validation, reference checks, the conventions and the provenance of each person's confirmation.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the adapt copy, the bundle and the Copilot skill to a release, when dispatched or once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly check that keeps the KTL copies and the skills pin at the newest KTL release, by a pull request.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` and, once `KNOWLEDGE_WEBSITE_ENABLED` is true, deploys it to GitHub Pages.
