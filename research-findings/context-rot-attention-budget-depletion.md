---
name: Context Rot and Attention Budget Depletion
summary: As tokens in a context window increase, model recall accuracy degrades due to transformer attention budget depletion across n-squared pairwise relationships. Context is a finite, depletable resource
  — not merely a size limit.
implementation_notes: This reframes context management from 'stay under the limit' to 'minimize unnecessary tokens at all times.' Directly validates MetaSystem's aggressive context hygiene patterns.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-effective-context-engineering.md
related_findings:
- file: memory-decay-compaction-convergence.md
  rel: same-problem
- file: progressive-tiered-context-loading-convergence.md
  rel: same-problem
- file: attention-closure-goal-accessibility-collapse.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-07-11'
pipeline_status: synthesized
consumed_by:
- defending-agent-context.md
---

## What It Is

"Context rot" is the empirically observed phenomenon where LLM recall accuracy decreases as context window utilization grows. The transformer's attention mechanism creates pairwise relationships between every token, and models trained on shorter sequences have fewer specialized parameters for context-wide dependencies. Position encoding interpolation extends sequence length but introduces degradation.

## Why It Matters

Engineers who treat context windows as simple storage buckets see degraded agent performance on long-horizon tasks. Understanding the mechanism (attention budget, not just token count) changes how you architect multi-step agents. Every unnecessary token actively degrades performance on the tokens that matter.

## Why People Are Using It

Anthropic published this as the foundational premise of their context engineering guide. Claude Code's aggressive context management (compaction, /clear, tool result clearing) is a direct response.

## Potential Improvements

Future models may mitigate through architectural changes (linear attention, state-space models). Adaptive attention allocation could prioritize recent/relevant tokens.

## Potential Failure Modes

Over-aggressive context pruning that removes tokens the model actually needs. The balance between "lean context" and "sufficient context" is task-dependent and hard to calibrate automatically.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[context-rot-attention-budget-depletion]] in `extracts/patterns/`
