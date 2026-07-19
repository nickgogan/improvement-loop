---
title: "Deterministic Execution Boundary — Planner-Executor Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "planner-executor-deterministic-guardrails"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "engineers building planner-executor or plan/execute/verify agent architectures, where an LLM produces a plan and a separate phase carries it out"
    - "tool-heavy or side-effecting workflows — database writes, code changes, deployments, outbound API calls — where an ungoverned model action could trigger an irreversible mistake"
    - "teams drawing an explicit line between where model judgment is permitted (planning) and where only validated, deterministic actions may run (execution)"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — refactoring a mixed plan-and-act loop into a plan/execute/verify split is an architectural change (extract the plan format, strip reasoning from the executor, add the verifier); undoing it means re-merging the phases, so it is neither trivial nor irreversible"
  auditability: "high — the executor phase can be inspected for any LLM/agent call; the presence of a model call inside execution is a visible, node-level violation, and the plan format is an explicit artifact that can be checked against schema"
  evidence_strength: "Strong"
  adoption:
    status: "Partially Adopted"
    notes: "A version is implemented in a plan-phase/execute-phase/verify-phase planning plugin; Microsoft Agent Framework separates agent orchestration (LLM-driven) from workflow orchestration (deterministic) as first-class primitives; corroborated from enterprise multi-agent deployments (the 'don't let the agent decide the track' analogy)."
contract:
  preconditions: "An agent workflow is structured (or is being structured) into distinct planning and execution responsibilities, and the executor performs actions with side effects (tool calls, file edits, DB writes, deploys). A plan or step format exists (or can be defined) that the executor can validate against schema before acting."
  invariants: "All model judgment is confined to the planning phase. Once a plan is finalized, the executor runs its steps with zero LLM reasoning — only schema validation and tool invocation. Compliance controls and retry logic in the executor are deterministic, not model-driven. A verifier checks each step's output against the plan's quality constraints before the next step proceeds."
  governance: "Owner: whoever designs or maintains the agent architecture / orchestrator, and any skill that modifies files or external systems. The plan/execute boundary must be explicit in the harness, skill, or workflow definition — it is not satisfied by an LLM 'trying' to only act on validated plans. Consumer-side design/audit tooling should verify that side-effecting skills declare the separation."
  recovery: "If an LLM/agent call is discovered inside the executor phase, move the judgment it performs up into the planning phase and replace the executor step with schema validation + tool invocation. If the executor encounters a runtime state the plan does not cover, halt and re-plan — probabilistic re-planning happens in the planner, never inline in the executor. If the verifier passes a bad output, tighten the plan's quality constraints rather than adding judgment to the executor."
tags:
  - "extracted-artifact"
  - "rule"
---

# Deterministic Execution Boundary — Planner-Executor Rule

**Source:** [[planner-executor-deterministic-guardrails]]
**Form:** rule
**Extraction date:** 2026-07-19

> **Related rule (same family, distinct scope):** [[deterministic-nodes-for-non-reasoning-steps]] is the general per-node audit heuristic — for *each* node in *any* workflow graph, ask "does this step need reasoning?" and make it deterministic if not, while explicitly retaining LLM calls for nodes that do need judgment. This rule is the stricter *architectural phase-boundary* claim specific to a planner-executor(-verifier) split: the entire executor phase is deterministic by construction (the judgment already happened during planning), with no per-node reasoning exception at execution time. Ruled create-new (not a merge into the general rule) per the 2026-07-19 extension-proposals report — the two are complementary siblings: apply the general node-audit when you are *not* using a planner-executor split; apply this phase-boundary rule when you are.

## Condition

An agent workflow is organized into a planning phase and an execution phase — or is a candidate to be (a plan/execute/verify architecture). The executor carries out steps that produce side effects: tool invocations, file edits, database queries, deployments, outbound API calls. Fires whenever such an architecture is designed, reviewed, or found to be mixing planning and acting in one probabilistic loop.

## Action

**Required:** Confine all model judgment to the planning phase. The planner (LLM) produces an explicit step plan with dependencies and quality constraints. The executor then runs each step **deterministically** — schema validation and tool invocation only, no LLM reasoning during execution. A verifier checks each step's output against the plan's quality constraints before the next step proceeds. Compliance controls and retry logic in the executor are deterministic, not model-driven.

