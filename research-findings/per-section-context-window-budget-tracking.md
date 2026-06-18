---
name: Per-Section Context Window Budget Tracking
summary: Independent token accounting per prompt section (system instructions, memory blocks, conversation history, tool results) rather than aggregate per-turn tracking. Enables targeted compaction of the largest section rather than uniform compression, and makes context budgets debuggable.
implementation_notes: null
category: Context Engineering
evidence_strength: "Medium (practitioner-documented)"
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
related_findings:
- file: token-budget-pre-turn-projection.md
  rel: extends
- file: context-usage-status-line-visual-budget-tracking.md
  rel: extends
pipeline_status: raw
---

# Per-Section Context Window Budget Tracking

## What It Is

A context management architecture where token consumption is tracked independently for each logical section of the prompt — system instructions, core memory blocks, memory filesystem, tool rules, directory listings, conversation summary, function definitions, and message history — rather than as a single aggregate count. The `ContextWindowOverview` structure provides complete per-section accounting, enabling the system to identify which section is consuming the most budget and apply targeted compaction only where needed rather than compressing everything uniformly.

## Why It Matters

Aggregate token tracking treats all context equally, forcing uniform compression when limits are hit. This destroys high-value sections (like recent conversation) to save space occupied by low-churn sections (like system instructions). Per-section tracking makes the budget visible and actionable: if memory blocks are consuming 40% of the window, compact memory; if conversation history is the bottleneck, summarize old turns. It transforms context management from a blunt instrument into a precision tool.

## Why People Are Using It

Observed in [Letta](https://github.com/letta-ai/letta) v0.16.8 — see [[letta-analysis]] for structural details. The system implements a dedicated `services/context_window_calculator/` service that computes token usage per section and exposes it as a structured `ContextWindowOverview` object, used to drive compaction decisions and enforce per-section limits.

## Potential Alternatives

Single aggregate token counter with proportional compression (simpler but wasteful). Fixed allocation per section regardless of actual usage (predictable but inflexible). Dynamic allocation with priority ordering where high-priority sections get budget first (respects importance but harder to implement).

## Potential Improvements

Historical budget tracking across turns to detect trends (e.g., memory blocks growing faster than expected). Predictive budget projection that estimates whether the next turn will overflow before it happens. User-configurable section priorities that determine which sections get compressed first when the aggregate limit is reached.

## Potential Failure Modes

Per-section tracking adds computational overhead to every turn (tokenization is not free). Section boundaries may not align with semantic boundaries, causing splits at awkward points. Over-optimizing one section's budget can starve others — a section that looks small in tokens may be disproportionately important. The accounting can become inconsistent if tools modify context outside the tracked sections.
