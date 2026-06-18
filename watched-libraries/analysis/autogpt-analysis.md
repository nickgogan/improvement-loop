---
title: "AutoGPT -- Structural Analysis"
id: "autogpt-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-05-25"
updated: "2026-05-25"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "autogpt"
analyzed_version: "v0.5.0"
analyzed_date: "2026-05-25"
repo_url: "https://github.com/significant-gravitas/autogpt"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
spectrum_position: "cherry-pick"
---

# AutoGPT -- Structural Analysis

## Executive Summary

AutoGPT is a large-scale monorepo (~3,941 files) containing two distinct generations of an AI agent platform. The **modern platform** (`autogpt_platform/`) is a full-stack SaaS product with visual block-based workflow composition, a CoPilot chat-driven agent builder, and a marketplace. The **classic system** (`classic/`) is a legacy autonomous GPT-4 agent preserved for historical reference.

The repository demonstrates sophisticated multi-layer context engineering for coding agents: hierarchical CLAUDE.md + AGENTS.md files, an orchestration skill that manages fleets of Claude Code agents via tmux, and a production-grade block-based execution engine with human-in-the-loop gates, content moderation (AutoMod), and permission sandboxing.

---

## 1. Structural Inventory

### File Statistics

| Metric | Count |
|--------|-------|
| Total files | 3,941 |
| Python files (`.py`) | 1,285 |
| TypeScript/TSX files | 1,604 |
| Markdown files (`.md`) | 347 |
| JSON files (non-git, non-node_modules) | 69 |
| YAML/YML files | 50 |
| Block implementation files (`backend/blocks/`) | 339 |
| GitHub Actions workflow files | 37 |

### Top-Level Directory Tree

```
autogpt/
├── .agents/                    # Symlink to .claude/skills
├── .claude/                    # Claude Code configuration
│   ├── settings.json           # Minimal permission allowlist
│   └── skills/                 # 10 skill directories
├── .github/                    # CI/CD, templates, CODEOWNERS
├── autogpt_platform/           # Modern platform (Polyform Shield License)
│   ├── backend/                # Python FastAPI service
│   ├── frontend/               # Next.js 15 application
│   ├── autogpt_libs/           # Shared Python libraries
│   ├── db/                     # Docker-based PostgreSQL setup
│   ├── graph_templates/        # Pre-built agent workflow templates (JSON)
│   └── installer/              # One-line setup scripts
├── classic/                    # Legacy AutoGPT (MIT License, unsupported)
│   ├── forge/                  # Core agent framework
│   ├── original_autogpt/       # Original autonomous agent
│   ├── direct_benchmark/       # Benchmark harness
│   └── reports/                # Benchmark reports
├── docs/                       # Documentation site content
│   ├── content/                # MkDocs content (challenges, guides)
│   ├── home/                   # GitBook home site
│   ├── integrations/           # Block integration docs
│   └── platform/               # Platform guides (getting started, blocks)
├── assets/                     # Brand assets
├── AGENTS.md                   # Root contribution guide for coding agents
├── CLAUDE.md                   # Root pointer (@AGENTS.md)
├── README.md                   # Project overview
├── SECURITY.md                 # Security policy
├── CONTRIBUTING.md             # Contributor guide
└── CODE_OF_CONDUCT.md          # Code of conduct
```

### Naming Conventions

- **Python**: snake_case files and directories; `_base.py`, `_utils.py` for internal modules
- **TypeScript/React**: PascalCase for components, camelCase for hooks (`useComponentName.ts`)
- **Blocks**: Each integration gets a directory (`blocks/discord/`, `blocks/github/`) or a file (`blocks/llm.py`)
- **Tests**: Co-located `*_test.py` (backend) and `__tests__/` directories (frontend)
- **Context files**: `CLAUDE.md` and `AGENTS.md` at multiple hierarchy levels
- **Skills**: `.claude/skills/<name>/SKILL.md` with YAML frontmatter

### Markdown Composition

Of 347 markdown files:
- ~21 are CLAUDE.md or AGENTS.md context files (hierarchical coding agent instructions)
- ~50+ are platform documentation pages (block guides, integration docs)
- ~30+ are challenge/benchmark definitions
- ~40+ are integration block documentation with MANUAL sections
- The rest are standard project docs (README, CONTRIBUTING, templates, changelogs)

---

## 2. Context File Map

### CLAUDE.md Hierarchy (Claude Code Agent Context)

