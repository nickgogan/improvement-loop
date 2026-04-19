---
name: "Micro Compact: Stale Tool Call Removal Strategy"
summary: "An unreleased compaction strategy in Claude Code that removes tool calls older than the most recent five from agent context. Tool calls are identified as the most context-dense part of Claude Code sessions. Feature-flagged off, but signals Anthropic's direction on granular compaction."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: ["claude-codes-leak-changes-everything.md"]
date_discovered: "2026-04-07"
last_updated: 2026-04-08
related_findings:
  - file: "ace-delta-updates-over-monolithic-rewrites.md"
    rel: "same-problem"
  - file: "agent-context-kiss-commandments-minimum-viable.md"
    rel: "same-problem"
pipeline_status: "raw"
consumed_by: []
---

## What It Is

One of five compaction strategies found in Claude Code's leaked source code (most behind feature flags, off by default). Micro compact specifically targets stale tool calls -- calls older than the most recent five -- and removes them from agent context. This is notable because tool calls are the most token-dense elements in Claude Code sessions (they include full file contents, command outputs, etc.).

The video explicitly warns that most coverage of the leak presents all five compaction strategies as if they are live features. They are not -- most are experimental and feature-flagged off.

## Why It Matters

Tool call history accumulates rapidly and consumes disproportionate context. A single file read can be thousands of tokens. Removing stale tool calls (while keeping the five most recent) is a targeted optimization that addresses the highest-density context elements first. This aligns with the general principle of keeping only task-relevant context.

The transcript explicitly warns that most coverage of the leak incorrectly presents all five compaction strategies as live features -- they are not. Most are behind feature flags that are off by default. Micro compact is one of these unreleased strategies. A related finding from the same codebase: 18% of all file reads in Claude Code are duplicates, which led to a separate deduplication system that returns a one-line stub for unchanged files, saving 2.6% of fleet-wide token costs.

## Why People Are Using It

Not yet live in production. However, the principle is actionable: custom harnesses and agent pipelines can implement their own version of stale tool call removal. The "keep 5 most recent" heuristic provides a concrete starting point.

## Potential Improvements

Implement a similar strategy in MetaSystem's agent pipelines -- when constructing context for sub-agents, include only recent tool call results rather than full history. The threshold (5) could be tuned per task type.

## Potential Failure Modes

Aggressive tool call removal can lose important context from earlier in the session. The "most recent 5" heuristic may not be optimal for all workflows -- some tasks require referencing older tool outputs. No mechanism to mark specific tool calls as "important" and exempt from removal.
