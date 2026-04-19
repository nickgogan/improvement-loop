---
title: "Context Rot and Attention Budget Depletion"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "context-rot-attention-budget-depletion"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "System uses LLM context windows for multi-step agent tasks; token usage is measurable; context management primitives (compaction, clearing, summarization) are available."
  invariants: "Every token added to context has a cost beyond storage — it degrades attention on all other tokens. Context hygiene is continuous, not a one-time budget check."
  governance: "Context management policy is reviewed when switching model families or context window sizes. Token budgets are explicit per skill/agent, not implicit."
  recovery: "When agent performance degrades mid-session: measure current context utilization, apply compaction or /clear, re-inject only essential context, and resume. If degradation persists after compaction, escalate to session restart."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Context Rot and Attention Budget Depletion

**Source:** [[context-rot-attention-budget-depletion]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems that treat the LLM context window as a simple storage container — where the only concern is staying under the token limit — experience progressive performance degradation on long-horizon tasks. Recall accuracy, instruction following, and reasoning quality silently erode as the context fills, even when the window is not technically full.

## Forces

- **Completeness vs. performance.** Agents need sufficient context (instructions, history, tool results) to act correctly, but every additional token degrades attention on all others.
- **Invisible degradation.** Context rot is not a hard failure — it manifests as subtly worse outputs, missed instructions, and forgotten constraints, making it difficult to diagnose.
- **Quadratic attention cost.** Transformer attention creates pairwise relationships between all tokens (O(n^2)), so the marginal cost of each token accelerates as context grows.
- **Training-length mismatch.** Models trained on shorter sequences have fewer specialized parameters for long-range dependencies. Position encoding interpolation extends length but introduces its own degradation.
- **Pruning risk.** Aggressive context hygiene can remove tokens the model actually needs, causing different failures than the ones it prevents.

## Solution

Treat context as a **finite, depletable resource** — not merely a size limit. Apply these structural measures:

1. **Continuous compaction.** Periodically summarize or discard context that has served its purpose (completed tool results, resolved subtasks, stale history). Do not wait until the window is near-full.
2. **Token budgets per phase.** Allocate explicit token budgets to each agent skill or task phase. Monitor utilization and trigger compaction when a phase exceeds its budget.
3. **Essential-only injection.** When re-injecting context after compaction or session restart, include only what is required for the current task — not the full history.
4. **Recency weighting.** Structure context so that the most recent and most relevant information is positioned where attention is strongest (typically the beginning and end of the window).
5. **Proactive clearing.** Use explicit clearing primitives (/clear, tool result clearing) rather than relying on the model to "ignore" irrelevant context.

## Consequences

**Positive:**
- Sustained agent accuracy across long sessions and multi-step tasks.
- Lower token costs per session (less redundant context carried forward).
- Explicit token budgets make performance problems diagnosable.

**Negative:**
- Compaction introduces information loss — summaries may omit details the model later needs.
- Token budgets require calibration per task type; static budgets will be wrong for some tasks.
- Additional engineering overhead to implement compaction, monitoring, and budget enforcement.
- The optimal balance between "lean context" and "sufficient context" is task-dependent and cannot be fully automated.

## Known Uses

- **Anthropic Claude Code:** Aggressive context management via compaction, /clear, and tool result clearing — designed specifically to mitigate attention budget depletion.
- **Anthropic context engineering guide:** Published context rot as the foundational premise for all context engineering recommendations.
- **MetaSystem session hygiene:** Session handoff, PROGRESS.md compression, and skill-scoped context injection all follow this pattern implicitly.

## Contract

### Preconditions
- The system uses LLM context windows for multi-step agent tasks.
- Token usage is measurable (token counts are available per turn or per session).
- Context management primitives (compaction, clearing, summarization) are available in the runtime.

### Invariants
- Every token added to context has a cost beyond storage — it degrades attention on all other tokens.
- Context hygiene is continuous, not a one-time budget check at injection time.
- No context management action removes tokens that are actively required by the current task step.

### Governance
- Context management policy is reviewed when switching model families or context window sizes.
- Token budgets are explicit per skill/agent, not implicit or unbounded.
- Compaction quality is spot-checked during governance audits (are summaries losing critical details?).

### Recovery
- When agent performance degrades mid-session: measure current context utilization, apply compaction or /clear, re-inject only essential context, and resume.
- If degradation persists after compaction, escalate to a full session restart with fresh context injection.
- Log the degradation event and context size at time of failure for calibration of future token budgets.
