---
name: Typed-Edge Knowledge Graph for Agent Token Reduction
summary: Restructuring a knowledge base from human-centric folder hierarchies (PARA) to AI-optimized atomic nodes with typed edges (supports, contradicts, depends-on, derived-from) reduced token consumption
  from ~9,000 to ~600 for equivalent queries — a ~93% reduction. Typed links let agents prune traversal paths without reading full documents. 16 node types proposed; each node carries a one-sentence summary
  for agent triage before loading full content.
implementation_notes: MetaSystem already uses frontmatter metadata and typed related_findings links (enables, contradicts, extends, same-problem). The token reduction claim is unverified (single practitioner,
  no methodology). Worth monitoring for independent validation before restructuring KB around atomic-node principles.
category: Context Engineering
evidence_strength: Anecdotal
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- karpathy-second-brain-typed-edge-alternative.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-25'
related_findings:
- file: typed-relationship-memory-graph.md
  rel: extends
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ai-readable-naming-conventions-as-a-navigation.md
  rel: same-problem
- file: background-hooks-as-token-economy.md
  rel: same-problem
- file: ai-as-primary-reader-design-principle.md
  rel: enabled-by
- file: summary-gate-agent-traversal-pattern.md
  rel: enables
- file: untyped-links-as-token-waste-anti-pattern.md
  rel: enables
- file: human-to-ai-knowledge-architecture-migration.md
  rel: enables
- file: ai-delegated-knowledge-organization.md
  rel: enables
- file: token-economics-as-architecture-driver.md
  rel: enabled-by
pipeline_status: raw
tags:
- context-engineering
- memory
- knowledge-management
- session-95-reextract
---

# Typed-Edge Knowledge Graph for Agent Token Reduction

## What It Is

An AI-optimized knowledge base architecture using atomic nodes with typed edges, replacing human-centric folder hierarchies (e.g., PARA: Projects/Areas/Resources/Archive). Each node is a single concept with a one-sentence summary. Edges carry explicit relationship types (supports, contradicts, depends-on, derived-from, related-to, part-of, preceded-by, followed-by, authored, tagged). 16 node types proposed (decisions, concepts, hypotheses, patterns, sources, etc.).

## Why It Matters

Typed edges let agents prune traversal paths without reading full documents. The practitioner claims a same-data query went from ~9,000 tokens (untyped PARA structure) to ~600 tokens (typed atomic nodes) — though this is a single uncontrolled test. The atomic note size guideline (50-300 lines) and mandatory one-sentence summaries enable agents to decide whether to load full content before spending tokens.

## Why People Are Using It

The practitioner reports active use with multiple clients: "It's working way better for me. It's way working way better for my clients. I'm using this for data. I'm using this for design. I'm using this for analysis. I'm using this for building knowledge libraries or SOP libraries." The system is framed around five pillars: (1) atomic notes at 50-300 lines, (2) 16 node types, (3) 10 typed edge types, (4) one-sentence summaries per node for agent triage, and (5) AI-delegated organization (the AI builds and maintains the graph, the human provides raw input).

The practitioner describes a specific failure scenario with PARA-style structures: "It's really hard for an AI to be like, 'I want to know the pricing decision made on this certain day' and find it. It has to look at your pricing document and read the entire long document that would have been in this old system. And probably a lot of that's wasted tokens." The typed-graph alternative lets the agent navigate directly to the decision node and trace its provenance through typed edges.

## Re-extraction Note — 2026-05-25

Full transcript re-extraction (session 95) yielded 6 additional findings decomposed from this parent pattern: AI-as-primary-reader design principle, summary-gate agent traversal pattern, AI-delegated knowledge organization, human-to-AI knowledge architecture migration, knowledge graph as persistent institutional memory, untyped links as token waste anti-pattern, and token economics as architecture driver. These capture the meta-principles and sub-patterns that the original extraction compressed into a single finding.

## How It Could Fail

The 93% reduction claim is unverified — no methodology, no reproducible benchmark, single practitioner. Atomic node overhead (splitting, maintaining typed edges) could exceed the token savings for small KBs. The 16 node types and 10 edge types add schema complexity that may not be justified at current scale.
