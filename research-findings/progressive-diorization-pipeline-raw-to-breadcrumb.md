---
name: "Progressive Diorization Pipeline: Raw Recordings to AI Breadcrumbs"
summary: "You cannot pump 100,000 hours of recordings into a context window. The pattern: record everything (raw capture) → diorize/categorize into semantic areas (fundraising, hiring, disputes) → synthesize into distilled knowledge artifacts → give AI breadcrumbs (pointers to relevant synthesized content). Each stage reduces volume while preserving what matters. YC regenerated a 150-page user manual from 2,000 hours of recordings in one weekend using this pipeline."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "self-improving-company-yc-five-layer-loop.md"
related_findings:
  - file: "total-organizational-legibility-as-ai-prerequisite.md"
    rel: "enables"
  - file: "distillator-with-round-trip-validation.md"
    rel: "same-problem"
  - file: "ace-delta-updates-over-monolithic-rewrites.md"
    rel: "same-problem"
  - file: "lossy-compression-boundary-headless-return.md"
    rel: "same-problem"
  - file: "four-tier-agent-memory-model-with-write-policy.md"
    rel: "extends"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "classified"
consumed_by: []
tags:
  - "session-95-reextract"
---

# Progressive Diorization Pipeline: Raw Recordings to AI Breadcrumbs

## What It Is

A multi-stage compression pipeline that transforms raw organizational data (recordings, messages, emails) into AI-consumable context. The pipeline has four stages:

1. **Raw capture** — Record everything (meetings, office hours, Slack, emails). Store permanently.
2. **Diorization** — Categorize and segment raw content into semantic areas (e.g., fundraising, hiring, co-founder disputes, product strategy).
3. **Synthesis** — Within each category, distill down to the important parts. Generate coherent knowledge artifacts (a user manual, a decision log, a policy document).
4. **Breadcrumbs** — Give AI systems pointers to the synthesized content rather than the raw data. The AI navigates breadcrumbs to find relevant context on demand.

YC example: 2,000 hours of recorded office hours → categorized into topic areas → synthesized into a 150-page user manual in one weekend. The manual is now refreshed monthly: each new piece of advice is compared against the existing manual and either incorporated or discarded.

## Why It Matters

The fundamental constraint of LLM-based systems is context window size. Raw organizational data easily exceeds any context window by orders of magnitude. Without a compression pipeline, organizations face a choice between "give AI nothing" and "give AI a random slice." Neither works. Progressive diorization solves this by creating intermediate representations at different granularities — each usable for different purposes.

For MetaSystem: the IL pipeline performs a version of this for research (raw sources → extracted findings → synthesized guides). The transcript fetcher → research-loop extraction is effectively stages 1-3. The missing piece is the "breadcrumb" layer — a routing mechanism that tells an agent "for context about X, look at finding Y" without loading all findings into context.

## Why People Are Using It

YC internal system (2026). The 150-page user manual regeneration demonstrates the pattern working end-to-end: raw data in, usable synthesized artifact out, in a single weekend. Monthly refresh shows the pipeline can run continuously, not just once.

## Potential Improvements

- Add verification at each compression stage (round-trip validation a la Distillator) to catch lossy compression.
- Build the breadcrumb layer as a structured index rather than just a flat file — enable semantic search across synthesized artifacts.
- Make the categorization taxonomy itself self-improving (new categories emerge from data, stale ones merge).

## Potential Failure Modes

- Each compression stage is lossy. Without verification, critical nuances can be silently discarded.
- The categorization step requires domain judgment — incorrect categories cause information to be routed to the wrong synthesis bucket and lost to queries.
- Monthly refresh cycles may be too slow for fast-moving contexts (daily decisions, rapid product changes).
- The "150-page manual" may contain AI hallucinations or confident synthesis of contradictory advice — quality control at the synthesis stage is critical.
