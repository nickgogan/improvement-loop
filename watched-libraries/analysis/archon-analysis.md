---
title: "Archon -- Structural Analysis"
id: "archon-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-09"
updated: "2026-04-09"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "archon"
analyzed_version: "v0.3.2"
analyzed_date: "2026-04-09"
repo_url: "https://github.com/coleam00/archon"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# Archon -- Structural Analysis

## Metadata
- **Repo:** https://github.com/coleam00/archon
- **Version analyzed:** v0.3.2 (commit 95679fa, 2026-04-09)
- **Date:** 2026-04-09
- **Spectrum position:** cherry-pick

---

## 1. Structural Inventory

### File Tree Statistics

| Metric | Value |
|--------|-------|
| Total files | 745 |
| Total directories | 139 |
| Markdown files | 271 |
| TypeScript files (.ts) | 278 |
| TSX files (.tsx) | 70 |
| JSON files | 27 |
| YAML files | 22 |
| SQL files | 22 |
| Shell scripts (.sh) | 9 |
| CSS files | 2 |
| MD-to-code ratio | 0.78:1 (271 MD : 348 TS/TSX) |
| Max directory depth | 8 |

### Markdown Composition

| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions | 16 | `.claude/agents/`, `.github/agents/` |
| Commands/prompts | 51 | `.archon/commands/defaults/`, `.claude/commands/`, `.github/prompts/` |
| Skills (SKILL.md + guides/refs) | ~40 | `.claude/skills/` (archon, archon-dev, playwright-cli, agent-browser, docker-extend, release, remotion-best-practices) |
| Workflow docs/references | 4 | `.claude/docs/` |
| Rules (domain constraints) | 11 | `.claude/rules/` |
| PRPs (issue plans) | 11 | `.claude/PRPs/issues/` |
| Workshop/onboarding | 4 | `.claude/workshop/` |
| Documentation site | ~60 | `packages/docs-web/src/content/docs/` |
| Human docs (README, CONTRIBUTING, etc.) | 6 | root, `.github/` |
| YAML workflows | 21 | `.archon/workflows/defaults/` |
| Dev cookbooks | 10 | `.claude/skills/archon-dev/cookbooks/` |
| Other (CHANGELOG, adapter READMEs) | ~37 | various |

**Key observation**: Markdown is heavily operational — agent definitions, command prompts, skill guides, and workflow documentation are the primary use case. The docs-web package adds ~60 user-facing documentation pages. The MD-to-code ratio of 0.78:1 is close to parity, indicating markdown is a first-class runtime artifact, not just supplementary documentation.

### Directory Naming Conventions

- **kebab-case** throughout (packages, directories, files)
- **Role-based top-level**: `packages/` for code, `.claude/` for Claude Code context, `.archon/` for Archon runtime config, `.github/` for GitHub Copilot/Actions
- **Monorepo workspaces**: `packages/{cli,core,workflows,git,isolation,paths,adapters,server,web,docs-web}`
- **Context namespace separation**: `.claude/` (Claude Code), `.archon/` (Archon platform), `.github/` (GitHub agents/prompts)

### Top-Level Structure

```
.
├── .archon/                    # Archon platform config + defaults
│   ├── commands/defaults/      # 37 default command files
│   └── workflows/defaults/     # 21 default workflow YAMLs
├── .claude/                    # Claude Code context layer
│   ├── PRPs/                   # Issue implementation plans
│   ├── agents/                 # 13 specialist agent definitions
│   ├── commands/               # 15 slash commands
│   ├── docs/                   # 4 architecture docs
│   ├── rules/                  # 11 domain rule files
│   ├── skills/                 # 7 skills (archon, archon-dev, etc.)
│   └── workshop/               # Onboarding guides
├── .github/                    # GitHub integration
│   ├── agents/                 # 3 Copilot agent definitions
│   ├── prompts/                # 14 Copilot prompt files
│   └── workflows/              # CI/CD
├── assets/                     # Logo
├── auth-service/               # Auth service (minimal)
├── deploy/                     # Docker deployment
├── homebrew/                   # Homebrew formula
├── migrations/                 # SQL migration files
├── packages/                   # Monorepo packages (10)
│   ├── adapters/               # Platform adapters (Slack, Telegram, GitHub, Discord)
│   ├── cli/                    # CLI entry point
│   ├── core/                   # Business logic, DB, orchestrator
│   ├── docs-web/               # Documentation website (Starlight)
│   ├── git/                    # Git operations library
│   ├── isolation/              # Worktree isolation
│   ├── paths/                  # Path utilities + logger
│   ├── server/                 # HTTP server (Hono)
│   └── web/                    # React frontend (Vite)
└── scripts/                    # Build/release scripts
```

