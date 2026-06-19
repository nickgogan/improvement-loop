---
title: "GSD (Get Shit Done) -- Structural Analysis"
id: "gsd-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-07"
updated: "2026-04-07"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "gsd"
analyzed_version: "v1.33.0"
analyzed_date: "2026-04-07"
repo_url: "https://github.com/gsd-build/get-shit-done"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# GSD (Get Shit Done) -- Structural Analysis

## Metadata
- **Repo:** https://github.com/gsd-build/get-shit-done
- **Version analyzed:** v1.33.0
- **Date:** 2026-04-07
- **Spectrum position:** wholesale

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 600 |
| Total directories | 48 |
| Markdown files | 341 (56.8%) |
| `.cjs` files (CommonJS) | 160 (26.7%) |
| `.ts` files (TypeScript) | 47 (7.8%) |
| Config files (`.yml`, `.json`) | 26 (4.3%) |
| Shell scripts (`.sh`) | 7 |
| Image files (`.svg`, `.png`) | 5 |
| MD-to-code ratio | **1.64:1** (MD dominant) |
| Max directory depth | 5 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions | 24 | `agents/` |
| Commands (slash entry points) | 70 | `commands/gsd/` |
| Workflows (orchestration) | 10 | `get-shit-done/workflows/` |
| Reference docs (shared knowledge) | 34 | `get-shit-done/references/` |
| Templates (artifact schemas) | 33 | `get-shit-done/templates/` |
| Context profiles | 3 | `get-shit-done/contexts/` |
| SDK prompts (agents + workflows + templates) | 20 | `sdk/prompts/` |
| Human documentation | 25 | `docs/`, root READMEs, CHANGELOG, CONTRIBUTING |
| i18n translations | ~100 | `docs/ja-JP/`, `docs/ko-KR/`, `docs/pt-BR/`, `docs/zh-CN/` |
| Other (plans, PR templates) | ~22 | `.plans/`, `.github/` |
| **Total** | **341** | |

**Key insight**: Of 341 markdown files, **194 are functional** (agent definitions, commands, workflows, references, templates, context profiles) — these ARE the codebase. Only ~25 are human documentation in the traditional sense. The remaining ~122 are i18n translations, SDK re-packaged copies, and project management files.

### Directory Naming Conventions

Kebab-case throughout. Directories are **role-based** (named by function, not technology):

- `agents/` -- agent persona definitions
- `commands/gsd/` -- slash command entry points
- `get-shit-done/workflows/` -- orchestration logic
- `get-shit-done/references/` -- shared reference docs
- `get-shit-done/templates/` -- artifact templates
- `get-shit-done/contexts/` -- context profiles (dev, research, review)
- `sdk/` -- SDK for external integrations
- `docs/` -- human documentation (with i18n subdirectories)

### Top-Level Structure

```
.
├── .clinerules          # Cline-compatible project rules
├── .github/             # CI, issue/PR templates
├── .plans/              # Internal development plans
├── agents/              # 24 agent definition files (.md)
├── assets/              # Images
├── bin/                 # Installer scripts
├── commands/gsd/        # 70 slash command files (.md)
├── docs/                # Human docs + i18n (ja-JP, ko-KR, pt-BR, zh-CN)
├── get-shit-done/       # Core runtime
│   ├── bin/             # CLI tools (gsd-tools.cjs + lib/)
│   ├── contexts/        # 3 context profiles
│   ├── references/      # 34 reference docs
│   ├── templates/       # 33 artifact templates
│   └── workflows/       # 10 workflow orchestrators
├── hooks/               # Git/Claude hooks
├── scripts/             # Build/release scripts
├── sdk/                 # SDK (prompts + src)
└── tests/               # Test files (.test.cjs)
```

### Notable Structural Patterns

