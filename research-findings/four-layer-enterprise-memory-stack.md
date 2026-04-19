---
notion_id: 3351e08b-9b34-8174-98c3-d9da290d9a8b
name: Four-Layer Enterprise Memory Stack (Working / Episodic / Semantic / Governance)
summary: 'Production memory architecture with four explicit tiers: (1) Working memory -- ephemeral, context window only; (2) Episodic memory -- specific tasks and cases with temporal context; (3) Semantic
  memory -- knowledge graph of entities, relationships, constraints; (4) Governance memory -- versioned audit log of every prompt, retrieval, action, and output. Layer 4 is framed as non-optional for production
  in 2026.'
implementation_notes: 'Extends the KB''s existing context taxonomy into a full enterprise memory stack. Governance/observability layer (Layer 4) is the new piece. EU AI Act compliance is pushing this into
  design requirements. Source: https://alok-mishra.com/2026/01/07/a-2026-memory-stack-for-enterprise-agents/'
category: Memory Architecture
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- 4-layer-memory-stack-for-2026-enterprise-agents-al.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-08'
related_findings:
- file: memory-cross-layer-promotion-governance.md
  rel: enables
- file: governance-memory-append-only-audit-layer.md
  rel: extends
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
---
# Four-Layer Enterprise Memory Stack (Working / Episodic / Semantic / Governance)

## What It Is
A distributed-systems-style taxonomy for agent memory with four explicit layers each having defined read/write policies, retention targets, and ownership:
1. **Working Memory** -- context window only; last 6-10 exchanges + active plan; ephemeral
2. **Episodic Memory** -- specific tasks, cases, journeys with temporal context; durable across sessions
3. **Semantic Memory** -- entities, relationships, constraints as a knowledge graph; slowly evolving
4. **Governance Memory** -- versioned audit log of every prompt, retrieval, action, and output; non-optional

## Why It Matters
Most production agent failures aren't model failures -- they're memory failures.

## Why People Are Using It
Redis (Agent Memory Server), LangGraph, and others converge on similar layered architectures. Enterprise AI Act compliance is driving adoption.

## Potential Improvements

- Define explicit read/write policies per layer with ownership and approval levels
- Implement the interaction sequence: read semantic -> retrieve episodic -> compose working (budgeted) -> execute -> write-back (policy-gated) -> governance log
- Precompute embeddings at ingestion, cache per episode, limit retrieval hops deterministically
- Keep semantic memory small and structured by design

## Potential Failure Modes
Semantic memory write policies are the hardest to get right. Governance memory can become a storage cost problem. Integration complexity across four layers requires significant infrastructure investment.

---

## April 2026 Deep Extraction Update

**Implementation details from source (Alok Mishra):**

**Layer properties matrix:**
| Layer | Primary Goal | Capacity | Latency | Security |
|-------|-------------|----------|---------|----------|
| Working | Minimize sensitive carry-over | Minutes/hours | Chat-speed | Strict token budget + compaction |
| Episodic | Continuity + audit | Months (with pruning) | Seconds (indexed) | Role-based access + evidence pointers |
| Semantic | Shared truth + consistency | Small by design, distilled | Fast reads | Governance + schema ownership |
| Governance | Accountability | Append-only retention | Not in hot path | Immutable logs + versioning |

**Safety and privacy requirements:**
- Data minimisation: store what you need for future reasoning, not everything you can access
- Access control: not every agent sees every layer or every field
- Redaction and residency: episodes often contain sensitive content
- Separation of duties: approvals and writes should be policy-gated

**Architecture board review questions:**
1. Who owns promotion policy changes?
2. Who can override memory pruning?
3. What constitutes a rollback trigger?
4. How quickly can the team reconstruct a corrupted memory state?

**Academic convergence (March 2026):** arXiv 2603.17787 "Governed Memory" validates with production evidence: 99.6% fact recall, 92% governance routing precision, 50% token reduction from progressive delivery, zero cross-entity leakage. arXiv 2603.29194 confirms working/episodic/semantic hierarchy reduces cross-session drift.

**Related new findings:** memory-cross-layer-promotion-governance.md (promotion patterns), governance-memory-append-only-audit-layer.md (Layer 4 implementation details)

**Updated evidence strength:** Strong (was Medium -- now with academic validation + multiple practitioner implementations)
