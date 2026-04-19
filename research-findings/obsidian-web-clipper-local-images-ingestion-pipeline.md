---
name: Obsidian Web Clipper + Local Images Plugin as Research Ingestion Pipeline
summary: A two-tool combination (Obsidian Web Clipper Chrome extension + Local Images Plus community plugin) that converts any web page into a markdown file with locally cached images, auto-routed to a
  raw/ staging folder for wiki compilation.
implementation_notes: MetaSystem's research-loop currently processes URLs via transcript-fetcher and Perplexity. The Web Clipper pipeline would add a manual but high-fidelity ingestion path for blog posts,
  documentation, and articles that are not video content.
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- karpathys-obsidian-rag-claude-code.md
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: firecrawl-cli-for-research-ingestion.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---

## What It Is

A lightweight research ingestion pipeline using two Obsidian ecosystem tools:

1. **Obsidian Web Clipper** (Chrome extension at obsidian.md/clipper): Converts any web page to a markdown file. Configuration: set the "note location" in the clipper template to `raw/` so clipped pages auto-route to the staging folder.
2. **Local Images Plus** (Obsidian community plugin): Automatically downloads images referenced in markdown files and stores them locally in the vault. Without this plugin, the Web Clipper only captures image URLs (which break when the source changes).

Setup steps from the Chase AI tutorial:
- Install Web Clipper extension and configure default template location to `raw/`
- Install Local Images Plus from Obsidian community plugins, enable it
- Clip any web page -> it lands in raw/ with local images
- Claude Code then compiles raw/ contents into structured wiki articles

The raw/ folder serves as a staging area where both human-clipped content and Claude Code's own web research output accumulate before being organized into the wiki structure.

## Why It Matters

Research ingestion is the bottleneck for knowledge base quality. The Web Clipper provides a one-click path from "interesting article" to "structured markdown in the vault." Local image caching prevents link rot and makes articles readable offline.

## Why People Are Using It

Chase AI demonstrates this as part of the Karpathy Obsidian RAG setup. The workflow is simple enough for non-technical users. Obsidian's community plugin ecosystem provides the image handling that the Web Clipper lacks natively.

## Potential Improvements

Automated clipper triggers (e.g., save-to-pocket integration). Metadata extraction (author, date, tags) during clipping. Batch clipping for research sessions.

## Potential Failure Modes

Web Clipper struggles with JavaScript-heavy pages (SPAs, dynamic content). Image-heavy pages produce large vault sizes. No deduplication if the same page is clipped multiple times.
