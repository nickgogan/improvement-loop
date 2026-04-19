---
title: "Planner-Executor with Deterministic Guardrails"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "planner-executor-deterministic-guardrails"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A workflow exists that involves side effects (file modifications, API calls, database writes, deployments). The workflow has identifiable steps that can be expressed as a plan with explicit dependencies. A verification function or quality constraint exists for each step's output."
  invariants: "Planning is the only phase where LLM reasoning occurs. Execution is deterministic -- no LLM reasoning during step execution, only schema validation and tool invocation. Every step output is verified against quality constraints before the next step proceeds. The executor never modifies the plan; only the planner can produce or revise plans."
  governance: "Plan schemas are versioned and reviewed when workflow scope changes. Quality constraints per step are defined by the workflow owner, not the LLM. Verification logic is deterministic and auditable. Plan revisions triggered by execution failures require human approval for workflows with irreversible side effects."
  recovery: "If a step fails verification, halt execution and return the failure to the planner for re-planning. Do not retry failed steps without a revised plan. For partially executed plans with irreversible side effects, log the completed steps and surface the partial state for human review before re-planning."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Planner-Executor with Deterministic Guardrails

**Source:** [[planner-executor-deterministic-guardrails]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

When LLM reasoning and side-effecting execution are mixed in the same phase, hallucinations can trigger irreversible actions -- wrong database queries, incorrect deployments, malformed API calls. The agent decides both *what* to do and *how* to do it in the same turn, with no checkpoint between reasoning and action. Retry logic, compliance controls, and error handling become probabilistic rather than reliable.

## Forces

- **Flexibility vs. safety:** Allowing the LLM to reason during execution enables adaptation to unexpected states, but also enables hallucination-driven side effects.
- **Planning quality vs. execution reliability:** Good plans require probabilistic reasoning (weighing trade-offs, handling ambiguity), but execution requires deterministic guarantees (exact commands, validated inputs, predictable outputs).
- **Adaptability vs. determinism:** Over-rigid plans cannot respond to runtime conditions; fully adaptive execution cannot provide safety guarantees.
- **Speed vs. verification:** Verifying every step output before proceeding adds latency, but skipping verification risks cascading failures from undetected errors.

## Solution

Enforce a hard architectural boundary between three phases:

**1. Planner (probabilistic):**
- The LLM produces a step plan with explicit dependencies between steps
- Each step specifies: the action to take, the inputs required, the expected output shape, and the quality constraints that must hold
- The planner can reason freely -- weighing trade-offs, handling ambiguity, considering alternatives
- The plan is a data structure, not executable code -- it describes what should happen, not how

**2. Executor (deterministic):**
- Runs each step in dependency order using schema validation and tool invocation
- No LLM reasoning occurs during execution -- the executor is a state machine
- Inputs are validated against the plan's schema before each tool call
- The executor cannot modify the plan, skip steps, or reorder dependencies

**3. Verifier (deterministic):**
- Checks each step's output against the quality constraints defined in the plan
- Verification is pass/fail against concrete conditions, not subjective assessment
- If verification fails, execution halts and the failure is returned to the planner
- The verifier never "fixes" outputs -- it only gates progression

The key insight: letting an agent decide process flow is "like ripping up your railroad and sticking your train on the ground and saying kind of go that way" (Nate B Jones). The agent's value is within each step -- composing text, calling tools -- not in deciding step order. The deterministic rails are the railroad; the agent is the train.

## Consequences

**Positive:**
- Hallucinations during planning cannot directly trigger side effects -- the deterministic executor gates all actions
- Compliance controls and retry logic are deterministic and auditable, not probabilistic
- Failed steps produce clear diagnostics: which step, which constraint, what the actual output was
- Plans are inspectable artifacts -- humans can review what will happen before execution begins
- Matches established patterns in CI/CD pipelines and infrastructure-as-code

**Negative:**
- Over-rigid plans cannot adapt to genuinely unexpected runtime states without re-planning
- Re-planning after execution failure adds latency compared to inline adaptation
- The planner can produce steps that are syntactically valid but semantically wrong -- the executor will faithfully execute a bad plan
- Verification is only as good as the quality constraints -- insufficient constraints pass invalid outputs
- Adds architectural complexity compared to a single agent loop

## Known Uses

- Nick Gupta's multi-agent orchestration playbook describes this as a core production pattern
- Microsoft Agent Framework separates agent orchestration (LLM-driven) from workflow orchestration (deterministic) as first-class primitives
- MetaSystem's GSD plugin implements plan phase, execute phase, verify phase as distinct workflow stages
- CI/CD pipelines and infrastructure-as-code embody the same principle: declarative plans, deterministic execution, verification gates
- Nate B Jones corroborates from enterprise OpenClaw deployments: agents receive the same deterministic trigger at the same time every time a workflow event fires

## Contract

### Preconditions
A workflow exists that involves side effects (file modifications, API calls, database writes, deployments). The workflow has identifiable steps that can be expressed as a plan with explicit dependencies. A verification function or quality constraint exists -- or can be defined -- for each step's output. The plan schema is defined before the first execution.

### Invariants
Planning is the only phase where LLM reasoning occurs. Execution is deterministic -- no LLM reasoning during step execution, only schema validation and tool invocation. Every step output is verified against quality constraints before the next step proceeds. The executor never modifies the plan; only the planner can produce or revise plans. Plans are data structures, not executable code.

### Governance
Plan schemas are versioned and reviewed when workflow scope changes. Quality constraints per step are defined by the workflow owner, not generated by the LLM. Verification logic is deterministic, inspectable, and auditable. Plan revisions triggered by execution failures require human approval for workflows with irreversible side effects. New workflows must define quality constraints for every step before first execution.

### Recovery
If a step fails verification: halt execution, preserve the current state, and return the failure (step ID, constraint violated, actual output) to the planner for re-planning. Do not retry failed steps without a revised plan. For partially executed plans with irreversible side effects: log all completed steps, capture the partial system state, and surface it for human review before the planner produces a revised plan. If the planner cannot produce a valid revised plan after two attempts, escalate to human intervention.