| Path | Scope | Mechanism | Content |
|------|-------|-----------|---------|
| `/CLAUDE.md` | Root | Pointer (`@AGENTS.md`) | Redirects to AGENTS.md |
| `/AGENTS.md` | Root | Direct content | Full contribution guide: directory overview, code style, frontend guidelines, testing, conventional commits, PR process |
| `/autogpt_platform/CLAUDE.md` | Platform scope | Pointer (`@AGENTS.md`) | Redirects to platform AGENTS.md |
| `/autogpt_platform/AGENTS.md` | Platform scope | Direct content | Key concepts (Agent Graphs, Blocks, Store), env config, branching strategy (`dev` base), conventional commits, TDD workflow, PR review with `/pr-review` and `/pr-address` |
| `/autogpt_platform/backend/CLAUDE.md` | Backend | Pointer (`@AGENTS.md`) | Redirects to backend AGENTS.md |
| `/autogpt_platform/backend/AGENTS.md` | Backend | Direct content | Essential commands, architecture, code style rules (30+ specific conventions), testing approach, database schema, Block SDK guide, workspace/media architecture, security middleware |
| `/autogpt_platform/frontend/CLAUDE.md` | Frontend | Pointer (`@AGENTS.md`) | Redirects to frontend AGENTS.md |
| `/autogpt_platform/frontend/AGENTS.md` | Frontend | Direct content | Commands, pre-completion checks (MANDATORY), code style, architecture (Next.js 15), data fetching patterns, feature development, naming conventions |
| `/autogpt_platform/frontend/src/tests/CLAUDE.md` | Frontend tests | Pointer | Testing-specific context |
| `/autogpt_platform/frontend/src/tests/AGENTS.md` | Frontend tests | Direct content | Detailed MSW patterns, decision flowchart |
| `/autogpt_platform/backend/backend/copilot/bot/CLAUDE.md` | CoPilot bot | Pointer (`@README.md`) | Bot architecture, adding adapters |
| `/autogpt_platform/backend/backend/copilot/graphiti/CLAUDE.md` | Graphiti | Direct content | Memory system context |
| `/classic/CLAUDE.md` | Classic | Direct content | Full architecture guide for legacy system: workspace structure, permissions model (pattern matching, first-match-wins), layered settings |
| `/classic/direct_benchmark/CLAUDE.md` | Benchmark | Direct content | Benchmark-specific context |
| `/classic/forge/CLAUDE.md` | Forge | Direct content | Forge framework context |
| `/classic/original_autogpt/CLAUDE.md` | Original agent | Direct content | Original agent context |
| `/docs/CLAUDE.md` | Documentation | Pointer (`@AGENTS.md`) | Doc writing guidelines |
| `/docs/AGENTS.md` | Documentation | Direct content | Block documentation MANUAL section patterns, style guidelines |

### Other Coding Agent Context Files

| Path | Target Agent | Purpose |
|------|--------------|---------|
| `/.github/copilot-instructions.md` | GitHub Copilot | Full onboarding: repo overview, build commands, architecture, security, CI alignment |
| `/.claude/settings.json` | Claude Code | Minimal permission allowlist (Read, Grep, Glob, limited Bash, git, tmux, branchlet) |
| `/.branchlet.json` | Branchlet tool | Worktree copy patterns, post-create commands |
| `/.vscode/all-projects.code-workspace` | VS Code | Multi-root workspace config |
| `/.pre-commit-config.yaml` | Pre-commit | Secret detection, Poetry install hooks |

### Key Pattern: `@` Pointer Delegation

The majority of CLAUDE.md files contain only `@AGENTS.md` (a pointer directive), which instructs Claude Code to load the sibling AGENTS.md file instead. This creates a two-file system:
- **CLAUDE.md** = entry point that Claude Code auto-discovers per its directory hierarchy rules
- **AGENTS.md** = the actual content, also readable by other AI coding agents (GitHub Copilot, Cursor)

This is a **dual-audience context pattern** -- single source of truth, two discovery mechanisms.

---

## 3. Workflow Topology

### Platform Execution Engine (Graph-Based)

The modern platform uses a **directed graph execution model**:

