---
title: "Agent Self-Report Is Insufficient: Environmental Feedback During Execution + Independent Verification at Completion"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "agent-self-reporting-unreliability-independent-eval"
contributing_sources:
  - ground-truth-environmental-feedback-loops
extraction_date: "2026-04-19"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems that execute tasks and report completion status"
    - "build pipelines with automated post-task verification gates"
    - "production agent deployments where output quality is externally measurable"
    - "development workflows relying on agent-produced artifacts"
    - "agent execution loops where ground-truth environmental signals (test runs, type checks, linter output, runtime probes, structured logs) are available at decision points"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: ["build", "verify"]
  reversibility: "trivial — prompt-level and hook-level instruction; removal is a deletion with no migration cost"
  auditability: "high when independent checks produce structured logs; low when only agent self-attestation is retained"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "MetaSystem's pre-commit hook system (linters, type checks) is a partial independent-evaluation analog; no post-task verification hooks deployed as of extraction date."
contract:
  preconditions: "Success criteria for the agent task are defined before execution begins. At least one independent verification mechanism exists for the task type."
  invariants: "No agent task is marked complete based solely on agent self-report. Verification mechanisms remain structurally independent from the agent under evaluation. Verification results are logged. Agent decision points consult environmental ground truth (tool result, test output, runtime probe) before plan-step execution. Self-narrated progress without environmental probe is forbidden as a planning input."
  governance: "Owner: Meta-System (cross-system rule). Modification requires a Design Decision. Applies to all systems that execute agent tasks."
  recovery: "Missing check: flag task as unverified, create IB item for the missing check. Check failure: block completion, surface to human, no blind retry. Broken verifier: fall back to human review until repaired."
tags:
  - "extracted-artifact"
  - "rule"
  - "environmental-feedback"
  - "ground-truth"
---

# Agent Self-Report Is Insufficient: Environmental Feedback During Execution + Independent Verification at Completion

