---
title: "OpenClaw -- Structural Analysis"
id: "openclaw-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-08"
updated: "2026-04-08"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "openclaw"
analyzed_version: "v2026.4.5"
analyzed_date: "2026-04-08"
repo_url: "https://github.com/openclaw/openclaw"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
  - "research-dimension-mapping"
---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 13,216 |
| Total directories | 796 |
| TypeScript files | 10,711 (81%) |
| Markdown files | 636 (4.8%) |
| Swift files | 617 (4.7%) |
| JSON files | 410 |
| Kotlin files | 139 |
| MJS files | 124 |
| Shell scripts | 92 |
| PNG files | 86 |
| Prose files (.prose) | 64 |
| YAML/YML files | 58 |
| Go files | 24 |
| MD-to-code ratio | **0.054:1** (code dominant — production codebase) |
| Max directory depth | 12 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skills (SKILL.md entrypoints) | 53 | `skills/` |
| Dev/maintainer skills | 8 | `.agents/skills/` |
| Context/boundary files (CLAUDE.md + AGENTS.md) | ~24 (12 pairs) | Root, `extensions/`, `src/` subsystems |
| Workspace templates | 6 | `docs/reference/templates/` |
| Human documentation | ~200 | `docs/` (concepts, channels, CLI, plugins, etc.) |
| Extension READMEs | ~100 | `extensions/*/` |
| i18n docs | ~50 | `docs/.i18n/` |
| Project files | ~15 | Root (README, CHANGELOG, CONTRIBUTING, SECURITY, etc.) |
| Prose test files | 64 | Various (`.prose` extension) |
| Other | ~120 | Various |
| **Total** | **~636** |

Key insight: Unlike BMAD/GSD where markdown IS the codebase, OpenClaw is a production TypeScript codebase (81% TS) where markdown serves as documentation and context files. The 53 skills + 8 maintainer skills represent the framework's markdown-as-code surface, but it's a small fraction of the total.

### Directory Naming Conventions
Kebab-case throughout. Directories are organization-based:
- `extensions/` (plugin packages, one per provider/channel/feature)
- `skills/` (SKILL.md-based user skills)
- `src/` (core source, feature-organized subdirectories)
- `apps/` (mobile apps: android, ios, macos)
- `packages/` (NPM workspace packages)

### Top-Level Structure
```
.
├── .agents/              # Maintainer skills (PR, release, QA, security)
│   └── skills/           # 8 maintainer skills
├── .pi/                  # Pi (another AI tool) config
│   ├── extensions/
│   ├── git/
│   └── prompts/          # 4 Pi prompts (cl, is, landpr, reviewpr)
├── apps/                 # Native apps (Android, iOS, macOS)
├── assets/               # Chrome extension, images
├── docs/                 # Mintlify documentation site
│   ├── concepts/         # 36 concept docs (architecture, memory, agents, etc.)
│   ├── channels/         # Channel-specific docs
│   ├── plugins/          # Plugin SDK docs
│   ├── reference/        # Templates (SOUL.md, USER.md, etc.)
│   └── ...
├── extensions/           # ~100 bundled plugin packages
├── git-hooks/            # Pre-commit hooks
├── packages/             # NPM workspace packages (SDK, bots)
├── qa/                   # QA scenarios
├── scripts/              # Build, dev, test, deployment scripts
├── skills/               # 53 user-facing skills
├── src/                  # Core source (~50 subdirectories)
│   ├── agents/           # Agent lifecycle, ACP spawn
│   ├── context-engine/   # Pluggable context assembly
│   ├── flows/            # Flow orchestration
│   ├── hooks/            # Hook system
│   ├── plugins/          # Plugin loader, registry
│   ├── sessions/         # Session management
│   └── ...
├── test/                 # Test helpers, fixtures
├── ui/                   # React control UI
└── vendor/               # Vendored dependencies
```

