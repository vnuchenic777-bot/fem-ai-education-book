#!/usr/bin/env python3
"""Validate JSON and YAML files used by the Jupyter Book."""

from __future__ import annotations

import json
from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "_build", ".venv", "venv", "env", "__pycache__", ".jupyter_cache"}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)


def validate_json(path: Path) -> str | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except Exception as exc:  # noqa: BLE001 - report parser errors plainly.
        return f"{path.relative_to(ROOT)}: JSON error: {exc}"
    return None


def validate_yaml(path: Path) -> str | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            yaml.safe_load(handle)
    except Exception as exc:  # noqa: BLE001 - report parser errors plainly.
        return f"{path.relative_to(ROOT)}: YAML error: {exc}"
    return None


def main() -> int:
    errors: list[str] = []
    json_files = []
    yaml_files = []

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or should_skip(path):
            continue
        suffix = path.suffix.lower()
        if suffix == ".json":
            json_files.append(path)
            error = validate_json(path)
        elif suffix in {".yaml", ".yml"}:
            yaml_files.append(path)
            error = validate_yaml(path)
        else:
            continue
        if error:
            errors.append(error)

    print("Structured data validation")
    print(f"- JSON files checked: {len(json_files)}")
    print(f"- YAML files checked: {len(yaml_files)}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("- Result: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
