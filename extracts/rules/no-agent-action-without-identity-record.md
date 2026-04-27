---
title: "No Agent Action Without an Identity Record Bound to the Task — Identity-Gating Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "agent-identity-governance-enforcement-layer"
identification_report: "agent-governance-and-trust.harvest-queue.md::agent-identity-governance-enforcement-layer::rule::no-agent-action-without-identity-record"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "production agent deployments where actions must be auditable to a specific task and a specific human delegator"
    - "regulated environments (EU AI Act Article 14, NIST AI RMF) requiring demonstrable, traceable human oversight of AI systems"
    - "any orchestration layer that mediates between agents and external resources (APIs, databases, infrastructure, people)"
  platform_coupling: "specific:identity-aware-orchestration-layer"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — retrofitting identity binding into an agent system that already operates without it requires re-plumbing the orchestration layer; rolling back is structurally costly once deployed"
  auditability: "high when every action carries a verifiable identity record on the audit log; medium when records exist but are not validated against actions; low when relied on by convention"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-tested by Strata.io across enterprise deployments. CSA survey data: only 28% of organizations can trace agent actions back to a human sponsor — the rule's invariant is failing at scale in current practice. Regulatory pressure (EU AI Act, NIST AI RMF) is driving adoption."
contract:
  preconditions: "An agent operates in an environment where actions touch external resources (APIs, databases, files, people, infrastructure). An orchestration layer (gateway, broker, dispatcher, or equivalent) sits between the agent and those resources and can be configured to validate requests. An identity infrastructure exists that can issue, validate, and bind identity records to tasks and human delegators."
  invariants: "Every action an agent takes against an external resource carries a validated identity record at the time of the request. The identity record binds the action to (a) a specific task identifier, (b) a specific human delegator, and (c) a time-bounded validity window. The orchestration layer rejects any request that lacks a valid identity record, has an expired record, or carries a record bound to a different task. Records are append-only on the audit log; once issued, the record cannot be retroactively modified."
  governance: "Owner: the orchestration layer's policy and the identity infrastructure that issues records. The rule must be embedded as a hard reject in the orchestration layer — not advisory, not warning-only. The identity-issuing layer must implement (a) JIT provisioning (records issued at task start, scoped to that task), (b) time-bounded validity (records expire), (c) human-delegator binding (every record traces to a human authority), and (d) tamper-evident audit logging. Audit verifies every executed action has a corresponding valid identity record on the log."
  recovery: "If an action is discovered without an identity record (or with an invalid one): treat the action as un-authorized and trigger the system's anomaly response — log the event, alert the responsible human, freeze further actions on the affected resource until the identity gap is investigated. If JIT provisioning latency causes legitimate delays at task start: tune the provisioning path; do not relax the rule by allowing actions to proceed pre-provisioning. If a record is found that is bound to the wrong task or wrong delegator: revoke the record, audit the actions taken under it, treat them as un-authorized until each is reconciled."
tags:
  - "extracted-artifact"
  - "rule"
  - "agent-identity"
  - "hitl-enforcement"
  - "identity-governance"
  - "audit"
---

# No Agent Action Without an Identity Record Bound to the Task — Identity-Gating Rule

