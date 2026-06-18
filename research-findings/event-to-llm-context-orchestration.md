---
name: Events as Ground Truth, LLM Context as Orchestrated Derived View
summary: Events as ground truth, LLM context as orchestrated derived view. Three pollution-prevention strategies — delegation translation (tool-call results only), branch isolation (parallel paths don't see siblings), history compaction (condense old turns). Separates what happened from what the model sees.
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
- file: ace-agentic-context-engineering-rag-based.md
  rel: extends
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
pipeline_status: raw
---

# Events as Ground Truth, LLM Context as Orchestrated Derived View

## What It Is

An architectural pattern where all agent activity is persisted as an immutable event stream (the ground truth), while what the LLM actually sees in its context window is a separately orchestrated, filtered view derived from those events. Three distinct pollution-prevention strategies keep the derived view clean: delegation translation (sub-agent task results are compressed to tool-call outputs only), branch isolation (parallel execution paths cannot see each other's history), and history compaction (older turns are condensed to preserve budget for recent context).

## Why It Matters

Without this separation, agent context degrades in proportion to system complexity. Multi-agent handoffs, parallel execution, and long conversations all inject noise into the LLM's view, reducing output quality. By treating events and LLM context as fundamentally different data structures with different lifecycles, systems can scale in complexity without proportional context degradation.

## Why People Are Using It

Observed in [Google ADK-Python](https://github.com/google/adk-python) v2.0.0 — see [[adk-python-analysis]] for structural details. The pattern emerges from Google's need to support graph-based multi-agent workflows where dozens of nodes execute concurrently, each generating events that would overwhelm any single agent's context window if passed through unfiltered.

## Potential Alternatives

Flat conversation history with aggressive summarization (simpler but loses the event audit trail). RAG over event history (retrieval-based rather than structural filtering). Per-agent context windows without shared event store (loses coordination visibility).

## Potential Improvements

Configurable filter policies per node type would allow fine-grained control over what each agent sees. A "context replay" mechanism could reconstruct any historical point-in-time view from the event stream for debugging. Priority-weighted event inclusion could replace binary include/exclude decisions.

## Potential Failure Modes

Over-aggressive filtering strips context the model actually needs, causing hallucinated assumptions. Branch isolation prevents agents from learning useful information discovered by siblings. Compaction loses details that become relevant later (e.g., error patterns from early turns). The complexity of maintaining two parallel representations (events + views) increases debugging surface area.
