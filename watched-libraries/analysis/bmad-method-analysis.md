---
title: "BMAD Method -- Structural Analysis"
id: "bmad-method-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
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
  - "bmad-method"
analyzed_version: "v6.10.0"
analyzed_date: "2026-07-13"
repo_url: "https://github.com/bmad-code-org/BMAD-METHOD"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
  - "research-dimension-mapping"
---

# BMAD Method -- Structural Analysis

## Metadata
- **Repo:** <https://github.com/bmad-code-org/BMAD-METHOD>
- **Version analyzed:** v6.10.0 (2026-07-03; clone HEAD 8ea1b76, 2026-07-12)
- **Date:** 2026-07-13
- **Spectrum position:** cherry-pick

This re-run supersedes the v6.2.2 analysis (2026-04-08). Special attention in this pass
(per the agentic-OS direction note, feeding restructure-program Phases 4/5): the new
critical-thinking skill layer (forge-idea, investigate, prfaq, anti-consensus party-mode),
the governance primitives (decision-log/memlog, four-layer TOML resolver,
checkpoint-preview), the rebuilt product layer (spec kernel, prd/brief three-intent,
architecture lean spine), the persona consolidation, and the bmad-loop autonomous dev
module. See "What BMAD now demonstrates that it didn't at v6.2.2" below.

**Scope note:** `bmad-loop` (the unattended-dev orchestrator) lives in a separate
marketplace-plugin repo, not in BMAD-METHOD; only its worker skill `bmad-dev-auto` is in
this repo. `bmad-investigate` (added v6.7.0) was **retired in v6.10.0** — the registry
entry's delta section lists it as a current skill; this analysis corrects that.

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | v6.10.0 | v6.2.2 (prior) |
|--------|---------|----------------|
| Total files | 590 | 559 |
| Total directories | 165 | 144 |
| Markdown files | 395 (67%) | 418 (74.8%) |
| JS/MJS files | 61 | 48 |
| TOML files | 37 | 5 |
| Python files | 16 | 1 |
| YAML files | 19 | 26 |
| CSV files | 14 | 18 |
| MD-to-code ratio | ~5:1 | 8.5:1 |
| Max directory depth (repo-relative) | 6 | 7 |

Code grew (installer hardening + a new Python governance-script layer: `memlog.py`,
`resolve_config.py`, `resolve_customization.py`, `lint_spine.py`, per-skill resolvers,
plus tests) while markdown shrank despite six more skills — the direct signature of the
skill-flattening described below.

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Skill definitions (SKILL.md entrypoints) | 47 | `src/bmm-skills/` (33), `src/core-skills/` (14) |
| Step files (workflow steps) | 35 | 10 skills only (research x3, check-readiness, epics, project-context, checkpoint-preview, code-review, dev-auto, quick-dev) |
| Workflow orchestrators | 1 | `bmad-quick-dev/workflow.md` (last survivor) |
| Skill references (on-demand procedure modules) | 26 | `src/*/references/` |
| Skill assets (templates, schemas, examples) | 19 | `src/*/assets/` |
| Templates (other `*template*.md`) | 18 | `src/*/` |
| Agent sub-definitions | 2 | `bmad-prfaq/agents/` (only skill retaining a subagent dir) |
| Human documentation (en + i18n cs/fr/vi-vn/zh-cn) | 174 | `docs/` |
| Web bundles (Gemini Gems / Custom GPTs) | 16 | `web-bundles/` |
| Tools/test/community files | ~21 | `tools/`, `test/`, `.github/`, root |

**Key structural shift since v6.2.2 — skill flattening.** The v6.2.2 signature was the
step-file micro-architecture: 22 `workflow.md` orchestrators fanning into 112 numbered
step files with just-in-time loading. At v6.10.0 that is down to 1 workflow.md and 35
step files, confined to mechanical execution skills. The rebuilt flagship skills
(bmad-prd, bmad-spec, bmad-architecture, bmad-ux, bmad-product-brief, bmad-forge-idea,
bmad-party-mode) are each a **single outcome-driven SKILL.md** (~85–160 lines) plus
`references/` modules loaded per intent, `assets/` templates, and a `customize.toml`.
The v6.7.0+ changelogs call the old shape "five-stage scripted workflow" and the new one
"a single outcome-driven SKILL.md." Sequencing rigidity was traded for judgment-driven
prose plus deterministic side-rails (scripts, linters, reviewer gates).

### Directory Naming Conventions
Kebab-case throughout; phase-numbered module folders (`1-analysis` … `4-implementation`)
retained. Skills prefixed `bmad-`. Uniform per-skill anatomy: `SKILL.md` +
`customize.toml` (+ optional `references/`, `assets/`, `scripts/`, step files).

### Top-Level Structure
```
.
├── .augment/  .claude-plugin/  .github/  .husky/  .vscode/
├── docs/               # human docs + i18n (cs, fr, vi-vn, zh-cn)
├── src/
│   ├── bmm-skills/     # 33 skills in 4 numbered SDLC phases
│   ├── core-skills/    # 14 cross-phase skills (incl. forge-idea, spec, party-mode)
│   └── scripts/        # shared governance primitives: memlog.py, resolve_config.py (+tests)
├── test/               # incl. adversarial-review-tests/
├── tools/              # installer, skill validator, docs tools
├── web-bundles/        # 6 planning bundles for Gemini Gems / Custom GPTs
└── website/            # Astro 6 docs site
```

