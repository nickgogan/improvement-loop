---
name: 'Scalpel: Local Parse Then LLM Cost Optimization'
summary: Use local models as a 'scalpel' to pre-process documents before sending to expensive LLM APIs. MinerU handles layout detection, OCR, and text extraction locally (free), and only entity/relationship
  extraction hits the LLM. Dramatically cheaper than sending entire documents as screenshots to an LLM.
implementation_notes: 'Generalizable pattern: local/cheap models for structural decomposition, expensive API calls for semantic understanding only.'
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-plus-rag-anything.md
related_findings:
- file: rag-anything-multimodal-document-processing.md
  rel: extends
- file: dual-path-rag-ingestion-text-vs-multimodal.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: dual-path-rag-ingestion-text-vs-multimodal.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "synthesized"
consumed_by:
  - "session-persistence-and-memory.md"
---
# Scalpel: Local Parse Then LLM Cost Optimization

## What It Is
A cost optimization pattern where local, free models handle the structural decomposition of documents (layout detection, OCR, text extraction, image segmentation) and expensive LLM API calls are reserved exclusively for semantic understanding (entity extraction, relationship mapping, summarization). MinerU serves as the local "scalpel" — it parses PDFs, handles complex layouts, extracts text blocks, and identifies images without any API cost. Only the extracted, structured content is then sent to the LLM for higher-order reasoning.

## Why It Matters
Sending raw documents (especially as screenshots) to LLM APIs is extremely expensive and wasteful — the LLM spends tokens on layout parsing that a local model can do for free. This pattern can reduce API costs by an order of magnitude for document-heavy workflows. It also improves quality because the LLM receives clean, structured input rather than raw pixels, reducing hallucination from OCR ambiguity.

## Why People Are Using It
Chase AI demonstrates the cost difference explicitly: processing a multi-page document via screenshots to an LLM versus using MinerU locally first and only sending extracted text. The local-first approach is not just cheaper but also faster, since local parsing runs without network latency or rate limits.

## Potential Improvements
The pattern currently relies on MinerU specifically, but the principle generalizes to any local parsing tool. A pluggable parser interface that can swap between MinerU, Marker, Docling, or other local extraction tools based on document type would increase robustness. Quality validation between the local parse step and the LLM step could catch extraction errors before they propagate.

## Potential Failure Modes
Local parsing models may miss or misinterpret complex layouts (nested tables, multi-column academic papers, handwritten annotations), producing corrupted input for the LLM. The two-stage pipeline introduces a failure boundary — if the local parse silently drops content, the LLM has no way to know what it is missing. Documents with tightly integrated text and visuals (infographics, annotated diagrams) may lose critical context when decomposed into separate text and image streams.
