---
name: Context-Order Diversity for Bug Detection
summary: Bugs can be made visible or invisible by the order in which code is loaded into an LLM's context window. Intentionally diversifying traversal entry points across parallel sub-agents ensures that
  no single ordering bias hides a real bug.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-ultra-review-multi-agent-verification.md
related_findings:
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: extends
- file: context-pollution-same-window-verification-bias.md
  rel: same-problem
- file: subagent-exploration-mode-parallel-codebase-mappi.md
  rel: same-problem
- file: fork-subagent-parallel-trajectory-exploration.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: holdout-validation-pattern-blind-regression.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---
# Context-Order Diversity for Bug Detection

## What It Is
When an LLM reviews code, the order in which files and code sections are loaded into its context window affects what it can see. A bug may be clearly visible when file A is loaded before file B, but hidden when the order is reversed — because the model's attention and reasoning are shaped by what came first. Claude Code's Ultra Review exploits this by spinning up multiple sub-agents that each begin at a different position in the codebase and follow different traversal paths. Each sub-agent effectively sees the same code through a different "lens," making different bugs salient.

The key insight: context ordering is not neutral. It is a variable that, when diversified across parallel agents, functions as a coverage mechanism. The same logic applies to any multi-agent code analysis task — not just bug hunting.

## Why It Matters
Single-agent or single-traversal review has a systematic blind spot: whatever the traversal order obscures will stay obscured. This is a structural limitation of how LLMs process sequential context, not a model quality issue. Throwing more compute at the same traversal order yields diminishing returns. Diversifying entry points yields orthogonal coverage — each agent's blind spots are different, so their union covers more ground.

## Why People Are Using It
Anthropic built this directly into Ultra Review (the "Bug Hunter" feature), where five sub-agents (default fleet size, max 20) each start from a different codebase position. The approach found 47-64 bug candidates on an 11,000-line PR — a number that would be significantly lower with a single traversal. Practitioners independently arrived at similar intuitions by using multiple models, which inherently traverse context differently.

## Potential Improvements
- Explicit traversal strategy assignment: rather than random starting positions, assign specific entry patterns (e.g., start from the diff, start from the test suite, start from the entry point, start from the data model) for deterministic coverage.
- Larger fleet sizes for high-criticality reviews (Ultra Review supports up to 20 sub-agents for enterprise).
- Logging which traversal orders produced which findings, to build evidence on which entry points are highest yield.

## Potential Failure Modes
- The mechanism relies on the assumption that different start positions produce meaningfully different reasoning — this may not hold for all bug types (e.g., bugs that are obvious regardless of order).
- Fleet cost scales linearly with fleet size. Larger fleets for large PRs are expensive.
- If the codebase is small enough to fit entirely in one context window, traversal diversity provides no benefit.
