---
title: "gstack -- Structural Analysis"
id: "gstack-analysis"
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
  - "gstack"
analyzed_version: "v0.15.16.0"
analyzed_date: "2026-04-08"
repo_url: "https://github.com/garrytan/gstack"
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
| Total files | 413 |
| Total directories | 87 |
| TypeScript files | 175 (42.4%) |
| Markdown files | 90 (21.8%) |
| Template files (.tmpl) | 38 (9.2%) |
| HTML files | 25 (6.1%) |
| Shell scripts | 7 |
| JSON files | 7 |
| JS files | 6 |
| YAML/YML files | 8 |
| SQL files | 4 |
| Ruby files | 4 |
| CSS files | 4 |
| PNG files | 5 |
| MD-to-code ratio | **0.49:1** (balanced — skill pack with browser tooling) |
| Max directory depth | 4 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Generated SKILL.md files | 41 | Various skill directories (root-level: `review/`, `qa/`, `ship/`, etc.) |
| Skill templates (.tmpl) | 38 | Same directories (source of truth) |
| Architecture/philosophy docs | 5 | Root (ARCHITECTURE.md, ETHOS.md, DESIGN.md, BROWSER.md, CONTRIBUTING.md) |
| Review specialist guides | 7 | `review/specialists/` |
| QA references/templates | 3 | `qa/references/`, `qa/templates/` |
| OpenClaw integration files | 4 | `openclaw/` (CLAUDE.md variants, agents section) |
| Human docs | 8 | `docs/` |
| Test fixtures | 4 | `test/fixtures/` |
| Project files | 5 | Root (README, CHANGELOG, TODOS, AGENTS.md, CLAUDE.md) |
| Other | ~15 | Various |
| **Total** | **~90** |

Key insight: gstack is a skill pack with browser tooling. SKILL.md files are **generated** from `.tmpl` templates — the templates are source of truth. 38 templates generate 41 SKILL.md files (some skills have host-specific variants). TypeScript powers the browser daemon, CLI tooling, and build system.

