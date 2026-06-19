---
title: "Beads — Structural Analysis"
id: "beads-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-04-19"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "beads"
analyzed_version: "v1.0.2"
analyzed_date: "2026-04-19"
repo_url: "https://github.com/gastownhall/beads"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# Beads — Structural Analysis

## Metadata
- **Repo:** https://github.com/gastownhall/beads
- **Version analyzed:** v1.0.2
- **Date:** 2026-04-19
- **Spectrum position:** cherry-pick
- **Stars:** 20.9k

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 1,545 |
| Total directories | 146 |
| Markdown files | 250 |
| Code files (Go) | 1,061 |
| SQL files | 63 |
| Shell scripts | 41 |
| Python files | 23 |
| Config (YAML/JSON) | 29 |
| MD-to-code ratio | 0.24 (1 MD per ~4 Go files) |
| Max directory depth | 5 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions / context | ~15 | `claude-plugin/agents/`, `claude-plugin/skills/beads/resources/`, root |
| Commands/skills | ~30 | `claude-plugin/commands/`, `claude-plugin/skills/` |
| Workflows | ~5 | `.agent/workflows/`, `claude-plugin/skills/beads/resources/` |
| Design docs / ADRs | ~10 | `docs/adr/`, `docs/design/`, `docs/dev-notes/` |
| Website/user docs | ~100+ | `website/docs/`, `website/versioned_docs/` |
| Examples | ~40 | `examples/` (14 example directories) |
| Templates | ~5 | `internal/templates/` |
| Human documentation | ~40 | `docs/`, root README/CONTRIBUTING |

### Directory Naming Conventions
- kebab-case throughout (`bash-agent`, `claude-desktop-mcp`, `multi-phase-development`)
- Internal Go packages use lowercase single-word (`beads`, `compact`, `config`, `git`)
- Plugin structure mirrors Claude Code conventions (`commands/`, `skills/`, `agents/`)

### Top-Level Structure
```
.
├── .agent/workflows/          # Agent workflow definitions
├── .claude/hooks/             # Claude Code hooks (SessionStart, PreCompact)
├── .claude-plugin/            # Plugin manifest
├── claude-plugin/             # Plugin: agents, commands, skills
├── cmd/bd/                    # CLI entry point
├── docs/                      # Design docs, ADRs, dev notes
├── examples/                  # 14 usage examples
├── format/                    # Output formatting
├── integrations/              # beads-mcp, claude-code, junie
├── internal/                  # Core Go packages (30+ packages)
├── npm-package/               # npm distribution
├── scripts/                   # Build/migration scripts
├── tests/                     # Integration and regression tests
├── website/                   # Docusaurus site
├── winget/                    # Windows package manager
```

