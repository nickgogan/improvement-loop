---
title: "n8n -- Structural Analysis"
id: "n8n-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
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
  - "n8n"
analyzed_version: "v2.16.0"
analyzed_date: "2026-04-09"
repo_url: "https://github.com/n8n-io/n8n"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# n8n -- Structural Analysis

## Metadata
- **Repo:** https://github.com/n8n-io/n8n
- **Version analyzed:** v2.16.0 (commit dfdc6d2, 2026-04-09)
- **Date:** 2026-04-09
- **Spectrum position:** cherry-pick

---

## 1. Structural Inventory

### File Tree Statistics

| Metric | Value |
|--------|-------|
| Total files | 17,158 |
| Total directories | 4,154 |
| Markdown files | 220 |
| TypeScript files (.ts) | 11,625 |
| Vue files (.vue) | 911 |
| JSON files | 2,773 |
| YAML/YML files | 212 |
| Snapshot files (.snap) | 204 |
| JavaScript files (.js/.mjs) | 214 |
| Python files (.py) | 63 |
| SVG files | 498 |
| SCSS files | 88 |
| MD-to-code ratio | 0.017:1 (220 MD : 12,536 TS/Vue) |
| Max directory depth | 14 |

### Markdown Composition

| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent/LLM context (CLAUDE.md + AGENTS.md) | ~18 | Root, packages/*, .github/ |
| Plugin agents | 2 | `.claude/plugins/n8n/agents/` |
| Plugin skills | 11 | `.claude/plugins/n8n/skills/` |
| Plugin commands | 2 | `.claude/plugins/n8n/commands/` |
| Claude templates | 2 | `.github/claude-templates/` |
| Design system rules | 1 | `.agents/` |
| Community node templates | ~8 | `packages/@n8n/node-cli/src/template/` |
| CI/CD documentation | ~10 | `.github/` |
| Human documentation | ~30 | Root, packages/*/docs/ |
| Package-level docs | ~50 | `packages/*/README.md`, CONTRIBUTING.md |
| Architecture docs (in-package) | ~15 | `packages/@n8n/instance-ai/docs/`, `packages/@n8n/agents/docs/` |
| Other (changelogs, security, etc.) | ~70 | Various |

**Key observation**: MD-to-code ratio of 0.017:1 is the lowest among all watched libraries — this is overwhelmingly a code-first repo with 11,625 TypeScript and 911 Vue files. Markdown serves three distinct purposes: (1) Claude Code context engineering (~35 files), (2) human documentation (~100 files), and (3) package/template scaffolding (~85 files). The context engineering files are high-value despite being a small fraction of total markdown.

### Directory Naming Conventions

- **kebab-case** for packages and directories
- **Scoped packages**: `@n8n/` prefix for internal packages (~44 scoped packages)
- **Convention-based directories**: `.agents/` (root-level style rules), `.claude/plugins/n8n/` (plugin system), `.github/claude-templates/` (task templates)
- **Enterprise suffix**: `.ee` for enterprise-only packages (e.g., `ai-workflow-builder.ee`)

### Top-Level Structure

```
.
├── .agents/                    # Root-level agent rules (design system style)
├── .claude/                    # Claude Code plugin system
│   ├── plugins/n8n/            # n8n-namespaced plugin
│   │   ├── agents/             # 2 specialist agents
│   │   ├── commands/           # 2 slash commands
│   │   └── skills/             # 11 skills (SKILL.md each)
│   └── README.md
├── .github/                    # GitHub CI/CD + Claude templates
│   ├── claude-templates/       # Task-specific templates
│   ├── workflows/              # GitHub Actions
│   ├── actions/                # Reusable actions
│   └── scripts/                # Release automation
├── packages/                   # Monorepo packages
│   ├── @n8n/                   # ~44 scoped internal packages
│   │   ├── agents/             # AI agent SDK (builder pattern)
│   │   ├── ai-workflow-builder.ee/ # AI workflow builder (enterprise)
│   │   ├── db/                 # TypeORM database layer
│   │   ├── instance-ai/        # Deep agent / instance AI
│   │   ├── task-runner/        # Sandboxed code execution
│   │   └── ...                 # 38 more scoped packages
│   ├── cli/                    # Express backend + CLI
│   ├── core/                   # Workflow execution engine
│   ├── frontend/               # Vue 3 frontend (editor-ui, design-system, i18n)
│   ├── nodes-base/             # 400+ built-in integration nodes
│   ├── testing/                # Playwright E2E + janitor
│   ├── workflow/               # Core workflow types
│   └── ...
├── docker/                     # Docker images
├── scripts/                    # Build/release scripts
└── security/                   # Security policies
```

