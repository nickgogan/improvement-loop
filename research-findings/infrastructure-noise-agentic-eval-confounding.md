---
name: 'Infrastructure Noise: Resource Configuration as Agentic Eval Confound'
summary: Infrastructure configuration (CPU, RAM, resource enforcement) swings agentic coding benchmark scores by up to 6 percentage points (p < 0.01), exceeding typical leaderboard gaps between top models.
  Resource enforcement strategy (guaranteed allocation vs hard kill threshold) is the primary noise source, with infra error rates ranging from 5.8% at strict 1x to 0.5% uncapped.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
sources:
- anthropic-infrastructure-noise-evals.md
related_findings:
- file: benchmark-signal-mismatch-optimization-gap.md
  rel: extends
- file: factorial-design-eval-systematic-context-variati.md
  rel: same-problem
- file: four-layer-production-eval-stack-with-golden-traces.md
  rel: same-problem
- file: eval-driven-development-autonomous-quality.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Infrastructure Noise: Resource Configuration as Agentic Eval Confound

## What It Is

Anthropic quantified how infrastructure configuration affects agentic coding benchmark scores. Testing Terminal-Bench 2.0 across six resource configurations (from strict 1x enforcement to uncapped), they found:

**Resource enforcement band matters more than capability:** From 1x (guaranteed = hard limit, zero headroom) to 3x headroom, infra error rates dropped from 5.8% to 2.1% (p < 0.001), but success rates fluctuated within noise (p = 0.40). Most 1x crashes were on unsolvable tasks anyway. From 3x to uncapped, errors dropped an additional 1.6 points while success jumped ~4 points -- extra resources enabled agents to install large dependencies, run expensive subprocesses, and execute memory-intensive tests.

**Total effect:** 1x to uncapped = +6 percentage points success (p < 0.01), exceeding typical leaderboard gaps between top models.

**Cross-benchmark validation on SWE-bench:** 227 problems, 10 samples each, RAM varied to 5x baseline. Scores rose monotonically, +1.54 points at 5x vs 1x (smaller effect because SWE-bench tasks are less resource-intensive).

**Configuration determines strategy winners:** Tight limits reward efficient, stdlib-only approaches (e.g., pure-math Bayesian fitting). Generous limits reward brute-force, heavy-dependency approaches (e.g., pandas/networkx/scikit-learn). Different models default to different strategies, so resource configuration determines which model "wins" the benchmark -- a confound, not a capability measurement.

**Other noise sources:** Cluster health, hardware specs, concurrency, egress bandwidth, time-of-day API latency from traffic/incidents. Pod failure rates up to 6% in GKE, unrelated to model ability.

## Why It Matters

Leaderboard gaps under 3 points should be treated with skepticism. The infra spread alone is ~2 points under moderate configurations and 6 points at extremes, stacking on top of binomial confidence intervals of 1-2 points. A 2-point lead on a coding benchmark might reflect capability, or it might reflect a beefier VM or luckier time of day.

For MetaSystem's evaluation design: any agentic eval must document and control resource configuration as a first-class variable, equivalent to prompt and temperature. Without this, eval results are not reproducible and comparisons between runs are invalid.

## Why People Are Using It

Anthropic published this as a methodological warning to the evaluation community. They advocate treating infrastructure as a controlled variable, specifying both guaranteed allocation (floor) and hard kill threshold (ceiling) per task, running multiple times across different days, and using dedicated hardware when possible.

## Potential Improvements

Standardized resource profiles for common eval suites. Eval harnesses that report resource configuration alongside scores. Dual-score reporting: "score at standard config" and "score at generous config" to separate efficiency from capability. Automated resource profiling that determines minimum viable allocation per task.

## Potential Failure Modes

Over-provisioning resources to inflate scores. Under-provisioning to test efficiency but missing capability. Ignoring time-of-day effects in single-run evaluations. Treating resource configuration as a one-time decision rather than an ongoing variable to control. The noise floor means some real capability differences are undetectable -- legitimate 1-2 point improvements may be indistinguishable from infrastructure variance.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[infrastructure-noise-eval-confound-control.md]] in `extracts/patterns/`
