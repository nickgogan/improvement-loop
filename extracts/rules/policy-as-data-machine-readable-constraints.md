---
title: "Governance Rules Are Machine-Readable Data, Not Prose"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "policy-as-data-machine-readable-constraints"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "governance layers in multi-agent systems that enforce boundary, authority, and data-handling rules"
    - "any system where governance rules are currently expressed only as prose instructions to agents"
  platform_coupling: "agnostic"
  autonomy: "autonomous-only"
  stage: "build"
  reversibility: "high — migrating from prose governance to machine-readable policy requires encoding existing rules, building an evaluation engine, and integrating it into the event pipeline; rollback restores prose-only governance"
  auditability: "high when each event carries a policy evaluation record (which rules were checked, outcome, policy version); low when policy enforcement is implicit in agent behavior rather than logged at the runtime layer"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The system has a defined ontology (what entities exist) and an event schema (what operations can happen). Governance rules exist, currently expressed as prose documentation or CLAUDE.md instructions."
  invariants: "Every governance rule has a machine-readable encoding that the runtime evaluates against every event. Policy evaluation is a blocking step in the event pipeline — events that fail policy validation do not proceed. Policy versions are tracked; each event's audit record references the policy version in effect at execution time."
  governance: "Owner: the system architect or governance layer responsible for the policy encoding. The meta-rule applies to itself: this rule must have a machine-readable encoding. Consumer-side audit checks that no governance rule exists only in prose form without a corresponding machine-readable encoding. Policy changes follow the same governance lifecycle as other design decisions — no ad-hoc updates."
  recovery: "If a new event type is introduced without corresponding policy coverage → treat as blocked by default (deny-by-default posture) until policy coverage is added. If policy-reality drift is detected (policy does not reflect current system behavior) → halt new deployments; audit and reconcile before proceeding. If prose governance diverges from machine-readable policy → the machine-readable policy is authoritative; update the prose to match."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "policy-enforcement"
  - "machine-readable"
---

# Governance Rules Are Machine-Readable Data, Not Prose

