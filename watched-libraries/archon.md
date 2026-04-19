---
name: "Archon"
type: "watched-library"
repo_url: "https://github.com/coleam00/archon"
description: "Workflow engine for AI coding agents — YAML-defined DAG workflows with git worktree isolation, multi-platform adapters (Slack/Telegram/GitHub/Discord/Web/CLI), and composable AI+deterministic nodes"
spectrum_position: "cherry-pick"
what_we_use: "DAG workflow engine patterns, YAML workflow authoring, git worktree isolation architecture, multi-platform adapter pattern, command/skill/agent context file taxonomy"
local_derivations: []
last_evaluated_version: "v0.3.2"
last_evaluated_date: "2026-04-09"
maintainer: "coleam00 (Cole Medin)"
status: "active"
tags:
  - "orchestration"
  - "workflows"
  - "claude-code"
  - "isolation"
  - "multi-platform"
related_findings: []
related_sources: []
date_added: "2026-04-09"
---

## What It Does

A remote agentic coding platform and workflow engine for AI coding agents. Define development processes as YAML DAG workflows (planning, implementation, validation, code review, PR creation) and run them reliably across projects. Like Dockerfiles for infrastructure or GitHub Actions for CI/CD, Archon aims to make AI coding workflows deterministic and repeatable. Supports Claude Code SDK and Codex SDK as AI backends. Monorepo with 10 packages (cli, core, workflows, git, isolation, paths, adapters, server, web, docs-web). Bun + TypeScript + SQLite/PostgreSQL.

Key capabilities:
- **DAG workflows**: Nodes with `depends_on` edges, topological execution, parallel independent nodes
- **Mixed node types**: AI prompts, bash scripts, TypeScript/Python scripts, command files, loop nodes, approval gates
- **Git worktree isolation**: Every workflow run in its own worktree, parallel execution without conflicts
- **Multi-platform**: Unified conversation interface across Slack, Telegram, GitHub, Discord, Web UI, CLI
- **AI routing**: Orchestrator uses AI to route user messages to workflows or direct responses
- **Variable substitution**: `$nodeId.output` cross-node data flow, `$ARGUMENTS`, `$ARTIFACTS_DIR`, etc.

## What We Use From It

Cherry-pick patterns:
1. **DAG workflow engine design** — YAML-defined nodes with dependency edges, topological layer execution, mixed AI/deterministic nodes
2. **Git worktree isolation architecture** — IsolationResolver 7-step resolution, branded types (RepoPath, BranchName), GitResult discriminated union
3. **Multi-platform adapter pattern** — IPlatformAdapter interface, platform-specific auth, unified conversation model
4. **Context file taxonomy** — Three-tier context (CLAUDE.md global + .claude/rules/ domain + .claude/agents/ specialists + .claude/skills/ capabilities + .archon/commands/ + .archon/workflows/)
5. **Workflow dependency injection** — WorkflowDeps pattern keeping workflow engine decoupled from core

## Spectrum Rationale

**Cherry-pick** — Archon is a full platform (server, web UI, adapters, database) designed for remote agentic coding. MetaSystem doesn't need the platform layer but can learn from its workflow engine architecture, isolation patterns, and context file organization. The DAG execution model and mixed node types are directly relevant to orchestration research.

## Change Signals

Watch for:
- New node types or workflow capabilities
- Changes to the isolation/worktree architecture
- Context file loading strategy changes
- New adapter patterns
- Workflow composability improvements
