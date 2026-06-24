import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import generate_artifacts as ga  # noqa: E402

FIXTURE_CSV = (
    "ID,Control,NIST AI RMF,EU AI Act,OWASP LLM Top 10 (2025),"
    "ISO/IEC 42001,Implementation Guidance,Tooling,Evidence Required,"
    "Enforced in CI,Risk Tiers\n"
    "AIGOV-001,Risk assessment,GOVERN 1.1,Art. 9,—,Clause 6.1,g,t,e,no,high\n"
    "AIGOV-003,Encryption,MANAGE 2.2,Art. 15,LLM02,A.6.2.4,g,t,e,yes,"
    "high;limited;minimal\n"
)


def test_write_data_json(tmp_path, monkeypatch):
    csv_path = tmp_path / "catalog.csv"
    csv_path.write_text(FIXTURE_CSV, encoding="utf-8")
    version_path = tmp_path / "CATALOG_VERSION"
    version_path.write_text("2.0.0\n", encoding="utf-8")
    out_path = tmp_path / "data.json"

    monkeypatch.setattr(ga, "CSV_PATH", csv_path)
    monkeypatch.setattr(ga, "VERSION_PATH", version_path)
    monkeypatch.setattr(ga, "DATA_JSON_PATH", out_path)

    rows = ga.load_rows()
    ga.write_data_json(rows)

    data = json.loads(out_path.read_text(encoding="utf-8"))
    assert data == {"required_controls": ["AIGOV-003"], "catalog_version": "2.0.0"}
