---
title: "Archon -- Structural Analysis"
id: "archon-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-09"
updated: "2026-07-13"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "archon"
analyzed_version: "v0.5.0"
analyzed_date: "2026-07-13"
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
- **Version analyzed:** v0.5.0 (commit dad62d8, 2026-07-13)
- **Date:** 2026-07-13
- **Spectrum position:** cherry-pick
- **Supersedes:** v0.3.2 analysis (2026-04-09). Re-run triggered by /watch-upstream refresh (registry Upstream Delta v0.3.2 → v0.5.0).

## What Archon Now Demonstrates That It Didn't at v0.3.2

Written for the named-deps gap-check (Archon vs the engine's agentic-OS direction-note asks).

1. **First-class Ralph loops as an engine primitive, not a prompt idiom.** The `loop:` node config is now a complete loop-anatomy schema: `until` (completion-signal string), `until_bash` (deterministic exit-0 check as an alternative/companion to signal matching), `max_iterations` hard stop, `fresh_context` per-iteration session reset, `interactive: true` + `gate_message` (pause every iteration for human input via `/workflow approve`), and `$LOOP_PREV_OUTPUT` (cleaned prior-iteration output bridged into fresh-context iterations). The engine emits `loop_iteration_started/completed/failed` events and reports `loopIterations` in run metrics — loop progress is observable in the UI, not opaque. `archon-ralph-dag.yaml` (28k) is a full production Ralph pipeline: detect input → generate prd.md/prd.json → validate → fresh-context loop implementing one story per iteration → PR.
2. **A matured workflow UI stack.** The run-centric console is now the **default UI at `/`** (classic UI re-rooted under `/legacy` for a deprecation window): RunsPage (monitoring hub), RunDetailPage (step-by-step execution viewer), plus a drag-and-drop workflow builder (`experiments/console/builder/` with flow/yaml/validation/variants modules) and an `archon-workflow-builder` default workflow (scan codebase → extract intent JSON → generate YAML → validate → save) — workflow authoring exists as both a UI and an AI workflow.
3. **A genuine multi-provider abstraction.** New `packages/providers` (11th package) with a typed provider registry: core Claude + Codex, community Pi (~20 LLM backends), OpenCode (embedded local runtime), and GitHub Copilot. Capabilities are declared per provider and are **tiered, not boolean** (`structuredOutput: 'enforced' | 'best-effort' | false`; `nativeTools`; `sessionResume`), and the engine branches on them (validate-and-reask loop for best-effort providers; native `manage_run` tool vs prompt-section fallback). Per-node MCP server config (`mcp/config.ts`) extends the Codex/MCP seam.
4. **Identity, auth, and attribution as an architectural layer.** GitHub App auth (per-installation ~1h tokens, loopback-only `/internal/git-credential` helper, user-attribution on comments/commits) replaces shared PATs; `users`/`user_identities` tables unify identity across platforms; per-user encrypted credential vaults (AES-256-GCM) and per-user AI prefs form the highest-precedence config layer; execution runs as the **acting user** (message sender / run starter).
5. **Governance escalated from convention to product identity.** Self-description changed from "single-developer tool" to "self-hostable, **governed** agentic automation engine" — approval gates, audit trails, `requires: [github]` pre-flight blocks, fail-closed structured output, server-side API auth gate, and a committed `direction.md` that drives automated PR triage.
6. **Counter-signal on context layering:** the 11-file `.claude/rules/` domain-rules layer was **deleted**; everything consolidated into a 979-line `CLAUDE.md` plus a root `AGENTS.md` near-mirror (964 lines) for non-Claude harnesses — with observable drift between the two.

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | v0.5.0 | v0.3.2 |
|--------|--------|--------|
| Total files | 1,262 | 745 |
| Total directories | 194 | 139 |
| Markdown files | 289 | 271 |
| TypeScript files (.ts) | 632 | 278 |
| TSX files (.tsx) | 153 | 70 |
| YAML files (.yaml + .yml) | 66 | 22 |
| JSON files | 30 | 27 |
| SQL files | 24 | 22 |
| Shell scripts (.sh) | 14 | 9 |
| MD-to-code ratio | 0.37:1 (289 MD : 785 TS/TSX) | 0.78:1 |
| Max directory depth | 8 | 8 |

The repo grew ~70% in file count in three months, and code grew much faster than markdown — MD:code ratio halved. Archon at v0.5.0 is decisively a **platform codebase with an operational markdown layer**, no longer near markdown/code parity.

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skills (SKILL.md + guides/refs/cookbooks) | 92 | `.claude/skills/` (14 skills, was 7) |
| Documentation site | 64 | `packages/docs-web/src/content/docs/` |
| Commands/prompts (Archon runtime) | 45 | `.archon/commands/` (36 defaults + docs) |
| Claude Code commands | 19 | `.claude/commands/` (incl. `prime-*` context loaders) |
| GitHub Copilot prompts | 14 | `.github/prompts/` |
| Agent definitions | 13 + 3 | `.claude/agents/`, `.github/agents/` |
| PRPs (issue plans) | 12 | `.claude/PRPs/` |
| Web package docs (experiments READMEs) | 5 | `packages/web/` |
| Workshop/onboarding | 4 | `.claude/workshop/` |
| Architecture docs | 4 | `.claude/docs/` |
| Maintainer standup (north-star + template) | 2 | `.archon/maintainer-standup/` |
| Root context/human docs | 6 | `CLAUDE.md`, `AGENTS.md`, `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md` |
| YAML workflows | 20 | `.archon/workflows/defaults/` |

### Directory Naming Conventions
- **kebab-case** throughout, unchanged.
- **Monorepo workspaces** now 11 packages: `packages/{cli,core,workflows,git,isolation,paths,providers,adapters,server,web,docs-web}` — `providers` is new.
- **Context namespace separation** persists: `.claude/` (Claude Code), `.archon/` (Archon runtime), `.github/` (Copilot) — but the `.claude/rules/` sub-namespace was removed.
- New top-level items since v0.3.2: `.archon/maintainer-standup/`, `.archon/scripts/` (named scripts for `script:` nodes), `examples/workflows/`, `.husky/` (git hooks).

### Top-Level Structure
```
.
├── .archon/                    # Archon platform config + defaults
│   ├── commands/defaults/      # 36 default command files
│   ├── workflows/defaults/     # 20 default workflow YAMLs
│   ├── scripts/                # Named scripts for script: nodes (bun/uv)
│   └── maintainer-standup/     # Daily-brief workflow config (direction.md north-star)
├── .claude/                    # Claude Code context layer
│   ├── PRPs/                   # Issue implementation plans
│   ├── agents/                 # 13 specialist agent definitions
│   ├── commands/               # 19 slash commands (incl. prime-* context loaders)
│   ├── docs/                   # 4 architecture docs
│   ├── skills/                 # 14 skills (was 7)
│   └── workshop/               # Onboarding guides
├── .github/                    # GitHub integration (3 Copilot agents, 14 prompts, CI)
├── .husky/                     # Git hooks
├── AGENTS.md                   # Root cross-harness context mirror (NEW, 964 lines)
├── CLAUDE.md                   # Master context (979 lines; absorbed the rules layer)
├── auth-service/  deploy/  homebrew/  migrations/  scripts/  assets/
├── examples/workflows/         # Example workflow YAMLs (NEW)
└── packages/                   # Monorepo (11)
    ├── providers/              # NEW — AI agent providers + registry (core + community)
    ├── adapters/               # chat/ (Slack, Telegram), forge/ (GitHub), community/ (Discord)
    ├── cli/ core/ workflows/ git/ isolation/ paths/ server/ web/ docs-web/
```

### Code Surface Outline (optional — ast-grep)
Skipped — ast-grep unavailable on this machine (repo is well above the 200-code-file gate; the outline pass would have helped).

### Notable Structural Patterns
1. **Rules-layer collapse.** The 11-file path-scoped `.claude/rules/` layer (v0.3.2's second context tier) is gone. Domain constraints now live inline in `CLAUDE.md` (780 → 979 lines). A deliberate consolidation from layered to monolithic context.
2. **Dual root context files.** `CLAUDE.md` + `AGENTS.md` (new) — the AGENTS.md mirror serves Codex/OpenCode/Copilot harnesses that read the emerging `AGENTS.md` convention. The two have drifted: CLAUDE.md carries the new "governed agentic automation engine" positioning and multi-user auth docs; AGENTS.md still opens with the older "single-developer tool" framing.
3. **Provider layer extraction.** All AI-SDK dependencies moved to `packages/providers`; `@archon/providers/types` is a zero-SDK-dep contract subpath that `@archon/workflows` imports. Community providers live under `community/` and register with `builtIn: false`.
4. **Generated-bundle discipline.** Defaults (commands, workflows, skill, schema, Pi vendor map) are compile-time embedded via generated files; `bun run validate` runs four staleness checks (`check:bundled*`, `check:pi-vendor-map`) that fail CI if regeneration was skipped.
5. **Skills as the dominant markdown surface.** 92 of 289 md files are skill content; skills doubled (7 → 14: + `manage-run`, `replicate-issue`, `rulecheck`, `save-task-list`, `test-release`, `triage`, `validate-ui`).

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Constraints/Rules + Workflow/Process | 979-line master context: principles, product direction, architecture, 18-table DB schema, API surface, testing/mock-isolation rules. Absorbed the former rules layer. |
| `AGENTS.md` | LLM | Global | Auto-loaded (non-Claude harnesses) | Constraints/Rules + Workflow/Process | 964-line near-mirror of CLAUDE.md for Codex/OpenCode/Copilot; partially stale vs CLAUDE.md (older positioning). |
| `.claude/agents/*.md` (13) | LLM | Task | Injected | Identity/Persona | Same 13-specialist roster as v0.3.2 (code-reviewer, triage-agent, rulecheck-agent, silent-failure-hunter, etc.). |
| `.claude/skills/*/SKILL.md` (14) | LLM | Task | Injected | Workflow/Process + Tool Usage | 7 new since v0.3.2. New frontmatter features in use: `disable-model-invocation`, `context: fork`, `agent:` (skill→agent binding), skill-level `hooks:` (Stop-hook prompt evaluator in `save-task-list`), `allowed-tools` scoping (`Bash(gh *)` in `triage`). |
| `.claude/commands/*.md` (19) | LLM | Task | Injected | Workflow/Process | Includes `prime`, `prime-backend`, `prime-frontend`, `prime-isolation`, `prime-workflows` — explicit per-domain context loaders replacing the auto-loaded rules layer with on-demand priming. |
| `.claude/docs/*.md` (4) | LLM | Project | Referenced | Workflow/Process | Architecture deep-dive, adapter guide, isolation guide, YAML reference. |
| `.archon/commands/defaults/` (36) | LLM | Task | Injected (workflow `command:` nodes) | Workflow/Process | Runtime prompt library shipped with the engine; repo overrides by filename. |
| `.archon/workflows/defaults/` (20 YAML) | LLM (prompts inside YAML) | Task | Injected (engine) | Workflow/Process | DAG definitions; heavy inline prompt engineering (ralph-dag 28k, piv-loop 28k, create-issue 27k). |
| `.archon/maintainer-standup/direction.md` | LLM | Project | Referenced (by standup workflow) | Constraints/Rules | Committed north-star ("what Archon IS / IS NOT") consumed by the daily standup workflow to classify PRs P1–P4 and cite decline clauses. |
| `.archon/maintainer-standup/profile.md` (gitignored) | LLM | Task | Referenced | Memory/State | Per-maintainer config; `state.json` + `briefs/` are run-to-run carry-over memory. |
| `.github/agents/*.agent.md` (3) | LLM | Task | Injected | Identity/Persona | Copilot mirrors of analyst/explorer/researcher. |
| `.github/prompts/*.prompt.md` (14) | LLM | Task | Injected | Workflow/Process | Copilot prompt files. |
| `packages/docs-web/` (64) | Human | Global | N/A | Human docs | Starlight docs site incl. brand foundation. |

### Classification Key
Standard key (Audience: LLM/Human/Both; Scope: Global/Project/Task/Tool; Mechanism: Auto-loaded/Chain-loader/Hook-injected/Referenced/Injected; Content Type: Identity/Persona, Constraints/Rules, Workflow/Process, Tool Usage, Memory/State).

### Sampling Notes
Read in full: `CLAUDE.md`, `AGENTS.md` (first 30 lines + diff spot-checks), `loop.ts` schema, `archon-ralph-dag.yaml` (head), `archon-adversarial-dev.yaml` (head), `archon-test-loop-dag.yaml`, `archon-workflow-builder.yaml` (head), 7 new SKILL.md headers, `maintainer-standup/README.md` + `direction.md` (head), `App.tsx` routing. Classified by pattern: 13 agents (unchanged roster from v0.3.2 full reads), 36 command defaults, 14 Copilot prompts, docs-web content.

### Context Loading Strategy
**Consolidated two-file global layer + on-demand priming + injected specialists:**

1. **Global layer**: `CLAUDE.md` (Claude Code) and `AGENTS.md` (other harnesses) — both monolithic and self-contained. The v0.3.2 three-tier strategy (CLAUDE.md → path-scoped rules → agents) became two-tier: the auto-loaded rules layer was replaced by (a) inline CLAUDE.md sections and (b) **explicit `prime-*` commands** that load domain context on demand. This trades always-on token cost for user/agent-initiated context assembly.
2. **Specialist layer**: `.claude/agents/` unchanged; skills now **bind to agents** (`agent:` frontmatter in `rulecheck`, `triage` skills) — a skill is the invocation surface, the agent definition is the persona/constraints, and `context: fork` isolates the run from the main conversation.
3. **Runtime layer**: workflow YAML prompts + `.archon/commands/` + home-scoped `~/.archon/{workflows,commands,scripts}` with load priority bundled < global < project.
4. **Cross-platform mirrors**: `.github/agents` + `.github/prompts` unchanged; `AGENTS.md` extends the mirroring pattern to the root context file itself.

---

## 3. Workflow Topology

### Phases/Stages

#### Platform Workflow Engine (DAG)
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Node resolution | Workflow invocation (CLI/chat/web/console) | Topological layer complete | No |
| DAG execution | `executeWorkflow()` | Terminal nodes complete/failure | No (unless `approval:`) |
| Loop iteration | `loop:` node | `until` signal detected, `until_bash` exits 0, or `max_iterations` | Optional — `interactive: true` pauses **every** iteration for `/workflow approve` (with `gate_message`) |
| Approval gate | `approval:` node | User approves/rejects; `capture_response: true` stores comment as `$<id>.output` | **Yes** |
| Pre-flight identity gate | Workflow-level `requires: [github]` | Originating user has connected GitHub identity | **Yes** (hard block before any worktree/AI cost) |
| Resume | `/workflow resume <id>` | Re-runs failed run, skipping completed nodes | No |

Node types now: `command`, `prompt`, `bash`, `loop`, `approval`, `cancel`, `script` (inline TS/Python or named script via bun/uv) — `cancel` and `script` are new since v0.3.2. Any node can declare `output_type` to have the executor write typed output sidecars (`$ARTIFACTS_DIR/nodes/<id>.md` + `<id>.meta.json`) so downstream nodes locate output by type instead of guessing filenames.

#### Loop Node Anatomy (matured — the Ralph primitive)
| Element | Mechanism |
|---------|-----------|
| Completion signal | `until:` string matched in AI output (e.g. `<promise>COMPLETE</promise>`) |
| Deterministic check | `until_bash:` optional script after each iteration; exit 0 = complete |
| Budget | `max_iterations` (required); exceeding fails the node; `retry` explicitly unsupported on loop nodes |
| Context policy | `fresh_context: true` starts a new session per iteration; `$LOOP_PREV_OUTPUT` bridges the previous iteration's cleaned output into the fresh session |
| Human-in-loop | `interactive: true` + `gate_message`; `$LOOP_USER_INPUT` carries feedback from `/workflow approve <id> <text>` into the resumed iteration |
| Observability | `loop_iteration_started/completed/failed` events; `loopIterations` + summed token/cost totals in run metrics; `interactive_loop` pause type distinct from `approval` in run metadata |
| Resume semantics | Paused loop persists iteration counter + session id; resume continues at iteration N+1 |

#### Default Workflow Library (20 workflows; heavy churn since v0.3.2)
| Workflow | Pattern | Notable |
|----------|---------|---------|
| `archon-ralph-dag` (28k) | detect input → generate PRD (md+json) → validate → **fresh-context Ralph loop, one story/iteration** → PR | Structured-output classification nodes (`output_format`), small-model routing (`model: small`) for detection |
| `archon-adversarial-dev` (15k) | Planner → state-machine loop alternating **Generator vs Evaluator** with 7/10 pass thresholds | GAN-inspired; evaluator's job is to break the generator's work; cites Anthropic harness-design article |
| `archon-architect` (16k) | Architecture planning | New |
| `archon-workflow-builder` (10k) | scan codebase → intent JSON → generate YAML → validate → save | Workflow that authors workflows |
| `archon-refactor-safely` (23k) | Guarded refactoring | New |
| `archon-create-issue` (27k) | Issue creation pipeline | New |
| `archon-piv-loop` (28k) | plan → implement+validate loop | Massively expanded (3k → 28k) |
| `archon-fix-github-issue`, `archon-plan-to-pr`, `archon-idea-to-pr`, `archon-feature-development`, `archon-validate-pr`, `archon-interactive-prd`, `archon-assist` | Carried over | |
| `archon-smart-pr-review`, `archon-comprehensive-pr-review`, `archon-issue-review-full`, `archon-test-loop-dag`, `archon-remotion-generate`, `archon-resolve-conflicts` | New review/utility workflows | `test-loop-dag` is a minimal loop-node exemplar |

### Flow Diagram (ASCII)
```
User (Slack/Telegram/GitHub/Discord/CLI/Web console)
    │
    ▼
Platform Adapter (IPlatformAdapter) ── auth inside adapter; per-user identity resolved
    │
    ▼
Orchestrator handleMessage() ──► deterministic commands | AI router (tools: [])
    │                                                        │
    │                                    /invoke-workflow ◄──┘  (fallback: archon-assist)
    ▼
requires: [github] pre-flight gate ──► blocked message (no worktree/AI cost)
    │
    ▼
IsolationResolver (worktree per run; folder projects run in place)
    │
    ▼
DAG Executor (topological layers, Promise.allSettled)
  ┌─────────┐  ┌─────────┐  ┌──────────────────────────────┐
  │ command │  │ script  │  │ loop:                        │
  │ prompt  │  │ bash    │  │  iterate ── until/until_bash │──► loop_iteration_* events
  │ approval│  │ cancel  │  │  fresh_context / interactive │        │
  └─────────┘  └─────────┘  └──────────────────────────────┘        ▼
    │                                                     Console UI (/) — RunsPage hub,
    ▼                                                     RunDetailPage step viewer,
  Events + typed output sidecars + artifacts              clickable artifact paths
```

### Transition Mechanisms
- **AI routing** unchanged (structured `/invoke-workflow` parsing; `resolveWorkflowName()` 4-tier fallback: exact → case-insensitive → suffix → substring, with ambiguity detection).
- **DAG edges**: `depends_on` + `when:` conditions + `trigger_rule` join semantics — unchanged.
- **Structured data flow hardened**: `output_format` is schema-validated for **every** provider; best-effort providers (Pi/Copilot) get up to 3 validate-and-reask attempts; a node that declares `output_format` but returns no schema-valid output **fails** rather than degrading. `$nodeId.output.field` access is strict against the producer's declared schema.
- **Session persistence**: `persist_session` (node-level) / `persist_sessions: true` (workflow-level) keeps provider sessions across runs, keyed `(workflow_name, node_id, scope_key, provider)` — cross-run memory as an engine feature.
- **Event emission from inside prompts**: `archon workflow event emit --run-id ... --type ...` lets loop prompts signal the engine.

### Parallelism
- Within-layer node concurrency, per-run worktrees, parallel review agents, deterministic port allocation (3190–4089) — all unchanged from v0.3.2.
- New: `--detach` background workflow runs from CLI; folder projects (non-git workspaces) run in place without worktrees.

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Master context principles | `CLAUDE.md` / `AGENTS.md` | Soft (LLM instruction) | KISS/YAGNI/DRY+Rule-of-Three, Fail Fast, Determinism, Reversibility |
| **New principle: No Autonomous Lifecycle Mutation Across Process Boundaries** | `CLAUDE.md` | Soft (with cited precedent #1216) | A process that can't distinguish "running elsewhere" from "orphaned" must not mark work failed/cancelled on a staleness guess — surface to user with one-click action |
| North-star triage constitution | `.archon/maintainer-standup/direction.md` | Soft (drives automated P1–P4 PR triage; declines must cite a clause) | "cite `direction.md §single-tenant-per-install`" |
| Pre-flight identity gate | Workflow `requires: [github]` | Hard (blocks before worktree/AI cost) | Enforced only when per-user GitHub enabled |
| Server-side API gate | `packages/server` (`isApiGateEnabled`) | Hard (401) | Every `/api/*` request needs identity when web auth on; `/api/auth/*` + `/api/health*` exempt |
| Signup posture | `getSignupMode` | Hard | No allowlist ⇒ signup **disabled** by default + boot WARN; open signup is explicit opt-in |
| Loopback-only credential endpoint | `/internal/git-credential` | Hard (server **refuses to start** if App mode + public bind, absent explicit escape hatch) | Installation tokens never exposed beyond 127.0.0.1 |
| Structured-output fail-closed | `output_format` validation | Hard (node fails) | No schema-valid output ⇒ node failure, never silent degradation |
| Schema validation | `packages/workflows/src/schemas/` (Zod) | Hard (load-time) | `dagNodeSchema` superRefine: node-kind mutual exclusivity, retry-on-loop rejection, interactive-requires-gate_message |
| Generated-bundle staleness | CI (`bun run validate`, 8 checks) | Hard (CI gate) | `check:bundled`, `check:bundled-skill`, `check:bundled-schema`, `check:pi-vendor-map` |
| Hook validation | triage agent PostToolUse; skill Stop hooks | Hard (hook rejects) | Carried over; now also skill-frontmatter hooks |
| Type safety / ESLint zero-warning | CI | Hard | Unchanged |

### Guardrail Patterns
1. **Identity-first governance (new).** Every action attributes to an Archon `users` row (created lazily per platform identity via `user_identities`); runs and messages carry `user_id`; execution uses the **acting user's** credentials (sender-first, creator fallback — #1982). `role` (`admin`/`member`) is the seam for future per-resource scoping.
2. **Credential containment (new).** Per-user GitHub device-flow tokens and AI-provider keys encrypted at rest (AES-256-GCM), auto-provisioned local key, vendor-canonical credential ids, no secrets in list responses, masked logging.
3. **App-mode token hygiene (new).** Per-installation ~1h tokens; git credential helper installed per-worktree so long-running workflows outlive token expiry; single 401 retry with cache invalidation.
4. **Ambiguity-surfacing over auto-mutation (new).** The lifecycle-mutation principle plus one-click user actions for orphan-looking runs.
5. Carried over: isolation-by-default worktrees, env leak gate (`--allow-env-keys`), conversation locking, immutable audit-trail sessions, per-node tool allow/deny lists, `tools: []` routing calls, adapter-internal auth allowlists with silent rejection.

### Permission Model
- **Single-tenant per install, multi-user within it** — explicitly documented as a deployment-layer isolation decision (no row-scoping in code; "don't conflate multi-user with multi-tenant").
- **Web**: opt-in Better Auth (Postgres + secret) with server-side API gate; `?mine=true` filters are convenience, explicitly "not a security boundary".
- **GitHub**: App mode (per-installation tokens + per-user attribution) vs legacy PAT mode.
- **Workflow-level**: per-node `allowed_tools`/`denied_tools` (Claude), `sandbox` option, `maxBudgetUsd` cost ceiling.
- Visibility remains open across users today (roles reserved for future scoping).

---

## 5. Cross-Agent Protocol

### Agent Roster
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Orchestrator (routing agent) | `packages/core/src/orchestrator/` | AI routing to workflows/direct response; run-management via native tool or prompt section | All adapters, workflow engine |
| 13 Claude specialists (unchanged roster) | `.claude/agents/*.md` | code-reviewer, triage-agent, rulecheck-agent, code-simplifier, codebase-analyst/explorer, comment-analyzer, docs-impact, pr-test-analyzer, sdk-verifier, silent-failure-hunter, type-design-analyzer, web-researcher | Spawned by workflows/skills |
| 3 Copilot mirrors | `.github/agents/` | analyst/explorer/researcher | Copilot harness |
| **Provider registry (new)** | `packages/providers/src/registry.ts` | ProviderRegistration records: Claude + Codex (`builtIn: true`); community Pi (~20 backends via `<provider>/<model>` refs), OpenCode (embedded runtime, dynamic catalog), Copilot | Workflow executor + chat orchestrator via `IAgentProvider` |
| Workflow-inline sub-agents (new) | `agents:` node option | Inline agent definitions invokable via Task tool (Claude only) | Within a workflow node |
| Ralph/adversarial loop roles (new) | Workflow YAML prompts | Planner/Generator/Evaluator (adversarial-dev); story-implementer (ralph-dag) | Via loop iterations + files |

### Handoff Mechanisms
1. `$nodeId.output` variable substitution — now **schema-strict** when the producer declares `output_format` (unknown field access fails the consumer; author-declared-optional resolves to `''`).
2. **Typed output sidecars (new)**: `output_type` on any node writes `$ARTIFACTS_DIR/nodes/<id>.md` + `<id>.meta.json` — downstream nodes and later runs locate output **by type**, not filename convention.
3. **Loop-iteration bridging (new)**: `$LOOP_PREV_OUTPUT` carries the previous iteration's cleaned output into fresh-context iterations; `$LOOP_USER_INPUT` injects human gate feedback; `$REJECTION_REASON` flows reviewer feedback into `on_reject` prompts.
4. **Cross-run session memory (new)**: `persist_session` per-node provider session continuity keyed `(workflow, node, scope, provider)`; reset via `/workflow reset-sessions`.
5. **Capability-gated protocol delivery (new)**: run management reaches the chat agent as an in-process native `manage_run` tool on providers with `nativeTools` (Claude, Pi), and as a generated system-prompt section teaching CLI-over-bash on providers without (Codex/OpenCode/Copilot) — same protocol, two delivery mechanisms selected by declared capability.
6. **Skill→agent binding (new)**: skills (`rulecheck`, `triage`) declare `agent:` + `context: fork` — the skill is the trigger/argument surface; the agent definition supplies persona and hooks; the fork isolates context.
7. Orchestrator `/invoke-workflow` routing, `$ARTIFACTS_DIR`, DB-mediated state — carried over.

### Shared State
| State | Mechanism | Scope |
|-------|-----------|-------|
| Node outputs | `$nodeId.output` (+ typed sidecars) | Within (and across, via sidecars) workflow runs |
| Loop state | Iteration counter + session id in run metadata (`interactive_loop` pause) | Within a run, survives pause/resume |
| Provider sessions | `workflow_node_sessions` table (`persist_session`) | Across runs, per scope key |
| Identity | `users` + `user_identities` tables | Global, cross-platform |
| Credentials | `user_github_tokens`, `user_provider_keys` (encrypted) | Per user |
| AI prefs | `user_ai_prefs` (tiers/aliases/default) | Per user; highest-precedence config layer |
| Maintainer standup memory | `state.json` + `briefs/YYYY-MM-DD.md` (last 3 read into next run) | Per maintainer, cross-run |
| Events/runs/conversations | 18 DB tables (was ~8 at v0.3.2) | Persistent |

### Coordination Patterns
**Hub-and-spoke with DAG execution** — unchanged at the core. New layers on top:
- **Provider abstraction as a coordination seam**: the engine coordinates heterogeneous AI backends through one `IAgentProvider` contract with tiered capability declarations; engine behavior (structured-output enforcement path, tool delivery, session resume) branches on capabilities, not provider identity.
- **Generator-critic coordination inside one workflow**: adversarial-dev's state-machine loop alternates builder and attacker roles with numeric pass thresholds — an intra-workflow peer-adversary pattern absent at v0.3.2.
- **Human-on-the-loop for iterations**: interactive loops make the human a per-iteration coordinator (approve-with-feedback), distinct from one-shot approval gates.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Rules-layer collapse into monolithic CLAUDE.md + AGENTS.md dual-file mirror (with drift); `prime-*` on-demand context loaders replacing auto-loaded path-scoped rules; `fresh_context` + `$LOOP_PREV_OUTPUT` iteration context policy; `persist_session` cross-run memory; typed output sidecars |
| Model | **High** (was Medium) | Model tiers (`small`/`medium`/`large`) + `@alias` refs resolving provider+model+effort; layered precedence global < repo < **per-user**; per-node tier routing in default workflows (`model: small` for classification); Pi model catalog with cost/reasoning hints |
| Prompt | **Medium** | 27–28k inline prompt engineering in default workflows; structured-output prompt-augmentation + validate-and-reask for best-effort providers; `$LOOP_USER_INPUT`/`$REJECTION_REASON` feedback variables |
| Tools | **High** | Tiered capability declaration (`structuredOutput: 'enforced' \| 'best-effort' \| false`, `nativeTools`, `sessionResume`); capability-gated tool delivery (native `manage_run` vs prompt-section CLI-bash); per-node MCP config incl. Codex MCP node; `script:` nodes (bun/uv) with `deps:` |
| Intent | **High** | AI routing + 4-tier name resolution; `requires:` pre-flight intent gating; workflow-builder intent-extraction node (JSON intent → YAML); interactive loop gates as recurring intent checkpoints |
| Orchestration | **High** | First-class loop nodes (full anatomy above); Ralph DAG (PRD-driven fresh-context story loop); adversarial generator/evaluator state machine; `cancel` nodes; detached runs; resume-skipping-completed-nodes |
| Evaluation | **High** | Adversarial-dev numeric thresholds (below 7/10 ⇒ back to generator); `until_bash` deterministic loop verification; schema-validated structured output with bounded re-ask; fail-closed on validation miss; validate-ui / replicate-issue / test-release skills as E2E eval procedures |
| Sandboxing | **High** | Worktree-per-run unchanged; folder projects (run-in-place, non-git); `maxBudgetUsd` + `sandbox` per node; loopback-only credential endpoint with refuse-to-start guard |
| Governance | **High** (was Medium) | "Governed engine" as product identity; per-user identity/attribution/credential layer; App-mode token hygiene; API gate + signup-disabled default; no-autonomous-lifecycle-mutation principle; direction.md as committed triage constitution |
| Agent Design | **High** | Skill→agent binding with `context: fork` and skill-frontmatter hooks; `disable-model-invocation`; workflow-inline `agents:`; maintainer-standup as a persistent-memory scheduled agent (profile/state/briefs) |

### Findings Candidates

New candidates from the v0.5.0 re-analysis (promotion is a separate gated step — `/promote-findings`):

1. **Loop-node anatomy as an engine primitive** (Orchestration / 11.A Loop Engineering) — A complete, schema-enforced Ralph-loop config: signal-string `until` + deterministic `until_bash` (exit 0) + `max_iterations` + `fresh_context` + `interactive` per-iteration human gates + `$LOOP_PREV_OUTPUT` bridging + iteration-level events and metrics + pause/resume with session restoration. Retry is explicitly rejected on loop nodes ("loop manages its own iteration"). This is the most complete production loop-anatomy spec in the watched set and maps directly onto 11.A's "init → iterate → evaluate → exit" framing. Files: `packages/workflows/src/schemas/loop.ts`, `dag-executor.ts:2203+`, `event-emitter.ts:49-70`.
   → Promoted to [[loop-node-anatomy-schema-enforced-ralph-primitive]] on 2026-07-13
2. **Ralph-as-DAG: PRD-driven fresh-context story loop** (11.A / Orchestration) — `archon-ralph-dag.yaml` operationalizes the Ralph pattern: classify input with a small model (structured output), generate `prd.md` + `prd.json`, validate, then loop with fresh context implementing exactly one story per iteration, then PR. Demonstrates loop-scoped work decomposition (stories as iteration units) and cost-tiered model routing within one workflow.
   → Skipped: substantially covered by [[incremental-one-feature-per-session-pattern]] + [[ralph-wiggum-execution-pattern]] + [[self-contained-phase-prompt-pattern]]; deferred as corroborating-evidence EXTEND (crosslink follow-up pass) on 2026-07-13
3. **Adversarial generator/evaluator workflow with numeric pass thresholds** (Evaluation / Orchestration) — `archon-adversarial-dev.yaml`: Planner → state-machine loop alternating Generator and Evaluator whose explicit job is to break the generator's work; any criterion below 7/10 returns the sprint with adversarial feedback; bounded retries. A concrete generator-assessor-separation implementation (cites Anthropic's harness-design article).
   → Skipped: substantially covered by [[cross-vendor-adversarial-build-attack-loop]] + [[iterative-refinement-loop-with-quality-gate]] + [[builder-validator-chain-pattern]]; deferred as corroborating-evidence EXTEND (crosslink follow-up pass) on 2026-07-13
4. **Tiered provider-capability registry driving engine behavior** (Tools / Model) — Capabilities are declared per provider as discriminated values, not booleans (`structuredOutput: 'enforced' | 'best-effort' | false`), and the engine branches on them: grammar-constrained vs validate-and-reask (≤3) vs unsupported; native in-process tool vs generated prompt-section fallback for run management. Capability-gated feature delivery keeps one protocol across heterogeneous backends. Files: `packages/providers/src/registry.ts`, `types.ts`; orchestrator gating in `packages/core/src/orchestrator/`.
   → Promoted to [[tiered-capability-registry-engine-behavior-branching]] on 2026-07-13
5. **Model tiers + aliases as a cross-provider abstraction with per-user precedence** (Model) — `small`/`medium`/`large` tiers and `@alias` refs resolve provider+model+effort; precedence global config < repo config < per-user prefs; reserved-name protection; workflows reference tiers instead of model literals. Decouples workflow authoring from provider/model churn.
   → Promoted to [[model-tiers-aliases-cross-provider-indirection]] on 2026-07-13
6. **Rules-layer collapse: monolithic dual context files + on-demand priming** (Context Engineering) — Archon deleted its 11-file path-scoped `.claude/rules/` layer and consolidated into a 979-line CLAUDE.md + root AGENTS.md mirror, with `prime-*` commands for on-demand domain context. Counter-signal to the layered-rules convention the v0.3.2 analysis recorded — and the two mirror files have already drifted (AGENTS.md retains superseded positioning), illustrating the maintenance cost of duplicated context. Worth capturing as evidence on both sides of the layering debate.
   → Promoted to [[rules-layer-collapse-monolithic-context-counter-signal]] on 2026-07-13
7. **direction.md as a committed triage constitution for a scheduled maintainer agent** (Governance / 11 Agentic Systems) — `.archon/maintainer-standup/` separates shared committed direction (`direction.md`: "what Archon IS / IS NOT"; declines must cite a clause) from personal gitignored memory (`profile.md`, `state.json`, rolling `briefs/` with last-3 read-back). A concrete pattern for consistent multi-operator agent judgment with per-operator memory.
   → Promoted to [[direction-md-committed-triage-constitution]] on 2026-07-13
8. **Skill→agent binding with forked context and skill-level hooks** (Agent Design) — Skills declare `agent:` (delegate persona/constraints to an agent definition), `context: fork` (isolate from main conversation), `disable-model-invocation` (human-trigger-only), and skill-frontmatter `hooks:` (Stop-hook prompt evaluator). Separates trigger surface from persona definition — same decomposition the engine's skill/agent substrate assumes.
   → Skipped: duplicate of [[skill-forked-subagent-execution]] (mechanism already captured; flags covered by [[claude-code-skill-frontmatter-extensions]] and [[skill-invocation-control-side-effect-guard]]); deferred as corroborating-evidence EXTEND (crosslink follow-up pass) on 2026-07-13
9. **Typed node-output sidecars for by-type artifact discovery** (Orchestration / Context Engineering) — `output_type` on any node makes the executor write `$ARTIFACTS_DIR/nodes/<id>.md` + `<id>.meta.json`, so downstream nodes and later runs locate outputs by declared type rather than filename convention. Small, generalizable contract for cross-step artifact handoff.
   → Promoted to [[typed-node-output-sidecars-by-type-artifact-discovery]] on 2026-07-13
10. **No-autonomous-lifecycle-mutation principle** (Governance / Intent) — Codified engineering principle: a process that cannot distinguish "actively running elsewhere" from "orphaned" must not mark that work failed/cancelled on a staleness heuristic; surface ambiguity to the human with a one-click action. Cleanly generalizes to any multi-entry-point agent system with shared run state.
    → Promoted to [[no-autonomous-lifecycle-mutation-principle]] on 2026-07-13

#### v0.3.2 candidates (dispositioned — retained for /promote-findings dedup history)

1. DAG workflow engine with mixed node types → Skipped: duplicate of [[durable-workflow-engine-for-agent-systems]] and [[dag-vs-bsp-two-graph-based-orchestration-models]] on 2026-04-19
2. IsolationResolver 7-step worktree resolution → Promoted to [[isolation-resolver-worktree-lifecycle-algorithm]] on 2026-04-09
3. Intent-based meta-routing skill → Promoted to [[intent-based-meta-routing-skill]] on 2026-04-09
4. Hook-based enforcement for agent outputs → Promoted to [[hook-based-enforcement-for-agent-outputs]] on 2026-04-09
5. Triple context namespace for cross-platform agents → Skipped: partial match with [[multi-ide-portability-via-installer-templates]]; single-source on 2026-04-19
6. Per-node tool restrictions in YAML workflows → Skipped: implementation-specific on 2026-04-19
7. Workflow dependency injection (WorkflowDeps) → Skipped: standard DI pattern on 2026-04-19

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-09 | v0.3.2 | all | Initial analysis — 745 files, 10-package monorepo, DAG workflow engine, 21 default workflows, 13 agents |
| 2026-07-13 | v0.5.0 | all | Re-analysis after upstream delta — 1,262 files, 11 packages (+providers), first-class loop nodes (until/until_bash/fresh_context/interactive + iteration events), console UI default at `/` with builder + monitoring hub, provider registry (Pi/OpenCode/Copilot community + Codex MCP node), GitHub App auth + per-user identity/credential layer, rules layer collapsed into CLAUDE.md + AGENTS.md, skills 7→14, 20 default workflows (heavy churn: ralph-dag, adversarial-dev, workflow-builder) |
