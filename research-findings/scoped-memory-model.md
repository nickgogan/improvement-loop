---
name: Scoped Memory Model
summary: mem0 scopes all memories by three composable dimensions — user_id, agent_id, and run_id — enabling intersection queries (e.g., user + agent = personalized agent memory). All CRUD operations filter
  by scope. No cross-scope access without explicit filtering.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- mem0-analysis.md
related_findings:
- file: memory-bank-isolation-per-agent-per-project.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
## What It Is

mem0 scopes all memories by three dimensions:

- **user_id** — per-user preferences, history, and context
- **agent_id** — per-agent learned patterns and behaviors
- **run_id** — per-session ephemeral context

Scopes are composable. A query with `user_id + agent_id` retrieves memories for a specific user interacting with a specific agent — personalized agent memory. A query with only `agent_id` retrieves all memories that agent has accumulated across all users. All CRUD operations (add, search, get, update, delete) filter by scope. There is no cross-scope access without explicitly omitting or combining scope filters.

## Why It Matters

Memory isolation is a security and correctness requirement. User A's memories should not leak into User B's context. Agent-level learnings (e.g., "this codebase uses tabs not spaces") should persist across sessions but not across projects. Session context should be available during a run but not pollute long-term memory.

The three-dimension model is minimal but covers the key isolation boundaries. The composability is the key design insight — rather than creating separate storage for each combination, a single store with filterable dimensions handles all cases.

## Why People Are Using It

Observed in [mem0](https://github.com/mem0ai/mem0) v1.0.11 — see [[mem0-analysis]] for structural details.

This scoping model maps naturally to MetaSystem's memory types: `user_id` maps to user memories, `agent_id` maps to project memories, `run_id` maps to session context. The approach is simpler than OpenClaw's workspace isolation or Paperclip's company-scoped hierarchy while remaining flexible enough for multi-tenant scenarios.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Workspace-level isolation (OpenClaw) | Separate memory stores per workspace | When hard isolation is required and cross-workspace queries are never needed |
| Company-scoped hierarchy (Paperclip) | Company → team → user hierarchy | For enterprise multi-tenant deployments with organizational structure |
| Flat memory with tags | Single store with freeform tags for filtering | When scope dimensions are unpredictable or frequently changing |
| Directory-based isolation | Separate file directories per scope | For file-based memory systems without a database |

## Potential Improvements

- Evaluate whether a fourth dimension (e.g., `project_id` or `team_id`) is needed for MetaSystem's multi-system architecture
- Assess how scope composition handles the "shared memory" case — memories that should be accessible across all users of an agent
- Investigate whether scope enforcement happens at the API layer, storage layer, or both

## Potential Failure Modes

- **Scope misconfiguration**: Omitting a scope filter accidentally returns cross-scope results — a silent correctness bug
- **Scope explosion**: Combinatorial growth of user x agent x run creates many sparse scope partitions
- **No hierarchical scoping**: The flat three-dimension model doesn't naturally support "team memories visible to all team members"
- **Run_id lifecycle management**: Who decides when a run ends? Orphaned run-scoped memories accumulate without cleanup
- **Cross-scope insights lost**: Patterns visible across scopes (e.g., "all users struggle with X") require explicit aggregation queries
