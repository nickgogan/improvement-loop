---
name: Atomic Checkout with 409 Exclusion
summary: 'Single-assignee task model enforced by atomic HTTP checkout. POST /checkout with expectedStatuses returns 409 Conflict if another agent owns the task. Hard rule: never retry a 409. Simple HTTP
  status codes as coordination primitives.'
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
- file: database-as-shared-memory-coordination.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Atomic Checkout with 409 Exclusion

## What It Is
Paperclip's single-assignee task model is enforced by atomic checkout: `POST /checkout` with `expectedStatuses`. If another agent already owns the task, the server returns 409 Conflict. The hard rule is "Never retry a 409." This prevents concurrent work on the same task without distributed locking complexity. Simple HTTP status codes serve as coordination primitives — 409 means stop, no ambiguity.

## Why It Matters
Multi-agent coordination is typically complex — distributed locks, message queues, consensus protocols. Atomic checkout reduces the problem to a single HTTP endpoint with idempotent semantics. The "never retry 409" rule eliminates contention loops entirely. Agents that lose the race simply move to the next available task.

## Why People Are Using It
Observed in [Paperclip](https://github.com/paperclipai/paperclip) v2026.403.0 — see [[paperclip-analysis]] for structural details. Elegant coordination primitive. Most multi-agent systems use complex locking, message queues, or consensus protocols. Paperclip uses a single HTTP endpoint with idempotent semantics. 409 = stop, no ambiguity.

## Potential Alternatives
Distributed locks (complex, failure-prone). Message queues with exclusive consumers. Optimistic concurrency with version checks. Central scheduler that pre-assigns tasks (eliminates contention but creates a bottleneck).

## Potential Improvements
Soft reservation with timeout (agent can claim for N minutes, then release). Priority-based checkout where higher-priority agents can preempt. Batch checkout for related tasks that should be done by the same agent.

## Potential Failure Modes
Task starvation if one agent consistently wins checkouts. Abandoned tasks if an agent checks out but crashes before completion (needs timeout/reclaim mechanism). No support for collaborative tasks that benefit from multiple agents working together.
