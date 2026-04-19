---
title: "Infrastructure Noise as Eval Confound — Control Resource Configuration"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "infrastructure-noise-agentic-eval-confounding"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Eval harness must support specifying resource profiles (CPU, RAM, disk) per task. Resource monitoring (peak usage, OOM kills, timeout events) must be instrumented before running comparative evaluations."
  invariants: "No eval comparison is valid without documented resource configuration. Resource profiles are reported alongside scores. Single-run evaluations are never used for model comparison."
  governance: "Owned by Meta-System knowledge layer. Resource profile standards require a Design Decision to modify. Eval result publication must include the resource configuration appendix."
  recovery: "If infra errors exceed 5% of task runs, flag the batch as confounded and re-run with relaxed resource limits. If scores differ by less than the infrastructure noise floor (~3 points), report the comparison as inconclusive rather than declaring a winner."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Infrastructure Noise as Eval Confound — Control Resource Configuration

**Source:** [[infrastructure-noise-agentic-eval-confounding]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agentic coding evaluations produce unstable scores when infrastructure configuration varies between runs. Resource enforcement strategy (CPU, RAM, disk limits) swings benchmark scores by up to 6 percentage points (p < 0.01) — a spread that exceeds typical leaderboard gaps between top models. Teams interpret these swings as capability differences when they are actually infrastructure artifacts. A model's apparent "lead" may reflect a beefier VM or luckier time of day rather than genuine ability.

## Forces

- **Reproducibility vs. cost.** Dedicated, identical hardware for every eval run eliminates infra noise but is expensive. Shared infrastructure is cheaper but introduces confounds from cluster health, concurrency, and time-of-day effects.
- **Generosity vs. realism.** Generous resource limits (uncapped RAM/CPU) let agents install heavy dependencies and exercise full capability, but inflate scores beyond what production constraints would allow. Tight limits test efficiency but may mask capability.
- **Simplicity vs. rigor.** Reporting a single score is simple and communicable. Reporting score-at-standard-config and score-at-generous-config is more informative but harder to consume.
- **Strategy bias.** Resource configuration determines which coding strategies succeed — tight limits reward stdlib-only approaches while generous limits reward brute-force dependency-heavy approaches. Different models default to different strategies, so the infrastructure silently picks the winner.

## Solution

Treat resource configuration as a **first-class controlled variable** in every agentic evaluation, equivalent to prompt template and temperature.

The pattern has five components:

1. **Resource profile specification.** Define both the guaranteed allocation floor and the hard kill ceiling for CPU, RAM, and disk per task. Document these as part of the eval configuration, not as implicit infrastructure defaults.

2. **Dual-band scoring.** Run each eval at two resource profiles — a "standard" profile (moderate headroom, e.g., 3x baseline) and a "generous" profile (uncapped or high ceiling). Report both scores. The gap between them measures how much capability is resource-gated vs. intrinsic.

3. **Multi-run temporal averaging.** Run evaluations across multiple days and times to average out cluster health, API latency, and concurrency effects. Single-run evaluations are insufficient for model comparison.

4. **Infrastructure error tracking.** Instrument the harness to record infra errors (OOM kills, timeouts, pod failures) separately from task failures. Report infra error rate alongside task success rate. If infra errors exceed a threshold (e.g., 5%), the batch is confounded.

5. **Noise floor declaration.** Establish the infrastructure noise floor for your specific setup (typically 2-3 points under moderate configurations). Score differences below the noise floor are reported as statistically indistinguishable.

## Consequences

**Positive:**
- Eliminates the largest known confound in agentic coding benchmarks.
- Enables valid cross-run and cross-model comparisons by controlling the primary noise source.
- Dual-band scoring separates efficiency (what the model can do under constraints) from capability (what it can do with unlimited resources), providing richer signal.
- Infrastructure error tracking surfaces silent failures that otherwise inflate or deflate scores unpredictably.

**Negative:**
- Doubles evaluation compute cost (two resource profiles per run) and increases wall-clock time (multi-day averaging).
- Requires eval harness engineering to support resource profiles, monitoring, and dual reporting.
- Noise floor declaration requires calibration runs that consume resources without producing capability signal.
- Over-provisioning to minimize infra noise may produce scores that don't generalize to production resource constraints.

## Known Uses

- **Anthropic Terminal-Bench 2.0 study.** Six resource configurations tested, 1x to uncapped. Documented the 6-point spread (p < 0.01) and the infra error rate curve (5.8% at strict 1x, 0.5% uncapped). Published as a methodological warning to the evaluation community.
- **SWE-bench cross-validation.** 227 problems, 10 samples each, RAM varied to 5x baseline. Confirmed monotonic score increase with resources (+1.54 points at 5x vs. 1x), with smaller effect due to less resource-intensive tasks.
- **Anthropic's internal eval practice.** Advocates specifying guaranteed allocation and hard kill threshold per task, running multiple times across different days, and using dedicated hardware when possible.

## Contract

### Preconditions

- Eval harness must support per-task resource profile specification (guaranteed floor + hard kill ceiling for CPU, RAM, disk).
- Resource monitoring must be instrumented to capture OOM kills, timeouts, pod failures, and peak resource usage per task.
- A baseline calibration run must establish the infrastructure noise floor before comparative evaluations begin.

### Invariants

- No eval comparison is published or acted upon without documented resource configuration for all runs being compared.
- Resource profiles are reported alongside scores in every eval output.
- Single-run evaluations are never used for cross-model comparison; multi-run temporal averaging is mandatory.
- Score differences below the declared noise floor are reported as statistically indistinguishable.

### Governance

- Owned by Meta-System knowledge layer.
- Resource profile standards (what constitutes "standard" and "generous") require a Design Decision to modify.
- Eval result publication must include the resource configuration appendix.

### Recovery

- If infra errors exceed 5% of task runs in a batch, flag the batch as confounded, diagnose the infra issue, and re-run with corrected configuration.
- If scores differ by less than the infrastructure noise floor, report the comparison as inconclusive rather than declaring a winner.
- If resource monitoring fails mid-run, discard the affected batch rather than reporting unmonitored results.
