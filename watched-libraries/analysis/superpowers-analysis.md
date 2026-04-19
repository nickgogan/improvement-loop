---
title: "Superpowers -- Structural Analysis"
id: "superpowers-analysis"
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
  - "superpowers"
analyzed_version: "v5.0.7"
analyzed_date: "2026-04-08"
repo_url: "https://github.com/obra/superpowers"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
  - "research-dimension-mapping"
---

# Superpowers -- Structural Analysis

## Metadata
- **Repo:** https://github.com/obra/superpowers
- **Version analyzed:** v5.0.7
- **Date:** 2026-04-08
- **Spectrum position:** thin-wrapper

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 142 |
| Total directories | 48 |
| Markdown files | 75 (52.8%) |
| Shell scripts (`.sh`) | 26 (18.3%) |
| Text files (`.txt`) | 15 (10.6%) |
| JSON files | 10 (7.0%) |
| JavaScript (`.js`, `.cjs`) | 6 (4.2%) |
| Config (`.yml`) | 2 |
| Other (`.ts`, `.py`, `.html`, `.dot`, `.cmd`) | 5 |
| MD-to-code ratio | **9.4:1** (overwhelmingly MD) |
| Max directory depth | 4 |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skill definitions (SKILL.md) | 14 | `skills/*/SKILL.md` |
| Skill supporting docs | 23 | `skills/*/` (non-SKILL.md) |
| Agent definitions | 1 | `agents/` |
| Commands (deprecated) | 3 | `commands/` |
| Human documentation | 16 | `docs/` |
| Platform integration | 2 | `.codex/`, `.opencode/` |
| Root-level (README, CLAUDE, AGENTS, GEMINI, etc.) | 7 | root |
| Test fixtures | 5 | `tests/` |
| Other (CHANGELOG, RELEASE-NOTES, CODE_OF_CONDUCT) | 4 | root |
| **Total** | **75** | |

**Key insight**: Of 75 markdown files, **38 are functional** (14 SKILL.md + 23 supporting skill docs + 1 agent). This is an even more extreme "markdown IS the codebase" ratio than GSD — the 26 shell scripts are mostly installer/hook glue, and the 15 `.txt` files are test fixtures. The entire framework is essentially 14 skill definitions with supporting prompts.

### Directory Naming Conventions

Kebab-case throughout. Directories are **capability-named** (named by what they teach the agent to do):

- `skills/brainstorming/` -- not `skills/design/` or `skills/ideation/`
- `skills/test-driven-development/` -- not `skills/tdd/`
- `skills/verification-before-completion/` -- not `skills/verification/`
- `skills/finishing-a-development-branch/` -- full phrases, not abbreviations

### Top-Level Structure

```
.
├── .claude-plugin/        # Claude Code marketplace integration
├── .codex/                # OpenAI Codex integration
├── .cursor-plugin/        # Cursor IDE integration
├── .opencode/             # OpenCode integration
├── agents/                # 1 agent definition (code-reviewer)
├── commands/              # 3 deprecated commands (→ skills)
├── docs/                  # Human docs + plans + design specs
├── hooks/                 # SessionStart hook + runner
├── scripts/               # Install/release scripts
├── skills/                # 14 skill directories (the core)
│   ├── brainstorming/
│   ├── dispatching-parallel-agents/
│   ├── executing-plans/
│   ├── finishing-a-development-branch/
│   ├── receiving-code-review/
│   ├── requesting-code-review/
│   ├── subagent-driven-development/
│   ├── systematic-debugging/
│   ├── test-driven-development/
│   ├── using-git-worktrees/
│   ├── using-superpowers/
│   ├── verification-before-completion/
│   ├── writing-plans/
│   └── writing-skills/
└── tests/                 # Test fixtures for skill behavior
```

### Notable Structural Patterns

1. **Plugin-first architecture**: Four platform integration directories (`.claude-plugin/`, `.cursor-plugin/`, `.codex/`, `.opencode/`) — designed as a cross-platform plugin from day one, not a single-harness tool.
2. **Skills-as-directories**: Each skill is a directory containing `SKILL.md` plus supporting files (subagent prompts, reference docs, visual companions). This is richer than GSD's flat agent files.
3. **No workflow layer**: Unlike GSD's three-layer hierarchy (commands -> workflows -> agents), Superpowers has only skills + 1 agent. Skills chain to each other directly.
4. **Deprecated commands**: `commands/` contains stubs pointing users to skills — indicates a migration from command-based to skill-based activation.
5. **Test fixtures as `.txt` files**: 15 text files in `tests/` — adversarial test scenarios for skill behavior verification.
6. **Meta-skill**: `writing-skills/` is a skill for writing skills — self-referential development methodology.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Constraints/Rules | Contributor guidelines: 94% PR rejection rate, quality gates, anti-slop rules |
| `AGENTS.md` | LLM | Global | Auto-loaded | Constraints/Rules | Identical to CLAUDE.md (cross-platform compatibility) |
| `GEMINI.md` | LLM | Global | Chain-loader | Constraints/Rules | @-references using-superpowers SKILL.md and gemini-tools.md |
| `skills/using-superpowers/SKILL.md` | LLM | Global | Injected (via SessionStart hook) | Workflow/Process + Constraints/Rules | Master skill: priority hierarchy, skill invocation rules, rationalization prevention |
| `skills/brainstorming/SKILL.md` | LLM | Task | Injected | Workflow/Process | Design-first process: explore context, ask questions, propose approaches, write spec |
| `skills/writing-plans/SKILL.md` | LLM | Task | Injected | Workflow/Process | Plan creation: bite-sized tasks, TDD, file structure mapping |
| `skills/subagent-driven-development/SKILL.md` | LLM | Task | Injected | Workflow/Process | Subagent orchestration: implementer per task + two-stage review |
| `skills/test-driven-development/SKILL.md` | LLM | Task | Injected | Constraints/Rules | TDD enforcement: delete pre-test code, Red-Green-Refactor |
| `skills/verification-before-completion/SKILL.md` | LLM | Task | Injected | Constraints/Rules | Verification: evidence before claims, rationalization prevention |
| `skills/systematic-debugging/SKILL.md` | LLM | Task | Injected | Workflow/Process | 4-phase debugging: root cause first, no guessing |
| `skills/executing-plans/SKILL.md` | LLM | Task | Injected | Workflow/Process | Sequential plan execution (alternative to subagent-driven) |
| `skills/dispatching-parallel-agents/SKILL.md` | LLM | Task | Injected | Workflow/Process | Parallel agent dispatching |
| `skills/finishing-a-development-branch/SKILL.md` | LLM | Task | Injected | Workflow/Process | Branch cleanup and completion |
| `skills/receiving-code-review/SKILL.md` | LLM | Task | Injected | Workflow/Process | Handling review feedback |
| `skills/requesting-code-review/SKILL.md` | LLM | Task | Injected | Workflow/Process | Initiating code review |
| `skills/using-git-worktrees/SKILL.md` | LLM | Tool | Injected | Tool Usage | Git worktree patterns |
| `skills/writing-skills/SKILL.md` | LLM | Tool | Injected | Workflow/Process | Meta-skill: how to write effective skills |
| `skills/writing-skills/persuasion-principles.md` | LLM | Global | Referenced | Constraints/Rules | 7 persuasion principles for skill design (based on Meincke et al. 2025) |
| `skills/subagent-driven-development/implementer-prompt.md` | LLM | Task | Referenced | Identity/Persona | Template for implementer subagent prompt |
| `skills/subagent-driven-development/spec-reviewer-prompt.md` | LLM | Task | Referenced | Identity/Persona | Template for spec compliance reviewer |
| `skills/subagent-driven-development/code-quality-reviewer-prompt.md` | LLM | Task | Referenced | Identity/Persona | Template for code quality reviewer |
| `skills/brainstorming/visual-companion.md` | LLM | Task | Referenced | Tool Usage | Browser-based visual mockup companion |
| `skills/brainstorming/spec-document-reviewer-prompt.md` | LLM | Task | Referenced | Identity/Persona | Spec review subagent template |
| `agents/code-reviewer.md` | LLM | Task | Injected | Identity/Persona | Senior Code Reviewer persona for post-step review |
| `hooks/session-start` | LLM | Global | Auto-loaded (hook) | Memory/State | SessionStart hook: injects using-superpowers as context |
| `hooks/hooks.json` | System | Global | Auto-loaded (config) | Tool Usage | Hook configuration for SessionStart |
| `README.md` | Human | Global | Referenced | Identity/Persona | Project overview, install, philosophy |

### Context Loading Strategy

**Hook-injected bootstrap + on-demand skill activation:**

1. **SessionStart hook** (`hooks/session-start`): On every session/clear/compact, a bash script runs that reads `using-superpowers/SKILL.md` and injects it as `additionalContext` wrapped in `<EXTREMELY_IMPORTANT>` tags. This is the ONLY skill loaded automatically — all others are on-demand.

2. **Skill invocation**: The `using-superpowers` skill instructs the agent to invoke skills via the `Skill` tool whenever there's "even a 1% chance a skill might apply." Skills are NOT `@`-referenced or chain-loaded — they're loaded on demand by the harness when the agent calls the Skill tool.

3. **Intra-skill references**: Skills reference supporting docs within their own directory (e.g., `brainstorming/visual-companion.md`, `subagent-driven-development/implementer-prompt.md`). These are read by the agent during skill execution, not pre-loaded.

4. **Cross-platform adaptation**: `GEMINI.md` uses `@` references, `AGENTS.md` duplicates `CLAUDE.md`, and platform-specific tool mapping docs exist in `skills/using-superpowers/references/`. The hook script detects platform (Cursor, Claude Code, Copilot CLI, Codex) and emits the appropriate JSON format.

**Key contrast with GSD**: GSD pre-loads context via `@`-reference chains (command -> workflow -> references). Superpowers loads ONE skill at session start and relies on the agent to self-activate other skills on demand. This is a pull model (agent decides what to load) vs. GSD's push model (harness assembles what the agent sees).

---

## 3. Workflow Topology

### Phases/Stages

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| **Brainstorm** | Any creative/implementation request | Spec written, committed, and user-approved | Yes -- user approves design after each section |
| **Write Plan** | Spec approved | Plan written with bite-sized tasks | No (auto from brainstorm) |
| **Execute** | Plan exists | All tasks implemented and reviewed | Checkpoints per task |
| **Review** | Step completed | Code reviewer approves | Yes -- two-stage review |
| **Verify** | About to claim completion | Fresh verification evidence exists | Hard gate -- no claims without evidence |
| **Finish** | All tasks done | Branch cleaned up, ready for merge | Yes -- human reviews final diff |

### Flow Diagram (ASCII)

```
┌───────────────────┐
│   BRAINSTORM      │──── Human: approves design sections
│  (spec document)  │──── Hard gate: NO implementation without approved spec
└────────┬──────────┘
         │
┌────────▼──────────┐
│   WRITE PLAN      │──── Auto-transition from brainstorm
│ (bite-sized tasks) │──── Scope check: decompose if too large
└────────┬──────────┘
         │
┌────────▼──────────┐
│   EXECUTE          │──── Per-task subagent dispatch
│  (per task):       │     ┌─────────────────────────┐
│  implement →       │     │ Implementer subagent     │
│  spec review →     │     │ Spec reviewer subagent   │
│  quality review    │     │ Quality reviewer subagent│
└────────┬──────────┘     └─────────────────────────┘
         │
┌────────▼──────────┐
│   VERIFY           │──── Hard gate: evidence before claims
│ (fresh evidence)   │──── No "should work", no "probably"
└────────┬──────────┘
         │
┌────────▼──────────┐
│   FINISH           │──── Human reviews final diff
│ (branch cleanup)   │
└───────────────────┘
```

### Transition Mechanisms

- **Skill chaining**: Each skill names the next skill to invoke. Brainstorming explicitly says "The ONLY skill you invoke after brainstorming is writing-plans." Writing-plans says to use `subagent-driven-development` or `executing-plans`.
- **Hard gates in skill text**: `<HARD-GATE>` XML tags block progression. Brainstorming's gate: "Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it."
- **Checklist-driven**: Skills with checklists require TodoWrite items per step. Progress is tracked by checking off items.
- **Self-activation**: The `using-superpowers` skill instructs the agent to activate skills whenever there's "even a 1% chance" one applies — the agent drives transitions, not the harness.

### Parallelism

- **Subagent-driven development**: Fresh subagent per task within a plan. Tasks are sequential by default but `dispatching-parallel-agents` skill enables parallel execution.
- **Two-stage review**: Spec compliance review and code quality review run sequentially per task (not parallelized).
- **Worktree isolation**: `using-git-worktrees` skill enables parallel work on different branches via git worktrees.

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| `<HARD-GATE>` XML tags | Skill files (inline) | Hard | "Do NOT invoke any implementation skill until design approved" |
| `<EXTREMELY_IMPORTANT>` tags | SessionStart hook injection | Hard | Skill invocation mandate |
| Iron Laws | Skill files (inline) | Hard | "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" |
| Red Flags tables | Skill files (inline) | Soft | "Using 'should', 'probably', 'seems to'" = STOP |
| Rationalization Prevention tables | Skill files (inline) | Soft | "I'm confident" → "Confidence ≠ evidence" |
| Anti-Pattern sections | Skill files (inline) | Soft | "This Is Too Simple To Need A Design" |
| Persuasion principles | `writing-skills/persuasion-principles.md` | Meta (design guidance) | 7 principles for designing effective constraints |
| Contributor guidelines | `CLAUDE.md`, `AGENTS.md` | Hard | 94% PR rejection rate, anti-slop rules |
| Instruction priority hierarchy | `using-superpowers/SKILL.md` | Hard | User instructions > Superpowers skills > System prompt |

### Guardrail Patterns

1. **Persuasion-engineered constraints**: Skills explicitly use persuasion psychology (authority, commitment, scarcity, social proof, reciprocity, liking, unity) based on Meincke et al. 2025 research showing 33%→72% compliance improvement. This is documented and deliberate, not accidental.
2. **Rationalization prevention**: Every discipline-enforcing skill (TDD, verification, debugging) includes a table of common rationalizations with rebuttals. "Just this once" → "No exceptions." "I'm confident" → "Confidence ≠ evidence."
3. **Hard gates via XML tags**: `<HARD-GATE>` and `<EXTREMELY_IMPORTANT>` tags serve as structural enforcement — positioned where the agent is most likely to skip a step.
4. **Iron Laws as anchors**: Single-line imperatives ("NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST") serve as memorable, non-negotiable rules. Placed prominently in each skill.
5. **Red Flags as detection patterns**: Tables of "thoughts that mean STOP" help the agent self-detect when it's about to rationalize skipping a rule.
6. **"Human partner" language**: Deliberate terminology choice — not "user" but "human partner" — frames the relationship as collaborative. Documented as a design decision that should not be changed.
7. **Explicit priority hierarchy**: User instructions > Superpowers skills > System prompt. Skills are powerful but the user always wins.

### Permission Model

- **No per-agent tool restrictions**: Unlike GSD, Superpowers does not restrict tools per skill. Any skill can use any tool available in the session.
- **Instruction priority**: User's CLAUDE.md/AGENTS.md/GEMINI.md > Superpowers skills > default system prompt.
- **Zero-dependency design**: No external packages, no MCP servers, no API calls. Pure markdown + hooks.
- **Plugin-scoped**: Skills operate within the session context. No persistent state beyond git.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Main agent (orchestrator) | Session context | All tools | Subagents via Task tool |
| Implementer subagent | `subagent-driven-development/implementer-prompt.md` | Task tool (general-purpose) | Main agent (results) |
| Spec reviewer subagent | `subagent-driven-development/spec-reviewer-prompt.md` | Task tool (general-purpose) | Main agent (pass/fail) |
| Code quality reviewer subagent | `subagent-driven-development/code-quality-reviewer-prompt.md` | Task tool (general-purpose) | Main agent (pass/fail) |
| Spec document reviewer subagent | `brainstorming/spec-document-reviewer-prompt.md` | Task tool (general-purpose) | Main agent (feedback) |
| Plan document reviewer subagent | `writing-plans/plan-document-reviewer-prompt.md` | Task tool (general-purpose) | Main agent (feedback) |
| Code reviewer agent | `agents/code-reviewer.md` | Dedicated agent definition | Main agent (review report) |

### Handoff Mechanisms

1. **Prompt-template based dispatch**: The main agent reads a prompt template file (e.g., `implementer-prompt.md`), fills in task-specific context, and dispatches a subagent via the Task tool. The template IS the handoff protocol.
2. **Full text embedding**: "Paste the full text of the task from the plan — don't make the subagent read the file." Context is embedded in the prompt, not referenced.
3. **Two-stage review loop**: After each task: implementer → spec reviewer → (fix if needed) → code quality reviewer → (fix if needed) → complete. Each reviewer is a fresh subagent.
4. **Skill chaining**: Skills name the next skill to invoke. This is a verbal handoff protocol — skills tell the agent what to do next in prose.

### Shared State

- **Git**: All agents operate on the same repo. Commits are the shared state mechanism.
- **TodoWrite**: Main agent tracks task progress via checklist items. Subagents don't see this.
- **Spec and plan files**: Written to `docs/superpowers/specs/` and `docs/superpowers/plans/`. These are the shared artifacts between brainstorming, planning, and execution.
- **No persistent state file**: Unlike GSD's STATE.md, Superpowers has no central state tracker. The main agent maintains state in its context window.

### Coordination Patterns

**Orchestrator-with-disposable-workers.** The main agent (session orchestrator) dispatches fresh subagents for implementation, review, and quality checks. Subagents are single-use: they do one task, return a result, and are discarded. The main agent maintains all coordination state in its context window.

Key differences from GSD's hub-and-spoke:
- **No workflow layer**: The main agent IS the orchestrator. GSD has separate workflow files.
- **Disposable subagents**: Subagents are generic (general-purpose Task tool), not named specialized agents. GSD has 24 named agent types.
- **Two-stage review per task**: Spec compliance then quality — more granular than GSD's single plan-checker.
- **No persistent state**: GSD writes STATE.md. Superpowers relies on context window + git.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Hook-based bootstrap injection (SessionStart → using-superpowers). Pull model: agent self-activates skills on demand vs. GSD's push model. Full-text embedding in subagent prompts ("don't make subagent read the file"). Platform-adaptive context injection (Cursor/Claude Code/Copilot/Codex/Gemini detection). |
| Model | Low | `model: inherit` on code-reviewer agent. No model-specific configuration or profiling. |
| Prompt | **High** | Persuasion-engineered skill design based on academic research (Meincke et al. 2025). Iron Laws as non-negotiable anchors. Red Flags tables for self-detection of rationalization. `<HARD-GATE>` and `<EXTREMELY_IMPORTANT>` XML tags for structural enforcement. "Violating the letter of this rule is violating the spirit" pattern. Graphviz `.dot` diagrams embedded in skill files for process visualization. |
| Tools | Medium | Cross-platform plugin architecture (Claude Code, Cursor, Codex, OpenCode, Copilot, Gemini). Skill tool as primary skill-activation mechanism. Visual companion (browser-based mockup tool) in brainstorming. |
| Intent | **High** | Brainstorming as mandatory pre-implementation gate: "EVERY project regardless of perceived simplicity." One question at a time. YAGNI ruthlessly. Scope decomposition for large projects. "Human partner" framing (not "user"). Explicit instruction priority hierarchy (user > skills > system). |
| Orchestration | **High** | Orchestrator-with-disposable-workers pattern. Two-stage review (spec compliance then quality) per task. Skill chaining via explicit next-skill naming. Self-activation ("1% chance → invoke skill"). No workflow layer — main agent orchestrates directly. |
| Evaluation | **High** | Verification-before-completion as Iron Law ("evidence before claims"). Red-Green-Refactor TDD enforcement with code deletion for violations. Two-stage review per task. Rationalization prevention tables. "Claiming work is complete without verification is dishonesty." |
| Sandboxing | Medium | Git worktree isolation for parallel development branches. No container/VM sandboxing. |
| Governance | **High** | Persuasion principles as explicit design methodology. XML-tag enforcement (`<HARD-GATE>`, `<EXTREMELY_IMPORTANT>`). Rationalization prevention (anticipating and blocking common evasion patterns). "94% PR rejection rate" as social proof. Instruction priority hierarchy. "Human partner" terminology as deliberate framing choice. |
| Agent Design | **High** | Skills-as-directories pattern (SKILL.md + supporting docs). Hook-injected bootstrap skill. Self-activation model ("1% chance → invoke"). Meta-skill (writing-skills for writing skills). Disposable subagents with prompt templates. Cross-platform agent identity (same skills, different harnesses). |

