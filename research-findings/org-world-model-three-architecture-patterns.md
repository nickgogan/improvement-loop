---
name: "Org World-Model Three Architecture Patterns"
summary: "Three distinct architectures are used to build organizational world models — vector DB (semantic retrieval), structured ontology (schema-bounded reasoning), and signal fidelity (high-quality data exhaust) — each with a characteristic failure mode rooted in how it mishandles the information/judgment boundary."
implementation_notes: null
category: "Memory Architecture"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "world-models-orgs-three-architectures.md"
related_findings:
  - file: interpretive-boundary-layer-fact-vs-judgment.md
    rel: enables
  - file: governance-ontology-semantic-foundation.md
    rel: same-problem
  - file: four-layer-enterprise-memory-stack.md
    rel: same-problem
  - file: hybrid-retrieval-pattern-semantic-lexical-graph.md
    rel: related
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---

## What It Is

Three architectural approaches companies use to build organizational world models — software that maintains a living, continuously updated picture of business state (what's being built, what's blocked, where customers are struggling) so that information flows without human information-routing overhead.

**Architecture 1: Vector Database (semantic retrieval)**
Wire up data sources, embed everything, let agents retrieve by semantic similarity. Fast to deploy; adequate for pure information logistics — status synthesis, dependency detection, report generation.
- *Failure mode:* Never draws the information/judgment boundary. Semantic ranking is itself an interpretation (a claim about what matters), but nothing in the architecture signals that. At small scale, senior humans override bad rankings. At scale, the ranking becomes organizational reality — what the system surfaces gets acted on; what it doesn't, gets ignored. The editorial function is automated by default with no one deciding to automate it.
- *Breaks at:* ~10,000 documents or when the user base can no longer apply independent judgment to system output.

**Architecture 2: Structured Ontology (schema-bounded reasoning)**
Explicitly define domain objects, relationships, and actions (the Palantir model). AI reasons within the bounded structure. Cannot hallucinate relationships that don't exist in the schema.
- *Failure mode:* Draws the boundary too conservatively. Ontology can only represent what has already been categorized — it handles known relationships precisely but is blind to emergent ones. The unnamed pattern that reframes how you understand the business is invisible to the system. Precise within its schema; silent about what it doesn't know; and what it doesn't know may be what matters most.
- *Breaks at:* Novel business conditions that fall outside the schema.

**Architecture 3: Signal Fidelity (high-quality data exhaust)**
Build the world model around the highest-fidelity data the business generates — transactions in Block's case. "Money is honest": every purchase is a fact; model improves as a byproduct of doing business.
- *Failure mode:* Assumes the signal interprets itself. Connections between facts (why a merchant's cash flow is tightening) still require judgment. Because the underlying signal is clean, interpretive moves look more trustworthy than they are — a correlation in transaction data feels more authoritative than a correlation in Slack messages, even when causal reasoning behind both is equally thin. High signal fidelity at the input layer creates an illusion of high judgment quality at the output layer.
- *Breaks at:* Any causal inference that requires context the signal doesn't carry.

**Sizing guidance:**
| Company type | Recommended start |
|---|---|
| <100 people, strong senior team | Vector DB — senior people supply the judgment |
| Enterprise / regulated | Structured ontology — high upfront cost, captures surprises |
| Platform business with clean signal (transactions) | Signal fidelity — but invest heavily in interpretive boundary labeling |
| Knowledge-work company (docs + conversations) | Vector DB first, but build an interpretive layer on top; plan migration to structured approach before 10K documents |

## Why It Matters

"World model" is one phrase covering three completely different architectures that fail in different ways. Teams that treat them as interchangeable will copy the architecture without understanding which failure mode they're importing. Architectural choice determines which risks are systemic and invisible vs. loud and diagnosable.

## Why People Are Using It

The vector DB approach dominates because it deploys fast and works for information logistics. The structured ontology approach is used in regulated industries and by vendors like Palantir. The signal fidelity approach reflects Jack Dorsey's published blueprint for Block, which received significant practitioner attention in 2025.

## Potential Improvements

Hybrid architectures that layer structured ontology on top of semantic retrieval — providing both discovery (vector) and precision (schema). The interpretive boundary layer is a meta-layer that can be added to any of the three architectures.

## Potential Failure Modes

- Choosing architecture by deployment speed rather than org size and risk profile
- Outgrowing the vector DB approach and not having a migration plan to structured data
- Treating signal fidelity as a substitute for judgment rather than high-quality input to judgment
- None of these architectures solves the outcome-encoding problem (see `compounding-knowledge-loop-internal-data.md`)
