---
notion_id: 32b1e08b-9b34-810f-b532-c4dd3ebbdef7
name: 'Factorial Design Eval: Systematic Context Variation for Hidden Bias Detection'
summary: Testing the same scenario across multiple controlled contextual variations (social cues, extreme risk, tool failure, time pressure) exposes anchoring bias, guardrail inversion, and tail failures
  that single-scenario testing always misses.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- General
adopted_in: null
sources:
- chatgpt-health-identified-respiratory-failure-then.md
- anthropic-infrastructure-noise-evals.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: success-rate-eval-over-binary-pass-fail.md
  rel: extends
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: volume-over-quality-eval-principle.md
  rel: enables
- file: infrastructure-noise-agentic-eval-confounding.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
  - verifying-agent-output.md
---
# Factorial Design Eval: Systematic Context Variation for Hidden Bias Detection

## What It Is
Mount Sinai tested ChatGPT Health on the same clinical cases across 16 contextual variations — adding/removing social minimization cues, adding/removing extreme risk markers, varying framing. This factorial design revealed anchoring bias (12x output shift with social cue), guardrail inversion, and tail failures that would have been invisible in standard single-scenario testing. The variation types are domain-general (social pressure, extreme risk, tool failure, time pressure, contradictory context, hedging qualifiers) while the scenarios themselves are domain-specific. This means a single eval library structure scales across all domains — build the variation type library once, populate with domain-specific scenarios. Enterprise scenarios can be semi-automatically generated from historical data (processed claims, compliance screenings, customer service records). The pattern: variation types are the sections of the eval library (stable); scenarios are the books (domain-specific).

## Why It Matters
Standard benchmarks that test each scenario once under one condition produce misleading accuracy numbers. Factorial design is the only method that reliably surfaces the structural biases and failure modes described above. Without it, production agents can pass all standard tests while systematically failing on the exact cases that matter most.

## Why People Are Using It
Adoption is currently low — most teams rely on single-scenario benchmarks. The investment required (domain expertise, test case design, execution infrastructure) is significant but front-loaded.

## Potential Alternatives
Red-teaming (manual adversarial testing). A/B testing in production shadow mode. Statistical sampling of production logs for anomaly detection.

## Potential Improvements
LLM-based semi-automatic scenario generation from historical data to populate the eval library. Tooling that automates variation injection across existing scenario sets.

## Potential Failure Modes
Factorial testing is expensive and cannot be run continuously on all agents. Must be reserved for high-stakes agents and run periodically rather than on every deployment.