### Notable Structural Patterns
1. **Plugin-centric architecture**: ~100 bundled plugins in `extensions/`, each a self-contained NPM workspace package. Same boundary as third-party plugins.
2. **Massive skill ecosystem**: 53 user-facing skills (camera, calendar, Discord, GitHub, Notion, Obsidian, Slack, Spotify, Trello, weather, etc.) + 8 internal maintainer skills.
3. **Multi-platform native apps**: iOS (Swift), Android (Kotlin), macOS (Swift) — not just a CLI tool.
4. **Symlinked context files**: `CLAUDE.md` is a symlink to `AGENTS.md` in each location, so both Claude Code and other AI tools see the same boundary context.
5. **Prose test files**: `.prose` extension for natural language test scenarios — unusual testing pattern.

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `AGENTS.md` / `CLAUDE.md` (root) | LLM | Global | Auto-loaded | Constraints/Rules | Comprehensive repo guidelines: structure, boundaries, coding style, testing, git, security (~300 lines) |
| `extensions/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Plugin boundary rules: import restrictions, SDK contract |
| `extensions/acpx/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | ACP extension boundary |
| `src/channels/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Channel implementation boundary |
| `src/gateway/protocol/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Gateway wire protocol boundary |
| `src/gateway/server-methods/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Server method boundary |
| `src/plugin-sdk/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Plugin SDK public contract boundary |
| `src/plugins/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Plugin loader/registry boundary |
| `test/helpers/channels/AGENTS.md` + `CLAUDE.md` | LLM | Project | Auto-loaded | Constraints/Rules | Test channel helper boundary |
| `docs/reference/templates/SOUL.md` | Both | Global | Referenced | Identity/Persona | Template for agent personality/identity |
| `docs/reference/templates/USER.md` | Both | Global | Referenced | Memory/State | Template for user profile record |
| `docs/reference/templates/AGENTS.md` | Both | Global | Referenced | Constraints/Rules | Template for workspace rules/conventions |
| `docs/reference/templates/HEARTBEAT.md` | Both | Global | Referenced | Workflow/Process | Template for proactive tasks |
| `docs/reference/templates/TOOLS.md` | Both | Global | Referenced | Tool Usage | Template for local environment notes |
| `skills/*/SKILL.md` (53 files) | LLM | Tool | Auto-loaded | Tool Usage | User-facing skills (L1 metadata + L2 instructions) |
| `.agents/skills/*/SKILL.md` (8 files) | LLM | Tool | Auto-loaded | Tool Usage + Workflow | Maintainer skills (PR, release, QA, security) |
| `.pi/prompts/*.md` (4 files) | LLM | Tool | Auto-loaded | Workflow/Process | Pi-specific prompts (changelog, issue analysis, land PR, review PR) |
| `.github/instructions/copilot.instructions.md` | LLM | Global | Auto-loaded | Constraints/Rules | GitHub Copilot-specific instructions |
| `.agents/maintainers.md` | LLM | Global | Auto-loaded | Constraints/Rules | Maintainer team roster |

Sampling notes: Read root AGENTS.md/CLAUDE.md in full (300 lines). Read 3 subsystem AGENTS.md exemplars (extensions, plugins, channels). Read 2 skill exemplars (coding-agent, taskflow). Read all 6 workspace templates. Classified remaining by pattern.

### Context Loading Strategy
**Distributed boundary guides with CLAUDE.md/AGENTS.md symlink pairs:**

1. **Root context** (`CLAUDE.md`/`AGENTS.md`): Massive (~300 lines) repo-wide guidelines covering structure, architecture boundaries, coding style, testing, git, security. Auto-loaded by harness.
2. **Subsystem boundary guides**: Each major subsystem (`extensions/`, `src/channels/`, `src/plugins/`, `src/gateway/protocol/`, etc.) has its own `AGENTS.md` + `CLAUDE.md` symlink pair. These define import restrictions, public contracts, and boundary rules. Progressive disclosure — devs working in a subsystem get subsystem-specific rules without loading all rules.
3. **Skills**: 53 user-facing + 8 maintainer skills using standard SKILL.md format. Loaded on-demand by the skill system.
4. **Workspace templates**: 6-file taxonomy (SOUL.md, USER.md, AGENTS.md, TOOLS.md, HEARTBEAT.md, MEMORY.md) defines the context structure for deployed agents. These templates are not used during development — they define what the shipped product creates for end users.

**Key pattern: CLAUDE.md symlinks to AGENTS.md.** This ensures both Claude Code and other AI tools (Pi, Copilot, etc.) see identical boundary context. The canonical file is AGENTS.md; CLAUDE.md is always a symlink.

**Multi-AI-tool context**: The repo carries context files for Claude (CLAUDE.md), Pi (.pi/prompts/), and Copilot (.github/instructions/). Same repo, multiple AI tool support.

## 3. Workflow Topology

### Phases/Stages
OpenClaw is a production software product, not a workflow framework. It doesn't have SDLC phases like BMAD or GSD. Instead, it has:

| System | Trigger | Purpose | Human Gate? |
|--------|---------|---------|-------------|
| **Gateway** | `openclaw gateway run` | Main runtime: routes messages between channels and model providers | No (autonomous) |
| **Agent Loop** | Incoming message | Model inference cycle: context assembly → model call → tool execution → response | No (autonomous) |
| **Dreaming** | Background timer | Memory consolidation: Light→Deep→REM phases for promoting short-term to long-term memory | No (autonomous, but human can review DREAMS.md) |
| **TaskFlow** | Code/plugin | Durable flow substrate for multi-step background work | Optional (setWaiting for human input) |
| **Skills** | User invocation or auto-trigger | Skill execution: SKILL.md loaded → instructions followed → tools used | Per-skill |
| **PR Maintainer** | Maintainer invocation | PR triage, review, close, merge workflow | Yes (explicit approval for merge/close) |
| **Release** | Maintainer invocation | Version bump, changelog, publish workflow | Yes (explicit approval) |

### Flow Diagram (ASCII)
```
Inbound Message
      │
      ▼
┌─────────────┐
│  GATEWAY    │──── Routes to correct agent
│  (routing)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐    ┌──────────────┐
│  CONTEXT    │◄──►│ MEMORY CORE  │
│  ENGINE     │    │ (recall,     │
│ (assemble)  │    │  search,     │
└──────┬──────┘    │  dreaming)   │
       │           └──────────────┘
       ▼
┌─────────────┐
│  MODEL RUN  │──── Tool calls, skill invocations
│  (agent     │
│   loop)     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  RESPONSE   │──── Back to originating channel
│  (routing)  │
└─────────────┘

Background:
┌──────────────────────────────────┐
│  DREAMING (Light → Deep → REM)  │
│  Promotes daily notes → MEMORY  │
└──────────────────────────────────┘
```

### Transition Mechanisms
- **Message-driven**: Incoming messages trigger the agent loop.
- **Plugin hooks**: Plugins register lifecycle hooks (onLoad, onEnable, etc.).
- **TaskFlow**: Durable flow substrate with revision-checked mutations, waiting states, and child task linkage.
- **Heartbeats**: Periodic polls that the agent can use for proactive background work.
- **Cron**: Time-based task scheduling with model/channel configuration.

### Parallelism
- **Multi-agent routing**: Gateway can host multiple isolated agents simultaneously, each with its own workspace, sessions, and auth.
- **ACP spawn**: Agent Client Protocol for spawning subagent processes (Claude Code, Codex, OpenCode, Pi).
- **Background sessions**: Skills can run in background mode with session monitoring.
- **Dreaming phases**: Run as background cooperative phases, not parallel.

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Root AGENTS.md | `AGENTS.md` | Soft (LLM-read) | 300 lines of repo guidelines, architecture boundaries, coding style |
| Subsystem boundary guides | `*/AGENTS.md` | Soft (LLM-read) | Import restrictions, public contract definitions per subsystem |
| CODEOWNERS | `.github/CODEOWNERS` | Hard (GitHub) | Security-focused paths require listed owner review |
| Pre-commit hooks | `git-hooks/` + `prek` | Hard | `pnpm check` (lint, format, type-check) |
| Architecture checks | CI `check-additional` | Hard (CI) | Boundary policy guards, import fan-out enforcement |
| Plugin SDK contract | `src/plugin-sdk/` | Hard (TypeScript) | Type-checked plugin boundary, API drift detection |
| Drift detection | `.sha256` hash files | Hard (CI) | Config schema, Plugin SDK API drift auto-detected |
| Skill metadata schema | `openclaw.plugin.json` | Hard | Manifest validation, capability registration |
| Committer script | `scripts/committer` | Soft | Scoped staging to prevent unrelated file inclusion |
| Auto-close labels | `.github/workflows/auto-response.yml` | Hard (GitHub Actions) | Auto-close issues/PRs matching specific patterns |

### Guardrail Patterns
1. **Boundary guide cascade**: Root `AGENTS.md` sets global rules. Subsystem `AGENTS.md` files add subsystem-specific constraints. This is progressive disclosure for governance.
2. **Plugin SDK as hard boundary**: Extensions import only from `openclaw/plugin-sdk/*`. Core never imports extension internals. This is enforced by CI architecture checks and TypeScript.
3. **Drift detection via SHA-256 hashes**: Config schema and Plugin SDK API have generated baselines with hash files. Changes auto-detected in CI.
4. **Bug-fix evidence bar**: Maintainer skill requires symptom evidence, verified root cause, implicated code path fix, and regression test before merge. Not just "it looks right."
5. **Prompt cache stability as correctness**: Deterministic ordering of model payloads is treated as performance-critical, not cosmetic. Explicit rules about preserving cached prefixes.
6. **No-AGENTS.md-without-CLAUDE.md rule**: Adding a new AGENTS.md requires also adding a CLAUDE.md symlink to it. Ensures cross-AI-tool compatibility.

### Permission Model
- **CODEOWNERS for security paths**: Specific security-focused files require listed owner review.
- **Plugin capability registration**: Plugins declare capabilities in manifest; runtime only grants what's declared.
- **Agent skill allowlists**: Per-agent configuration can restrict which skills are available.
- **Sandbox mode**: Optional sandboxing restricts agent file system access.
- **Auth isolation**: Each agent has its own auth profiles — no credential sharing by default.

## 5. Cross-Agent Protocol

### Agent Roster
OpenClaw's "agents" operate at two levels: (1) deployed AI agents that serve end users across channels, and (2) development agents (skills) that assist maintainers.

**Development/Maintainer Agents:**
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| PR Maintainer | `.agents/skills/openclaw-pr-maintainer/` | PR triage, review, close, merge, evidence verification | GitHub API |
| Release Maintainer | `.agents/skills/openclaw-release-maintainer/` | Version coordination, changelog, publish | GitHub releases |
| GHSA Maintainer | `.agents/skills/openclaw-ghsa-maintainer/` | Security advisory management | GitHub Security Advisories |
| QA Testing | `.agents/skills/openclaw-qa-testing/` | Test automation | Vitest |
| Parallels Smoke | `.agents/skills/openclaw-parallels-smoke/` | Cross-platform testing | Parallels VMs |
| Security Triage | `.agents/skills/security-triage/` | Security report evaluation | CODEOWNERS |
| Heap Leak Tester | `.agents/skills/openclaw-test-heap-leaks/` | Memory leak detection | Node.js profiler |
| Discord Roundtrip | `.agents/skills/parallels-discord-roundtrip/` | Discord E2E testing | Parallels + Discord |

**Runtime Agent Architecture (shipped product):**
| Component | Role | Communicates With |
|-----------|------|-------------------|
| Gateway | Message routing, multi-agent hosting | Channels, agents |
| Agent (per instance) | Isolated brain: workspace, sessions, auth | Context engine, model providers, skills |
| Context Engine | Context assembly, compaction | Agent loop, memory plugins |
| Memory Core | Short-term/long-term memory, dreaming | Context engine, workspace files |
| Memory Wiki | Structured knowledge base | Memory core, workspace |
| Skills (53) | User-facing capabilities | Agent loop, external services |
| TaskFlow | Durable multi-step orchestration | Agent loop, child tasks |
| ACP Spawn | Subagent process management | External AI tools (Claude Code, Codex, Pi) |

### Handoff Mechanisms
1. **Message routing**: Gateway routes inbound messages to the correct agent based on channel bindings. Agent processes message through the agent loop.
2. **Context assembly**: Context engine assembles model context from session history, memory files, and system prompt additions. Pluggable — can be replaced by third-party engines.
3. **Skill invocation**: Skills are invoked by name or auto-triggered from user intent. SKILL.md loaded, instructions followed.
4. **ACP spawning**: Agent can spawn subprocesses (Claude Code, Codex, etc.) for coding tasks. Background mode with session monitoring.
5. **TaskFlow durable flows**: Multi-step work persisted across sessions with revision-checked state mutations.
6. **Heartbeat proactive polling**: Agent checks workspace files and external services on a timer.

### Shared State
- **Workspace files**: SOUL.md (identity), USER.md (user profile), MEMORY.md (long-term memory), memory/ (daily notes), TOOLS.md (environment), AGENTS.md (rules), HEARTBEAT.md (proactive tasks), DREAMS.md (dreaming output).
- **Session store**: Chat history per agent under `~/.openclaw/agents/<agentId>/sessions/`.
- **Config**: `~/.openclaw/openclaw.json` for system config.
- **Auth profiles**: Per-agent under `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

### Coordination Patterns
**Gateway-mediated hub-and-spoke for runtime.** The gateway routes messages to isolated agents. Agents are fully scoped — separate workspace, sessions, auth. No direct inter-agent communication in the current architecture.

**Plugin-as-capability-extension for features.** ~100 bundled plugins extend the agent's capabilities (channels, providers, media, memory). Plugins communicate through the Plugin SDK contract, not by reaching into each other.

**Skill-as-tool for user interactions.** 53 skills provide specific capabilities (coding, calendar, music, etc.). Skills are invoked by the agent during the model loop when relevant to the user's request.

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | 6-file workspace taxonomy (SOUL/USER/AGENTS/TOOLS/HEARTBEAT/MEMORY). Pluggable context engine with 4-phase lifecycle (ingest, assemble, compact, afterTurn). Dreaming memory consolidation (Light→Deep→REM). Short-term promotion with weighted scoring. Prompt cache stability as correctness concern. Progressive disclosure via distributed AGENTS.md files. |
| Model | **High** | Multi-provider architecture (Anthropic, OpenAI, Google, Mistral, Ollama, etc. via ~100 provider plugins). Model failover. Provider-family helpers. Auth profile isolation per agent. |
| Prompt | Medium | SOUL.md as personality/identity definition. System prompt assembly from workspace files. Prompt cache stability rules. No complex prompt engineering patterns — the product's value is in infrastructure, not prompts. |
| Tools | **High** | 53 user-facing skills + Plugin SDK for third-party extensibility. MCP integration. ACP spawn for delegating to other AI tools. Background session management. Process lifecycle (PTY, background, monitoring). |
| Intent | Medium | Heartbeat proactive polling. Dreaming as autonomous background processing. TaskFlow for durable multi-step intent. Skill auto-trigger from user intent. |
| Orchestration | **High** | Multi-agent gateway routing. Plugin-based capability extension (~100 plugins). TaskFlow durable flow substrate. ACP spawn for subagent processes. Isolated agent workspaces. |
| Evaluation | Medium | Vitest with 70% coverage thresholds. `.prose` natural language test scenarios. Architecture boundary checks in CI. Drift detection via SHA-256 hashes. Bug-fix evidence bar in PR maintainer skill. |
| Sandboxing | **High** | Agent workspace isolation. Per-agent auth profiles. Configurable sandboxing for file system access. Session transcript redaction for dreaming. MEMORY.md security: only loaded in DM sessions, never in group chats. |
| Governance | **High** | Distributed AGENTS.md boundary guides. CODEOWNERS for security paths. Plugin SDK hard boundary. Drift detection for schema/API changes. Auto-close labels for PR triage. Bug-fix evidence gates. No-merge-commit policy. Committer script for scoped staging. |
| Agent Design | **High** | 6-file workspace taxonomy for agent identity (SOUL.md = who you are, USER.md = who you help, AGENTS.md = workspace rules, TOOLS.md = local notes, HEARTBEAT.md = proactive tasks, MEMORY.md = long-term memory). CLAUDE.md-as-symlink pattern for multi-AI-tool compatibility. Dreaming as memory consolidation with human-reviewable DREAMS.md. Agent isolation (separate workspace, sessions, auth). Agent as "guest" metaphor: "You have access to someone's life... That's intimacy. Treat it with respect." |

### Findings Candidates

1. **6-file workspace taxonomy for agent identity** (Agent Design, Context Engineering) — SOUL.md (identity/personality), USER.md (user profile), AGENTS.md (workspace rules), TOOLS.md (local environment), HEARTBEAT.md (proactive tasks), MEMORY.md (long-term memory). Clean separation of concerns for who the agent IS vs. who it helps vs. what it knows vs. what it does. Compare to GSD's single CLAUDE.md and BMAD's config.yaml approach.
→ Promoted to [[six-file-workspace-taxonomy]] on 2026-04-08

2. **Dreaming memory consolidation** (Context Engineering, Agent Design) — Three-phase background memory system: Light (sort/stage recent signals), Deep (score/promote to MEMORY.md with threshold gates), REM (extract themes/reflections). Mimics human sleep memory consolidation. Includes Dream Diary (DREAMS.md) for human review. Novel approach to the "what should the agent remember" problem.
→ Promoted to [[dreaming-memory-consolidation]] on 2026-04-08

3. **Distributed boundary guides via AGENTS.md/CLAUDE.md symlink pairs** (Governance, Context Engineering) — Each subsystem gets its own boundary guide rather than one monolithic context file. CLAUDE.md symlinks to AGENTS.md for cross-AI-tool compatibility. Progressive disclosure: developers in a subsystem see subsystem rules without loading all rules.
→ Promoted to [[distributed-boundary-guides]] on 2026-04-08

4. **Pluggable context engine** (Context Engineering, Orchestration) — Four-phase lifecycle (ingest, assemble, compact, afterTurn) that can be replaced by third-party plugins. Separates context assembly from the agent loop. Enables experimentation with different context strategies without modifying core.
→ Promoted to [[pluggable-context-engine]] on 2026-04-08

5. **Prompt cache stability as correctness** (Context Engineering, Prompt) — Explicit rules about deterministic ordering of model payloads and preserving cached prefixes across turns. Truncation prefers mutating newest content first to keep the prefix byte-identical. This treats cache stability as performance-critical infrastructure, not cosmetic.
→ Promoted to [[prompt-cache-stability-as-correctness]] on 2026-04-08

6. **Agent-as-guest metaphor** (Agent Design, Governance) — "You have access to someone's life — their messages, files, calendar, maybe even their home. That's intimacy. Treat it with respect." This philosophical framing shapes concrete rules: external actions require asking, MEMORY.md only loads in DM sessions (not group chats), private things stay private. Compare to BMAD's "fully embody this persona" and GSD's "trust-nothing verification."
→ Promoted to [[agent-as-guest-metaphor]] on 2026-04-08

7. **ACP spawn for cross-tool delegation** (Orchestration, Tools) — Agent can spawn subprocesses for coding tasks using Claude Code, Codex, OpenCode, or Pi. Background mode with session monitoring (poll, log, kill). This is multi-AI-tool orchestration: the agent delegates to specialized coding tools rather than trying to do everything itself.
→ Promoted to [[acp-spawn-cross-tool-delegation]] on 2026-04-08

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v2026.4.5 | all | Initial analysis. 13,216 files, 636 MD, 53 skills + 8 maintainer skills, ~100 bundled plugins, multi-platform (TS + Swift + Kotlin). |