### Notable Structural Patterns

1. **Triple context namespace**: `.claude/` (Claude Code), `.archon/` (Archon engine), `.github/` (GitHub Copilot) — same agent definitions adapted for three different AI platforms
2. **Commands vs workflows separation**: Commands are single-prompt markdown files; workflows are multi-node YAML DAGs that reference commands
3. **Bundled defaults pattern**: `.archon/commands/defaults/` and `.archon/workflows/defaults/` ship with the repo; user overrides by filename
4. **Package dependency layering**: `paths` (zero deps) → `git` → `isolation` → `workflows` → `core` → `adapters` → `server`. Clean DAG, no cycles.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Constraints/Rules + Workflow/Process | 780-line master context: principles, architecture, commands, patterns, testing, DB schema, API endpoints |
| `.claude/rules/orchestrator.md` | LLM | Project | Auto-loaded | Constraints/Rules | Orchestrator message flow, routing agent arch, session transitions |
| `.claude/rules/workflows.md` | LLM | Project | Auto-loaded | Constraints/Rules | DAG format, variable substitution, WorkflowDeps injection, node types |
| `.claude/rules/isolation.md` | LLM | Project | Auto-loaded | Constraints/Rules | Branded types, IsolationResolver 7-step order, error handling |
| `.claude/rules/adapters.md` | LLM | Project | Auto-loaded | Constraints/Rules | Platform adapter patterns |
| `.claude/rules/cli.md` | LLM | Project | Auto-loaded | Constraints/Rules | CLI conventions |
| `.claude/rules/database.md` | LLM | Project | Auto-loaded | Constraints/Rules | DB operations and schema |
| `.claude/rules/dx-quirks.md` | LLM | Project | Auto-loaded | Constraints/Rules | Known DX issues and workarounds |
| `.claude/rules/isolation-patterns.md` | LLM | Project | Auto-loaded | Constraints/Rules | Isolation patterns |
| `.claude/rules/server-api.md` | LLM | Project | Auto-loaded | Constraints/Rules | Server API conventions |
| `.claude/rules/testing.md` | LLM | Project | Auto-loaded | Constraints/Rules | Testing conventions, mock isolation |
| `.claude/rules/web-frontend.md` | LLM | Project | Auto-loaded | Constraints/Rules | Frontend conventions |
| `.claude/agents/code-reviewer.md` | LLM | Task | Injected | Identity/Persona | Code review specialist, high-confidence only, model: sonnet |
| `.claude/agents/triage-agent.md` | LLM | Task | Injected | Identity/Persona | GitHub issue triage with hook-based label validation |
| `.claude/agents/code-simplifier.md` | LLM | Task | Injected | Identity/Persona | Code simplification specialist |
| `.claude/agents/codebase-analyst.md` | LLM | Task | Injected | Identity/Persona | Implementation analysis, data flow tracing |
| `.claude/agents/codebase-explorer.md` | LLM | Task | Injected | Identity/Persona | Codebase exploration |
| `.claude/agents/comment-analyzer.md` | LLM | Task | Injected | Identity/Persona | Comment quality analysis |
| `.claude/agents/docs-impact.md` | LLM | Task | Injected | Identity/Persona | Documentation impact assessment |
| `.claude/agents/pr-test-analyzer.md` | LLM | Task | Injected | Identity/Persona | PR test coverage analysis |
| `.claude/agents/rulecheck-agent.md` | LLM | Task | Injected | Identity/Persona | CLAUDE.md rule compliance checking |
| `.claude/agents/sdk-verifier.md` | LLM | Task | Injected | Identity/Persona | SDK type verification |
| `.claude/agents/silent-failure-hunter.md` | LLM | Task | Injected | Identity/Persona | Silent failure detection |
| `.claude/agents/type-design-analyzer.md` | LLM | Task | Injected | Identity/Persona | Type system design analysis |
| `.claude/agents/web-researcher.md` | LLM | Task | Injected | Identity/Persona | Web research specialist |
| `.claude/skills/archon/SKILL.md` | LLM | Task | Injected | Workflow/Process | Archon CLI usage — routing table to guides, run/create/setup |
| `.claude/skills/archon-dev/SKILL.md` | LLM | Task | Injected | Workflow/Process | Primary dev workflow — routes to 10 cookbooks by intent |
| `.claude/skills/playwright-cli/SKILL.md` | LLM | Task | Injected | Tool Usage | Playwright testing patterns |
| `.claude/skills/agent-browser/SKILL.md` | LLM | Task | Injected | Tool Usage | Browser automation |
| `.claude/skills/docker-extend/SKILL.md` | LLM | Task | Injected | Tool Usage | Docker extension patterns |
| `.claude/skills/release/SKILL.md` | LLM | Task | Injected | Workflow/Process | Release workflow (semver, changelog) |
| `.claude/docs/architecture-deep-dive.md` | LLM | Global | Referenced | Workflow/Process | End-to-end flow traces with file:line refs (~500 lines) |
| `.claude/docs/adapter-implementation-guide.md` | LLM | Project | Referenced | Workflow/Process | How to build new adapters |
| `.claude/docs/isolation-and-worktree-guide.md` | LLM | Project | Referenced | Workflow/Process | Isolation architecture guide |
| `.claude/docs/workflow-yaml-reference.md` | LLM | Project | Referenced | Workflow/Process | YAML format reference |
| `.github/agents/codebase-analyst.agent.md` | LLM | Task | Injected | Identity/Persona | GitHub Copilot version of codebase analyst |
| `.github/agents/codebase-explorer.agent.md` | LLM | Task | Injected | Identity/Persona | GitHub Copilot version of explorer |
| `.github/agents/web-researcher.agent.md` | LLM | Task | Injected | Identity/Persona | GitHub Copilot version of web researcher |
| `.github/prompts/*.prompt.md` (14 files) | LLM | Task | Injected | Workflow/Process | GitHub Copilot prompt files for common tasks |

