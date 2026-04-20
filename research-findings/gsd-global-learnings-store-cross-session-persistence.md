---
name: GSD Global Learnings Store — Cross-Session Persistence
summary: Persistent CRUD library for cross-session learnings stored outside .planning/, auto-injected into planner context at phase start.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gsd-v1340-v1342-changelog.md
related_findings:
- file: gsd-queryable-codebase-intelligence-store.md
  rel: same-problem
- file: progress-md-session-bridge.md
  rel: extends
- file: four-tier-agent-memory-model-with-write-policy.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: progress-md-session-bridge.md
  rel: extends
- file: four-tier-agent-memory-model-with-write-policy.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
- file: hook-based-transparent-memory-injection.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---

## What It Is

A structured persistence mechanism for cross-session learnings in the GSD framework. Learnings are stored outside `.planning/` so they survive project cleanup and directory resets. The store exposes full CRUD operations via CLI, auto-copies learnings to the global store at phase completion, and automatically injects relevant learnings into planner context before plan generation. This is a *structured* persistence layer — not a freeform memory file or append-only log.

## Why It Matters

Agent sessions lose hard-won context at every boundary — new session, new phase, project cleanup. A structured global store that survives these resets and feeds forward into planning means agents stop re-learning the same lessons. The auto-injection into planner context is the critical design choice: learnings are not just stored, they are *consumed* at the right moment without human intervention.

## Why People Are Using It

Teams working with agentic coding tools hit the same failure modes repeatedly across sessions — wrong library versions, project-specific quirks, deployment constraints. A persistent learnings store converts these repeated failures into durable institutional knowledge. The CRUD interface makes it manageable rather than an ever-growing blob.

## Potential Improvements

The auto-injection mechanism could benefit from relevance filtering — as the store grows, injecting all learnings into every plan becomes a context budget problem. A retrieval layer that matches learnings to the current phase's domain or technology stack would improve signal-to-noise. Learnings could also carry confidence scores that decay over time as the codebase evolves.

## Potential Failure Modes

Stale learnings that no longer apply to the current codebase state could actively mislead the planner. Without expiry or validation mechanisms, the store becomes a source of outdated constraints. The CRUD interface also requires discipline — if learnings are never pruned or updated, the store degrades into noise. Over-reliance on auto-injection could mask the need for fresh analysis when project fundamentals change.