**Source:** [[agent-identity-governance-enforcement-layer]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

An agent operates in an environment where its actions touch external resources — APIs, databases, files, people, infrastructure. An orchestration layer mediates between the agent and those resources. An identity infrastructure exists that can issue records binding actions to tasks and human delegators.

Scope of application: any agent deployment where post-hoc accountability is required — production systems, regulated environments, multi-tenant platforms, or any setting where "who took this action and why" must be answerable from the audit log alone.

## Action

**Required:** Every action an agent takes against an external resource must carry a validated identity record at the time the request reaches the orchestration layer. The identity record binds:

1. **A specific task identifier** — what work the agent is doing.
2. **A specific human delegator** — which authorized human delegated this work.
3. **A time-bounded validity window** — when the record expires.

The orchestration layer validates the record on every request. Missing record, expired record, mismatched task, or mismatched delegator → request rejected.

The identity record is JIT-provisioned: issued at task start, scoped to the task, expiring with the task. No pre-provisioned static accounts. The record is logged append-only at issuance.

**Forbidden:** Allowing any agent action to reach an external resource without a validated identity record. Pre-provisioning static identities for "agents in general" rather than scoping per task. Allowing the orchestration layer to issue advisory warnings instead of hard rejects. Modifying or deleting identity records after issuance.

## Boundary

Enforced at the orchestration layer — the gateway through which agent actions reach external resources. Applies to every request type the orchestration layer mediates: API calls, database queries, file operations, human-approval requests, infrastructure changes.

Out of scope: actions that occur entirely within the agent's own context (computation, reasoning, internal state changes) and never touch the orchestration layer. The rule fires at the first request that crosses into shared or external state.

## Enforcement

- **Mechanism:** The orchestration layer is configured to require a valid identity record on every request. The validation is structural, not advisory: requests without a valid record receive a synchronous reject. The identity-issuing layer (JIT provisioning, OAuth On-Behalf-Of, equivalent) provides records that the orchestration layer can verify cryptographically or via a trusted lookup.
- **Check (deterministic):** For every action `A` reaching the orchestration layer: `identity_record(A) != null` AND `validated(identity_record(A)) == true` AND `now < identity_record(A).expires_at` AND `identity_record(A).task == A.task` AND `identity_record(A).delegator in authorized_delegators_for(A.task)`. Any branch false → request rejected.
- **Violation response:**
  - *Action attempted without record:* request rejected; event logged; agent receives a structured failure that distinguishes "missing identity" from other reject causes (so retry logic can request provisioning rather than retrying blindly).
  - *Expired record:* same — re-provision through the identity layer; do not extend or reuse expired records.
  - *Wrong-task or wrong-delegator binding:* request rejected; event logged as a potential misconfiguration or boundary violation; investigate.
  - *Action discovered post-hoc with no matching record:* treat as un-authorized; trigger anomaly response; freeze further action on the affected resource until investigation completes.
- **Cannot be relaxed for convenience:** The rule does not permit advisory-only enforcement. If JIT provisioning is too slow for a workload, the fix is to make provisioning faster — not to allow ungated actions while provisioning catches up.

## Rationale

The rule exists because audit and accountability collapse without identity binding. An agent action without a tied identity is an action without an answer to "who did this and why" — which makes incident response, regulatory compliance, and trust calibration all impossible. The pre-AI default of static service accounts cannot survive at agent volumes; per-task JIT provisioning is the structural replacement.

Industry data shows the problem is widespread: only 28% of organizations can trace agent actions back to a human sponsor (CSA survey). The other 72% cannot answer the most basic accountability question. The rule fixes this by making the orchestration layer reject ungated actions at the request boundary — turning identity from a logging concern into a hard gate.

The three components of the binding (task, delegator, time-bounded validity) are jointly necessary. Task binding prevents reuse of one task's record on another task's actions. Delegator binding prevents agent self-delegation. Time-bounded validity prevents stale records from accreting authority indefinitely.

The rule is the positive-space restatement of the unaccountable-action anti-pattern. Rather than enumerating ways accountability can fail (untraceable actions, shared service accounts, agent self-authorization, post-hoc identity guessing), the positive invariant is "every action has a binding record at request time." One rule, deterministic enforcement.

## Failure Modes

- **JIT provisioning latency.** Issuing identity records at task start adds latency that may be unacceptable for time-sensitive work. Mitigation: tune the provisioning path; pre-warm provisioning for predictable task patterns; do not relax the rule.
- **Static-fallback creep.** Under deadline pressure, a static service account is configured as a fallback when provisioning fails. Mitigation: the orchestration layer rejects static accounts that aren't bound to a task; treat any "fallback to static" path as a violation, regardless of how it was rationalized at config time.
- **Delegator-binding theater.** The delegator field is filled with a generic "system" or "ops-team" identity that doesn't trace to an accountable human. Mitigation: enforce that the delegator is a real human identity with audit traceability; reject system-account delegators.
- **Record-extension creep.** Records are extended when they expire mid-task instead of being re-provisioned. Mitigation: expiration is hard; re-provisioning issues a new record; the audit log captures the boundary cleanly. Extension is a violation.
- **Audit-log disconnection.** Identity records are issued but the orchestration layer's audit log doesn't preserve the record alongside the action. Mitigation: action and record are written to the audit log atomically; an action log entry without a corresponding record entry is itself a violation.
- **Over-engineering for low-risk agent systems.** Small-scale or single-user agent deployments adopt full identity infrastructure when simpler scoping (e.g., per-user OAuth) would suffice. Mitigation: the rule is about *binding records to tasks and delegators*; the implementation can be simpler than enterprise JIT for low-stakes deployments — but the binding invariant remains.

## Contract

### Preconditions
An agent operates in an environment where actions touch external resources (APIs, databases, files, people, infrastructure). An orchestration layer (gateway, broker, dispatcher, or equivalent) sits between the agent and those resources and can be configured to validate requests. An identity infrastructure exists that can issue, validate, and bind identity records to tasks and human delegators.

### Invariants
Every action an agent takes against an external resource carries a validated identity record at the time of the request. The identity record binds the action to (a) a specific task identifier, (b) a specific human delegator, and (c) a time-bounded validity window. The orchestration layer rejects any request that lacks a valid identity record, has an expired record, or carries a record bound to a different task. Records are append-only on the audit log; once issued, the record cannot be retroactively modified.

### Governance
Owner: the orchestration layer's policy and the identity infrastructure that issues records. The rule must be embedded as a hard reject in the orchestration layer — not advisory, not warning-only. The identity-issuing layer must implement (a) JIT provisioning (records issued at task start, scoped to that task), (b) time-bounded validity (records expire), (c) human-delegator binding (every record traces to a human authority), and (d) tamper-evident audit logging. Audit verifies every executed action has a corresponding valid identity record on the log.

### Recovery
If an action is discovered without an identity record (or with an invalid one): treat the action as un-authorized and trigger the system's anomaly response — log the event, alert the responsible human, freeze further actions on the affected resource until the identity gap is investigated. If JIT provisioning latency causes legitimate delays at task start: tune the provisioning path; do not relax the rule by allowing actions to proceed pre-provisioning. If a record is found that is bound to the wrong task or wrong delegator: revoke the record, audit the actions taken under it, treat them as un-authorized until each is reconciled.