### Sampling Notes

Read in full: `CLAUDE.md`, `code-reviewer.md`, `triage-agent.md`, `archon/SKILL.md`, `archon-dev/SKILL.md`, `orchestrator.md`, `workflows.md`, `isolation.md`, `architecture-deep-dive.md`. Classified by pattern: remaining 10 agents (uniform frontmatter + persona + step structure), 14 GitHub prompts (uniform tool list + instruction pattern), 5 remaining skills (SKILL.md + reference structure).

### Context Loading Strategy

**Three-tier layered context with cross-platform mirroring:**

1. **Global layer**: `CLAUDE.md` (780 lines) — auto-loaded, contains full project context including architecture, principles, commands, patterns. This is an unusually large single context file.
2. **Domain rules layer**: `.claude/rules/*.md` (11 files) — auto-loaded by Claude Code when matching `paths:` patterns. Each scoped to a package or concern (orchestrator, workflows, isolation, adapters, etc.).
3. **Specialist layer**: `.claude/agents/*.md` (13 agents) — injected when spawned as subagents. Each has `name`, `description`, `model`, and optionally `tools` and `hooks` frontmatter.
4. **Skill layer**: `.claude/skills/*/SKILL.md` — injected on skill trigger. Skills route to sub-files (cookbooks, guides, references) via intent matching.
5. **Cross-platform mirrors**: `.github/agents/` and `.github/prompts/` provide GitHub Copilot versions of key agents and workflows.

