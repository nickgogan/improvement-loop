---
name: Prompt Caching for Stable Agent Context
summary: Cache system prompts, tool definitions, persona instructions, and reference material. Cache hits on Opus cost $0.50/M vs $5/M standard — a 90% discount. Called 'lowest effort, highest impact optimization'
  by Nate B Jones.
implementation_notes: Enable prompt caching for all stable context elements (system prompts, tool definitions, persona instructions). Requires Anthropic API beta header.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in:
- S3 (Claude Code Build)
sources:
- your-claude-limit-burns-in-90-minutes.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- defending-agent-context.md
related_findings:
- file: prompt-cache-stability-as-correctness.md
  rel: extended-by
- file: cache-stable-progressive-disclosure-catalog.md
  rel: enables
---

## What It Is

Prompt caching is an Anthropic API feature that stores frequently reused context (system prompts, tool definitions, persona instructions, reference material) so subsequent requests serve from cache instead of re-processing. Cache hits on Claude Opus cost $0.50/M tokens vs $5/M standard input — a 90% cost reduction.

## Why It Matters

For agent systems that make repeated calls with stable context (which is most of them), the majority of input tokens are identical across turns. Without caching, every turn pays full price to re-read the same system prompt, tool definitions, and persona instructions. This is the single highest-leverage cost optimization for repeated agent calls.

## Why People Are Using It

Nate B Jones calls this the "lowest effort, highest impact optimization." The math is straightforward: if 80% of your input tokens are stable context and you cache them, your effective input cost drops by ~72%. For heavy agent users hitting rate limits, this extends session budgets dramatically.

## Potential Improvements

- Audit all context elements to identify which are truly stable (system prompt, tool defs, persona) vs which change per turn (conversation history, user input)
- Structure prompts to front-load cacheable content before dynamic content
- Monitor cache hit rates to validate the optimization is working

## Potential Failure Modes

- **Cache invalidation on any change:** Even a single character change to cached content forces a full-price re-read of the entire block. Frequent prompt iteration during development negates the benefit.
- **Ordering dependency:** Cached content must appear in the same position in the message array. Reordering context elements breaks cache hits.
- **False economy during iteration:** Heavy prompt development phases may see low cache hit rates, making the optimization irrelevant until prompts stabilize.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[prompt-caching-for-stable-agent-context.md]] in `extracts/patterns/`
