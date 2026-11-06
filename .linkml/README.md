<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# calm

FINOS CALM 1.3 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/calm](https://lmodel.github.io/calm)

## What it models

The schema models [CALM](https://calm.finos.org/), the Common Architecture Language Model of FINOS's Architecture as Code project, at release 1.3 of [calm-schema](https://github.com/finos/calm-schema): architectures, their nodes, relationships, flows and controls, timelines, decorators, evidence, control requirements and units. Each module renders one of CALM's eleven JSON Schema files, and [meta/](meta) holds those files generated from the model, which [tests/test_parity.py](tests/test_parity.py) holds to CALM's own.

This repository is a fork of [finos/architecture-as-code](https://github.com/finos/architecture-as-code). FINOS's tree sits unchanged at the repository's root, and this project sits beside it, in this folder, `.lokf/` and `website/`. [upstream/](upstream) holds calm-schema's v1.3 files, and a weekly workflow opens an issue when calm-schema tags a release or FINOS's main moves.

## Mappings

* **CALM's own definitions**: each class, enum and type names the definition it renders in `exact_mappings`, such as `calm_meta:core.json#/defs/node`. `tests/test_schema_rules.py` resolves each one in the pinned copy.

## Repository Structure

* [docs/](docs/): the website's own pages
* [meta/](meta): CALM's JSON Schema files and a JSON-LD context with CALM's keys, which [scripts/calm_meta.py](scripts/calm_meta.py) writes from the schema
* [parity/](parity): the differences from CALM's files the tests allow, each with its reason
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the build of `meta/`, the upstream watch and the sidecar's preflight
* [src/calm/schema/](src/calm/schema): the LinkML schema (edit it), also at `linkml_schema/` in the repository's root
* [src/calm/datamodel/](src/calm/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/problem/](tests/data/problem) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream): calm-schema's v1.3 files, unchanged

The knowledge bundle is in `.lokf/` and the website in `website/`, at the repository's root.

## Developer Tools

Run `just` from this folder to list the project's [just](https://github.com/casey/just/) recipes. Never run `just setup`, which nests a repository, or `just deploy`, which pushes the root of `gh-pages`.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) sidecar. Its domain schema, `.lokf/schema/calm.yaml`, is the copy `just lokf-adapt` writes from `src/calm/schema/calm.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-calm.yaml`.

In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
CalmControlRequirement, CalmFlow, CalmNode, CalmNodeMoment, CalmRelationship
```

The copy roots `CalmNode`, `CalmRelationship`, `CalmFlow` and `CalmControlRequirement` on LOKF's `Concept`, and folds `name` and `description` into LOKF's `title` and `description`. A concept keeps CALM's `unique_id`. Five slots keep a key LOKF defines out of the copy: `source_end`, `destination_end`, `target_architectures`, `unit_of_time` and `decorator_type`. CALM's files take the key from each slot's `aliases`. Every class and enum carries the `Calm` prefix, so none is a neighbour's. CALM's keys are ordinary words, so the copy shares some with other lmodel copies, which `tests/test_schema_rules.py` lists.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier) published under [10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).

## License

The schema project is under the [Apache License 2.0](LICENSE), and the bundle under CC BY 4.0.

CALM and FINOS's tree are FINOS's, under the [Apache License 2.0](../LICENSE), and the schema keeps CALM's descriptions under the same terms. [NOTICE](NOTICE) says what comes from where. This project is not a FINOS project, and FINOS does not endorse it.