1. **Three-layer markdown hierarchy**: commands (entry) -> workflows (orchestration) -> agents (execution). Each layer is a separate directory.
2. **Massive markdown dominance**: 56.8% of all files are `.md`. The framework IS its prompts -- code is glue.
3. **Internationalization at docs level**: 4 language directories under `docs/`, plus root-level README translations.
4. **SDK as separate concern**: `sdk/` contains both TypeScript source and markdown prompt templates, suggesting the SDK re-packages the markdown for external consumption.
5. **Reference docs are shared context**: `get-shit-done/references/` acts as a knowledge base that agents `@`-reference. 34 files covering gates, checkpoints, TDD, verification patterns, etc.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `.clinerules` | LLM | Global | Auto-loaded | Constraints/Rules | Project-wide rules: no direct edits, CommonJS only, safety constraints |
| `agents/gsd-executor.md` | LLM | Task | Injected | Identity/Persona + Workflow | Executor agent: atomic commits, deviation handling, checkpoints |
| `agents/gsd-planner.md` | LLM | Task | Injected | Identity/Persona + Workflow | Planner agent: task breakdown, dependency analysis, goal-backward verification |
| `agents/gsd-verifier.md` | LLM | Task | Injected | Identity/Persona + Workflow | Verifier agent: goal-backward verification, trust-nothing mindset |
| `agents/gsd-debugger.md` | LLM | Task | Injected | Identity/Persona + Workflow | Debug agent: scientific method, checkpoint management |
| `agents/gsd-phase-researcher.md` | LLM | Task | Injected | Identity/Persona + Workflow | Research agent: phase-scoped technical investigation |
| `agents/gsd-project-researcher.md` | LLM | Task | Injected | Identity/Persona + Workflow | Research agent: domain ecosystem before roadmap |
| `agents/gsd-plan-checker.md` | LLM | Task | Injected | Identity/Persona + Workflow | Checker agent: plan quality validation |
| `agents/gsd-roadmapper.md` | LLM | Task | Injected | Identity/Persona + Workflow | Roadmap agent: phase breakdown, requirement mapping |
| `agents/gsd-code-reviewer.md` | LLM | Task | Injected | Identity/Persona + Workflow | Code review agent |
| `agents/gsd-code-fixer.md` | LLM | Task | Injected | Identity/Persona + Workflow | Code fix agent |
| `agents/gsd-codebase-mapper.md` | LLM | Task | Injected | Identity/Persona + Workflow | Codebase analysis agent |
| `agents/gsd-ui-researcher.md` | LLM | Task | Injected | Identity/Persona + Workflow | UI design contract agent |
| `agents/gsd-ui-checker.md` | LLM | Task | Injected | Identity/Persona + Workflow | UI validation agent |
| `agents/gsd-ui-auditor.md` | LLM | Task | Injected | Identity/Persona + Workflow | UI audit agent |
| `agents/gsd-doc-writer.md` | LLM | Task | Injected | Identity/Persona + Workflow | Documentation generation agent |
| `agents/gsd-doc-verifier.md` | LLM | Task | Injected | Identity/Persona + Workflow | Documentation validation agent |
| `agents/gsd-integration-checker.md` | LLM | Task | Injected | Identity/Persona + Workflow | Cross-phase integration checker |
| `agents/gsd-nyquist-auditor.md` | LLM | Task | Injected | Identity/Persona + Workflow | Verification coverage auditor |
| `agents/gsd-security-auditor.md` | LLM | Task | Injected | Identity/Persona + Workflow | Security audit agent |
| `agents/gsd-intel-updater.md` | LLM | Task | Injected | Identity/Persona + Workflow | Codebase intelligence updater |
| `agents/gsd-assumptions-analyzer.md` | LLM | Task | Injected | Identity/Persona + Workflow | Assumption extraction agent |
| `agents/gsd-advisor-researcher.md` | LLM | Task | Injected | Identity/Persona + Workflow | Gray area decision research agent |
| `agents/gsd-user-profiler.md` | LLM | Task | Injected | Identity/Persona + Workflow | User behavioral profiling agent |
| `agents/gsd-research-synthesizer.md` | LLM | Task | Injected | Identity/Persona + Workflow | Multi-research synthesis agent |
| `commands/gsd/*.md` (70 files) | LLM | Tool | Chain-loader | Workflow/Process | Slash command entry points: auto-loaded by harness, then @-reference workflows and reference docs to assemble full context |
| `get-shit-done/workflows/*.md` (10 files) | LLM | Project | Injected | Workflow/Process | Orchestration workflows: discuss, plan, execute, verify, review, manager |
| `get-shit-done/references/*.md` (34 files) | LLM | Global | Referenced | Constraints/Rules + Tool Usage | Shared knowledge: gates, checkpoints, TDD, verification, agent contracts |
| `get-shit-done/templates/*.md` (33 files) | LLM | Tool | Referenced | Memory/State | Artifact templates: PLAN.md, STATE.md, CONTEXT.md, SUMMARY.md, etc. |
| `get-shit-done/contexts/*.md` (3 files) | LLM | Global | Injected | Identity/Persona | Context profiles (dev, research, review) that adjust output style |
| `sdk/prompts/agents/*.md` (8 files) | LLM | Task | Injected | Identity/Persona | SDK-packaged agent prompts (subset of agents/) |
| `sdk/prompts/workflows/*.md` (5 files) | LLM | Project | Injected | Workflow/Process | SDK-packaged workflow prompts |
| `sdk/prompts/templates/*.md` (7+ files) | LLM | Tool | Referenced | Memory/State | SDK-packaged templates |
| `docs/AGENTS.md` | Both | Global | Referenced | Workflow/Process | Human-readable agent reference with spawn patterns, tools, relationships |
| `docs/ARCHITECTURE.md` | Both | Global | Referenced | Workflow/Process | System architecture for contributors |
| `README.md` | Human | Global | Referenced | Identity/Persona | Project overview, install, usage |

