---
title: "Map Control Points Before Agent Deployment"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "supervision-debt-anti-pattern"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent workflows being designed or promoted from development to production"
    - "any workflow where an agent performs mutations, irreversible operations, or multi-step tasks on behalf of a user"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — control-point mapping is a design-time activity; retrofitting into deployed agents requires workflow redesign and may require infrastructure changes"
  auditability: "high when each control point classification is documented and linked to the workflow spec; low when approvals are added reactively without documented rationale"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "DD-29 (human gate) establishes blanket review before system modification but does not require upfront control-point classification per workflow. The finding raises whether MetaSystem's gates are mapped to identified control points or applied uniformly."
contract:
  preconditions: "An agent workflow has been specified and is being evaluated for production deployment. The workflow includes operations that affect external systems, data, or user state."
  invariants: "Every workflow has a control-point map completed before production deployment. Each control point is classified as: auto-approve (read-only, reversible, low-risk), human-approve (mutations, side effects, or elevated risk), or human-initiate (irreversible operations). The control-point map is a required artifact in the workflow specification, not a post-deployment addition."
  governance: "Owner: the agent, skill, or workflow spec that governs a given production workflow. Control-point mapping is a required step in the workflow specification process — no workflow reaches production without a completed map. Consumer-side audit checks that every workflow spec includes a control-point classification table."
  recovery: "If a workflow reaches production without a control-point map → treat as a governance gap; conduct retrospective mapping immediately; apply the most conservative control classification (human-approve) to any unclassified operations until reclassification is approved. If a production surprise reveals an uncovered control point → add to the map; do not patch the UI without updating the spec. If approval fatigue is detected (humans routinely bypassing approvals) → reclassify; the problem is misclassification, not the gating mechanism."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "human-in-the-loop"
  - "agent-deployment"
---

# Map Control Points Before Agent Deployment

**Source:** [[supervision-debt-anti-pattern]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent workflow is being designed or evaluated for production deployment. The workflow involves operations with side effects — mutations, irreversible actions, external system calls, or multi-step execution where intermediate states are non-trivial.

Supervision debt accrues when teams wire agents to tools and ship them before identifying where human oversight is needed. The debt compounds in production as reactive retrofits — approval buttons, audit logs, cancel mechanisms — are bolted on after production surprises rather than designed in upfront.

## Action

**Required:** Before any agent workflow is deployed to production, produce a control-point map: an explicit classification of every step where a human may need to observe, approve, steer, or cancel the agent's work. Classify each control point as auto-approve, human-approve, or human-initiate. The map must be a documented artifact in the workflow specification, not implicit in the implementation.

**Forbidden:** Deploying an agent workflow without a completed control-point map. Treating blanket approval gates as equivalent to identified control points. Adding approval or audit mechanisms reactively after production surprises without updating the workflow spec.

## Boundary

Enforced at the workflow specification stage, before any production deployment. Applies to new agent workflows and to significant revisions of existing workflows (new operations added, risk tier changed).

Does not apply to fully read-only agent workflows with no external side effects — these have no control points requiring classification by definition.

## Enforcement

- **Mechanism:** Workflow specifications must include a control-point classification table. The deployment gate checks for the presence of a completed map. Any workflow missing the map is blocked from production promotion.
- **Check (deterministic):** `control_point_map_present == true AND all_operations_classified == true` for any workflow in the production promotion queue.
- **Violation response:**
  - *Missing map:* block promotion; require the map to be completed before re-evaluating.
  - *Reactive retrofit without spec update:* treat the retrofit as ungoverned; require the workflow spec to be updated to reflect the newly identified control point.
  - *Approval fatigue detected:* investigate; misclassification is the root cause, not the gating mechanism.
- **Cannot be self-certified by the agent:** Control-point classification is a human-authored design artifact. Agents may propose a classification, but the map must be reviewed and approved by a human before production deployment.

## Rationale

Traditional web applications are built for call-and-response. They do not handle streaming work, mid-task discovery of new information, or non-deterministic execution. Retrofitting observation, approval, steering, and cancel capabilities into an architecture not designed for them is fundamentally harder than designing them in.

Supervision debt parallels technical debt: it accrues silently during development, compounds when agents reach production, and becomes expensive to repay because the approval and audit infrastructure was not designed into the system. The root issue is not the absence of UI elements — it is the absence of upfront control-point identification that would have driven those UI elements.

DD-29's human gate is a necessary but not sufficient condition. Blanket gating prevents the worst failures, but it may be its own form of debt: uniform approval friction that masks which operations genuinely need human oversight and which do not. Identified control points transform a blanket policy into a governed classification.

## Failure Modes

- **Over-identification.** Too many control points create approval fatigue; humans start bypassing approvals, which defeats the purpose. Mitigation: bias toward auto-approve for clearly read-only operations; reserve human-approve for genuine mutations and elevated-risk steps.
- **Under-classification.** Operations that look safe in development become risky at production scale or with production data. Mitigation: include a production-data review in the deployment gate; reclassify if the risk profile changes.
- **Observability theater.** Adding dashboards and logs without connecting them to actionable human decisions. Mitigation: each control point must have an actionable response path defined — not just a log entry.
- **Self-reinforcing anti-pattern.** Teams under delivery pressure skip control-point mapping, produce production surprises, and consume the bandwidth that should have gone to proper control design. Mitigation: make the control-point map a non-negotiable deployment gate, not an optional step.

## Contract

### Preconditions
An agent workflow has been specified and is being evaluated for production deployment. The workflow includes operations that affect external systems, data, or user state.

### Invariants
Every workflow has a control-point map completed before production deployment. Each control point is classified as: auto-approve (read-only, reversible, low-risk), human-approve (mutations, side effects, or elevated risk), or human-initiate (irreversible operations). The control-point map is a required artifact in the workflow specification, not a post-deployment addition.

### Governance
Owner: the agent, skill, or workflow spec that governs a given production workflow. Control-point mapping is a required step in the workflow specification process — no workflow reaches production without a completed map. Consumer-side audit checks that every workflow spec includes a control-point classification table.

### Recovery
If a workflow reaches production without a control-point map → treat as a governance gap; conduct retrospective mapping immediately; apply the most conservative control classification (human-approve) to any unclassified operations until reclassification is approved. If a production surprise reveals an uncovered control point → add to the map; do not patch the UI without updating the spec. If approval fatigue is detected (humans routinely bypassing approvals) → reclassify; the problem is misclassification, not the gating mechanism.
