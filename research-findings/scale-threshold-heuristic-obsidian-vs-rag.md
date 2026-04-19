---
name: 'Scale Threshold Heuristic: Obsidian Wiki vs True RAG'
summary: 'A practical decision framework: use Obsidian + Claude Code file traversal for solo devs and small teams under ~1000 documents; migrate to true RAG (vector DB, embeddings) only when scale clearly
  exceeds what markdown navigation can handle. Start simple, upgrade when needed.'
implementation_notes: MetaSystem operates well under this threshold. The heuristic validates the current approach of using Obsidian + file-based navigation rather than investing in RAG infrastructure.
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- karpathys-obsidian-rag-claude-code.md
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: raw
consumed_by: []
---

## What It Is

A decision heuristic from Chase AI (interpreting Karpathy's Obsidian KB approach) for choosing between lightweight Obsidian-based knowledge management and full RAG infrastructure:

**Use Obsidian + Claude Code file traversal when:**
- Solo operator or small team
- Document count under ~1000
- Content is primarily text/markdown
- You want human-readable, editable knowledge
- You are already using Obsidian
- Cost sensitivity (Obsidian is free; RAG requires infrastructure)

**Migrate to true RAG when:**
- Scaling to thousands or millions of documents
- Need sub-second retrieval across massive corpora
- Multiple concurrent users querying the same knowledge base
- Documents are heterogeneous (PDFs, images, structured data)

Chase AI's core advice: "Just try it. Just experiment. It's not costing you anything to use Obsidian. And if it doesn't work, fine, then go use LightRAG instead. People want to sit here and argue this back and forth. Just try it."

The heuristic is explicitly pragmatic -- start with the simpler system and migrate only when you hit clear scaling limits, rather than over-engineering from the start.

## Why It Matters

RAG infrastructure (vector DBs, embedding pipelines, retrieval tuning) is significant overhead for small teams. The Obsidian approach provides 80% of RAG's value at 10% of the complexity for the common case of solo devs and small teams.

## Why People Are Using It

Karpathy himself uses the lightweight approach despite having the expertise for full RAG. Chase AI frames it as "the perfect middle ground for a solo operator or a small team." The approach has gained traction because it leverages existing Obsidian investments.

## Potential Improvements

Hybrid approach: Obsidian for curated knowledge, RAG for bulk ingestion. Monitoring tools to detect when the Obsidian approach is hitting scaling limits (slow queries, missed results).

## Potential Failure Modes

The threshold is fuzzy -- some teams may stay too long on Obsidian and accumulate poorly organized content. Migration from Obsidian to RAG is non-trivial if the wiki structure is deeply coupled to the workflow.
