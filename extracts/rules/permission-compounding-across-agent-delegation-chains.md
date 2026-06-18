---
title: "Permissions Narrow Monotonically Across Delegation Chains"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "permission-compounding-across-agent-delegation-chains"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-agent workflows where a parent agent spawns or delegates to subagents"
    - "orchestration layers that mediate agent-to-agent handoffs"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — permission narrowing constraints are specified at orchestration design time; retrofitting into an existing multi-agent architecture requires redesigning delegation contracts"
  auditability: "high when each delegation event records the granted permission subset; low when orchestration layers pass credentials through without logging the effective scope at each step"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent is about to delegate a subtask to another agent. The delegating agent holds a defined permission scope. The target system or subagent accepts credentials or a permission token from the delegator."
  invariants: "The subagent's granted permissions are a strict subset of the delegating agent's permissions at the moment of delegation. No delegation step adds permissions — it can only reduce or preserve them. The compound permission surface across all active subagents is enumerable and auditable at any point during execution."
  governance: "Owner: the orchestration layer or skill that defines how parent agents spawn subagents. Permission subsets must be declared explicitly in the delegation contract — no implicit credential inheritance. Audit tooling validates that no delegation event grants a superset of the delegator's permissions. Applies at agent-spawn time and at any mid-task re-delegation."
  recovery: "If a subagent requires permissions the delegating agent does not hold → escalate the request to a human gate rather than elevating the delegating agent's scope. If an implicit credential inheritance is discovered at runtime → halt the delegation chain; the compound permission surface is undefined. If audit reveals a subagent held permissions beyond its delegator's scope → treat as a governance violation; revoke, log, and classify the root cause."
tags:
  - "extracted-artifact"
  - "rule"
  - "permissions"
  - "agent-delegation"
  - "governance"
---

# Permissions Narrow Monotonically Across Delegation Chains

**Source:** [[permission-compounding-across-agent-delegation-chains]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent is delegating work to another agent (spawning a subagent, handing off a subtask, or passing a credential to a downstream service). The delegating agent holds a defined permission scope. The delegation boundary is a point where permission compounding can silently occur.

Applies to any multi-agent topology: hierarchical (parent/subagent), peer-to-peer handoff, or sequential pipeline where one agent's output authorizes the next agent's action.

## Action

**Required:** At each delegation boundary, explicitly define the permission subset being granted. The granted subset must be equal to or smaller than the delegating agent's current scope. Record the granted scope as a first-class artifact in the delegation event log.

**Forbidden:** Passing through credentials, tokens, or permission contexts without explicitly narrowing them. Allowing a subagent to inherit the full permission scope of a broader orchestrator by default. Treating compound permissions across all active subagents as an implementation detail rather than a governed invariant.

## Boundary

Enforced at every delegation event — the moment a parent agent creates, spawns, or hands off to another agent. Also applies at mid-task re-delegation (when a subagent further delegates to another agent).

Does not apply to single-agent workflows operating on their own credentials without delegation intermediaries.

## Enforcement

- **Mechanism:** Each agent spawn or delegation call must include an explicit permission parameter (allowlist of tools, data scopes, or system access) rather than inheriting ambient context. The orchestration layer validates that the granted set is a subset of the delegator's current scope before the delegation executes.
- **Check (deterministic):** `granted_permissions ⊆ delegator_permissions` at every delegation event. Any violation → block the delegation.
- **Violation response:**
  - *Superset granted:* block; require explicit human approval to proceed with elevated scope.
  - *Implicit inheritance detected:* treat as a violation; make implicit scope explicit and reduce to the minimum required.
  - *Compound audit fails:* enumerate all active subagent permission sets; identify the violation point; revoke excess permissions and log.
- **Cannot be self-certified by agents:** Enforced at the orchestration layer, not by agent self-reporting. An agent cannot grant permissions it does not hold — this must be checked structurally, not behaviorally.

## Rationale

Human delegation naturally bounds permission compounding through screen-mediated access: a colleague sees only what their screen shows them. Agent delegation has no such implicit bound. Each system the agent touches evaluates access independently, and the compound access across all systems is nobody's explicit design — until it produces a breach.

The production precedent (Lilly incident) demonstrated a single-agent version: one agent accessing 22 unauthenticated endpoints across a single platform. Multi-agent compounding is worse because the permission surface grows combinatorially with each delegation step. Monotonic narrowing is the only structural defense that prevents the compound surface from exceeding any individual design boundary.

This rule expresses a positive invariant: permissions narrow at each step. The negative-space version (enumerating all ways permissions can compound) is unbounded. One rule; structural enforcement; bounded maintenance.

## Failure Modes

- **Legitimate escalation need.** Some workflows require a subagent to access systems the delegating agent cannot — e.g., a coordinator delegates to a specialist with domain credentials. Mitigation: route those cases through a human gate rather than encoding escalation as an agent-to-agent permission transfer.
- **Design-time blindness.** Permission compounds are only visible at runtime. No static analysis can predict all delegation chains in a dynamic system. Mitigation: require explicit permission declarations at every spawn point; make the runtime check the enforcement mechanism.
- **Audit overhead at scale.** Tracking compound permissions across many delegation steps may produce more data than reviewers can process. Mitigation: aggregate by violation (flag any delegation that grants a superset) rather than logging every delegation event at full fidelity.
- **Monotonic narrowing too restrictive.** Narrow permissions prevent legitimate multi-system workflows. Mitigation: accept that multi-system access requiring broader permissions goes through a human-initiated grant, not an agent-to-agent transfer.

## Contract

### Preconditions
An agent is about to delegate a subtask to another agent. The delegating agent holds a defined permission scope. The target system or subagent accepts credentials or a permission token from the delegator.

### Invariants
The subagent's granted permissions are a strict subset of the delegating agent's permissions at the moment of delegation. No delegation step adds permissions — it can only reduce or preserve them. The compound permission surface across all active subagents is enumerable and auditable at any point during execution.

### Governance
Owner: the orchestration layer or skill that defines how parent agents spawn subagents. Permission subsets must be declared explicitly in the delegation contract — no implicit credential inheritance. Audit tooling validates that no delegation event grants a superset of the delegator's permissions. Applies at agent-spawn time and at any mid-task re-delegation.

### Recovery
If a subagent requires permissions the delegating agent does not hold → escalate the request to a human gate rather than elevating the delegating agent's scope. If an implicit credential inheritance is discovered at runtime → halt the delegation chain; the compound permission surface is undefined. If audit reveals a subagent held permissions beyond its delegator's scope → treat as a governance violation; revoke, log, and classify the root cause.
