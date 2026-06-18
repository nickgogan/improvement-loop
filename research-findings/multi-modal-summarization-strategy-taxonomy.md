---
name: Multi-Modal Summarization Strategy Taxonomy with Structured Preservation Template
summary: Four distinct summarization modes (all-at-once, sliding-window, self-compact-all, self-compact-sliding-window) with a 7-section template that explicitly preserves identifiers, lookup hints, and error/fix history during compaction. Fills the gap between 'when to compact' and 'how to compact well'.
implementation_notes: null
category: Context Engineering
evidence_strength: "Medium (practitioner-documented)"
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
related_findings:
- file: proactive-compaction-before-intelligence-degradation.md
  rel: extends
- file: two-threshold-compaction-strategy.md
  rel: extends
pipeline_status: raw
---

# Multi-Modal Summarization Strategy Taxonomy with Structured Preservation Template

## What It Is

A taxonomy of four distinct summarization modes — all-at-once (summarize the entire evicted window into a single summary), sliding-window (summarize only the evicted prefix while keeping recent messages intact), self-compact-all (the agent itself summarizes its full context), and self-compact-sliding-window (agent self-summarizes with windowing) — combined with a 7-section structured template that explicitly instructs the summarizer to preserve identifiers, lookup hints, and error/fix history. The template closes the gap between knowing when to compact and knowing how to compact without losing operationally critical details.

## Why It Matters

Most compaction implementations treat summarization as a generic "make this shorter" task, which systematically strips the details agents need most: entity identifiers that enable future lookups, error patterns that prevent repeated failures, and cross-reference hints that maintain navigability. A structured preservation template ensures that compaction produces usable summaries rather than merely shorter text.

## Why People Are Using It

Observed in [Letta](https://github.com/letta-ai/letta) v0.16.8 — see [[letta-analysis]] for structural details. The system implements all four modes with configurable defaults per provider (Haiku 4.5 for Anthropic, GPT-5-mini for OpenAI, Gemini 2.5 Flash for Google), and the structured prompt template is visible in `prompts/summarizer_prompt.py` with explicit sections for what must be preserved.

## Potential Alternatives

Single summarization strategy with variable aggressiveness (simpler but one-size-fits-all). Extractive summarization that pulls key sentences verbatim (preserves exact wording but may miss synthesized insights). Embedding-based archival where old context is retrievable via semantic search rather than summarized (avoids lossy compression entirely).

## Potential Improvements

Adaptive mode selection based on conversation characteristics (e.g., high-entropy debugging sessions get sliding-window; low-entropy chat gets all-at-once). Post-compaction validation that checks whether preserved identifiers are still resolvable. User-configurable preservation priorities beyond the fixed 7-section template.

## Potential Failure Modes

The 7-section template may not cover domain-specific preservation needs, causing silent information loss in specialized contexts. Self-compact modes rely on the agent's own judgment about what matters, which can be biased toward recent or salient content. Provider-specific summarizer models may produce inconsistent quality across the four modes, making behavior unpredictable when switching providers.
