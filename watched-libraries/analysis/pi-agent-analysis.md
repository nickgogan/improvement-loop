---
title: "Pi Agent Harness -- Structural Analysis"
id: "pi-agent-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-05-24"
updated: "2026-05-24"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "pi-agent"
  - "coding-agent"
  - "extension-api"
  - "self-modifying"
  - "typescript"
analyzed_version: "latest (commit e007fcd, 2026-05-24)"
analyzed_date: "2026-05-24"
repo_url: "https://github.com/earendil-works/pi"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# Pi Agent Harness -- Structural Analysis

## Metadata
- **Repo:** https://github.com/earendil-works/pi
- **Version analyzed:** latest (commit e007fcd, 2026-05-24 shallow clone)
- **Date:** 2026-05-24
- **Spectrum position:** study
- **Stars:** ~5k | Monorepo (4 packages)

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total TypeScript source lines | ~38,065 |
| Packages | 4 (`pi-ai`, `pi-agent-core`, `pi-coding-agent`, `pi-tui`) |
| Test files | 40+ (coding-agent package) |
| Scripts | 15 (repo root) |

### Package Architecture
| Package | Purpose | Key Exports |
|---------|---------|-------------|
| `@earendil-works/pi-ai` | Unified multi-provider LLM API | `Api`, `Model`, `Context`, `StreamOptions` |
| `@earendil-works/pi-agent-core` | Agent runtime with tool calling | `AgentMessage`, `AgentToolResult`, `ToolExecutionMode` |
| `@earendil-works/pi-coding-agent` | Interactive coding agent CLI | Extension API, skills, tools, session management |
| `@earendil-works/pi-tui` | Terminal UI with differential rendering | `TUI`, `Component`, `EditorComponent`, `KeyId` |

### Key Source Directories (coding-agent)
```
src/core/
  extensions/     — Extension system (loader, runner, types, wrapper)
  compaction/     — Context compaction with branch summarization
  tools/          — Built-in tools (bash, read, write, edit, grep, find, ls)
  agent-session.ts
  agent-session-runtime.ts
  system-prompt.ts
  skills.ts
  session-manager.ts
  model-registry.ts
  model-resolver.ts
  event-bus.ts
  keybindings.ts
```

---

## 2. Context File Map

### Agent Context Files
| File | Purpose | Loading |
|------|---------|---------|
| `AGENTS.md` (repo root) | Development rules for humans and agents | Loaded as project context |
| Context files (per-project) | Project-specific instructions | Pattern-matched, loaded into system prompt |

### Context Assembly
Pi uses a `buildSystemPrompt()` function that:
1. Accepts custom prompt OR builds default
2. Appends project context files (`<project_instructions path="...">`)
3. Appends skills section (formatted for LLM invocation)
4. Adds date and working directory

Context files are discovered by `ResourceLoader` which scans configured directories for matching files.

---

## 3. Workflow Topology

### Extension Lifecycle (30+ events)

**Session Events:**
- `resources_discover` → `session_start` → ... → `session_shutdown`
- `session_before_switch`, `session_before_fork`, `session_before_compact`, `session_before_tree`

**Agent Loop Events:**
- `input` → `before_agent_start` → `agent_start` → `turn_start` → `message_start` → `message_update` → `message_end` → `turn_end` → `agent_end`

**Tool Events:**
- `tool_call` (can block, mutate args) → `tool_execution_start` → `tool_execution_update` → `tool_execution_end` → `tool_result` (can modify result)

**Model Events:**
- `model_select`, `thinking_level_select`

### Session Tree
Sessions are file-based with tree structure:
- **Branching**: Fork from any entry point
- **Compaction**: Summarize and compress context
- **Tree navigation**: Jump to any point with optional summarization
- **Labels**: User-defined bookmarks on entries

### Extension Registration
Extensions can:
1. Register tools (LLM-callable, with schema + execute + render)
2. Register commands (slash commands with handlers)
3. Register shortcuts (keyboard bindings)
4. Register CLI flags
5. Register message renderers (custom display for custom message types)
6. Register providers (add/override LLM providers at runtime)
7. Subscribe to events (session, agent, tool, model, input)

---

## 4. Governance Model

### Development Rules (from AGENTS.md)
- Keep answers short and concise, no emojis
- Read files in full before wide-ranging changes
- No `any` unless necessary; no inline imports
- Only commit files changed in this session (multi-agent safe)
- Never `git add -A`, `git reset --hard`, `git commit --no-verify`
- Multiple sessions may run concurrently in same cwd
- Supply-chain: exact-pinned deps, `min-release-age=2`, shrinkwrap checks

### Release Process
Lockstep versioning across all packages. 6-step release with WebAuthn 2FA, local smoke tests (Node + Bun), explicit changelog management.

### Contribution Model
Auto-close on new issues/PRs from new contributors. Maintainers review daily. LGTM gate for approval.

---

## 5. Cross-Agent Protocol

### Multi-Session Safety
Pi explicitly handles concurrent sessions in the same working directory:
- Stage only your own files
- Never use `git add -A` or destructive git commands
- If rebase conflicts in files you didn't modify, abort

### Extension Communication
- Shared `EventBus` for inter-extension communication
- `sendMessage()` / `sendUserMessage()` for programmatic agent interaction
- `appendEntry()` for state persistence (custom entries not sent to LLM)

### SDK Integration
Pi supports embedding via SDK mode (see openclaw/openclaw integration). Extensions can operate the agent programmatically via the same API.

---

## Findings Candidates

| # | Pattern | Priority | Category | Evidence |
|---|---------|----------|----------|----------|
| 1 | **Runtime Self-Modification via Extension API** — Agent can register/unregister tools, providers, and commands at runtime. Extensions are TypeScript modules with full lifecycle hooks. The agent can ask itself to build extensions. | P1 | Agent Design | 1500-line types.ts; loader.ts with jiti for runtime TS eval |
| 2 | **Session Tree as First-Class Abstraction** — Sessions branch, compact, and navigate like git. Entries have labels, tree navigation generates summaries. Enables exploratory work without losing context. | P2 | Context Engineering | session-manager.ts, tree events, branch summarization |
| 3 | **Tool Call Event Interception Pattern** — `tool_call` event allows extensions to block execution or mutate arguments in-place before the tool runs. Later handlers see earlier mutations. No re-validation after mutation. | P2 | Tool Integration | ToolCallEvent type with block/reason result |
| 4 | **Supply-Chain Hardening for Agent Packages** — Exact-pinned deps, min-release-age, shrinkwrap generation, pre-commit lockfile guards, no lifecycle scripts. Treats npm dependency changes as reviewed code. | P2 | Governance | AGENTS.md, .npmrc, scripts/generate-coding-agent-shrinkwrap.mjs |
| 5 | **Multi-Provider LLM Abstraction with Dynamic Registration** — Extensions can register entirely new providers at runtime (baseUrl, models, OAuth, custom stream handlers). Provider registration is queued during init, immediate after binding. | P3 | Model Selection | ProviderConfig type, registerProvider/unregisterProvider API |
| 6 | **Concurrent Agent Session Safety Rules** — Explicit governance for multi-agent concurrent access: stage only your files, never destructive git, abort on foreign conflicts. | P3 | Governance | AGENTS.md Git section |
