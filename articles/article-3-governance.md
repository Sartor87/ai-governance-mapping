# Building a unified Responsible AI governance framework

> Outline. Pairs directly with this repo (the unified controls catalog, OPA
> policies, templates, and gap-check CLI are the publishable artifacts).
> Replace `<FILL: ...>` with anonymized adoption specifics.

## Hook
- Why teams face four frameworks at once: NIST AI RMF, EU AI Act, OWASP LLM
  Top 10, ISO/IEC 42001 — and why four checklists is the wrong answer.

## The unifying move
- One controls catalog, each control mapped to all four frameworks.
- Walk the crosswalk (link `controls/unified_controls.csv` and the `docs/`).

## From paper to code
- Controls that land as guardrails (input/output moderation), audit logging,
  encryption, retention, human oversight, rate limiting.
- Policy-as-code: the OPA/Rego policies that gate deploys.
- Model cards, risk assessments, audit-log schema as living templates.
- The `compliance-check` gap report in CI.

## Adoption
- Rollout across `<FILL: number>` products in `<FILL: timeframe>`.
- Resistance patterns and how we overcame them: `<FILL: 2–3 concrete ones>`.

## What's next
- EU AI Act high-risk obligations phasing through 2026–2027; GPAI duties.
- Where this catalog goes next.

## Takeaways
- The mapping is the leverage; the tooling makes it stick.
