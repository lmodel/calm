# Playbooks

* [Regenerate and test after a schema change](regenerate-and-test.md) - The steps after an edit to the schema: lint, regenerate the project, CALM's files, the docs and the adapt copy, then run the tests from `.linkml/`.
* [Take a new release of CALM or FINOS's tree](take-a-new-calm-release.md) - What to do when the weekly watch reports a calm-schema release or a move of FINOS's main: refresh `.linkml/upstream/` and the pins, or merge FINOS's tree and rewrite its list.
* [Release the schema](release.md) - How a release is cut: typed commits, an `## [Unreleased]` changelog section, semantic-release from the `v0.0.0` baseline on the merge of FINOS's tree, and the knowledge release's assets.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons. FINOS's other files are its tools and stay outside the map.