```
User defines graph (visual builder) → AgentGraph (JSON) stored in DB
                                       ↓
Trigger event (webhook, schedule, manual, CoPilot)
                                       ↓
ExecutionManager (RabbitMQ consumer)
  → Validates permissions & billing
  → AutoMod content moderation (if enabled)
  → Topologically sorts nodes
  → Executes blocks sequentially/parallel per graph links
                                       ↓
Each Node → Block.run(inputs, execution_context)
  → Yields outputs → Propagated via Links to downstream nodes
                                       ↓
Graph execution complete → Store results → Notify user
```

### Block Types (Execution Primitives)

| BlockType | Purpose |
|-----------|---------|
| `STANDARD` | General-purpose blocks |
| `INPUT` / `OUTPUT` | Graph I/O boundaries |
| `WEBHOOK` / `WEBHOOK_MANUAL` | External trigger entry points |
| `AGENT` | Sub-agent invocation (recursive graph execution) |
| `AI` | LLM-powered blocks |
| `HUMAN_IN_THE_LOOP` | Pauses for human approval/rejection |
| `MCP_TOOL` | Model Context Protocol tool blocks |
| `NOTE` | Documentation-only (no execution) |

### Block Categories

AI, Social, Text, Search, Basic, Input, Output, Logic, Communication, Developer Tools, Data, Hardware, Agent, CRM, Safety, Productivity, Issue Tracking, Multimedia, Marketing.

### Human Gates

1. **HumanInTheLoopBlock** -- Pauses execution, presents data to reviewer, routes to `approved_data` or `rejected_data` output pins. Supports editable data before approval.
2. **AutoMod** -- Pre-execution content moderation via external API. Feature-flagged per user. Fail-open configurable.
3. **CoPilot Permissions** -- Tool and block allow/deny filtering with recursive inheritance (children can only be more restrictive).

### CoPilot Agent (Conversational Builder)

The CoPilot is a separate agentic subsystem that lets users build/modify agents through chat:

```
User message → CoPilot Service
  → Model router (selects provider/model)
  → Prompting system (builder context, tool definitions)
  → Tool call loop (built-in or extended thinking mode)
  → Tools: create_agent, edit_agent, run_agent, run_block, 
            agent_generator, web_search, bash_exec, sandbox, etc.
  → Graphiti memory (knowledge graph for long-term memory)
  → Stream back to user (SSE with heartbeats)
```

The `OrchestratorBlock` implements the actual tool-call loop with two execution modes:
- **BUILT_IN**: Default tool-call loop supporting all LLM providers
- **EXTENDED_THINKING**: Delegates to Claude Agent SDK for richer reasoning

### Classic AutoGPT Execution Loop (Legacy)

```
User goal → Agent (prompt strategies) → LLM → Actions
  → Permission check (workspace/agent allow/deny lists)
  → Action execution (file I/O, web search, code execution)
  → Result → Memory → Next cycle
```

The classic system has a sophisticated **layered permission model**:
1. Agent deny list → Block
2. Workspace deny list → Block
3. Agent allow list → Allow
4. Workspace allow list → Allow
5. Session denied list → Block
6. Prompt user → Interactive approval

### Development Workflow (Claude Code Skills)

The repo has a complete CI/CD workflow for AI coding agents:

```
/setup-repo → /worktree → [development] → /open-pr → /pr-review → /pr-address → /pr-polish
                                                                                      ↕
                                                               /orchestrate (fleet management)
```

---

## 4. Governance Model

### Constraint Files

| File/Mechanism | Scope | Purpose |
|----------------|-------|---------|
| `.claude/settings.json` | Claude Code | Minimal permission allowlist (read-only + git + tmux) |
| `.pre-commit-config.yaml` | All contributors | Secret detection (detect-secrets + gitleaks), dependency checks |
| `.gitleaks.toml` | Pre-commit | Gitleaks configuration for secret scanning |
| `.secrets.baseline` | Pre-commit | Known secrets baseline to avoid false positives |
| `.github/CODEOWNERS` | GitHub | Team-based ownership (maintainers, devops, forge-maintainers, etc.) |
| `SECURITY.md` | Project | Responsible disclosure, 90-day fix window, supported versions |
| `LICENSE` (MIT + Polyform Shield) | Legal | Classic=MIT, Platform=proprietary Polyform Shield |
| `.pr_agent.toml` | PR Agent | PR review bot configuration |
| `.deepsource.toml` | DeepSource | Static analysis configuration |

### Permission and Security Model (Platform)

