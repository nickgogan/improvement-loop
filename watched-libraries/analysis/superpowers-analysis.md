---
title: "Superpowers -- Structural Analysis"
id: "superpowers-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-08"
updated: "2026-07-13"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "superpowers"
analyzed_version: "v6.1.1"
analyzed_date: "2026-07-13"
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
- **Version analyzed:** v6.1.1 (commit d884ae0, 2026-07-02)
- **Date:** 2026-07-13
- **Spectrum position:** thin-wrapper
- **Supersedes:** v5.0.7 analysis (2026-04-08). Re-run triggered by /watch-upstream registry refresh (registry Upstream Delta v5.0.7 → v6.1.1); primary driver is the v6.0.0 Subagent-Driven Development rewrite.

## What Superpowers Now Demonstrates That It Didn't at v5.0.7

Written for the restructure-program Phase 4/5 consumer. Six capabilities are new or fundamentally reshaped since the prior analysis:

1. **Unified single-reviewer with dual verdicts (v6.0.0).** The two-stage review — spec-compliance reviewer, then code-quality reviewer, each a fresh subagent — is gone. One `task-reviewer-prompt.md` reads the task's diff once and returns BOTH a spec-compliance verdict and a quality verdict, plus a new "⚠️ cannot verify from diff" verdict for requirements living in untouched code (the controller resolves those itself). One fix pass clears both verdicts. Upstream's evals: roughly 2x faster and ~50% fewer tokens vs v5.x at similar quality. Our v5 analysis and the KB finding that recorded "two-stage review" describe a superseded architecture.
2. **File-mediated subagent handoffs.** v5 said "paste the full text of the task — don't make the subagent read the file." v6 inverts this: three shell scripts (`task-brief`, `review-package`, `sdd-workspace`) write task briefs, implementer reports, and review diffs to a self-ignoring `.superpowers/sdd/` working-tree workspace (moved out of `.git/` in v6.0.3 because Claude Code write-protects `.git/`); the dispatch prompt carries file paths, not content. Rationale is context economy: "everything you paste into a dispatch prompt stays resident in your context for the rest of the session." Implementer return messages are capped under 15 lines — detail lives in the report file. This strongly corroborates our own file-mediated handoff protocol.
3. **Plans that carry their own contract (v6.0.0).** `writing-plans` now mandates a **Global Constraints** header block (project-wide requirements copied verbatim from the spec so they actually reach implementers and reviewers) and a per-task **Interfaces** block (Consumes/Produces with exact signatures, so an implementer who sees only its own task knows its neighbors' contracts), plus task right-sizing guidance ("the smallest unit that carries its own test cycle and is worth a fresh reviewer's gate"). The structure downstream agents used to re-derive on every dispatch is now authored once into the plan.
4. **Controller de-authorization.** v6 removes judgment calls the controller was gaming in real runs: every dispatch MUST name a model explicitly (an omitted model silently inherits the session's most expensive one — one observed run put all 26 reviewers on the top tier); the controller may not tell a reviewer what not to flag or pre-rate severity ("if the prompt you are writing contains 'do not flag'... stop"); a defect the plan itself mandates is reported as a finding for the human to adjudicate, never waved through; reviews are read-only on the checkout (a reviewer running `git checkout` had orphaned commits); and implementer rationales ("left it per YAGNI") never downgrade a finding.
5. **Whole-branch end review + durable progress ledger.** Per-task review is now a task-scoped gate; ONE broad whole-branch review runs at the end on the most capable model, fed a `review-package` for the full branch range. A progress ledger at `.superpowers/sdd/progress.md` survives compaction — controllers that lost context had re-dispatched entire completed task sequences, "the single most expensive failure observed."
6. **Vendor-neutral skill language + per-harness tool maps (v6.0.0/v6.1.0).** Skills no longer speak Claude Code's dialect: "use the Task tool" became "dispatch a subagent," "CLAUDE.md" became "your instructions file," "Claude" became "your agent," and "Claude Search Optimization" was renamed "Skill Discovery Optimization." Harness-specific detail moved to per-harness reference files under `skills/using-superpowers/references/` (now trimmed to codex/pi/antigravity — files with nothing harness-specific left were deleted in v6.1.0's bootstrap-compression pass). Three harnesses added (Kimi Code, Pi, Antigravity); Gemini CLI removed (Google EOL 2026-06-18). Behavior evals moved to a separate `superpowers-evals` repo using a "drill" framework that runs real harness sessions and judges them with an LLM.

**What has NOT changed (direction-note confirmation, verified against the clone):**
- The **brainstorming HARD-GATE is verbatim identical** to v5.0.7: "Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it. This applies to EVERY project regardless of perceived simplicity." The "This Is Too Simple To Need A Design" anti-pattern section is likewise unchanged. Additions around it are incremental: a spec self-review checklist, an explicit user-review gate on the written spec file, and just-in-time (not upfront) offering of the visual companion.
- **No thinking skills were added or removed.** The skill roster is the same 14 directories as v5.0.7. `systematic-debugging` keeps its 4-phase structure; its only change is a bug fix — one bullet accidentally contained the exact keyword Claude Code scans for to trigger extended thinking, silently forcing it on every session; a hyphen now breaks the keyword. The `using-superpowers` "1% chance → invoke" mandate and full Red Flags rationalization table survive the v6.1.0 bootstrap compression intact.
- TDD's Iron Law ("NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"), verification-before-completion's Iron Law, rationalization-prevention tables, persuasion principles, and "human partner" framing are all unchanged.

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value (v6.1.1) | v5.0.7 |
|--------|-------|--------|
| Total files | 171 | 142 |
| Total directories | 55 | 48 |
| Markdown files | 82 (48.0%) | 75 (52.8%) |
| Shell scripts (`.sh` + extensionless SDD scripts) | 39 | 26 |
| JSON files | 13 | 10 |
| JavaScript (`.js`, `.mjs`, `.cjs`) | 13 | 6 |
| Text files (`.txt`, test fixtures) | 9 | 15 |
| TypeScript (`.ts`) | 2 | — |
| Config (`.yml`, `.yaml`) | 3 | 2 |
| Other (`.py`, `.html`, `.dot`, `.cmd`, `.svg`, `.png`) | 6 | 5 |
| MD-to-code ratio (md : js/ts/py, v5 basis) | ~5.1:1 | 9.4:1 |
| Max directory depth | 4 | 4 |

The falling MD-to-code ratio reflects growth in glue code (brainstorm-server JS, Pi TypeScript extension, SDD shell scripts, packaging scripts), not a shift away from markdown-as-codebase — the behavioral core is still the 14 skills.

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skill definitions (SKILL.md) | 14 | `skills/*/SKILL.md` |
| Skill supporting docs (prompt templates, references, examples) | 22 | `skills/*/` (non-SKILL.md) |
| Human documentation | 34 | `docs/` (incl. 24 dogfooded specs/plans under `docs/superpowers/` and `docs/plans/`) |
| Root-level (README, CLAUDE, GEMINI, RELEASE-NOTES, CODE_OF_CONDUCT, AGENTS→CLAUDE symlink) | 6 | root |
| GitHub templates (PR + 3 issue templates) | 4 | `.github/` |
| Platform integration | 1 | `.opencode/INSTALL.md` |
| Test docs | 1 | `tests/claude-code/README.md` |
| **Total** | **82** | |

**Key insight**: The functional core is still 36 markdown files (14 SKILL.md + 22 supporting). Two v5 categories vanished: `agents/` (the sole named agent, code-reviewer, was merged into `skills/requesting-code-review/code-reviewer.md` as a dispatch template in v5.1.0) and `commands/` (the 3 deprecated command stubs were deleted in v5.1.0). The repo now has **zero named agents and zero commands** — everything behavioral is a skill or a prompt template owned by a skill. Notably, `docs/superpowers/specs+plans` is the project dogfooding its own workflow: 24 spec/plan documents produced by its own brainstorming/writing-plans skills, including the specs for the v6.0.0 SDD rewrite itself (`2026-06-10-strict-cost-sdd-design.md`, `2026-06-09-sdd-task-scoped-review-dispatch-design.md`).

### Directory Naming Conventions

Unchanged: kebab-case throughout; skill directories are capability-named full phrases (`finishing-a-development-branch`, not `finish`). New harness-integration dirs follow dot-prefixed harness naming (`.kimi-plugin/`, `.pi/`, `.codex-plugin/`, `.agents/plugins/` for the Codex marketplace manifest).

### Top-Level Structure

```
.
├── .agents/plugins/       # Codex marketplace manifest (v6.1.0)
├── .claude-plugin/        # Claude Code marketplace integration
├── .codex-plugin/         # OpenAI Codex plugin (was .codex/)
├── .cursor-plugin/        # Cursor IDE integration
├── .kimi-plugin/          # Kimi Code integration (v6.0.0)
├── .opencode/             # OpenCode integration
├── .pi/extensions/        # Pi session-start extension, TypeScript (v6.0.0)
├── assets/                # icons
├── docs/                  # Human docs + dogfooded specs/plans + porting guide
├── hooks/                 # SessionStart hook (Claude Code/Cursor/Copilot variants)
├── scripts/               # Install/release/packaging scripts
├── skills/                # 14 skill directories (the core; same set as v5.0.7)
└── tests/                 # Plugin-infrastructure tests (11 suites incl. per-harness)
```

Six harness plugin surfaces (Claude Code, Codex, Cursor, Kimi, OpenCode, Pi) plus Antigravity via direct install. Gemini support removed in v6.1.0 (Google EOLed the CLI), though a stale root `GEMINI.md` chain-loader remains (see Dimension 2).

### Code Surface Outline (optional — ast-grep)

Skipped — below size gate (~55 code files; gate is ≥ 200).

### Notable Structural Patterns

1. **Skills as the only behavioral abstraction.** With `agents/` and `commands/` deleted, every behavior is either a SKILL.md or a prompt-template file owned by a skill. Reviewer personas that were named agents are now inline dispatch templates (`skills/requesting-code-review/code-reviewer.md`).
2. **Runtime scratch workspace convention.** `.superpowers/sdd/` (created at runtime by `sdd-workspace`, self-ignoring via its own `.gitignore`) holds task briefs, implementer reports, review packages, and the progress ledger — per-worktree, out of `git status`, out of commits, and deliberately outside `.git/` because harnesses write-protect it.
3. **Executable helpers shipped inside a skill directory.** `skills/subagent-driven-development/scripts/` is the first skill to carry its own shell tooling — the skill's prose instructs the controller to run them rather than reproduce their output through its own context.
4. **Eval externalization.** Skill-behavior tests moved to a separate `superpowers-evals` repo ("drill" framework: real tmux sessions of Claude Code/Codex judged by an LLM verifier); in-tree `tests/` retains only plugin-infrastructure tests. The split is documented in `docs/testing.md`. The evals submodule was briefly shipped in v6.0.0 and removed in v6.0.2 because it broke plugin installs.
5. **Self-dogfooding artifact trail.** The specs and plans for Superpowers' own major changes live in `docs/superpowers/`, written by its own brainstorming/writing-plans workflow — a browsable audit trail of design → plan → release.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `CLAUDE.md` | LLM | Global | Auto-loaded | Constraints/Rules | Contributor guidelines, heavily expanded: "If You Are an AI Agent" pre-submission checklist, disclosure mandate (model/harness/plugins per PR), dev-branch targeting, will-not-accept list |
| `AGENTS.md` | LLM | Global | Auto-loaded | Constraints/Rules | Now a **symlink** to CLAUDE.md (was a duplicate copy at v5.0.7) |
| `GEMINI.md` | LLM | Global | Chain-loader (stale) | Constraints/Rules | @-references `using-superpowers/SKILL.md` and `references/gemini-tools.md` — the latter was **deleted** in v6.1.0 (Gemini EOL); orphaned entry point |
| `skills/using-superpowers/SKILL.md` | LLM | Global | Hook-injected (SessionStart) | Workflow/Process + Constraints/Rules | Bootstrap skill, compressed in v6.1.0 (3.1k): 1%-chance invocation mandate, Red Flags table, skill priority (process before implementation), platform-adaptation pointers. New `<SUBAGENT-STOP>` guard tells dispatched subagents to ignore it |
| `skills/using-superpowers/references/{codex,pi,antigravity}-tools.md` | LLM | Tool | Referenced | Tool Usage | Per-harness tool maps: action → harness tool (e.g. Codex `spawn_agent`/`wait_agent`/`close_agent`), environment detection, sandbox caveats. claude-code/copilot/gemini variants deleted in v6.1.0 |
| `skills/brainstorming/SKILL.md` | LLM | Task | Injected | Workflow/Process | Design-first process; HARD-GATE verbatim unchanged from v5.0.7; adds spec self-review, user spec-review gate, just-in-time visual-companion offer |
| `skills/writing-plans/SKILL.md` | LLM | Task | Injected | Workflow/Process | Plan creation; new mandatory Global Constraints header block, per-task Interfaces block, task right-sizing, No Placeholders list, plan self-review |
| `skills/subagent-driven-development/SKILL.md` | LLM | Task | Injected | Workflow/Process | SDD controller procedure (22k, ~3x its v5 size): pre-flight plan review, model selection rules, four-status handling, reviewer-prompt construction rules, file handoffs, durable progress ledger |
| `skills/subagent-driven-development/implementer-prompt.md` | LLM | Task | Referenced | Identity/Persona | Implementer dispatch template; reads task brief file; writes report file; returns <15 lines; four statuses; TDD red/green evidence |
| `skills/subagent-driven-development/task-reviewer-prompt.md` | LLM | Task | Referenced | Identity/Persona | **New in v6.0.0** — unified reviewer: spec compliance + code quality in one pass; replaces deleted `spec-reviewer-prompt.md` and `code-quality-reviewer-prompt.md`; read-only; "Do Not Trust the Report" skepticism; ⚠️ cannot-verify verdict; calibrated severity |
| `skills/requesting-code-review/code-reviewer.md` | LLM | Task | Referenced | Identity/Persona | Self-contained Senior Code Reviewer dispatch template (absorbed the deleted `agents/code-reviewer.md` in v5.1.0); used for the final whole-branch review; read-only mandate |
| `skills/test-driven-development/SKILL.md` (+ `testing-anti-patterns.md`) | LLM | Task | Injected | Constraints/Rules | Iron Law unchanged; now links the anti-patterns reference |
| `skills/verification-before-completion/SKILL.md` | LLM | Task | Injected | Constraints/Rules | Iron Law + gate function unchanged |
| `skills/systematic-debugging/SKILL.md` (+ 4 reference docs) | LLM | Task | Injected | Workflow/Process | 4-phase debugging unchanged; extended-thinking keyword defused (v6.0.0 fix) |
| `skills/executing-plans/SKILL.md` | LLM | Task | Injected | Workflow/Process | Inline alternative to SDD; now explicitly steers toward SDD when subagents are available |
| `skills/dispatching-parallel-agents/SKILL.md` | LLM | Task | Injected | Workflow/Process | Vendor-neutral "dispatch" vocabulary; same-response dispatches = parallel |
| `skills/using-git-worktrees/SKILL.md` | LLM | Tool | Injected | Tool Usage | Rewritten (v5.1.0/v6.0.0): environment detection, consent before creation, project-local `.worktrees/` default (global `~/.config/superpowers/worktrees/` removed) |
| `skills/finishing-a-development-branch/SKILL.md` | LLM | Task | Injected | Workflow/Process | Forge-neutral (no hardcoded `gh pr create`); provenance-based worktree cleanup |
| `skills/writing-skills/SKILL.md` (+ 3 references, examples) | LLM | Tool | Injected | Workflow/Process | Meta-skill; adds "Match the Form to the Failure" table and "Micro-Test Wording" method; "Claude Search Optimization" renamed "Skill Discovery Optimization" |
| `skills/writing-skills/persuasion-principles.md` | LLM | Global | Referenced | Constraints/Rules | Unchanged: 7 persuasion principles (Meincke et al. 2025) |
| `skills/brainstorming/visual-companion.md` (+ `scripts/`) | LLM | Task | Referenced | Tool Usage | Browser companion; v6.0.0 security model: per-session auth key, sandboxed file server, 4h idle timeout, restart survival |
| `hooks/session-start` | LLM | Global | Auto-loaded (hook) | Memory/State | Injects using-superpowers wrapped in `<EXTREMELY_IMPORTANT>`; emits platform-specific JSON (Cursor snake_case / Claude Code nested / Copilot+SDK top-level) |
| `hooks/hooks.json`, `hooks/hooks-cursor.json` | System | Global | Auto-loaded (config) | Tool Usage | Hook wiring; Codex hook removed in v6.1.0 (Codex triggers skills natively); v6.1.1 sets explicit `hooks: {}` in the Codex manifest to suppress auto-discovery |
| `.superpowers/sdd/*` (runtime) | LLM | Task | Referenced | Memory/State | Runtime-generated context files: task briefs, implementer reports, review packages, progress ledger — the file-mediated handoff substrate |
| `docs/porting-to-a-new-harness.md` | Human | Global | Referenced | Workflow/Process | 51k porting guide; the one rule: load the bootstrap at session start |
| `README.md` | Human | Global | Referenced | Identity/Persona | Overview, per-harness install |

### Sampling Notes

Read in full: `using-superpowers`, `brainstorming`, `writing-plans`, `subagent-driven-development` (+ both prompt templates and all 3 scripts), `executing-plans`, `verification-before-completion` (first 40 lines), `codex-tools.md`, `session-start` hook, `CLAUDE.md`, `GEMINI.md`, RELEASE-NOTES v5.1.0–v6.1.1. Classified by pattern + release-note deltas: the remaining 8 SKILL.md files and supporting docs (grep-verified for Iron Laws, HARD-GATE, phase structure, and rename markers).

### Context Loading Strategy

The v5 pull-model architecture is intact — SessionStart hook injects ONE bootstrap skill; all other skills self-activate on demand via the Skill tool — with three refinements:

1. **Bootstrap is now cost-managed.** v6.1.0 explicitly treats the injected bootstrap as a per-session tax and compressed it (graphviz diagram → prose, merged sections, trimmed platform pointers) without touching the behavior-shaping Red Flags content. The per-harness references were pruned on the same principle; reference files with nothing harness-specific left were deleted outright.
2. **Subagent context is file-assembled, not pasted.** The controller curates a dispatch of file paths (brief, report, review package) plus a thin prose frame (scene-setting, interfaces from earlier tasks, global constraints). Explicit anti-pattern: "a real session's dispatch hit 42k chars of which 99% was pasted history."
3. **Subagents opt out of the bootstrap.** The new `<SUBAGENT-STOP>` block at the top of `using-superpowers` prevents the skill-invocation mandate from recursing into dispatched workers.

One drift artifact: root `GEMINI.md` still chain-loads a reference file deleted in v6.1.0 — a dangling entry point for a harness that no longer exists.

---

## 3. Workflow Topology

### Phases/Stages

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| **Brainstorm** | Any creative/implementation request | Spec written, self-reviewed, committed, user-approved | Yes -- per-section design approval AND written-spec review gate |
| **Write Plan** | Spec approved | Plan with Global Constraints block, per-task Interfaces, bite-sized steps; self-reviewed | Execution-mode choice (subagent-driven vs inline) |
| **Pre-Flight Plan Review** (new v6.0.0) | Before Task 1 dispatch | Plan conflicts surfaced as one batched question, or clean scan | Yes, if conflicts found -- human adjudicates plan-vs-rubric contradictions |
| **Execute (per task)** | Plan exists | Implementer DONE + task reviewer approves both verdicts | No -- continuous execution, explicitly no between-task check-ins |
| **Task Review (per task)** | Implementer reports DONE | Spec ✅ + quality Approved (fix subagent loop until clean) | No (controller-mediated; plan-mandated defects escalate to human) |
| **Final Whole-Branch Review** (new v6.0.0) | All tasks complete | Final reviewer approves; one fix subagent for the full findings list | No (findings triage; Minor items via ledger) |
| **Verify** | About to claim completion | Fresh verification evidence | Hard gate -- unchanged Iron Law |
| **Finish** | All tasks done, reviews clean | Branch merged/PR'd/kept per user choice; provenance-based worktree cleanup | Yes -- human chooses disposition |

### Flow Diagram (ASCII)

```
┌───────────────────┐
│   BRAINSTORM      │── Human: approves design per section
│  (spec document)  │── HARD-GATE: no implementation before approval (verbatim v5)
│                   │── NEW: spec self-review + user reviews written spec file
└────────┬──────────┘
┌────────▼──────────┐
│   WRITE PLAN      │── NEW: Global Constraints block (verbatim spec values)
│ (bite-sized tasks)│── NEW: per-task Interfaces block (Consumes/Produces)
└────────┬──────────┘── NEW: task right-sizing (one test cycle per reviewer gate)
┌────────▼──────────┐
│ PRE-FLIGHT REVIEW │── NEW: scan plan for conflicts & plan-mandated defects;
│  (controller)     │        one batched question to human, else proceed
└────────┬──────────┘
┌────────▼────────────────────────────────────────────────┐
│  EXECUTE — per task, continuous (no between-task pauses) │
│   task-brief script ──► brief file                       │
│   dispatch implementer (explicit model) ──► report file  │
│   review-package script ──► diff file                    │
│   dispatch task reviewer (read-only)                     │
│     ├── spec verdict ✅/❌/⚠️  ── one reviewer,           │
│     └── quality verdict        ── two verdicts           │
│   ❌/Needs fixes ──► fix subagent ──► re-review          │
│   clean ──► append to progress ledger, next task         │
└────────┬────────────────────────────────────────────────┘
┌────────▼──────────┐
│ FINAL BRANCH      │── NEW: one whole-branch review, most capable model,
│ REVIEW            │        review-package(MERGE_BASE, HEAD); ONE fix
└────────┬──────────┘        subagent for the complete findings list
┌────────▼──────────┐
│   VERIFY          │── Iron Law unchanged: evidence before claims
└────────┬──────────┘
┌────────▼──────────┐
│   FINISH          │── forge-neutral; provenance-based worktree cleanup
└───────────────────┘
```

### Transition Mechanisms

Unchanged in kind: skill chaining by explicit next-skill naming ("The ONLY skill you invoke after brainstorming is writing-plans"), `<HARD-GATE>` tags, checklist-driven todos, self-activation via the bootstrap mandate. Changed in degree:

- **Script-mediated transitions.** Task → review transitions now pass through shell scripts (`task-brief`, `review-package`) whose printed file paths are the handoff tokens.
- **Status-protocol transitions.** Implementer statuses (DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT) each have a prescribed controller response, including an escalation ladder: more context → more capable model → decompose task → escalate to human.
- **Ledger-mediated resume.** After compaction, the progress ledger + `git log` — not conversation memory — determine where execution resumes.

### Parallelism

- Sequential-by-default task execution is unchanged; parallel implementation dispatches remain explicitly forbidden within SDD ("conflicts").
- `dispatching-parallel-agents` still covers independent parallel work (same-response dispatches run in parallel).
- The two-stage sequential review per task is gone — replaced by one reviewer pass, which is where most of the claimed 2x speedup comes from.
- Worktree isolation is now project-local (`.worktrees/`) with environment detection and consent, replacing the global worktree directory.

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| `<HARD-GATE>` XML tags | `brainstorming/SKILL.md` | Hard | Verbatim unchanged from v5.0.7 |
| `<EXTREMELY_IMPORTANT>` injection | SessionStart hook | Hard | Skill invocation mandate |
| `<SUBAGENT-STOP>` guard | `using-superpowers/SKILL.md` | Hard | New — bootstrap self-exempts dispatched subagents |
| Iron Laws | TDD, verification skills | Hard | Unchanged |
| Red Flags tables | Skill files (inline) | Soft | Unchanged in bootstrap; SDD adds 18-item Never list |
| Rationalization prevention tables | Skill files (inline) | Soft | Unchanged; scope tightened to discipline failures (v6.0.0) |
| Controller prohibition rules | `subagent-driven-development/SKILL.md` | Hard | New — no "do not flag," no severity pre-rating, mandatory model naming |
| Reviewer read-only mandate | Both reviewer templates | Hard | New — "Do not mutate the working tree, the index, HEAD, or branch state" |
| Reviewer skepticism rule | `task-reviewer-prompt.md` | Hard | New — "Do Not Trust the Report"; rationales never downgrade severity |
| Plan structure contract | `writing-plans/SKILL.md` | Hard | New — Global Constraints + Interfaces blocks; "No Placeholders" list framed as plan failures |
| Persuasion principles | `writing-skills/persuasion-principles.md` | Meta | Unchanged (Meincke et al. 2025) |
| Contributor guidelines | `CLAUDE.md` (AGENTS.md symlink) | Hard | Expanded — agent-addressed checklist, disclosure mandate, dev-branch rule |
| Eval-gated skill changes | `CLAUDE.md` + external `superpowers-evals` repo | Hard (process) | Skill-content PRs need before/after eval evidence; "skills are code that shapes agent behavior" |
| Instruction priority hierarchy | `using-superpowers/SKILL.md` | Hard | Unchanged: user instructions > skills > default behavior |

### Guardrail Patterns

All seven v5 patterns persist (persuasion-engineered constraints, rationalization prevention, XML hard gates, Iron Laws, Red Flags, "human partner" language, explicit priority hierarchy). New at v6:

1. **De-authorizing the orchestrator.** The most distinctive v6 governance move: constraints aimed at the *controller*, not the workers. Real-run evidence showed controllers gaming their own review process (coaching reviewers to skip findings, pre-rating severity, omitting model choices); v6 bans each observed evasion explicitly and moves the judgment into templates and scripts.
2. **Independence of review as an invariant.** Reviewers are read-only, skeptical-by-instruction, and shielded from controller influence; plan-mandated defects route to the human rather than being self-adjudicated ("the plan's authorship does not grade its own work").
3. **Evidence chains.** Findings require file:line citations; implementer reports carry TDD red/green command output; fix reports must name covering tests, command, and output before re-review dispatches.
4. **Failure-mode-derived rules.** Nearly every new rule cites its motivating incident inline (the 26-top-tier-reviewers run, the 42k-char dispatch, the orphaned-commits checkout, the re-dispatched completed tasks). Governance grows by post-mortem, and the rules carry their own rationale.
5. **Contributor-facing agent governance.** `CLAUDE.md` now opens with a section addressed directly to AI agents ("Stop. Read this section before doing anything."), a 6-step pre-submission checklist, and a mandatory authoring-environment disclosure — governance of agents *outside* the session, at the project boundary.
6. **Form-matching meta-governance.** "Match the Form to the Failure" (v6.0.0) codifies when prohibition-based bulletproofing works (discipline slips) vs backfires (wrong-shaped output → use worked examples), plus "Micro-Test Wording" for cheap A/B validation of phrasing against a no-guidance control.

### Permission Model

- Still no per-skill tool restrictions and still zero-dependency (no packages, no MCP servers).
- New read/write boundaries by role: reviewers read-only on the checkout; implementers write code + their own report file; the controller writes dispatches, the ledger, and runs the handoff scripts.
- Model selection is now a governed resource: dispatches must name a model; guidance maps task complexity to model tier; "turn count beats token price" (cheapest models take 2-3x the turns on multi-step work).
- Visual companion gained a real security model (v6.0.0): per-session auth key on every request/WebSocket, sandboxed file server (no symlinks/dotfiles/path escape), owner-only key files, 4h idle timeout.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Controller (main agent) | Session context + SDD SKILL.md | All tools; runs handoff scripts; explicitly de-authorized from review influence | All subagents via dispatch |
| Implementer subagent | `subagent-driven-development/implementer-prompt.md` | Code + tests + commits; writes report file | Controller (4-status protocol, <15-line return) |
| Task reviewer subagent | `subagent-driven-development/task-reviewer-prompt.md` | Read-only; dual verdicts (spec + quality) | Controller (structured report, file:line evidence) |
| Fix subagent | Dispatched ad hoc per findings | Fixes Critical/Important findings; appends to report file; re-runs covering tests | Controller |
| Final whole-branch reviewer | `requesting-code-review/code-reviewer.md` | Read-only; most capable model; full-branch package | Controller |
| Spec document reviewer | `brainstorming/spec-document-reviewer-prompt.md` | Spec critique | Controller |
| Plan document reviewer | `writing-plans/plan-document-reviewer-prompt.md` | Plan critique | Controller |

The v5 roster's named `code-reviewer` agent and the separate spec-reviewer/code-quality-reviewer pair are gone. Everything is `general-purpose` + prompt template + explicit model.

### Handoff Mechanisms

1. **File-mediated artifact exchange (the headline change).** Task text, implementer reports, and review diffs travel as files in `.superpowers/sdd/`: `task-brief PLAN N` → `task-N-brief.md`; implementer writes `task-N-report.md`; `review-package BASE HEAD` → `review-<base7>..<head7>.diff` (commit list + stat + `-U10` diff in one Read). The v5 doctrine — "paste the full text of the task, don't make the subagent read the file" — is explicitly inverted; briefs are extracted per task so no subagent ever reads the whole plan.
2. **Thin dispatch prompts over fat files.** A dispatch carries: one line of scene-setting, the brief path ("read this first — it is your requirements"), interfaces/decisions from earlier tasks, ambiguity resolutions, and the report-file path + contract. Exact values live only in the brief. Anti-pattern documented: pasting accumulated prior-task summaries.
3. **Structured status protocol.** DONE / DONE_WITH_CONCERNS / BLOCKED / NEEDS_CONTEXT, each with a prescribed controller response and an escalation ladder ending at the human.
4. **Review loop with evidence contract.** Fix dispatches carry the complete findings list (one fixer per review, not per finding — a per-finding fix wave "cost more than all its tasks combined"); fix reports must show covering tests + command + output before re-review.
5. **Skill chaining** remains the inter-phase handoff (prose naming of the next skill), now in vendor-neutral vocabulary.

### Shared State

- **`.superpowers/sdd/` workspace** — briefs, reports, review packages, progress ledger; per-worktree; self-ignoring; survives compaction but not `git clean -fdx` (documented, with `git log` as the recovery source).
- **Progress ledger** (`progress.md`) — one line per completed task with commit range; the controller's post-compaction recovery map, explicitly trusted over its own recollection.
- **Git** — commits remain the durable state; BASE SHAs recorded per task (never `HEAD~1`, which truncates multi-commit tasks).
- **TodoWrite** — still controller-only, now explicitly backed by the ledger because "conversation memory does not survive compaction."

### Coordination Patterns

**Orchestrator-with-disposable-workers, hardened into a constrained controller.** The v5 pattern survives, but v6 redistributes authority: judgment calls that v5 left to the orchestrator (model choice, review scope, severity, what to relay) are now fixed by templates, scripts, and prohibitions. The orchestrator becomes a logistics role — extract brief, record BASE, dispatch with model, package diff, route findings, keep the ledger — while quality judgment sits with independent read-only reviewers and conflict adjudication sits with the human. Cost architecture is explicit: per-task review is scoped narrow and cheap; breadth is concentrated in one end-of-branch review on the most capable model.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | File-mediated handoffs as context economy (dispatch carries paths, not content; "everything you paste stays resident"); bootstrap compression as per-session token-cost management (v6.1.0); brief extraction so subagents never read whole plans; review packages read in one call; `<SUBAGENT-STOP>` scoping of injected context; durable progress ledger as compaction-surviving memory |
| Model Selection | **High** (was Low) | Mandatory explicit model per dispatch (silent inheritance of the most expensive model named as the failure); task-complexity → model-tier mapping; "turn count beats token price" heuristic; final review pinned to the most capable model; review-model scaled to diff size/risk |
| Prompt Craft | **High** | Persuasion principles unchanged; "Match the Form to the Failure" (prohibitions for discipline slips, worked examples for shape failures); "Micro-Test Wording" (sample phrasings vs no-guidance control); accidental extended-thinking keyword trigger defused by a hyphen; reviewer templates carrying process rules so per-dispatch prompts stay thin |
| Tool Integration | **High** (was Medium) | Vendor-neutral action vocabulary ("dispatch a subagent") + per-harness tool maps as the portability layer; 7-harness support with per-harness bootstrap mechanisms (hook / native / extension); skill-owned shell scripts as controller tools; forge-neutral finishing; `hooks: {}` vs absent-field semantics (v6.1.1) as harness-config subtlety |
| Intent Engineering | **High** | Brainstorming HARD-GATE unchanged; spec self-review + user review gate on the written spec; Global Constraints block carrying verbatim spec values downstream; per-task Interfaces block as cross-task contract; pre-flight plan review batching conflicts into one human question |
| Orchestration | **High** | Unified single-reviewer with dual verdicts replacing two-stage review (~50% fewer tokens, ~2x faster per upstream evals); whole-branch end review; controller de-authorization; 4-status protocol with escalation ladder; one-fixer-per-review-wave rule; continuous execution (no between-task check-ins) |
| Evaluation | **High** | Reviewer independence invariants (read-only, skepticism, no controller coaching); ⚠️ cannot-verify-from-diff verdict; evidence chains (file:line, red/green output, covering tests before re-review); external eval repo with "drill" (real harness sessions + LLM judging); eval-gated skill-content changes; calibrated severity rubric with plan-mandated-defect escalation |
| Sandboxing | Medium | Read-only review as a checkout-level constraint; `.superpowers/sdd/` isolation outside `.git/` (harness write-protection); visual-companion security model (per-session key, sandboxed file server, idle timeout); project-local worktrees with consent |
| Governance | **High** | Failure-mode-derived rules citing their motivating incidents; de-authorization of the orchestrator; contributor-facing agent governance (agent-addressed CLAUDE.md, authoring-environment disclosure, acceptance-test transcript for new harnesses); positive-instruction redesign (dogfooded spec `2026-06-10-positive-instruction-redesign-design.md`); eval evidence as the bar for behavior-content changes |
| Agent Design | **High** | Skills as the sole behavioral abstraction (named agent + commands deleted); prompt-template-owned personas; skill-owned executable helpers; Skill Discovery Optimization (renamed from Claude Search Optimization); meta-skill additions for skill authors; "human partner" framing unchanged |
| Agentic Systems | Low | Single-project development workflow, not an operational multi-agent system; no scheduled loops or cross-session system assembly. (11.A Loop Engineering: the SDD review loop is single-run orchestration → D6, not a designed recurring cycle) |

### Findings Candidates

Suggestions only — promotion requires `/promote-findings` or `/research-loop`. Not promoted here.

1. **Unified dual-verdict reviewer supersedes two-stage review** (Orchestration, Evaluation) — v6.0.0 collapsed spec-reviewer + quality-reviewer into one `task-reviewer-prompt.md` returning both verdicts from one diff read, with a third ⚠️ cannot-verify verdict routing unverifiable requirements back to the controller. Upstream evals: similar quality, ~2x faster, ~50% fewer tokens. Directly supersedes our KB finding `two-stage-sequential-review` (promoted 2026-04-08) and the review architecture recorded in `superpowers-plugin-spec-driven-sub-agent-orchestra.md` — the KB needs a supersession pass, and DD-62's citation of two-stage review is stale (flagged in the watch-upstream report for Nick; DDs immutable).
   → Promoted to [[unified-dual-verdict-reviewer]] (carries a contradicts-link to [[two-stage-sequential-review]]; pre-existing findings untouched per the new-files-only constraint) on 2026-07-13
2. **File-mediated subagent handoff workspace** (Context Engineering, Orchestration) — task briefs, implementer reports, and review diffs move as files in a self-ignoring `.superpowers/sdd/` working-tree workspace created by shared scripts (`task-brief`, `review-package`, `sdd-workspace`); dispatch prompts carry paths + thin framing; implementer returns capped under 15 lines. Inverts the v5 "paste full text" doctrine on context-economy grounds. Strong corroboration of IL's own file-mediated handoff protocol (`agents/handoff-protocol.md`) from an independent, eval-backed source.
   → Promoted to [[file-mediated-subagent-handoff-workspace]] (cross-repo: BMAD compact-summary returns and spec-file protocol cited as corroboration) on 2026-07-13
3. **Controller de-authorization / reviewer independence invariants** (Governance, Evaluation) — bans on coaching reviewers ("do not flag"), pre-rating severity, and skipping model choice; read-only reviews; implementer rationales never downgrade findings; plan-mandated defects escalate to the human ("the plan's authorship does not grade its own work"). Each rule cites the real failure that motivated it. A rare worked example of generator-assessor separation enforced against the *orchestrator* — resonates with our generator-assessor standing rule.
   → Promoted to [[controller-deauthorization-reviewer-independence]] on 2026-07-13
4. **Mandatory explicit model-per-dispatch with tiering heuristics** (Model Selection) — omitted models silently inherit the session's most expensive one (observed: all 26 reviewers on top tier); templates hard-require a model; complexity→tier mapping plus "turn count beats token price" (cheap models take 2-3x turns on multi-step work, costing more). Candidate input for the model capability registry's delegation guidance.
   → Promoted to [[mandatory-explicit-model-per-dispatch]] on 2026-07-13
5. **Plans that carry their own contract: Global Constraints + per-task Interfaces blocks** (Intent Engineering, Orchestration) — project-wide requirements copied verbatim into a plan header and per-task Consumes/Produces signatures, so context-isolated implementers and reviewers receive binding constraints without re-derivation. Upstream testing: structured plans needed one fix round vs two-to-four for control (which also shipped a real bug).
   → Promoted to [[plans-that-carry-their-own-contract]] (cross-repo: BMAD sealed file contracts cited as convergence) on 2026-07-13
6. **Durable progress ledger for compaction recovery** (Context Engineering) — one appended line per completed task (commit range + review status) in the scratch workspace; on resume, the ledger and `git log` outrank the agent's own recollection. Motivated by "the single most expensive failure observed": controllers re-dispatching entire completed task sequences after context loss.
   → Promoted (merged) into [[append-only-run-log-as-working-memory]] together with BMAD candidate 1 (memlog) — one cross-repo finding on 2026-07-13
7. **Vendor-neutral skill vocabulary with per-harness tool maps** (Tool Integration, Agent Design) — skills rewritten to action language ("dispatch a subagent," "your instructions file"), with harness-specific mappings isolated in per-harness reference files that are deleted when they carry nothing harness-specific. The portability layer that let one skill set add Kimi/Pi/Antigravity and drop Gemini without touching skill bodies. Relevant to `/meta-skill-author`'s porting concern and the DD-92 universal-vocabulary requirement.
   → Promoted to [[vendor-neutral-skill-vocabulary-per-harness-tool-maps]] on 2026-07-13
8. **Behavior evals externalized to real-session LLM-judged harness ("drill")** (Evaluation) — skill-behavior tests moved to a separate repo that drives real tmux sessions of multiple harnesses and judges compliance with an LLM verifier; in-tree tests retained only for plugin infrastructure; skill-content PRs require before/after eval evidence. A concrete architecture for "prompts are code, so eval them like code."
   → Promoted to [[externalized-real-session-behavior-evals]] on 2026-07-13
9. **Bootstrap compression as recurring token-cost maintenance** (Context Engineering) — v6.1.0 treats the always-injected bootstrap as a standing per-session tax and shrinks it (diagram→prose, section merges, reference pruning) while explicitly preserving behavior-shaping content. Same economic reasoning as our token-economy standing rule, applied to hook-injected context.
   → Skipped: already-adopted practice (token-economy standing rule, /simplify-context); corroboration only on 2026-07-13
10. **Extended-thinking keyword as accidental context trigger** (Prompt Craft, minor) — a skill bullet containing the exact keyword Claude Code scans for silently forced extended thinking on every session that loaded the skill; fixed by hyphenating the word. A concrete instance of harness keyword-scanning interacting destructively with instruction prose — cheap, memorable defect class for skill authors.
    → Skipped: minor single-incident defect class; observational on 2026-07-13

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v5.0.7 | all | Initial analysis. 142 files, 75 MD, 14 skills, 1 agent. Persuasion-engineered constraints, pull-model context loading. |
| 2026-07-13 | v6.1.1 | all | Re-run after v6.0.0 SDD rewrite (registry Upstream Delta). 171 files, 82 MD, same 14 skills, 0 named agents/commands. Unified dual-verdict reviewer replaces two-stage review; file-mediated handoffs in `.superpowers/sdd/`; Global Constraints + Interfaces plan blocks; whole-branch end review; controller de-authorization; vendor-neutral skill language + per-harness tool maps; brainstorming HARD-GATE and thinking-skill surfaces confirmed unchanged. 10 finding candidates (not promoted). |
