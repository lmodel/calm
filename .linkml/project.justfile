## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ CALM's JSON Schema files ============

# Write meta/, CALM's eleven JSON Schema files, from the model (run after every schema change)
[group('model development')]
gen-calm:
  uv run python scripts/calm_meta.py

# Fail when meta/ differs from what the model gives
[group('model development')]
check-calm:
  uv run python scripts/calm_meta.py --check

# ============ Upstream ============

# Report what has moved in calm-schema and in FINOS's tree since the pins
[group('model development')]
check-upstream:
  uv run python scripts/check_upstream_release.py

# Write tests/upstream_tree.tsv from FINOS's tree at a commit, after a merge of it
[group('model development')]
pin-finos-tree commit:
  uv run python scripts/pin_finos_tree.py {{commit}}

# ---- linkml-sidecar: the linkml_schema doorway (kept across `just update`) ----
# The schema folder under an ordinary, visible name at the host root, for
# folder pickers and file managers that hide dot-folders. Git carries the
# link; a sync service does not, so this recipe recreates it on a machine
# where it is missing. POSIX only; on Windows run, from the host root,
# mklink /J linkml_schema .linkml\src\calm\schema

# Create (or recreate) the linkml_schema link at the host root, to .linkml/src/calm/schema
[group('sidecar')]
linkml-link:
    #!/usr/bin/env bash
    set -euo pipefail
    target=".linkml/src/{{schema_name}}/schema"
    [ -d "../$target" ] || { echo "no $target to link to" >&2; exit 1; }
    if [ -L ../linkml_schema ]; then
      if [ "$(readlink ../linkml_schema)" = "$target" ]; then echo "linkml_schema already present - nothing to link"; exit 0; fi
      echo "../linkml_schema is a link elsewhere ($(readlink ../linkml_schema)) - remove it and re-run" >&2; exit 1
    fi
    if [ -e ../linkml_schema ]; then echo "../linkml_schema exists and is not a link - leaving it alone" >&2; exit 1; fi
    ln -s "$target" ../linkml_schema && echo "linked linkml_schema -> $target"
