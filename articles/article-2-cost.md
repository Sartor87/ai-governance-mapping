---
title: "Cutting LLM Inference Cost with Prompt Optimization and Semantic Caching"
tags: [LLM, Cost Optimization, Semantic Caching, LLMOps, Generative AI]
status: draft — replace [FILL: ...] with your anonymized specifics before publishing
---

# Cutting LLM Inference Cost with Prompt Optimization and Semantic Caching

Inference cost is the line item that surprises finance. It starts negligible
during the prototype, then scales linearly with adoption until someone asks why
the AI feature costs [FILL: $ or "$X0K/yr"]. This is how we took a production
workload's spend down by [FILL: % or $] without degrading quality. Absolute
dollars are redacted; the ratios and the method are the shareable part.

## Know where the money actually goes

Before optimizing, we instrumented every LLM call with a span carrying provider,
model, and token usage (input vs. output, separately). That gave a per-route
cost breakdown, and it immediately reframed the problem:

- A small number of routes drove most of the spend.
- **Input tokens dominated.** We were paying to re-send the same large context
  on every call.

The cheapest token is the one you don't send. Most "LLM is expensive" problems
are actually "we send too much context, too often" problems.

## Lever 1: stop sending redundant context

We audited the prompts and found the usual culprits — a giant static system
preamble re-sent every call, retrieved passages that overlapped heavily, few-shot
examples that no longer earned their tokens. Trimming and de-duplicating context
cut input tokens by [FILL: %] with no measurable quality change (we confirmed
with the eval harness — never cut tokens on faith).

Prompt compression techniques (structural trimming, and for the largest prompts
a compression pass) extended this further on the heavy routes.

## Lever 2: route the easy work to a cheaper model

Not every request needs the strongest model. We added a lightweight router: a
cheap model (or a heuristic) classified request difficulty, and only the hard
routes hit the expensive model. The trick is measuring quality *per route* so
you can prove the cheap model is good enough where you use it — again, the eval
harness paid for itself.

## Lever 3: semantic caching

This was the biggest single win. A large fraction of real traffic is
near-duplicate — users ask the same things in different words. A semantic cache
serves a stored answer when a new query is sufficiently similar to a past one.

The design decisions that mattered:

- **Cache key.** Embed the normalized query; look up by vector similarity.
  Normalize aggressively (casing, whitespace, boilerplate) before embedding.
- **Similarity threshold.** Too loose and you serve a subtly-wrong cached answer;
  too tight and the hit rate collapses. We tuned the threshold against a labeled
  set, optimizing for "answer still correct" not just "queries look similar."
- **What not to cache.** Anything personalized, time-sensitive, or
  authorization-dependent was excluded by route. A cache that serves one user's
  answer to another is a security incident, not a cost saving.
- **TTL.** Short enough that stale answers age out, long enough to capture the
  duplicate-query bursts.

Cache hit rate went from [FILL: starting %] to [FILL: improved %] after tuning
the threshold and key normalization. Every hit is a full inference call avoided.

## Measuring and holding the gains

We built cost dashboards (architecture shareable, dollars redacted) tracking
spend per route, cache hit rate, and — crucially — a **quality line next to the
cost line**. The improvement loop was: measure → adjust threshold/compression →
re-measure quality and cost. Cost work that silently degrades quality isn't a
saving; it's a deferred incident.

## Gotchas we hit

- **Cache serving stale answers** after the underlying data changed — fixed with
  shorter TTLs and event-based invalidation on the affected routes.
- **Threshold over-tuning** — chasing hit rate past the point where correctness
  held. The eval caught it.
- [FILL: one more specific-to-you gotcha].

## The outcome

- Spend: [FILL: before] → [FILL: after] ([FILL: % saved or "$X0K/yr"]).
- Quality delta: [FILL: "flat — confirmed no regression on the eval gate"].
- Cache hit rate: [FILL: %], i.e. [FILL: %] of calls avoided entirely.

## Takeaways

1. Instrument token usage per route before optimizing — you'll be surprised what
   dominates.
2. The cheapest token is the one you don't send: trim context first.
3. Route by difficulty; prove per-route quality with an eval.
4. Semantic caching is the big lever — but the threshold, key normalization, and
   exclusion rules are where correctness lives.
5. Always chart quality next to cost. A saving that regresses quality isn't one.

*Methodology is generic and my own; product specifics are anonymized.*
