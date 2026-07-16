---
name: Untyped Links as Token Waste Anti-Pattern
summary: When knowledge base links carry no relationship type (just 'A links to B'), the agent must load and read both endpoints to determine the nature of the relationship — whether it supports, contradicts,
  depends on, or is merely tangentially related. This forces exhaustive document loading at every traversal step, directly causing the 15x token overhead observed when comparing untyped PARA links to typed
  graph edges.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- karpathy-second-brain-typed-edge-alternative.md
related_findings:
- file: typed-edge-knowledge-graph-token-reduction.md
  rel: enables
- file: typed-relationship-memory-graph.md
  rel: same-problem
- file: concept-graph-support-contradiction-detection.md
  rel: same-problem
- file: token-waste-taxonomy-and-two-mode-workflow.md
  rel: extends
- file: ai-as-primary-reader-design-principle.md
  rel: enables
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- extracts/rules/untyped-links-as-token-waste.md
- structuring-agent-context.md
tags:
- session-95-reextract
---

# Untyped Links as Token Waste Anti-Pattern

## What It Is

An anti-pattern where knowledge base links between documents carry no semantic type — they indicate only "A is connected to B" without specifying how. This forces AI agents into exhaustive document loading: to understand whether document B supports, contradicts, or is merely tangentially related to document A, the agent must load and read document B in full.

The practitioner identifies this as the primary structural cause of token waste in PARA-style knowledge bases: "Instead of just linking things together, I actually made more complex edge types. An edge basically means like connecting from one to the other. Like, what is the connection? Instead of just saying, 'Hey, they link,' it's like, 'What is the nature of that link?'"

Three specific failure modes of untyped links:

1. **Forced full-document reads** — the agent sees "pricing-philosophy links to no-free-tier-decision" but cannot determine the relationship type without reading both documents. With a typed edge (`depends-on`), the agent knows the relationship without loading either
2. **Irrelevant traversals** — an agent investigating conceptual relationships follows operational links (preceded-by, followed-by) because all links look the same. With typed edges, the agent can skip operational links when doing conceptual analysis: "It's not even relevant for what we're talking about. It's just — it's only relevant if you're looking at the operations side, not relevant if you're thinking conceptually."
3. **Traversal explosion** — without type information, every link is equally likely to be relevant, so the agent tends to follow more links than necessary, loading documents that turn out to be tangentially related

The anti-pattern is common because untyped links are the default in most knowledge management tools — Obsidian wiki-links, markdown hyperlinks, Notion relations — all create connections without requiring the user to specify relationship semantics.

## Why It Matters

Typed edges are a form of metadata investment: they cost a small amount of effort at write time (classifying the relationship) but save significant token expenditure at read time (every agent query that traverses that edge benefits from knowing the relationship type without loading documents). The ROI scales with query frequency — the more times an edge is traversed, the more tokens the upfront typing investment saves.

For MetaSystem: the IL KB's `related_findings` field already uses typed relationships (enables, contradicts, extends, same-problem). This is the correct approach. The anti-pattern warning applies to other parts of MetaSystem where links are untyped — Obsidian wiki-links between governance documents, cross-references in CLAUDE.md reference tables, and skill-to-finding pointers in the extraction pipeline.

## Why People Are Using It

The practitioner's before/after comparison: same data, same query, untyped PARA links consumed ~9,000 tokens, typed graph edges consumed ~600 tokens. The 10 edge types (supports, contradicts, depends-on, derived-from, related-to, part-of, preceded-by, followed-by, authored, tagged) provide the semantic vocabulary for the agent to prune traversals.

This aligns with the typed-relationship memory graph finding (updates/extends/derives) from Supermemory and the concept graph with support/contradiction detection from TasteMatter — independent practitioner convergence on the same principle.

## Potential Improvements

- **Retroactive typing** — AI-assisted classification of existing untyped links, reviewing the content of both endpoints to suggest a relationship type
- **Typing vocabulary standards** — converging on a shared vocabulary of relationship types across tools and knowledge bases, so agents trained on one vocabulary can navigate another
- **Graduated typing** — supporting a `related-to` catch-all for genuinely ambiguous relationships while encouraging specific types for clear relationships

## Potential Failure Modes

- **Mis-typing** — a relationship classified as `supports` when it actually `contradicts` is worse than an untyped link, because the agent trusts the type and makes incorrect traversal decisions
- **Typing maintenance burden** — relationships can change over time (a supporting finding may be superseded by contradicting evidence), requiring edge type updates
- **Vocabulary disagreement** — different contributors typing the same relationship differently creates inconsistency that degrades agent trust in edge types
- **Over-typing** — creating too many edge types (20+) that overlap semantically, making classification ambiguous and the vocabulary harder for agents to reason about