### Context Loading Strategy

**Three-layer dynamic injection with `@`-references:**

1. **Command layer** (`commands/gsd/*.md`): Entry point loaded by the harness when user types `/gsd:command`. Contains frontmatter (name, description, allowed-tools) and an `<execution_context>` block with `@` references to workflow files.
2. **Workflow layer** (`get-shit-done/workflows/*.md`): Loaded via `@` references from commands. Contains orchestration logic and its own `@` references to reference docs. Spawns agents.
3. **Agent layer** (`agents/*.md`): Loaded by the harness when workflows spawn subagents via `Task(subagent_type="gsd-executor")`. Each agent has frontmatter (name, description, tools, color) and XML-structured sections (`<role>`, `<execution_flow>`, `<rules>`).

**Key mechanism**: Agents further load project-specific context by reading `./CLAUDE.md` and `.claude/skills/` from the target project's working directory. This means GSD agents compose their context from both the GSD framework files AND the user's project files.

**Reference documents** (`get-shit-done/references/`) are shared across agents via `@` references in `<required_reading>` blocks. This is the "shared knowledge base" pattern -- common rules live in one place, consumed by multiple agents.

**Templates** (`get-shit-done/templates/`) define the shape of artifacts that agents produce (PLAN.md, SUMMARY.md, STATE.md, etc.). Templates are the schema contract between agents.

---

## 3. Workflow Topology

### Phases/Stages

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| **New Project** | `/gsd:new-project` | PROJECT.md + REQUIREMENTS.md + ROADMAP.md created | Yes -- user reviews requirements |
| **Discuss** | `/gsd:discuss-phase <N>` | CONTEXT.md with locked decisions | Yes -- user answers gray area questions |
| **Research** | Auto via plan-phase or `/gsd:research-phase` | RESEARCH.md produced | No (auto) |
| **Plan** | `/gsd:plan-phase <N>` | PLAN.md files approved | Yes -- approve/revise/abort gate |
| **Execute** | `/gsd:execute-phase <N>` | All plans executed, SUMMARY.md per plan | Checkpoint gates during execution |
| **Verify** | `/gsd:verify-work` | VERIFICATION.md with pass/fail | Yes -- escalation for gaps |
| **Complete Milestone** | `/gsd:complete-milestone` | Milestone archived, next milestone started | Yes -- retrospective review |

