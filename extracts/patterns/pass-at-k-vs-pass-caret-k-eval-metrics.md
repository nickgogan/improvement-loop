---
title: "Dual-Metric Agent Reliability Evaluation"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "pass-at-k-vs-pass-caret-k-eval-metrics"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Evaluation harness exists that can run k repeated trials of the same task and record per-trial pass/fail."
  invariants: "Every evaluation context has an explicitly declared metric (pass@k or pass^k) before results are interpreted. No evaluation is reported without stating which metric was used."
  governance: "Metric assignment to evaluation contexts is a Design Decision. Changing which metric applies to a given context requires DD review."
  recovery: "If an evaluation is discovered to have been reported under the wrong metric, re-score under the correct metric and append a correction note to the evaluation record."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Dual-Metric Agent Reliability Evaluation

**Source:** [[pass-at-k-vs-pass-caret-k-eval-metrics]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Non-deterministic agents produce variable outputs across runs. A single success/failure measurement tells you nothing about whether the agent is reliably good or merely occasionally lucky. Teams default to whichever metric makes their agent look better, producing misleading reliability claims that collapse in production.

## Forces

- **Optimism vs. conservatism.** Stakeholders want to know "can it do this?" (capability) while operators need to know "will it always do this?" (consistency). These are fundamentally different questions answered by different metrics.
- **Sample size amplifies divergence.** At small k, pass@k and pass^k are close. At production-relevant k values (10+), they diverge dramatically, making metric choice a design decision rather than a reporting preference.
- **Retry tolerance varies by context.** Interactive tools where users retry are well-served by pass@k. Autonomous agents where failures propagate silently demand pass^k.
- **Single-metric reporting obscures reality.** Reporting only one metric hides the information the other would reveal. pass@k hides fragility; pass^k hides capability.

## Solution

Maintain two complementary evaluation metrics and assign each evaluation context an explicit primary metric:

1. **pass@k** -- probability of at least one success in k trials. Use for capability exploration, interactive tools, and research contexts where "can it ever do this?" is the question. Formula: 1 - (1 - p)^k.
2. **pass^k** -- probability of all k trials succeeding. Use for production reliability gates, autonomous pipelines, and contexts where every invocation must succeed. Formula: p^k.

For each evaluation context:
- Declare the primary metric in the evaluation spec before running trials.
- Report both metrics but interpret results through the declared primary.
- Track pass^k trends over time to distinguish stability improvements from capability improvements.
- Set minimum thresholds per metric appropriate to the deployment context (e.g., pass^k >= 0.90 for production gates).

## Consequences

**Positive:**
- Eliminates metric-shopping where teams pick whichever number looks better.
- Makes reliability conversations precise -- "42% pass^k at k=3" communicates something unambiguous.
- Separates capability discovery from production readiness, allowing honest assessment of both.

**Negative:**
- Requires running k trials per evaluation, increasing eval cost by a factor of k.
- Teams must maintain metric assignment records, adding governance overhead.
- Composite scores (combining both metrics) are tempting but can obscure the very distinction this pattern creates.

## Known Uses

- Anthropic's agent evaluation infrastructure uses both metrics across their eval suite.
- The Think Tool blog post references pass^k specifically for consistency measurement of extended thinking.
- Production agent teams at Anthropic use pass^k as the gate for deployment readiness.

## Contract

### Preconditions
The evaluation harness must be capable of running k repeated trials of the same task and recording per-trial pass/fail results independently.

### Invariants
Every evaluation context has an explicitly declared primary metric (pass@k or pass^k) before results are interpreted. No evaluation result is reported without stating which metric was used and the value of k.

### Governance
Metric assignment to evaluation contexts is a Design Decision. Changing which metric applies to a given context requires a DD review and update cycle. Ad-hoc switching between metrics without governance is a violation.

### Recovery
If an evaluation is discovered to have been reported under the wrong metric, re-score the raw trial data under the correct metric and append a correction note to the evaluation record. Historical trend data must be recomputed under the corrected metric assignment.
