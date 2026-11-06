# Explanations

* [How the fork is laid out](fork-layout.md) - Why this repository keeps FINOS's tree unchanged at its root and puts the schema project in `.linkml/`, the bundle in `.lokf/` and the site in `website/`, and what links and pointers it adds.
* [How CALM's files are generated from the model](how-meta-is-generated.md) - How `scripts/calm_meta.py` turns gen-json-schema's single document into CALM's eleven files: routing by module, keys from exact mappings, five repairs of linkml 1.12.1 and four rules for what LinkML cannot state.
* [Where the model differs from CALM's files](differences-from-calm.md) - The differences the parity tests allow between the generated files and CALM's: metadata and decorator data are wider, a controls map is narrower, and three faults of CALM's own files are not repeated.
* [How the model keeps CALM's form](modelling-choices.md) - The modelling choices that keep CALM's documents valid as they are: CALM's keys as aliases, four slots renamed apart from LOKF, open and closed classes as CALM has them, CALM's descriptions, and references as strings.
* [What the model leaves out](what-is-left-out.md) - What this schema does not model: CALM's decorator standards beyond the decorator itself, the constraints a pattern states, and FINOS's tools.
