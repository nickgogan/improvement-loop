---
name: "n8n"
type: "watched-library"
repo_url: "https://github.com/n8n-io/n8n"
description: "Open-source workflow automation platform with visual node-based editor, 400+ integrations, AI agent framework (@n8n/agents), and extensive Claude Code context engineering (CLAUDE.md/AGENTS.md chain-loading, plugin system, spec-driven development)"
spectrum_position: "cherry-pick"
what_we_use: "Context file architecture (CLAUDE.md→AGENTS.md chain-loading), plugin namespacing pattern, spec-driven development skill, package-scoped AGENTS.md convention, AI agent SDK design (@n8n/agents), janitor static analysis pattern"
local_derivations: []
last_evaluated_version: "v2.29.10"
last_evaluated_date: "2026-07-13"
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
- Instance-level MCP server evolution (new exposed tools, TypeScript workflow SDK changes)

## Upstream Note: Official Instance-Level MCP Server (2026-07-13)

n8n now ships an **official instance-level MCP server built for coding agents** (Claude Code, Claude Desktop, ChatGPT, custom agents). Enabled per instance via Settings → instance-level MCP (self-hosted or cloud); auth via access token or OAuth2. Exposed capabilities: create new workflows from a description and edit existing ones (n8n 2.13 onward), search/run existing workflows, manage data tables, and test/iterate in-conversation. Existing workflows must be individually opted in before the MCP server can touch them. Replaces the prior community band-aids (Lancowski-style community MCP servers, giant JSON-authoring skill files).

**Transferable pattern — typed-IR compile gate.** The model does not emit workflow JSON directly. It authors the workflow as **TypeScript against an SDK**; that code must **type-check and compile** before being converted to JSON and populated into the instance. The compile step is a hard structural-validity gate between generation and deployment — the model "has to produce something that actually compiles, which filters out a ton of errors" versus raw-JSON guessing with no guards. Generalizes to any pipeline where an LLM authors structured config: route generation through a typed intermediate representation whose compiler is the acceptance gate (same family as our pre-commit frontmatter parse gate, DD-114 — binary parse/compile checks, not heuristic guards).

Sources: wave-3 video Gq0l4IYRIIU (Chase AI, 2026-05-01; transcript in `app/transcript-fetcher/transcripts/`), verified against official docs (`docs.n8n.io/build/ways-of-building-workflows/connect-to-n8n-mcp-server`) for the MCP server, enablement, auth, and exposed tools. The TypeScript compile-gate mechanism is stated by an n8n team member (LinkedIn post quoted in the video); the fetched docs page confirms the server but not the TS internals — treat that detail as maintainer-attributed, not docs-confirmed.

Consumption ruling (link-intake gate 2026-07-13): changelog note only — no source extraction, no finding. Context-engineering patterns we track (CLAUDE.md/AGENTS.md chain-loading, plugins, specs) unaffected by this change.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-09 | v2.16.0 | Initial evaluation — context file architecture, plugin namespacing, spec-driven development, @n8n/agents SDK, janitor. |
| 2026-07-13 | v2.29.10 | /watch-upstream refresh (wave-3 gate follow-up 4). Official instance-level MCP server for coding agents + typed-IR compile gate (TypeScript type-check/compile before JSON conversion/deploy). See Upstream Note. No extraction — changelog note per gate ruling. |
