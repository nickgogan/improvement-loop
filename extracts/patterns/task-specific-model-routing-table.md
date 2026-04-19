---
title: "Task-Specific Model Routing Table"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "task-specific-model-routing-table-march-2026-bench"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Benchmark data from at least two independent sources exists for the models being routed. Task taxonomy is defined with clear boundaries between categories."
  invariants: "Every routed task maps to exactly one primary model. Cost-per-task is tracked alongside quality. No model is selected by default without task classification."
  governance: "Routing table is reviewed when any constituent model has a major release. Benchmark sources are cited and dated. Superseded rows are archived, not deleted."
  recovery: "If a routed model is unavailable or deprecated, fall back to the next-best model in the same task tier. If benchmark data is invalidated, revert to the previous validated routing table."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Task-Specific Model Routing Table

**Source:** [[task-specific-model-routing-table-march-2026-bench]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams default to a single frontier model for all tasks, paying premium costs (e.g., Opus at 3.5x Sonnet pricing) without quality gains, while simultaneously underperforming on task categories where a different model demonstrably excels. Without structured routing, model selection becomes a matter of habit or brand loyalty rather than evidence.

## Forces

- **Cost vs. quality:** The most expensive model is not always the most accurate for a given task type. Defaulting to the cheapest model sacrifices quality on complex tasks; defaulting to the most expensive wastes budget on simple ones.
- **Benchmark volatility:** Model rankings shift with each release cycle (monthly or faster). A routing table that is correct today may be wrong in 60 days.
- **Task taxonomy ambiguity:** Real-world tasks do not always map cleanly to benchmark categories. A "coding" task that also requires long-horizon reasoning spans two routing tiers.
- **Operational simplicity vs. optimization:** Routing to multiple models increases infrastructure complexity (API keys, rate limits, context format differences) compared to a single-model default.

## Solution

Maintain a structured routing table that maps task categories to recommended models, grounded in converging benchmark evidence from multiple independent sources.

**Shape:**

1. **Define a task taxonomy** with 3-5 non-overlapping categories (e.g., repository-level coding, orchestration/browser automation, abstract reasoning, batch extraction/transformation).
2. **For each category, identify the leading model** using at least two independent benchmark sources. Record the specific benchmark scores and dates.
3. **Include a cost column** showing relative cost per task, so routing decisions account for both quality and economics.
4. **Flag the "anti-default"** -- the model that appears best by reputation but is dominated on cost-adjusted quality (e.g., Opus 4.6 at 3.5x Sonnet cost with no accuracy premium).
5. **Set a review cadence** tied to major model releases rather than calendar dates.

**Example (March 2026 consensus):**

| Task Type | Model | Evidence | Relative Cost |
|---|---|---|---|
| Repo-level coding, knowledge work | Claude Sonnet 4.6 | GDPval Elo 1633, SWE-bench ~79.6% | 1x |
| Computer use, orchestration | GPT-5.4 | WebArena-Verified 67.3% | ~1.2x |
| Abstract reasoning, long-horizon math | Gemini 3.1 Pro | ARC-AGI-2 77.1% | ~1.5x |
| Batch extraction/transformation | Gemini Flash | 97.1% quality | ~0.1x |

## Consequences

**Positive:**
- Material quality gains on tasks where the default model underperforms (e.g., abstract reasoning routed to Gemini 3.1 Pro instead of Sonnet).
- Significant cost reduction on batch tasks routed to cost-floor models.
- Makes the "Opus by default" anti-pattern visible and actionable.

**Negative:**
- Routing table requires periodic maintenance as models and benchmarks evolve.
- Task classification itself introduces a decision point that can be wrong -- misrouted tasks get the wrong model.
- Multi-model infrastructure is more complex than single-model deployments.
- Benchmarks measure specific capabilities; real-world tasks may not align cleanly.

## Known Uses

- Ian L. Paterson's 38-task, 15-model benchmark (March 2026) independently converged on the same tier structure.
- Lorka.ai's Gemini vs. GPT vs. Claude comparison validated the routing splits.
- ARC-AGI-2 and ARC-AGI-3 results confirmed Gemini's reasoning advantage and all models' ceilings on novel abstraction.

## Contract

### Preconditions
Benchmark data from at least two independent sources exists for the models being routed. A task taxonomy with clear category boundaries is defined before routing begins.

### Invariants
Every routed task maps to exactly one primary model. Cost-per-task is tracked alongside quality scores. No model is selected by default without explicit task classification.

### Governance
The routing table is reviewed whenever a constituent model has a major release. All benchmark sources are cited with dates. Superseded routing rows are archived with the date of supersession, not silently deleted.

### Recovery
If a routed model becomes unavailable or is deprecated, fall back to the next-best model in the same task tier. If benchmark data is invalidated (e.g., a benchmark is found to be contaminated), revert to the previous validated routing table and flag for re-evaluation.
