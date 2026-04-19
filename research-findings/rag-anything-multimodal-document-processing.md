---
name: 'RAG-Anything: Multimodal Document Processing for Claude Code'
summary: 'RAG-Anything wraps LightRAG to handle non-text documents (images, charts, equations). Dual-bucket processing: Paddle OCR for text extraction, AI model for image analysis. Creates two knowledge
  graphs (text + image) merged by matching entities into a unified queryable system.'
implementation_notes: null
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-plus-rag-anything.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: mineru-local-document-parsing-for-rag.md
  rel: enabled-by
pipeline_status: raw
consumed_by: []
---
# RAG-Anything: Multimodal Document Processing for Claude Code

## What It Is
A wrapper around LightRAG that extends it to handle non-text documents. Documents are scanned and split into text (via Paddle OCR) and image components. Both are processed by an AI model to extract entities, relationships, and embeddings. Creates four outputs — two vector DBs and two knowledge graphs — merged by matching entities into one unified queryable system. Integrated with Claude Code as a skill for seamless document ingestion.

## Why It Matters
Standard RAG can't process charts, diagrams, or equations embedded in documents. RAG-Anything bridges this gap for document-heavy workflows where visual content carries significant information.

## Why People Are Using It
Chase AI demonstrates integration with Claude Code as a skill — users say "use the RAG-Anything skill to ingest this document" and the complexity is abstracted away. Useful for technical documentation, research papers, and business reports with charts.

## Potential Alternatives
Manual image description before RAG ingestion. Multimodal embedding models that handle text and images natively. Claude's native vision capabilities for one-off image analysis without persistent storage.

## Potential Improvements
Performance optimization — currently computationally heavy for large document sets. Streaming processing for real-time ingestion. Better entity matching algorithms to reduce false merges between text and image graphs. GPT-5.4 nano model emerging as a cost-effective option for RAG extraction pipelines. Ollama local substitution enables fully local document processing without API costs.

## Potential Failure Modes
OCR quality varies significantly by document type and formatting. Entity matching between text and image knowledge graphs can produce false merges. Overkill for text-only workflows where standard RAG or Markdown wiki approaches suffice.