### Directory Naming Conventions
Kebab-case throughout. Each skill gets its own top-level directory (flat structure — no nesting like BMAD's phase-based organization).

### Top-Level Structure
```
.
├── agents/              # Agent personality configurations (empty/minimal)
├── autoplan/            # Auto-review pipeline skill
├── benchmark/           # Performance regression detection
├── bin/                 # CLI tools (29 shell scripts)
├── browse/              # Headless browser daemon + CLI (Playwright + Bun)
│   ├── src/             # Server, commands, snapshot
│   ├── test/            # Integration tests
│   └── dist/            # Compiled binary
├── canary/              # Post-deploy monitoring loop
├── careful/             # Destructive command warning
├── checkpoint/          # Session checkpoint/recovery
├── codex/               # Multi-AI second opinion (Codex CLI)
├── cso/                 # Chief Security Officer audit
├── design*/             # Design skills (consultation, html, review, shotgun)
├── devex-review/        # Developer experience audit
├── document-release/    # Post-ship doc updates
├── freeze/ + unfreeze/  # Directory edit lock/unlock
├── guard/               # Combined careful + freeze
├── gstack-upgrade/      # Self-update skill
├── health/              # Health check skill
├── hosts/               # Typed host configs (claude, codex, cursor, factory, kiro, openclaw, opencode, slate)
├── investigate/         # Root-cause debugging
├── land-and-deploy/     # Merge → deploy → canary
├── learn/               # Cross-session learnings management
├── office-hours/        # YC-style brainstorming / design thinking
├── openclaw/            # OpenClaw integration (CLAUDE.md variants + skills)
├── pair-agent/          # Pair programming with multiple AI agents
├── plan-*/              # Plan review skills (ceo, design, devex, eng)
├── qa/ + qa-only/       # Browser-based QA (fix vs report-only)
├── retro/               # Weekly retrospective
├── review/              # PR review with specialist dispatch
│   └── specialists/     # 7 specialist guides (api-contract, data-migration, maintainability, performance, red-team, security, testing)
├── scripts/             # Build tooling (gen-skill-docs, host-config, resolvers, host-adapters)
├── setup-*/             # Setup skills (browser cookies, deploy)
├── ship/                # Ship workflow (test → review → push → PR)
├── supabase/            # Supabase functions + migrations
├── test/                # Skill validation + E2E evals
└── lib/                 # Shared TypeScript utilities
```

### Notable Structural Patterns
1. **Template-generated skills**: SKILL.md files are generated from `.tmpl` templates via `gen-skill-docs.ts`. Templates are the source of truth. This enables host-specific skill variants (Claude, Codex, Cursor, etc.).
2. **Flat skill directory structure**: Each skill is a top-level directory. No grouping by phase/category. 31 unique skills covering the full development lifecycle.
3. **Headless browser daemon**: `browse/` is a full Playwright-based headless browser with persistent state (cookies, tabs, sessions), sub-second command latency (~100ms after first call), and compiled Bun binary.
4. **Multi-host architecture**: `hosts/` defines typed configs for 8 AI hosts (Claude, Codex, Cursor, Factory, Kiro, OpenClaw, OpenCode, Slate). Skills are regenerated per-host.
5. **CLI tooling in `bin/`**: 29 shell scripts for config, telemetry, learnings, session management, community features, and repo-mode detection.
6. **Review Army pattern**: `review/specialists/` contains 7 specialist guides that are dispatched in parallel during PR review.

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Constraints/Rules + Tool Usage | Dev commands, project structure, testing conventions, skill generation |
| `AGENTS.md` | Both | Global | Auto-loaded | Identity/Persona + Tool Usage | Skill catalog with descriptions. Available skills table. Key conventions. |
| `ETHOS.md` | LLM | Global | Referenced | Identity/Persona + Constraints | Builder philosophy: "Boil the Lake" (completeness is cheap), "Search Before Building" (3 layers of knowledge), "User Sovereignty" (AI recommends, users decide) |
| `ARCHITECTURE.md` | Both | Global | Referenced | Workflow/Process | Browser daemon architecture, host config system, build pipeline |
| `SKILL.md` (root) | LLM | Tool | Auto-loaded | Tool Usage | Main gstack skill: headless browser commands, preamble setup |
| `*/SKILL.md` (40 files) | LLM | Tool | Auto-loaded | Various | Individual skill definitions (generated from templates) |
| `*/SKILL.md.tmpl` (38 files) | Build | Tool | Referenced | Various | Source templates for skill generation |
| `hosts/*.ts` (8 files) | Build | Global | Referenced | Tool Usage | Typed host configs defining preamble, allowed-tools, and host-specific behavior per AI platform |
| `review/specialists/*.md` (7 files) | LLM | Tool | Referenced | Constraints/Rules | Specialist review guides: API contract, data migration, maintainability, performance, red-team, security, testing |
| `openclaw/gstack-full-CLAUDE.md` | LLM | Global | Injected | Constraints/Rules | Full gstack context for OpenClaw integration |
| `openclaw/gstack-lite-CLAUDE.md` | LLM | Global | Injected | Constraints/Rules | Lite gstack context for OpenClaw |
| `qa/references/issue-taxonomy.md` | LLM | Tool | Referenced | Constraints/Rules | Bug classification taxonomy for QA skill |
| `qa/templates/qa-report-template.md` | LLM | Tool | Referenced | Memory/State | QA report output template |

Sampling notes: Read root CLAUDE.md (100 lines), AGENTS.md (80 lines), ETHOS.md in full, ARCHITECTURE.md (80 lines). Read 5 SKILL.md exemplars (root, review, cso, office-hours, autoplan). Read 1 specialist guide. Classified remaining by pattern.

### Context Loading Strategy
**Preamble-driven bootstrap with session state injection:**

1. **Preamble execution**: Every SKILL.md starts with an identical preamble bash block (~80 lines) that runs on invocation. The preamble: checks for updates, creates session markers, loads config (proactive mode, skill prefix, telemetry), detects repo mode, loads learnings count, records session timeline, and checks for CLAUDE.md routing rules.
2. **Template generation**: Skills are generated from `.tmpl` templates via `gen-skill-docs.ts`. The generator injects host-specific configuration (preamble, allowed tools, tool aliases) based on the target host (Claude, Codex, etc.).
3. **Ethos injection**: ETHOS.md principles are injected into every workflow skill's preamble automatically. Every skill starts with "Boil the Lake" / "Search Before Building" / "User Sovereignty" context.
4. **Learnings system**: Cross-session learnings stored in `~/.gstack/projects/{slug}/learnings.jsonl`. Recent learnings loaded in preamble and searched at skill start. The `/learn` skill manages review, search, prune, and export.
5. **Session intelligence**: Session markers in `~/.gstack/sessions/`, timeline events in `~/.gstack/analytics/`, and skill usage tracking enable cross-session state.

**Key pattern: Shell preamble as context injection.** Unlike BMAD's config-driven activation or GSD's @-reference chain, gstack uses a bash preamble block that runs shell scripts to assemble context (config values, repo mode, learnings, session state, telemetry). The preamble is identical across all skills — injected by the template generator.

## 3. Workflow Topology

### Phases/Stages (Review Pipeline)

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| **Office Hours** | `/office-hours` | Design doc saved | Yes (6 forcing questions) |
| **CEO Review** | `/plan-ceo-review` | CEO-level plan approved | Yes (taste decisions) |
| **Design Review** | `/plan-design-review` | Design dimensions scored 0-10 | Yes (approval) |
| **Eng Review** | `/plan-eng-review` | Architecture locked | Yes (approval) |
| **DevEx Review** | `/plan-devex-review` | DX audit complete | Optional |
| **Implementation** | User writes code | Code ready for review | No |
| **PR Review** | `/review` | Review findings addressed | Yes (author decides) |
| **QA** | `/qa` or `/qa-only` | Bugs found and fixed (or reported) | Yes (author verifies) |
| **Ship** | `/ship` | Tests pass, PR created | Yes (merge decision) |
| **Deploy** | `/land-and-deploy` | Deployed + canary verified | Yes (deploy approval) |
| **Post-ship** | `/document-release` | Docs updated | No |
| **Retro** | `/retro` | Weekly retro complete | No |

### Flow Diagram (ASCII)

```
┌──────────────────┐
│  /office-hours   │──── 6 forcing questions (startup mode)
│  (idea → design) │     or design thinking (builder mode)
└────────┬─────────┘
         │
┌────────▼─────────┐
│  /autoplan        │──── Runs CEO → design → eng reviews
│  (auto-review     │     auto-decisions with 6 principles
│   pipeline)       │     surfaces taste decisions at gate
└────────┬─────────┘
         │  (or run reviews individually)
   ┌─────┼─────────┬──────────┐
   ▼     ▼         ▼          ▼
 /plan-  /plan-    /plan-    /plan-
 ceo     design    eng       devex

         │ (implementation happens)
         ▼
┌────────────────┐
│  /review       │──── 7 specialists dispatched in parallel
│  (PR review)   │     API contract, security, performance,
│                │     data migration, red-team, testing,
│                │     maintainability
└────────┬───────┘
         ▼
┌────────────────┐    ┌──────────────┐
│  /qa           │    │  /cso        │
│  (browser QA)  │    │  (security   │
│                │    │   audit)     │
└────────┬───────┘    └──────────────┘
         ▼
┌────────────────┐
│  /ship         │──── test → review → push → PR
└────────┬───────┘
         ▼
┌────────────────┐
│ /land-and-     │──── merge → deploy → canary verify
│  deploy        │
└────────┬───────┘
         ▼
┌────────────────┐
│ /document-     │──── update docs to match shipped code
│  release       │
└────────┬───────┘
         ▼
┌────────────────┐
│  /retro        │──── weekly retro with shipping streaks
└────────────────┘

Cross-cutting:
  /careful   — warn before destructive commands
  /freeze    — lock directory edits
  /guard     — careful + freeze combined
  /learn     — cross-session learnings
  /checkpoint — session save/restore
  /investigate — root-cause debugging
  /canary    — post-deploy monitoring loop
  /benchmark — performance regression detection
  /codex     — multi-AI second opinion
  /pair-agent — pair programming with multiple AIs
```

### Transition Mechanisms
- **User-initiated**: User invokes skills via slash commands. Skills are independent — any can be used standalone.
- **Autoplan pipeline**: `/autoplan` chains CEO → design → eng → devex reviews with auto-decisions, surfacing only taste decisions at a final gate.
- **Proactive suggestions**: Skills can proactively suggest themselves based on context (e.g., `/review` suggests itself when user is about to merge).
- **Voice triggers**: Some skills have speech-to-text aliases (e.g., "see-so" for `/cso`, "auto plan" for `/autoplan`).

### Parallelism
- **Review Army**: `/review` dispatches 7 specialist subagents in parallel (API contract, data migration, maintainability, performance, red-team, security, testing). Results are aggregated.
- **Multi-AI second opinion**: `/codex` spawns OpenAI Codex CLI for a second opinion on the same task.
- **Pair agent**: `/pair-agent` enables pair programming with multiple AI agents simultaneously.
- **No workflow-level parallelism**: Skills are sequential; parallelism is within skills (specialist dispatch).

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| ETHOS.md philosophy | `ETHOS.md` (injected into all skills) | Soft | "Boil the Lake" (completeness), "User Sovereignty" (AI recommends, users decide) |
| Careful skill | `careful/SKILL.md` | Soft (advisory) | Warns before rm -rf, DROP TABLE, force-push |
| Freeze/guard skills | `freeze/`, `guard/` | Hard (directory lock) | Blocks edits outside specified directory |
| Specialist review guides | `review/specialists/*.md` | Soft | 7 domain-specific review checklists |
| Preamble-tier system | SKILL.md frontmatter | Soft | Tiers 1-4 controlling preamble depth |
| Skill validation | `test/skill-validation.test.ts` | Hard (CI) | Static validation of SKILL.md structure |
| LLM-as-judge evals | `test/skill-llm-eval.test.ts` | Hard (CI gate) | LLM evaluates skill output quality |
| E2E evals | `test/skill-e2e-*.test.ts` | Hard (CI gate) | End-to-end testing via `claude -p` |
| Two-tier test system | `touchfiles.ts` | Hard | Gate tier (blocks merge) vs periodic tier (weekly cron) |
| Diff-based test selection | `touchfiles.ts` | Soft | Only tests touching changed files run |

### Guardrail Patterns
1. **Ethos as constitutional document**: ETHOS.md defines 3 principles injected into every skill: "Boil the Lake" (completeness is cheap with AI), "Search Before Building" (check existing solutions), "User Sovereignty" (AI recommends, users decide). This is philosophical governance — shaping judgment, not blocking actions.
2. **Safety skill triad**: `careful` (warns before destructive commands), `freeze` (locks directory edits), `guard` (both combined). Progressive safety enforcement.
3. **Review Army specialist dispatch**: 7 specialist guides define domain-specific review criteria. Dispatched in parallel during `/review`. Each specialist has explicit scope and red flags.
4. **Three-tier eval system**: Tier 1 (free, static validation), Tier 2 (E2E via claude -p, ~$3.85/run), Tier 3 (LLM-as-judge, ~$0.15/run). Gate vs periodic classification.
5. **Autoplan auto-decisions**: 6 decision principles for auto-resolving review findings. Surfaces only "taste decisions" (close approaches, borderline scope, Codex disagreements) at a final human gate.

### Permission Model
- **Allowed-tools per skill**: Each SKILL.md frontmatter declares which tools it can use.
- **Preamble-tier system**: Skills declare their tier (1-4) controlling how much preamble context loads.
- **Proactive mode**: Configurable per-user — skills can suggest themselves or stay passive.
- **Telemetry opt-in**: Usage analytics are opt-in with explicit prompting.

## 5. Cross-Agent Protocol

### Agent Roster
gstack is primarily a single-agent skill pack (one AI agent with many role-based skills). Multi-agent coordination exists in specific skills:

| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Primary agent (Claude/Codex/etc.) | Whichever host is active | All skills | Review specialists, Codex second opinion |
| Review specialists (7) | `review/specialists/*.md` | Domain-specific review | Primary agent via subagent dispatch |
| Codex second opinion | `codex/SKILL.md` | Independent code review | Primary agent (results compared) |
| Pair agent | `pair-agent/SKILL.md` | Pair programming | Primary agent |

### Handoff Mechanisms
1. **Specialist subagent dispatch**: `/review` spawns 7 specialist subagents in parallel via the Agent tool. Each specialist receives the diff and its domain-specific guide. Results are aggregated by the primary agent.
2. **Cross-AI delegation**: `/codex` spawns OpenAI Codex CLI for an independent second opinion. The primary agent and Codex opinions are compared; disagreements are surfaced to the user.
3. **Skill chaining**: `/autoplan` chains CEO → design → eng → devex reviews sequentially. Each review's output feeds into the next.
4. **Learnings handoff**: Cross-session learnings in JSONL files persist state between sessions. Skills load relevant learnings at startup.

### Shared State
- **`~/.gstack/` directory**: Sessions, analytics, config, learnings, timeline
- **`~/.gstack/projects/{slug}/learnings.jsonl`**: Per-project cross-session learnings
- **`~/.gstack/sessions/`**: Active session markers (30-min idle timeout)
- **`~/.gstack/analytics/`**: Skill usage tracking, telemetry
- **Git state**: Branch, diff scope, repo mode — all detected in preamble

### Coordination Patterns
**Single-agent with role-switching and specialist dispatch.** The primary agent switches roles via skill invocation (CEO, designer, engineer, QA, security officer). Multi-agent coordination is limited to specialist dispatch during review and cross-AI second opinion via Codex. This is more like a Swiss Army knife (one tool, many blades) than a team (many tools, one goal).

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Shell preamble context injection (identical across 41 skills). Cross-session learnings in JSONL with search. Session intelligence (markers, timeline, usage tracking). Repo-mode detection. Template-generated skills with host-specific context. Ethos injection as constitutional context. |
| Model | Medium | Multi-host architecture (8 hosts: Claude, Codex, Cursor, Factory, Kiro, OpenClaw, OpenCode, Slate). Host-specific skill generation. Cross-AI second opinion via `/codex`. |
| Prompt | **High** | ETHOS.md as philosophical constitution injected into all skills. "Boil the Lake" principle (completeness is cheap with AI). "Search Before Building" (3 layers of knowledge). "User Sovereignty" (AI recommends, users decide). Voice triggers for speech-to-text. Proactive skill suggestion. |
| Tools | **High** | Headless browser daemon (Playwright + Bun, sub-second commands, persistent state). 29 CLI tools in `bin/`. Skill template generator. Health dashboard. Eval framework (3 tiers). Compiled Bun binary for browser CLI. |
| Intent | **High** | "User Sovereignty" as core principle — AI recommends, users decide. Proactive mode (configurable). Autoplan auto-decisions with taste-decision surfacing. `/careful` warns before destructive actions. `/freeze` locks directory edits. 6 decision principles for auto-resolution. |
| Orchestration | Medium | `/autoplan` pipeline (CEO → design → eng → devex). Review Army parallel specialist dispatch. Cross-AI second opinion. Primarily single-agent with role-switching, not multi-agent orchestration. |
| Evaluation | **High** | Three-tier eval system: Tier 1 (free, static, <1s), Tier 2 (E2E via claude -p, ~$3.85/run), Tier 3 (LLM-as-judge, ~$0.15/run). Diff-based test selection. Gate vs periodic tier classification. Review Army with 7 specialist perspectives. Eval run persistence and comparison. |
| Sandboxing | Medium | Browser daemon isolation (Chromium sandboxed, no code execution). `/freeze` directory locking. Careful skill for destructive commands. Session marker cleanup (30-min idle timeout). |
| Governance | Medium | ETHOS.md as philosophical governance. Safety skill triad (careful/freeze/guard). Autoplan taste-decision gate. Review specialist guides. Allowed-tools per skill. |
| Agent Design | **High** | Role-based specialist tools (CEO, designer, engineer, QA, security officer, release engineer, debugger). Template-generated skills with host-specific variants. Shell preamble as boot sequence. Cross-session learnings system. Proactive skill suggestion. Session timeline and analytics. Voice trigger aliases. |

### Findings Candidates

1. **Template-generated skills with multi-host variants** (Agent Design, Tools) — SKILL.md files are generated from `.tmpl` templates via `gen-skill-docs.ts`. Templates are source of truth. Host configs (8 hosts) define preamble, allowed-tools, and tool aliases. Same skill, different packaging per AI platform. Compare to BMAD's multi-IDE installer templates.
→ Promoted to [[template-generated-skills-multi-host]] on 2026-04-08

2. **Shell preamble as universal boot sequence** (Context Engineering, Agent Design) — Every SKILL.md starts with an identical ~80-line bash preamble that: checks for updates, creates session markers, loads config, detects repo mode, loads learnings, records timeline events, and checks for routing rules. This is context assembly via shell execution rather than file loading or config parsing.
→ Promoted to [[shell-preamble-as-boot-sequence]] on 2026-04-08

3. **ETHOS.md as philosophical constitution** (Prompt, Governance) — Three principles ("Boil the Lake", "Search Before Building", "User Sovereignty") injected into every skill as preamble context. Not rules or constraints — philosophical stances that shape judgment. "Completeness is cheap" reframes the AI cost equation. "User Sovereignty" explicitly prevents autonomous action. Compare to BMAD's persona persistence and GSD's scope guardrails.
→ Promoted to [[ethos-md-philosophical-constitution]] on 2026-04-08

4. **Review Army parallel specialist dispatch** (Evaluation, Orchestration) — `/review` dispatches 7 specialist subagents in parallel (API contract, data migration, maintainability, performance, red-team, security, testing). Each specialist has a dedicated guide with scope, red flags, and criteria. Results are aggregated. This is the most structured review decomposition across all analyzed repos.
→ Skipped: duplicate of [[gstack-review-army-parallel-specialist-dispatch]] on 2026-04-19

5. **Three-tier eval system** (Evaluation, Tools) — Tier 1: free static validation (<1s). Tier 2: E2E via `claude -p` (~$3.85/run). Tier 3: LLM-as-judge (~$0.15/run). Diff-based test selection. Gate tier (blocks merge) vs periodic tier (weekly cron). Eval runs persisted with comparison across runs. Novel pattern: costing eval tiers explicitly.
→ Promoted to [[three-tier-costed-eval-system]] on 2026-04-08

6. **Cross-session learnings system** (Context Engineering, Agent Design) — Per-project learnings in JSONL (`~/.gstack/projects/{slug}/learnings.jsonl`). Loaded in preamble, searched at skill start, managed via `/learn` skill (review, search, prune, export). This is persistent learning that survives session boundaries — the agent gets smarter over time within a project.
→ Promoted to [[cross-session-learnings-jsonl]] on 2026-04-08

7. **Autoplan auto-decision pipeline with taste-decision surfacing** (Orchestration, Evaluation) — `/autoplan` chains CEO → design → eng → devex reviews with 6 auto-decision principles. Auto-resolves clear findings. Surfaces only "taste decisions" (close approaches, borderline scope, Codex disagreements) at a final human gate. This balances automation with human judgment.
→ Promoted to [[autoplan-auto-decision-pipeline]] on 2026-04-08

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v0.15.16.0 | all | Initial analysis. 413 files, 90 MD, 41 skills (38 templates), 8 host configs, headless browser daemon. Role-based specialist tools. |
