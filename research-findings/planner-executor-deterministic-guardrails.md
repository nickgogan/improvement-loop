---
name: Planner-Executor with Deterministic Guardrails
summary: 'Hard rule: planning can be probabilistic; execution must be deterministic. Planner produces step plans with explicit dependencies. Executor runs deterministic steps. Verifier checks outputs before
  continuing. Critical for tool-heavy workflows involving DB queries, code changes, and deployments.'
implementation_notes: 'MetaSystem''s GSD plugin implements a version of this (plan phase -> execute phase -> verify phase). The key insight is formalizing the boundary: LLM reasoning for planning, deterministic
  execution for actions, verification before proceeding. Skills that modify files or external systems should enforce this separation.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- multi-agent-orchestration-production-playbook-nick.md
- ai-agents-in-production-2026-nick-gupta-linkedin.md
related_findings:
- file: tool-gateway-security-boundary.md
  rel: enables
- file: workflow-state-vs-conversation-state.md
  rel: same-problem
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: durable-workflow-engine-for-agent-systems.md
  rel: enabled-by
- file: task-contract-pattern-schema-first-agent.md
  rel: enabled-by
- file: gsd-get-shit-done-plugin.md
  rel: enabled-by
- file: agent-architecture-layer-impermanence.md
  rel: contradicts
- file: skill-vs-process-distinction-deterministic-rails.md
  rel: same-problem
- file: specialized-harness-engineering-deterministic-rail.md
  rel: same-problem
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: advisor-executor-api-pattern.md
  rel: same-problem
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---
# Planner-Executor with Deterministic Guardrails

## What It Is
A hard architectural boundary between probabilistic planning and deterministic execution. The planner (LLM) produces step plans with explicit dependencies and quality constraints. The executor runs steps deterministically -- no LLM reasoning during execution, only schema validation and tool invocation. A verifier checks each output against quality constraints before the next step proceeds. This three-phase pattern (plan -> execute -> verify) applies to any workflow involving side effects.

## Why It Matters
When planning and execution are mixed, LLM hallucinations can trigger irreversible side effects (wrong DB queries, incorrect deployments, malformed API calls). The deterministic execution boundary ensures that only validated plans produce actions. Compliance controls and retry logic should be deterministic, not probabilistic.

## Why People Are Using It
Nick Gupta describes this as a core multi-agent orchestration pattern. Microsoft Agent Framework separates agent orchestration (LLM-driven) from workflow orchestration (deterministic) as first-class primitives. The principle echoes established patterns in CI/CD pipelines and infrastructure-as-code. Nate B Jones corroborates from enterprise OpenClaw deployments with a vivid analogy: letting an agent decide process flow is "like ripping up your railroad and sticking your train on the ground and saying kind of go that way." The agent should receive the same deterministic trigger at the same time every time a workflow event fires; the agent's value is within each step (composing text, calling tools), not deciding step order.

## Potential Improvements
Dynamic re-planning when execution encounters unexpected states. Rollback support for partially executed plans. Plan caching for recurring workflows.

## Potential Failure Modes
Over-rigid plans that cannot adapt to runtime conditions. Planner producing steps that are syntactically valid but semantically wrong. Verifier that passes invalid outputs due to insufficient quality constraints.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[planner-executor-deterministic-guardrails.md]] in `extracts/patterns/`
