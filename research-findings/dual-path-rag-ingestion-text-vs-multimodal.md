---
name: 'Dual-Path RAG Ingestion: Text vs Multimodal Document Routing'
summary: 'RAG-Anything implements a dual-path ingestion architecture: text documents go through LightRAG''s standard UI/API, while non-text documents route through a separate Python script (wrapped as a
  Claude Code skill). Both paths merge into a single knowledge graph and vector database. The split optimizes cost -- local parsing handles what it can, LLM API calls only for what requires vision.'
implementation_notes: The pattern of separate ingestion paths merging into a unified store is applicable to any system that handles mixed document types. The skill-wrapping of scripts is a reusable integration
  pattern.
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-plus-rag-anything.md
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: mineru-local-document-parsing-for-rag.md
  rel: enables
- file: "scalpel-local-parse-then-llm-cost-optimization.md"
  rel: "same-problem"
pipeline_status: "raw"
consumed_by: []
---
## What It Is

RAG-Anything's architecture requires two distinct ingestion paths that merge into a unified backend:

**Path 1 (text):** Standard LightRAG pipeline -- documents uploaded via web UI or API, processed into entities/relationships/embeddings, stored in knowledge graph + vector database.

**Path 2 (multimodal):** Non-text documents processed via a Python script that invokes MinerU for local parsing, then sends extracted text and image buckets to an LLM for entity/relationship extraction. Creates its own knowledge graph + vector database, then merges with LightRAG's stores by matching entities.

The practical integration uses Claude Code skills to abstract the complexity: users invoke a skill that runs the Python script, processes the document, and restarts the Docker container (required for merge to take effect). From the user's perspective, it is a single command.

The cost optimization is deliberate: local parsing (MinerU, Paddle OCR) handles the heavy lifting for free; only the entity extraction step hits the LLM API. This is cheaper and faster than sending entire documents as screenshots to an LLM.

## Why It Matters

Mixed document types are the norm in real-world knowledge bases. A system that handles both text and visual content through a single queryable interface eliminates the "can't process this PDF" failure mode. The skill-wrapping pattern (turning a Python script into a Claude Code skill) is a reusable integration technique.

## Why People Are Using It

Chase AI demonstrates the full pipeline end-to-end, including querying data extracted from bar charts in a PDF that would be invisible to text-only RAG. The dual-path approach is described as "the only weird part" -- everything else (querying, knowledge graph, embeddings) works identically to standard LightRAG.

## Potential Improvements

A unified ingestion endpoint that auto-detects document type and routes to the correct path would eliminate the dual-path complexity. LightRAG or RAG-Anything may add this in future versions.

## Potential Failure Modes

Docker restart requirement after multimodal ingestion is a fragile integration point. Two separate ingestion paths create maintenance burden and potential state inconsistencies. Entity matching during merge may produce duplicates or miss connections across the two paths.
