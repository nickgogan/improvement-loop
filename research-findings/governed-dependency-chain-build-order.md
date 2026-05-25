---
name: "Governed Dependency Chain — 11-Step Multi-Agent Build Order"
summary: "Governed multi-agent systems require a strict sequential build order where each layer depends on the one before it: ontology → events → policy → actors → context → state machines → IO contracts → provenance → runtime controls → capability contracts. Bypassing the chain breaks system integrity."
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
  - file: governance-ontology-semantic-foundation.md
    rel: part-contains
  - file: event-schema-noun-verb-contract.md
    rel: part-contains
  - file: policy-as-data-machine-readable-constraints.md
    rel: part-contains
  - file: actor-passport-schema-bound-identity.md
    rel: part-contains
  - file: context-warrant-justified-data-package.md
    rel: part-contains
  - file: tool-model-io-contracts-with-preconditions.md
    rel: part-contains
  - file: runtime-threshold-management-truth-conditions.md
    rel: part-contains
  - file: structural-vs-psychological-vs-economic-governance.md
    rel: same-problem
  - file: specification-as-governance-fourth-enforcement-philosophy.md
    rel: same-problem
  - file: bmad-dependency-graph-module-ordering.md
    rel: same-problem
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: synthesized
consumed_by:
  - "agent-governance-and-trust.md"
---

## What It Is

The overarching architecture pattern from the 11-step governance build order: a sequentially dependent construction order for governed multi-agent systems. Each layer must be complete before the next is started, because each layer depends on the artifacts of the layer below it.

**The 11 layers:**

| Step | Layer | What It Defines |
|------|-------|----------------|
| 1 | Ontology + Semantic Model | Core domain nouns; disambiguation rules |
| 2 | Event Schema | Noun-verb mappings; mandatory fields; state implications |
| 3 | Policy as Data | Boundary, authority, data-handling rules (machine-readable) |
| 4 | Actor Model + Passport Schema | Actor classes; role bindings; authority ceilings; trust markers |
| 5 | Context Warrant | Justified minimum-necessary data assembly; freshness enforcement |
| 6 | Protocol + State Machines | Allowed action sequences; transition rules; timeouts |
| 7 | Tool and Model IO Contracts | External effect boundaries; preconditions; rate limits; idempotency |
| 8 | Provenance + Audit/Replay | Action lineage; policy traces; decision logic; replay capability |
| 9 | Threshold Management | Live signal monitoring; escalation and containment triggers |
| 10 | Truth Conditions Framework | Three-level verification: semantic, procedural, historical |
| 11 | Capability Contracts | Runtime engines with no independent logic; derive authority from chain |

**The dependency chain narrative:** Meaning dictates events. Events are filtered by policy. Policy governs actors. Actors wield context. Context navigates state. State triggers effects. Effects generate proof. Proof is verified by runtime controls. Runtime is operationalized by capability contracts.

**The atomic rule:** One artifact serves exactly one concern. One model handles one kind of truth. Mixing semantic definitions with runtime thresholds — or any other cross-layer contamination — breaks system integrity.

**Capability contracts (Step 11):** The terminal layer consists of runtime engines that have no independent logic. They derive their intelligence and authority strictly from the governed dependency chain beneath them. This is intentional: intelligence without governance is uncontrollable; governance without intelligence is useless. The capability contract is the interface between the two.

## Why It Matters

Most multi-agent systems are built in reverse order: teams design agent personas, prompt protocols, and runtime engines first, then attempt to add governance after the fact. Post-hoc governance fails because governance requirements should constrain architectural decisions, not be retrofitted around them.

The 11-step build order is the correct construction sequence: governance artifacts are built in dependency order before any agents are instantiated. Agents are not designed until Steps 4-5; execution engines are not defined until Step 11. By that point, every constraint the engine must respect is already specified in layers 1-10.

The result is a system that is "scalable, composable, and undeniably provable." Provable is the key word: the system can demonstrate compliance with every constraint, trace any action back to its authority basis, and replay any past decision for audit.

## Why People Are Using It

Practitioner-documented as a response to observed multi-agent system failures. The video opens by illustrating the failure mode: "category drift, meaning control, history, trust, and state are mixed into an unmanageable blob where no element is independently verifiable." The 11-step order is presented as the engineered solution to that failure.

The pattern has conceptual foundations in formal methods engineering (where specifications precede implementations) and enterprise IAM architecture (where identity and policy layers precede application layers).

## Potential Improvements

- Tooling to verify build order compliance: automated checks that detect when a higher-layer artifact references an undefined lower-layer artifact
- Partial order implementation: some systems may not need all 11 layers; a principled way to determine the minimum required layers for a given risk profile
- Iterative build order: for evolving systems, how to add new layers or modify existing ones without breaking dependent layers

## Potential Failure Modes

- **Layer 11 hubris**: Teams that build capability contracts first (typical path) and then attempt to retrofit layers 1-10 beneath them — this inverts the dependency chain and produces unmaintainable governance theater
- **Over-engineering for simple systems**: A 3-agent workflow doesn't need all 11 layers; applying the full build order to low-complexity systems introduces unnecessary overhead
- **Dependency chain staleness**: As the system evolves, lower layers may be updated without cascading updates to higher layers that depend on them
- **Atomicity violations in practice**: Teams under time pressure combine concerns from multiple layers into single artifacts, breaking the one-artifact-one-concern rule
- **Build order vs. operate order**: The construction sequence (ontology first) differs from the operational order (capability contracts execute first). Confusing the two leads to operational systems that don't reflect their governance structure
