# NIST AI RMF → unified controls

**Source:** [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
(NIST AI 100-1, Jan 2023) and the
[Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) (NIST-AI-600-1,
Jul 2024). The framework is organized into four functions: **GOVERN, MAP,
MEASURE, MANAGE**.

Mappings are interpretive aids, not a NIST conformance claim.

| NIST function / subcategory | Theme | Unified controls |
|---|---|---|
| GOVERN 1.1–1.5 | Policies, accountability, roles | AIGOV-001, AIGOV-004, AIGOV-010 |
| GOVERN 3.2 | Human roles and oversight | AIGOV-005 |
| GOVERN 5.1 | Mechanisms for stakeholder feedback | AIGOV-016 |
| MAP 1.1 | Context and intended purpose established | AIGOV-001 |
| MAP 2.1 | Data and input provenance documented | AIGOV-002 |
| MAP 3.4 | Data privacy risks characterized | AIGOV-004, AIGOV-014 |
| MAP 4.1 | Third-party / supply-chain risks mapped | AIGOV-013 |
| MEASURE 2.2–2.3 | Evaluation of data and model performance | AIGOV-002, AIGOV-011 |
| MEASURE 2.6–2.7 | Safety and security evaluated | AIGOV-006, AIGOV-007 |
| MEASURE 2.10–2.11 | Privacy and fairness evaluated | AIGOV-014, AIGOV-016 |
| MEASURE 1.1 | Metrics and logging in place | AIGOV-009 |
| MANAGE 2.2–2.3 | Risk treatment and response | AIGOV-003, AIGOV-006, AIGOV-007, AIGOV-015 |
| MANAGE 4.1–4.3 | Monitoring, incident response, recovery | AIGOV-005, AIGOV-011, AIGOV-012 |

The **Generative AI Profile** (NIST-AI-600-1) sharpens MEASURE/MANAGE for LLM
risks — prompt injection, data leakage, and harmful content — which map to
AIGOV-006, AIGOV-007, AIGOV-009, and AIGOV-014.