### Flow Diagram (ASCII)

```
                    ┌──────────────────┐
                    │   NEW PROJECT    │
                    │  (PROJECT.md,    │
                    │  REQUIREMENTS,   │
                    │  ROADMAP)        │
                    └────────┬─────────┘
                             │
              ┌──────────────▼──────────────┐
              │   For each phase in ROADMAP  │
              └──────────────┬──────────────┘
                             │
                    ┌────────▼─────────┐
                    │     DISCUSS      │──── Human: gray area decisions
                    │  (CONTEXT.md)    │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │    RESEARCH      │──── Auto: 4 parallel researchers
                    │  (RESEARCH.md)   │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │      PLAN        │◄─── Revision loop (max 3)
                    │   (PLAN.md x N)  │──── Human: approve/revise/abort
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │    EXECUTE       │──── Wave-based parallel
                    │ (SUMMARY.md x N) │──── Checkpoint gates
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │     VERIFY       │──── Escalation for gaps
                    │(VERIFICATION.md) │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │   NEXT PHASE     │
                    │  (or COMPLETE    │
                    │   MILESTONE)     │
                    └──────────────────┘
```

### Transition Mechanisms

- **Command invocation**: User triggers each phase via `/gsd:*` commands. `/gsd:next` auto-routes to the next logical step.
- **State file tracking**: `STATE.md` tracks current phase, status, and last operation. All transitions read/write STATE.md.
- **CLI tool orchestration**: `gsd-tools.cjs init <workflow>` returns JSON with phase context, letting workflows discover what to do next.
- **`@`-reference chaining**: Commands `@`-reference workflows, workflows `@`-reference docs. The harness resolves the chain at invocation time.
- **Artifact-based handoff**: Each phase produces a specific artifact (CONTEXT.md, RESEARCH.md, PLAN.md, SUMMARY.md, VERIFICATION.md) that the next phase consumes.

### Parallelism

- **Research phase**: 4 parallel researcher agents (stack, features, architecture, pitfalls) + synthesizer.
- **Execute phase**: Wave-based parallel execution. Plans grouped into waves by dependency graph. Plans in the same wave run in parallel via subagents. Waves execute sequentially.
- **Autonomous mode**: `/gsd:autonomous` chains discuss->plan->execute per phase automatically, but phases still run sequentially.

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| Project rules file | `.clinerules` | Hard | "Never edit outside a GSD workflow", "CommonJS only" |
| Gate taxonomy | `references/gates.md` | Hard | Pre-flight, Revision, Escalation, Abort gates |
| Gate prompts | `references/gate-prompts.md` | Soft | approve-revise-abort, yes-no, scope-confirm patterns |
| Agent tool restrictions | Agent frontmatter `tools:` field | Hard | Each agent lists exactly which tools it can use |
| Scope guardrails | Workflow files (inline) | Soft | "No scope creep" in discuss-phase, "phase boundary is FIXED" |
| Anti-patterns | `references/universal-anti-patterns.md` | Soft | Documented patterns to avoid |
| Context budget | `references/context-budget.md` | Soft | ~15% orchestrator, 100% fresh per subagent |
| Checkpoint protocol | `references/checkpoints.md` | Hard | Execution checkpoints with human intervention points |
| Revision loop cap | Workflow files + `references/revision-loop.md` | Hard | Max 3 iterations, then escalation |
| Security constraints | `.clinerules` | Hard | `execFileSync` over `execSync`, path validation |

### Guardrail Patterns

