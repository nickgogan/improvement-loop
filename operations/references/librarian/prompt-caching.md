---
term: prompt-caching
type: concept
variants: []
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "claude"
stage: "draft"
tags:
  - "librarian-concept"
  - "prompt-caching"
  - "cost"
aliases:
  - "Prompt caching"
  - "Cache hit"
  - "Stable context caching"
---

# Prompt Caching

## Short definition

**Prompt caching** is a harness-level mechanism that stores the cacheable prefix of a prompt (system prompt, tool definitions, persona instructions, stable reference material) and reuses it across calls at a reduced per-token cost. Cache hits on Claude Opus cost $0.50/M versus $5/M standard — 90% savings (G2b §Token Cost Defense). The mechanism requires that cached content is *exactly identical* across calls: a single character change to cached content forces a full-price re-read of the entire cached block.

Single referent. No variants. The adjacent concept "what *is* stable context" is an authoring discipline (see `context-rot.md` §Defenses and G2a §Curation Discipline); caching is the mechanism that rewards that discipline.

## Not to be confused with

| Not prompt caching | What it is instead |
|---|---|
| **Context window** | The model-side input. Caching is a harness-side optimization over what's *in* the context. See `context-rot.md` and G2b §Key Concepts. |
| **Memory** | Persistent store across turns / sessions with a read/write policy. Cache is stateless from the agent's perspective — the model does not "remember," the harness re-supplies. See `memory.md`. |
| **RAG / retrieval** | A retrieval pattern that fetches content at query time. Caching shortens the delivery cost of whatever content the harness prepends; it does not decide *what* gets prepended. |
| **Second brain** | A knowledge surface. Caching is a billing optimization, not a knowledge surface. |
| **Context budget** | The authoring discipline for deciding what belongs in context. Caching is downstream of the budget — cache what the budget decided to include. |

## Mechanism

Two forces make caching load-bearing:

1. **Cost arithmetic.** Cache hits on Claude Opus cost $0.50/M vs $5/M standard — a 10× reduction on the cached portion. For long, stable prefixes (multi-thousand-token system prompts, comprehensive tool definitions, large persona / reference content), this compounds across every call in a session.
2. **Cache invalidation is all-or-nothing.** The cache is keyed by exact prefix match. Any character change — a whitespace edit, a date substitution, a reordered line — invalidates the block and forces a full-price re-read (G2b §Pitfalls). The discipline is therefore: *stabilize content before caching, then leave it alone*.

## Composition

Substrate pointers. Smaller table than variant-carrying concepts because the substrate is tightly clustered in G2b (degradation defense) and G2a (structuring).

| Aspect | Tier 1 (guides, default) | Tier 2 (patterns / findings) | Tier 3 (watched-libraries) |
|---|---|---|---|
| Mechanism / pricing math | G2b §Token Cost Defense, §Contract item "Stable context is cached" | `prompt-caching-for-stable-agent-context` | Anthropic prompt caching docs |
| Stable vs volatile content | G2a §Key Concepts, §Tiered and Progressive Loading | Patterns on tiered context loading, CLAUDE.md discipline | — |
| Cache invalidation failure mode | G2b §Pitfalls ("check for cache invalidation — any character change forces full-price re-read") | — | Anthropic caching error-mode docs |
| Front-loading cacheable content | G2b §Token Cost Defense ("Structure prompts to front-load cacheable content before dynamic content") | Patterns on prompt structure for cache hits | Anthropic SDK cookbook — prompt-caching examples |
| Hidden cost amplifier (reasoning-token inflation) | G2b §Detecting Context Degradation (reasoning token overhead) | — | — |
| Cache-hit monitoring | G2a §Templates §Context Budget, audit checkbox "Cache hit rates are monitored" | — | — |

## Librarian read rule

**Default (Tier 1).** For `(explain, prompt-caching)` queries (UC-6.3: "why does prompt caching reduce cost so dramatically?"), read G2b §Token Cost Defense (mechanism + pricing math). The section carries both cost arithmetic and the stable-content discipline.

**Escalate to Tier 2 when:**
- Consumer is tuning cache hit rates — pull `prompt-caching-for-stable-agent-context` for practitioner specifics beyond the G2b summary.

**Escalate to Tier 3 when:**
- Consumer asks about SDK-level specifics (cache-control parameters, `cache_control` block placement, streaming behavior under caching) — Anthropic docs are authoritative.
- Consumer is comparing caching behavior across harnesses (Claude Code vs raw API vs Cursor).

**Do not:**
- Treat caching as a memory substitute. Cache resets with any content change; memory has policy gates and retention. See `memory.md`.
- Recommend caching without first establishing that the cacheable content *is* stable. Caching volatile content is a net loss — the churn cost exceeds the hit savings.
- Skip the cache-invalidation Pitfall when a consumer reports "token costs spiked." That is G2b's diagnostic recovery pointer.

## Provenance surfacing

Tier-1 citations: `<guide>.md#<anchor>` with line-range appendix until the section manifest lands. Tier-2 citations: finding file path + slug. Tier-3 citations: Anthropic doc URLs / watched-lib paths. Pricing figures should always cite G2b §Token Cost Defense (not restated as Librarian assertion) — prices change and the substrate is the source of truth, not the Librarian's memory.

## Cross-references

- Related concepts: `context-rot.md` (stabilizing content is the authoring discipline that makes caching pay off), `harness.md` (caching is harness-implemented), `memory.md` (what caching is *not*).
- Related operations: `explain.md` (primary consumer — UC-6.3), `audit.md` (G2b Contract item "Stable context is cached" fires as an audit check for any prompt that embeds stable context).
- Use-case registry (UC-6.3): `operations/references/librarian/use-case-registry.md`.
- Governing DDs: DD-78 (Contract triple-role — G2b Contract's caching invariant is an emergent audit criterion).
