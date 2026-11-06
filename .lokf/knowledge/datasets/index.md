# Datasets

* [The CALM LinkML schema](calm-linkml-schema.md) - The LinkML model of CALM 1.3 in `.linkml/src/calm/schema/`: one module per file of CALM's, `Calm` classes that keep CALM's keys as aliases, and the umbrella `calm.yaml` with `CalmArchitecture` as its root.
* [CALM's JSON Schema files, generated](calm-meta-files.md) - The eleven files in `.linkml/meta/`, at CALM's own addresses, and the JSON-LD context beside them with CALM's keys, which `scripts/calm_meta.py` writes from the LinkML schema; the parity tests hold the files to CALM's own.
* [Pinned copy of calm-schema v1.3](upstream-copy.md) - calm-schema's files at the tag v1.3, unchanged under `.linkml/upstream/calm-schema/v1.3/`, each pinned by its git object hash in `scripts/upstream_pins.tsv`.
* [FINOS's tree](finos-tree.md) - Every file of FINOS's architecture-as-code at the merged commit, kept unchanged beside `.linkml/`, which `tests/upstream_tree.tsv` lists by hash and the parity tests read for CALM documents.
* [The schema's adapt copy](adapt-copy.md) - `.lokf/schema/calm.yaml`, the copy `lokf adapt` writes from the schema so that this bundle and a host's can type concepts with `CalmNode`, `CalmRelationship`, `CalmFlow` and `CalmControlRequirement`.
* [Parity allowances](parity-allowances.md) - `.linkml/parity/`: the probes whose verdicts the parity tests check, and the definitions allowed to differ in shape from CALM's files, each with its kind and reason.
* [Example data](example-data.md) - The examples and counter-examples under `.linkml/tests/data/problem/`, written with CALM's keys, which `tests/test_data.py` checks against both CALM's files and the generated ones.
* [Neighbour copies](neighbour-copies.md) - The released adapt copies of 33 other lmodel schemas in `.linkml/tests/neighbours/`, each pinned by checksum, that `tests/test_schema_rules.py` checks this copy's names against.
* [Generated artefacts](generated-artefacts.md) - What the LinkML generators write from the schema: `.linkml/project/` (JSON Schema, OWL, SHACL, ShEx, Java, TypeScript and more), the Python datamodel and `docs/schema/calm.yaml`. None is edited by hand.
* [CALM's own architecture](calm-own-architecture.md) - FINOS's CALM description of its own tools, in `calm/architecture/` of FINOS's tree: three moments of one architecture and a timeline, from which this bundle's typed CALM concepts are taken.
