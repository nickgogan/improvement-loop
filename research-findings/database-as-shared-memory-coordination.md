---
name: Database-as-Shared-Memory Coordination
summary: Multi-agent coordination via a shared versioned database (Dolt) rather than message passing or file-based handoffs. Hash-based IDs prevent collision. Cell-level merge handles concurrent writes.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: file-locking-based-agent-coordination.md
  rel: same-problem
- file: agent-teams-shared-communication-channel.md
  rel: same-problem
- file: atomic-checkout-with-409-exclusion.md
  rel: same-problem
- file: file-based-task-locking-parallel-agents.md
  rel: same-problem
- file: parallel-claude-code-instances-per-workspace.md
  rel: same-problem
- file: session-as-append-only-event-log.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A coordination pattern where multiple agents share state exclusively through a versioned database (Dolt — SQL with Git-like version control), rather than through message queues, event buses, or direct agent-to-agent communication. Agents read and write issue/task state in the database. Hash-based task IDs (e.g., `bd-a1b2`) prevent collision when multiple agents create work concurrently. Dolt's cell-level three-way merge resolves concurrent write conflicts automatically.

## Why It Matters

Most multi-agent coordination patterns rely on either file-based handoffs (MetaSystem's current approach) or message-passing (LangGraph channels, event buses). Database-as-shared-memory offers a third paradigm with distinct advantages: ACID transactions, queryable state, automatic conflict resolution, and version history. It eliminates the need for a coordination framework or custom handoff protocol.

## Why People Are Using It

Observed in [Beads](https://github.com/gastownhall/beads) v1.0.2 — see [[beads-analysis]] for structural details. Beads is a 20.9k-star distributed issue tracker purpose-built for AI agents. The database approach enables concurrent multi-agent workflows where agents create, claim, and close issues without coordination overhead. The `bd dolt push/pull` mechanism acts as the synchronization primitive.

## Potential Alternatives

- File-based handoffs (MetaSystem's current pipeline_status approach)
- Message-passing via LangGraph channels or event systems
- Shared filesystem with file-locking (existing KB finding)

## Potential Improvements

Could be combined with typed channels (LangGraph pattern) for structured data flow, while using the database for persistent state that survives context compaction.

## Potential Failure Modes

- Database becomes a bottleneck under high write concurrency
- Merge conflicts in complex concurrent modifications may require manual resolution
- Agent must understand SQL semantics or use a CLI wrapper (Beads uses `bd` CLI)
