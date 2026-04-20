---
name: Memory Decay/Compaction Is Converging on Multi-Strategy Approaches
summary: 'Three repos address context compaction with semantically-aware strategies beyond simple truncation: OpenViking (two-threshold), Paperclip (weekly synthesis + decay), DeerFlow (async summarization). Each solves a different facet of the same problem. Note: Beads was previously listed here as "semantic decay" — Beads is actually an issue-based agent orchestration system, not a compaction strategy.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: semantic-memory-decay-compaction.md
  rel: extends
- file: two-threshold-compaction-strategy.md
  rel: extends
- file: five-context-management-techniques-in-claude-code.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: context-rot-attention-budget-depletion.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
- file: dreaming-memory-consolidation.md
  rel: same-problem
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
---

## What It Is

A cross-repo convergence observation: three repos independently implement semantically-aware compaction — going beyond FIFO/sliding-window to use importance scoring, thresholds, or summarization to decide what survives. Each implementation solves a different facet:
- **OpenViking**: When to compact — dual thresholds (50% async archive, 70% forced clear)
- **Paperclip**: How often to consolidate — weekly synthesis cycles with decay rules
- **DeerFlow**: Where to persist — per-thread async summarization via MemoryMiddleware

Note: Beads (Yegge) was previously attributed here as "semantic decay / what to keep." This was a misattribution from repo analysis. Beads is an issue-based agent orchestration system — it replaces markdown plan hierarchies with git-backed JSONL issue graphs. Its contribution to the memory/coordination space is issue-scoped session atomicity, not compaction strategy. See [[issue-based-agent-orchestration-replacing-markdown-plans.md]].

## Why It Matters

The community has collectively learned that naive compaction (truncation, FIFO) loses too much valuable context. All three implementations use semantic understanding — LLM-based summarization or importance scoring — to make intelligent retention decisions. A complete solution would combine all three observed facets: threshold-triggered timing (when), periodic consolidation (how often), and scoped persistence (where).

## Why People Are Using It

Cross-repo observation across 14 analyzed repos — see [[cross-repo-comparison]] for structural details. Observed in [OpenViking](https://github.com/volcengine/OpenViking), [Paperclip](https://github.com/nicholasgriffintn/paperclip), and [DeerFlow](https://github.com/bytedance/deer-flow). Beads removed from this list — it is an issue-based orchestration system, not a compaction strategy (see [[issue-based-agent-orchestration-replacing-markdown-plans.md]]).

## Potential Alternatives

- Simple FIFO compaction (drop oldest)
- Sliding window with fixed token budget
- Manual compaction (user-triggered)

## Potential Improvements

Combine all three observed facets into a unified compaction architecture: dual thresholds decide when → periodic consolidation sweeps → scoped storage persists. The "what to keep" dimension (importance scoring) is the missing piece not yet observed in any of these repos.

## Potential Failure Modes

- Summary quality is the bottleneck — bad summaries lose information permanently
- Multiple strategies add complexity and debugging difficulty
- Threshold values need per-use-case tuning