### Code Surface Outline (optional — ast-grep)
Skipped — below size gate (79 code files; gate is ≥200). Find-based stats above are the baseline.

### Notable Structural Patterns
1. **Uniform skill anatomy with a customization sidecar.** Every one of the 47 skills
   carries a `customize.toml` (37 in src; agent skills use an `[agent]` table, workflow
   skills a `[workflow]` table) declaring `activation_steps_prepend/append`,
   `persistent_facts`, `on_complete`, output paths, and reviewer rosters. The skill body
   reads its own merged config at activation — behavior extension without forking.
2. **Shared script layer as a first-class module.** `src/scripts/` is new: `memlog.py`
   (append-only working memory) and `resolve_config.py` (four-layer TOML merge) install
   to `{project-root}/_bmad/scripts/` and are invoked by name from skill prose via
   `uv run`. BMAD is standardizing Python invocation on `uv` (v7 breaking change
   pre-announced in v6.9.0).
3. **Run-folder workspaces.** Flagship skills bind a per-run workspace folder
   (`{output_path}/{run_folder_pattern}`) holding the artifact, its `.memlog.md`, and
   review/reconcile files — same-slug reinvocation resumes in place.
4. **Web bundles as a parallel packaging target.** Six planning skills re-packaged for
   Gemini Gems/Custom GPTs with schema parity so Gem ↔ IDE handoffs don't break.
5. **42 platform targets** via the cross-tool `.agents/skills/` standard (up from 7).

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|-----------|----------|-------|-----------|--------------|---------|
| `AGENTS.md` (root, 12 lines) | LLM | Global | Auto-loaded | Constraints/Rules | Conventional commits; `npm run quality` before push; points to skill-validator |
| `src/*/SKILL.md` (47) | LLM | Tool | Auto-loaded | Identity/Persona + Workflow | Skill entrypoints; agent skills carry persona; workflow skills carry the full outcome-driven procedure |
| `src/*/customize.toml` (37) | LLM (via resolver) | Tool | Referenced | Constraints/Rules + Memory/State | Per-skill override surface: activation hooks, persistent_facts, reviewer rosters, paths |
| `_bmad/config.toml` 4-layer set (installed) | LLM (via `resolve_config.py`) | Global | Referenced | Constraints/Rules | Central config: team/user x installer-owned/human-authored; structural merge |
| `src/*/references/*.md` (26) | LLM | Task | Referenced | Workflow/Process | Intent-scoped procedure modules (headless.md, validate.md, reviewer-gate.md, mode-*.md) loaded on demand |
| `src/*/assets/*.md` (19) | LLM | Tool | Referenced | Memory/State | Templates and schemas (spec-template, spine-template, stories-schema, headless-schemas) |
| `src/*/step-*.md` (35) | LLM | Task | Referenced | Workflow/Process | Sequential steps, retained only in mechanical execution skills |
| `src/bmm-skills/1-analysis/bmad-prfaq/agents/*.md` (2) | LLM | Task | Injected | Identity/Persona | Last remaining in-repo subagent definitions |
| `.memlog.md` (per run folder, installed projects) | LLM | Task | Referenced | Memory/State | Append-only working memory; read only on resume; artifacts derived from it |
| `project-context.md` (installed projects) | LLM | Project | Referenced | Memory/State | Shared project context; default `persistent_facts` entry across skills |
| `tools/skill-validator.md` | Both | Global | Referenced | Constraints/Rules | 26 rule IDs across PATH/REF/SEQ/SKILL/STEP/TPL/WF families |
| `web-bundles/*/**.md` (16) | LLM | Global | Auto-loaded (web platform) | Identity/Persona + Workflow | Gem/GPT instruction + knowledge files, schema parity with IDE skills |
| `docs/**/*.md` (174) | Human | Global | Referenced | Workflow/Process | Human docs + 4 translations |

### Sampling Notes
Read in full: 8 SKILL.md exemplars (forge-idea, spec, party-mode, prd, architecture,
agent-dev, dev-auto, checkpoint-preview), `memlog.py`, `resolve_config.py`, root
`AGENTS.md`, `docs/reference/agents.md`, party-mode `customize.toml` (anti-consensus
room), forge-idea `customize.toml`, dev-auto `step-04-review.md`, full CHANGELOG
v6.3.0–v6.10.0. Remaining 39 skills classified by the uniform anatomy pattern
(identical activation protocol confirmed across the exemplars).

### Context Loading Strategy
Still three-level progressive disclosure (L1 frontmatter, L2 SKILL.md body, L3
resources), but the L3 layer changed character: intent-scoped `references/` modules
(load `validate.md` only under Validate intent; `headless.md` only when headless)
replaced forward-chained step files. Three new cross-cutting context mechanisms:

1. **Config resolution at activation** — every skill's step 1 runs
   `resolve_customization.py`, with a documented in-prose fallback (read three TOML
   layers yourself and apply the same merge rules) so a missing script degrades
   gracefully rather than blocking.
