---
name: 'Dual Ingestion Funnel: Human Clip + LLM Research'
summary: 'Two parallel data ingestion paths: human-driven via Web Clipper (user manually clips web pages into raw/ folder) and LLM-driven where Claude Code autonomously conducts web research and creates
  raw markdown files or directly generates wiki articles. The raw/ folder is ''more for you, the human'' while Claude can bypass it.'
implementation_notes: 'Relevant to MetaSystem''s research-loop: the skill already does LLM-driven research ingestion while human sources come through manual URL submission.'
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in:
- Improvement Loop
sources:
- karpathys-obsidian-rag-claude-code.md
related_findings:
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: extends
- file: obsidian-web-clipper-local-images-ingestion-pipeline.md
  rel: extends
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: same-problem
- file: context-infrastructure-seven-level-maturity-model.md
  rel: enables
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
---
# Dual Ingestion Funnel: Human Clip + LLM Research

## What It Is
A knowledge base architecture with two parallel ingestion paths operating simultaneously. The human path uses Obsidian Web Clipper to manually capture web pages into a raw/ staging folder, where the human reviews and curates before promotion to the main knowledge base. The LLM path has Claude Code autonomously conducting web research, creating raw markdown files, or directly generating polished wiki articles that bypass the raw/ staging folder entirely. The raw/ folder is explicitly described as "more for you, the human" — a curation space that the LLM does not need because it can generate structured output directly.

## Why It Matters
Human and LLM ingestion have fundamentally different characteristics. Humans are good at serendipitous discovery (noticing relevant content while browsing) but slow at structuring it. LLMs are fast at structured extraction but need explicit direction on what to research. A dual-funnel architecture leverages both strengths without forcing either path through the other's workflow. This prevents the LLM from being bottlenecked by human curation and prevents humans from being overwhelmed by LLM output volume.

## Why People Are Using It
Chase AI demonstrates the Karpathy-inspired setup where Web Clipper captures are reviewed in the raw/ folder while Claude Code independently researches topics and writes wiki entries. The two paths feed the same knowledge base but through different processing pipelines appropriate to their origin.

## Potential Improvements
The two paths currently operate independently with no cross-referencing — the LLM does not know what the human has clipped, and the human may not see what the LLM has researched. A shared intake log or dashboard showing recent additions from both paths would improve coordination. Deduplication between human clips and LLM research would prevent the same content from entering through both funnels.

## Potential Failure Modes
Without coordination, the two funnels may produce contradictory entries on the same topic — a human clip capturing one perspective and an LLM article capturing another, with no reconciliation. The LLM bypass of raw/ staging means its output receives less human scrutiny, which could allow low-quality or hallucinated content into the knowledge base. Over time, the knowledge base may develop an uneven quality distribution where human-curated entries are reliable but sparse while LLM-generated entries are plentiful but less trustworthy.