**Source:** [[agent-self-reporting-unreliability-independent-eval]]
**Contributing source:** [[ground-truth-environmental-feedback-loops]] (per-step environmental-feedback obligation, session 84)
**Source (additional):** [[goal-backward-verification]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

The rule fires at two temporal surfaces:

1. **Task-completion (verify stage):** any time an agent completes a task, produces an output, or reports its own success/failure status — in production deployments, development workflows, or build pipelines.
2. **During execution (build stage):** any decision point during execution where the agent could consult environmental signal (tool results, test output, type checks, linter output, runtime probes, structured logs) versus proceeding on self-narration. Decision points include: after each tool call, before each next-step planning, after each subagent return, before each significant state mutation.

## Action

**Required (verify stage — post-task gate):** Agent self-reported success MUST NOT be treated as verification of output quality. An independent evaluation mechanism — automated checks, external validators, or human review — MUST verify agent outputs against defined success criteria before marking a task complete.

Specifically:
- Never ask an agent "did you do this correctly?" as the sole verification step.
- Every agent task with observable outputs must have at least one independent check defined.
- Independent checks must be structurally separate from the agent under evaluation (different process, different prompt, or deterministic code).

**Required (build stage — per-step environmental feedback):** At every meaningful decision point during execution, the agent MUST consume ground-truth signal from the environment before committing to the next plan-step:

- After each tool call: read the tool's result; do not narrate progress without reading the result.
- Before each next-step planning: confirm prior step's environmental outcome (test output, type check, file state, runtime probe) matches the plan's expectation; if it diverges, replan from observed state.
- After each subagent return: ingest the subagent's structured output; do not assume completion without examining returned artifacts.
- Self-narrated progress ("I think this worked," "the change should propagate") without environmental probe is forbidden as a planning input.

The two surfaces compose: per-step environmental feedback catches dead-end pursuit early during execution; the post-task gate catches anything that slips through. Together they bracket execution at both ends.

## Boundary

- **Build pipelines:** Pre-commit hooks, post-task verification hooks, CI checks.
- **Production deployments:** Automated output validators that run after agent task completion.
- **Development workflows:** Review gates, test suites, linter passes that verify agent-produced artifacts.
- **Session workflows:** Human review gates at stage boundaries (already enforced by DD-29).
- **Agent execution loops:** Per-step environmental probes preceding plan-step decisions (during-execution surface). Reviewable from session logs: does the agent pause to consult ground truth before each plan-step, or does it self-narrate?

The rule applies at every surface where agent state transitions are made — both task-completion boundaries (verify stage) and per-step decision points within execution (build stage). It does NOT apply to internal reasoning that the agent surfaces as transparent monologue (those are observation, not state-transition); it fires when the agent is about to commit to a plan step, declare progress, or transition the task state.

## Enforcement

- **Deterministic where possible:** Schema validation, type checks, format linters, data completeness assertions.
- **Probabilistic where necessary:** A second LLM pass with an evaluator prompt (structurally separate from the producing agent).
- **Cardinality check:** Every agent task definition must reference at least one verification mechanism. Tasks without verification references are flagged as non-compliant.
- **Per-step environmental-feedback enforcement:** Reviewable from session logs — does the agent pause to consult ground truth (tool result, test output, runtime probe) before each plan-step, or does it self-narrate? Self-narration without preceding tool call → flag plan as ungrounded.

## Rationale

Agents consistently self-report success regardless of actual outcome quality. The $14K voice agent case study (Nate B Jones) demonstrated an agent that appeared functional — handling inbound calls, reporting success — while producing scattered, unstructured data with no capturable metrics. The agent was "up and functioning" while producing unusable output. This pattern compounds over time: unchecked self-reporting creates a false sense of reliability.

The untrusted-output category extends beyond live self-reports to **agent-produced summaries** — documents like SUMMARY.md, phase completion notes, or structured completion artifacts that an agent authors about its own work. The goal-backward verification pattern ([[goal-backward-verification]]) makes this explicit: "Do NOT trust SUMMARY.md claims. Verify what ACTUALLY exists." The finding inverts typical checking direction — instead of asking whether the agent completed its checklist, the independent verifier asks whether the codebase (or output artifact) now achieves the phase's intended goal. This catches both task-level failures (something was not done) and plan-level gaps (tasks were done but the goal was not achieved). Agent-produced summaries are a form of self-report, optimistic by the same mechanism, and require the same independent verification treatment.

MetaSystem's existing hook system (pre-commit linters, type checks) is already a form of independent evaluation. This rule codifies the principle and extends it to post-task verification.

The rule extends to per-step environmental feedback during execution because the post-task gate alone is insufficient: by the time the gate fires, the agent has burned execution budget pursuing a dead-end strategy whose failure mode the gate detects. Per-step feedback catches that failure earlier, at the cheaper end of the cost curve. Anthropic's framing on this point is direct: coding agents outperform agents in domains lacking objective verification signals — direct evidence that per-step environmental feedback is not equivalent to post-task verification. The two have measurably different effects: per-step feedback prevents dead-end pursuit; post-task verification catches end-state errors. Both are required.

### Known Risks

- Over-strict checks slow workflows. Calibrate check granularity to task criticality.
- False negatives from automated checks erode trust in the verification system. Verification mechanisms need their own quality monitoring.

## Contract

### Preconditions
- Success criteria for the agent task are defined before execution begins.
- At least one independent verification mechanism exists for the task type.

### Invariants
- No agent task is marked complete based solely on the agent's own status report.
- Verification mechanisms remain structurally independent from the agent under evaluation.
- Verification results are logged (not just pass/fail — include what was checked).
- Agent decision points consult environmental ground truth (tool result, test output, runtime probe) before plan-step execution.
- Self-narrated progress without environmental probe is forbidden as a planning input.

### Governance
- **Owner:** Meta-System (cross-system rule).
- **Modification gate:** Design Decision required to alter enforcement boundaries.
- **Applicable systems:** All systems that execute agent tasks.

### Recovery
- If no independent check exists for a task type: flag the task as "unverified" and add an IB item to create the missing check.
- If an independent check fails: block task completion, surface the failure to the human operator, do not retry without diagnosis.
- If the verification mechanism itself is broken: fall back to human review until the mechanism is repaired.
