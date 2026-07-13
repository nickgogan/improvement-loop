---
title: "Never Inline Ephemeral Turn State into Cached Prompt Layers"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "layered-prompt-assembly-stable-segment-caching"
extraction_date: "2026-05-25"
last_change_session: 146
last_change_report: "2026-07-13-source-drift"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "developers building agents or tools that make repeated Anthropic API calls within a session"
    - "prompt assembly modules that combine stable identity/memory/skill layers with dynamic per-turn state"
    - "teams deciding whether to enable prompt caching by default and where to place cache breakpoints"
  platform_coupling: "specific:anthropic-api"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — separating or recombining content blocks in a prompt assembly module is a structural change with no data migration cost"
  auditability: "high — cache hit/miss rates and cache-read vs. cache-write token counts are observable via API response usage fields; stable vs. ephemeral block boundaries are auditable in prompt assembly code"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Two independent production harnesses corroborate: Hermes agent (NousResearch) marks stable layers via a dedicated prompt_caching.py module; opencode ships caching default-on with an automatic breakpoint-placement heuristic and documented cache-write/read economics."
contract:
  preconditions: "The agent or tool makes repeated Anthropic API calls within a session. The prompt contains at least one segment that is stable across calls (identity, memory, skills) and at least one segment that changes per call (budget warnings, turn state, context pressure). The Anthropic API's prompt caching feature is available."
  invariants: "Stable segments (identity, persistent memory, skill definitions, project context) are assembled into cache-marked content blocks and placed before any ephemeral content. Ephemeral segments (budget warnings, context pressure hints, turn-specific state) are injected as separate, unmarked content blocks after cached blocks. No ephemeral content is inlined into or appended to a stable block. The cache breakpoint always sits at the deepest point of stability — never before a segment that is genuinely stable, never after a segment that changes per call. The caching boundary coincides with the stable/ephemeral structural boundary — not with the prompt structure boundary."
  governance: "Owner: the prompt assembly module or API call site. Stable vs. ephemeral classification of each prompt segment must be declared explicitly in the assembly module (not inferred at call time). Changes to segment classification require deliberate re-audit of cache hit rates. The five-minute Anthropic cache TTL means benefits only accrue for rapid multi-turn conversations — do not apply cache markers to segments in single-turn or long-gap workflows."
  recovery: "If cache invalidation is observed despite the rule being followed: audit the stable block contents for any dynamic content that slipped in (timestamps, session IDs, per-turn counts). If a stable segment changes legitimately (skill update, memory write): accept cache miss for that call; the penalty is a one-time re-write cost (~1.25x base input tokens for the changed prefix), not a structural problem. If over-caching causes stale context (old skill definitions, evicted memory): reduce the TTL assumption in design; consider treating semi-dynamic segments as ephemeral."
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

**Required:** Assemble the prompt as ordered content blocks. Place stable segments (identity, SOUL.md, MEMORY.md, USER.md, skill metadata, project context) in cache-marked blocks. Place ephemeral segments (budget warnings, context pressure hints, turn state) in separate, unmarked blocks after all cached content. The cache breakpoint must sit at the deepest stable point — the caching boundary coincides with the stable/ephemeral boundary.

**Forbidden:** Inlining ephemeral content (a budget warning, a per-turn counter, a dynamic status) into any block that carries a cache marker. Appending ephemeral content to the end of a stable block. Treating the prompt as a single string and applying a cache marker to the whole thing. Placing the cache breakpoint before a genuinely stable segment (which forfeits reusable prefix depth).

## Boundary

Enforced at the prompt assembly step — specifically, at the point where content blocks are constructed and cache markers are assigned. The rule does not govern what content goes into stable vs. ephemeral segments (that is a design decision); it governs the structural rule that once a segment is classified as ephemeral, it must not be inlined into a cached block, and that the breakpoint is anchored at the last stable segment.

## Enforcement

- **Mechanism:** The prompt assembly module maintains an explicit segment registry: each segment is classified as `stable` or `ephemeral` at definition time. Block construction reads from this registry — stable segments go into cache-marked blocks, ephemeral segments go into unmarked blocks. No mixed blocks.
- **Breakpoint anchors (opencode heuristic):** Auto-anchor cache breakpoints at the deepest reliably-stable boundaries — in a tool-using multi-turn agent, that means the last tool definition, the last stable system part, and (for read-reuse across turns) the latest user message. The cached prefix should always extend as deep as stability allows; the rule forbids any ephemeral segment from appearing before one of these anchors.
- **Check (deterministic):** For each content block: `(block.cache_control == "ephemeral") IMPLIES (all segments in block are classified stable)`. Any ephemeral-classified segment appearing in a cache-marked block is a violation.
- **Violation response:**
  - *Ephemeral content in cached block:* move the ephemeral segment to its own unmarked block; re-run the assembly.
  - *Unexpected cache misses despite compliance:* audit the stable block for dynamic content that bypassed classification (hardcoded timestamps, session IDs).
  - *Cache TTL exceeded:* this is expected, not a violation — the miss is bounded to one call.
- **Observable signal:** API response usage fields expose cache-read vs. cache-write token counts. A prompt that is compliant but produces persistent cache-write charges on the stable prefix indicates an undetected dynamic segment.

