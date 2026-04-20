---
name: Session as Append-Only Event Log
summary: Externalize agent session state as an append-only event log outside the context window and sandbox. Enables crash-proof recovery via getSession(id)/wake(sessionId)/emitEvent(id, event), flexible
  context slicing via getEvents(), and decoupling of session durability from harness lifecycle.
implementation_notes: MetaSystem uses PROGRESS.md as a coarse session log. An append-only structured event log would enable finer-grained recovery and cross-session context slicing.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-managed-agents-decoupling.md
related_findings:
- file: session-persistence-crash-resilient.md
  rel: extends
- file: immutable-sessions-as-audit-architecture.md
  rel: same-problem
- file: workflow-state-vs-conversation-state.md
  rel: extends
- file: durable-workflow-engine-for-agent-systems.md
  rel: same-problem
- file: brain-hands-decoupling-architecture.md
  rel: enabled-by
- file: system-event-logging-actions-not-words.md
  rel: same-problem
- file: database-as-shared-memory-coordination.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

## What It Is

The session is externalized as an append-only stream of events that lives outside both the context window and the sandbox. Three core APIs: `getSession(id)` fetches the event log, `wake(sessionId)` reboots a new harness instance from the log, and `emitEvent(id, event)` appends events durably during execution. The session log also supports flexible context slicing via `getEvents()` -- selecting positional slices to resume from the last read, rewind for additional context, or reread before a critical action. This goes beyond simple crash recovery: it makes the session a queryable knowledge base that outlives any individual harness or sandbox instance.

## Why It Matters

Prior approaches to session persistence (compaction, memory tools, conversation trimming) make irreversible cuts to history. The append-only event log preserves everything and lets the brain select what to load. Combined with brain-hands decoupling, the harness becomes truly disposable ("cattle, not pets") -- crash, restart, and resume from the log without losing any state.

## Why People Are Using It

Anthropic's production managed agents platform. The pattern enables crash-proof agent sessions that survive harness failures, sandbox crashes, and network interruptions. It also enables session handoff between different harness implementations (e.g., from Claude Code to a custom harness).

## Potential Improvements

Semantic event indexing for intelligent context retrieval rather than positional slicing. Event compression for long-running sessions. Cross-session event linking for multi-agent coordination.

## Potential Failure Modes

Event log growth for very long sessions (needs retention policies). Latency of replaying large event logs on wake. Event schema evolution across harness versions.
