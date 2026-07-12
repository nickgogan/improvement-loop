---
name: 'Write-Time vs Query-Time Synthesis: KB Poisoning Tradeoff'
summary: 'LLM-authored content re-indexed into a knowledge base creates a poisoning risk: summaries lose specifics, subsequent queries reason from LLM outputs instead of originals, and circular reinforcement
  disconnects the KB from ground truth. Write-time synthesis (Karpathy pattern) trades long-term trustworthiness for speed. Query-time synthesis (extract structure at ingestion, synthesize from originals
  at query) preserves chain of custody but costs more per query.'
implementation_notes: 'MetaSystem''s IL pipeline partially mitigates this: findings carry evidence_strength, sources link back to originals, and the Researcher mandate requires one canonical entry per pattern
  with evidence pointers. The risk exists wherever LLM-authored artifacts get indexed alongside source material — especially in the compile step of the Karpathy pattern. The article''s three principles
  (immutable originals, structure over prose, query-time synthesis) are worth evaluating against IL''s current write-time approach.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- hidden-flaw-karpathy-llm-wiki.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-07-12'
related_findings:
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: contradicts
- file: ai-managed-vault-separate-from-human-vault.md
  rel: extends
- file: scale-threshold-heuristic-obsidian-vs-rag.md
  rel: extends
- file: agentic-search-memory-retrieval-architecture.md
  rel: contradicts
- file: automatic-fact-extraction.md
  rel: contradicts
- file: evergreen-vs-volatile-ingestion-rule.md
  rel: same-problem
- file: okf-open-knowledge-format-curated-bundle-spec.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
- rules/never-ask-claude-to-compact-claudemd.md
tags:
- context-engineering
- memory
- knowledge-management
---

# Write-Time vs Query-Time Synthesis: KB Poisoning Tradeoff

## What It Is

A critique of the Karpathy LLM-compiled wiki pattern identifying a critical failure mode at organizational scale: knowledge base poisoning through write-time synthesis. When an LLM authors persistent content (summaries, concept articles, cross-references) that gets re-indexed alongside source documents, unverifiable information enters the knowledge base. Subsequent LLM responses reason from prior LLM outputs rather than originals, creating circular reinforcement disconnected from ground truth.

## Why It Matters

The distinction between write-time and query-time synthesis determines whether a knowledge system maintains chain of custody to source material:

- **Write-time synthesis** (Karpathy pattern): LLM reads raw documents and produces persistent artifacts integrated into the retrieval corpus. Fast queries, amortized cost, but compounds errors systematically. A vendor contract specifying "net 30, 2% discount within 10 days" becomes "standard net-30 terms with early-payment discounts" — losing specifics that can't be recovered from the summary.

- **Query-time synthesis**: LLM extracts structured metadata at ingestion (entities, relationships, topic tags, source-linked evidence) without authoring narrative content. Answers synthesize fresh from originals each time. Preserves chain of custody indefinitely but costs more per query.

## Key Principles for Organizational Systems

1. **Immutable originals:** Source documents remain authoritative and unmodified. LLMs never produce "cleaned up" versions for retrieval.
2. **Structure over prose:** LLMs extract verifiable structure (relationships, claims with citations, classifications tagged to source spans) rather than narrative content.
3. **Query-time synthesis:** Extracted structure serves as navigation aids guiding retrievers to relevant documents. Answers derive from originals, not from prior LLM responses about originals.

## How It Could Fail

The query-time approach has its own costs: higher per-query expense, latency, and reliance on source availability. For personal wikis with active review, write-time synthesis remains superior. The tradeoff favors query-time only when organizational scale makes active human review infeasible and long-term trustworthiness outweighs speed.
