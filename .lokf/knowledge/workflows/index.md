# Workflows

* [Build and test (main.yaml)](main.md) - The test workflow: on each pull request and push to main it installs from `.linkml/uv.lock`, lints the schema, runs `just test` on Python 3.10 to 3.14, and checks CALM's files and the adapt copy.
* [Lint and docs (lint-and-docs.yaml)](lint-and-docs.md) - Static checks of this project's files, never FINOS's: ShellCheck, actionlint on the project's workflows, word budgets, markdownlint, lychee and codespell.
* [Upstream watch (upstream-watch.yaml)](upstream-watch.md) - The weekly check that `.linkml/scripts/check_upstream_release.py` runs against calm-schema and FINOS's main; a failing check opens or updates an issue.
* [Semantic release (semantic-release.yml)](semantic-release.md) - The release workflow: it previews each pull request's release and, on a push to main, promotes the changelog, tags and publishes the release behind the `release` Environment.
* [Knowledge librarian (knowledge-librarian.yaml)](knowledge-librarian.md) - The scheduled run of the ktl-librarian skill, from the KTL v0.61.0 templates; inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is true.
* [Knowledge registrar (knowledge-registrar.yaml)](knowledge-registrar.md) - The gate on every pull request that touches `.lokf/`: validation, reference checks, the conventions and the provenance of each person's confirmation.
* [Knowledge release (knowledge-release.yaml)](knowledge-release.md) - The workflow that attaches the adapt copy, the bundle and the Copilot skill to a release, when dispatched or once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Knowledge sync (knowledge-sync.yaml)](knowledge-sync.md) - The weekly check that keeps the KTL copies and the skills pin at the newest KTL release, by a pull request.
* [Knowledge website (knowledge-website.yaml)](knowledge-website.md) - The workflow that builds `website/` and, once `KNOWLEDGE_WEBSITE_ENABLED` is true, deploys it to GitHub Pages.
