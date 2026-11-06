# Glossary

* [CALM](calm.md) - The Common Architecture Language Model: FINOS's JSON Schema vocabulary for describing a software architecture as data, which this schema models at release 1.3.
* [Pattern (CALM)](pattern.md) - A CALM pattern: a JSON Schema whose `$schema` is CALM's and which constrains the architectures that follow it. It validates here as an architecture.
* [Decorator (CALM)](decorator.md) - A CALM decorator: supplementary information about elements of one or more architectures, kept apart from them, which `CalmDecorator` models.
* [Alias (of a slot)](alias.md) - In this schema, the CALM key a slot carries when its name differs, such as `unique-id` for `unique_id`; scripts/calm_meta.py writes CALM's files with the aliases as keys.
