---
name: 'Task Contract Pattern: Schema-First Agent Interactions'
summary: Define explicit contracts for every agent interaction including input/output schemas, quality constraints, cost/latency budgets, and allowed tools per role. Contracts should be maintained centrally
  and inherited by all agent sessions. Eliminates hallucination failures by replacing text-only interfaces with validated schemas.
implementation_notes: 'MetaSystem''s skill SKILL.md files partially implement this -- they define inputs and outputs but lack formal schemas, quality constraints, and cost/latency budgets. The task contract
  pattern would formalize what skills currently do informally. Priority: apply to any skill that spawns subagents.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- multi-agent-orchestration-production-playbook-nick.md
- ai-agents-in-production-2026-nick-gupta-linkedin.md
related_findings:
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: enabled-by
- file: planner-executor-deterministic-guardrails.md
  rel: enables
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: same-problem
- file: spec-as-source-of-truth-for-agent-construction.md
  rel: same-problem
- file: skill-vs-process-distinction-deterministic-rails.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
- writing-agent-specifications.md
---
# Task Contract Pattern: Schema-First Agent Interactions

## What It Is
Layer 0 of production multi-agent systems. Every agent interaction gets an explicit contract defining: input schema, output schema, quality constraints (must/should), cost/latency budgets, and allowed tools per role. Contracts are maintained centrally and inherited by all agent sessions. This replaces text-only agent interfaces with validated schemas that prevent hallucination at the boundary.

## Why It Matters
Without contracts, agents "negotiate" their interfaces in natural language -- introducing ambiguity, drift, and hallucination at every boundary. Contracts provide the organizational infrastructure that prevents context rot and makes agent behavior predictable and testable.

## Why People Are Using It
Nick Gupta identifies this as Layer 0 (foundational) in his production playbook. Microsoft Agent Framework treats contracts as first-class primitives. The pattern maps directly to API contract-first development, which has decades of precedent in service-oriented architecture.

## Potential Improvements
Auto-generation of contracts from observed agent behavior (mine production traces for implicit schemas). Version-aware contracts that handle schema evolution across agent updates.

## Potential Failure Modes
Over-specification that constrains agent flexibility for exploratory tasks. Contract maintenance overhead if contracts are not auto-validated. Schema drift between contract definition and actual behavior if validation is not enforced at runtime.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[task-contract-pattern-schema-first-agent.md]] in `extracts/patterns/`
