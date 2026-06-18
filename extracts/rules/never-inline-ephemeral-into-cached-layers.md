---
title: "Never Inline Ephemeral Turn State into Cached Prompt Layers"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "layered-prompt-assembly-stable-segment-caching"
extraction_date: "2026-05-25"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "developers building agents or tools that make repeated Anthropic API calls within a session"
    - "prompt assembly modules that combine stable identity/memory/skill layers with dynamic per-turn state"
  platform_coupling: "specific:anthropic-api"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — separating or recombining content blocks in a prompt assembly module is a structural change with no data migration cost"
  auditability: "high — cache hit/miss rates are observable via API response headers; stable vs. ephemeral block boundaries are auditable in prompt assembly code"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agent or tool makes repeated Anthropic API calls within a session. The prompt contains at least one segment that is stable across calls (identity, memory, skills) and at least one segment that changes per call (budget warnings, turn state, context pressure). The Anthropic API's prompt caching feature is available."
  invariants: "Stable segments (identity, persistent memory, skill definitions, project context) are assembled into cache-marked content blocks and placed before any ephemeral content. Ephemeral segments (budget warnings, context pressure hints, turn-specific state) are injected as separate, unmarked content blocks after cached blocks. No ephemeral content is inlined into or appended to a stable block. The caching boundary coincides with the stable/ephemeral structural boundary — not with the prompt structure boundary."
  governance: "Owner: the prompt assembly module or API call site. Stable vs. ephemeral classification of each prompt segment must be declared explicitly in the assembly module (not inferred at call time). Changes to segment classification require deliberate re-audit of cache hit rates. The five-minute Anthropic cache TTL means benefits only accrue for rapid multi-turn conversations — do not apply cache markers to segments in single-turn or long-gap workflows."
  recovery: "If cache invalidation is observed despite the rule being followed: audit the stable block contents for any dynamic content that slipped in (timestamps, session IDs, per-turn counts). If a stable segment changes legitimately (skill update, memory write): accept cache miss for that call; the penalty is a one-time miss, not a structural problem. If over-caching causes stale context (old skill definitions, evicted memory): reduce the TTL assumption in design; consider treating semi-dynamic segments as ephemeral."
tags:
  - "extracted-artifact"
  - "rule"
  - "prompt-engineering"
  - "caching"
  - "context-engineering"
---

# Never Inline Ephemeral Turn State into Cached Prompt Layers