**Source:** [[policy-as-data-machine-readable-constraints]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A multi-agent system has governance rules — boundary rules (what the system may and may not do), authority rules (who may trigger which operations), and data-handling rules (how data may be accessed, retained, and shared). Those rules are currently expressed as prose: documentation, CLAUDE.md files, or constitution files that agents are instructed to read and follow.

Prose governance is aspirational. Agents are instructed to follow rules; the runtime does not enforce them. The gap between governance-as-instruction and governance-as-enforcement is the condition this rule addresses.

## Action

**Required:** Every governance rule must have a machine-readable encoding that the runtime evaluates against every relevant event. Three categories require encoding:

1. **Boundary rules** — what the system is and is not permitted to do (scope constraints)
2. **Authority rules** — who is permitted to trigger which events (access constraints)
3. **Data-handling rules** — how data may be accessed, retained, and shared (compliance constraints)

Machine-readable policy sits above the event schema and acts as a filter. Every event must pass policy validation before proceeding. Policy cannot reference things that do not exist in the ontology or event schema — it depends on those lower layers being defined first.

**Forbidden:** Operating any governance rule in prose-only form as the sole enforcement mechanism. Treating agent instruction-following as equivalent to runtime enforcement. Deploying a new event type without corresponding policy coverage.

## Boundary

Enforced at governance rule authorship: every rule that is written must also have a machine-readable encoding before the system that rule governs reaches production. Also enforced at event pipeline design: policy evaluation is a non-optional blocking step, not an optional middleware.

The meta-rule applies to itself: this rule (governance rules must be machine-readable) must have a machine-readable encoding in any system that adopts it.

Does not eliminate prose governance entirely — human-readable policy documentation remains valuable. The constraint is that machine-readable encoding must co-exist with prose; the machine-readable form is the enforcement source of truth.

## Enforcement

- **Mechanism:** The event pipeline includes a policy evaluation layer. Events are submitted to the policy engine; the engine evaluates them against the current policy set; events that fail are blocked. The evaluation result (allowed/denied, rule reference, policy version) is recorded per event.
- **Check (deterministic):** For every event: `policy_evaluation_result == 'allowed'` before the event proceeds. For every governance rule: `machine_readable_encoding_exists == true` before the rule enters the governance corpus.
- **Violation response:**
  - *Event fails policy evaluation:* block the event; log the violation with rule reference and policy version.
  - *Governance rule has no machine-readable encoding:* treat it as unenforced; flag for encoding before the system it governs is promoted.
  - *New event type without policy coverage:* deny by default; require explicit policy addition before the event type is permitted.
  - *Policy-reality drift detected:* halt new deployments; audit and reconcile before proceeding.
- **Cannot be self-certified by agents:** Policy evaluation is a runtime layer the agent cannot bypass — the enforcement is structural, not behavioral. An agent that disagrees with a policy outcome must escalate to a human; it cannot self-authorize.

## Rationale

Prose policies are governance-as-documentation. Machine-readable policies are governance-as-enforcement. The distinction is the difference between "agents are instructed to follow rules" and "events are blocked if they violate rules."

The 11-step governed multi-agent build order places policy as Step 3 — after the ontology (what exists) and event schema (what can happen), but before actors are defined. This ordering is not arbitrary: policy cannot reference things that do not exist in the lower layers, and actors cannot be safely scoped until the policy layer constrains them.

Structural enforcement is consistently more reliable than psychological enforcement (agents following instructions) or economic enforcement (consequences for violations). Policy as data is structural enforcement applied to the governance layer itself — the same principle that makes type systems more reliable than documentation, and the same principle that makes access control lists more reliable than trust.

The analogy to existing practice: OPA, Cedar, and Casbin all implement this pattern for infrastructure authorization. The finding extends the same principle to governance rules in agent systems.

## Failure Modes

- **Policy explosion.** Encoding every edge case produces policy sets too complex to reason about. Mitigation: encode invariants (positive-space rules), not exceptions; tolerate one-off cases without encoding them until recurrence justifies the cost.
- **False completeness.** Machine-readable policies may appear comprehensive while missing coverage for novel event types. Mitigation: deny-by-default posture — events without policy coverage are blocked, not permitted.
- **Evaluation latency.** Runtime policy evaluation adds overhead to every event; poorly optimized policy engines become bottlenecks. Mitigation: policy evaluation is designed for performance at the same time as correctness; late optimization is acceptable, no-evaluation is not.
- **Policy-reality drift.** Policies are defined but not updated when the system evolves, creating silent gaps. Mitigation: policy changes follow the same lifecycle as design decisions; the system architect is responsible for keeping policy and system behavior synchronized.
- **Prose residue.** Some rules are encoded in machine-readable form; others remain in documentation only. The hybrid creates a two-tier governance system harder to audit than either approach alone. Mitigation: treat any governance rule that exists only in prose as an open action item; track until encoded.

## Contract

### Preconditions
The system has a defined ontology (what entities exist) and an event schema (what operations can happen). Governance rules exist, currently expressed as prose documentation or CLAUDE.md instructions.

### Invariants
Every governance rule has a machine-readable encoding that the runtime evaluates against every event. Policy evaluation is a blocking step in the event pipeline — events that fail policy validation do not proceed. Policy versions are tracked; each event's audit record references the policy version in effect at execution time.

### Governance
Owner: the system architect or governance layer responsible for the policy encoding. The meta-rule applies to itself: this rule must have a machine-readable encoding. Consumer-side audit checks that no governance rule exists only in prose form without a corresponding machine-readable encoding. Policy changes follow the same governance lifecycle as other design decisions — no ad-hoc updates.

### Recovery
If a new event type is introduced without corresponding policy coverage → treat as blocked by default (deny-by-default posture) until policy coverage is added. If policy-reality drift is detected (policy does not reflect current system behavior) → halt new deployments; audit and reconcile before proceeding. If prose governance diverges from machine-readable policy → the machine-readable policy is authoritative; update the prose to match.
