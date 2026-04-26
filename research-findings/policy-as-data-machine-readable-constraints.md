---
name: "Policy as Data — Machine-Readable Constraints"
summary: "Governance rules are encoded as machine-readable data structures (not prose), acting as a filter over the event schema. Boundary, authority, and data-handling rules are enforced at runtime against every event, not just documented for human reference."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P1 (Strong, Directly Applicable)"
applicability:
  - "General"
adopted_in: []
sources:
  - "11-step-governance-build-order-multi-agent-systems.md"
related_findings:
  - file: governed-dependency-chain-build-order.md
    rel: part-of
  - file: event-schema-noun-verb-contract.md
    rel: depends-on
  - file: governance-ontology-semantic-foundation.md
    rel: depends-on
  - file: context-warrant-justified-data-package.md
    rel: enables
  - file: actor-passport-schema-bound-identity.md
    rel: enables
  - file: specification-as-governance-fourth-enforcement-philosophy.md
    rel: same-problem
  - file: structural-vs-psychological-vs-economic-governance.md
    rel: same-problem
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: "classified"
---

## What It Is

Step 3 of the 11-step governed multi-agent build order. After the system knows what exists (ontology) and what can happen (event schemas), it must define what must be true — the policy layer.

**Core pattern:** Instead of prose documentation, governance rules are represented as machine-readable data structures that the runtime evaluates against every event. Three categories of rules:

1. **Boundary rules** — what the system is and is not permitted to do (scope constraints)
2. **Authority rules** — who is permitted to trigger which events (access constraints)
3. **Data handling rules** — how data may be accessed, retained, and shared (compliance constraints)

**Position in the dependency chain:** Policy sits above the event schema and acts as a filter. Every event must pass policy validation before proceeding to the actor layer. Policy cannot reference things that don't exist in the ontology or event schema — it depends on both lower layers.

**Machine-readability requirement:** Prose policies ("agents should not access PII without authorization") are aspirational. Machine-readable policies are enforced — the runtime checks them and blocks non-compliant events. This is the distinction between governance-as-documentation and governance-as-enforcement.

## Why It Matters

MetaSystem currently expresses governance rules primarily as prose in CLAUDE.md files and constitution.md. These are read by agents but not enforced by the runtime. Policy as data transforms governance from a soft constraint (agents are instructed to follow rules) into a hard constraint (events are blocked if they violate rules).

This finding sits at P1 because it directly addresses a gap in MetaSystem's governance model: the gap between policy-as-instruction and policy-as-enforcement. The 11-step build order frames this as the difference between a "manual or set of guidelines" and a "physically engineered dependency chain."

## Why People Are Using It

Practitioner-documented in the 11-step governance build order. The pattern has analogues in open policy agent (OPA) frameworks, authorization-as-code approaches (Cedar policy language, Casbin), and formal methods research. The video frames it as the only path from aspirational to provable governance.

The structural enforcement philosophy (per `structural-vs-psychological-vs-economic-governance`) validates this — structural enforcement is consistently the most reliable approach. Policy as data is structural enforcement applied to the governance layer itself.

## Potential Improvements

- Policy versioning: policies change; audit trails must capture which policy version was in effect when an event was executed
- Policy testing: machine-readable policies can have unit tests — test cases that verify specific events are allowed or denied as expected
- Policy composition: layered policies (global → system → agent-level) with clear precedence rules
- Human-readable policy views: machine-readable policies with tooling to render them as readable documentation, so humans and machines can both consume the same source of truth

## Potential Failure Modes

- **Policy explosion**: Attempting to encode every edge case creates policy sets too complex to reason about
- **False completeness**: Machine-readable policies may appear comprehensive while missing coverage for novel event types
- **Evaluation latency**: Runtime policy evaluation adds overhead to every event; poorly optimized policy engines can become bottlenecks
- **Policy-reality drift**: Policies may be defined but not updated when the system evolves, creating silent gaps
- **Prose residue**: Teams encode some rules as machine-readable data and leave others in documentation, creating two-tier governance that's harder to audit than either approach alone