**Forbidden:** Any LLM/agent call inside the executor phase. Letting the model decide step order, re-interpret the plan, or improvise an action at execution time. Mixing "figure out what to do" and "do it" in a single probabilistic step when the step has side effects.

**Permitted:** Probabilistic reasoning during planning (that is the planner's whole job) and during an explicit *re-planning* hop back into the planner when the executor hits a state the plan does not cover.

## Boundary

Enforced at the plan/execute seam. The boundary is the moment a plan is finalized and handed to the executor: everything upstream may be probabilistic; everything downstream must be deterministic. Applies to any workflow with side effects; it does not apply to a pure single-shot generation with no actions to execute (there is no execution phase to govern).

## Enforcement

- **Mechanism:** Inspect the executor's implementation. Every executor step must resolve to schema validation or a tool call with fixed logic — never a model completion. The plan format is an explicit artifact; the executor validates against it before acting.
- **Check:** For the execution phase `E`: `count(LLM_calls in E) == 0`. Any model call reachable from the executor is a violation. Separately: every finalized plan step passes schema validation before its tool is invoked, and its output passes the verifier before the next step runs.
- **Violation response:** A model call found in the executor → lift its judgment into the planner and replace the step with validation + invocation. An uncovered runtime state → halt and re-plan (in the planner), never improvise in the executor. A verifier passing invalid output → tighten the plan's quality constraints, not the executor's autonomy.

## Rationale

When planning and execution are mixed, a single model hallucination can trigger an irreversible side effect — a wrong DB write, an incorrect deployment, a malformed API call. The deterministic execution boundary guarantees that only *validated plans* produce actions: the stochastic surface is pushed entirely into the planning phase, where mistakes are cheap (a bad plan is caught by the verifier before any action fires), and kept out of the phase where mistakes are expensive (execution with side effects).

The architectural insight is that the plan/execute boundary is itself a *categorical* answer to "does this step need reasoning?": once the plan is finalized, every downstream step is non-reasoning **by construction** — the judgment already happened during planning. This is why the executor needs no per-node reasoning exception (contrast the general node-audit sibling, which preserves LLM calls for individual nodes that genuinely need judgment). The agent's value is *within* each planned step (composing text, calling a tool correctly), not in deciding the step order at run time.

## Failure Modes

- **Over-rigid plans.** A finalized plan cannot adapt to a runtime condition it did not anticipate. Mitigation: an explicit re-planning hop — the executor halts and hands control back to the planner, rather than the executor improvising. Re-planning stays probabilistic; execution stays deterministic.
- **Syntactically valid, semantically wrong plan.** The planner emits steps that pass schema validation but are wrong. Mitigation: the verifier's quality constraints, not executor judgment — strengthen what the verifier checks.
- **Weak verifier.** The verifier passes invalid outputs due to insufficient quality constraints, and the bad output propagates. Mitigation: treat verifier constraints as a first-class part of the plan format; tighten them rather than reintroducing model judgment into execution.
- **Boundary erosion.** A "small" model call sneaks into the executor "just to handle one edge case." Mitigation: the enforcement check is zero LLM calls in the executor — any nonzero count is a violation, regardless of how small the call seems.

## Contract

### Preconditions
An agent workflow is structured (or is being structured) into distinct planning and execution responsibilities, and the executor performs actions with side effects (tool calls, file edits, DB writes, deploys). A plan or step format exists (or can be defined) that the executor can validate against schema before acting.

### Invariants
All model judgment is confined to the planning phase. Once a plan is finalized, the executor runs its steps with zero LLM reasoning — only schema validation and tool invocation. Compliance controls and retry logic in the executor are deterministic, not model-driven. A verifier checks each step's output against the plan's quality constraints before the next step proceeds.

### Governance
Owner: whoever designs or maintains the agent architecture / orchestrator, and any skill that modifies files or external systems. The plan/execute boundary must be explicit in the harness, skill, or workflow definition — it is not satisfied by an LLM "trying" to only act on validated plans. Consumer-side design/audit tooling should verify that side-effecting skills declare the separation.

### Recovery
If an LLM/agent call is discovered inside the executor phase, move the judgment it performs up into the planning phase and replace the executor step with schema validation + tool invocation. If the executor encounters a runtime state the plan does not cover, halt and re-plan — probabilistic re-planning happens in the planner, never inline in the executor. If the verifier passes a bad output, tighten the plan's quality constraints rather than adding judgment to the executor.
