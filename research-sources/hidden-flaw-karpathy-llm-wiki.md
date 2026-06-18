---
name: "The Hidden Flaw in Karpathy's LLM Wiki"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Write-time synthesis (LLM authoring wiki content) causes KB poisoning at organizational scale: LLM outputs get re-indexed as authoritative sources, creating circular reinforcement disconnected from ground truth. Recommends query-time synthesis: extract structure (entities, relationships, tags) at ingestion, synthesize answers from originals at query time. Three principles: immutable originals, structure over prose, query-time synthesis."
relevance: "High"
added_by: "Nick"
tags:
  - "context-engineering"
  - "memory"
url: "https://foundanand.medium.com/the-hidden-flaw-in-karpathys-llm-wiki-e3a86a94b459"
authority: []
findings:
  - "write-time-vs-query-time-synthesis-kb-poisoning.md"
date_added: "2026-05-24"
date_processed: "2026-05-24"
---

# The Hidden Flaw in Karpathy's LLM Wiki

By Anand Lahoti (Medium, 2026-04-17).

Critiques Karpathy's LLM-compiled wiki pattern at organizational scale. While the write-time synthesis approach works for personal use with active review, it introduces a critical failure mode when deployed at team scale: knowledge base poisoning.

## Key Arguments

1. **KB Poisoning mechanism:** LLM-authored summaries drop specifics, get re-indexed as authoritative, and subsequent queries reason from LLM outputs rather than originals. Circular reinforcement disconnects the KB from ground truth.

2. **Distinction from RAG failures:** Standard RAG hallucinations come from retrieval problems but source documents remain intact. Write-time synthesis corrupts the sources themselves — retrieval works correctly but surfaces summaries-of-summaries that lost information.

3. **Two synthesis approaches:** Write-time amortizes cost but compounds errors. Query-time costs more per query but preserves chain of custody indefinitely.

4. **Three principles for teams:** Immutable originals (never let LLMs produce "cleaned up" versions for retrieval), structure over prose (extract verifiable structure rather than narrative), query-time synthesis (structure as navigation aids, answers from originals).
