# OWASP Top 10 for LLM Applications (2025) → unified controls

**Source:** [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/).
These are the most critical security risks for LLM apps; the controls below are
the defensive measures.

| OWASP ID | Risk | Unified controls |
|---|---|---|
| LLM01 | Prompt Injection | AIGOV-006, AIGOV-009 |
| LLM02 | Sensitive Information Disclosure | AIGOV-003, AIGOV-004, AIGOV-014 |
| LLM03 | Supply Chain | AIGOV-013 |
| LLM04 | Data and Model Poisoning | AIGOV-002 |
| LLM05 | Improper Output Handling | AIGOV-007 |
| LLM06 | Excessive Agency | AIGOV-005, AIGOV-010 |
| LLM07 | System Prompt Leakage | AIGOV-006, AIGOV-009 |
| LLM08 | Vector and Embedding Weaknesses | AIGOV-003, AIGOV-014 |
| LLM09 | Misinformation | AIGOV-008, AIGOV-011, AIGOV-016 |
| LLM10 | Unbounded Consumption | AIGOV-015 |

**Testing:** the OWASP risks double as a red-team checklist. A red-team suite of
prompt-injection, system-prompt-leak, and unbounded-consumption probes provides
the evidence for AIGOV-006, AIGOV-007, and AIGOV-015.