2. **`persistent_facts`** — a per-skill, user-overridable list of standing context
   (literal facts, `file:` globs, `skill:` pointers) held for the whole run; default
   loads `project-context.md`. This is user-injectable context as a governed config
   field rather than prompt editing.
3. **Memlog-mediated state** — the run's decisions live in `.memlog.md` (write-only
   during the session, read only on resume); the parent context never re-reads its own
   history mid-run because every `memlog.py` call echoes state as one JSON line.

Activation-sequence integrity is itself guarded: v6.8.0 strengthened 23+ skills against
LLMs short-circuiting the activation chain ("guessing variables instead of executing in
order") — an explicit acknowledgment that prompt-defined boot sequences drift and need
confirmation steps.

---

## 3. Workflow Topology

### Phases/Stages
| Phase | Entry Trigger | Exit Condition | Human Gate? |
|-------|--------------|----------------|-------------|
| 0. Idea forge (new, optional) | `bmad-forge-idea` | Idea Hardened / Killed / Clearer; optional `forged-idea.md` | Yes — user is the interrogated party |
| 1. Analysis | Analyst/researcher skills; `bmad-prfaq` | Brief, research docs, PRFAQ | Yes |
| 2. Plan | `bmad-prd` (Create/Update/Validate), `bmad-ux` | PRD + addendum; DESIGN.md + EXPERIENCE.md | Yes — coaching default, reviewer gate |
| 2.5. Spec distillation (new, cross-phase) | `bmad-spec` from any intent input | SPEC.md five-field kernel + companions (+ stories.yaml) | Yes interactive; headless returns JSON |
| 3. Solutioning | `bmad-architecture` (Create/Update/Validate) | ARCHITECTURE-SPINE.md, epics/stories | Yes — coaching default, reviewer gate, lint |
| 4. Implementation (attended) | Amelia menu: dev-story, quick-dev, code-review, sprint-* | Stories implemented, reviewed | Yes — incl. `bmad-checkpoint-preview` |
| 4-auto. Implementation (unattended, new) | `bmad-dev-auto` invoked per iteration (by bmad-loop or directly) | Spec frontmatter reaches terminal status | **No** — explicitly no-human; HALT protocol instead |

### Flow Diagram (ASCII)
```
            ┌────────────────┐
            │ 0. FORGE IDEA  │  Socratic pressure-test; attack/defend modes
            │ (optional)     │  exits: HARDENED / KILLED / CLEARER
            └───────┬────────┘
                    │ forged-idea.md (optional)
   ┌────────────────▼─────────────────────────────┐
   │ 1. ANALYSIS   Mary / Paige / PRFAQ / research│
   └────────────────┬─────────────────────────────┘
                    ▼
   ┌──────────────────────────────────────────────┐
   │ 2. PLAN       bmad-prd (C/U/V, Fast|Coaching)│
   │               bmad-ux → DESIGN.md+EXPERIENCE │
   └────────────────┬─────────────────────────────┘
                    ▼
        ┌───────────────────────┐
        │ bmad-spec (any order) │  five-field kernel; single writer;
        │ SPEC.md + companions  │  derived from .memlog.md
        └───────────┬───────────┘
                    ▼
   ┌──────────────────────────────────────────────┐
   │ 3. SOLUTIONING  bmad-architecture (C/U/V)    │
   │   ARCHITECTURE-SPINE.md → adopted companion  │
   └────────────────┬─────────────────────────────┘
                    ▼
   ┌───────────────────────────────┬──────────────────────────────┐
   │ 4. IMPLEMENTATION (attended)  │ 4-auto (unattended)          │
   │ Amelia: dev-story, quick-dev, │ bmad-loop (external module)  │
   │ code-review, sprint-*,        │   polls spec frontmatter →   │
   │ checkpoint-preview [human]    │   bmad-dev-auto per iteration│
   └───────────────────────────────┴──────────────────────────────┘

Cross-phase: brainstorming (108 techniques, 3 modes), advanced elicitation
(71 methods), party-mode (incl. anti-consensus club), editorial/adversarial
reviews, edge-case hunter, verification-gap review, shard-doc, customize, help.
```

### Transition Mechanisms
- **User-initiated persona menus** persist (Amelia et al. render a menu, HALT, dispatch
  on code/fuzzy match — but now skip the menu when the opening message names the intent).
- **Intent detection replaced fixed pipelines**: Create/Update/Validate detected from
  conversation + input shape; the input artifact itself tells the skill what job it is
  ("read the input to know the job" — a spec package, raw idea, codebase, or existing
  spine each route differently).
- **Sealed file contracts**: downstream skills discover their inputs via SPEC.md
  frontmatter (`companions:`, `sources:`), stable IDs (CAP-N, AD-n, FR IDs), and fixed
  file names (SPEC.md, stories.yaml, .memlog.md) rather than conversational handoff.
- **Spec-frontmatter state machine** (unattended branch): `status:` in the story spec's
  frontmatter is the transition variable; an orchestrator polls it; `final_revision`
  written at exit is the only link from an out-of-tree spec to its in-tree commits.
- **Forwarding shims**: legacy skills (create-prd, edit-prd, validate-prd,
  create-architecture) route to the consolidated skill with the proper intent;
  removal scheduled for v7.

### Parallelism
- **Reviewer gates** dispatch rubric walker + configured reviewer lenses as parallel
  subagents; each writes `review-{slug}.md` and returns only a compact summary.
- **dev-auto review layers** run in parallel with an explicit synchronicity mandate:
  "several blocking calls awaited together in one turn — never backgrounded," because
  unattended runs have no event loop to resume a yielded turn.
- **party-mode** offers four run modes (session / auto / subagent / agent-team) with
  graceful degradation to inline voicing when a mechanism isn't available.
- Phases remain sequential for a given artifact, but the spec-kernel design explicitly
  allows PRD/UX/architecture/epics to run **in any order** against the same spec because
  the append-only memlog absorbs their contributions without merge drift.

---

## 4. Governance Model

### Constraint Expression
| Mechanism | Location | Enforcement | Example |
|-----------|----------|-------------|---------|
| AGENTS.md project rules | root `AGENTS.md` | Hard (CI mirror) | Conventional commits; `npm run quality` before push |
| Skill validator | `tools/skill-validator.md` + `validate-skills.js` (in `npm run quality`) | Hard (deterministic) + Soft (inference) | 26 rule IDs: PATH-01..05, REF-01..03, SEQ-01..02, SKILL-01..07, STEP-01..07, TPL-01, WF-03; deprecated shims exempted from trigger-phrase check |
| Four-layer TOML config | `_bmad/config.toml` → `config.user.toml` → `custom/config.toml` → `custom/config.user.toml` via `resolve_config.py` | Hard (script) with documented prose fallback | Scalars override, tables deep-merge, `code`/`id`-keyed arrays merge by key, other arrays append |
| Per-skill customize.toml | every skill dir + `_bmad/custom/{skill}.toml` overrides | Hard (resolver) | `activation_steps_prepend/append`, `persistent_facts`, `on_complete`, reviewer rosters |
| Memlog invariants | `_bmad/scripts/memlog.py` | Hard (by construction) | No edit/delete subcommand exists; atomic temp+fsync+rename writes; no lifecycle status field |
| Derived-artifact rule | bmad-spec / bmad-prd / bmad-architecture prose | Soft (stated) + structural | "SPEC.md … DERIVED from .memlog.md, never hand-edited"; bmad-spec is its single writer; hand-edits overwritten on next derive |
| Spec Law | `bmad-spec` SKILL.md | Soft, self-validated | 8 rules (intent+success per capability; WHAT not HOW; constraints must bind; explicit non-goals; testable success signal; stable IDs; preservation; lean prose) |
| Spine linter | `bmad-architecture/scripts/lint_spine.py` (28 regression tests) | Hard (deterministic pass in reviewer gate) | Structural checks on ARCHITECTURE-SPINE.md before rubric/lens review |
| Review scope authority | `bmad-dev-auto/step-04-review.md` | Hard (routing rule) | Only the intent itself may authorize defer/reject-as-out-of-scope; spec language, plan, and diff shape are inadmissible |
| Severity authority | same | Hard | Parent discards subagent-assigned severity — reviewers operate under "by-design information asymmetry" |
| Anti-sycophancy protocol | `bmad-forge-idea` | Soft | "Praise is noise"; agreement only when it helps thinking; in attack mode never agree until user ends the mode |
| Persona persistence | agent SKILL.md files | Soft | Unchanged from v6.2.2; icon-prefix requirement added for visual identifiability |

### Guardrail Patterns
1. **Deterministic side-rails around judgment-driven prose.** The flattened skills lost
   step-sequencing enforcement but gained scripts and linters at the boundaries:
   memlog.py (state), lint_spine.py (artifact shape), resolve_config.py (config),
   validate-skills.js (skill quality), plus reviewer gates before finalize.
2. **Append-only memory as audit trail.** Every flagship workflow logs each decision,
   assumption, override, and terminal event as a one-line memlog entry as it happens;
   the finalize sequence starts with a "memlog audit" walking the log with the user.
   The changelog frames the v6.7.0 `.decision-log` pattern as canonical across
   workflows; v6.9.0 replaced per-skill decision logs with the one shared memlog script.
3. **Human review as a dedicated skill.** `bmad-checkpoint-preview` structures
   commit/branch/PR review for a human: concern-ordered walkthrough, clickable
   `path:line` refs, "front-load then shut up" delivery rule, explicit HALT between
   steps (a v6.3.0 bug fix added the HALT after the skill advanced without confirmation).
4. **Stakes-calibrated rigor.** Reviewer gates scale to stakes (hobby runs may skip;
   launch-grade gets the full menu); PRD length scales with stakes; opt-in reviewer
   gates avoid "auto-spend on parallel reviewers for hobby work."
5. **Graceful degradation everywhere.** Missing config keys take neutral defaults and
   "never block"; failed memlog init downgrades to in-conversation state with a warning;
   missing script triggers the documented manual merge fallback; unavailable party modes
   fall back to session voicing. Halting is reserved for unattended runs (HALT protocol
   with terminal status + blocking condition).
6. **Model parity for reviewers** (v6.4.0): code-review subagents must match the
   orchestrator session's model capability — rare-event detection degrades on cheaper
   models. (Party-mode, by contrast, explicitly favors cheaper models for persona
   subagents — different job, different floor.)

### Permission Model
- Still no per-skill tool allowlists; skills assume full tool access.
- Boundaries are expressed as **write-ownership rules** instead: bmad-spec is SPEC.md's
  single writer; adopted companions are read-only to the adopting skill; inherited
  parent-spine ADs are "binding, read-only" for child spines (a conflicting local AD is
  "a conflict to surface, not a local override"); dev-auto's diff construction is
  read-only ("Do NOT git add anything").
- User-owned override surface is filesystem-partitioned: installer-owned files are
  regenerated on update (`# DO NOT EDIT`), human-authored overrides live in
  `_bmad/custom/` (team, committed) and `*.user.toml` (personal, gitignored).

---

## 5. Cross-Agent Protocol

### Agent Roster
| Agent/Role | Defined In | Capabilities | Communicates With |
|------------|-----------|--------------|-------------------|
| Mary (Analyst) | `bmad-agent-analyst/SKILL.md` | Brainstorm, market/domain/technical research, brief, PRFAQ, document-project | User; invokes sub-skills |
| John (PM) | `bmad-agent-pm/SKILL.md` | PRD C/U/V, epics/stories, readiness, correct-course | User; invokes sub-skills |
| Winston (Architect) | `bmad-agent-architect/SKILL.md` | Architecture, readiness | User; invokes sub-skills |
| **Amelia (Developer — consolidated)** | `bmad-agent-dev/SKILL.md` | Dev story, quick dev, QA test gen, code review, sprint planning/status, create story, retrospective | User; invokes sub-skills |
| Sally (UX Designer) | `bmad-agent-ux-designer/SKILL.md` | UX design (two-spine) | User |
| Paige (Tech Writer) | `bmad-agent-tech-writer/SKILL.md` | Document project, write/validate doc, mermaid, explain | User |
| PRFAQ sub-agents | `bmad-prfaq/agents/` (2) | Artifact analysis, web research | PRFAQ orchestrator |
| Reviewer lenses (ephemeral) | `customize.toml` reviewer rosters (`skill:`/`file:`/text entries) | Rubric walk, adversarial, edge-case, blind-hunter | Parent skill via review files |
| Party personas (ephemeral/configured) | party-mode `customize.toml` (`party_members`, `party_groups`) | Discussion voices; Anti-Consensus Club: Wildcard, Level, Killjoy, Splinter | Orchestrator; user |
| bmad-loop orchestrator (external module) | separate marketplace repo | Polls spec frontmatter, dispatches dev-auto iterations, deferred-work sweeps | bmad-dev-auto via spec files |

**Persona consolidation (v6.3.0):** Barry (quick-flow solo dev), Quinn (QA), and Bob
(Scrum Master) were removed and their capabilities folded into Amelia — three
role-personas collapsed into one Developer agent whose menu spans the whole
implementation phase. Roster went 9 → 6. All six carry `team: software-development`
(v6.4.0) for unified grouping in party-mode and retrospectives. The consolidation
direction is capability-per-menu-item under fewer identities, not more specialists.

### Handoff Mechanisms
1. **Sealed file contracts** (the headline change): the v6.8.0 changelog states it
   directly — "The handoff from design into engineering is now a sealed file contract,
   not a translation layer." SPEC.md frontmatter `companions:` lists what downstream
   MUST read; `sources:` lists fully-absorbed inputs downstream must NOT re-read;
   process metadata is explicitly excluded. Stable IDs (CAP-N, AD-n) survive updates so
   cross-artifact citation holds.
2. **Memlog as the inter-stage medium**: stages contribute append-only entries; the
   artifact re-renders from the log. bmad-architecture can even capture missing answers
   "into a shared spec workspace through the same memlog.py, so bmad-spec can later
   derive SPEC.md without drift."
3. **Compact-summary subagent returns**: reviewer and reconciliation subagents write
   full output to files and return only verdict + top findings + path — "the parent
   never holds full review text." Sequential fallback: write the file first, then flush
   the review from working context.
4. **Extract, don't ingest**: source documents go to extraction subagents; the parent
   assembles from extracts and only loads sources wholesale when subagents are
   unavailable.
5. **Persona carry-through**: unchanged — an active persona persists across sub-skill
   invocations; forge-idea explicitly lets an already-active persona lead the session.
6. **Cross-repo handoff**: bmad-loop ↔ dev-auto communicate solely through story-spec
   files (frontmatter `status`, `## Auto Run Result`, `## Review Triage Log` sections)
   — a file-mediated protocol across separately-installed modules.

### Shared State
- `_bmad/` — four-layer config, custom overrides, shared scripts, installed skills.
- Per-run workspace folders — artifact + `.memlog.md` + review/reconcile files.
- `project-context.md` — standing project context via `persistent_facts` defaults.
- Per-party memory — `{memory_dir}/<party_id>/.memlog.md`, append-only, opt-in
  (the anti-consensus decision room ships `memory = false` by design).
- `sprint-status.yaml` — now also accumulates retrospective `action_items`.
- Still no global STATE.md; state is per-artifact/per-run, discovered by glob +
  frontmatter status (e.g., resume scans for `status` ≠ `final`/`complete`).

### Coordination Patterns
**User-mediated hub with file-contract pipelines and one unattended branch.** The human
remains the orchestrator for phases 0–4; within a run, skills fan out ephemeral
subagents (reviewers, extractors, personas) hub-and-spoke and reabsorb them via compact
summaries. The unattended branch inverts it: bmad-loop is a machine orchestrator polling
a file-based state machine, with adversarial review layers substituting for the human
gate and a HALT protocol substituting for questions. Party-mode's agent-team mode adds a
genuine peer topology (Claude Code Agent Teams) — with the v6.10.0 correction that
teams communicate mailbox-style point-to-point, not broadcast, so the lead must relay
turns; subagent mode remains true broadcast.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | **High** | Memlog working memory (append-only, write-only/blind, JSON ack, read-on-resume-only); derive-don't-edit artifacts; intent-scoped references/ modules replacing forward-chained steps; persistent_facts config field; compact-summary subagent returns; extract-don't-ingest; run-folder workspaces |
| Model Selection | Medium | Model parity mandate for review subagents vs cheaper-model preference for persona subagents — an explicit per-task capability-floor distinction |
| Prompt Craft | **High** | Anti-sycophancy protocol ("praise is noise"); one-question-at-a-time Socratic discipline; "elicitation, not direction — hand the pen back"; front-load-then-shut-up delivery; activation-guardrail hardening against short-circuited boot sequences; named-set generalization pass in edge-case hunter |
| Tool Integration | Medium | uv-run standardization (v7 pre-announcement); stdlib-only Python scripts; 42-platform installer on `.agents/skills/` standard; marketplace-plugin module routing; web-bundle packaging with schema parity |
| Intent Engineering | **High** | Five-field spec kernel + Spec Law; invariant/seed split with the two-builders divergence test; verbatim_intent as sole scope authority in review triage; Ready-for-Development standard (surface-anchored ACs); three-exit taxonomy where "Killed" is a success outcome; coaching-path default |
| Orchestration | **High** | Order-independent pipeline stages via memlog absorption; sealed file contracts with stable IDs; forwarding shims for consolidation migrations; synchronous-subagent mandate for unattended runs; party-mode 4-mode ladder with graceful degradation; mailbox-vs-broadcast topology distinction |
| Evaluation | **High** | Two-pass self-validate (coherence + preservation, with logged "wrapper-only content" drops); review triage with 5 routing categories and admissible-authority rules; parent-owned severity; deterministic lint + rubric walker + lens subagents layered per gate; quality-rubric synthesis replacing adversarial PRD review; measured guardrail ROI (edge-case pass: 50–100% catch-rate gain at 19% token cost) |
| Sandboxing | Low | Unchanged — no isolation mechanisms; read-only diff inspection is prose-enforced |
| Governance | **High** | Four-layer TOML config with structural merge; installer-owned vs human-authored file partition; write-ownership boundaries (single-writer artifacts, read-only inherited ADs); memlog audit at finalize; add-then-retire lifecycle (bmad-investigate, deletion auditor, distillator, automator all retired with cost rationale); stakes-calibrated rigor |
| Agent Design | **High** | Persona consolidation (9→6, three dev-adjacent personas into Amelia); agent-as-skill with customize.toml persona layering; icon-prefix identifiability; anti-consensus persona architecture (four structural dissent roles + scene-level meta-instructions recommending context isolation) |
| Agentic Systems (11.A Loop Engineering) | **High** | bmad-loop/dev-auto: spec-frontmatter state machine polled by an orchestrator; HALT protocol with terminal status + blocking condition; append-only review-triage log with loopback tracking; end-of-run commit for clean next iteration; re-entry on completed spec for follow-up review; `final_revision` linking out-of-tree spec to in-tree commits |

### Findings Candidates

Suggestions only — promotion requires `/promote-findings` or `/research-loop`. All seven
v6.2.2 candidates were previously dispositioned (6 promoted, 1 deduped); candidate 11
below supersedes-in-part one of them.

1. **Memlog: append-only working memory with write-only/blind discipline** (Context
   Engineering 1.C, Agentic Systems) — One shared script (`memlog.py`) as the working-
   memory primitive across a whole skill suite. Three designed invariants: append-only
   chronological (no edit/delete subcommand exists), write-only/blind (every call echoes
   state as one JSON line so the caller never re-reads mid-session; the file is read
   only on resume), and no lifecycle status (completion is an `event` entry, not
   mutable frontmatter — "a resume learns the state by reading the last entries, the
   same way it learns everything else"). Atomic temp+fsync+rename writes. Directly
   relevant to the engine's IB-172 layered-memory design and PROGRESS/HISTORY spine.
   → Promoted to [[append-only-run-log-as-working-memory]] (cross-repo merge with superpowers candidate 6, the durable progress ledger) on 2026-07-13
2. **Derive-don't-edit: artifacts as renders of a decision log** (Context Engineering,
   Orchestration) — SPEC.md, ARCHITECTURE-SPINE.md, and PRD are distilled from the
   memlog at finalize, never hand-patched; each has a single writer; hand-edits are
   overwritten on next derive. Stated payoff: surrounding stages (PRD, UX, architecture,
   epics) can run in any order against the same spec "without merge drift: the log only
   accumulates, the artifact is re-rendered."
   → Promoted to [[derive-dont-edit-artifacts-as-log-renders]] on 2026-07-13
3. **Four-layer TOML config + per-skill customization sidecar** (Governance, Tools) —
   Installer-owned vs human-authored x team vs personal, merged by a stdlib-only script
   with typed structural rules (scalars override, tables deep-merge, code/id-keyed
   arrays merge by key, other arrays append); every skill carries a `customize.toml`
   exposing activation hooks, persistent_facts, reviewer rosters, and on_complete —
   behavior extension without forking skill prose. The prose fallback (skill re-derives
   the merge manually if the script fails) makes the mechanism degradation-tolerant.
   → Promoted to [[four-layer-config-merge-with-customization-sidecar]] on 2026-07-13
4. **Anti-consensus decision room** (Agent Design, Orchestration) — A persona party
   built from four structural dissent roles (Wildcard/option-generator,
   Level/claim-checker, Killjoy/loop-stopper, Splinter/consensus-challenger) whose scene
   instructions forbid voting, declaring consensus, or speaking with authority, and
   recommend subagent mode "because separate context windows make it less likely that
   one shared context will make every voice agree too quickly" — context isolation
   deployed as a debiasing mechanism. Ships `memory = false` so decision rooms start
   fresh.
   → Promoted to [[anti-consensus-decision-room-structural-dissent-roles]] on 2026-07-13
5. **Socratic idea-forge with kill-as-success exit taxonomy** (Intent Engineering,
   Prompt Craft) — Pressure-testing "while changing your mind is still cheap"; three
   valid exits (Hardened/Killed/Clearer) with artifact production optional and explicit
   instruction not to steer toward "shall we build it?"; anti-sycophancy protocol;
   two-voice mechanics (one installed persona + one generated outside voice, varied to
   prevent dominance); memlog vocabulary includes `crack`, `kill`, and `lock` entry
   types. Adjacent to the engine's /solicit-proposals and gate-preparation needs.
   → Promoted to [[socratic-idea-forge-kill-as-success-exit]] on 2026-07-13
6. **Five-field spec kernel with companions and preservation validation** (Intent
   Engineering, Context Engineering) — Any input shape distilled to Problem/Capabilities/
   Constraints/Non-goals/Success-signal; load-bearing test routes overflow to
   content-typed companions (spec-authored vs adopted, with ownership rules); eight-rule
   Spec Law; two-pass self-validate where pass 2 walks the source claim-by-claim and
   logs "wrapper-only content" drops so omissions are on the record, not silent.
   → Promoted to [[five-field-spec-kernel-with-typed-companions]] on 2026-07-13
7. **Architecture spine: invariants vs seed, with a divergence test** (Intent
   Engineering, Governance) — The spine fixes only what keeps independently-built units
   from diverging; admission test: "If two units one level down built this independently,
   could they choose incompatibly?" AND non-obvious AND a real trade-off — else Deferred.
   Everything structural is "seed: true at cold-start, owned by the code once it exists."
   AD-n entries carry Binds/Prevents/Rule; child spines inherit parent ADs as binding
   read-only constraints; conflicts surface rather than override.
   → Promoted to [[architecture-spine-invariants-vs-seed-divergence-test]] on 2026-07-13
8. **Review triage with admissible scope authority and parent-owned severity**
   (Evaluation) — Findings routed to exactly one of intent_gap/bad_spec/patch/defer/
   reject; only the verbatim intent may authorize out-of-scope routing (spec language,
   plan, and diff shape are inadmissible — if only they exclude a finding, that is
   evidence of intent_gap/bad_spec); the parent discards reviewer-assigned severity
   because reviewers operate under "by-design information asymmetry"; severity is judged
   by consequence for the artifact's main consumer after reading surrounding source.
   → Promoted to [[review-triage-admissible-scope-authority]] on 2026-07-13
9. **Add-then-retire abstraction lifecycle at framework scale** (Governance) — Within
   eight minor versions BMAD retired bmad-investigate ("reached the same conclusions as
   plain investigation at higher cost; the case-file artifact didn't justify the
   overhead"), the standalone deletion auditor (folded into edge-case hunter: "cold-start
   cost for near-zero yield"), bmad-distillator (superseded by bmad-spec), and
   bmad-automator (superseded by bmad-loop) — each with a stated cost rationale and a
   migration path (shims, installer cleanup). Upstream corroboration for the engine's
   "abstractions must earn their keep" rule, with a worked deprecation mechanic.
   → Promoted to [[add-then-retire-lifecycle-at-framework-scale]] on 2026-07-13
10. **Spec-frontmatter state machine for unattended dev loops** (Agentic Systems 11.A) —
    dev-auto runs one iteration entirely off `status:` in the story spec's frontmatter
    so any orchestrator can poll it; HALT protocol writes terminal status + blocking
    condition into the artifact itself; append-only review-triage log with loopback
    tracking; end-of-run commit keeps the worktree clean for the next iteration;
    `final_revision` recorded at exit as "the only link back from an out-of-tree spec to
    its in-tree commits"; subagents must be invoked synchronously because "there is no
    event loop to resume a yielded turn."
    → Promoted to [[spec-frontmatter-state-machine-unattended-dev-loop]] on 2026-07-13
11. **Skill flattening: retreat from step-file micro-architecture** (Context
    Engineering, Agent Design) — Partial supersession signal for the existing KB finding
    [[step-file-micro-architecture]]: BMAD cut workflow.md orchestrators 22→1 and step
    files 112→35, rebuilding flagship skills as single outcome-driven SKILL.md files
    with intent-scoped references/ and deterministic side-rails. Step files survive only
    in mechanical execution skills — an empirical boundary for where sequencing
    enforcement pays vs where it fights model judgment.
    → Promoted to [[skill-flattening-outcome-prose-over-step-files]] (carries a contradicts-link to [[step-file-micro-architecture]]; the pre-existing finding is untouched per the new-files-only constraint) on 2026-07-13
12. **Measured guardrail ROI** (Evaluation) — v6.10.0 reports the edge-case hunter's
    named-set generalization pass as "catch-rate improvement of 50% to 100% on a real
    regression, at a 19% token cost per run" — an example of pricing a review layer in
    catch-rate-per-token instead of adopting it on principle. Small but rare: guardrail
    changes shipped with measured cost/benefit.
    → Skipped: weak signal / single quantified anecdote on 2026-07-13

---

## What BMAD now demonstrates that it didn't at v6.2.2

For the restructure-program Phase 4 (agent-vs-skill interview) and Phase 5 consumers:

1. **A critical-thinking layer above the SDLC.** v6.2.2 BMAD was a delivery pipeline;
   v6.10.0 adds reasoning skills whose output is *better judgment, not artifacts*:
   forge-idea (Socratic pressure-testing where killing the idea is a success exit),
   PRFAQ challenge, anti-consensus decision rooms, 71 elicitation methods, 108
   brainstorming techniques with facilitation modes. Artifact production is optional
   throughout. This is the layer the direction note asked about — it exists, it is
   skill-shaped (not agent-shaped), and it composes with personas rather than adding
   them.
2. **Governance by shared primitives, not per-skill discipline.** v6.2.2 governance was
   validator rules over skill files. v6.10.0 adds runtime governance: one shared memlog
   script as the audit trail every flagship workflow writes through, a four-layer
   config resolver with typed merge semantics, write-ownership rules (single-writer
   artifacts, read-only inherited invariants), and a human-review skill
   (checkpoint-preview). Decisions-with-reasons are now infrastructure.
3. **The artifact/memory inversion.** The deepest architectural change: canonical truth
   moved from the rendered artifact to the append-only log; artifacts became derived
   views. This is what makes BMAD's pipeline order-independent and its resumes cheap —
   and it is directly relevant to the engine's PROGRESS/HISTORY spine and IB-172.
4. **Evidence that step-file rigidity loses to outcome prose at the flagship tier.**
   BMAD invented the step-file micro-architecture and has now retreated from it for all
   judgment-heavy skills (112→35 step files), keeping it only for mechanical execution.
   The replacement pattern is: short outcome-driven SKILL.md + intent routing +
   intent-scoped reference modules + deterministic side-rails + reviewer gates.
5. **Persona consolidation over specialist proliferation.** Three personas folded into
   one Developer agent; roster 9→6 while skill count grew 41→47. Capability lives in
   menu-dispatched skills; identity is a thin, customizable layer (`[agent]` TOML block)
   on top. Directly relevant to the single-implicit-agent vision.
6. **A worked unattended-autonomy design.** dev-auto + bmad-loop show what BMAD thinks
   full autonomy requires: file-based state machine, HALT-with-status instead of
   questions, adversarial review layers with severity authority at the orchestrator,
   synchronous subagent mandates, end-of-run commits, and an explicit revision link from
   spec to commits. The human gate is replaced by structured adversarial review plus
   auditable triage logs — not removed.
7. **Deprecation as routine practice.** Four capabilities retired in eight minor
   versions, each with a cost rationale and a migration path. The framework treats
   removal as a feature-grade change, which is what keeps 47 skills from becoming 60.

Contrasts worth carrying into Phase 4/5: BMAD's governance primitives are
runtime/per-project (config layers, memlogs) where the engine's are design-time/
system-scoped (DDs, FOUNDATIONS); BMAD still has no tool-permission model (write-
ownership prose instead); and its critical-thinking skills are user-facing coaching
surfaces, whereas the engine's equivalent pressure (assess-*, adversarial gates) is
producer-facing.

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-04-08 | v6.2.2 | all | Initial analysis. 559 files, 418 MD, 41 skills (30 phase + 11 core), 112 step files, 22 workflows. Everything-as-skill architecture. |
| 2026-07-13 | v6.10.0 | all | Re-run for registry refresh (supersedes v6.2.2 analysis). 590 files, 395 MD, 47 skills, step files 112→35, workflows 22→1 (skill flattening). New: memlog + four-layer TOML governance primitives, spec-kernel product layer (spec/prd/ux/architecture rebuilds), critical-thinking layer (forge-idea, party-mode anti-consensus; investigate added v6.7.0 and retired v6.10.0), persona consolidation 9→6 (Amelia absorbs Barry/Quinn/Bob), dev-auto unattended worker (bmad-loop orchestrator is a separate module repo). 12 finding candidates, incl. partial supersession of [[step-file-micro-architecture]]. |
