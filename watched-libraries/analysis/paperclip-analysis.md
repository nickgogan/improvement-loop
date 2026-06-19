---
title: "Paperclip -- Structural Analysis"
id: "paperclip-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
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
  - "paperclip"
analyzed_version: "v2026.403.0"
analyzed_date: "2026-04-08"
repo_url: "https://github.com/paperclipai/paperclip"
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
| Total files | 1,462 |
| Total directories | 200 |
| TypeScript files | 817 (55.9%) |
| TSX files (React) | 207 (14.2%) |
| Markdown files | 184 (12.6%) |
| JSON files | 92 |
| SQL files | 53 |
| SVG files | 19 |
| Shell scripts | 19 |
| PNG files | 14 |
| MJS files | 14 |
| YAML/YML files | 14 |
| MD-to-code ratio | **0.18:1** (code dominant — full-stack application) |
| Max directory depth | 7 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Dev/maintainer skills (SKILL.md) | 6 | `.agents/skills/` |
| Product skills (SKILL.md) | 4 | `skills/`, `.claude/skills/` |
| Onboarding assets | 6 | `server/src/onboarding-assets/` (CEO: AGENTS, SOUL, HEARTBEAT, TOOLS; default: AGENTS) |
| Product/strategy docs | ~25 | `doc/` (SPEC, PRODUCT, GOAL, DEVELOPING, DATABASE, etc.) |
| Release notes | 6 | `releases/` |
| User-facing docs | ~40 | `docs/` (adapters, API, CLI, deploy, guides, specs, etc.) |
| Package changelogs/READMEs | ~20 | `packages/*/` |
| Skill references | ~8 | `.agents/skills/*/references/`, `skills/*/references/` |
| Project files | ~5 | Root (README, CONTRIBUTING, AGENTS.md, adapter-plugin.md) |
| Plans | ~10 | `doc/plans/` |
| Other | ~54 | Various |
| **Total** | **~184** |

Key insight: Paperclip is a full-stack application (Express API + React UI + Drizzle ORM + multi-adapter orchestration). The markdown composition reflects a production system: onboarding assets for deployed agents (SOUL.md, AGENTS.md), coordination skills for the Paperclip API, and extensive strategic/product documentation.

### Directory Naming Conventions
Kebab-case throughout. Organization:
- `server/` (Express API + orchestration)
- `ui/` (React + Vite)
- `packages/` (NPM workspace packages: db, shared, adapters, plugins, mcp-server)
- `skills/` (user-facing product skills)
- `.agents/skills/` (internal maintainer skills)
- `doc/` (product/strategic docs)
- `docs/` (user-facing documentation)

### Top-Level Structure
```
.
├── .agents/              # Internal maintainer skills (6)
│   └── skills/           # company-creator, create-agent-adapter, doc-maintenance, pr-report, release-changelog, release
├── .claude/              # Claude-specific skills (1)
│   └── skills/           # design-guide
├── cli/                  # CLI package (paperclipai)
├── doc/                  # Product/strategic docs (SPEC, GOAL, PRODUCT, etc.)
│   ├── plans/            # Dated plan documents
│   ├── plugins/          # Plugin architecture docs
│   └── spec/             # Detailed spec sections
├── docker/               # Docker configs (openclaw-smoke, quadlet, untrusted-review)
├── docs/                 # User-facing documentation
├── evals/                # Evaluation framework (promptfoo)
├── packages/
│   ├── adapter-utils/    # Shared adapter utilities
│   ├── adapters/         # 7 adapters (claude-local, codex-local, cursor-local, gemini-local, openclaw-gateway, opencode-local, pi-local)
│   ├── db/               # Drizzle ORM schema + migrations (53 SQL files)
│   ├── mcp-server/       # MCP server implementation
│   ├── plugins/          # Plugin SDK + examples
│   └── shared/           # Shared types, constants, validators
├── server/               # Express API + orchestration
│   └── src/onboarding-assets/  # Agent workspace templates (CEO, default)
├── skills/               # Product skills (4)
│   ├── paperclip/        # Main coordination skill
│   ├── paperclip-create-agent/
│   ├── paperclip-create-plugin/
│   └── para-memory-files/  # PARA-based file memory
├── tests/                # E2E + release smoke tests
└── ui/                   # React + Vite board UI
```

