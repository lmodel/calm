---
type: Playbook
id: https://w3id.org/lmodel/calm/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons. FINOS's other files are its tools and stay outside the map."
resource: .
references:
  - https://w3id.org/lmodel/calm/knowledge/datasets/calm-linkml-schema
  - https://w3id.org/lmodel/calm/knowledge/references/calm-schema
  - https://w3id.org/lmodel/calm/knowledge/references/finos-architecture-as-code
sources:
  - resource: .linkml/src/calm/schema
  - resource: .linkml/meta
  - resource: .linkml/upstream
  - resource: .linkml/parity
  - resource: .linkml/scripts
  - resource: .linkml/tests
  - resource: .linkml/docs
  - resource: .linkml/project
  - resource: .linkml/src/calm/datamodel
  - resource: website
  - resource: .github/workflows/main.yaml
  - resource: .github/workflows/lint-and-docs.yaml
  - resource: .github/workflows/upstream-watch.yaml
  - resource: .github/workflows/semantic-release.yml
  - resource: .github/workflows/knowledge-librarian.yaml
  - resource: .github/workflows/knowledge-registrar.yaml
  - resource: .github/workflows/knowledge-release.yaml
  - resource: .github/workflows/knowledge-sync.yaml
  - resource: .github/workflows/knowledge-website.yaml
  - resource: .github/scripts
  - resource: .github/release
  - resource: .github/SECURITY.md
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: .lokf/schema/calm.yaml
  - resource: .lokf/schema/lokf.yaml
  - resource: .linkml/generators.yaml
  - resource: .linkml/.linkmllint.yaml
  - resource: .linkml/config.public.mk
  - resource: .linkml/justfile
  - resource: .linkml/project.justfile
  - resource: .linkml/README.md
  - resource: .linkml/CHANGELOG.md
  - resource: .linkml/CONTRIBUTING.md
  - resource: .linkml/AI_COVENANT.md
  - resource: .linkml/NOTICE
  - resource: .releaserc.json
  - resource: calm/architecture
  - resource: README.md