1. **CoPilot Permissions** (`copilot/permissions.py`):
   - Tool-level allow/deny with blacklist (default) or whitelist mode
   - Block-level allow/deny by UUID, partial UUID, or name
   - Recursive inheritance -- children can never exceed parent permissions
   - `DISABLED_LEGACY_TOOL_NAMES` for deprecated tool removal

2. **Security Hooks** (`copilot/sdk/security_hooks.py`):
   - Pre-execution validation of tool calls
   - Multi-user isolation enforcement
   - Workspace scoping for file access
   - Dangerous pattern detection
   - BiDi/zero-width character sanitization (anti-injection)
   - Sub-agent detection and control

3. **Cache Protection Middleware** (`api/middleware/security.py`):
   - Default no-cache for all endpoints
   - Allow-list for cacheable paths (static assets, health checks)
   - Prevents sensitive data caching in browsers/proxies

4. **AutoMod** (`executor/automod/`):
   - Content moderation before graph execution
   - External API integration with configurable timeout, retries, and fail-open behavior
   - Feature-flagged per user

### Branching and Release Strategy

- `dev` = main development branch (all PRs target here)
- `master` = production branch (releases only)
- Conventional commits enforced via PR titles
- CODEOWNERS for team-based review requirements

### CI/CD Governance

37 GitHub Actions workflows covering:
- Backend CI (Python 3.11-3.13, Prisma, Redis, RabbitMQ, ClamAV)
- Frontend CI (Node.js 21, pnpm, Playwright)
- Full-stack integration tests
- Claude Code integration (responds to `@claude` mentions)
- Claude CI failure auto-fix workflow
- Copilot setup steps
- PR overlap detection
- Base branch enforcement
- Stale issue closing
- Dependabot auto-merge via Claude

---

## 5. Cross-Agent Protocol

### Development Agent Fleet (Claude Code Orchestrator)

The `/orchestrate` skill implements a **meta-agent supervisor** that manages parallel Claude Code instances:

**Architecture:**
```
Orchestrating Claude (supervisor — this conversation)
  └── run-loop.sh (mechanical babysitter in tmux window)
        ├── Agent 1 (tmux window + worktree + Claude Code session)
        ├── Agent 2 (tmux window + worktree + Claude Code session)
        └── Agent N (tmux window + worktree + Claude Code session)
```

**State Management:**
- `~/.claude/orchestrator-state.json` -- JSON state file with atomic writes
- Agent states: `running | idle | stuck | waiting_approval | complete | done | escalated`
- Per-agent tracking: window, worktree, branch, objective, PR number, checkpoints, session_id

**Coordination Mechanisms:**
- **Checkpoint Protocol**: Agents output `CHECKPOINT:<step-name>` to signal progress
- **ORCHESTRATOR:DONE**: Terminal signal from agents, triggers verification (not acceptance)
- **verify-complete.sh**: Validates checkpoints, unresolved threads, CI status, CHANGES_REQUESTED staleness
- **Thread Resolution Integrity**: Strict rule -- no GraphQL resolveReviewThread without a committed code fix
- **Serial /pr-test**: Only one test runs at a time (shared ports/DB); orchestrator owns the queue
- **Self-recovery**: Agents auto-recover from context compaction via state file + `gh pr view`
- **tmux send-keys pattern**: Text and Enter always split with sleep 0.3 for reliability

**Handoff to Agents:**
- Worktree auto-assignment from spare pool
- `--permission-mode bypassPermissions` on all spawns
- Session ID for exact session resume after crashes
- Images passed via file path (agents use multimodal Read tool)

### Platform Multi-Agent Architecture

1. **AgentExecutorBlock** -- Invokes one agent graph from within another (recursive sub-agent calls)
2. **AutoPilotBlock** -- Spawns a CoPilot sub-agent with:
   - Recursion depth limits (`SubAgentRecursionError`)
   - Permission inheritance (merged with parent, only more restrictive)
   - Active turn management with lifetime limits
3. **OrchestratorBlock** -- LLM-driven tool-call loop that coordinates multiple blocks as "tools"
4. **CoPilot Bot** -- Multi-platform (Discord, extensible) bridge to AutoPilot

### Agent Roster (Development Agents via Claude Code Skills)