### Notable Structural Patterns

1. **Massive monorepo**: ~44 scoped `@n8n/` packages — one of the largest monorepos analyzed. Each package is independently buildable with isolated config.
2. **Three-namespace context system**: `.agents/` (root rules), `.claude/plugins/n8n/` (Claude Code plugin), and per-package CLAUDE.md/AGENTS.md — three distinct mechanisms for agent context.
3. **Enterprise boundary**: `.ee` suffix packages are clearly separated. Enterprise features are structurally isolated.
4. **Template-as-documentation**: `packages/@n8n/node-cli/src/template/` contains full CLAUDE.md + AGENTS.md + `.agents/` files for community node development — context files shipped as part of the scaffolding template.
5. **Dual frontend structure**: `packages/frontend/` contains `editor-ui/`, `@n8n/design-system/`, and `@n8n/i18n/` — frontend is a sub-monorepo within the monorepo.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Chain-loader | — | One-liner: `@AGENTS.md` — delegates all content to AGENTS.md |
| `AGENTS.md` | LLM | Global | Referenced (from CLAUDE.md) | Constraints/Rules + Workflow/Process | ~230 lines: project overview, commands, architecture, patterns, testing, security |
| `.github/CLAUDE.md` | LLM | Project | Chain-loader | Constraints/Rules | Chain-loads `@../AGENTS.md` + adds .github quick reference (workflow naming, CI structure) |
| `packages/frontend/CLAUDE.md` | LLM | Project | Chain-loader | — | One-liner: `@AGENTS.md` |
| `packages/frontend/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules | CSS variables reference, design system style rules reference |
| `packages/nodes-base/CLAUDE.md` | LLM | Project | Chain-loader | — | One-liner: `@AGENTS.md` |
| `packages/nodes-base/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules | Node development guide: INodeType interface, types, versioning, credentials, testing |
| `packages/@n8n/agents/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules | Agent SDK conventions: builder pattern, package structure, credential pattern |
| `packages/@n8n/db/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules | Database migration DSL, UUID primary key rules |
| `packages/@n8n/ai-workflow-builder.ee/CLAUDE.md` | LLM | Project | Chain-loader | — | One-liner: `@AGENTS.md` |
| `packages/@n8n/ai-workflow-builder.ee/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules + Tool Usage | PromptBuilder utility, Mermaid workflow visualization, evaluation framework |
| `packages/@n8n/instance-ai/CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Instance AI engineering standards, architecture doc refs, streaming protocol, memory tiers |
| `packages/testing/playwright/CLAUDE.md` | LLM | Project | Chain-loader | — | One-liner: `@AGENTS.md` |
| `packages/testing/playwright/AGENTS.md` | LLM | Project | Referenced | Constraints/Rules + Workflow/Process | Playwright commands, janitor tool, TCR workflow, architecture rules |
| `packages/testing/janitor/CLAUDE.md` | LLM | Project | Chain-loader | — | One-liner: `@README.md` |
| `packages/frontend/editor-ui/.../workflowDocument/CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Apply/public method split pattern, CRDT-ready event hooks |
| `.agents/design-system-style-rules.md` | LLM | Global | Referenced | Constraints/Rules | CSS token priority, hard-coded value flagging, legacy token detection |
| `.claude/plugins/n8n/agents/developer.md` | LLM | Task | Injected | Identity/Persona | Full-stack n8n developer agent (frontend + backend + workflow engine) |
| `.claude/plugins/n8n/agents/linear-issue-triager.md` | LLM | Task | Injected | Identity/Persona | Linear issue investigation, severity assessment, handover report |
| `.claude/plugins/n8n/commands/plan.md` | LLM | Task | Injected | Workflow/Process | Plan implementation from Linear ticket via Plan agent |
| `.claude/plugins/n8n/commands/triage.md` | LLM | Task | Injected | Workflow/Process | Triage Linear issue via linear-issue-triager agent |
| `.claude/plugins/n8n/skills/spec-driven-development/SKILL.md` | LLM | Task | Injected | Workflow/Process | Spec ↔ implementation sync loop, `.claude/specs/` as source of truth |
| `.claude/plugins/n8n/skills/reproduce-bug/SKILL.md` | LLM | Task | Injected | Workflow/Process | Bug reproduction framework with test layer routing table |
| `.claude/plugins/n8n/skills/conventions/SKILL.md` | LLM | Task | Injected | Constraints/Rules | Quick reference for critical n8n patterns |
| `.claude/plugins/n8n/skills/content-design/SKILL.md` | LLM | Task | Injected | Constraints/Rules | Content design guidelines |
| `.claude/plugins/n8n/skills/create-pr/SKILL.md` | LLM | Task | Injected | Workflow/Process | PR creation workflow |
| `.claude/plugins/n8n/skills/create-issue/SKILL.md` | LLM | Task | Injected | Workflow/Process | GitHub issue creation |
| `.claude/plugins/n8n/skills/linear-issue/SKILL.md` | LLM | Task | Injected | Workflow/Process | Linear issue management |
| `.claude/plugins/n8n/skills/create-skill/SKILL.md` | LLM | Task | Injected | Workflow/Process | Meta-skill for creating new skills |
| `.claude/plugins/n8n/skills/setup-mcps/SKILL.md` | LLM | Task | Injected | Tool Usage | MCP server setup |
| `.claude/plugins/n8n/skills/loom-transcript/SKILL.md` | LLM | Task | Injected | Tool Usage | Loom video transcript fetching |
| `.claude/plugins/n8n/skills/node-add-oauth/SKILL.md` | LLM | Task | Injected | Workflow/Process | Adding OAuth to nodes |
| `.claude/plugins/n8n/skills/create-community-node-lint-rule/SKILL.md` | LLM | Task | Injected | Workflow/Process | Creating ESLint rules for community nodes |
| `.github/claude-templates/security-fix.md` | LLM | Task | Referenced | Workflow/Process | Security vulnerability fix decision tree and process |
| `.github/claude-templates/e2e-test.md` | LLM | Task | Referenced | Workflow/Process | E2E test writing guide with spec validation checklist |
| `packages/@n8n/node-cli/.../default/CLAUDE.md` | LLM | Global | Chain-loader | — | Template: `@AGENTS.md` — shipped in community node scaffolding |
| `packages/@n8n/node-cli/.../default/AGENTS.md` | LLM | Global | Referenced | Constraints/Rules | Template: community node development guide with detailed patterns |

### Sampling Notes

Read in full: root `CLAUDE.md`, root `AGENTS.md`, `.github/CLAUDE.md`, `frontend/AGENTS.md`, `nodes-base/AGENTS.md`, `@n8n/agents/AGENTS.md`, `@n8n/db/AGENTS.md`, `@n8n/ai-workflow-builder.ee/AGENTS.md`, `@n8n/instance-ai/CLAUDE.md`, `playwright/AGENTS.md`, `workflowDocument/CLAUDE.md`, `.agents/design-system-style-rules.md`, all plugin agents/commands/skills. Chain-loader CLAUDE.md files (one-liners) verified by reading: 6 all contained `@AGENTS.md` or `@../AGENTS.md` or `@README.md`.

### Context Loading Strategy

**Chain-loading with package-scoped distribution:**

n8n uses a distinctive context architecture with three layers:

1. **Chain-loader pattern**: Root `CLAUDE.md` is a single line: `@AGENTS.md`. This causes Claude Code to auto-load CLAUDE.md (which is just a pointer) and then follow the `@` reference to load `AGENTS.md` as the actual content. This pattern repeats at every package level — `packages/frontend/CLAUDE.md` → `@AGENTS.md`, `packages/nodes-base/CLAUDE.md` → `@AGENTS.md`, etc. The benefit: Claude Code only auto-loads files named CLAUDE.md, but the actual content lives in AGENTS.md (which is more descriptive and also supported by GitHub Copilot and other tools).

2. **Package-scoped AGENTS.md**: Each package gets its own `AGENTS.md` with domain-specific conventions. When Claude Code is working in `packages/frontend/`, it loads that package's `AGENTS.md` via its `CLAUDE.md` chain-loader. This distributes context across the monorepo — no single monolithic file needs to contain everything.

3. **Plugin namespace layer**: `.claude/plugins/n8n/` provides the `n8n:` namespace prefix for all skills, commands, and agents. This is a Claude Code plugin feature that enables colon-namespaced items (e.g., `/n8n:create-pr`, `n8n:developer` agent). The plugin contains 2 agents, 2 commands, and 11 skills.

4. **Additional context surfaces**: `.agents/` directory at root (design system style rules), `.github/claude-templates/` (task-specific templates), and deeply nested CLAUDE.md files (e.g., `workflowDocument/CLAUDE.md` for specific store patterns).

**This is the most sophisticated context loading strategy observed across all watched libraries.** The chain-loader indirection (`CLAUDE.md` → `@AGENTS.md`) is a novel pattern that solves the naming constraint (Claude Code auto-loads CLAUDE.md) while keeping content in a more descriptive filename (AGENTS.md) that works across multiple AI tools.

---

## 3. Workflow Topology

n8n is a workflow automation **platform** — its primary purpose is to let users build and execute workflows visually. The "workflow topology" dimension here covers both the platform's internal development workflow and the user-facing workflow execution engine.

### Development Workflow (for contributing to n8n)

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Ticket triage | Linear issue created | Severity + area classified | No (agent-assisted) |
| Planning | `/n8n:plan PAY-XXXX` command | Plan file saved to `.claude/plans/` | Yes (plan review) |
| Spec creation | Non-trivial task identified | Spec in `.claude/specs/` | Yes (spec review) |
| Implementation | Plan approved | Code + tests written | No |
| Validation | Code complete | `pnpm typecheck && pnpm lint && pnpm test` pass | No |
| PR creation | `/n8n:create-pr` | Draft PR created | Yes (PR review) |
| Code review | PR created | Approvals received | Yes |

### User Workflow Execution Engine

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Trigger | Webhook, polling, schedule, or manual | Trigger data available | No |
| Node execution | Previous node output | Node completes or errors | No |
| Error handling | Node throws error | Error workflow triggered or stopped | Configurable |
| Sub-workflow | Execute Workflow node | Sub-workflow completes | No |

### Flow Diagram (ASCII)

```
Development Workflow:

Linear Ticket
    │
    ▼
┌──────────────┐
│ n8n:triage    │  (linear-issue-triager agent)
│ agent         │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ /n8n:plan     │  (Plan agent → .claude/plans/)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Spec-driven   │  (.claude/specs/ ↔ implementation)
│ development   │  Read → Implement → Verify → Update
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ n8n:developer │  (developer agent)
│ agent         │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Validate      │  typecheck + lint + test
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ /n8n:create-pr│  (PR skill)
└──────────────┘
```

### Transition Mechanisms

- **Linear integration**: Tickets trigger triage via `/n8n:triage` command, which uses the `linear-issue-triager` agent to fetch and analyze issues via Linear MCP.
- **Plan files**: `/n8n:plan` saves structured plans to `.claude/plans/` (gitignored). Plans contain ticket context, implementation approach, testing strategy, and risks.
- **Spec-driven loop**: `.claude/specs/` files serve as living architectural decisions. The spec-driven-development skill enforces bidirectional sync between specs and implementation.
- **Validation commands**: `pnpm typecheck`, `pnpm lint`, `pnpm test` as deterministic gates.

### Parallelism

- **Turbo build orchestration**: `pnpm build` uses Turborepo for parallel package building with dependency-aware scheduling.
- **Test parallelism**: Playwright E2E tests run in parallel. Backend tests are per-package.
- **No workflow-level parallelism**: Development workflows are sequential (triage → plan → implement → validate → PR).

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Root AGENTS.md | `AGENTS.md` | Soft (LLM instruction) | "Always use pnpm", "Never use `any` type" |
| Package AGENTS.md | `packages/*/AGENTS.md` | Soft (LLM instruction, path-scoped) | CSS variable reference, node type patterns, migration DSL rules |
| Plugin skills | `.claude/plugins/n8n/skills/conventions/` | Soft (LLM instruction) | Quick reference for critical patterns |
| Design system rules | `.agents/design-system-style-rules.md` | Soft (LLM instruction) | Token priority, legacy token flagging |
| Security fix template | `.github/claude-templates/security-fix.md` | Soft (process guide) | "Never expose attack vector in branch names, commit messages, test descriptions" |
| ESLint config | `packages/@n8n/eslint-config/` | Hard (CI) | Lint rules enforced at build time |
| Biome formatting | Config | Hard (CI) | Formatting enforced |
| TypeScript strict | `tsconfig.json` | Hard (compile) | Strict typing, no `any` |
| lefthook git hooks | `.lefthookrc` | Hard (pre-commit) | Git hooks for pre-commit validation |
| Janitor analysis | `packages/testing/janitor/` | Hard (static analysis) | Architecture rule enforcement for Playwright tests |
| Community node ESLint | `packages/@n8n/eslint-plugin-community-nodes/` | Hard (lint) | Community node compliance rules |

### Guardrail Patterns

1. **Security hygiene as a first-class constraint**: Detailed rules for security fix commits — neutral branch names, commit messages, test descriptions. This prevents attackers from monitoring the public repo for vulnerability signals.
2. **Design system token enforcement**: `.agents/design-system-style-rules.md` provides a severity-graded system: hard-coded values are "strong warning", legacy tokens are "strong warning", deprecated surfaces are "strong warning".
3. **TCR (test-commit-revert) for test maintenance**: The janitor tool uses TCR — changes commit only if tests pass, revert if they fail. This is a code-level guardrail against breaking test infrastructure.
4. **Architecture layering enforcement**: Janitor enforces `Tests → Flows → Page Objects → Components → Playwright API` layering with specific rules (selector-purity, no-page-in-flow, boundary-protection).
5. **Build output redirection**: AGENTS.md explicitly instructs to redirect build output to files (`pnpm build > build.log 2>&1`) — a practical guardrail against overwhelming context windows with build noise.
6. **Linear priority cap**: Instance AI AGENTS.md states "Never set priority to Urgent (1). Use High (2) as the maximum." — a governance constraint on agent-driven triage.

### Permission Model

- **No explicit RBAC for agents**: All Claude Code agents operate with the same permissions. No tool restrictions per agent.
- **Enterprise boundary**: `.ee` packages are structurally separated but not permission-gated in the context system.
- **Plugin namespacing**: `n8n:` prefix prevents collision with personal plugins but doesn't restrict access.
- **Linear MCP integration**: Agents can read/write Linear tickets via MCP tools — no explicit permission boundary on ticket actions.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Developer | `.claude/plugins/n8n/agents/developer.md` | Full-stack n8n development (Vue 3 + Node.js + TypeScript) | Linear MCP, gh CLI, git |
| Linear Issue Triager | `.claude/plugins/n8n/agents/linear-issue-triager.md` | Issue investigation, severity assessment, handover reports | Linear MCP, gh CLI, git |
| Plan Agent | Built-in (via `/n8n:plan` command) | Research and design implementation plans | Saves to `.claude/plans/` |
| Janitor | `packages/testing/janitor/` (tool, not agent) | Static analysis for Playwright test architecture | Direct CLI invocation |

### Handoff Mechanisms

1. **Agent → File → Human**: Triager agent produces a handover report. Plan command saves plans to `.claude/plans/`. These files are consumed by the human developer or the developer agent.
2. **Command → Agent delegation**: `/n8n:triage PAY-XXXX` delegates to the `linear-issue-triager` agent. `/n8n:plan PAY-XXXX` delegates to the built-in Plan agent.
3. **Spec → Implementation sync**: The spec-driven development skill creates a bidirectional loop between `.claude/specs/` files and implementation code. No explicit agent handoff — the same agent/session maintains both.
4. **Linear MCP as shared state**: Both the triager and developer agents read Linear ticket data via MCP tools, creating an implicit shared context layer.

### Shared State

| State | Mechanism | Scope |
|-------|-----------|-------|
| Linear tickets | Linear MCP tools | Cross-agent (read/write) |
| Implementation plans | `.claude/plans/*.md` files (gitignored) | Per-ticket |
| Specs | `.claude/specs/*.md` files | Per-feature |
| Git state | Git CLI | Global |
| GitHub PRs/issues | gh CLI | Global |

### Coordination Patterns

**Sequential handoff with file-based state**:
- Agents coordinate via files (plans, specs) and external services (Linear, GitHub), not via direct inter-agent communication.
- The pattern is: Triager produces analysis → Human reviews → Plan agent produces plan → Human reviews → Developer agent implements → Validation tools check → PR created.
- This is a lightweight sequential pipeline with human gates at each stage, mediated by files and external APIs rather than a workflow engine.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | CLAUDE.md→AGENTS.md chain-loading, package-scoped distribution, plugin namespacing, `.agents/` root rules, `.github/claude-templates/`, deeply nested CLAUDE.md for specific patterns (workflowDocument store) |
| Model | **Low** | `model: inherit` in agent definitions, no model-specific patterns |
| Prompt | **High** | PromptBuilder utility in ai-workflow-builder (section/sectionIf/examples/build), Mermaid workflow visualization for LLM consumption (fewer tokens than JSON), spec-driven development as a prompt management pattern |
| Tools | **Medium** | Linear MCP integration, gh CLI, janitor static analysis tool, TCR workflow |
| Intent | **Medium** | Spec-driven development (specs as intent artifacts), plan files as intent documentation, `/n8n:plan` as structured intent capture |
| Orchestration | **Medium** | Turbo for build orchestration, Playwright janitor for test architecture, but no multi-agent orchestration framework |
| Evaluation | **High** | Evaluation framework in ai-workflow-builder.ee (evaluations/README.md), janitor architecture rules with baseline tracking, TCR as verification mechanism |
| Sandboxing | **High** | `@n8n/task-runner` for sandboxed code execution, `@n8n/task-runner-python` for Python sandboxing, Daytona/local sandbox providers in instance-ai, workspace lifecycle management |
| Governance | **High** | Security fix hygiene rules, design system token enforcement, architecture layering via janitor, Linear priority caps, build output redirection guidance |
| Agent Design | **High** | AGENTS.md as the primary context file (not CLAUDE.md), agent definitions with frontmatter (name, description, model, color), plugin namespacing for organizational clarity, template-shipped context files for community node development |

### Findings Candidates

1. **CLAUDE.md → AGENTS.md chain-loading pattern** (Context Engineering / Agent Design) — n8n's root `CLAUDE.md` is a single line: `@AGENTS.md`. This indirection solves a practical problem: Claude Code auto-loads files named `CLAUDE.md`, but `AGENTS.md` is more descriptive and works across multiple AI tools (GitHub Copilot, etc.). The pattern repeats at every package level, creating a distributed context system where each package's `CLAUDE.md` chain-loads its own `AGENTS.md`. This is a novel approach to naming constraints in multi-tool environments.
→ Skipped: duplicate of [[three-layer-context-chain-loading]] (same pattern, different source) on 2026-04-19

2. **Plugin namespacing for organizational Claude Code context** (Context Engineering) — `.claude/plugins/n8n/` with `n8n:` prefix provides namespaced skills, commands, and agents. This prevents collisions in large teams where multiple developers might have personal Claude Code plugins. The plugin system auto-discovers and namespace-prefixes all items. Known limitation: requires omitting the `name` field from SKILL.md frontmatter due to a Claude Code bug.
→ Promoted to [[plugin-namespacing-for-organizational-context]] on 2026-04-09

3. **Spec-driven development as a skill** (Intent / Governance) — A Claude Code skill that enforces bidirectional sync between `.claude/specs/` files and implementation code. Core loop: read spec → implement → verify alignment → update spec or code. Specs are the source of truth for architectural decisions and API contracts. TODO checkboxes track completion, with strikethrough+annotation for deliberately skipped items. This is intent engineering as a development practice, not just a one-time planning step.
→ Skipped: partial match with [[superpowers-plugin-spec-driven-sub-agent-orchestra]]; single-source on 2026-04-19

4. **Package-scoped AGENTS.md convention** (Context Engineering) — Each monorepo package gets its own `AGENTS.md` with domain-specific conventions. Frontend AGENTS.md has CSS variable references. Nodes-base AGENTS.md has INodeType interface patterns. Database AGENTS.md has migration DSL rules. This distributes context knowledge to where it's needed, avoiding a monolithic context file that contains everything.
→ Skipped: single-source; narrow monorepo-specific convention on 2026-04-19

5. **Janitor static analysis with TCR workflow** (Evaluation / Governance) — A custom AST-based tool for Playwright test architecture enforcement. 7 rules: selector-purity, no-page-in-flow, boundary-protection, scope-lockdown, dead-code, deduplication, duplicate-logic. Uses TCR (test-commit-revert): changes commit only if tests pass, revert if they fail. Includes baseline tracking for incremental cleanup. This is automated evaluation of test code quality, not just functional correctness.
→ Promoted to [[janitor-tcr-test-architecture-enforcement]] on 2026-04-09

6. **Security fix hygiene as explicit governance** (Governance) — Detailed rules for security-related work in a public repository: neutral branch names, commit messages, test descriptions, and code comments. "Never expose the attack vector or vulnerability type in any public-facing artifact." This is a governance pattern specifically designed for open-source projects where attackers monitor repo activity.
→ Promoted to [[security-fix-hygiene-public-repo-governance]] on 2026-04-09

7. **PromptBuilder utility with Mermaid visualization** (Prompt) — `@n8n/ai-workflow-builder.ee` has a `PromptBuilder` class with `section()`, `sectionIf()`, `examples()`, and `build()` methods for composing LLM prompts programmatically. Workflow JSON is converted to Mermaid flowcharts for LLM consumption — more readable and fewer tokens than raw JSON. This bridges visual workflow representation with LLM prompt engineering.
→ Promoted to [[promptbuilder-programmatic-prompt-composition]] on 2026-04-09

8. **CRDT-ready state management pattern** (Agent Design) — The `workflowDocument` store follows a public/apply method split where all mutations go through private `apply*()` methods that write to refs and fire event hooks. This exists to support future CRDT: local actions, remote sync, and undo/redo all converge on the same apply methods. This forward-looking architectural pattern is documented in a deeply nested CLAUDE.md.
→ Promoted to [[crdt-ready-state-management-pattern]] on 2026-04-09

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-09 | v2.16.0 | all | Initial analysis — 17,158 files, ~44 scoped packages, most sophisticated context loading strategy observed, 8 findings candidates |
