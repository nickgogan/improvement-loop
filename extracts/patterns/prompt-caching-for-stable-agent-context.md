---
title: "Prompt Caching for Stable Agent Context"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "prompt-caching-for-stable-agent-context"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "An agent system makes repeated API calls with stable context elements (system prompts, tool definitions, persona instructions). The API provider supports prompt caching. The stable context portion is large enough that caching provides meaningful cost reduction."
  invariants: "Cacheable content is placed before dynamic content in the message array. Cached content position and byte content are identical across requests. Cache hit rates are monitored to validate the optimization is active."
  governance: "Context element stability is assessed before marking content as cacheable. Cache-breaking changes (prompt edits, tool definition updates) are batched to minimize cache invalidation frequency. Cache hit rate metrics are reviewed periodically."
  recovery: "If cache hit rates drop unexpectedly, audit recent changes to cached content blocks for unintended modifications. If prompt iteration during development negates caching benefits, defer caching activation until prompts stabilize."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Prompt Caching for Stable Agent Context

**Source:** [[prompt-caching-for-stable-agent-context]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems that make repeated API calls re-send the same stable context -- system prompts, tool definitions, persona instructions, reference material -- on every turn. Each turn pays full input token cost to re-process content that has not changed. For heavy agent usage, this redundancy dominates the token budget and accelerates rate limit exhaustion.

## Forces

- **Cost vs. simplicity:** Sending everything on every turn is simple to implement but expensive. Caching reduces cost but adds ordering constraints and invalidation concerns.
- **Iteration speed vs. cache stability:** During active prompt development, frequent edits invalidate the cache and negate the cost benefit. Caching is most valuable after prompts stabilize, but teams want savings during development too.
- **Context ordering flexibility vs. cache requirements:** Cached content must appear in the same position in the message array across requests. This constrains how context can be structured and reordered.
- **Monitoring overhead vs. silent failure:** Without cache hit rate monitoring, the optimization can silently stop working (due to content drift or ordering changes) and no one notices.

## Solution

Separate agent context into stable and dynamic elements, then cache the stable portion:

**1. Classify context elements by stability:**
- **Stable (cacheable):** System prompts, tool definitions, persona instructions, reference documentation, rules, schemas -- content that does not change between turns
- **Dynamic (not cacheable):** Conversation history, user input, per-turn state, intermediate results

**2. Structure messages to front-load cacheable content:**
- Place all stable context elements at the beginning of the message array
- Place dynamic content (conversation history, current user input) after the cached block
- This ordering is required by most caching implementations -- cached content must appear in the same position with identical bytes

**3. Enable caching via the API:**
- For Anthropic: use the prompt caching beta header; mark stable content blocks with cache control directives
- Cache hits on Claude Opus cost $0.50/M tokens vs. $5.00/M standard input -- a 90% cost reduction per cached token
- If 80% of input tokens are stable context, the effective input cost drops by approximately 72%

**4. Monitor cache hit rates:**
- Track cache hit/miss rates per request to confirm the optimization is active
- Alert on cache hit rate drops -- these indicate unintended content changes or ordering shifts
- Validate after any prompt, tool definition, or schema update

**Key constraint:** Even a single character change to cached content forces a full-price re-read of the entire block. Batch prompt edits rather than making incremental changes. Defer caching activation during heavy prompt iteration phases.

## Consequences

**Positive:**
- 90% cost reduction on cached input tokens (Opus: $0.50/M vs. $5.00/M)
- Approximately 72% effective input cost reduction when 80% of tokens are stable context
- Extends session budgets and delays rate limit exhaustion for heavy agent usage
- Described as "lowest effort, highest impact optimization" -- minimal implementation complexity for large savings
- No quality impact -- the model receives identical context, just served from cache

**Negative:**
- Cache invalidation on any content change forces full-price re-processing of the entire cached block
- Ordering dependency: reordering context elements breaks cache hits silently
- Low cache hit rates during active prompt development phases make the optimization irrelevant until prompts stabilize
- Adds a monitoring requirement -- without cache hit rate tracking, silent failures go undetected
- Provider-specific implementation details (API headers, cache control syntax) reduce portability

## Known Uses

- Nate B Jones describes this as the "lowest effort, highest impact optimization" for agent cost management
- Claude Code (Anthropic) uses prompt caching for system prompts, tool definitions, and CLAUDE.md context
- Production agent systems with stable personas and tool sets report 60-80% cost reductions on input tokens
- MetaSystem's Claude Build system qualifies for caching: stable system prompts, tool definitions, and persona instructions across repeated skill invocations

## Contract

### Preconditions
An agent system makes repeated API calls with stable context elements (system prompts, tool definitions, persona instructions, reference material). The API provider supports prompt caching (e.g., Anthropic prompt caching beta). The stable context portion is large enough relative to total input tokens that caching provides meaningful cost reduction (rule of thumb: stable content should be at least 50% of input tokens).

### Invariants
Cacheable content is placed before dynamic content in the message array -- this ordering is maintained across all requests. Cached content position and byte content are identical across requests; any divergence breaks the cache. Cache hit rates are monitored and tracked as a system health metric. The model receives identical context regardless of whether it is served from cache or re-processed -- caching is a cost optimization, not a content optimization.

### Governance
Context element stability is assessed before marking content as cacheable -- only content that genuinely does not change between turns is cached. Cache-breaking changes (prompt edits, tool definition updates, schema modifications) are batched to minimize cache invalidation frequency. Cache hit rate metrics are reviewed after any change to cached content blocks. During active prompt development phases, caching may be deferred until prompts stabilize -- this is a valid operational choice, not a failure.

### Recovery
If cache hit rates drop unexpectedly: audit recent changes to cached content blocks for unintended modifications (whitespace changes, reordering, version bumps). Restore identical content and ordering to re-establish cache hits. If prompt iteration during development negates caching benefits, accept the higher cost during the iteration phase and re-enable caching once prompts stabilize. If the API provider changes caching behavior or pricing, re-evaluate whether the optimization is still cost-effective and adjust accordingly.
