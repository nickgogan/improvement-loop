---
title: "Event Schema as Noun-Verb Contract"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "event-schema-noun-verb-contract"
extraction_date: "2026-05-25"
last_change_session: 94
last_change_sl: "session-94-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Teams designing or building multi-agent systems where more than one agent can modify shared state and auditability or governance of those mutations is required"
    - "Systems where agent action spaces must be finite and verifiable — it must be possible to enumerate all possible agent actions without reading agent code"
    - "Architects defining a governed build order for a multi-agent system who need the event definition step to be concrete and enforceable"
    - "Any project that has experienced or anticipates divergent event semantics between agents — two agents naming the same operation differently — causing reconciliation failures or audit gaps"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "medium — the event schema is a design artifact; once agents are built against it, changing the schema requires coordinated updates across all consumers"
  auditability: "High — every event rejection is logged with event name, noun type, missing fields, and agent identity; the registry itself is a readable artifact auditable against agent code"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An ontology (noun definitions) exists or is being defined concurrently. A validation mechanism exists to check events against the registry before execution. All agents acting on shared state are subject to the same event schema."
  invariants: "The event registry is the single authoritative source for permitted events. Every event instance carries all mandatory fields. State implications are applied consistently. Individual agents do not modify the registry unilaterally."
  governance: "Owner: team or architect responsible for the multi-agent system design. Schema changes require coordination across all agents consuming affected noun types. Ontology owner and event schema owner must coordinate on noun changes."
  recovery: "Out-of-registry event: reject without state mutation, log, surface to agent owner. Missing mandatory fields: reject, log, return field list. Ontology change invalidates mappings: audit registry, update or deprecate affected events before resuming."
tags:
  - "extracted-artifact"
  - "rule"
---

# Event Schema as Noun-Verb Contract

**Source:** [[event-schema-noun-verb-contract]]
**Form:** rule
**Extraction date:** 2026-05-25

A design rule requiring that multi-agent systems define an explicit event schema — a registry mapping each noun type to its allowed verbs, with mandatory fields, semantic bindings, and state implications for each event. Agents may only trigger events defined in this schema, against permitted noun types, with the required fields present.

## Condition

A system is being designed or extended where multiple agents (or agent roles) can take actions that affect shared state. Those actions must be auditable, reconcilable across agents, and governable by shared policies. An ontology (noun definitions) already exists or is being defined concurrently.

## Action

**Required:** Define an event reference registry listing every permitted event in the system, scoped to specific noun types. For each event, define a precise schema containing:
- Mandatory fields that must be present on every instance
- Semantic bindings: how fields relate to ontology nouns
- State implications: what state changes the event triggers

**Required:** Treat the event schema as a noun-verb contract. An agent's action space is finite and bounded by this contract.

**Forbidden:** Triggering events not in the registry. Executing events with missing mandatory fields. Agents modifying the event registry unilaterally without an explicit update process. Triggering events against noun types not listed in the schema.

## Boundary

Enforced at **system design time** (after the ontology is established) and at **runtime** before any agent action is processed. Event validation must occur before state is mutated.

## Enforcement

- **Registry check:** Before executing any agent action, verify the event name exists in the event registry and is permitted for the target noun type.
- **Field validation:** Confirm all mandatory fields are present and non-null before the event is executed.
- **State implication check:** Before applying state changes, confirm the declared state implications are consistent with the noun's current state.
- **Violation response:** Any event that fails registry check, field validation, or state implication check is rejected without state mutation. The rejection is logged with: event name, noun type, missing or invalid fields, and the identity of the agent that attempted the trigger.

## Rationale

Without defined events, agents in a multi-agent system invent their own action vocabularies. Two agents using different event semantics for the same operation cannot be audited together, cannot have their state reconciled, and cannot be governed by shared policies. The event schema makes the system's action space finite and verifiable. The state implication field is particularly important: by declaring what state changes each event triggers, the schema makes state machine design tractable and prevents implicit, untracked mutations.

## Contract

### Preconditions
An ontology (noun definitions) has been established. Event schemas depend on noun types — verbs cannot be mapped until nouns are defined. A mechanism exists to validate events against the registry before execution. All agents operating on shared state are subject to the same event schema.

### Invariants
The event registry is the single authoritative source for permitted events. No out-of-registry events are executed. Every event instance carries all mandatory fields before execution. State implications declared in the schema are applied consistently across all agents and sessions. Schema changes require an explicit update process; individual agents do not modify the registry unilaterally.

### Governance
Owner: the team or architect responsible for the multi-agent system's design. Schema changes require coordination across all agents that consume the affected noun types. The ontology owner and the event schema owner must coordinate on noun changes that invalidate existing verb mappings.

### Recovery
Out-of-registry event submitted: reject without state mutation, log the violation, surface to the agent's owner for schema update. Mandatory fields missing: reject, log, return the field list to the submitting agent. Ontology changes invalidate noun-verb mappings: audit the event registry for affected events, update or deprecate as needed before resuming agent operations.
