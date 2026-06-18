---
title: "AGUI Boundary Control-Points Specification"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "agui-human-control-layer-not-ui"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic workflows where human oversight gates must be designed explicitly before implementation"
    - "any system composing multiple agent steps that will run with varying levels of autonomy"
    - "teams auditing existing agent systems for missing or implicit human control points"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "low — changing a control-point classification after the workflow is deployed may require re-wiring approval hooks; specification changes before deployment are trivial"
  auditability: "high — the specification document is the audit record; each row's classification and rationale are inspectable; changes are diffable"
  evidence_strength: "Anecdotal"
  adoption:
    status: "Not Yet Started"
    notes: "AGUI protocol is still maturing as of 2026-05-24. The control-points framing is inferred from Google I/O presentation analysis and the supervision-debt anti-pattern. MetaSystem's DD-29 (human gate discipline) serves an equivalent function conversationally — this template would formalize that discipline as a structured contract."
contract:
  preconditions: "The agent workflow has been decomposed into a sequence of named steps. The system designer can enumerate every step and knows approximately what action occurs in each. The deployment context (fully autonomous, human-in-the-loop, human-on-the-loop) has been chosen."
  invariants: "Every step in the workflow has a control-point classification (observe / approve / cancel). Every approve-classified step has a stated rationale. No step is left unclassified. The completed specification exists as a persistent artifact before the workflow is implemented."
  governance: "Owner: the agent system's designer or architect. The specification must be completed before implementation begins. Any post-deployment change to a control-point classification is a design change requiring explicit review. Consumer agents (builders, reviewers) check that the implemented workflow matches the specification."
  recovery: "If a step's classification is disputed after implementation → revert to the specification, treat the specification as authoritative, and update the implementation to match. If supervision debt is discovered (a control point was not implemented) → add the missing gate immediately and log it as a finding. If the workflow is refactored and new steps are added → re-run the classification pass on the amended step list before deploying the refactored version."
tags:
  - "extracted-artifact"
  - "template"
  - "human-in-the-loop"
  - "orchestration"
  - "governance"
---

# AGUI Boundary Control-Points Specification

**Source:** [[agui-human-control-layer-not-ui]]
**Form:** template
**Extraction date:** 2026-05-25

A specification template for identifying and classifying human control points across every step of an agentic workflow. Fill in one specification per workflow before implementation begins. The goal is to make every "where does a human intervene?" decision explicit rather than leaving it implicit or retrofitting it after errors emerge.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{WORKFLOW_NAME}}` | Name of the agentic workflow being specified | Yes |
| `{{WORKFLOW_PURPOSE}}` | One-sentence description of what the workflow accomplishes | Yes |
| `{{AUTONOMY_LEVEL}}` | Overall autonomy level: `fully-autonomous`, `human-in-the-loop`, or `human-on-the-loop` | Yes |
| `{{STEP_N_NAME}}` | Name of step N in execution order | Yes |
| `{{STEP_N_ACTION}}` | Plain-English description of what happens in this step | Yes |
| `{{STEP_N_CLASSIFICATION}}` | One of: `observe`, `approve`, `cancel` | Yes |
| `{{STEP_N_RATIONALE}}` | Why this classification was chosen (required for `approve` and `cancel`) | Conditional |
| `{{STEP_N_SURFACE}}` | How the human interacts at this step (UI element, chat message, hook, etc.) | No |
| `{{STEP_N_TIMEOUT}}` | How long to wait for human response before auto-proceeding or halting | No |
| `{{ESCALATION_PATH}}` | What happens if no human responds within the timeout | Yes (if any timeouts defined) |
| `{{SPEC_AUTHOR}}` | Name or role of the person completing this specification | Yes |
| `{{SPEC_DATE}}` | Date the specification was completed | Yes |

## Body

```markdown
# Control-Points Specification: {{WORKFLOW_NAME}}

**Purpose:** {{WORKFLOW_PURPOSE}}
**Autonomy level:** {{AUTONOMY_LEVEL}}
**Author:** {{SPEC_AUTHOR}}
**Date:** {{SPEC_DATE}}

