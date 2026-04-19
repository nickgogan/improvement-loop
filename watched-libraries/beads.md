---
name: "Beads"
type: "watched-library"
repo_url: "https://github.com/gastownhall/beads"
description: "Distributed graph issue tracker for AI agents — Dolt-based SQL with version control, hash-based task IDs for collision-free multi-agent workflows, dependency graph links, and semantic memory decay compaction"
spectrum_position: "cherry-pick"
what_we_use: "Hash-based ID collision avoidance, dependency graph links (relates_to/duplicates/supersedes/replies_to), semantic memory decay compaction, agent-optimized JSON output, CLAUDE.md/AGENTS.md context file patterns"
local_derivations: []
last_evaluated_version: "v1.0.2"
last_evaluated_date: "2026-04-19"
maintainer: "gastownhall"
status: "active"
tags:
  - "task-management"
  - "multi-agent"
  - "memory"
  - "graph"
  - "dolt"
related_findings: []
related_sources: []
date_added: "2026-04-19"
---

## What It Does

A distributed graph issue tracker purpose-built for AI agents, powered by Dolt (a SQL database with Git-like version control and cell-level merge). Uses hash-based task IDs (bd-a1b2) to prevent merge collisions in multi-agent workflows. Supports dependency tracking via graph links (relates_to, duplicates, supersedes, replies_to), hierarchical task organization (epics/subtasks), and semantic "memory decay" compaction that summarizes closed tasks to preserve context while reducing noise. Embedded mode (single-writer) and server mode (multi-concurrent writers). Go primary (94%), with Python/Shell/JS components.

Key capabilities:
- **Hash-based IDs**: Collision-free task creation across distributed agents
- **Graph links**: Typed dependency edges between tasks
- **Memory decay**: Semantic compaction of closed tasks — preserves context, reduces noise
- **Agent-optimized output**: JSON output with auto-ready task detection
- **Dolt branching**: Branch/merge workflows for parallel agent work
- **Role isolation**: Contributor vs maintainer detection and separation

## What We Use From It

Cherry-pick patterns:
1. **Hash-based ID collision avoidance** — pattern for distributed multi-agent task creation without coordination overhead
2. **Typed dependency graph** — relates_to/duplicates/supersedes/replies_to edge types for knowledge relationships
3. **Semantic memory decay** — compaction strategy that summarizes rather than deletes
4. **Agent context files** — CLAUDE.md, AGENTS.md, AGENT_INSTRUCTIONS.md patterns
5. **Dolt as versioned state** — SQL + Git semantics for agent-accessible structured data

## Spectrum Rationale

**Cherry-pick** — MetaSystem doesn't need a Dolt-based issue tracker, but the patterns around collision-free distributed work, typed graph relationships, and semantic memory compaction are directly relevant to multi-agent coordination and memory architecture research.

## Change Signals

Watch for:
- New link types or graph query patterns
- Memory decay algorithm changes
- Multi-writer conflict resolution improvements
- Agent instruction file evolution