**Notable**: The `archon-dev` skill acts as a **meta-router** — it inspects user intent and dispatches to one of 10 specialized cookbooks, each containing a focused workflow for a specific development task. This is intent-based context loading.

**Also notable**: The triage agent uses `hooks.PostToolUse` to validate label application via a prompt-based hook — enforcement-by-hook pattern.

---

## 3. Workflow Topology

### Phases/Stages

Archon has two workflow layers: the **platform workflow engine** (YAML DAGs executed at runtime) and the **development workflow** (skill-based, for contributing to Archon itself).

#### Platform Workflow Engine (DAG)

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Node resolution | Workflow invocation (CLI/chat/web) | All nodes in topological layer complete | No |
| DAG execution | `executeWorkflow()` | Terminal node(s) complete or failure | No (unless `approval:` node) |
| Loop iteration | `loop:` node with `until:` signal | Completion signal detected or `max_iterations` | Optional (`interactive: true`) |
| Approval gate | `approval:` node | User approves or rejects | **Yes** — mandatory human gate |

#### Default Workflow Library (21 workflows)

| Workflow | Nodes | Pattern | Human Gate? |
|----------|-------|---------|-------------|
| `archon-fix-github-issue` | ~12 | classify → research → implement → review → self-fix → report | No |
| `archon-plan-to-pr` | ~10 | setup → confirm → implement → validate → PR → review → fix → summary | No |
| `archon-idea-to-pr` | ~10 | PRD → plan → implement → validate → review → PR | No |
| `archon-feature-development` | ~8 | plan → implement → validate → review → PR | No |
| `archon-validate-pr` | ~6 | parallel review agents → synthesize → fix → report | No |
| `archon-interactive-prd` | ~4 | research → draft → **approval** → refine | **Yes** |
| `archon-piv-loop` | ~3 | plan → implement+validate loop | No |
| `archon-assist` | 1 | single AI prompt (fallback/default) | No |

### Flow Diagram (ASCII)

```
User Message (CLI/Slack/Telegram/GitHub/Discord/Web)
    │
    ▼
┌─────────────────────┐
│   Platform Adapter   │  (IPlatformAdapter)
│  Slack/TG/GH/Web/CLI│
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Conversation Lock   │  (acquireLock)
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   handleMessage()    │
│   (orchestrator)     │
└─────────┬───────────┘
          │
    ┌─────┴─────┐
    ▼           ▼
┌────────┐ ┌──────────┐
│Determ. │ │ AI Router│
│Commands│ │(10 cmds) │
│(5 cmds)│ └────┬─────┘
└────────┘      │
          ┌─────┴─────┐
          ▼           ▼
    ┌──────────┐ ┌──────────┐
    │ Workflow  │ │ Direct   │
    │ Dispatch  │ │ Response │
    └────┬─────┘ └──────────┘
         │
         ▼
┌─────────────────────┐
│ IsolationResolver    │  (7-step worktree resolution)
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  DAG Executor        │
│  (topological layers)│
│  ┌───┐ ┌───┐ ┌───┐ │
│  │N1 │→│N2 │→│N3 │ │  Parallel within layers
│  └───┘ └───┘ └───┘ │
└─────────────────────┘
```

### Transition Mechanisms

- **AI routing**: The orchestrator uses an AI call with a structured prompt listing available workflows. The AI responds with `/invoke-workflow <name> --project <project> --prompt "..."` which is parsed by `parseOrchestratorCommands()`.
- **DAG edges**: Explicit `depends_on` arrays. Kahn's algorithm builds topological layers. Independent nodes run in parallel via `Promise.allSettled()`.
- **Condition gates**: `when:` expressions on nodes (e.g., `$classify.output.type == 'FEATURE'`). `trigger_rule` controls join semantics (`all_success`, `one_success`, `none_failed_min_one_success`, `all_done`).
- **Loop signals**: `until:` string matched against AI output. `max_iterations` as hard stop.
- **Approval gates**: `approval:` nodes pause execution and wait for human `/workflow approve` or `/workflow reject`.
- **Session transitions**: Immutable sessions linked by `parent_session_id`. Only `plan-to-execute` creates a new session immediately; others deactivate current and create on next message.