1. **Four-gate taxonomy**: Every validation checkpoint is one of: Pre-flight (block entry), Revision (loop back with feedback, capped at 3), Escalation (surface to human), Abort (stop and preserve state). This is the core guardrail architecture.
2. **Tool allowlists per agent**: Agent frontmatter explicitly lists permitted tools. An executor gets Read/Write/Edit/Bash; a verifier gets Read/Bash/Grep/Glob (no Write/Edit).
3. **Artifact-as-contract**: Templates define the exact shape of artifacts. Agents produce artifacts matching the template; downstream agents validate against it.
4. **Scope containment**: Discuss-phase explicitly blocks scope creep ("Does this clarify HOW we implement what's already in the phase, or does it add a new capability?").
5. **Trust-nothing verification**: Verifier is told "Do NOT trust SUMMARY.md claims. Verify what ACTUALLY exists in the code."
6. **Stale detection**: Revision loops detect stall (issue count not decreasing between iterations) and escalate early rather than burning iterations.

### Permission Model

- **Per-agent tool access**: Defined in agent `.md` frontmatter `tools:` field. Agents cannot access tools not in their list.
- **Model profiles**: `references/model-profiles.md` defines quality/balanced/budget tiers controlling which model each agent type uses.
- **Context profiles**: `contexts/*.md` (dev, research, review) adjust output style but not capabilities.
- **No file-level permissions**: Any agent with `Read` can read anything. No scoped filesystem access.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Category | Defined In | Tools | Communicates With |
|------------|----------|-----------|-------|-------------------|
| gsd-project-researcher (x4) | Researcher | `agents/` | Read, Write, Bash, Grep, Glob, WebSearch, WebFetch, MCP | research-synthesizer |
| gsd-phase-researcher (x4) | Researcher | `agents/` | Read, Write, Bash, Grep, Glob, WebSearch, WebFetch, MCP | planner (via RESEARCH.md) |
| gsd-ui-researcher | Researcher | `agents/` | Read, Write, Bash, Grep, Glob, WebSearch, WebFetch, MCP | ui-checker |
| gsd-research-synthesizer | Synthesizer | `agents/` | Read, Write, Bash | planner (via SUMMARY.md) |
| gsd-assumptions-analyzer | Analyzer | `agents/` | Read, Bash, Grep, Glob | discuss workflow |
| gsd-advisor-researcher | Analyzer | `agents/` | Read, Bash, Grep, Glob, WebSearch, WebFetch, MCP | discuss workflow |
| gsd-planner | Planner | `agents/` | Read, Write, Bash, Glob, Grep, WebFetch, MCP | plan-checker, executor |
| gsd-plan-checker | Checker | `agents/` | Read, Bash, Glob, Grep | planner (revision loop) |
| gsd-roadmapper | Planner | `agents/` | Read, Write, Bash, Glob, Grep | new-project workflow |
| gsd-executor | Executor | `agents/` | Read, Write, Edit, Bash, Grep, Glob | verifier (via SUMMARY.md) |
| gsd-verifier | Verifier | `agents/` | Read, Write, Bash, Grep, Glob | escalation to user |
| gsd-integration-checker | Checker | `agents/` | Read, Bash, Grep, Glob | verify workflow |
| gsd-nyquist-auditor | Auditor | `agents/` | Read, Write, Edit, Bash, Glob, Grep | verify workflow |
| gsd-security-auditor | Auditor | `agents/` | Read, Bash, Grep, Glob | secure-phase workflow |
| gsd-ui-checker | Checker | `agents/` | Read, Bash, Glob, Grep | ui-phase workflow |
| gsd-ui-auditor | Auditor | `agents/` | Read, Write, Bash, Grep, Glob | ui-review workflow |
| gsd-codebase-mapper | Mapper | `agents/` | Read, Bash, Grep, Glob, Write | map-codebase workflow |
| gsd-debugger | Debugger | `agents/` | Read, Write, Edit, Bash, Grep, Glob, WebSearch | debug workflow |
| gsd-code-reviewer | Reviewer | `agents/` | Read, Bash, Grep, Glob | code-review workflow |
| gsd-code-fixer | Fixer | `agents/` | Read, Write, Edit, Bash, Grep, Glob | code-review-fix workflow |
| gsd-doc-writer | Writer | `agents/` | Read, Write, Bash, Grep, Glob | docs-update workflow |
| gsd-doc-verifier | Verifier | `agents/` | Read, Bash, Grep, Glob | docs-update workflow |
| gsd-intel-updater | Updater | `agents/` | Read, Write, Bash, Grep, Glob | intel workflow |
| gsd-user-profiler | Profiler | `agents/` | Read | profile-user workflow |

