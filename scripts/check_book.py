#!/usr/bin/env python3
"""Check required Jupyter Book files and TOC targets."""

from __future__ import annotations

from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "_config.yml",
    "_toc.yml",
    "index.md",
    "requirements.txt",
]


def iter_toc_files(node):
    if isinstance(node, dict):
        if "file" in node:
            yield node["file"]
        for value in node.values():
            yield from iter_toc_files(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_toc_files(item)


def source_exists(stem: str) -> bool:
    path = ROOT / stem
    if path.suffix:
        return path.exists()
    return any(path.with_suffix(ext).exists() for ext in [".md", ".ipynb", ".myst"])


def main() -> int:
    errors: list[str] = []

    print("Jupyter Book structure check")
    for filename in REQUIRED_FILES:
        path = ROOT / filename
        if path.exists():
            print(f"- OK: {filename}")
        else:
            errors.append(f"Missing required file: {filename}")

    toc_path = ROOT / "_toc.yml"
    toc = {}
    if toc_path.exists():
        try:
            toc = yaml.safe_load(toc_path.read_text(encoding="utf-8")) or {}
        except Exception as exc:  # noqa: BLE001 - report parser errors plainly.
            errors.append(f"_toc.yml cannot be parsed: {exc}")

    toc_files = sorted(set(iter_toc_files(toc)))
    print(f"- TOC entries checked: {len(toc_files)}")
    for stem in toc_files:
        if source_exists(stem):
            print(f"  OK: {stem}")
        else:
            errors.append(f"TOC target does not exist: {stem}")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("- Result: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
