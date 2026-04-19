---
name: Structured Fact Extraction from Conversations
summary: Memory systems that extract discrete, structured facts (decisions, preferences, relationships, technical context) from conversations outperform those that store raw transcripts. Hindsight extracts
  facts asynchronously in the background, tagging each with type, timestamp, and entities involved. This enables semantic recall by relevance rather than recency.
implementation_notes: 'MetaSystem''s current approach stores session notes as prose in PROGRESS.md. Structured fact extraction would convert ''we decided to use fractal pattern'' into a typed fact {type:
  decision, content: ''fractal pattern for system organization'', date: 2026-04-07, involving: [''MetaSystem'', ''DD-52'']}. This enables querying by decision type, entity, or timeframe.'
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- openclaude-build-a-claude-code-agent-with-long-ter.md
related_findings:
- file: biomimetic-memory-auto-recall-over-tool-based.md
  rel: same-problem
- file: claude-code-hooks-for-automatic-session-memory.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: enabled-by
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
---
## What It Is

A memory processing pattern from Hindsight and the broader agent memory community: instead of storing raw conversation transcripts, extract discrete structured facts in the background after each agent turn.

Hindsight's approach:
- **Auto-capture**: After each agent turn, the conversation is stored and processed asynchronously
- **Fact extraction**: Facts, entities, and relationships are extracted without blocking the response
- **Typed facts**: Each fact includes type (e.g., "world", "preference", "decision"), text content, timestamp, and entities involved
- **Semantic ranking**: At recall time, memories are ranked by semantic similarity and recency

Example:
```
User: I prefer JSON responses
-> Stored fact: {"text": "User prefers JSON responses", "type": "world", "when": "2026-01-30", "involving": "User"}
```

The fact is later auto-recalled when the user asks for any formatted output, even if they don't mention JSON.

Hindsight reuses whatever LLM provider is already configured (OpenAI, Anthropic, Gemini, Groq, Ollama, or Claude Code's own model), adding no separate API cost.

## Why It Matters

Raw transcript storage creates a recall problem: finding relevant context in thousands of lines of conversation requires either keyword search (brittle) or embedding the entire transcript (expensive). Structured facts are compact, typed, and individually embeddable, making recall precise and efficient.

The always-on agent community has independently discovered that "compaction kills context" -- Claude Code's built-in compaction summarizes away critical decisions. Structured fact extraction preserves decisions in a form that survives compaction because facts live outside the conversation window.

## Why People Are Using It

Multiple implementations exist: Hindsight (biomimetic, production-grade), claude-code-vector-memory (ChromaDB-backed with hybrid scoring: 70% semantic + 20% recency + 10% complexity), and Anthropic's own research on long-running Claude sessions using CHANGELOG.md as structured memory.

## Potential Improvements

Fact validation: cross-reference extracted facts against existing knowledge base entries to detect contradictions before they enter memory. Priority scoring: weight facts by their downstream impact (architectural decisions > preferences > one-time observations).

## Potential Failure Modes

Extraction quality depends on the LLM used. Subtle decisions embedded in multi-turn reasoning chains may be missed. Over-extraction creates a noisy memory store where trivial facts crowd out important ones. The extraction step adds latency and cost to every agent turn.
