---
title: "Agent Self-Reporting Unreliability and Independent Evaluation Requirement"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "agent-self-reporting-unreliability-independent-eval"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems that execute tasks and report completion status"
    - "build pipelines with automated post-task verification gates"
    - "production agent deployments where output quality is externally measurable"
    - "development workflows relying on agent-produced artifacts"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — prompt-level and hook-level instruction; removal is a deletion with no migration cost"
  auditability: "high when independent checks produce structured logs; low when only agent self-attestation is retained"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "MetaSystem's pre-commit hook system (linters, type checks) is a partial independent-evaluation analog; no post-task verification hooks deployed as of extraction date."
contract:
  preconditions: "Success criteria for the agent task are defined before execution begins. At least one independent verification mechanism exists for the task type."
  invariants: "No agent task is marked complete based solely on agent self-report. Verification mechanisms remain structurally independent from the agent under evaluation. Verification results are logged."
  governance: "Owner: Meta-System (cross-system rule). Modification requires a Design Decision. Applies to all systems that execute agent tasks."
  recovery: "Missing check: flag task as unverified, create IB item for the missing check. Check failure: block completion, surface to human, no blind retry. Broken verifier: fall back to human review until repaired."
tags:
  - "extracted-artifact"
  - "rule"
---

# Agent Self-Reporting Unreliability and Independent Evaluation Requirement

**Source:** [[agent-self-reporting-unreliability-independent-eval]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

Any time an agent completes a task, produces an output, or reports its own success/failure status — in production deployments, development workflows, or build pipelines.

## Action

Agent self-reported success MUST NOT be treated as verification of output quality. An independent evaluation mechanism — automated checks, external validators, or human review — MUST verify agent outputs against defined success criteria before marking a task complete.

Specifically:
- Never ask an agent "did you do this correctly?" as the sole verification step.
- Every agent task with observable outputs must have at least one independent check defined.
- Independent checks must be structurally separate from the agent under evaluation (different process, different prompt, or deterministic code).

## Boundary

- **Build pipelines:** Pre-commit hooks, post-task verification hooks, CI checks.
- **Production deployments:** Automated output validators that run after agent task completion.
- **Development workflows:** Review gates, test suites, linter passes that verify agent-produced artifacts.
- **Session workflows:** Human review gates at stage boundaries (already enforced by DD-29).

## Enforcement

- **Deterministic where possible:** Schema validation, type checks, format linters, data completeness assertions.
- **Probabilistic where necessary:** A second LLM pass with an evaluator prompt (structurally separate from the producing agent).
- **Cardinality check:** Every agent task definition must reference at least one verification mechanism. Tasks without verification references are flagged as non-compliant.

## Rationale

Agents consistently self-report success regardless of actual outcome quality. The $14K voice agent case study (Nate B Jones) demonstrated an agent that appeared functional — handling inbound calls, reporting success — while producing scattered, unstructured data with no capturable metrics. The agent was "up and functioning" while producing unusable output. This pattern compounds over time: unchecked self-reporting creates a false sense of reliability.

MetaSystem's existing hook system (pre-commit linters, type checks) is already a form of independent evaluation. This rule codifies the principle and extends it to post-task verification.

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

### Governance
- **Owner:** Meta-System (cross-system rule).
- **Modification gate:** Design Decision required to alter enforcement boundaries.
- **Applicable systems:** All systems that execute agent tasks.

### Recovery
- If no independent check exists for a task type: flag the task as "unverified" and add an IB item to create the missing check.
- If an independent check fails: block task completion, surface the failure to the human operator, do not retry without diagnosis.
- If the verification mechanism itself is broken: fall back to human review until the mechanism is repaired.
