---
name: Balanced Positive and Negative Eval Sets
summary: Test both positive cases (behavior should trigger) and negative cases (behavior should not trigger). Claude.ai's web search overtriggered because early evals only tested 'should search' scenarios.
implementation_notes: When building evals for MetaSystem skills (e.g., should research-loop extract a finding or skip it?), include explicit negative cases to prevent overtriggering.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-demystifying-evals-for-ai-agents.md
related_findings:
- file: volume-over-quality-eval-principle.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- rules/balanced-positive-negative-eval-sets.md
- building-agent-evaluation-suites.md
---

## What It Is
When evals only cover cases where an agent should act, optimization drives it to always act — even when it shouldn't. Balanced sets include explicit negative cases where the correct behavior is restraint. Example: "find the weather in Paris" (should search) alongside "who founded Apple?" (should use existing knowledge).

## Why It Matters
Claude.ai's web search experienced overtriggering because early evals only tested "should search" scenarios. Class imbalance in evals produces class-imbalanced agent behavior. Required "many rounds of refinements" to correct after rebalancing.

## Why People Are Using It
Anthropic documented this as a lesson learned from production Claude.ai web search deployment.

## Potential Improvements
Automated negative case generation from positive cases. Adversarial eval generation that specifically probes boundary conditions.

## Potential Failure Modes
Over-indexing on negative cases can make agents too conservative (undertriggering). Need calibrated balance, not just 50/50 split.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[balanced-positive-negative-eval-sets]] in `extracts/rules/`