---

## Classification Key

| Classification | Meaning |
|----------------|---------|
| `observe` | Human receives real-time visibility into this step; no action required |
| `approve` | Human must explicitly approve before this step proceeds |
| `cancel` | Human can interrupt and cancel at this step; proceeds automatically otherwise |

---

## Step Classification Table

| # | Step Name | Action | Classification | Rationale | Surface | Timeout |
|---|-----------|--------|----------------|-----------|---------|---------|
| 1 | {{STEP_1_NAME}} | {{STEP_1_ACTION}} | {{STEP_1_CLASSIFICATION}} | {{STEP_1_RATIONALE}} | {{STEP_1_SURFACE}} | {{STEP_1_TIMEOUT}} |
| 2 | {{STEP_2_NAME}} | {{STEP_2_ACTION}} | {{STEP_2_CLASSIFICATION}} | {{STEP_2_RATIONALE}} | {{STEP_2_SURFACE}} | {{STEP_2_TIMEOUT}} |
| 3 | {{STEP_3_NAME}} | {{STEP_3_ACTION}} | {{STEP_3_CLASSIFICATION}} | {{STEP_3_RATIONALE}} | {{STEP_3_SURFACE}} | {{STEP_3_TIMEOUT}} |

*Add rows for all steps. No step may be left unclassified.*

---

## Escalation

**If a human does not respond within the specified timeout:**
{{ESCALATION_PATH}}

---

## Supervision Debt Audit

*Complete this section when updating an existing specification.*

| Previously missing control point | Step it belongs to | Classification assigned | Date added |
|-----------------------------------|--------------------|------------------------|-----------|
| — | — | — | — |

---

## Approval

This specification must be reviewed and signed off before workflow implementation begins.

| Reviewer | Role | Sign-off date |
|----------|------|---------------|
| — | — | — |
```

## Usage

1. Enumerate every step in the workflow (including error-handling branches if they have distinct actions).
2. Classify each step as `observe`, `approve`, or `cancel`. Start permissive — it is easier to add gates than remove them.
3. Write a rationale for every step classified `approve` or `cancel`. Rationale-free classifications indicate implicit assumptions that should be surfaced.
4. Identify the human surface for each gated step — a chat response, a UI button, a hook confirmation, or a file write.
5. Get sign-off before implementation. The specification is the contract; the implementation must match it.

## Variation Axis

| Variation | Adaptation |
|-----------|-----------|
| Fully autonomous workflow | All steps classified `observe`; the specification documents that choice explicitly rather than leaving it implicit |
| Tiered autonomy (some steps autonomous, some gated) | Mix classifications per step; document the rationale for each gate especially carefully |
| Retroactive audit of existing workflow | Use the Supervision Debt Audit table to record control points added after deployment |
| Sub-workflow composition | Nest specifications — each sub-workflow has its own specification; the parent specification references child specs |
| Time-sensitive workflow (tight timeouts) | Define the escalation path precisely; consider whether auto-proceed or auto-halt is safer for each step |

## Contract

### Preconditions
The agent workflow has been decomposed into a sequence of named steps. The system designer can enumerate every step and knows approximately what action occurs in each. The deployment context (fully autonomous, human-in-the-loop, human-on-the-loop) has been chosen.

### Invariants
Every step in the workflow has a control-point classification (observe / approve / cancel). Every approve-classified step has a stated rationale. No step is left unclassified. The completed specification exists as a persistent artifact before the workflow is implemented.

### Governance
Owner: the agent system's designer or architect. The specification must be completed before implementation begins. Any post-deployment change to a control-point classification is a design change requiring explicit review. Consumer agents (builders, reviewers) check that the implemented workflow matches the specification.

### Recovery
If a step's classification is disputed after implementation → revert to the specification, treat the specification as authoritative, and update the implementation to match. If supervision debt is discovered (a control point was not implemented) → add the missing gate immediately and log it as a finding. If the workflow is refactored and new steps are added → re-run the classification pass on the amended step list before deploying the refactored version.
