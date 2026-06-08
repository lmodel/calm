"""Data test."""

import os
import glob
import subprocess
import pytest
from pathlib import Path

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"
DATA_DIR_CHANDRALANKA_VALID = Path(__file__).parent / "data" / "chandralanka" / "valid"
DATA_DIR_CHANDRALANKA_INVALID = Path(__file__).parent / "data" / "chandralanka" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml")) + \
    glob.glob(os.path.join(DATA_DIR_CHANDRALANKA_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml")) + \
    glob.glob(os.path.join(DATA_DIR_CHANDRALANKA_INVALID, "*.yaml"))

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PROJECT_ROOT / "src" / "calm" / "schema" / "calm.yaml"


def _validate(filepath: str, target_class_name: str) -> subprocess.CompletedProcess[str]:
    """Run linkml-validate against one fixture and target class."""
    return subprocess.run(
        [
            "uv",
            "run",
            "linkml-validate",
            "--schema",
            str(SCHEMA_PATH),
            "--target-class",
            target_class_name,
            filepath,
        ],
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        check=False,
    )


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test all valid data files pass linkml-validate."""
    target_class_name = Path(filepath).stem.split("-")[0]
    result = _validate(filepath, target_class_name)
    assert result.returncode == 0, (
        f"Expected valid fixture to pass: {filepath}\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Test all invalid data files fail linkml-validate."""
    target_class_name = Path(filepath).stem.split("-")[0]
    result = _validate(filepath, target_class_name)
    assert result.returncode != 0, (
        f"Expected invalid fixture to fail: {filepath}\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )
