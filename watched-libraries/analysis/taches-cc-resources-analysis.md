---
title: "TÂCHES CC Resources -- Structural Analysis"
id: "taches-cc-resources-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
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
  - "taches-cc-resources"
  - "claude-code"
  - "skills"
  - "prompt-engineering"
analyzed_version: "latest (2026-05-24 — shallow clone)"
analyzed_date: "2026-05-24"
repo_url: "https://github.com/glittercowboy/taches-cc-resources"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# TÂCHES CC Resources -- Structural Analysis

## Metadata
- **Repo:** https://github.com/glittercowboy/taches-cc-resources
- **Version analyzed:** latest (2026-05-24 shallow clone; no semantic version tag)
- **Date:** 2026-05-24
- **Spectrum position:** cherry-pick (not yet formally registered as watched library)
- **Prior analysis:** Source entry only (`taches-claude-code-resources-commands-skills-thinki.md`), no previous structural analysis. Two findings extracted 2026-03-28: meta-prompting-separating-analysis-from-execution.md, thinking-models-mental-framework-commands-for-codi.md
- **Stars:** ~1.9k | **Forks:** ~404

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total directories (non-git) | ~40 |
| Top-level directories | 5 (`.claude-plugin/`, `agents/`, `commands/`, `docs/`, `skills/`) |
| Command files (.md in commands/) | 27 (19 top-level + 8 research/* subdirectory) |
| Skill directories | 11 (create-agent-skills, create-hooks, create-mcp-servers, create-meta-prompts, create-plans, create-slash-commands, create-subagents, debug-like-expert, expertise, setup-ralph, the-pirate-bay) |
| Agent files | 3 (skill-auditor, slash-command-auditor, subagent-auditor) |
| Docs files | 3 (context-handoff.md, meta-prompting.md, todo-management.md) |
| Config files | 2 (.claude-plugin/marketplace.json, plugin.json) |
| Languages in repo | TypeScript (57.1%), Shell (35.6%), Python (6.3%), Dockerfile (1.0%) |
| Max directory depth | 4 (skills/expertise/[domain]/references/, skills/create-plans/workflows/) |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions (subagents) | 3 | `agents/` |
| Commands/slash commands | 27 | `commands/`, `commands/consider/`, `commands/research/` |
| Skills (SKILL.md + references) | 11+ | `skills/*/SKILL.md` + `skills/*/references/` |
| Domain expertise skills | 3 | `skills/expertise/macos-apps/`, `iphone-apps/`, `n8n-automations/` |
| Human documentation (docs/) | 3 | `docs/` |
| README files | ~5 | Root, skills/create-plans, skills/setup-ralph |
| Templates | present | `skills/create-plans/templates/` |
| Workflow definitions | present | `skills/create-plans/workflows/`, `skills/the-pirate-bay/workflows/` |

### Directory Naming Conventions
Kebab-case throughout. Skills follow verb-noun convention (create-*, debug-*, setup-*, the-*). Commands use verb-noun (add-to-todos, check-todos, heal-skill) or verb-colon-noun namespace for grouped commands (consider:pareto, research:deep-dive). Expertise skills live in `skills/expertise/[domain]/` — a subdirectory within skills, not a parallel top-level directory.

### Top-Level Structure
```
taches-cc-resources/
├── .claude-plugin/         # Plugin marketplace config (plugin.json, marketplace.json)
├── agents/                 # 3 subagent auditor definitions
├── commands/               # 27 slash command .md files
│   ├── consider/           # 12 mental model commands (/consider:*)
│   └── research/           # 8 research methodology commands (/research:*)
├── docs/                   # 3 human-readable docs explaining major patterns
└── skills/                 # 11 skill directories
    ├── create-agent-skills/
    ├── create-hooks/
    ├── create-mcp-servers/
    ├── create-meta-prompts/
    ├── create-plans/       # Most complex skill — has templates/, workflows/, references/
    ├── create-slash-commands/
    ├── create-subagents/
    ├── debug-like-expert/
    ├── expertise/          # Domain knowledge sub-skills (macos-apps, iphone-apps, n8n-automations)
    ├── setup-ralph/        # Autonomous loop scaffolding
    └── the-pirate-bay/     # Torrent search CLI (added 2026-04-01)
```

### Notable Structural Patterns
1. **Command-as-skill-proxy pattern**: Many top-level commands are 1-2 line wrappers that invoke a skill (`allowed-tools: Skill(create-hooks)`). The command is just a named entry point; the logic lives in the skill.
2. **Namespace grouping with colon syntax**: `consider:pareto`, `consider:first-principles`, `research:deep-dive` create sub-namespaces by slash command filename directory. All 12 consider commands are in `commands/consider/` and all 8 research commands are in `commands/research/`.
3. **Expertise-as-loadable-context**: Domain expertise is a skill subtype. `skills/expertise/[domain]/SKILL.md` is a knowledge base (not a workflow) that other skills load selectively when planning domain-specific work.
4. **Plugin distribution**: `.claude-plugin/` directory with `plugin.json` and `marketplace.json` makes the whole repo installable via `claude plugin marketplace add glittercowboy/taches-cc-resources`.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `commands/consider/*.md` | LLM | Task | Auto-loaded | Constraints/Rules | 12 mental model commands. Each is a pure prompt with YAML frontmatter (`description`, `argument-hint`). No injected identity. |
| `commands/research/*.md` | LLM | Task | Auto-loaded | Workflow/Process | 8 research methodology commands. Each uses `<intake_gate>` → `<decision_gate>` pattern with `AskUserQuestion`. Saves output to `artifacts/research/`. |
| `commands/heal-skill.md` | LLM | Task | Auto-loaded | Workflow/Process | XML-structured; 5-step self-healing workflow for skills. Requires user approval before applying changes. |
| `commands/whats-next.md` | LLM | Task | Auto-loaded | Workflow/Process | Context handoff command. Creates `whats-next.md` in CWD. Comprehensive XML-tagged output schema. |
| `commands/ask-me-questions.md` | LLM | Task | Auto-loaded | Workflow/Process | Intake-and-decision-gate pattern; used to gather requirements before any task execution. |
| `agents/skill-auditor.md` | LLM | Task | Injected | Identity/Persona + Workflow/Process | Subagent with `model: sonnet`, `tools: Read, Grep, Glob`. Reads best practices files first via `@`-reference chain. Outputs severity-based findings. |
| `agents/slash-command-auditor.md` | LLM | Task | Injected | Identity/Persona + Workflow/Process | Same audit pattern as skill-auditor. Reads create-slash-commands references first. |
| `agents/subagent-auditor.md` | LLM | Task | Injected | Identity/Persona + Workflow/Process | Same audit pattern. Reads create-subagents references first. Distinguishes structural issues from style preferences. |
| `skills/create-plans/SKILL.md` | LLM | Task | Auto-loaded | Workflow/Process | Most complex skill in repo. XML principles + context_scan + domain_expertise + intake routing. ~18k (>500 lines) — full lifecycle planning with deviation rules. |
| `skills/create-hooks/SKILL.md` | LLM | Task | Auto-loaded | Workflow/Process | Hook creation guide with full JSON config examples. Covers all 9 hook event types. |
| `skills/setup-ralph/README.md` | Human | Task | Referenced | Workflow/Process | Human-facing Ralph loop documentation. SKILL.md contains the actual automated setup procedure. |
| `skills/the-pirate-bay/SKILL.md` | LLM | Task | Auto-loaded | Workflow/Process | Intent-routing SKILL.md. Routes to workflows/ subdirectory by user intent. |
| `skills/expertise/macos-apps/SKILL.md` | LLM | Task | Referenced | Constraints/Rules | Domain expertise context (~5k tokens). Loaded selectively by create-plans based on project domain. |
| `skills/create-agent-skills/references/use-xml-tags.md` | LLM | Task | Referenced | Constraints/Rules | Required and conditional XML tag specifications for skills. Read by all three audit agents at start of every audit. |
| `skills/create-agent-skills/references/skill-structure.md` | LLM | Task | Referenced | Constraints/Rules | YAML naming rules, progressive disclosure pattern, anti-patterns. |

### Classification Key Notes
- All YAML frontmatter in commands uses `description`, optional `argument-hint`, optional `allowed-tools`.
- Skills use YAML frontmatter with `name` and `description` matching directory name.
- Agent files add `tools:` (minimal set) and `model:` (typically `sonnet`).
- `@`-references inside agent critical_workflow sections make all three auditors chain-loaders (they pull in references/ files before executing).

### Context Loading Strategy
Two-tier assembly. Commands are self-contained flat prompts. Skills use SKILL.md as entry point (overview + principles) with selective reads into `references/` for detail. A third pattern is the expertise sub-skill: `create-plans/SKILL.md` dynamically loads domain expertise skills at runtime based on project keyword inference — making context loading partially data-driven rather than statically defined. Agents are injected by the calling command and assemble their own context via `@`-reference chains before executing.

---

## 3. Workflow Topology

### Primary Workflows

**A. Meta-Prompting Workflow (create-plans / create-meta-prompts)**
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Brief creation | `/create-plan` with no planning structure | User confirms brief | Yes (inline question) |
| Domain expertise loading | Domain keyword detected or explicit | User confirms domain or declines | Yes (AskUserQuestion) |
| Roadmap creation | Brief confirmed | User confirms roadmap | Yes (inline question) |
| Phase planning | User selects "Plan next phase" | PLAN.md written | Yes (before PLAN.md write) |
| Phase execution | `/run-plan <path>` | SUMMARY.md written + git commit | No (autonomous) |
| Context handoff | 10–25% tokens remaining | `.continue-here.md` written | Soft (user can override) |

**B. Research Workflow (commands/research/)**
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Intake | Command invoked | User confirms all questions answered | Yes (decision gate loop) |
| Research | "Start research" chosen | Output written to `artifacts/research/` | No |

**C. Audit-Heal Loop**
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Audit | `/audit-skill`, `/audit-slash-command`, `/audit-subagent` | Findings report presented | No |
| Heal | `/heal-skill` | Proposed diffs applied | Yes (explicit 4-option approval gate) |

**D. Ralph Autonomous Loop**
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| Setup | `/setup-ralph` | loop.sh + PROMPT files generated | Yes (config questions) |
| Planning | `./loop.sh plan` | IMPLEMENTATION_PLAN.md generated | No (autonomous) |
| Building | `./loop.sh [N]` | All tasks complete or N iterations | No (autonomous) |
| Observation | Loop exits | Human reviews AGENTS.md, updates specs | Yes (environment engineering) |

### Flow Diagram (ASCII) — create-plans

```
/create-plan
     │
     ▼
context_scan (git status, .planning/ structure check)
     │
     ▼
intake (AskUserQuestion — present state-aware options)
     │
     ├── New project → Brief → Roadmap → [domain expertise] → Phase Plan → PLAN.md
     │
     ├── Existing → Resume from handoff / Plan next phase / Execute current
     │
     └── Handoff found → Resume or discard

Phase execution via /run-plan <PLAN.md>:
     │
     ▼
execute (subagent with fresh context)
     │
     ├── Bug found → auto-fix (Rule 1-3)
     ├── Architectural change → ask user (Rule 4)
     └── Enhancement → log to ISSUES.md (Rule 5)
     │
     ▼
SUMMARY.md + git commit
```

### Transition Mechanisms
- User-facing: AskUserQuestion with structured numbered options (2-4 choices).
- Automatic: Context percentage thresholds (25%, 15%, 10%) trigger handoff warnings and auto-handoff.
- File-based state: `.continue-here.md` in phase directory encodes resume state; `.planning/ROADMAP.md` encodes phase status.
- Deviation rules are embedded in execution behavior — no external trigger needed.

### Parallelism
The meta-prompting system supports parallel sub-agent execution when dependencies are independent. `create-plans` can spawn multiple subagents for independent phase tasks. `setup-ralph` scripts support batched parallel reads.

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| XML `<constraints>` in agent files | `agents/*.md` | Hard (MUST/NEVER/ALWAYS) | "NEVER modify files during audit - ONLY analyze and report" |
| Human approval gate in heal-skill | `commands/heal-skill.md` | Hard | 4-option approval before any edits applied |
| Context thresholds + auto-handoff | `skills/create-plans/SKILL.md` | Soft → Hard | 15% = pause; 10% = auto-handoff, stop |
| Tool restriction per command | YAML `allowed-tools:` | Hard (harness enforces) | `allowed-tools: [Read, Edit, Bash(ls:*), Bash(git:*)]` |
| Deviation classification rules | `skills/create-plans/SKILL.md` | Embedded | Rules 1-3: auto-fix; Rule 4: ask; Rule 5: log |
| Read-before-audit requirement | `agents/*.md` critical_workflow | Hard (MANDATORY marker) | All audit agents read best practices files first |
| Security checklist | `skills/create-hooks/SKILL.md` | Checklist | Infinite loop prevention, path safety, JSON validation |

### Guardrail Patterns
- **Minimal tool scopes**: Every agent and command declares only what it needs. Audit agents are read-only (`Read, Grep, Glob` only). Heal-skill restricts to `[Read, Edit, Bash(ls:*), Bash(git:*)]`.
- **Human gate as prerequisite to destructive action**: `heal-skill` cannot apply any change without explicit 4-option user approval. No auto-apply path exists.
- **Reference-first pattern**: All three audit agents use `<critical_workflow>` that MANDATES reading best practices files before executing any evaluation — preventing "rules from memory" drift.
- **Anti-enterprise principle**: `create-plans` has an explicit `<principle name="anti_enterprise_patterns">` section banning RACI, stakeholder management, sprint ceremonies, etc. This is a stylistic governance constraint embedded in skill behavior.

### Permission Model
No system-wide allowlist/denylist. Governance is per-artifact: each command and agent declares its own tool surface via YAML `allowed-tools:`. The pattern is minimum-necessary-surface declared at definition time, not at runtime. `the-pirate-bay` has no `allowed-tools:` restriction (implied broad access for CLI tool invocation).

---

## 5. Cross-Agent Protocol

### Agent Roster
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| skill-auditor | `agents/skill-auditor.md` | Read/Grep/Glob (read-only); Sonnet model | Called by `/audit-skill` command |
| slash-command-auditor | `agents/slash-command-auditor.md` | Read/Grep/Glob (read-only); Sonnet model | Called by `/audit-slash-command` command |
| subagent-auditor | `agents/subagent-auditor.md` | Read/Grep/Glob (read-only); Sonnet model | Called by `/audit-subagent` command |
| create-plans subagent | Inline in `skills/create-plans` | Full tool access; spawned per phase | Fresh context, receives PLAN.md as input |
| Ralph loop agent | `./loop.sh` script | Full Claude access via CLI; `--dangerously-skip-permissions` | Reads PROMPT_plan.md / PROMPT_build.md; writes IMPLEMENTATION_PLAN.md, commits |

### Handoff Mechanisms
- **Command → Agent**: Commands invoke subagents via `allowed-tools: Skill(...)` or `Task` delegation. No state is passed; the subagent reads its own reference files on boot.
- **Plan → Subagent**: `create-plans` generates PLAN.md, then `/run-plan` passes PLAN.md path to a fresh subagent. State is entirely file-mediated.
- **Session → Session (whats-next)**: `/whats-next` writes `whats-next.md` with XML-tagged sections. Next session loads it via `@whats-next.md`. No runtime passing — pure file bridge.
- **Ralph loop**: Each iteration reads PROMPT.md from disk, executes, commits, exits. The next iteration starts fresh. State encoded in: IMPLEMENTATION_PLAN.md (task list), AGENTS.md (operational learnings), git history (committed outcomes).

### Shared State
- Per-project files: `TO-DOS.md`, `whats-next.md`, `.planning/`, `IMPLEMENTATION_PLAN.md`, `AGENTS.md`.
- No centralized runtime state object. Every shared state mechanism is a file on disk.
- Expertise skills are loaded from `~/.claude/skills/expertise/` — a global shared read-only context.

### Coordination Patterns
- **Sequential pipeline with human gates**: create-plans workflow (Brief → Roadmap → Phase → Execute → Summary).
- **Hub-and-spoke auditor**: Command invokes specialized subagent, subagent returns findings report, command presents to user.
- **Autonomous loop with environment engineering**: Ralph pattern — no in-loop coordination; the human updates the environment (specs, AGENTS.md, prompts) and the loop picks up changes on next iteration.
- **Parallel fan-out**: create-meta-prompts detects independent task subtrees and launches parallel subagents.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | High | Context percentage thresholds (25%/15%/10%) with automatic handoff. `whats-next.md` XML-tagged file bridge for session continuity. Expertise selective loading (SKILL.md only: ~5k tokens vs. all refs: ~20-27k tokens). |
| Model Selection | Low | Agents specify `model: sonnet`. No model selection logic or rationale beyond that. |
| Prompt Craft | High | Pure XML structure standard for skills and agents. Intake-and-decision-gate pattern with AskUserQuestion. `/consider:*` mental model namespace. `heal-skill` self-correction workflow. Research command suite (8 methodology variants with structured output schemas). |
| Tool Integration | High | `create-hooks` skill: full documentation of all 9 Claude Code hook event types, command vs. prompt hook types, matcher syntax, input/output schemas, security checklist. Plugin marketplace distribution pattern. |
| Intent Engineering | Medium | Deviation classification rules (5 rules: auto-fix vs. ask vs. log). Anti-enterprise principle embedded in planning skill. Autonomy boundaries defined per-command via `allowed-tools:`. |
| Orchestration | High | Ralph autonomous loop pattern (fresh context per iteration, file-state, backpressure via tests). create-plans parallel/sequential subagent dispatch. Command-as-proxy pattern (commands are thin wrappers over skills). |
| Evaluation | High | Three dedicated audit subagents (skill, slash-command, subagent). `/heal-skill` closes the feedback loop: audit → findings → heal → verify. Read-before-audit requirement prevents evaluation from memory. Severity-based findings (Critical / Recommendations / Quick Fixes) instead of scores. |
| Sandboxing | Medium | Ralph Docker mode: container-isolated Claude execution with project-directory-only mount. `--dangerously-skip-permissions` in isolated container as explicit safety affordance. Non-root user requirement for permissions mode. |
| Governance | Medium | NEVER-modify constraints on audit agents. Mandatory human gate on heal-skill. Tool surface minimization per-agent. Reference-first pattern as anti-drift mechanism. |
| Agent Design | High | Three-role auditor design (skill/command/subagent typed specialists). Expertise-as-skill pattern (domain knowledge as loadable context, not embedded in planner). Context percentage monitoring for graceful degradation. Plans-as-prompts principle (PLAN.md IS the execution prompt). |
| Agentic Systems | Medium | Ralph loop: full autonomous build system with planning phase, building phase, human observation phase. create-plans: full solo-developer+Claude lifecycle (Brief → Roadmap → Phases → Ship → Milestone). |

### Findings Candidates

**1. Intake-and-Decision-Gate Pattern** (Dim 3 — Prompt Craft)
The `ask-me-questions.md` and research commands implement a reusable pattern: analyze existing context first (don't re-ask what's stated), ask 2-4 questions about genuine gaps, then present a looping decision gate ("Start / Ask more / Add context"). This prevents premature execution while giving the user control over when work begins. The pattern is explicitly named and reused across at least 8 commands. Novel: the decision gate loop (not just an intake gate — a recursive loop until user chooses "start").

**2. Severity-Based Audit Output Without Scores** (Dim 7 — Evaluation)
All three audit agents produce structured findings in Critical / Recommendations / Quick Fixes tiers, explicitly refusing to use scoring. Combined with the reference-first mandatory read and the "verify before flagging" instruction (check if content exists under different tag name before flagging), this is a well-developed practitioner rubric for evaluating LLM artifacts. The meta-commentary that "contextual judgment trumps arbitrary rules" is notable.

**3. Context Percentage Threshold Degradation Model** (Dim 1 — Context Engineering)
`create-plans` documents a specific degradation curve: 0-30% peak quality, 30-50% good, 50-70% degrading, 70%+ poor — with the key insight that Claude enters "completion mode" at ~40-50% when it *sees* context mounting, not at 80% when it's actually full. The response is aggressive atomicity (2-3 tasks per PLAN.md, not 10). This is a quantified practitioner model of context quality degradation.

**4. Domain Expertise as Loadable Context Sub-Skill** (Dim 10 — Agent Design / Dim 1 — Context Engineering)
`create-plans` separates domain expertise from planning logic. Expertise skills (~5k tokens each) live in `~/.claude/skills/expertise/[domain]/` and are loaded selectively by the planner when domain keywords are detected. The expertise SKILL.md contains a `<references_index>` that maps planning phase types to specific reference files — enabling partial loading (8-12k tokens) vs. full loading (20-27k tokens). This is a token-efficient, extensible domain-knowledge injection pattern.

**5. Ralph Autonomous Loop: Fresh Context Per Iteration as Hallucination Prevention** (Dim 6 — Orchestration / Dim 8 — Sandboxing)
The Ralph pattern explicitly frames fresh context per iteration as a solution to "hallucination accumulation and context poisoning." Each iteration: read specs+plan from disk → pick most important task → implement → validate (tests/lint/build) → commit → exit → restart. The backpressure mechanism (tests/lints/builds must pass before commit) prevents bad iterations from accumulating. Stuck detection (auto-skip after 3 failures) prevents infinite loops. Docker mode adds filesystem isolation. The human role is "environment engineer, not code fixer."

**6. `create-hooks` as Hook Design Reference** (Dim 4 — Tool Integration)
The `create-hooks` SKILL.md is a complete Claude Code hooks reference: all 9 event types (PreToolUse, PostToolUse, UserPromptSubmit, Stop, SubagentStop, SessionStart, SessionEnd, PreCompact, Notification), command vs. prompt hook types, regex matcher syntax, JSON input/output schemas, environment variables, and a security checklist (infinite loop prevention via `stop_hook_active`, path safety, JSON validation). This is the most comprehensive hooks guide observed in any watched library.

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-05-24 | latest (shallow clone) | all 6 | First structural analysis. Prior entries: source entry (2026-03-28) + 2 findings extracted. New since 2026-03-28: create-hooks skill, setup-ralph skill, the-pirate-bay skill, 8 research commands (/research:*), ask-me-questions command, create-plans skill (major new addition), 3 audit agents, docs/ directory, plugin marketplace config. |
