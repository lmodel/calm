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