**Total: 24 agent definitions** (some spawned in parallel instances, e.g., 4x project-researcher).

### Handoff Mechanisms

1. **Artifact-based handoff (primary)**: Agents produce files that downstream agents consume. The artifact IS the communication channel:
   - CONTEXT.md (discuss -> research, plan)
   - RESEARCH.md (research -> plan)
   - PLAN.md (plan -> plan-checker -> executor)
   - SUMMARY.md (executor -> verifier)
   - VERIFICATION.md (verifier -> user/next-phase)

2. **Completion markers**: Agents emit standardized H2 markers (`## PLANNING COMPLETE`, `## RESEARCH BLOCKED`, etc.) in their output. Orchestrators parse these to determine success/failure/escalation routing. Documented in `references/agent-contracts.md`.

3. **Subagent spawning**: Workflows use `Task(subagent_type="gsd-executor", prompt="...")` to spawn agents. The spawning call blocks until the agent completes and returns its output.

4. **`<files_to_read>` blocks**: Orchestrators include explicit file lists in agent prompts. Agents MUST read these files before doing anything else -- this is the primary context injection mechanism.

### Shared State

- **`.planning/` directory**: All persistent state lives here. Contains STATE.md, config.json, phase directories, research artifacts.
- **STATE.md**: Central state file tracking current phase, status, and operation history. Read by every workflow at startup.
- **ROADMAP.md**: Phase registry. Read by plan/execute/verify workflows.
- **config.json**: User preferences (model profiles, workflow toggles, branching strategy). Read via `gsd-tools.cjs config-get`.
- **Git**: Atomic commits per task. Git state is shared implicitly -- all agents operate on the same repo.

### Coordination Patterns

**Hub-and-Spoke with artifact passing.** Workflow files (the "hub") orchestrate by spawning specialized agents (the "spokes"), passing context via `<files_to_read>` blocks and agent prompts, and collecting results via completion markers and produced artifacts. Agents never communicate directly with each other -- all coordination flows through the workflow orchestrator.