### Notable Structural Patterns
- **Massive internal package count**: 30+ packages under `internal/` — well-decomposed Go architecture
- **14 example directories**: Heavy investment in usage examples (bash-agent, python-agent, team-workflow, multi-phase-development, etc.)
- **Claude plugin as a first-class artifact**: Full `claude-plugin/` directory with agents, commands, skills, resources — not an afterthought
- **Triple integration**: `integrations/` covers beads-mcp (MCP server), claude-code, and junie (JetBrains AI)
- **Website with versioned docs**: Docusaurus-based docs with versioned sidebars

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `/CLAUDE.md` | LLM | Project | Auto-loaded | Workflow/Process + Constraints/Rules | Architecture overview, defers to AGENTS.md |
| `/AGENTS.md` | LLM | Project | Auto-loaded + Chain-loader → AGENT_INSTRUCTIONS.md | Tool Usage + Constraints/Rules | OpenAI agents.txt convention; redirects to detailed instructions |
| `/AGENT_INSTRUCTIONS.md` | LLM | Project | Referenced (from AGENTS.md) | Workflow/Process + Constraints/Rules + Tool Usage | Full operational instructions: workflow, dev standards, session close |
| `/cmd/bd/AGENTS.md` | LLM | Task | Auto-loaded (subdir) | Tool Usage | Minimal redirect to `bd prime` |
| `/cmd/bd/@AGENTS.md` | LLM | Task | Auto-loaded (subdir) | Tool Usage | Dual filename for agent-framework compatibility |
| `/docs/CLAUDE.md` | LLM | Task | Auto-loaded (subdir) | Identity context | Docs subdir context |
| `/claude-plugin/skills/beads/SKILL.md` | LLM | Tool | Referenced (skill invocation) | Workflow/Process + Tool Usage | Skill entry point with YAML frontmatter (`allowed-tools`, version) |
| `/claude-plugin/skills/beads/CLAUDE.md` | Both | Tool | Referenced | Constraints/Rules | DRY policy — `bd prime` is canonical |
| `/claude-plugin/skills/beads/resources/AGENTS.md` | LLM | Tool | Referenced | Workflow/Process | Agent bead state machine |
| `/claude-plugin/skills/beads/resources/BOUNDARIES.md` | LLM | Tool | Referenced | Constraints/Rules | bd vs TodoWrite decision matrix |
| `/claude-plugin/skills/beads/resources/WORKFLOWS.md` | LLM | Tool | Referenced | Workflow/Process | Session start, compaction recovery, epic planning |
| `/claude-plugin/skills/beads/resources/ASYNC_GATES.md` | LLM | Tool | Referenced | Workflow/Process | Gate types, approval flows |
| `/claude-plugin/skills/beads/resources/CHEMISTRY_PATTERNS.md` | LLM | Tool | Referenced | Workflow/Process | Mol/wisp lifecycle |
| `/claude-plugin/skills/beads/resources/MOLECULES.md` | LLM | Tool | Referenced | Workflow/Process | Template system |
| `/claude-plugin/agents/task-agent.md` | LLM | Task | Injected (subagent) | Identity/Persona + Workflow/Process | Autonomous task-completion agent persona |
| `/claude-plugin/commands/*.md` (~28 files) | LLM | Task | Referenced (slash commands) | Tool Usage | Per-command instructions |
| `/.agent/workflows/resolve-beads-conflict.md` | LLM | Task | Referenced | Workflow/Process | Dolt conflict resolution procedure |
| `/internal/templates/agents/defaults/beads-section.md` | LLM | Project | Injected (by `bd init`) | Constraints/Rules + Workflow/Process | Template injected into consumer project AGENTS.md |

### Context Loading Strategy

Beads uses a **layered, progressive-disclosure strategy with live CLI injection**:

1. **Static auto-load layer**: Root `CLAUDE.md` and `AGENTS.md` auto-loaded by Claude Code. Deliberately short; redirect to `AGENT_INSTRUCTIONS.md` and `bd prime`.

2. **Live CLI injection layer**: `bd hooks install` configures a `SessionStart` hook running `bd prime` — generates ~1-2k tokens of AI-optimized workflow context from the live CLI binary. A `PreCompact` hook runs `bd dolt push` before context compaction to prevent data loss. Canonical per ADR-0001.

3. **Progressive disclosure layer**: SKILL.md is a thin entry point with links to 14 resource files. Agent fetches only what it needs (BOUNDARIES.md for tool selection, WORKFLOWS.md for session patterns, ASYNC_GATES.md for gate coordination).

4. **Injection at consumer project init**: `bd init` writes `beads-section.md` content into the target project's AGENTS.md, embedding rules at the consumer level.

5. **Subdir context**: `cmd/bd/AGENTS.md` ensures agents working in CLI source folder get scoped instructions without content duplication.

---

## 3. Workflow Topology

