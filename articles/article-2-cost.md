# Cutting LLM inference cost with prompt optimization + semantic caching

> Outline. Replace `<FILL: ...>` with anonymized specifics. Redact absolute $
> where needed; ratios and methodology are the shareable part.

## Hook
- The workload: `<FILL: rough RPS / token volume, anonymized>`.
- Baseline monthly spend: `<FILL: $ or "$X0K/yr">`.

## Where the money goes
- Token accounting methodology: input vs output, per-route breakdown.
- Identifying redundant context (the cheapest tokens are the ones you don't send).

## Levers
- Prompt compression (e.g. LLMLingua / structural trimming): `<FILL: % token cut>`.
- Model routing (cheap model for easy routes, strong model for hard ones).
- **Semantic caching**: cache-key construction, similarity threshold, TTL
  strategy, and what *not* to cache.
- Cache hit rate: `<FILL: starting %>` → `<FILL: improved %>`.

## Measuring it
- Cost dashboards (architecture, redact $).
- The improvement loop: measure → tune threshold → re-measure.

## Outcome
- Savings: `<FILL: $/yr or %>` with `<FILL: quality delta — show it didn't regress>`.

## Gotchas
- Cache poisoning, stale answers, threshold over-tuning, and how we caught them.
