# How we cut LLM hallucination on a production assistant

> Outline. Replace every `<FILL: ...>` with anonymized specifics. Keep it
> generic — "a consumer fintech assistant, <FILL: scale> MAU", no internals.

## Hook
- The product (anonymized): `<FILL: one-line product description + scale>`
- The cost of hallucination in this domain (trust, support load, risk).

## How we measured it
- Defining "hallucination" operationally for this product.
- The eval setup: golden set, LLM-as-Judge, human spot-checks. (See the eval
  harness companion project.)
- Baseline rate: `<FILL: baseline %>`.

## What we tried (and what worked)
- Retrieval grounding + citation enforcement.
- Chain-of-verification / self-check prompting.
- Structured outputs to constrain free-text drift.
- Guardrails on output (post-call validation).
- What did **not** work: `<FILL: a failed approach + why>`.

## Rollout
- Shadow traffic → canary → ramp.
- A/B measurement and the guardrail that gated promotion.

## Outcome
- Hallucination rate `<FILL: before>` → `<FILL: after>` (`<FILL: % reduction>`).
- Secondary effects: `<FILL: support tickets / CSAT / etc.>`.

## Lessons
- 3–5 transferable takeaways for other teams.
