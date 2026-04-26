---
title: Explicit Permission Allow-Listing for Agent Resource Access
type: extracted-artifact
assigned_form: rule
source_finding: explicit-permission-allow-listing-for-agent-resou
extraction_date: '2026-04-26'
identification_report: 2026-04-26-identification-report.md
deployed: false
deployed_to: null
context:
  applies_to:
  - teams building or deploying agents that take real-world actions (file writes, API calls, email, calendar, database operations)
  - organizations where credential leaks or unsanctioned agent actions would cause compliance, financial, or reputational harm
  - any agentic workflow where the agent's access to external resources should be auditable and bounded by explicit human approval
  platform_coupling: agnostic
  autonomy: hitl-only
  stage: secure
  reversibility: low — adding allow-list infrastructure requires design changes to the agent orchestration layer; undoing an unauthorized access (deleted files, sent emails) may be impossible
  auditability: high — every approval event is logged with resource, access type, task context, and operator identity; compliance is externally verifiable by inspecting the audit log against the allow-list
  evidence_strength: Strong
  adoption:
    status: Not Yet Started
    notes: null
contract:
  preconditions: The agentic system has a mechanism to intercept resource access requests before they execute (hook, middleware, or skill-level gate). The operator is present and reachable at the time the
    agent runs — or the agent has a queuing mechanism for approval when the operator is unavailable. An allow-list store (session-scoped or persistent) is available for recording approvals.
  invariants: No resource access occurs without a corresponding entry in the allow-list, either pre-populated by the operator or granted at runtime. The allow-list is append-only for grants during a session;
    removals require explicit operator action. The audit log records every approval event and is not modifiable by the agent. Access types are granular enough that read approval does not imply write approval.
  governance: 'Owner: the team or individual responsible for the agentic system''s security posture. Allow-list entries are operator-owned: the agent may prompt for approval but may not self-grant. Audit
    logs are operator-readable and must be retained per the organization''s audit retention policy. Any change to the allow-list schema or trust-tier groupings requires operator review.'
  recovery: 'If an unauthorized access is detected: immediately revoke the agent''s current session access; audit the allow-list for gaps that enabled the bypass; investigate whether the agent circumvented
    the approval gate or the gate was absent. If permission fatigue is causing blind approvals: restructure the allow-list into broader trust tiers; pre-approve read-only access for known-safe resources;
    reduce approval surface to writes and executions only.'
tags:
- extracted-artifact
- rule
---

# Explicit Permission Allow-Listing for Agent Resource Access

**Source:** [[explicit-permission-allow-listing-for-agent-resou]]
**Form:** rule
**Extraction date:** 2026-04-26

## Condition

An agent is about to access a resource (file path, API endpoint, external service, system capability) that has not been previously approved for that agent in the current session or persistent allow-list. This rule fires at the moment the agent would issue the access request — before the request is executed.

This rule applies in any agentic system where agents can take real-world actions: file modification, API calls, email or calendar operations, database writes, or any other non-read-only effect.

## Action

**Required:** Before accessing a novel resource, the agent must surface the access request to a human operator for explicit approval. The request must identify: (1) the specific resource being accessed, (2) the type of access (read, write, execute, delete), and (3) the task context that requires the access. The human must affirmatively grant or deny before the access proceeds.

**Forbidden:**
- Proceeding with resource access that has not been explicitly approved
- Inferring approval from task context ("the task asked me to send an email, so email access is implicitly approved")
- Treating silence or ambiguity as approval
- Batching multiple novel resource accesses into a single approval request that obscures individual access types

**Permitted:**
- Persisting approved access in a session-scoped or persistent allow-list so that the same resource does not trigger repeat approval dialogs within the same scope
- Grouping resources by trust level (read-only, read-write, execute) in the allow-list to reduce approval overhead for similar access patterns

## Boundary

Enforced at the tool call layer — the moment before any agentic action that touches an external resource. For systems with hook infrastructure, this is a PreToolUse gate. For systems without hooks, it is an explicit approval step embedded in the skill or workflow before any resource-touching command is issued.

## Enforcement

- **Mechanism:** Maintain an allow-list of approved resources and access types. On every resource access attempt, check the allow-list first. If the (resource, access-type) pair is not present, halt and surface the approval prompt before proceeding.
- **Check (deterministic):** `allow_list.contains(resource_id, access_type) == true` before execution. Any false → approval prompt required.
- **Audit trail:** Every approval (grant or deny) is logged with timestamp, resource identifier, access type, task context, and operator identity. This log is the primary compliance artifact.
- **Violation response:**
  - Agent accesses a resource without approval → the action is treated as unauthorized; escalate to operator review; investigate how the allow-list check was bypassed.
  - Operator approves blindly under permission fatigue → review approval dialog design; simplify or batch lower-risk access types to reduce cognitive load.
- **Permission fatigue mitigation:** If approval dialogs become so frequent that operators approve reflexively, the allow-list design needs restructuring (broader trust tiers, pre-approved read-only scope, or per-skill permission profiles).

## Rationale

Real-world agentic failures — leaked credentials, deleted data, unsanctioned external actions — share a common root cause: the agent was granted or assumed access to resources beyond what the task required, and no human was in the loop when the boundary was crossed. Explicit allow-listing is the structural enforcement of least-privilege access: the agent can only touch what a human has affirmatively approved.

The security model mirrors mobile OS permission dialogs, which have proven effective precisely because they are point-in-time, specific, and require active user decision. The alternative — read-only scoped connectors, role-based profiles — can reduce dialog frequency but must still bottom out at explicit human approval for novel or elevated access.

For enterprise and business contexts, the audit trail produced by this rule is a prerequisite for regulatory compliance and incident investigation. Implicit access leaves no record; explicit approval produces one.

## Contract

### Preconditions
The agentic system has a mechanism to intercept resource access requests before they execute (hook, middleware, or skill-level gate). The operator is present and reachable at the time the agent runs — or the agent has a queuing mechanism for approval when the operator is unavailable. An allow-list store (session-scoped or persistent) is available for recording approvals.

### Invariants
No resource access occurs without a corresponding entry in the allow-list, either pre-populated by the operator or granted at runtime. The allow-list is append-only for grants during a session; removals require explicit operator action. The audit log records every approval event and is not modifiable by the agent. Access types are granular enough that read approval does not imply write approval.

### Governance
Owner: the team or individual responsible for the agentic system's security posture. Allow-list entries are operator-owned: the agent may prompt for approval but may not self-grant. Audit logs are operator-readable and must be retained per the organization's audit retention policy. Any change to the allow-list schema or trust-tier groupings requires operator review.

### Recovery
If an unauthorized access is detected: immediately revoke the agent's current session access; audit the allow-list for gaps that enabled the bypass; investigate whether the agent circumvented the approval gate or the gate was absent. If permission fatigue is causing blind approvals: restructure the allow-list into broader trust tiers; pre-approve read-only access for known-safe resources; reduce approval surface to writes and executions only.