### Findings Candidates

1. **Persuasion-engineered skill design** (Prompt, Governance) — Superpowers explicitly applies 7 persuasion principles from academic research (Meincke et al. 2025, N=28,000) to skill design. Documents show 33%→72% compliance improvement. This is the most rigorous, research-backed approach to "how to write prompts that agents actually follow" in any repo we've analyzed. Potentially a standalone finding.
→ Promoted to [[persuasion-engineered-skill-design]] on 2026-04-08

2. **Rationalization prevention pattern** (Governance, Evaluation) — Every discipline-enforcing skill includes a table of rationalizations with rebuttals and a "Red Flags" table of thoughts that mean STOP. This anticipates and blocks the specific ways LLMs evade constraints. Distinct from GSD's gate taxonomy (which focuses on structural enforcement, not psychological).
→ Promoted to [[rationalization-prevention-pattern]] on 2026-04-08

3. **Pull-model context loading vs. push-model** (Context Engineering, Agent Design) — Superpowers injects ONE bootstrap skill and relies on the agent to self-activate others ("1% chance → invoke"). GSD pre-assembles context via `@`-reference chains. Fundamental architectural difference with tradeoffs worth analyzing.
→ Promoted to [[push-vs-pull-context-loading]] on 2026-04-08

4. **Brainstorming as mandatory design-first gate** (Intent, Evaluation) — Every project, regardless of perceived simplicity, must go through brainstorming before implementation. The `<HARD-GATE>` prevents any implementation skill from running before spec approval. Compare to GSD's discuss-phase (which is per-phase, not per-project, and focuses on implementation decisions rather than design exploration). This is the thinking/critical-thinking skill Nick flagged.
→ Promoted to [[brainstorming-as-mandatory-design-gate]] on 2026-04-08

5. **Two-stage review per task** (Evaluation, Orchestration) — Spec compliance review THEN code quality review, each by a fresh subagent. More granular than GSD's plan-checker (which reviews plans, not task outputs). Worth comparing to BMAD's review patterns.
→ Promoted to [[two-stage-sequential-review]] on 2026-04-08

6. **"Human partner" framing** (Agent Design, Governance) — Deliberate terminology: not "user" but "human partner." Documented as a design decision that should not be changed. Frames the agent-human relationship as collaborative rather than service-oriented. Subtle but affects agent behavior.
→ Promoted to [[human-partner-framing]] on 2026-04-08

7. **Meta-skill for skill authorship** (Agent Design, Prompt) — `writing-skills/` contains persuasion principles, Anthropic best practices, testing methodology, and examples. A skill that teaches agents how to write skills — self-referential capability development. No equivalent in GSD.
→ Promoted to [[meta-skill-for-skill-authorship]] on 2026-04-08

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v5.0.7 | all | Initial analysis. 142 files, 75 MD, 14 skills, 1 agent. Persuasion-engineered constraints, pull-model context loading. |
