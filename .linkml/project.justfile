## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Upstream ============

# Report what has moved in calm-schema and in FINOS's tree since the pins
[group('model development')]
check-upstream:
  uv run python scripts/check_upstream_release.py
