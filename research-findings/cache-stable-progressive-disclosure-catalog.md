---
name: "Cache-Stable Progressive-Disclosure Catalog"
summary: |-
  Plain English: if an agent shows the model a catalog of on-demand capabilities, keep
  that catalog byte-identical every turn — even re-listing items already loaded — so the
  provider's prompt cache never breaks; it is cheaper to bounce an occasional redundant
  load than to bust the cache on every load. Pydantic AI v2.9.0's deferred-capability
  loader hides each `defer_loading=True` capability behind a framework-owned
  `load_capability` tool and renders the catalog as a dynamic instruction that
  deliberately lists EVERY deferred capability every turn, including already-loaded
  ones, so the rendered prefix stays byte-identical and the prompt cache stays warm.
  Redundant loads are rejected with a cheap `ModelRetry` — the in-code comment: "one
  occasional wasted retry is far cheaper than busting the prefix cache on every load."
  Loaded state is resumable across runs via message history.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "prompt-cache-stability-as-correctness.md"
    rel: "extends"
  - file: "gpt-54-tool-search-deferred-tool-loading.md"
    rel: "same-problem"
  - file: "capability-as-agent-composition-primitive.md"
    rel: "extends"
  - file: "layered-prompt-assembly-stable-segment-caching.md"
    rel: "same-problem"
  - file: "disclosure-granularity-decision-rubric.md"
    rel: "same-problem"
  - file: "progressive-skill-loading.md"
    rel: "extends"
  - file: "prompt-caching-for-stable-agent-context.md"
    rel: "enabled-by"
  - file: "hub-and-spoke-two-tier-skill-taxonomy.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "context-engineering"
  - "prompt-caching"
  - "progressive-disclosure"
---

# Cache-Stable Progressive-Disclosure Catalog

## What It Is

A progressive-disclosure mechanism designed *around* cache economics. Deferred
capabilities are hidden behind a `load_capability` tool; their descriptions render as a
catalog inside a dynamic instruction. Two deliberate design choices make the catalog
cache-stable:

1. **The catalog never changes shape mid-session.** Every deferred capability is listed
   every turn — already-loaded ones included — so the rendered instruction prefix is
   byte-identical across turns and the provider prompt cache stays warm.
2. **Redundant loads are cheap, cache busts are not.** If the model calls
   `load_capability` on an already-loaded capability, the framework bounces it with a
   `ModelRetry` rather than mutating the catalog to remove the entry.

Loaded state persists in message history, so resumed runs recover which capabilities are
active without any catalog mutation. (`pydantic_ai_slim/pydantic_ai/capabilities/_deferred_capability_loader.py`)

## Why It Matters

Progressive disclosure and prompt caching are usually treated as separate optimizations,
and naive disclosure defeats caching: removing a loaded item from the catalog rewrites
the prefix and invalidates the cache every time the agent learns something. This is the
first watched-set example of a disclosure surface whose rendering contract is explicitly
subordinated to cache stability, with the trade-off priced in code comments (an
occasional wasted retry vs a per-load cache bust). The design rule generalizes to any
always-injected catalog surface: skill tables, tool indexes, deferred-tool lists.

## Why People Are Using It

Shipped in a top-tier production agent framework as the default disclosure mechanism for
deferred capabilities. Source: Observed in [pydantic-ai](https://github.com/pydantic/pydantic-ai)
v2.9.0 — see [[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Mutate the catalog on load** (drop loaded entries) — smaller prompt, but busts the
  prefix cache on every load; only wins when loads are rare and the catalog is huge.
- **Tool search over a flat catalog** (GPT-5.4-style deferred tool loading) — same
  disclosure goal at tool granularity, without a rendered catalog to keep stable.
- **Static full disclosure** — no catalog churn at all, at the cost of a permanently
  larger prefix.

## Potential Improvements

- Publishing measured cache-hit/cost deltas for catalog-stable vs catalog-mutating
  disclosure would turn the in-code assertion into transferable evidence.
- The same contract could extend to dynamic instructions generally: a linter that flags
  mid-session prefix mutations as cache hazards.

## Potential Failure Modes

- **Stale-entry confusion** — models may re-load listed-but-already-loaded capabilities
  repeatedly if the retry message is not explicit about state.
- **Catalog bloat** — byte-stability does not cap catalog size; hundreds of deferred
  entries still pay their description cost every turn.
- **Provider variance** — the win assumes prefix caching semantics; providers without
  prefix caches get the redundancy without the discount.
