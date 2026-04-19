---
name: Capability Saturation Threshold for Multi-Agent Systems
summary: Multi-agent coordination yields diminishing or negative returns once single-agent baselines exceed ~45% performance. Past this threshold, adding agents degrades results due to coordination overhead.
  Under fixed computational budgets, tool-heavy tasks suffer disproportionately from multi-agent overhead.
implementation_notes: 'Provides a concrete decision heuristic: if a single agent achieves >45% baseline on a task, stop trying to orchestrate and invest in making that single agent better. Complements the
  L>D hypothesis with an empirical threshold. Apply when evaluating whether to use subagents vs. improving a single skill.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- agent-orchestrators-are-bad.md
related_findings:
- file: tool-shaped-object-evaluation-lens.md
  rel: same-problem
- file: specialization-theater-anti-pattern.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: l-d-hypothesis-information-loss-across-agent-bound.md
  rel: same-problem
- file: model-tier-routing-expensive-orchestrator-cheap-s.md
  rel: same-problem
- file: legitimate-multi-agent-domains-taxonomy.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---
# Capability Saturation Threshold for Multi-Agent Systems

## What It Is
Research evidence shows that multi-agent coordination produces diminishing or negative returns once single-agent baselines exceed approximately 45% performance on a task. Past this threshold, adding agents degrades results because coordination overhead (information loss, handoff costs, error amplification) exceeds the marginal benefit of additional agent capacity. Under fixed computational budgets, token allocation to depth (single agent reasoning) outperforms allocation to breadth (agent count).

## Why It Matters
Provides a concrete, empirically-grounded decision heuristic for the "should we use multiple agents?" question. Instead of architectural preference or FOMO-driven adoption, teams can measure single-agent baseline performance and make a data-driven decision. The 45% threshold is conservative -- the actual breakeven likely varies by task but the principle holds.

## Why People Are Using It
Cited in the "Agent Orchestrators Are Bad" analysis alongside Google research showing independent agents amplify errors 17.2x versus centralized coordination at 4.4x. The finding addresses the FOMO-driven technology adoption pattern where teams adopt orchestrators because they feel innovative, not because they produce measurable improvement.

## Potential Improvements
Task-specific calibration of the saturation threshold. Automated benchmarking that compares single-agent vs multi-agent performance on each new task type before committing to an architecture.

## Potential Failure Modes
The 45% threshold is an approximation -- some tasks may benefit from orchestration at lower baselines (genuinely parallelizable work) or degrade at higher baselines. Measuring "performance" itself requires well-defined eval criteria, creating a dependency on the eval infrastructure.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[capability-saturation-threshold]] in `extracts/patterns/`