### Phases/Stages
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Session Start | SessionStart hook fires | `bd prime` injected, ready to work | No |
| Task Selection | `bd ready` lists available work | Agent claims a task via `bd update --claim` | No |
| Work Loop | Task claimed | Task completed or blocker found | No (soft quality gates) |
| Discovery | New work found during implementation | New issue created with `discovered-from` dep | No |
| Landing the Plane | User phrase or session end | All gates passed, `git push` succeeds | Yes (hard) |
| Compaction Recovery | Context compaction triggers | Notes restored from bd state | No (automatic) |

### Flow Diagram (ASCII)
```
SESSION START
     │
     ▼
[SessionStart hook: bd prime injected]
     │
     ▼
 bd ready ──► (no ready work?)──► bd blocked ──► investigate
     │
     ▼
bd show <id> → bd update <id> --claim
     │
     ▼
 WORK LOOP ◄──────────────────────────┐
  │                                     │
  ▼                                     │
  Implement / test / document           │
  │                                     │
  ▼                                     │
  Discovery? ──► bd create → bd dep add │
  │                                     │
  ▼                                     │
  bd close <id> ──► bd ready ──────────┘
     │
     ▼
LANDING THE PLANE
  │
  ├─ [HARD] File issues for remaining work
  ├─ [HARD] make lint && make test
  ├─ [HARD] git pull --rebase && git push (loop until succeeds)
  └─ [HARD] git stash clear + git remote prune
     │
     ▼
[PreCompact hook: bd dolt push]
     │
     ▼
SESSION END — handoff prompt
```

### Gate Workflow (Async Gates)
```
bd gate create --await <type> --timeout <duration>
     │
     ▼
 PENDING ───────────────────────┐
     │                           │
     │ timer:*  → elapsed?       │
     │ gh:run:* → CI result?     │ (bd gate eval polls)
     │ gh:pr:*  → merged?        │
     │ human:*  → bd gate approve│
     │                           │
     └──► OPEN ─────────────────┘
              │
              ▼
          CLOSED
```

### Transition Mechanisms
- **State transitions**: SQL updates via `bd update` CLI (compare-and-swap for `--claim`)
- **Dependency resolution**: `bd ready` checks graph — surfaces tasks only when all blockers closed
- **Async gates**: Polling-based (`bd gate eval`) with typed gate matchers (timer, GitHub run/PR, human approval)

### Parallelism
- **Fan-out**: Coordinator creates sub-issues under an epic, pins each to a named agent
- **Fan-in**: Merge issue with deps on all parts; surfaces via `bd ready` only when all close
- **Concurrency control**: Hash-based IDs prevent collision; Dolt cell-level merge handles write conflicts

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| CLI behavioral constraint | AGENTS.md, AGENT_INSTRUCTIONS.md | Hard (agent hangs) | Never use `bd edit` (opens interactive editor) |
| Shell safety constraint | AGENTS.md | Hard (agent hangs) | Always use `-f` flags (cp, rm) |
| Data integrity rule | AGENT_INSTRUCTIONS.md | Soft (bd warns) | Never populate production DB with test issues |
| Process gate | AGENTS.md, AGENT_INSTRUCTIONS.md | Hard (instructional, 3x repeated) | Work is NOT complete until `git push` succeeds |
| Build correctness | AGENT_INSTRUCTIONS.md, docs/CLAUDE.md | Hard (stale binary) | Never use `go build -o bd` — use `make install` |
| Contributor protection | AGENT_INSTRUCTIONS.md | Hard (pre-commit hook) | Check existing contributor PRs before building |
| Audit trail | AGENT_INSTRUCTIONS.md | Soft (bd doctor detects) | Commit issue ID in commit message: `(bd-abc)` |
| Architecture principle | CONTRIBUTING.md | Soft (code review) | No hardcoded sequential logic (ZFC principle) |
| PR hygiene | CONTRIBUTING.md | Soft (code review) | One issue per PR, no "while I'm here" changes |
| Canonical source rule | ADR-0001, plugin CLAUDE.md | Soft (architectural) | `bd prime` is the canonical CLI reference; never duplicate in SKILL.md |