### Notable Structural Patterns
1. **Full-stack agent company**: Express API + React UI + PostgreSQL (Drizzle ORM). This is a production SaaS product, not a framework.
2. **Multi-adapter architecture**: 7 adapters (claude-local, codex-local, cursor-local, gemini-local, openclaw-gateway, opencode-local, pi-local) enabling agents to run on different AI backends.
3. **Onboarding assets as workspace templates**: CEO and default agent templates define identity (SOUL.md), rules (AGENTS.md), proactive tasks (HEARTBEAT.md), and tools.
4. **53 SQL migration files**: Substantial database schema for issue tracking, agent management, approvals, budgets, and company governance.
5. **Plugin SDK with examples**: Formal plugin system (SDK + create-paperclip-plugin scaffolder + 3 example plugins).

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `AGENTS.md` (root) | LLM | Global | Auto-loaded | Constraints/Rules | Repo guidelines: architecture, engineering rules, DB workflow, verification, PR requirements, definition of done |
| `server/src/onboarding-assets/ceo/SOUL.md` | LLM | Task | Injected | Identity/Persona | CEO persona: strategic posture, P&L ownership, delegation emphasis, voice/tone |
| `server/src/onboarding-assets/ceo/AGENTS.md` | LLM | Task | Injected | Constraints/Rules + Workflow | CEO workspace rules: mandatory delegation, chain of command, memory system integration |
| `server/src/onboarding-assets/ceo/HEARTBEAT.md` | LLM | Task | Injected | Workflow/Process | CEO heartbeat checklist: identity check, planning, approvals, assignments, delegation, fact extraction |
| `server/src/onboarding-assets/ceo/TOOLS.md` | LLM | Task | Injected | Tool Usage | CEO tool notes (placeholder) |
| `server/src/onboarding-assets/default/AGENTS.md` | LLM | Task | Injected | Constraints/Rules | Default agent workspace rules |
| `skills/paperclip/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage + Workflow | Main coordination skill: heartbeat procedure, API reference, governance rules (~500 lines) |
| `skills/para-memory-files/SKILL.md` | LLM | Tool | Auto-loaded | Memory/State | PARA-based file memory: 3-layer system, knowledge graph, daily notes, tacit knowledge |
| `skills/paperclip-create-agent/SKILL.md` | LLM | Tool | Auto-loaded | Workflow/Process | Agent hiring workflow |
| `skills/paperclip-create-plugin/SKILL.md` | LLM | Tool | Auto-loaded | Tool Usage | Plugin creation workflow |
| `.agents/skills/*/SKILL.md` (6 files) | LLM | Tool | Auto-loaded | Workflow/Process | Internal skills: company-creator, create-agent-adapter, doc-maintenance, pr-report, release-changelog, release |
| `.claude/skills/design-guide/SKILL.md` | LLM | Tool | Auto-loaded | Constraints/Rules | UI design system guide |
| `doc/SPEC-implementation.md` | Both | Global | Referenced | Workflow/Process | V1 build contract (~28K bytes) |
| `doc/SPEC.md` | Both | Global | Referenced | Workflow/Process | Long-horizon product context (~27K bytes) |
| `doc/GOAL.md` | Both | Global | Referenced | Identity/Persona | Product mission and vision |
| `doc/PRODUCT.md` | Both | Global | Referenced | Workflow/Process | Product design and features |

Sampling notes: Read root AGENTS.md in full. Read CEO onboarding assets in full (SOUL.md, AGENTS.md, HEARTBEAT.md). Read main paperclip skill in full. Read para-memory-files skill (100 lines). Classified remaining skills by pattern.

### Context Loading Strategy
**Heartbeat-driven context assembly with onboarding-asset injection:**

1. **Agent workspace creation**: When a new agent is created, onboarding assets (SOUL.md, AGENTS.md, HEARTBEAT.md, TOOLS.md) are copied into the agent's workspace directory. These define the agent's identity and operating rules.
2. **Skill loading**: The `paperclip` skill (~500 lines) is the primary coordination skill, loaded when agents interact with the Paperclip API. It defines the complete heartbeat procedure (9 steps), API endpoints, governance rules, and comment style.
3. **Memory skill**: `para-memory-files` defines a 3-layer memory system (knowledge graph, daily notes, tacit knowledge) using PARA (Projects/Areas/Resources/Archives). Agents are instructed to use this skill for all memory operations.
4. **Heartbeat-driven context**: Each heartbeat, agents receive env vars (PAPERCLIP_AGENT_ID, PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON, etc.) that provide context without requiring full state reload. The `heartbeat-context` API endpoint provides compact issue state.

**Key pattern: Env-var context injection.** Instead of assembling context from files at startup, Paperclip injects execution context via environment variables (PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON, PAPERCLIP_WAKE_COMMENT_ID, PAPERCLIP_APPROVAL_ID, etc.). This is a third context loading mechanism distinct from file-based (GSD, BMAD) and hook-injected (Superpowers) approaches.

## 3. Workflow Topology

### Phases/Stages

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| **Heartbeat** | Timer/event | Agent checks inbox, picks work, executes, exits | No (autonomous) |
| **Task Checkout** | `POST /api/issues/{id}/checkout` | 409 Conflict or success | No (atomic) |
| **Execution** | Checkout success | Task completed or blocked | Per governance policy |
| **Review** | Status -> `in_review` | Reviewer approves or requests changes | Yes (reviewer agent or human) |
| **Approval** | Approval request created | Board approves or denies | Yes (mandatory board gate) |
| **Delegation** | CEO/manager creates subtask | Subtask assigned to report | No (chain of command) |

### Flow Diagram (ASCII)

```
┌──────────────────────┐
│   HEARTBEAT TRIGGER  │ <-- Timer, event, @-mention, comment, blocker-resolved
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  1. IDENTITY CHECK   │ GET /api/agents/me
│  2. APPROVAL FOLLOWUP│ (if PAPERCLIP_APPROVAL_ID set)
│  3. GET ASSIGNMENTS  │ GET inbox-lite
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  4. PICK WORK        │ in_progress > in_review > todo
│     (mention overrides│  Skip blocked w/o new context)
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  5. CHECKOUT         │ POST /checkout (atomic, 409 = stop)
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│  6. CONTEXT LOAD     │ GET heartbeat-context + comments
│  7. DO WORK          │ Use tools, write code, delegate
│  8. UPDATE STATUS    │ done/blocked/in_review + comment
└──────────┬───────────┘
           │
    ┌──────┴──────┐
    ▼             ▼
┌────────┐  ┌──────────┐
│  DONE  │  │ DELEGATE │──── Create subtask w/ parentId + goalId
└────────┘  └──────────┘

Org Chart (CEO hierarchy):
  CEO ──► CTO (code, bugs, features, infra)
      ──► CMO (marketing, content, growth)
      ──► UXDesigner (design, user research)
```

### Transition Mechanisms
- **Heartbeat-driven**: Agents wake on timer events, @-mentions, comment triggers, approval resolutions, blocker completions, and child task completions.
- **Atomic checkout**: `POST /checkout` with `expectedStatuses` provides optimistic locking. 409 Conflict means another agent owns the task.
- **Status-based lifecycle**: `backlog -> todo -> in_progress -> in_review -> done` (or `blocked`, `cancelled`).
- **Execution policy stages**: Review and approval stages with `currentParticipant` routing. Decisions submitted through normal issue update route.
- **Wake reasons**: `issue_commented`, `issue_comment_mentioned`, `issue_blockers_resolved`, `issue_children_completed`.

### Parallelism
- **Multi-agent company**: Multiple agents run simultaneously, each with their own adapter (Claude, Codex, Cursor, etc.).
- **Concurrent heartbeats**: Different agents can be executing heartbeats concurrently on different tasks.
- **Checkout exclusion**: Atomic checkout prevents two agents from working on the same task simultaneously.
- **Cross-team delegation**: CEO delegates to CTO, CMO, UXDesigner -- each can work in parallel.

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Atomic checkout | Server API | Hard (409 Conflict) | Single-assignee task model -- only one agent can own a task |
| Budget hard-stop | Server API | Hard | Auto-pause at 100% budget. Above 80%, critical tasks only |
| Approval gates | Server API + UI | Hard | Board approval required for governed actions (spend, vendor, launch) |
| Chain of command | CEO AGENTS.md | Soft (LLM-read) | CEO -> CTO/CMO/UXDesigner routing rules |
| Activity logging | Server API | Hard | All mutating actions logged with run ID traceability |
| Company scoping | Server API + schema | Hard | Every entity scoped to a company; cross-company access prevented |
| PR template | `.github/PULL_REQUEST_TEMPLATE.md` | Soft | Thinking Path, What Changed, Verification, Risks, Model Used, Checklist |
| Definition of Done | `AGENTS.md` | Soft | Behavior matches spec, typecheck/tests/build pass, contracts synced, docs updated |
| Run audit trail | `X-Paperclip-Run-Id` header | Hard (enforced in skill) | Every API mutation includes run ID for traceability |
| Blocker dependencies | Server API | Hard | First-class `blockedByIssueIds` with automatic wake-on-resolution |

### Guardrail Patterns
1. **Atomic checkout with 409 exclusion**: Agents must checkout before working. If another agent owns the task, they get 409 Conflict and must stop. "Never retry a 409" is a hard rule. This prevents concurrent work on the same task.
2. **Budget hard-stop with auto-pause**: Agents are paused at 100% budget. Above 80%, they focus only on critical tasks. This is real resource governance, not advisory.
3. **Board approval gates**: Agents can create approval requests for board decisions (spend, vendor selection, launch). The board approves/denies through the UI. This is the human gate for consequential decisions.
4. **Run ID audit trail**: Every mutating API call requires `X-Paperclip-Run-Id` header. This creates a full audit trail linking actions to specific heartbeat runs.
5. **Blocked-task dedup**: Agents check if their most recent comment on a blocked task was a blocked-status update with no new comments since. If so, they skip the task entirely -- no repeated blocked comments.
6. **Execution policy stages**: Review and approval stages with designated participants. Only the current participant can advance the stage -- others get 422 rejection.

### Permission Model
- **Agent API keys**: Bearer tokens with company scoping. Agents cannot access other companies.
- **Board vs agent access**: Board has full control; agents have scoped access.
- **Chain of command**: CEO delegates to reports. Agents cannot self-assign unless explicitly @-mentioned.
- **Manager scope**: CEO can hire agents, set priorities, and approve/reject proposals.
- **Cross-team reassignment**: Agents cannot cancel cross-team tasks -- must reassign to manager with a comment.

## 5. Cross-Agent Protocol

### Agent Roster (Company Structure)
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| CEO | `onboarding-assets/ceo/` | Strategy, delegation, hiring, unblocking, approvals | Board (humans), CTO, CMO, UXDesigner via Paperclip API |
| CTO | Created via `paperclip-create-agent` | Code, bugs, features, infra, devtools | CEO, other engineers via task delegation |
| CMO | Created via `paperclip-create-agent` | Marketing, content, social, growth, devrel | CEO |
| UXDesigner | Created via `paperclip-create-agent` | Design, user research, design-system | CEO |

**Multi-adapter support:**
| Adapter | Package | AI Backend |
|---------|---------|------------|
| claude-local | `packages/adapters/claude-local/` | Claude Code CLI |
| codex-local | `packages/adapters/codex-local/` | OpenAI Codex |
| cursor-local | `packages/adapters/cursor-local/` | Cursor |
| gemini-local | `packages/adapters/gemini-local/` | Google Gemini |
| openclaw-gateway | `packages/adapters/openclaw-gateway/` | OpenClaw |
| opencode-local | `packages/adapters/opencode-local/` | OpenCode |
| pi-local | `packages/adapters/pi-local/` | Pi |

### Handoff Mechanisms
1. **Issue-based handoff (primary)**: Work is assigned via issues with status transitions. Agents pick up assigned tasks during heartbeats. Delegation creates subtasks with `parentId` linking.
2. **Comment-driven communication**: Agents communicate through issue comments. @-mentions trigger heartbeats. Comments follow strict style: status line + bullets + links.
3. **Approval workflow**: Agents create approval requests. Board approves/denies. Approval resolution triggers agent wake with `PAPERCLIP_APPROVAL_ID`.
4. **Blocker-based dependency**: `blockedByIssueIds` creates formal dependencies. When all blockers resolve, dependent agent is woken automatically.
5. **Workspace inheritance**: Subtasks inherit execution workspace from parent. Non-child follow-ups use `inheritExecutionWorkspaceFromIssueId` for workspace continuity.

### Shared State
- **PostgreSQL database**: Issues, agents, companies, approvals, budgets, routines, activity logs. Full relational schema with 53 migration files.
- **Agent workspaces**: Each agent has its own workspace directory with SOUL.md, AGENTS.md, HEARTBEAT.md, TOOLS.md, and PARA memory folders.
- **Company-scoped data**: All entities belong to a company. No cross-company data access.
- **Run audit trail**: Every heartbeat run has a unique ID. All mutations are linked to runs.

### Coordination Patterns
**Hierarchical delegation with API-mediated coordination.** The CEO sits at the top, delegating to functional reports (CTO, CMO, UXDesigner). All coordination flows through the Paperclip API -- issue creation, checkout, status updates, comments, approvals. Agents never communicate directly; the API is the message bus.

This is the closest to a real org chart of any analyzed repo. GSD uses hub-and-spoke with workflow orchestrators; BMAD uses user-mediated skill invocation; OpenClaw uses gateway-mediated routing. Paperclip models a corporate hierarchy with formal delegation, budget governance, and approval workflows.

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Env-var context injection (PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON, etc.). Heartbeat-context API endpoint for compact state. PARA-based file memory (knowledge graph + daily notes + tacit knowledge). Incremental comment loading (cursor-based). Wake payload JSON for inline context on comment-driven wakes. |
| Model | Medium | Multi-adapter architecture (7 adapters: Claude, Codex, Cursor, Gemini, OpenClaw, OpenCode, Pi). Model Used required in PR template. |
| Prompt | Medium | CEO persona in SOUL.md with specific voice/tone rules. Heartbeat procedure as structured prompt (9 steps). Comment style rules (status + bullets + links). |
| Tools | **High** | Paperclip API as primary tool (40+ endpoints). MCP server implementation. Plugin SDK with scaffolder and examples. qmd for semantic memory recall. Multi-adapter tool delegation. |
| Intent | **High** | CEO mandatory delegation ("You MUST delegate work rather than doing it yourself"). Chain of command routing rules. Goal ancestry (goalId on all tasks). Budget-aware prioritization (above 80%, critical only). |
| Orchestration | **High** | Hierarchical org chart (CEO -> CTO/CMO/UXDesigner). Heartbeat-driven execution cycle. Atomic checkout exclusion. Issue dependency graph with auto-wake. Execution policy stages (review -> approval). Multi-adapter parallel agent execution. Routines for recurring scheduled tasks. |
| Evaluation | Medium | Promptfoo eval framework in `evals/`. Untrusted PR review workflow (Docker-isolated). Bug-fix evidence bar in PR process. Self-test playbook for app-level validation. |
| Sandboxing | **High** | Docker-based untrusted PR review. Company-scoped data isolation. Agent workspace isolation. Budget hard-stop auto-pause. Atomic checkout preventing concurrent task access. Run ID audit trail for traceability. |
| Governance | **High** | Budget governance with hard-stop at 100%. Board approval gates for consequential decisions. Atomic checkout exclusion. Run audit trail. Chain of command enforcement. Activity logging for all mutations. Cross-team task rules (never cancel, reassign to manager). Blocked-task dedup to prevent noise. Company-scoping as hard boundary. |
| Agent Design | **High** | CEO persona with SOUL.md (strategic posture, voice/tone). Mandatory delegation rule ("Do NOT write code, implement features, or fix bugs yourself"). PARA-based memory system (knowledge graph, daily notes, tacit knowledge with decay). Heartbeat as execution model (wake, check, work, exit). Onboarding assets as agent identity templates. Agent hiring via skill (paperclip-create-agent). |

### Findings Candidates

1. **Hierarchical org-chart orchestration** (Orchestration, Governance) -- Paperclip models a corporate hierarchy: CEO delegates to CTO/CMO/UXDesigner, each can further delegate. All coordination via API (issue creation, checkout, status, comments). Formal chain of command with escalation. Compare to GSD's hub-and-spoke and BMAD's user-mediated model.
→ Skipped: duplicate of [[org-chart-hierarchy-as-scalable-claude-code]] on 2026-04-19

2. **Budget governance with hard-stop** (Governance, Sandboxing) -- Real resource governance: auto-pause at 100% budget, critical-only above 80%. Per-agent budget tracking with billing codes for cross-team work. This is production-grade resource management for AI agents, not advisory limits.
→ Promoted to [[budget-governance-with-hard-stop]] on 2026-04-08

3. **Heartbeat execution model** (Agent Design, Orchestration) -- Agents run in heartbeat cycles: wake on trigger, check inbox, pick work, checkout, execute, update, exit. Not a continuous loop -- discrete, short execution windows. Wake reasons provide context: comment, @-mention, approval, blocker-resolved, children-completed. Compare to OpenClaw's continuous agent loop.
→ Promoted to [[heartbeat-execution-model]] on 2026-04-08

4. **Atomic checkout with 409 exclusion** (Orchestration, Governance) -- Single-assignee task model enforced by atomic checkout. 409 Conflict = stop immediately, never retry. Prevents concurrent work on the same task without distributed locking complexity. Simple, effective coordination primitive.
→ Promoted to [[atomic-checkout-with-409-exclusion]] on 2026-04-08

5. **PARA-based file memory** (Context Engineering, Agent Design) -- Three-layer memory: (1) Knowledge graph in PARA folders with atomic YAML facts and supersession, (2) Daily notes as raw timeline, (3) Tacit knowledge (MEMORY.md) for user operating patterns. Includes memory decay rules, weekly synthesis, and qmd semantic recall. More structured than OpenClaw's flat memory files.
→ Promoted to [[para-based-file-memory]] on 2026-04-08

6. **Env-var context injection** (Context Engineering) -- Instead of assembling context from files at startup, Paperclip injects execution context via environment variables (PAPERCLIP_TASK_ID, PAPERCLIP_WAKE_REASON, PAPERCLIP_WAKE_COMMENT_ID, etc.). Combined with heartbeat-context API for compact state. This is a third context loading mechanism distinct from file-based and hook-injected approaches.
→ Promoted to [[env-var-context-injection]] on 2026-04-08

7. **CEO mandatory delegation pattern** (Agent Design, Intent) -- The CEO persona is explicitly told "You MUST delegate work rather than doing it yourself" and "Do NOT write code, implement features, or fix bugs yourself." This is intent engineering at the architectural level -- defining what the agent should NOT do is as important as what it should do.
→ Promoted to [[ceo-mandatory-delegation-pattern]] on 2026-04-08

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v2026.403.0 | all | Initial analysis. 1,462 files, 184 MD, 10 skills, 7 adapters, 53 SQL migrations. Hierarchical org-chart orchestration with budget governance. |
