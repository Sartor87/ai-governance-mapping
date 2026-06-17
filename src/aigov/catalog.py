"""Load the unified controls catalog from CSV."""

from __future__ import annotations

import csv
from pathlib import Path

from pydantic import BaseModel


class Control(BaseModel):
    """One catalog control (id + human-readable name)."""

    id: str
    control: str


def default_catalog_path() -> Path:
    """Path to the bundled unified controls catalog."""
    return Path(__file__).resolve().parents[2] / "controls" / "unified_controls.csv"


def load_catalog(path: str | Path | None = None) -> list[Control]:
    """Load controls from the unified controls CSV (needs ID and Control columns)."""
    csv_path = Path(path) if path else default_catalog_path()
    with csv_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return [
            Control(id=row["ID"].strip(), control=row["Control"].strip())
            for row in reader
            if row.get("ID", "").strip()
        ]