**Source:** [[layered-prompt-assembly-stable-segment-caching]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent or tool makes repeated Anthropic API calls within a session. The system prompt is assembled from multiple components: stable layers (identity, persistent memory, skill definitions, project context) that rarely or never change within the session, and ephemeral layers (budget warnings, context pressure hints, turn-specific state) that change on every call.

Applies when the Anthropic prompt caching feature is in use or being considered for use.

Scope: **Anthropic API prompt assembly only.** Prompt caching mechanics are API-specific; the structural principle (separate stable from dynamic) is generalizable, but the cache marker mechanism is Anthropic-specific.

## Action

**Required:** Assemble the prompt as ordered content blocks. Place stable segments (identity, SOUL.md, MEMORY.md, USER.md, skill metadata, project context) in cache-marked blocks. Place ephemeral segments (budget warnings, context pressure hints, turn state) in separate, unmarked blocks after all cached content. The caching boundary must coincide with the stable/ephemeral boundary.

**Forbidden:** Inlining ephemeral content (a budget warning, a per-turn counter, a dynamic status) into any block that carries a cache marker. Appending ephemeral content to the end of a stable block. Treating the prompt as a single string and applying a cache marker to the whole thing.

## Boundary

Enforced at the prompt assembly step — specifically, at the point where content blocks are constructed and cache markers are assigned. The rule does not govern what content goes into stable vs. ephemeral segments (that is a design decision); it governs the structural rule that once a segment is classified as ephemeral, it must not be inlined into a cached block.

## Enforcement

- **Mechanism:** The prompt assembly module maintains an explicit segment registry: each segment is classified as `stable` or `ephemeral` at definition time. Block construction reads from this registry — stable segments go into cache-marked blocks, ephemeral segments go into unmarked blocks. No mixed blocks.
- **Check (deterministic):** For each content block: `(block.cache_control == "ephemeral") IMPLIES (all segments in block are classified stable)`. Any ephemeral-classified segment appearing in a cache-marked block is a violation.
- **Violation response:**
  - *Ephemeral content in cached block:* move the ephemeral segment to its own unmarked block; re-run the assembly.
  - *Unexpected cache misses despite compliance:* audit the stable block for dynamic content that bypassed classification (hardcoded timestamps, session IDs).
  - *Cache TTL exceeded:* this is expected, not a violation — the miss is bounded to one call.
- **Observable signal:** API response headers expose cache hit/miss. A prompt that is compliant but produces persistent misses on the stable block indicates an undetected dynamic segment.

## Rationale

Prompt caching reduces cost and latency for repeated API calls by reusing the KV cache of a previously processed token prefix. The cache is invalidated whenever any token in the cached prefix changes. A single ephemeral value (a budget counter, a context pressure hint) inlined into a stable block causes the entire block's cache to invalidate on every call — eliminating the cost saving for all stable content that follows it.

The key insight from the Hermes agent (NousResearch): **decouple the caching boundary from the prompt structure boundary.** A well-structured prompt (identity → memory → skills → task → turn) does not automatically align caching boundaries with structural boundaries. The caching boundary must be set where content actually becomes dynamic, which may be mid-structure.

Ephemeral content that changes every turn has zero cache value — it cannot benefit from caching. Inlining it into stable blocks does not help the ephemeral content; it only harms the stable content by dragging it out of cache.

**Distinction from `never-ask-claude-to-compact-claudemd`:** That rule governs document maintenance — how CLAUDE.md files are updated (by humans, not by model compaction). This rule governs API prompt assembly — how stable and ephemeral segments are combined at call time. Different enforcement boundary: document editing vs. prompt construction.

## Failure Modes

- **Over-caching semi-dynamic content.** A segment that is "usually stable" (skill titles, project context) is cached, but changes mid-session after a skill update or memory write. Result: one call sends stale context. Mitigation: accept the occasional miss; design stable segments to be genuinely static within a session, not just usually static.
- **Under-caching genuinely stable content.** A segment is classified ephemeral out of caution, preventing cache reuse. Result: no cache benefit despite the content being identical across calls. Mitigation: audit cache hit rates; reclassify segments with consistently identical content as stable.
- **Single-turn workflows gain nothing.** Caching benefits only accrue within the five-minute TTL window. For single-turn or long-gap calls, the structural work of separating blocks adds complexity with no payoff. Mitigation: apply this rule only to multi-turn or rapid-iteration workflows.
- **Ephemeral content slips in via template interpolation.** A template string like `"You have {budget} tokens remaining"` is placed inside a stable block. The variable changes every call. Mitigation: lint the stable block templates for any interpolated values before classifying them as stable.

## Contract

### Preconditions
The agent or tool makes repeated Anthropic API calls within a session. The prompt contains at least one segment that is stable across calls (identity, memory, skills) and at least one segment that changes per call (budget warnings, turn state, context pressure). The Anthropic API's prompt caching feature is available.

### Invariants
Stable segments (identity, persistent memory, skill definitions, project context) are assembled into cache-marked content blocks and placed before any ephemeral content. Ephemeral segments (budget warnings, context pressure hints, turn-specific state) are injected as separate, unmarked content blocks after cached blocks. No ephemeral content is inlined into or appended to a stable block. The caching boundary coincides with the stable/ephemeral structural boundary — not with the prompt structure boundary.

### Governance
Owner: the prompt assembly module or API call site. Stable vs. ephemeral classification of each prompt segment must be declared explicitly in the assembly module (not inferred at call time). Changes to segment classification require deliberate re-audit of cache hit rates. The five-minute Anthropic cache TTL means benefits only accrue for rapid multi-turn conversations — do not apply cache markers to segments in single-turn or long-gap workflows.

### Recovery
If cache invalidation is observed despite the rule being followed: audit the stable block contents for any dynamic content that slipped in (timestamps, session IDs, per-turn counts). If a stable segment changes legitimately (skill update, memory write): accept cache miss for that call; the penalty is a one-time miss, not a structural problem. If over-caching causes stale context (old skill definitions, evicted memory): reduce the TTL assumption in design; consider treating semi-dynamic segments as ephemeral.