## Rationale

Prompt caching reduces cost and latency for repeated API calls by reusing the KV cache of a previously processed token prefix. The cache is invalidated whenever any token in the cached prefix changes. A single ephemeral value (a budget counter, a context pressure hint) inlined into a stable block causes the entire block's cache to invalidate on every call — eliminating the cost saving for all stable content that follows it.

The key insight from the Hermes agent (NousResearch): **decouple the caching boundary from the prompt structure boundary.** A well-structured prompt (identity → memory → skills → task → turn) does not automatically align caching boundaries with structural boundaries. The caching boundary must be set where content actually becomes dynamic, which may be mid-structure.

**Cross-harness corroboration — opencode (2026-07-12).** opencode ships prompt caching default-on, which quantifies why this rule pays off. Its cache-policy module documents the economics: a cache *write* costs roughly 1.25× the base input-token price, while a cache *read* costs roughly 0.1× — so a cached prefix breaks even once it is read about 1.4 times, a bar every multi-turn session clears. Inlining an ephemeral value into a stable block forfeits that ~0.9× per-read saving on *every* stable token that follows it, on every turn. opencode also resolves "where exactly does the marker go": its breakpoint-placement heuristic auto-anchors cache hints at the last tool definition, the last system part, and the latest user message, so the cached prefix always extends as deep as stability allows without per-feature opt-in. The rule's corollary follows directly — an ephemeral segment inlined ahead of any of those anchor points collapses the reusable prefix back to the point of the inlined change, converting cheap cache reads into full-price cache writes.

Ephemeral content that changes every turn has zero cache value — it cannot benefit from caching. Inlining it into stable blocks does not help the ephemeral content; it only harms the stable content by dragging it out of cache.

**Distinction from `never-ask-claude-to-compact-claudemd`:** That rule governs document maintenance — how CLAUDE.md files are updated (by humans, not by model compaction). This rule governs API prompt assembly — how stable and ephemeral segments are combined at call time. Different enforcement boundary: document editing vs. prompt construction.

## Failure Modes

- **Over-caching semi-dynamic content.** A segment that is "usually stable" (skill titles, project context) is cached, but changes mid-session after a skill update or memory write. Result: one call pays a cache-write (~1.25×) on the changed prefix. Mitigation: accept the occasional miss; design stable segments to be genuinely static within a session, not just usually static.
- **Under-caching genuinely stable content.** A segment is classified ephemeral out of caution, preventing cache reuse. Result: no cache benefit despite the content being identical across calls — every call pays full input price where a ~0.1× read would have served. Mitigation: audit cache-read vs. cache-write token counts; reclassify segments with consistently identical content as stable.
- **Breakpoint placed too shallow.** The cache marker is anchored before a segment that is in fact stable (e.g., on the identity layer when memory and skills are also stable). Result: the reusable prefix is shorter than it could be, leaving cheap reads on the table. Mitigation: anchor the breakpoint at the *last* stable segment, per the opencode heuristic.
- **Single-turn workflows gain nothing.** Caching benefits only accrue within the five-minute TTL window, and the first write costs ~1.25×. For single-turn or long-gap calls, the structural work of separating blocks adds complexity with net-negative payoff. Mitigation: apply this rule only to multi-turn or rapid-iteration workflows.
- **Ephemeral content slips in via template interpolation.** A template string like `"You have {budget} tokens remaining"` is placed inside a stable block. The variable changes every call. Mitigation: lint the stable block templates for any interpolated values before classifying them as stable.

## Contract

### Preconditions
The agent or tool makes repeated Anthropic API calls within a session. The prompt contains at least one segment that is stable across calls (identity, memory, skills) and at least one segment that changes per call (budget warnings, turn state, context pressure). The Anthropic API's prompt caching feature is available.

### Invariants
Stable segments (identity, persistent memory, skill definitions, project context) are assembled into cache-marked content blocks and placed before any ephemeral content. Ephemeral segments (budget warnings, context pressure hints, turn-specific state) are injected as separate, unmarked content blocks after cached blocks. No ephemeral content is inlined into or appended to a stable block. The cache breakpoint always sits at the deepest point of stability — never before a segment that is genuinely stable, never after a segment that changes per call. The caching boundary coincides with the stable/ephemeral structural boundary — not with the prompt structure boundary.

### Governance
Owner: the prompt assembly module or API call site. Stable vs. ephemeral classification of each prompt segment must be declared explicitly in the assembly module (not inferred at call time). Changes to segment classification require deliberate re-audit of cache hit rates. The five-minute Anthropic cache TTL means benefits only accrue for rapid multi-turn conversations — do not apply cache markers to segments in single-turn or long-gap workflows.

### Recovery
If cache invalidation is observed despite the rule being followed: audit the stable block contents for any dynamic content that slipped in (timestamps, session IDs, per-turn counts). If a stable segment changes legitimately (skill update, memory write): accept cache miss for that call; the penalty is a one-time re-write cost (~1.25x base input tokens for the changed prefix), not a structural problem. If over-caching causes stale context (old skill definitions, evicted memory): reduce the TTL assumption in design; consider treating semi-dynamic segments as ephemeral.
