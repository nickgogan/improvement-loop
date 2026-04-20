---
name: Issue-Based Agent Orchestration Replacing Markdown Plan Hierarchies
summary: Persistent, queryable issue graphs replace markdown plan files as the coordination layer for multi-session agent work. Agents file discovered problems as structured issues with dependency links,
  eliminating context-loss-driven work abandonment and plan proliferation.
implementation_notes: The Beads system stores issues as JSONL in git, giving both queryability and version history. Agents use `bd ready --json` to find actionable work without reading a plan file. Four
  dependency link types (parent/child, blocking, discovered-from) enable richer work graphs than GitHub Issues. Drop-in config via single-line agent instruction files.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- steve-yegge-beads-coding-agent-memory.md
related_findings:
- file: incremental-one-feature-per-session-pattern.md
  rel: same-problem
- file: orchestrated-execution-one-task-per-sub-agent-wit.md
  rel: same-problem
- file: phase-task-hierarchical-plan-decomposition.md
  rel: same-problem
- file: cross-session-learnings-jsonl.md
  rel: same-problem
- file: file-based-task-locking-parallel-agents.md
  rel: same-problem
- file: agent-sprawl-anti-pattern-microservices-redux.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---

## What It Is

An agent coordination pattern where work is tracked as structured issues in a persistent, queryable store — not as markdown plan files or task lists in context. The Beads system (Steve Yegge) implements this with JSONL files stored in git: each issue has an ID, status, event log, and typed dependency links (parent/child, blocking, discovered-from). Agents query available work via CLI (`bd ready --json`, `bd ls --assignee agent`), file new discovered problems without human intervention, and update issue state atomically at session end.

The key replacement: instead of an agent reading a 605-file markdown plan hierarchy and losing that context after 10 minutes, it reads a single issue via `bd show <id>`, does one piece of work, updates the issue status, and exits. The issue store maintains the global work graph — the agent only ever holds local context.

## Why It Matters

Markdown plan hierarchies accumulate decay artifacts — partially-completed nested plans, stale status, ambiguous handoff points. Yegge observed 605 plan files in a decade-old project, many partially decayed. The structured issue model prevents this: all state lives in the queryable store, not in agent memory or flat files. Dependency graphs are first-class, so agents can discover ready-work automatically without orchestrator intervention.

The pattern also solves the "dementia problem": agents in 10-minute sessions lose hierarchical context (which epic, which sprint, which task). An issue with explicit `discovered-from` links re-establishes context without requiring the agent to hold a full plan in memory.

## Why People Are Using It

Yegge tested on a decade-old Wyvern project — agents spontaneously switched from markdown plans to issue-centric workflows within 30 minutes of Beads being available. The system filed 128 issues from legacy TODOs in ~30 seconds and generated a 5-sub-epic dependency graph autonomously. With 5+ concurrent agents, each working a single issue, the system produced coherent multi-epic progress without agent-to-agent communication.

## Potential Improvements

- Bidirectional sync with GitHub Issues / Linear for human visibility into agent work queues
- Semantic clustering to identify duplicate issues filed by different agents
- Priority scoring on issues so `bd ready` returns highest-value work, not just unblocked work
- Integration with CI: auto-close issues when their associated tests pass

## Potential Failure Modes

- Issue proliferation: agents file too many fine-grained issues, fragmenting logical units of work
- Dependency cycle deadlock: agents block each other with circular blocking links
- Stale in-progress: agents die mid-session leaving issues in `in_progress` with no timeout/requeue mechanism
- Schema mismatch: concurrent agents on different branches create issues with conflicting schemas; AI-driven merge requires correct prompting to resolve intelligently
