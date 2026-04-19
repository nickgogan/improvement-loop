---
name: "n8n"
type: "watched-library"
repo_url: "https://github.com/n8n-io/n8n"
description: "Open-source workflow automation platform with visual node-based editor, 400+ integrations, AI agent framework (@n8n/agents), and extensive Claude Code context engineering (CLAUDE.md/AGENTS.md chain-loading, plugin system, spec-driven development)"
spectrum_position: "cherry-pick"
what_we_use: "Context file architecture (CLAUDE.md→AGENTS.md chain-loading), plugin namespacing pattern, spec-driven development skill, package-scoped AGENTS.md convention, AI agent SDK design (@n8n/agents), janitor static analysis pattern"
local_derivations: []
last_evaluated_version: "v2.16.0"
last_evaluated_date: "2026-04-09"
maintainer: "n8n-io"
status: "active"
tags:
  - "workflow-automation"
  - "context-engineering"
  - "claude-code"
  - "agent-sdk"
  - "monorepo"
related_findings: []
related_sources: []
date_added: "2026-04-09"
---

## What It Does

Open-source workflow automation platform. Visual node-based editor for connecting 400+ services, AI agent capabilities via @n8n/agents SDK, and a Vue 3 + Node.js/Express monorepo with ~44 packages under `packages/@n8n/`. Key capabilities: visual workflow builder, webhook/polling triggers, LangChain AI nodes, multi-database support (SQLite/PostgreSQL), CRDT-ready state management, enterprise features (.ee packages), and a full agent SDK with builder pattern, guardrails, memory, and evaluations.

From the MetaSystem perspective, n8n is most interesting for its **Claude Code context engineering** — one of the most sophisticated context file architectures observed across all watched libraries.

## What We Use From It

Cherry-pick patterns:
1. **CLAUDE.md → AGENTS.md chain-loading** — Root `CLAUDE.md` is a one-liner `@AGENTS.md`, making AGENTS.md the true context file. Package-level CLAUDE.md files chain-load with `@AGENTS.md` or `@../AGENTS.md`. Separates "what Claude loads automatically" from "where the content lives."
2. **Package-scoped AGENTS.md** — Each package gets its own AGENTS.md with domain-specific conventions (frontend CSS variables, node development patterns, database migration DSL, AI workflow builder prompts). Context is distributed, not monolithic.
3. **Plugin namespacing** — `.claude/plugins/n8n/` with `n8n:` prefix for skills, commands, agents. Avoids collisions with personal or third-party plugins.
4. **Spec-driven development skill** — `.claude/specs/` as source of truth for architectural decisions. Core loop: read spec → implement → verify alignment → update spec or code.
5. **Janitor static analysis** — Custom AST-based tool for Playwright test architecture enforcement (selector purity, layered architecture, dead code, deduplication). TCR (test-commit-revert) workflow for safe fixes.
6. **@n8n/agents SDK design** — Builder pattern with lazy build, Zod schemas, tool/guardrail/memory/eval primitives, sub-agent coordination.

## Spectrum Rationale

**Cherry-pick** — n8n is a full workflow automation platform, not an agentic coding tool. The platform itself is not relevant to MetaSystem. However, its context engineering approach (chain-loading, package-scoped AGENTS.md, plugin namespacing, spec-driven development) and its agent SDK design are highly relevant patterns for how large TypeScript monorepos structure AI agent context.

## Change Signals

Watch for:
- Changes to CLAUDE.md/AGENTS.md context loading patterns
- New plugin system capabilities
- @n8n/agents SDK architecture changes
- New skills or commands in .claude/plugins/n8n/
- Instance AI (deep agent) architecture evolution
- CRDT implementation in workflowDocument store