### Parallelism

- **Within DAG layers**: Independent nodes in the same topological layer execute concurrently via `Promise.allSettled()`.
- **Across workflows**: Multiple workflows run in parallel via separate git worktrees per workflow run.
- **Within review workflows**: `archon-validate-pr` and `archon-plan-to-pr` run 5+ parallel review agents (code-reviewer, test-coverage, error-handling, comment-quality, docs-impact).
- **Port isolation**: Worktrees get deterministic auto-allocated ports (3190-4089 range) for self-testing.

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| CLAUDE.md principles | `CLAUDE.md` | Soft (LLM instruction) | "Prefer straightforward control flow over clever meta-programming" |
| Engineering principles | `CLAUDE.md` | Soft (LLM instruction) | KISS, YAGNI, DRY+Rule-of-Three, SRP+ISP, Fail Fast, Determinism, Reversibility |
| Domain rules | `.claude/rules/*.md` | Soft (LLM instruction, path-scoped) | "Never run `git clean -fd`", "Always use `execFileAsync`" |
| Git workflow | `CLAUDE.md` | Soft (process) | "Never commit directly to `main`", "`dev` is the working branch" |
| Type safety | `CLAUDE.md` + ESLint | Hard (CI) | Zero-tolerance ESLint warnings, strict TypeScript |
| Hook validation | `.claude/agents/triage-agent.md` | Hard (hook rejects) | PostToolUse hook validates label categories |
| Schema validation | `packages/workflows/src/schemas/` | Hard (Zod runtime) | `dagNodeSchema.safeParse()` for workflow loading |
| Model validation | Workflow loader | Hard (load-time error) | Provider/model compatibility checked at load time |
| CI validation | `bun run validate` | Hard (CI gate) | type-check + lint + format + tests must all pass |

### Guardrail Patterns

1. **Process guardrails**: `dev` branch for all work, `main` for releases only. `/release` skill manages the merge.
2. **Tool restrictions**: Per-node `allowed_tools`/`denied_tools` in workflow YAML (Claude only). Orchestrator routing calls use `tools: []` to prevent tool use.
3. **Isolation by default**: CLI auto-creates worktrees; `--no-worktree` requires explicit opt-in.
4. **Auth boundaries**: Each platform adapter has its own auth check (allowlists from env vars). Silent rejection for unauthorized users.
5. **Env leak gate**: Codebases with sensitive `.env` keys require explicit `--allow-env-keys` consent. Audit-logged.
6. **Conversation locking**: `ConversationLockManager` prevents concurrent message handling on the same conversation.
7. **Immutable sessions**: Sessions are never mutated, only deactivated and replaced, maintaining an audit trail.

### Permission Model

