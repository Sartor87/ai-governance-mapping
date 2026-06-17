---
title: "Building a Unified Responsible AI Governance Framework"
tags: [Responsible AI, AI Governance, NIST AI RMF, EU AI Act, OWASP, ISO 42001]
status: draft — replace [FILL: ...] with your anonymized specifics before publishing
---

# Building a Unified Responsible AI Governance Framework

If you ship AI in an enterprise, you don't get to pick one governance framework.
You inherit several at once: the **NIST AI RMF** because it's the common
language, the **EU AI Act** because you have European users, the **OWASP LLM Top
10** because security asks, and **ISO/IEC 42001** because the auditors are
coming. The naive response is four checklists owned by four people that drift out
of sync within a quarter. This is how we collapsed them into one operational
framework — and the controls catalog, policies, and tooling are published as a
companion repo so you can start from ours instead of a blank page.

> Companion repo: a unified controls catalog (CSV), per-framework crosswalks,
> Open Policy Agent policies, documentation templates, and a `compliance-check`
> CLI. Links at the end.

## The insight: the frameworks mostly say the same things

Lay the four frameworks side by side and the overlap is enormous. "Keep records
of AI decisions" is EU AI Act Article 12, NIST MEASURE 1.1, and ISO 42001
A.6.2.8 — the *same control*, named three ways. "Defend against prompt
injection" is OWASP LLM01 and a slice of EU AI Act Article 15's cybersecurity
duty.

So we stopped maintaining four lists and built **one catalog of controls**, each
mapped to every framework. A single control — say, "audit logging of AI
interactions" — carries its NIST subcategory, its EU AI Act article, its OWASP
item, and its ISO clause in one row, plus implementation guidance, the tooling
that satisfies it, and the evidence an auditor will ask for. Add a control once,
and it's compliant against all four.

## From paper to code

A governance framework that lives in a slide deck changes no behavior. The
controls that earn their place are the ones that become *running code*:

- **Guardrails.** Input moderation (prompt-injection defense) and output
  moderation run on every model call — that's OWASP LLM01/LLM05 and EU AI Act
  Art. 15, enforced, not documented.
- **Audit logging.** A structured, tamper-evident log of inputs, outputs,
  decisions, and human overrides — no raw PII in plaintext — satisfies Art. 12 /
  ISO A.6.2.8 and gives incident response something to work with.
- **Encryption and retention.** At-rest encryption and a real retention/purge
  policy cover the data-protection controls that auditors check first.
- **Human oversight.** A review-and-override path for consequential outputs
  (Art. 14) — with the overrides logged.
- **Policy-as-code.** The machine-checkable controls become Open Policy Agent
  (Rego) policies that gate a deploy. A release that drops encryption or
  moderation fails the policy check, in CI, before it ships.
- **A compliance gap-check.** A CLI reads a project's declared controls, compares
  against the catalog, and produces a gap report — green when every applicable
  control has evidence, non-zero exit otherwise. Governance becomes a CI gate,
  not a quarterly audit scramble.

The templates — model card, risk assessment, audit-log schema — are the
human-readable evidence those controls produce.

## Adoption is the hard part

The framework was the easy 20%. Rolling it across [FILL: number] products in
[FILL: timeframe] meant overcoming predictable resistance:

- *"This will slow us down."* — Answer: it's a CI gate, not a committee. The
  gap-check runs in seconds; the policies fail fast. We measured [FILL: the
  actual overhead, e.g. "no measurable change in deploy frequency"].
- [FILL: a second resistance pattern you hit and how you handled it.]
- [FILL: a third, if you have one.]

What made it stick was meeting teams where they were: the controls mapped to
tooling they already had, and the evidence was generated as a byproduct of
shipping, not as separate paperwork.

## What's next

The EU AI Act's high-risk obligations phase in through 2026–2027, and
general-purpose-model duties (technical documentation, training-data summaries)
are landing now. A unified catalog absorbs new obligations as new rows mapped to
existing controls, instead of as a fifth checklist. That's the whole point: the
mapping is the leverage, and the tooling is what keeps it honest.

## Resources

- Companion repo: **ai-governance-mapping** — unified controls catalog, framework
  crosswalks with citations, OPA policies, templates, and the `compliance-check`
  CLI.
- Frameworks: [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework),
  [EU AI Act (Reg. 2024/1689)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj),
  [OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/),
  [ISO/IEC 42001](https://www.iso.org/standard/42001).

*Methodology is generic and my own; adoption specifics are anonymized. Mappings
are interpretive aids, not legal advice.*
