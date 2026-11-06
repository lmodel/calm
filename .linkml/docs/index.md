# calm

This project is a LinkML model of CALM 1.3, the Common Architecture Language Model that FINOS's Architecture as Code project publishes as the CALM Meta Schema. Each module renders one of CALM's JSON Schema files and keeps CALM's keys, so a CALM document validates here unchanged.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the modules fit together, how the model differs from CALM's files and what it leaves out
- [`calm.yaml`](schema/calm.yaml): the schema, its modules merged

## Validating a CALM document

The files under `meta/` are CALM's eleven JSON Schema files, generated from the model, at CALM's own addresses. A validator that loads them by `$id` reads them as it reads CALM's:

```bash
uv run python -c '
import json, sys, pathlib, jsonschema, referencing
from jsonschema_specifications import REGISTRY
from referencing.jsonschema import DRAFT202012
docs = [json.loads(p.read_text()) for p in pathlib.Path("meta").glob("*.json")]
registry = REGISTRY.with_resources((d["$id"], DRAFT202012.create_resource(d)) for d in docs)
schema = {"$ref": "https://calm.finos.org/release/1.3/meta/core.json"}
document = json.load(open(sys.argv[1]))
for error in jsonschema.Draft202012Validator(schema, registry=registry).iter_errors(document):
    print(error.json_path, error.message)
' architecture.json
```

FINOS's CLI reads a folder of CALM's files through its `--schema-directory` option. That route has not been tried with `meta/`.

`linkml-validate` and the generated dataclasses read keys by slot name (`unique_id`), not CALM's (`unique-id`), so they cannot read a CALM document. The generated Pydantic models read CALM's keys where a slot's alias is the key, but they refuse any key a class does not declare, because gen-pydantic in linkml 1.12.1 ignores `extra_slots`.

## What the tests hold

- **Addresses.** Every `$id`, every definition and every pointer that one of CALM's `$ref`s names exists in `meta/`.
- **Verdicts.** Each of the CALM documents in FINOS's tree and in calm-schema's release, each of their mutations, and each probe in `parity/probes.yaml` gets the same verdict from `meta/` and from CALM's files, or the difference `probes.yaml` gives with its reason.
- **Shape.** The definitions that differ in shape are the six `parity/structural.yaml` lists, each with its kind and reason, and every description CALM gives is kept word for word.
- **Examples.** An example of each class and a counter-example of each rule, under `tests/data/problem/`.