- **Single-developer tool**: No multi-tenant complexity. Auth is allowlist-based per platform.
- **Platform auth**: `TELEGRAM_ALLOWED_USER_IDS`, Slack authorized users, GitHub webhook signature verification.
- **Workflow permissions**: Per-node tool allow/deny lists. Workflow-level `sandbox` option for Claude SDK.
- **No RBAC**: Single user model means no role-based access control.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Orchestrator (routing agent) | `packages/core/src/orchestrator/` | Routes messages to workflows or direct responses via AI | All adapters, workflow engine |
| Code Reviewer | `.claude/agents/code-reviewer.md` | Reviews code against guidelines, 80+ confidence filter | Spawned by review workflows |
| Triage Agent | `.claude/agents/triage-agent.md` | GitHub issue labeling with hook validation | Spawned by triage skill |
| Code Simplifier | `.claude/agents/code-simplifier.md` | Simplifies code changes | Spawned by simplify commands |
| Codebase Analyst | `.claude/agents/codebase-analyst.md` | Traces data flow, maps integrations | Spawned by research/explore tasks |
| Codebase Explorer | `.claude/agents/codebase-explorer.md` | Codebase exploration | Spawned by research tasks |
| Comment Analyzer | `.claude/agents/comment-analyzer.md` | Comment quality analysis | Spawned by review workflows |
| Docs Impact | `.claude/agents/docs-impact.md` | Documentation impact assessment | Spawned by review workflows |
| PR Test Analyzer | `.claude/agents/pr-test-analyzer.md` | Test coverage analysis | Spawned by review workflows |
| Rulecheck Agent | `.claude/agents/rulecheck-agent.md` | CLAUDE.md compliance checking | Spawned by review workflows |
| SDK Verifier | `.claude/agents/sdk-verifier.md` | SDK type verification | Spawned by type tasks |
| Silent Failure Hunter | `.claude/agents/silent-failure-hunter.md` | Silent failure detection | Spawned by error workflows |
| Type Design Analyzer | `.claude/agents/type-design-analyzer.md` | Type system analysis | Spawned by type tasks |
| Web Researcher | `.claude/agents/web-researcher.md` | Web research | Spawned by research workflows |

### Handoff Mechanisms

1. **Workflow DAG**: Primary handoff is via `$nodeId.output` — each node's stdout/AI output is captured and available to downstream nodes via variable substitution.
2. **Orchestrator routing**: AI routing call emits `/invoke-workflow` command, parsed by `parseOrchestratorCommands()`, which dispatches to the workflow engine.
3. **Skill routing**: `archon-dev` SKILL.md acts as a meta-router — inspects user intent keywords and loads the appropriate cookbook file.
4. **Artifacts directory**: `$ARTIFACTS_DIR` provides a shared filesystem location per workflow run for cross-node data persistence.
5. **Database state**: Workflow runs, events, and session state stored in SQLite/PostgreSQL. Session resume via `session.assistant_session_id`.

### Shared State

| State | Mechanism | Scope |
|-------|-----------|-------|
| Node outputs | `$nodeId.output` variable substitution | Within a workflow run |
| Artifacts | `$ARTIFACTS_DIR` filesystem | Within a workflow run |
| Workflow events | `workflow_events` DB table | Persistent |
| Session state | `sessions` DB table | Per conversation |
| Conversation context | `conversations` + `messages` DB tables | Per conversation |
| Codebase metadata | `codebases` DB table | Global |

### Coordination Patterns

**Hub-and-spoke with DAG execution**:
- The **orchestrator** is the hub — all messages flow through it, it routes to workflows.
- The **workflow engine** executes DAGs with parallel layers — independent nodes run concurrently.
- **Agents** are stateless specialists spawned as Claude Code subagents within workflow nodes.
- **No peer-to-peer**: Agents don't communicate directly; all coordination flows through the DAG's `depends_on` edges and `$nodeId.output` variables.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Three-tier layered context (CLAUDE.md → rules → agents), path-scoped rule auto-loading, intent-based skill routing, `archon-dev` meta-router, `fresh_context` per loop iteration |
| Model | **Medium** | Multi-provider support (Claude + Codex), per-node model overrides, model validation at load time, `inherit` model option |
| Prompt | **Medium** | Structured command prompts as markdown files, variable substitution system, `output_format` for JSON schema enforcement |
| Tools | **High** | Per-node `allowed_tools`/`denied_tools` restrictions, `tools: []` for routing calls, per-node MCP server config, per-node skill preloading |
| Intent | **High** | AI routing agent (intent→workflow dispatch), intent-based skill routing (`archon-dev` keyword matching), approval gates as human intent checkpoints |
| Orchestration | **High** | DAG workflow engine with topological layer execution, mixed AI+deterministic nodes, parallel independent nodes, loop nodes with completion signals, workflow resume from failure, cross-workflow isolation via worktrees |
| Evaluation | **High** | Multi-agent parallel review (5+ agents), hook-based validation (triage agent PostToolUse), CI validation gate (`bun run validate`), workflow-level self-fix loops |
| Sandboxing | **High** | Git worktree isolation per workflow run, IsolationResolver 7-step resolution, branded types for path safety, auto-allocated ports, `sandbox` option for Claude SDK |
| Governance | **Medium** | Engineering principles as soft constraints, tool restrictions per node, auth allowlists, env leak gate with audit logging, immutable session audit trail |
| Agent Design | **High** | 13 specialist agents with frontmatter schema (name, description, model, tools, hooks), cross-platform mirroring (.claude/agents → .github/agents), cookbook-based routing |