Within this hub-and-spoke model:
- **Sequential pipeline** for the main flow (discuss -> research -> plan -> execute -> verify)
- **Parallel fan-out** within phases (4x researchers, wave-based executors)
- **Revision loops** between producer-checker pairs (planner <-> plan-checker, max 3 iterations)
- **Escalation to human** when automated resolution fails

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Three-layer context chain (command -> workflow -> agent). `@`-reference mechanism for dynamic assembly. `<files_to_read>` blocks for explicit context injection. Context profiles (dev/research/review) that adjust output style. Context budget rules (~15% orchestrator, 100% fresh per subagent). |
| Model | Medium | Model profiles (quality/balanced/budget) with per-agent tier selection. `executor_model` and `verifier_model` configurable per-phase. No model-specific prompting — same prompts across models. |
| Prompt | **High** | XML-structured agent prompts (`<role>`, `<execution_flow>`, `<rules>`). Completion markers as structured output contract (`## PLANNING COMPLETE`). Gate prompt patterns (approve-revise-abort, yes-no, scope-confirm). Frontmatter-as-metadata in command and agent files. Thinking partner philosophy in discuss-phase ("user = founder, Claude = builder"). |
| Tools | Medium | Tool allowlists per agent in frontmatter. MCP integration (Context7) as first-class. CLI tools layer (`gsd-tools.cjs`) providing state/config/template APIs. Cross-runtime compatibility (Claude Code, Copilot, Gemini CLI, OpenCode, Codex). |
| Intent | **High** | Scope guardrails in discuss-phase ("no scope creep" heuristic). Phase boundaries from ROADMAP.md are FIXED — discussion clarifies HOW, not WHETHER. Goal-backward verification (verifier starts from outcome, works backwards). CLAUDE.md enforcement as hard constraint during execution. |
| Orchestration | **High** | Hub-and-spoke with 24 specialized agents. Wave-based parallel execution. Thin orchestrators that coordinate but never execute. Revision loops between producer-checker pairs (max 3 iterations with stall detection). Artifact-based handoff (CONTEXT.md -> RESEARCH.md -> PLAN.md -> SUMMARY.md -> VERIFICATION.md). |
| Evaluation | **High** | Four-gate taxonomy (Pre-flight, Revision, Escalation, Abort). Trust-nothing verification ("Do NOT trust SUMMARY.md claims"). Nyquist auditor for verification coverage. Goal-backward methodology (task completion != goal achievement). Plan-checker with bounded revision loops. |
| Sandboxing | Medium | Git worktree isolation for parallel execution. Atomic commits per task (rollback granularity). Checkpoint protocol for pausing/resuming. No container/VM isolation — relies on file system and git. |
| Governance | **High** | `.clinerules` as project constitution. Gate taxonomy as enforcement framework. Tool allowlists per agent. Scope containment in discuss-phase. Human escalation gates at every workflow boundary. Security constraints (execFileSync over execSync, path validation). |
| Agent Design | **High** | 24 agent definitions with YAML frontmatter (name, description, tools, color). XML-structured personas (`<role>`, `<project_context>`, `<rules>`). Completion markers as inter-agent protocol. Agent categories (Researchers, Planners, Executors, Checkers, Verifiers, Auditors). Fresh context per agent (context rot prevention). |

### Findings Candidates

1. **Three-layer context chain-loading** (Context Engineering, Agent Design) — The command -> workflow -> agent `@`-reference chain is a distinctive pattern for assembling agent context dynamically. Worth comparing to OpenClaw's static 6-file taxonomy and BMAD's step-file system.
→ Promoted to [[three-layer-context-chain-loading]] on 2026-04-08

2. **Four-gate taxonomy** (Evaluation, Governance) — Pre-flight/Revision/Escalation/Abort is a clean, composable framework for validation checkpoints. More structured than most ad-hoc "check then retry" patterns. May already partially exist in KB — check for overlap.
→ Skipped: duplicate of [[gsd-gates-taxonomy-four-canonical-types]] on 2026-04-19

3. **Goal-backward verification** (Evaluation) — "Task completion != goal achievement" as a verification principle. The verifier starts from the outcome and works backwards rather than checking task checklists. Novel approach worth documenting.
→ Promoted to [[goal-backward-verification]] on 2026-04-08

4. **Artifact-as-contract pattern** (Orchestration) — Templates define artifact schemas, agents produce artifacts matching templates, downstream agents validate against them. The artifact IS the communication protocol — no message passing, no shared memory.
→ Promoted to [[artifact-as-contract-pattern]] on 2026-04-08

5. **Thinking partner philosophy** (Prompt, Agent Design) — discuss-phase's "user = founder/visionary, Claude = builder" framing. Explicitly scopes what the user should and shouldn't be asked about. Compare to Superpowers' brainstorming skills and BMAD's analyst agents.
→ Promoted to [[thinking-partner-philosophy]] on 2026-04-08

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-07 | v1.33.0 | all | Initial analysis. 600 files, 341 MD, 24 agents, 70 commands, 10 workflows. |
