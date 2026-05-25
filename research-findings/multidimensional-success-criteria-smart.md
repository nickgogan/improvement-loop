---
name: Multidimensional SMART Success Criteria for Evals
summary: 'Good eval success criteria are Specific, Measurable, Achievable, and Relevant. Most use cases require multidimensional evaluation along several criteria simultaneously: task fidelity, consistency,
  relevance/coherence, tone/style, privacy, context utilization, latency, and price. Even ''hazy'' topics like ethics and safety can be quantified with specific thresholds.'
implementation_notes: 'MetaSystem''s prompt-evaluator uses qualitative rubrics. This pattern suggests adding quantitative thresholds alongside qualitative scores: e.g., ''less than 0.1% of outputs flagged
  for toxicity out of 10,000 trials.'' Apply to skill evaluation where we can define measurable success criteria.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- anthropic-prompt-evaluation-framework.md
related_findings:
- file: benchmark-signal-mismatch-optimization-gap.md
  rel: same-problem
- file: binary-eval-assertion-design-deterministic-plus-ll.md
  rel: same-problem
- file: test-input-coverage-design-15-30-sweet-spot.md
  rel: same-problem
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: four-discipline-prompt-evaluator.md
  rel: same-problem
- file: volume-over-quality-eval-principle.md
  rel: same-problem
- file: three-tier-grading-hierarchy.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
- writing-agent-specifications.md
---
# Multidimensional SMART Success Criteria for Evals

## What It Is
Anthropic's framework for defining eval success criteria. Good criteria must be:
- **Specific:** "Accurate sentiment classification" not "good performance"
- **Measurable:** Quantitative metrics (F1 score, accuracy, precision, recall, response time) or well-defined qualitative scales (Likert 1-5)
- **Achievable:** Based on industry benchmarks and current frontier model capabilities
- **Relevant:** Aligned with application purpose and user needs

Most use cases require **multidimensional** evaluation across several criteria simultaneously. Anthropic's example for sentiment analysis: F1 >= 0.85, 99.5% non-toxic outputs, 90% of errors are inconvenience-level, 95% response time < 200ms.

Eight common success dimensions: task fidelity, consistency, relevance/coherence, tone/style, privacy preservation, context utilization, latency, and price.

## Why It Matters
Single-dimension evaluation (accuracy only) misses critical failure modes. A model achieving 95% accuracy but leaking PHI in 5% of responses is unacceptable. Multidimensional criteria force explicit tradeoff decisions and prevent optimizing one dimension at the expense of others.

## Why People Are Using It
Anthropic's official eval documentation. The framework echoes established measurement principles from software engineering (SLOs, SLAs) applied to LLM outputs.

## Potential Improvements
Automated dimension weighting based on use case classification. Dynamic thresholds that tighten as the system matures. Dimension interaction analysis (e.g., latency vs. quality tradeoffs).

## Potential Failure Modes
Proliferation of dimensions that makes evaluation expensive and slow. Dimensions that conflict (optimizing for consistency may reduce creativity). Thresholds that are set once and never updated as model capabilities improve.
