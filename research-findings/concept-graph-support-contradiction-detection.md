---
name: Concept Graph with Support/Contradiction Detection
summary: An LLM-maintained knowledge graph that checks each new piece of ingested content against existing concepts to classify whether it supports or contradicts them, then generates actionable daily briefs
  with full attribution chains. Goes beyond wiki compilation by encoding relationships between ideas, not just the ideas themselves.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- tastematter-concept-graph-mcp-ai-signal.md
related_findings:
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: extends
- file: compounding-knowledge-loop-internal-data.md
  rel: same-problem
- file: dual-ingestion-funnel-human-clip-plus-llm-research.md
  rel: same-problem
- file: mcp-accessible-concept-graph-domain-context.md
  rel: companion
- file: claude-code-daily-brief-multi-source-inbox-obsidian.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-27'
pipeline_status: synthesized
consumed_by:
  - "session-persistence-and-memory.md"
---

## What It Is

A knowledge graph where each newly ingested piece of content (tweet, newsletter, research paper, YouTube video) is processed by the LLM not just to summarize it, but to check it against existing concepts and classify whether it **supports** or **contradicts** them. The graph stores:

- Concepts (289+ in TasteMatter, organized by topic clusters)
- Source articles/posts (with attribution to author, platform, timestamp)
- Relationships: support edges and contradiction edges between concepts and sources

The LLM then synthesizes these relationships into a daily brief where every signal has:
1. A specific **action item** (not just a summary)
2. A **supporting context chain** tracing back to the originating source
3. Contradiction flags when conflicting evidence exists

Key mechanics:
- **Self-organizing taxonomy**: The graph clusters concepts automatically without manual category assignment. This can produce taxonomy bloat (289 concepts in days) requiring periodic pruning.
- **Temporal layering**: Timely signals surface in the daily brief; older signals persist in the long-tail graph for later retrieval.
- **Attribution chain**: Every brief item traces back to the person, post, and timestamp — enabling tradeoff decisions grounded in who found what under what conditions.

## Why It Matters

Most knowledge management systems encode *what happened* but not *how ideas relate*. A concept graph with contradiction detection encodes the epistemic state of a domain — where practitioners agree, where they conflict, and which signals are actionable right now. This is particularly valuable in a fast-moving field like AI engineering where contradictory findings (e.g., "memory architecture matters more than model choice") emerge weekly.

The actionable brief format (action item + attribution chain) addresses a core failure mode of knowledge bases: they accumulate information without converting it into decisions. By forcing every signal to a specific action item, the system serves as a decision-support layer, not just a reference.

## Why People Are Using It

TasteMatter (practitioner-built, in active daily use). The builder originally built it for personal overwhelm management — unable to keep up with the AI engineering signal-to-noise ratio. The pattern mirrors how a skilled analyst processes a literature review: synthesizing agreement and disagreement across sources, not just cataloging them.

## Potential Improvements

- **Contradiction resolution workflow**: When two sources contradict each other, surface both with a prompt to the human to adjudicate and record the outcome — turning contradictions into decisions.
- **Concept merge/prune pipeline**: Self-organizing taxonomy needs periodic human or LLM-driven cleanup to collapse synonymous concepts. This is a known failure mode from the TasteMatter demo (taxonomy bloated from hundreds of concepts in days).
- **Confidence-weighted relationships**: Weight support/contradict edges by the authority tier of the source.
- **Domain-specific graph subsets**: Allow querying a subgraph scoped to a domain (e.g., "only context engineering findings") rather than the full graph.

## Potential Failure Modes

- **Taxonomy bloat**: Self-organizing taxonomy with no pruning produces a long tail of near-duplicate concepts that degrade retrieval quality. Demonstrated live in the TasteMatter demo.
- **Attribution chain staleness**: Sources from months ago remain in the graph but their context (what was being debated at the time) may no longer be relevant.
- **Support/contradict false positives**: The LLM may incorrectly classify a nuanced finding as contradicting a concept when it actually qualifies it. This poisons the reliability of the brief.
- **Action item quality**: If the action item generation step is too generic, the brief becomes another summarization layer rather than a decision tool.