### Guardrail Patterns
- **Repetition as enforcement**: Critical constraints repeated across 3+ files (AGENTS.md, AGENT_INSTRUCTIONS.md, cmd/bd/AGENTS.md) to ensure coverage regardless of which file an agent reads
- **CLI as guardrail**: `bd` binary itself enforces constraints (compare-and-swap claims, "Test" prefix warnings, gate timeouts)
- **Hook-based safety net**: `PreCompact` hook auto-pushes Dolt state before context compaction prevents data loss
- **`bd doctor`**: Cross-references open issues against git history to detect orphan issues

### Permission Model
Flat — all agents operate under the same ruleset. Two routing modes:
- **Maintainer**: SSH remote → push to current repo
- **Contributor**: HTTPS remote → route to `~/.beads-planning`

Witness system monitors agent heartbeats; can set agent state to `dead` on timeout. Agents cannot set `dead` themselves.

---

## 5. Cross-Agent Protocol

### Agent Roster
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Task-completion agent | `claude-plugin/agents/task-agent.md` | Autonomous: find ready → claim → work → discover → close → repeat | All other agents via Dolt |
| Agent bead (type=agent) | `claude-plugin/skills/beads/resources/AGENTS.md` | First-class issue type with state machine and heartbeat | Other agents via issue fields |
| Witness | `claude-plugin/skills/beads/resources/AGENTS.md` | Monitors heartbeats; sets agents to `dead` on timeout | Agent beads (write `dead` state) |
| Coordinator (implied) | `website/docs/multi-agent/coordination.md` | Pins work to named agents, monitors progress, manages fan-out/fan-in | Agent beads via pins/hooks |
| Role bead (type=role) | `claude-plugin/skills/beads/resources/AGENTS.md` | Defines agent capabilities; referenced by agent beads | Agent beads via `role` slot |

### Agent State Machine
```
idle ──► spawning ──► running/working ──► done ──► idle
                           │
                        stuck ──► (requires intervention)
                           │
                        dead  (set only by Witness)
                           │
                        stopped (self-halted)
```

### Handoff Mechanisms
- **Sequential**: Agent A closes issue, pins it `--for agent-b` with context comment. Agent B runs `bd hook` to see pinned work.
- **Parallel fan-out**: Coordinator creates sub-issues under epic, pins each to named agent.
- **Fan-in (merge gate)**: Coordinator creates merge issue with deps on all parts; `bd ready` surfaces only when all close.
- **Cross-repo**: Issues routed via `.beads/routes.jsonl` pattern rules. External deps tracked as `external:<repo>/<id>`. `bd hydrate` pulls related issues.

### Communication Channels
| Channel | Mechanism |
|---------|-----------|
| Issue fields | `bd update --notes/--design/--acceptance` |
| Comments | `bd comment add` — threaded discussion |
| Labels | Status signaling (`needs-review`, `blocked`, `ready`) |
| Pins/Hooks | Direct work assignment to named agent |
| Reservations | `bd reserve <file> --for <agent>` — exclusive file lock |
| Issue locks | `bd lock <id> --for <agent>` — exclusive issue lock |
| Dolt remote | `bd dolt push/pull` — shared database sync |
| `discovered-from` deps | Provenance tracking for work found during execution |

### Shared State
All state stored in shared Dolt database. No message queue, no event bus, no direct agent-to-agent channel. **Database-as-shared-memory** pattern with hash-based IDs for collision prevention.

