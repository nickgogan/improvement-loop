---
name: "Event Schema as Noun-Verb Contract"
summary: "The second governance layer maps domain nouns to allowed verbs via a formal event schema set — defining mandatory fields, semantic bindings, and state implications for every permitted action before any agent is built."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "11-step-governance-build-order-multi-agent-systems.md"
related_findings:
  - file: governed-dependency-chain-build-order.md
    rel: part-of
  - file: governance-ontology-semantic-foundation.md
    rel: depends-on
  - file: policy-as-data-machine-readable-constraints.md
    rel: enables
  - file: non-deterministic-tool-contract-model.md
    rel: same-problem
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "raw"
---

## What It Is

Step 2 of the 11-step governed multi-agent build order. Once the ontology establishes what nouns exist, the event schema set defines what can happen — mapping each noun to its allowed verbs.

**Two artifacts:**

1. **Event reference data** — a registry of all permitted events in the system, each scoped to specific noun types. This is the authoritative list of what actions are possible.

2. **Event schema set** — for each event, a precise definition including:
   - Mandatory fields (what data must be present)
   - Semantic bindings (how fields relate to ontology nouns)
   - State implications (what state changes the event triggers)

The event schema acts as a noun-verb contract: agents may only trigger events that are defined here, with the fields specified, against the noun types permitted. There is no improvised action space.

**Dependency:** Event schemas depend on the ontology (Step 1). Nouns must be defined before verbs can be mapped to them. This is the second rung of the dependency chain — meaning dictates events, events dictate what policies govern.

## Why It Matters

Without defined events, agents invent their own action vocabularies. Two agents using different event semantics for the same operation cannot be audited together, cannot have their state reconciled, and cannot be governed by shared policies. The event schema is what makes a multi-agent system's action space finite and verifiable.

The state implication field is particularly important: by declaring what state changes each event triggers, the schema makes state machine design (Step 6) tractable. Without explicit state implications, state machines must be inferred from agent behavior — a reversal of the build order that leads to ungovernable systems.

## Why People Are Using It

Practitioner-documented in the 11-step governance build order video. The pattern mirrors formal event sourcing and CQRS approaches from distributed systems engineering, extended here to multi-agent governance. The "mandatory fields" requirement creates a self-enforcing structure — malformed events are rejected at the schema layer before reaching policy or actor validation.

## Potential Improvements

- Event versioning: as the system evolves, events may need new fields or changed semantics. A versioning scheme prevents breaking changes from corrupting historical audit trails
- Event catalog tooling: a queryable registry of all defined events enables agents to discover valid actions dynamically rather than from static documentation
- Semantic validation: automated checks that event fields actually reference valid ontology nouns, not free-form strings that bypass the semantic model

## Potential Failure Modes

- **Schema proliferation**: Every new use case spawns new event types until the schema set becomes unmanageable and overlapping
- **Mandatory fields bypass**: Agents or developers mark fields as optional that should be mandatory to avoid dealing with unknown values
- **State implication mismatch**: The declared state implications don't match actual system behavior, breaking the dependency between event schema and state machines
- **Noun-verb mismatch**: Events defined before the ontology is stable will reference nouns that later get renamed or split, requiring retroactive schema updates
