---
name: "Governance Ontology as Semantic Foundation"
summary: "An explicit domain ontology and semantic model must be the first layer in any governed multi-agent system — defining canonical nouns and disambiguation rules before any agents, prompts, or behaviors are designed."
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
  - file: event-schema-noun-verb-contract.md
    rel: enables
  - file: policy-as-data-machine-readable-constraints.md
    rel: enables
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: raw
---

## What It Is

The foundational layer of the 11-step governed multi-agent build order. Before defining agents, prompts, or runtime engines, the system requires:

1. **Ontology** — a formal definition of core domain nouns. These are the nine canonical backbone data types that provide the system's structural logic. Each noun is precisely scoped so meaning stays stable system-wide.

2. **Semantic model** — disambiguation rules that prevent any noun from being interpreted differently in different contexts. The semantic model is what keeps the ontology stable as the system scales.

The key architectural rule: the system must never mix structural meaning with behavioral history. Ontology is pure structure; logs are pure history. Conflating them causes category drift.

**Category drift** is the failure mode this prevents: when control, history, trust, and state collapse into an unmanageable blob where no element is independently verifiable. Category drift happens when teams design agent personas and prompt protocols before establishing a baseline of machine-readable meaning.

## Why It Matters

Every higher-level layer — events, policies, actors, context, state machines — inherits meaning from the ontology. If the ontology is missing or informal (prose descriptions instead of structured definitions), agents built on top are "operating on guesswork." Without stable noun definitions, different agents may use the same term to mean different things, making the system ungovernable.

The ontology-first principle also enforces atomicity: one artifact (the ontology) serves exactly one concern (structural meaning). This is the foundation of the atomic rule that governs the entire 11-step build order.

## Why People Are Using It

Practitioner-documented in a production architecture video (rQMnzWE36mY) demonstrating the failure mode of ontology-last design: "category drift, meaning control, history, trust, and state are mixed into an unmanageable blob." The nine canonical backbone data types are presented as battle-tested artifacts from real multi-agent system failures.

## Potential Improvements

- Machine-readable ontology formats (OWL, RDF, JSON Schema) could make the ontology automatically verifiable rather than documentation-only
- Versioned ontology releases would allow tracking when semantic meaning changes and which agents need to be updated
- Cross-system ontology alignment — when multiple teams build on the same ontology, a shared registry prevents semantic drift between teams

## Potential Failure Modes

- **Ontology creep**: Adding nouns reactively as new use cases emerge, eventually creating semantic overlap between terms
- **Premature closure**: Locking in an ontology too early before the domain is well understood, forcing expensive retrofits
- **Unused formalism**: A well-defined ontology that agents don't actually consult — the semantic model exists in docs but not in agent prompts or validators
- **Nine canonical types assumption**: Treating the nine-type model as universal when actual domain may require more or fewer canonical types
