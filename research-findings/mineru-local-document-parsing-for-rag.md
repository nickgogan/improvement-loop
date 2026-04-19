---
name: 'MinerU: Local Document Parsing for RAG Pipelines'
summary: MinerU is an open-source local document parser used by RAG-Anything. Runs entirely on-device with specialized models (Paddle OCR for text, layout detection for structure). Breaks documents into
  component parts (headers, text, charts, equations, images) before routing to specialized extraction models. Supports CPU and GPU execution.
implementation_notes: null
category: Tool Integration
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
last_updated: '2026-04-08'
related_findings:
- file: rag-anything-multimodal-document-processing.md
  rel: enables
- file: dual-path-rag-ingestion-text-vs-multimodal.md
  rel: enabled-by
pipeline_status: "raw"
consumed_by: []
---
## What It Is

MinerU is an open-source document parser that runs locally and forms the core of RAG-Anything's document processing pipeline. It performs two-stage processing: (1) layout detection -- identifies document components (headers, text blocks, charts, images, LaTeX equations) by drawing bounding boxes around each element, and (2) specialized extraction -- routes each component to a purpose-built model (Paddle OCR for text, equation parsers for LaTeX, screenshot capture for charts/images that cannot be converted to text).

The output is two buckets: text (everything that could be converted to readable text) and images (screenshots of visual content that resists text conversion). These buckets are then sent to an LLM for entity/relationship extraction and embedding generation.

Key technical details: runs on CPU by default (slower), can be configured for GPU via PyTorch configuration. Open source. Handles scanned PDFs that are not technically text -- a common real-world document type that defeats most RAG systems. Handles LaTeX equation extraction and rendering, preserving mathematical notation that other parsers typically flatten or corrupt.

## Why It Matters

Most RAG systems fail on non-text content. MinerU's local-first, multi-model approach handles the full spectrum of document types without sending raw documents to external APIs. The cost savings are significant -- local OCR and layout detection are free, and only the entity extraction step requires an LLM API call.

## Why People Are Using It

Chase AI demonstrates MinerU as part of the RAG-Anything + LightRAG stack. The tool handles scanned PDFs, charts, and equations -- document types that pure text RAG cannot process. The local execution model avoids per-document API costs for the parsing stage.

## Potential Improvements

Could be integrated into MetaSystem's research pipeline for processing PDF sources that contain charts or diagrams. Currently research intake is text-only.

## Potential Failure Modes

CPU-mode parsing is slow for large document sets. Layout detection accuracy varies with document formatting quality. The two-bucket approach (text vs image) may miss hybrid elements. Model download size adds to initial setup time.
