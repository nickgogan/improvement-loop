---
name: "Cache-Safe Compaction — Fork with Identical Prefix and Reserved Buffer"
summary: |-
  Naive compaction (a separate summarization call with its own system prompt and no tools) pays
  full price to re-read the whole conversation because its prefix diverges immediately. Claude
  Code instead forks the conversation with the exact same system prompt, context, and tool
  definitions, appending only the compaction request — so the entire parent conversation is a
  cache hit and marginal cost scales with the compaction prompt, not conversation length. A
  reserved "compaction buffer" in the context window guarantees room for the summary output.
implementation_notes: |-
  Relevant wherever we design compaction/summarization into long-running agents: (1) the
  summarizer call must replicate the parent's prefix byte-for-byte (system prompt, session
  context, tools) and add the summarization instruction as a new appended user message; (2)
  reserve a fixed output buffer below the context ceiling so compaction can always run before
  overflow; (3) note that the Claude API now offers native compaction built on these learnings —
  prefer the native mechanism when available instead of hand-rolling.
category: "Context Engineering"
evidence_strength: "Strong (production-tested, first-party)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "claude-code-prompt-caching-is-everything.md"
related_findings: []
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
---

## What It Is

Claude Code's compaction mechanic. When the context window fills, the harness must summarize the conversation to continue. The naive design — fire a separate API call with a summarizer system prompt and no tools — gets zero cache hits: its prefix differs from the parent conversation at token one, so the provider re-processes the entire transcript at full input price. Cache-safe forking instead constructs the compaction request as a child of the live conversation: identical system prompt, user/session context, and tool definitions, all parent messages prepended, and the compaction instruction appended as one new user message. Everything except the compaction prompt is served from cache. A reserved compaction buffer — headroom deliberately kept free within the context window — ensures the summary has space to be generated before the window actually overflows.

## Why It Matters

Compaction happens precisely when the conversation is at its longest, i.e., when a cache miss is at its most expensive. Cache-safe forking turns compaction's marginal cost from O(conversation length) to O(compaction prompt) — the difference between compaction being a routine background operation and a cost spike at the worst moment. The buffer detail matters equally: without reserved headroom, the harness can reach a state where it needs to compact but no longer has room to.

## Why People Are Using It

First-party production design in Claude Code. The post notes that compaction is now available natively in the Claude API based on these learnings, which both validates the pattern and gives builders a managed path to it.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Native API compaction | Let the provider compact server-side | Whenever available — it embodies this pattern without client effort |
| Fresh-session handoff | Write a handoff document and start a new session | Natural task boundaries; also resets accumulated noise (our /session-handoff pattern) |
| Truncation | Drop oldest messages without summarizing | Low-stakes sessions where early context is genuinely disposable |

## Potential Improvements

- Fold into our harness-design guidance alongside append-only updates and static tool sets as the third leg of prefix discipline
- Compare against our session-handoff practice: handoff-to-fresh-session and cache-safe compaction solve overlapping problems with different freshness/cost tradeoffs

## Potential Failure Modes

- **Prefix drift bugs:** any accidental difference between parent and fork prefixes (ordering, timestamps) silently reverts to full-price compaction
- **Buffer sizing:** too small a reserved buffer truncates summaries; too large wastes usable context every turn
- **Summary quality is unchanged:** cache-safety fixes the cost of compaction, not the lossiness — critical constraints can still fall out of the summary
