---
name: Four-Layer Production Eval Stack with Golden Traces
summary: 'Production agent evaluation requires four layers: (1) tool correctness (schema validation, timeout, permissions); (2) scenario workflows (task completion, tool selection, forbidden action avoidance);
  (3) shadow/canary (trace comparison, traffic slicing, regression detection); (4) online outcomes (success rate, override rate, cost-per-task). Backed by a golden traces library of canonical runs for replay-based
  regression testing.'
implementation_notes: 'MetaSystem has no eval layers beyond human review. Layer 1 (tool correctness) maps to hook-based validation. Layer 2 (scenario workflows) maps to skill acceptance criteria. Layers
  3-4 require production deployment. The golden traces concept is immediately applicable: capture canonical successful skill runs as regression baselines.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- ai-agents-in-production-2026-nick-gupta-linkedin.md
related_findings:
- file: four-layer-agent-evaluation-architecture.md
  rel: same-problem
- file: three-tier-grading-hierarchy.md
  rel: same-problem
- file: bmad-deterministic-skill-validator.md
  rel: same-problem
- file: agent-architecture-layer-impermanence.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: three-tier-grading-hierarchy.md
  rel: same-problem
- file: bmad-deterministic-skill-validator.md
  rel: same-problem
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
---

# Four-Layer Production Eval Stack with Golden Traces

## What It Is

A defense-in-depth evaluation architecture for production agent systems with four layers that catch different failure modes:

**Layer 1 -- Tool Correctness:** Schema validation for tool inputs/outputs, timeout behavior verification, permission enforcement checks, audit trail assertions. This is the deterministic foundation.

**Layer 2 -- Scenario Workflows:** End-to-end task completion tests. Correct tool selection for given inputs. Forbidden action avoidance (agent must NOT call certain tools in certain contexts). Proper approval requests for privileged operations. Citation presence in outputs. Correct termination (agent stops when it should).

**Layer 3 -- Shadow/Canary:** Run new agent versions against production traffic in shadow mode. Compare traces between versions. Detect regression in latency, policy compliance, and cost. Traffic slice testing (route small percentage to new version, compare outcomes).

**Layer 4 -- Online Outcomes:** Task success rate, human override rate, escalation rate, answer groundedness, cost-per-task. These are the ultimate production metrics.

**Golden Traces Library:** A curated set of canonical runs including: successful completions, known failure cases with explanations, edge cases, security tests, cost-stress scenarios, and latency-stress scenarios. Used for replay-based regression testing against any agent change.

**Hybrid Judge Stack:** Don't rely solely on LLM-as-judge. Combine: programmatic checks for deterministic facts, execution-result validation, human review for ambiguous samples, model judgment for fuzzy dimensions, production outcome metrics.

## Why It Matters

Each layer catches failures the others miss. Tool correctness catches schema violations before they reach users. Scenario testing catches logic failures in controlled conditions. Shadow/canary catches regressions that only manifest under real traffic. Online outcomes measure what actually matters. Without all four, evaluation has blind spots.

## Why People Are Using It

Nick Gupta documents this as the evaluation architecture for production agent systems. It converges with the existing KB's four-layer eval architecture (progressive autonomy, deterministic validation, LLM-as-judge, factorial stress testing) but adds the golden traces library and shadow/canary deployment patterns.

## Potential Improvements

Automated golden trace generation from production successes. Trace diff tooling that highlights semantic differences (not just structural). Cost-aware eval selection (don't run expensive Layer 4 evals on trivial changes).

## Potential Failure Modes

Golden traces becoming stale as requirements evolve. Shadow mode not capturing stateful interactions (agent behavior depends on prior state). Online outcome metrics that are noisy due to user behavior variability.
