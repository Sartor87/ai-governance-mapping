# AI Governance Mapping

> One **unified controls catalog** that crosswalks four AI governance frameworks —
> **NIST AI RMF 1.0** (+ Generative AI Profile), the **EU AI Act**, the **OWASP
> LLM Top 10 (2025)**, and **ISO/IEC 42001:2023** — plus Open Policy Agent
> policies, documentation templates, and a CLI that produces a compliance **gap
> report** for a project.

<!-- Badges placeholder: CI, license -->

---

## Why this exists

Enterprise AI teams don't comply with one framework — they comply with several at
once, and the controls overlap heavily. Maintaining four separate checklists is
wasteful and drifts out of sync. This repo collapses them into **one catalog of
controls**, each mapped back to every framework, with concrete implementation
guidance, tooling, and the evidence an auditor expects.

The catalog itself is the artifact: [`controls/unified_controls.csv`](controls/unified_controls.csv).

## What's inside

| Path | What |
|------|------|
| [`controls/unified_controls.csv`](controls/unified_controls.csv) | The master crosswalk — one row per control, mapped to all four frameworks |
| [`docs/`](docs/) | Per-framework explainers that crosswalk back to control IDs, with source citations |
| [`controls/policies/`](controls/policies/) | Open Policy Agent (Rego) policies enforcing the machine-checkable controls |
| [`templates/`](templates/) | Model card, risk assessment, and audit-log schema templates |
| [`tools/compliance_check.py`](tools/compliance_check.py) | CLI: takes a project config, reports satisfied vs. missing controls, exits non-zero on gaps |

## Quick start

```bash
pip install -e .
# Score a project's declared controls against the catalog:
compliance-check examples/sample_project.yaml
```

The check reads which controls a project claims to satisfy (with evidence),
compares against the catalog, and prints a gap report — green when every
applicable control has evidence, non-zero exit when gaps remain (CI-gateable).

## Frameworks covered

- **NIST AI RMF 1.0** (Jan 2023) and the **Generative AI Profile** (NIST-AI-600-1, Jul 2024) — functions GOVERN / MAP / MEASURE / MANAGE.
- **EU AI Act** — Regulation (EU) 2024/1689, high-risk obligations (Arts. 9–15, 72).
- **OWASP Top 10 for LLM Applications (2025)** — LLM01–LLM10.
- **ISO/IEC 42001:2023** — AI management system, Annex A controls.

> Citation discipline: every framework reference in [`docs/`](docs/) links to its
> source. Mappings are interpretive aids, not legal advice.

## License

MIT (see [LICENSE](LICENSE)).
