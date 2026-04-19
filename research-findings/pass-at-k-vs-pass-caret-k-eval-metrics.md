---
name: pass@k vs pass^k Eval Metrics for Agent Reliability
summary: 'Two complementary metrics for non-deterministic agents: pass@k (probability of at least one success in k trials — optimistic) vs pass^k (probability all k trials succeed — consistency-focused).
  Metric choice is a design decision.'
implementation_notes: MetaSystem's verification loops should explicitly choose which metric applies. pass^k for production reliability gates; pass@k for capability exploration. Current eval approach doesn't
  distinguish these.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-demystifying-evals-for-ai-agents.md
- anthropic-claude-think-tool.md
related_findings:
- file: think-tool-scratchpad-for-mid-chain-reasoning.md
  rel: enables
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

## What It Is

pass@k calculates the chance of at least one correct answer in k attempts — approaches 100% even for mediocre agents at high k. pass^k calculates the chance every trial succeeds — falls toward 0% for all but the most reliable agents. Example: 75% per-trial success over 3 trials yields pass^k of (0.75)^3 = ~42%.

## Why It Matters

Choosing the wrong metric produces misleading conclusions. Use pass@k for tools where users retry until success. Use pass^k for production agents where users expect consistent reliability. The two metrics diverge dramatically at higher k values.

## Why People Are Using It

Used across Anthropic's agent evaluation infrastructure. The think tool blog post also references pass^k for consistency measurement.

## Potential Improvements

Could combine into a composite reliability score. Could track pass^k trends over time to measure stability improvements distinct from capability improvements.

## Potential Failure Modes

Teams may default to pass@k because the numbers look better, masking reliability problems. Need explicit policy on which metric applies to which evaluation context.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[pass-at-k-vs-pass-caret-k-eval-metrics.md]] in `extracts/patterns/`
