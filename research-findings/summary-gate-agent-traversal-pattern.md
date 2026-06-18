---
name: "Summary-Gate Agent Traversal Pattern"
summary: "Each knowledge node carries a mandatory one-sentence summary that the agent reads before deciding whether to load the full document. The agent spends ~50 tokens on the summary to decide whether to spend ~500 tokens on the full content. This creates a two-phase retrieval: scan summaries (cheap), then load selected documents (expensive). Generalizes to any agent navigating a large document store."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "karpathy-second-brain-typed-edge-alternative.md"
related_findings:
  - file: typed-edge-knowledge-graph-token-reduction.md
    rel: enables
  - file: progressive-tiered-context-loading-convergence.md
    rel: same-problem
  - file: tool-registry-metadata-first-design.md
    rel: same-problem
  - file: push-vs-pull-context-loading.md
    rel: same-problem
  - file: claudemd-as-knowledge-base-traversal-guide.md
    rel: same-problem
  - file: agent-context-kiss-commandments-minimum-viable.md
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "structuring-agent-context.md"
  - "rules/knowledge-node-mandatory-summary-field.md"
tags:
  - "session-95-reextract"
---

# Summary-Gate Agent Traversal Pattern

## What It Is

A retrieval pattern where every knowledge node in a graph or document store carries a mandatory one-sentence summary field. When an agent is exploring the knowledge base, it reads summaries first (cheap — ~50 tokens each) and uses them to decide which full documents to load (expensive — potentially hundreds or thousands of tokens each). This creates a two-phase retrieval cycle:

1. **Scan phase:** Agent reads node summaries and edge types from the current node's neighbors
2. **Select phase:** Agent decides which neighbors are relevant to the current query
3. **Load phase:** Agent reads full content of selected nodes only

The practitioner describes it: "Before it even reads it and uses the tokens on it, it can then read this quick little summary which is like, 'Hey, this is the idea in one sentence.' Do you want to — and then the AI can basically decide, 'Okay, do I want to — I spent 50 tokens reading this sentence. Do I now want to go down and read more in depth on the whole topic?'"

This is distinct from progressive context loading (which loads tiers of the same document) — the summary gate operates at the inter-document level, helping the agent decide which documents to visit at all.

## Why It Matters

In a knowledge base with hundreds or thousands of nodes, an agent that loads every document it encounters will quickly exhaust its context window with marginally relevant content. The summary gate provides a cheap filtering layer that lets the agent make informed decisions about where to invest reading tokens.

The pattern is a generalization of several existing practices:
- **Tool registry metadata-first design** — tools carry descriptions; agents scan descriptions before invoking tools
- **Progressive tiered context loading** — L1 metadata is always loaded; L2/L3 loaded on demand
- **CLAUDE.md as traversal guide** — the navigation index serves a similar summary-first function

The video demonstrates this applied to a knowledge graph, but the pattern applies wherever an agent must choose between multiple documents: file systems, skill registries, API endpoint lists, research finding databases.

For MetaSystem: IL research findings already have a `summary` frontmatter field. This finding validates that design and suggests ensuring summaries are written with agent triage in mind — one sentence that helps the agent decide relevance without reading the body.

## Why People Are Using It

The practitioner reports that the summary-gate pattern (combined with typed edges) reduced token consumption from ~9,000 to ~600 for equivalent queries — a ~93% reduction. The summary acts as a cheap filter that prevents the agent from loading irrelevant documents, while typed edges let the agent prune entire traversal paths.

## Potential Improvements

- **Relevance-scored summaries** — summaries could be written to maximize distinctiveness, making it easier for the agent to differentiate between nodes. Formulaic summaries ("This is about X") are less useful than discriminating summaries ("X differs from Y because Z")
- **Query-conditioned summaries** — generating multiple summaries per node, each optimized for a different query type (factual lookup vs. decision support vs. debugging)
- **Summary quality metrics** — tracking how often agents load a full document after reading its summary. High load rates suggest the summary is not discriminating enough

## Potential Failure Modes

- **Summary drift** — if the summary is not updated when the document changes, it becomes a misleading gate that causes agents to skip relevant documents or load irrelevant ones
- **Summary quality variance** — inconsistent summary quality across nodes degrades the pattern's reliability. Some nodes have crisp discriminating summaries; others have vague ones
- **False negatives** — agents may skip relevant documents because the summary does not mention the aspect the agent is looking for. This is the retrieval recall problem at the summary level
- **Overhead for small KBs** — for knowledge bases under ~50 nodes, the summary scan phase may cost more tokens than just loading everything directly