| Skill | Role | Scope |
|-------|------|-------|
| `/orchestrate` | Fleet supervisor | Manages N parallel coding agents |
| `/pr-review` | Code reviewer | Posts inline findings with criticality badges |
| `/pr-address` | Comment resolver | Loops until CI green + 0 unresolved threads |
| `/pr-polish` | PR closer | Alternates review/address until merge-ready (max 10 rounds) |
| `/pr-test` | E2E tester | Full-stack testing with screenshots + evidence |
| `/open-pr` | PR creator | Template-driven PR creation with test coverage |
| `/setup-repo` | Environment bootstrap | Worktree-based parallel dev layout |
| `/worktree` | Worktree creator | Single worktree setup with env/deps |
| `/write-frontend-tests` | Test writer | Analyzes diff, plans and writes integration tests |
| `/vercel-react-best-practices` | Code quality | 50+ React/Next.js performance rules |

### Shared State Mechanisms

- **Graph execution state**: PostgreSQL via Prisma ORM (AgentGraph, AgentNode, AgentGraphExecution)
- **Real-time coordination**: RabbitMQ for async task processing; Redis for locks, pub/sub, active turns
- **Orchestrator state**: JSON file with atomic `jq + mv` writes
- **Agent memory**: Graphiti knowledge graph (FalkorDB-backed) for CoPilot long-term memory
- **Workspace files**: Persistent per-session scoped storage with virus scanning (ClamAV)

---

## 6. Research Dimension Mapping

### Relevance Ratings

| Dimension | Relevance | Key Patterns |
|-----------|-----------|--------------|
| **Context Engineering** | **High** | Hierarchical CLAUDE.md/AGENTS.md with `@` pointer delegation; dual-audience pattern (Claude + Copilot); scope-graduated context (root → platform → backend → subsystem); `vercel-react-best-practices` skill with 50+ rule files |
| **Model Selection** | **Medium** | Model router in CoPilot (`model_router.py`, `model_normalize.py`); multi-provider support (OpenAI, Anthropic, OpenRouter); Extended Thinking mode selection |
| **Prompt Craft** | **High** | CoPilot prompting system (`prompting.py`); builder context injection; tool definitions as structured schemas; conventional commit format enforcement in PR titles; system prompt composition for sub-agents |
| **Tool Integration** | **High** | 339 block implementations as visual tools; MCP Tool block type; CoPilot tool registry with 30+ tools; ProviderBuilder pattern for block configuration; `store_media_file()` abstraction with format-aware outputs |
| **Intent Engineering** | **Medium** | Block schemas with typed inputs/outputs (Pydantic); `SchemaField` descriptions; category system for block discovery; Why/What/How PR template structure |
| **Orchestration** | **High** | `/orchestrate` skill (fleet management with checkpoint protocol); OrchestratorBlock (LLM tool-call loop); graph execution engine (topological sort, parallel execution); `/pr-polish` convergence loop with safety valves |
| **Evaluation** | **Medium** | Direct benchmark system (classic); `/pr-test` with mandatory screenshots and before/after evidence; snapshot testing for API responses; block test validation |
| **Sandboxing** | **High** | Classic permission model (workspace/agent allow/deny with pattern matching); CoPilot SDK security hooks (multi-user isolation, dangerous pattern detection, workspace scoping); E2B sandbox for code execution; ClamAV virus scanning |
| **Governance** | **High** | CODEOWNERS; pre-commit secret detection (two tools); cache protection middleware; AutoMod content moderation; Polyform Shield license split; 90-day responsible disclosure; branching strategy enforcement |
| **Agent Design** | **High** | Block as atomic capability unit; visual graph composition; HumanInTheLoopBlock (pause/approve/reject); AutoPilotBlock with recursion depth limits and permission inheritance; self-recovery protocol for context compaction |
| **Agentic Systems** | **High** | Full multi-agent orchestration (tmux fleet); recursive sub-agent invocation with permission narrowing; CoPilot as conversational meta-agent (builds agents that run agents); marketplace for agent sharing; continuous execution with trigger-based activation |

### Findings Candidates

The following patterns are worth promoting to the Research KB:

1. **Dual-Audience Context Pattern** (Context Engineering, High)
   - CLAUDE.md uses `@AGENTS.md` pointer to maintain single source of truth while serving both Claude Code (discovers CLAUDE.md by convention) and other AI tools (can read AGENTS.md directly). Avoids content duplication while maximizing agent tool compatibility.

2. **Fleet Orchestration via tmux + State File** (Orchestration, High)
   - A meta-agent supervisor manages N parallel coding agents using tmux windows, a JSON state file with atomic writes, and a checkpoint protocol. Demonstrates production-grade multi-agent coordination for development workflows without custom infrastructure.