### Findings Candidates

1. **DAG workflow engine with mixed node types** (Orchestration) — Archon's DAG executor supports AI prompts, bash scripts, TypeScript/Python scripts, commands, loops, and approval gates as first-class node types within the same workflow. Topological layer execution enables natural parallelism. The `$nodeId.output` variable substitution provides structured data flow between nodes. This is a concrete, production implementation of composable AI+deterministic workflow authoring.
→ Skipped: duplicate of [[durable-workflow-engine-for-agent-systems]] and [[dag-vs-bsp-two-graph-based-orchestration-models]] on 2026-04-19

2. **IsolationResolver 7-step worktree resolution** (Sandboxing) — A concrete algorithm for worktree lifecycle management: existing env → no codebase skip → workflow reuse → linked issue sharing → PR branch adoption → limit check + auto-cleanup → create new. Includes orphan cleanup if DB write fails after worktree creation. Branded types (RepoPath, BranchName, WorktreePath) prevent string-type confusion.
→ Promoted to [[isolation-resolver-worktree-lifecycle-algorithm]] on 2026-04-09

3. **Intent-based meta-routing skill** (Intent / Agent Design) — The `archon-dev` skill acts as a meta-router: it inspects user input keywords and dispatches to one of 10 specialized cookbooks. This is intent classification implemented as a routing table in markdown, not code. Each cookbook is a self-contained workflow for a specific development task (research, plan, implement, review, debug, etc.).
→ Promoted to [[intent-based-meta-routing-skill]] on 2026-04-09

4. **Hook-based enforcement for agent outputs** (Evaluation / Governance) — The triage agent uses `hooks.PostToolUse` with a prompt-based hook that validates whether label application commands include exactly one type, effort, priority label plus area labels. This is enforcement-by-hook — the hook runs after every Bash tool call and can reject invalid operations.
→ Promoted to [[hook-based-enforcement-for-agent-outputs]] on 2026-04-09

5. **Triple context namespace for cross-platform agents** (Agent Design / Context Engineering) — Archon maintains parallel agent definitions in `.claude/agents/`, `.github/agents/`, and `.github/prompts/` — same specialists adapted for Claude Code, GitHub Copilot agents, and GitHub Copilot prompts respectively. This is a concrete pattern for cross-platform agent portability.
→ Skipped: partial match with [[multi-ide-portability-via-installer-templates]]; single-source on 2026-04-19

6. **Per-node tool restrictions in YAML workflows** (Tools / Governance) — Workflow nodes can specify `allowed_tools` or `denied_tools` arrays, giving fine-grained tool access control per workflow step. The orchestrator's routing calls use `tools: []` to prevent tool use entirely during classification. This is tool-level sandboxing within a workflow.
→ Skipped: implementation-specific to Archon YAML workflows; not generalizable on 2026-04-19

7. **Workflow dependency injection (WorkflowDeps)** (Orchestration) — The `@archon/workflows` package has zero dependency on `@archon/core`. Everything (DB, AI client, config) is injected via the `WorkflowDeps` interface. This enables testing the workflow engine in isolation and potentially running it outside the Archon platform.
→ Skipped: standard dependency injection pattern, not agent-specific on 2026-04-19

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-09 | v0.3.2 | all | Initial analysis — 745 files, 10-package monorepo, DAG workflow engine, 21 default workflows, 13 agents |
