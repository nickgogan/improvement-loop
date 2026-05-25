---
name: "Proactive Compaction Before Intelligence Degradation"
summary: "Anthropic argues /compact should be invoked proactively — early, while the model is still sharp — rather than reactively at the context hard cutoff. Rationale: 'model is at its least intelligent point when compacting.' A 1M context window is not a license to defer compaction indefinitely; it's time to compact well. The autocompact fallback produces worse summaries precisely because it fires when the model has the least headroom. This reframes compaction as a quality-of-summary decision, not just a capacity-management decision."
implementation_notes: "Directly counters the instinct to defer /compact until context is nearly full. In long-running sessions, consider /compact checkpoints at natural task boundaries well before capacity pressure. For autonomous harnesses, this is a strong argument against waiting for context pressure to drive compaction — schedule it at stable state, not under load."
category: "Context Engineering"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-claude-code-session-management-1m-context.md"
related_findings:
  - file: two-threshold-compaction-strategy.md
    rel: extends
  - file: claude-code-context-management-decision-matrix-five-tools.md
    rel: same-problem
  - file: work-disavowal-failure-mode-context-limit-cheating.md
    rel: same-problem
  - file: context-rot-silent-killer-and-mitigations.md
    rel: same-problem
  - file: memory-decay-compaction-convergence.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
  - "rules/context-degradation-40-percent-threshold.md"
---

## What It Is

An explicit Anthropic recommendation to run `/compact <hint>` **before** context pressure forces it, with the rationale quoted verbatim: **"model is at its least intelligent point when compacting."**

The argument structure:
1. Autocompaction fires at the context hard cutoff — when attention is spread thinnest across the most tokens.
2. At that moment, the model's summary quality is at its worst.
3. A larger context window (the 1M expansion) does not reduce this pressure — it only defers it, which makes the eventual compaction even worse because there's more to summarize.
4. Therefore: compact proactively. Pick a stable checkpoint (task boundary, post-test-pass, after a successful file read sequence), invoke `/compact` with a steering hint, and do it while the model is still sharp.

Related point from the same article: "Bad compacts can happen when the model can't predict the direction your work is going." A proactive `/compact` timed at a moment when direction is clear produces a better summary than an auto-compact at an ambiguous midpoint.

## Why It Matters

The default user mental model is that `/compact` is a fallback — something to reach for when context is about to overflow. This finding inverts that: `/compact` is a regular-cadence tool, best invoked at points of maximum clarity, not maximum pressure.

For long-running agent harnesses, this has operational implications:
- **Schedule compaction at stable state**, not at capacity triggers.
- **Instrument for "direction confidence"** — if the agent can predict the next phase of work, compact now.
- **Don't let 1M tokens lull you** into thinking compaction isn't needed — it's still needed, just later, and the later it fires, the worse the summary.

## Why People Are Using It

Source: Anthropic product blog, April 15, 2026 (Thariq Shihipar). Explicit Anthropic product recommendation. Complements existing cross-repo evidence in [[memory-decay-compaction-convergence.md]] that semantically-aware compaction outperforms naive truncation.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Reactive /compact at autocompact trigger | Let the system compact when capacity fills | For short sessions where proactive scheduling overhead isn't worth it |
| /clear at task boundaries | Start a fresh session with a hand-written brief | When you can write a better summary than the model can |
| Two-threshold async archive | Background archive at 50%, force-clear at 70% (see OpenViking) | When you need archival without summary loss |

## Potential Improvements

- **Direction-confidence heuristic** — explicit signals that indicate the model is clear on next steps (unambiguous test results, successful tool calls, user-confirmed plan). Trigger proactive compact off these.
- **Compact-hint library** — standard hint templates for common session shapes ("compact everything except the current file and the bug I'm chasing").
- **Automatic compact-then-rewind sequence** — compact the current state, then use the compacted summary as a new `/rewind` target.

## Potential Failure Modes

- **Over-compaction** — compacting too often loses detail; the user ends up in a summary of a summary of a summary.
- **Compact at wrong moment** — the user proactively compacts at what feels like a boundary, but actually discarded load-bearing context.
- **Hint quality determines summary quality** — without a good `<hint>`, proactive compact is no better than autocompact.
- **Not compatible with fully autonomous agents** — who decides the "stable state" moment? The model that is about to lose context when it compacts?
