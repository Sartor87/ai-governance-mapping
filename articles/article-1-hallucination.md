---
title: "How We Cut LLM Hallucination on a Production Assistant"
tags: [LLM, RAG, Evaluation, Generative AI, Production]
status: draft — replace [FILL: ...] with your anonymized specifics before publishing
---

# How We Cut LLM Hallucination on a Production Assistant

Most teams discover hallucination the same way: a user screenshots a confidently
wrong answer and it lands in a leadership channel. By then you're debugging in
public. This is a writeup of how we got ahead of that on a consumer-facing
assistant — [FILL: one-line anonymized product description, e.g. "a consumer
finance assistant serving ~X00K monthly users"] — and drove the hallucination
rate from [FILL: baseline %] to [FILL: after %]. The numbers are mine to share;
the method is the part worth your time.

## First, define what you're measuring

"Hallucination" is not one thing, and you can't reduce a metric you haven't
defined. We split it into three operational categories, because each has a
different fix:

1. **Unsupported claims** — the answer asserts something not present in the
   retrieved context. (A retrieval/grounding problem.)
2. **Misread context** — the right document was retrieved, but the model
   summarized it wrong. (A reasoning/prompting problem.)
3. **Fabricated specifics** — invented numbers, dates, names, or citations.
   (The most damaging category in a regulated domain.)

We labeled a few hundred real (anonymized) queries against these categories to
get a baseline. That labeling exercise was the single highest-leverage hour we
spent — it turned "the bot lies sometimes" into three tractable workstreams.

## Measure it like a test, not a vibe

We built an offline eval before changing a single prompt. The setup:

- A **golden set** of representative queries with reference answers and the
  source passages a correct answer must rest on.
- An **LLM-as-Judge** scoring each response for faithfulness to the retrieved
  context, with the judge's reasoning stored for audit (so we could spot a
  miscalibrated judge).
- **Human spot-checks** on a sample, to keep the judge honest.

Critically, this ran in CI and **gated releases**. A prompt change that improved
one query while regressing five never shipped. If you take one thing from this
article: *you cannot iterate on hallucination without a regression gate.* Vibes
optimize for the last example you looked at.

## What worked

**Retrieval grounding with citation enforcement.** We required the model to cite
the passage id backing each claim, and we post-validated that every cited id
actually existed in the retrieved set. Uncited claims were flagged. This alone
addressed most of category 1, and the citations doubled as a UX trust signal.

**Chain-of-verification for high-stakes routes.** For consequential answers, a
second pass asked the model to list the claims it just made and check each
against the context before finalizing. It costs latency and tokens, so we
applied it only where the cost of error justified it — not everywhere.

**Structured outputs to stop free-text drift.** Forcing the answer into a schema
(answer, citations, confidence) measurably reduced fabricated specifics. A model
that has to fill a `citations: []` field is far less likely to invent a source
than one writing free prose.

**Post-call validation as a safety net.** Before an answer reached the user, a
cheap deterministic check confirmed the structural invariants (every claim
cited, no empty citations, numbers traceable to context). Cheap, fast, and it
caught the embarrassing failures.

## What didn't work

[FILL: one approach you tried that failed and why — e.g. "naively cranking the
retrieval top-k, which buried the relevant passage in noise and *increased*
misreads."] Being honest about the dead ends is what makes this credible — every
real project has them.

We also learned that telling the model "do not hallucinate" in the system prompt
does almost nothing. Models don't know when they're hallucinating; instructions
to avoid it are wishes, not controls. The wins came from changing the *inputs*
(grounding), the *output shape* (schema), and the *verification* (a real check),
not from sterner prompting.

## Rolling it out without breaking trust

We didn't flip a switch. The sequence:

1. **Shadow traffic** — run the new pipeline alongside production, scoring both,
   shipping neither. Confirms the eval gains hold on live traffic distribution.
2. **Canary** — a small slice of real users, watched closely.
3. **Ramp** — widen only while the live faithfulness metric held.

The release gate was the same eval that ran in CI, now fed a sample of
production traffic. Same ruler at every stage.

## The outcome

- Faithfulness / hallucination rate: [FILL: before] → [FILL: after]
  ([FILL: % reduction]).
- Secondary effects: [FILL: e.g. support-ticket volume, CSAT, escalations].
- Cost of the verification passes: [FILL: roughly, or "offset by the drop in
  human review"].

## Transferable takeaways

1. Decompose "hallucination" into measurable categories before fixing anything.
2. Build the eval and the regression gate *first*. It's the flywheel.
3. Grounding + structured output + a deterministic post-check beats prompt
   pleading every time.
4. Reserve expensive techniques (chain-of-verification) for the routes whose
   errors actually cost something.
5. Ship behind shadow → canary → ramp, gated by the same metric throughout.

*Methodology is generic and my own; product specifics are anonymized.*
