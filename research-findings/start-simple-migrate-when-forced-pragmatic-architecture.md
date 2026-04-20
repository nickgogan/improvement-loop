---
name: Start Simple, Migrate When Forced (Pragmatic Architecture)
summary: 'Start with the simplest system that might work and only migrate to more complex infrastructure when hitting clear scaling limits. Anti-pattern: arguing about system choice before trying either.
  Applied to AI knowledge management: use Obsidian first, migrate to RAG only when scale forces it.'
implementation_notes: null
category: Agent Design
evidence_strength: Weak (theoretical)
adoption_status: Already Adopted
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in:
- General / Cross-System
sources:
- karpathys-obsidian-rag-claude-code.md
- karpathy-obsidian-rag-markdown-knowledge-base.md
related_findings:
- file: scale-threshold-heuristic-obsidian-vs-rag.md
  rel: extends
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Start Simple, Migrate When Forced (Pragmatic Architecture)

## What It Is
An architectural decision-making heuristic: always start with the simplest system that could plausibly work, and only migrate to more complex infrastructure when you hit concrete, measurable scaling limits that the simple system cannot overcome. The anti-pattern is debating system choices in the abstract before trying either option. Applied to AI knowledge management: start with an Obsidian vault (plain markdown files, no database, no embeddings), and only migrate to a RAG system when document count, query complexity, or retrieval latency demonstrably exceeds what file-based search can handle.

## Why It Matters
Complex systems have higher setup cost, higher maintenance burden, more failure modes, and more cognitive overhead — all of which are paid upfront regardless of whether the complexity is needed. Simple systems let practitioners start producing value immediately while deferring infrastructure investment until the actual scaling constraints are known (not hypothesized). This avoids the common trap of over-engineering for a scale that never arrives.

## Why People Are Using It
Chase AI frames the Obsidian-vs-RAG decision explicitly through this lens: Karpathy uses an Obsidian vault because it works at his current scale, and the advice is to use the same approach until you have concrete evidence that it does not scale. The video positions "which system should I use?" debates as premature optimization.

## Potential Improvements
The heuristic would benefit from explicit migration triggers — quantified thresholds (e.g., "when query latency exceeds X seconds" or "when document count exceeds Y") that signal when the simple system is reaching its limits. A pre-planned migration path (what to migrate to, how to export data) would reduce the cost of the eventual transition. Periodic scale assessments could prevent the "boiling frog" problem where gradual degradation goes unnoticed.

## Potential Failure Modes
The heuristic can justify staying with an inadequate system too long if "clear scaling limits" is interpreted too strictly — gradual quality degradation may not produce a clear breaking point. Some architectural choices are genuinely hard to migrate away from (data format lock-in, API dependencies), and starting simple with those may create costly technical debt. The heuristic also assumes the practitioner can recognize scaling limits when they arrive, which requires monitoring that simple systems often lack.