### Coordination Pattern
**Database-as-shared-memory + ZFC (Zero Framework Cognition)**. Go code handles state transitions, SQL queries, dependency graphs. All cognitive decisions delegated to LLM agents. Agents coordinate by reading and writing issue state in Dolt, not by sending messages directly.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | High | Layered progressive-disclosure context loading; `bd prime` live CLI injection; compaction-survival via notes fields; SessionStart + PreCompact hooks |
| Model | None | No model-specific patterns |
| Prompt | Medium | Repetition-as-enforcement for critical constraints; ZFC principle (cognitive logic in prompts, not code) |
| Tools | High | `bd` CLI as primary agent tool; MCP server integration; 28+ slash commands; hook-based lifecycle management |
| Intent | High | Explicit goal encoding via issue fields; dependency graph encodes task relationships; `bd ready` surfaces intent-aligned next work |
| Orchestration | High | Fan-out/fan-in via epic sub-issues; coordinator/worker pattern via pins; cross-repo routing via `routes.jsonl` |
| Evaluation | Medium | `bd doctor` orphan detection; `make lint && make test` quality gates; gate-based verification (CI gates, human gates) |
| Sandboxing | Low | Maintainer vs contributor routing isolation; `~/.beads-planning` contributor sandbox |
| Governance | High | Repetition-based constraint enforcement; hook-based safety nets; Witness heartbeat monitoring; pre-commit contributor protection; `bd rules audit` contradiction detection |
| Agent Design | High | Agent bead state machine; role beads for capability definition; task-agent persona file; heartbeat-based liveness; Witness external monitoring |

### Findings Candidates

1. **Database-as-shared-memory coordination** (Orchestration) — Agents coordinate exclusively through a shared Dolt database rather than message passing. Hash-based IDs prevent collision. Dolt's cell-level merge handles concurrent writes. This eliminates the need for a coordination framework or message bus.
→ Promoted to [[database-as-shared-memory-coordination]] on 2026-04-19

2. **Live CLI injection via hooks** (Context Engineering) — `bd prime` generates context from the live CLI binary at session start, ensuring context always matches the installed version. ADR-0001 makes this the canonical source of truth, explicitly prohibiting duplication in SKILL.md.
→ Skipped: niche to beads CLI, existing hook findings cover the general pattern on 2026-04-19

3. **Semantic memory decay compaction** (Context Engineering) — Closed tasks are summarized rather than deleted, preserving context while reducing noise. Combined with compaction-survival mechanics (notes fields persist through context compaction).
→ Promoted to [[semantic-memory-decay-compaction]] on 2026-04-19

4. **Repetition-as-enforcement governance** (Governance) — Critical constraints deliberately repeated across 3+ files to ensure coverage regardless of which file an agent reads. This is a conscious design choice, not duplication debt.
→ Skipped: covered by rationalization-prevention-pattern.md on 2026-04-19

5. **Agent state machine with Witness monitoring** (Agent Design) — Agent beads are first-class issue types with a formal state machine (idle → spawning → running → done/stuck/dead/stopped). External Witness monitors heartbeats and can set `dead` state. Agents cannot set `dead` themselves — separation of monitoring from execution.
→ Promoted to [[agent-state-machine-with-witness-monitoring]] on 2026-04-19

6. **Async gate taxonomy** (Orchestration) — Typed gates (timer, GitHub run, GitHub PR, human) with polling evaluation. Enables agents to pause and resume based on external conditions without blocking the session.
→ Skipped: covered by gsd-gates-taxonomy-four-canonical-types.md on 2026-04-19

7. **ZFC (Zero Framework Cognition)** (Agent Design) — Architectural principle keeping all cognitive/heuristic logic in LLM prompts, not in Go code. Code handles state transitions and data flow; LLMs handle decisions. Explicit constraint: "No hardcoded sequential logic in AI decision code."
→ Promoted to [[zero-framework-cognition-zfc]] on 2026-04-19

8. **Cross-repo issue routing** (Orchestration) — `.beads/routes.jsonl` enables pattern-based routing of issues across repos. `bd hydrate` pulls related issues from other repos. External dependencies tracked as `external:<repo>/<id>`.
→ Promoted to [[cross-repo-issue-routing]] on 2026-04-19

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-19 | v1.0.2 | All 5 | Initial analysis |
