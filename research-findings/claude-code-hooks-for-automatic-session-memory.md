---
name: Claude Code Hooks for Automatic Session Memory
summary: Three Claude Code hooks (session_start, pre_compact, session_end) automatically capture conversation summaries into daily logs and promote them to a structured wiki, creating persistent session
  memory without manual intervention.
implementation_notes: MetaSystem already has PROGRESS.md as a manual bridge. Hooks could automate a similar capture into the Improvement Loop KB. Directly actionable with existing Claude Code infrastructure.
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- self-evolving-claude-code-memory.md
proposals: []
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: structured-fact-extraction-from-conversations.md
  rel: same-problem
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Claude Code Hooks for Automatic Session Memory

## What It Is
A three-hook system where session_start loads agents.md (system rules) + index.md (file map) into context, pre_compact sends conversation to Claude Agent SDK to produce a structured summary appended to daily-logs/, and session_end fires the same capture on close. A daily flush process extracts concepts and connections from logs and promotes them to wiki pages. Hooks are defined in settings.json; scripts use the Claude Agent SDK (included with Anthropic subscription).

Additional post-session hook use case: auto-pushing to a git branch to keep git status clean, which is itself a context optimization (dirty git status adds noise to every session). The daily flush mechanics run once per day, extracting concepts AND connections as separate categories from daily-logs/, then promoting them to wiki/concepts/ and wiki/connections/ folders respectively. Note: agents.md is a complete system architecture description (not just a set of rules) — it gives the agent meta-reasoning about its own memory system, enabling it to understand why and how it captures and retrieves knowledge.

## Why It Matters
Every session currently loses context. Hooks automate the capture-and-promote cycle with zero manual effort, creating compounding memory from normal work.

## Why People Are Using It
Cole Medin demos a working implementation; open-source repo at github.com/coleam00/claude-memory-compiler. One-shot setup via Karpathy's gist prompt.

## Potential Alternatives
Manual PROGRESS.md updates, semantic memory plugins (mem0, OpenClaw/Hindsight), periodic manual knowledge base curation.

## Potential Improvements
Incremental compilation instead of full daily flush. Noise filtering to avoid polluting wiki with low-value session chatter.

## Potential Failure Modes
Hook failures silently lose data. Daily flush without supervision can promote low-quality or contradictory entries. Over-reliance on automated extraction may miss nuance that requires human judgment.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[hook-based-automatic-session-memory]] in `extracts/patterns/`