3. **Permission Narrowing via Recursive Inheritance** (Sandboxing, High)
   - CoPilot permissions use a model where sub-agents inherit parent permissions but can only be MORE restrictive, never less. Effective-allowed sets are intersected. This prevents privilege escalation through agent nesting.

4. **Convergence Loop with Dual Clean-Poll Exit** (Orchestration, High)
   - `/pr-polish` alternates review/address rounds until convergence, then requires 2 consecutive clean polls 60s apart before accepting. Accounts for delayed bot responses that would create false "done" signals. Includes MAX_ROUNDS safety valve.

5. **Block-as-Tool Architecture** (Tool Integration, High)
   - 339 blocks serve as both visual composition units (graph editor) and as LLM-callable tools (orchestrator/CoPilot). Each block has typed Pydantic input/output schemas, cost tracking, and a standard `run()` interface. The OrchestratorBlock converts blocks into LLM tool definitions dynamically.

6. **Thread Resolution Integrity Rule** (Governance, Medium)
   - Explicit rule: "Do NOT resolve any review thread via GraphQL unless the code fix is committed and pushed first." Detects fake resolutions by checking last comment for commit SHA. Addresses the most common failure mode in automated PR workflows.

7. **Security Hook Pre-Validation** (Sandboxing, High)
   - Claude Agent SDK integration includes pre-execution hooks that validate tool calls for multi-user isolation, workspace boundary enforcement, dangerous pattern detection, and BiDi/zero-width character sanitization. Defense-in-depth for LLM-driven tool execution.

8. **Agent Self-Recovery from Context Compaction** (Agent Design, Medium)
   - Agents include a self-recovery instruction: "If your context compacts and you lose track, read your state from the orchestrator state file and `gh pr view`." Acknowledges context window limits as a first-class operational concern and provides a deterministic recovery path.

---

## Appendix: Key File Paths

### Context Engineering Files
- `/AGENTS.md` -- Root contribution guide
- `/autogpt_platform/AGENTS.md` -- Platform-level guide
- `/autogpt_platform/backend/AGENTS.md` -- Backend architecture and conventions
- `/autogpt_platform/frontend/AGENTS.md` -- Frontend patterns
- `/autogpt_platform/frontend/CONTRIBUTING.md` -- Comprehensive frontend guide
- `/.github/copilot-instructions.md` -- GitHub Copilot onboarding

### Skills (Development Agent Tools)
- `/.claude/skills/orchestrate/SKILL.md` -- Fleet management (700+ lines)
- `/.claude/skills/pr-polish/SKILL.md` -- Convergence loop
- `/.claude/skills/pr-review/SKILL.md` -- Code review
- `/.claude/skills/pr-address/SKILL.md` -- Comment resolution
- `/.claude/skills/pr-test/SKILL.md` -- E2E testing
- `/.claude/skills/open-pr/SKILL.md` -- PR creation
- `/.claude/skills/setup-repo/SKILL.md` -- Environment bootstrap
- `/.claude/skills/worktree/SKILL.md` -- Worktree setup
- `/.claude/skills/write-frontend-tests/SKILL.md` -- Test generation
- `/.claude/skills/vercel-react-best-practices/` -- 50+ performance rules

### Platform Architecture
- `/autogpt_platform/backend/backend/blocks/_base.py` -- Block base class, types, categories, costs
- `/autogpt_platform/backend/backend/blocks/orchestrator.py` -- LLM tool-call loop
- `/autogpt_platform/backend/backend/blocks/human_in_the_loop.py` -- Human gate
- `/autogpt_platform/backend/backend/blocks/autopilot.py` -- Sub-agent block
- `/autogpt_platform/backend/backend/executor/manager.py` -- Graph execution engine
- `/autogpt_platform/backend/backend/executor/automod/manager.py` -- Content moderation
- `/autogpt_platform/backend/backend/copilot/permissions.py` -- Tool/block permission model
- `/autogpt_platform/backend/backend/copilot/sdk/security_hooks.py` -- Pre-execution validation

### Governance
- `/.claude/settings.json` -- Permission allowlist
- `/.pre-commit-config.yaml` -- Secret detection + dependency checks
- `/.github/CODEOWNERS` -- Team ownership
- `/SECURITY.md` -- Responsible disclosure policy
- `/.github/PULL_REQUEST_TEMPLATE.md` -- PR checklist template
