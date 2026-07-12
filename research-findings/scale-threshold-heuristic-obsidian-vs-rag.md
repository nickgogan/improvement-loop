---
name: 'Scale Threshold Heuristic: Obsidian Wiki vs True RAG'
summary: 'A practical decision framework: use Obsidian + Claude Code file traversal for solo devs and small teams under ~1000 documents; migrate to true RAG (vector DB, embeddings) only when scale clearly
  exceeds what markdown navigation can handle. Start simple, upgrade when needed.'
implementation_notes: 'MetaSystem operates well under this threshold. The heuristic validates the current

  approach of using Obsidian + file-based navigation rather than investing in RAG

  infrastructure. Corroboration status (2026-07-12): now backed by multiple independent

  channels — Chase AI (original + agentic-OS re-statement), Cole Medin/LlamaIndex

  (file search beats RAG below corpus threshold), Nate Herk (pain-driven level

  selection on a production business brain), plus Karpathy''s own practice. Flagged as

  a /reassess-priorities candidate on evidence-accumulation grounds (priority

  unchanged here — reassessment is the Curator''s call).'
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- karpathys-obsidian-rag-claude-code.md
- sdk-vs-framework-decision-ai-agents.md
- every-level-of-a-claude-second-brain-explained.md
- the-agentic-os-setup-that-will-10x-claude-code.md
date_discovered: '2026-04-07'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- building-agentic-systems.md
related_findings:
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: extended-by
- file: context-infrastructure-seven-level-maturity-model.md
  rel: enables
- file: file-search-outperforms-rag-for-small-corpora.md
  rel: same-problem
- file: per-folder-heterogeneous-retrieval-levels.md
  rel: extended-by
- file: curated-spine-plus-rag-hybrid-query-router.md
  rel: extended-by
- file: query-shape-first-storage-design.md
  rel: extended-by
- file: structure-addressed-retrieval-for-cited-document-domains.md
  rel: same-problem
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

**2026 corroboration (LlamaIndex study + coding agent ecosystem):** Cole Medin reports that a LlamaIndex study confirmed file search outperforms RAG for smaller corpora. This is further validated by the coding agent ecosystem shift: Claude Code and other coding agents stopped using vector databases entirely, relying on grep and file search built into their SDKs. The evidence strengthens the heuristic -- the threshold isn't just about Obsidian specifically, but about file-based search as a category outperforming semantic search below a corpus-size boundary.

**2026-07 corroboration (independent channels):** Nate Herk ("Every Level of a Claude Second Brain Explained") runs a production business brain deliberately held at the wiki level, with the same pain-driven trigger: "find the simplest level that actually fits your needs... if there's not pain, then why create more?" — and refines the heuristic from a system-wide threshold to a per-folder decision (see per-folder-heterogeneous-retrieval-levels). Chase AI's agentic-OS breakdown re-states it from the state-management side: "if you just set up Claude Code with a file structure that is coherent and makes sense, you're like 99% of the way there" — Obsidian and databases are conveniences on top, not the mechanism. The heuristic is now corroborated across multiple independent practitioner channels, all converging on the same order: structure first, retrieval infrastructure only on demonstrated pain.

## Potential Improvements

Hybrid approach: Obsidian for curated knowledge, RAG for bulk ingestion. Monitoring tools to detect when the Obsidian approach is hitting scaling limits (slow queries, missed results).

## Potential Failure Modes

The threshold is fuzzy -- some teams may stay too long on Obsidian and accumulate poorly organized content. Migration from Obsidian to RAG is non-trivial if the wiki structure is deeply coupled to the workflow.