exclusions:
  - resource: .github/dependabot.yml
    reason: "Tooling: when Dependabot opens version bumps."
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sync pull request text, from the KTL template, states nothing about the schema.
  - resource: .lokf/README.md
    reason: The sidecar README, from the KTL template, states nothing about this project.
  - resource: .lokf/queries.http
    reason: Sample queries from the KTL template.
  - resource: .lokf/ingest.yaml.sample
    reason: The ingest example from the KTL template, unused here.
  - resource: .lokf/uv.lock
    reason: The sidecar lock file, tooling that pins versions.
  - resource: .lokf/.gitignore
    reason: "Tooling: what git ignores in the sidecar."
  - resource: .lokf/.gitattributes
    reason: "Tooling: the line endings of the bundle."
  - resource: .lokf/scripts
    reason: The sidecar scripts, copies of the KTL templates that the weekly sync replaces.
  - resource: .lokf/m365
    reason: The Copilot skill builder, copies of the KTL templates that the weekly sync replaces.
  - resource: knowledge_bundle
    reason: A link to the bundle under an ordinary name.
  - resource: linkml_schema
    reason: A link to the schema folder under an ordinary name.
  - resource: llms.txt
    reason: The pointer for agents, from the KTL and linkml-sidecar templates.
  - resource: .linkml/.copier-answers.yml
    reason: The answers copier records, tooling with no fact about CALM.
  - resource: .linkml/.editorconfig
    reason: "Tooling: editor settings."
  - resource: .linkml/.gitignore
    reason: "Tooling: what git ignores in the project."
  - resource: .linkml/.markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown lint settings."
  - resource: .linkml/.pre-commit-config.yaml
    reason: "Tooling: the pre-commit hooks."
  - resource: .linkml/.yamllint.yaml
    reason: "Tooling: the YAML lint settings."
  - resource: .linkml/lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: .linkml/pyproject.toml
    reason: "Tooling: the Python project and its spell-check lists."
  - resource: .linkml/uv.lock
    reason: The project's lock file, tooling that pins versions.
  - resource: .linkml/CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, unchanged.
  - resource: .linkml/LICENSE
    reason: The Apache License text.
  - resource: .linkml/examples
    reason: The example runner's output folder, empty in git.
  - resource: .linkml/src/calm/__init__.py
    reason: Package scaffolding from the template.
  - resource: .linkml/src/calm/_version.py
    reason: Package scaffolding from the template.
  - resource: .devcontainer
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .flox
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .gitattributes
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .gitignore
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .husky
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .mvn
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .npmrc
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .nvmrc
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .roadmapper
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: AGENTS.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: CLAUDE.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: CONTRIBUTING.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: DEPLOYMENT-RECONCILIATION.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: Governance.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: LICENSE
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: LICENSE.spdx
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: MAINTAINERS.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: MAINTAINERS_GUIDELINES.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: NOTICE
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: PATTERN-DECISIONS.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: SECURITY.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: SUPPORT.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: THREAT_MODEL.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: brand
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-ai
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-guard
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-hub-ui
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-hub
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-lab
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-models
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-plugins
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-server
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-studio
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm-widgets
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: cli
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: commitlint.config.js
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: conferences
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: context7.json
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: docs
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: examples
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: experimental
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: hub-push-testing
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: mvnw
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: mvnw.cmd
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: osv-scanner.toml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: package-lock.json
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: package.json
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: pom.xml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: prettier.config.js
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: renovate.json
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: scripts
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: security-insights.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: shared
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: template-bundles
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: tsconfig.base.json
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: vex
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: vitest-globals.d.ts
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/CODEOWNERS
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/CODE_OF_CONDUCT.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/CONTRIBUTING.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/ISSUE_TEMPLATE
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/STYLE_GUIDE.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/labeler.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/pull_request_template.md
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/skills
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/auto-comment.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/automated-release-calm-server.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/automated-release-calm-studio.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/automated-release-vscode.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/automated-release.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-guard.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-hub-coverage.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-hub-ui.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-hub.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-lab.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-models.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-server.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-studio.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-calm-widgets.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-cli.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-docs.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-shared.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/build-vscode-extension.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/calm-schema-compatibility.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/cli-hub-smoke.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/codeql.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/dependency-review.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/docker-publish-calm-hub-native.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/docker-publish-calm-hub-readonly-native.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/docker-publish-calm-hub-readonly.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/docker-publish-calm-hub.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/license-scanning-maven.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/license-scanning-node.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/osv-fix.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/osv-scanner.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/pr-labelling.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/release-calm-models-maven-publish.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/release-calm-models-maven.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/release-parent.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/s3-docs-sync.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/s3-draft-sync.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/s3-lab-sync.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/s3-video-sync.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/semgrep-ci.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/validate-lockfile.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/validate-mongo-seed-counters.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/validate-renovate.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .github/workflows/validate-spectral.yml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm/draft
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: calm/pom.xml
    reason: "FINOS's tree: FINOS's own tools, docs and project files, which FINOS's documentation describes. This bundle covers the schema project beside them."
  - resource: .linkml/src/README.md
    reason: The template's placeholder README for the source folder.
generated:
  by: process:ktl-librarian
  at: "2026-11-06T20:27:22Z"
status: draft
---

# Knowledge sources map

| Source | Yields | Re-check |
| --- | --- | --- |
| `.linkml/src/calm/schema/` | the schema and its glossary terms (`Dataset`, `GlossaryTerm`) | the modules' headers and comments |
| `.linkml/meta/`, `.linkml/scripts/calm_meta.py` | CALM's generated files and how they are made (`Dataset`, `Explanation`) | `just check-calm` |
| `.linkml/upstream/`, `.linkml/scripts/upstream_pins.tsv` | the pinned copy of calm-schema (`Dataset`, `Reference`) | `tests/test_upstream.py` and the weekly watch |
| `.linkml/parity/`, `.linkml/tests/` | the allowances, the examples and the neighbours (`Dataset`) | `just test` |
| `.linkml/docs/`, `.linkml/README.md`, `.linkml/CONTRIBUTING.md` | explanations and playbooks | read them against the code they describe |
| `.linkml/AI_COVENANT.md`, `.linkml/NOTICE`, `.github/SECURITY.md` | the policies (`Policy`) | read them |
| `.github/workflows/`, `.github/scripts/`, `.github/release/`, `.releaserc.json` | this project's workflows (`Service`) | read each workflow's header |
| `website/` | the documentation site (`Service`) | `website/site.config.mjs` |
| `calm/architecture/` and `README.md` of FINOS's tree | CALM's own architecture and FINOS's project (`CalmNode`, `CalmRelationship`, `CalmFlow`, `Reference`) | `tests/upstream_tree.tsv` pins them; re-read after a merge of FINOS's tree |

FINOS's other workflows and tools are FINOS's project, not this one's, so the map lists them under `exclusions` and leaves them to FINOS's own documentation.
