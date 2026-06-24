#!/usr/bin/env python3
"""Regenerate controls/policies/data.json and docs/*-mapping.md AUTOGEN
blocks from controls/unified_controls.csv.

Run `python tools/generate_artifacts.py`, then `git diff --exit-code` in CI
to fail the build if committed output is stale relative to the CSV.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "controls" / "unified_controls.csv"
VERSION_PATH = REPO_ROOT / "controls" / "CATALOG_VERSION"
DATA_JSON_PATH = REPO_ROOT / "controls" / "policies" / "data.json"


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(encoding="utf-8", newline="") as fh:
        return [row for row in csv.DictReader(fh) if row.get("ID", "").strip()]


def write_data_json(rows: list[dict[str, str]]) -> None:
    version = VERSION_PATH.read_text(encoding="utf-8").strip()
    required = sorted(
        row["ID"].strip()
        for row in rows
        if row.get("Enforced in CI", "").strip().lower() == "yes"
    )
    data = {"required_controls": required, "catalog_version": version}
    DATA_JSON_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    write_data_json(load_rows())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
