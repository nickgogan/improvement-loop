---
title: "Watched Libraries"
id: "watched-libraries-index"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-07"
updated: "2026-04-07"
author: "nick"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "catalog"
  - "upstream-tracking"
  - "moc"
aliases:
  - "Watched Libraries MOC"
  - "Upstream Registry"
---

# Watched Libraries

Registry of external agentic tooling packages that MetaSystem monitors for relevant changes. Each entry tracks what we use, where it sits on the [[upstream-dependency-spectrum]], and what changed since we last looked.

No repo clones — only metadata, snapshots, and change summaries. See the upstream-dependency-spectrum pattern for why.

Structural analyses live in [[watched-library-analyses-index|analysis/]] — produced by `/repo-analyzer`.

## How This Gets Updated

1. **Manual** — Nick or JR adds a new library to watch
2. **`/watch-upstream` skill** (planned) — periodically fetches changelogs/READMEs and produces triage reports
3. **research-loop** — may flag new external projects worth tracking

## Catalog

| Library | Spectrum Position | Last Evaluated | What We Use |
|---------|-------------------|----------------|-------------|
| [[bmad-method\|BMAD Method]] | cherry-pick | v6.2.2 (2026-04-07) | Agent team patterns, docs-as-code, context sharding |
| [[gsd\|GSD]] | wholesale | v1.34.2 (2026-04-07) | Primary build orchestration — spec-driven phases, context management |
| [[superpowers\|Superpowers]] | thin-wrapper | v5.0.7 (2026-04-07) | TDD enforcement, skill auto-activation, subagent orchestration |
| [[openclaw\|OpenClaw]] | cherry-pick | v2026.4.5 (2026-04-07) | SOUL.md constitution pattern, memory file taxonomy |
| [[paperclip\|Paperclip]] | cherry-pick | v2026.403.0 (2026-04-07) | Multi-agent governance — goal ancestry, approval gates, budget tracking |
| [[gstack\|gstack]] | cherry-pick | v0.15.16.0 (2026-04-07) | Role-based specialist tools, Conductor parallel sessions |
| [[mem0\|mem0]] | evaluating | v1.0.11 (2026-04-07) | Memory architecture — auto-extraction, triple storage, scoped memory |
| [[archon\|Archon]] | cherry-pick | v0.3.2 (2026-04-09) | DAG workflow engine, YAML workflows, worktree isolation, multi-platform adapters |
| [[n8n\|n8n]] | cherry-pick | v2.16.0 (2026-04-09) | Context file architecture (CLAUDE.md→AGENTS.md chain-loading), plugin namespacing, spec-driven development |
| [[langgraph\|LangGraph]] | cherry-pick | v1.1.6 (2026-04-09) | Pregel BSP orchestration, typed channels, interrupt/Command primitives, threat model pattern |

## Dataview Query

```dataview
TABLE spectrum_position, last_evaluated_version, last_evaluated_date
FROM "systems/improvement-loop/watched-libraries"
WHERE type = "watched-library"
SORT last_evaluated_date DESC
```
