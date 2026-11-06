# About calm

This page says how the [LinkML](https://linkml.io) schema's modules fit together, how the model differs from CALM's own files, and what it leaves out.

## Where it comes from

CALM's schema is eleven JSON Schema files in FINOS's [calm-schema](https://github.com/finos/calm-schema), served at `https://calm.finos.org/release/1.3/meta/`. `upstream/calm-schema/v1.3/` holds them unchanged, with the release's deployment decorator standard. FINOS moved the schema there from architecture-as-code, whose tree sits at this repository's root, in October 2026.

## How the modules fit together

Each module renders one file, and `calm.yaml` imports them all:

| Module | CALM's file | Holds |
| --- | --- | --- |
| `calm_core` | `core.json` | `CalmNode`, `CalmRelationship` and its four kinds, `CalmDecision`, `CalmMetadata`, the protocols and node types |
| `calm` | `core.json`, its root | `CalmArchitecture`, the document itself |
| `calm_control` | `control.json` | `CalmControls`, the map of controls, and `CalmControlDetail` |
| `calm_control_requirement` | `control-requirement.json` | `CalmControlRequirement` |
| `calm_interface` | `interface.json` | `CalmInterfaceDefinition`, `CalmInterfaceType`, `CalmNodeInterface` |
| `calm_flow` | `flow.json` | `CalmFlow` and `CalmTransition` |
| `calm_timeline` | `timeline.json` | `CalmTimeline` and `CalmNodeMoment`, a subclass of `CalmNode` |
| `calm_decorators` | `decorators.json` | `CalmDecorator` |
| `calm_evidence` | `evidence.json` | `CalmEvidenceDocument` |
| `calm_units` | `units.json` | `CalmTimeUnit`, `CalmRateUnit`, `CalmCronExpression` |

Each class, enum and type that renders a definition of CALM's names it in `exact_mappings`, such as `calm_meta:core.json#/defs/node`. `calm.json` and `calm-timeline.json` declare CALM's vocabulary beside JSON Schema's own and define nothing, so no module renders them.

## How the model keeps CALM's form

- **Keys.** A slot is named in snake case, and CALM's key is its alias: `unique_id` for `unique-id`. Six slots list CALM's key under `aliases` instead, so that only CALM's files carry it. Five of them, `source_end`, `destination_end`, `target_architectures`, `unit_of_time` and `decorator_type`, hold CALM's `source`, `destination`, `target`, `unit` and `type`. LOKF defines all of those but `destination` with another meaning, and a composite's JSON-LD context gives each key one meaning. The sixth, `decorator_schema`, holds `$schema`, which gen-python would make an attribute's name.
- **Open and closed.** A class is closed where CALM's definition is, and `extra_slots` opens the rest. An architecture is open, since it is also a JSON Schema document and may carry `$schema` or a pattern's keys.
- **Descriptions.** Where CALM describes an element, the description is CALM's own words, and a test holds every one of them. The rest are this project's.
- **References.** A reference to a node, relationship or moment is its unique-id, a string, as in CALM. No slot is an identifier, because gen-python names an identifier's type after its alias, and `unique-id` is no Python name.

## How CALM's files are generated

`scripts/calm_meta.py` runs gen-json-schema once and writes `meta/`. Each module becomes its file, each definition takes the key its exact mapping names, and a class with no counterpart in CALM's files is written inline where it is used. The script repairs five faults of linkml 1.12.1's generator, and its docstring names each. It also writes by rule four things LinkML cannot state:

- an enum offered beside a free string, as `node-type-definition` is;
- a type as a definition, as `cron-expression` is;
- the one array CALM names, `option-type`;
- a key a slot lists under `aliases`. The `--split`, `--draft` and `--def-name-style` options proposed for gen-json-schema would take over most of its routing.

## Where the model differs from CALM's files

Every CALM document in FINOS's tree and calm-schema's release gets the same verdict from both. `parity/` lists what differs, each with its reason:

- **Wider.** `metadata` accepts any value, since LinkML cannot state "a list of objects, or an object". A decorator's `data` may be empty, since LinkML cannot state CALM's `minProperties`.
- **Narrower.** A controls map holds a control under every key. CALM's pattern for the key, which LinkML cannot state, checks nothing in CALM's file either, since a key outside it is left unchecked.
- **CALM's own faults.** `core.json` puts `additionalProperties: false` inside `properties`, so it refuses an architecture with a key of that name. `units.json` closes a root that defines nothing. The pattern of `cron-expression` refuses all three of CALM's examples.

## What is left out

- **CALM's standards**, such as the deployment and control evaluation decorator standards. Each has a version of its own, and a decorator that follows one validates here as a decorator. The tests read the deployment standard's examples.
- **Patterns.** A CALM pattern is a JSON Schema that constrains architectures. It validates here as an architecture, and nothing models its constraints.
- **CALM's tools**: the CLI, CALM Hub, the widgets and the rest of FINOS's tree.
