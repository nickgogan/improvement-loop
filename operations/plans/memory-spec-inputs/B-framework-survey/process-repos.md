---
title: "B — Process-Repo Framework Survey: Memory Mechanics in Superpowers, BMAD, GSD"
type: "resource"
target_system:
  - "improvement-loop"
category: "plan-input"
stage: "draft"
created: "2026-07-16"
author: "claude"
tags:
  - "memory"
  - "E1"
  - "spec-input"
  - "cross-framework-survey"
---

# B — Process-Repo Framework Survey: Memory Mechanics in Superpowers, BMAD, GSD

**Scope.** Design input for the E1 memory-architecture spec, sibling to A1 (KB design
brief), A2 (substrate inventory), A3 (per-actor requirements). Where A1 cited
`append-only-run-log-as-working-memory` as a P1 finding from a two-repo convergence
(BMAD memlog + Superpowers progress ledger), this document tests that claim in depth
across all three watched process/harness repos — Superpowers, BMAD-METHOD, GSD — and
adds the external-sentiment layer A1 did not need. **Verdict, stated up front and argued
below: the convergence claim survives, but narrower than "consensus" implies** — it holds
for exactly one memory type (working memory, session/run-scoped) and one governing
repo pair (BMAD, Superpowers); GSD's richest surface is the opposite pattern (mutable,
structured, self-healing), and GSD itself is no longer a stable comparison point as an
active project (see §GSD governance context).

Internal grounding: `watched-libraries/{superpowers,bmad-method,gsd}.md` +
`analysis/{superpowers,bmad-method,gsd}-analysis.md`; KB findings
`append-only-run-log-as-working-memory.md`, `derive-dont-edit-artifacts-as-log-renders.md`,
`phase-queue-state-file-as-orchestrator-memory.md`, `workflow-state-vs-conversation-state.md`,
`ledger-based-orchestration-stall-detection.md`, `production-memory-architecture-spectrum.md`,
`gsd-global-learnings-store-cross-session-persistence.md`,
`gsd-queryable-codebase-intelligence-store.md`, `gsd-stall-detection-revision-loop-escalation.md`.
External: WebSearch/WebFetch against GitHub (releases, changelog, discussions), Reddit,
Hacker News (2026-07-16 date-verified via HN API where cited).

---

## Superpowers

### Memory surfaces

| Surface | File shape | Writer | Cadence |
|---|---|---|---|
| Progress ledger | `.superpowers/sdd/progress.md` — flat append-only text, one line per completed task (task ref + commit range + review status) | Controller, via `sdd-workspace`/task-completion step in `subagent-driven-development/SKILL.md` | Event-driven — one append per task cleared through both review verdicts |
| Task brief | `.superpowers/sdd/task-N-brief.md` | `task-brief` script, extracting from the plan | Once per task, at dispatch |
| Implementer report | `.superpowers/sdd/task-N-report.md` | Implementer subagent | Once per task, on completion (DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT) |
| Review package (diff) | `.superpowers/sdd/review-<base7>..<head7>.diff` | `review-package` script | Once per review dispatch (per-task, plus one whole-branch at the end) |
| Git commits | standard git history | Implementer subagents | Per task |

All of the above live in one self-ignoring, per-worktree scratch directory
(`.superpowers/sdd/`) created at runtime — not committed, not tracked, explicitly
outside `.git/` because Claude Code write-protects that path. There is **no surface
that survives worktree deletion** except the progress ledger's echo in git log and
commit messages themselves.

### Memory model by type

- **Working memory:** the progress ledger, scoped to one SDD run in one worktree. This
  is the surface Superpowers actually engineered — everything else (brief, report,
  diff) is scratch that a review cycle consumes and discards.
- **Episodic memory:** **not handled as a distinct surface.** There is no cross-run
  record of "what SDD runs happened on this project" — each run's ledger starts fresh
  in its own worktree-scoped `.superpowers/sdd/`. Git log is the closest thing to
  episodic memory, and it is external to the framework (Superpowers reads it, doesn't
  own it).
- **Semantic memory: explicitly absent.** No lessons-learned store, no accumulated
  calibration, no cross-project learning surface exists anywhere in the repo. Confirmed
  unchanged from v5.0.7 through v6.1.1 — the six major v6.0.0 capability additions
  (unified reviewer, file-mediated handoffs, plan contracts, controller de-authorization,
  whole-branch review, vendor-neutral vocabulary) touch orchestration and governance,
  not memory scope. `production-memory-architecture-spectrum.md` places Superpowers at
  level 1 of 5 ("no memory — context window only") for this reason, though the v6 ledger
  is a partial revision of that: level 1 undersells the progress ledger's actual
  durability within a run.
- **Procedural memory: static, not learned.** The 14 SKILL.md files are the procedural
  layer, authored by humans (with an external eval-gated review process for changes) —
  not adapted from the agent's own run history. No skill rewrites itself based on
  ledger contents.

**What's not handled, stated plainly:** anything that needs to survive past one SDD
run — no lessons store, no project-level learnings, no cross-session semantic memory.
Superpowers' whole memory investment is in making one run survive its own compaction,
nothing more.

### Lifecycle trace of one entry

1. Controller dispatches Task 3's implementer via `task-brief`, which writes
   `task-3-brief.md` from the plan's Task 3 section.
2. Implementer subagent reads the brief, writes code + tests, commits, writes
   `task-3-report.md` (status: DONE, TDD red/green evidence), returns <15 lines to the
   controller (path to the report, nothing more).
3. Controller runs `review-package` to produce the task's diff file, dispatches the
   task reviewer (read-only, explicit model) against it.
4. Reviewer returns dual verdicts (spec ✅, quality ✅) in a structured report.
5. Controller appends one line to `progress.md`: task 3, commit range, review-clean.
   This is the only durable write in the whole cycle that is *designed* to persist
   past the current context window.
6. If the session compacts or crashes before Task 4 starts, a fresh controller session
   (or the same one post-compaction) reads `using-superpowers`, re-enters
   `subagent-driven-development`, and its first act is `cat progress.md` — Task 3 shows
   complete, so dispatch resumes at Task 4. The ledger and `git log` are explicitly
   trusted over the agent's own conversational recollection.
7. If a `git clean -fdx` runs between steps 5 and 6, `progress.md` is deleted (it is
   git-ignored scratch); recovery falls back to `git log` alone — documented as a known
   gap, not a designed recovery path.

### Practitioner sentiment

- **2026 (undated within year), r/ClaudeCode, u/MindCrusader:** "workflow good,
  packaging heavy" — a top-voted assessment that the SDD workflow (ledger included) is
  effective but the plugin is token-intensive to load. Not ledger-specific, but the
  closest concrete community verdict found. (Source: WebSearch aggregation, 2026-07-16
  query; exact comment date not resolvable via search snippet.)
- **Upstream-documented failure motivating the ledger (dated to the v6.0.0 design docs,
  ~2026-06):** "the single most expensive failure observed" — controllers re-dispatching
  entire completed task sequences after losing context to compaction. This is the
  project's own stated justification, not third-party sentiment, but it is the most
  concrete "did this work" evidence available: the ledger exists *because* an earlier,
  ledger-less version of SDD failed expensively in real use.
  (`superpowers-analysis.md`, confirmed against the v6.1.1 clone, 2026-07-13.)
  Superpowers' RELEASE-NOTES and the skill's own prose document a git-ignore caveat: a
  `git clean -fdx` deletes the ledger, with `git log` as the documented fallback — this
  is the project disclosing its own failure mode, not user-reported breakage.
- No practitioner reports of ledger *bloat* or *drift* were found — plausible given the
  ledger's small size (one line per task, one SDD run at a time, deleted with the
  worktree) rather than evidence the failure mode doesn't exist.

---

## BMAD-METHOD

### Memory surfaces

| Surface | File shape | Writer | Cadence |
|---|---|---|---|
| Memlog | `{run-folder}/.memlog.md` — append-only, one JSON-echoed line per call, no edit/delete subcommand | `_bmad/scripts/memlog.py`, invoked by skill prose (`uv run`) from any flagship skill in the run | Per decision/assumption/override/terminal event, as it happens during the run |
| Derived artifacts | `SPEC.md`, `ARCHITECTURE-SPINE.md`, PRD, etc. — polished markdown, single writer per artifact | The one skill that owns that artifact (e.g. `bmad-spec` owns SPEC.md) | At finalize / on explicit re-derive, never hand-patched |
| `project-context.md` | Flat markdown, shared project facts | Human-authored, loaded via `persistent_facts` config | Set once, read every run |
| Party-mode memory | `{memory_dir}/<party_id>/.memlog.md` | Party-mode orchestrator | Opt-in; anti-consensus room explicitly ships `memory = false` |
| Config layers | `_bmad/config.toml` (4-layer TOML: installer/human × team/personal) | `resolve_config.py` merge; human edits to `_bmad/custom/*.toml` and `*.user.toml` | Read every skill activation; written by installer or human, never by an agent mid-run |

The memlog is the one designed working-memory primitive; everything else is either a
derived view of it (artifacts) or configuration, not accumulated memory.

### Memory model by type

- **Working memory:** the memlog, with three designed invariants — append-only
  (no edit/delete subcommand exists, the discipline is enforced by tool shape),
  write-only/blind during the session (every call echoes state back as one JSON line
  so the writer never re-reads its own history mid-run — the file is read only on
  resume), and no lifecycle status field (completion is an `event` entry, not mutable
  frontmatter). Writes are atomic (temp+fsync+rename).
- **Episodic memory:** run-folder scoped, and this is where BMAD extends past
  Superpowers — a run-folder is a durable, resumable unit (same-slug reinvocation
  resumes in place by reading the memlog tail), and multiple pipeline stages (PRD, UX,
  architecture, epics) can each append to the *same* memlog "in any order… without
  merge drift: the log only accumulates, the artifact is re-rendered"
  (`derive-dont-edit-artifacts-as-log-renders.md`). This is a genuine episodic layer
  Superpowers doesn't have: one run's memory is addressable and reusable across several
  different skills, not just one controller's task loop.
- **Semantic memory: present but narrow, and explicitly NOT a cross-project store.**
  `project-context.md` via `persistent_facts` is standing, cross-skill shared context —
  but it is human-authored once, not accumulated from agent experience. There is no
  BMAD equivalent of GSD's Global Learnings Store or the engine's own lesson store: no
  mechanism promotes memlog entries from one run into durable knowledge usable by a
  *different* run. Each run's memlog is local to its run-folder; nothing distills it
  upward automatically.
- **Procedural memory:** `customize.toml`'s `activation_steps_prepend/append` is
  configuration-level behavior extension (per-skill, per-installation), not learned
  procedure — a human or installer edits it; no agent writes to it based on its own
  run history.

**What's not handled, stated plainly:** cross-run/cross-project semantic accumulation.
BMAD's memory investment, like Superpowers', is bounded to one run — BMAD's run just
happens to be a whole SDLC pipeline stage (potentially days), not one SDD task loop.
Nothing in the repo carries a lesson from one memlog into the next project's memlog.

### Lifecycle trace of one entry

1. During a `bmad-architecture` session, the user answers a question that resolves an
   architectural trade-off not yet captured in the spec.
2. The skill calls `memlog.py append` with an `event`-typed entry (decision content +
   metadata). The script performs an atomic write (temp file, fsync, rename) and echoes
   the resulting state back to the caller as one JSON line — the skill does not re-read
   the memlog file to confirm; it trusts the echo.
3. The session continues, appending more entries as the architecture conversation
   proceeds — none of these are re-read mid-session; the memlog is a blind write
   target during the run.
4. At finalize, `bmad-spec`'s derive step (a *different* skill than the one that wrote
   most of the entries) reads the full `.memlog.md` for the run-folder and renders
   `SPEC.md` from it — SPEC.md is DERIVED, never hand-edited; any manual edit to SPEC.md
   itself is overwritten on the next derive.
5. If the session is interrupted before finalize, a later invocation of any skill
   against the same run-folder (same-slug reinvocation) reads the memlog tail to learn
   what has already been decided, resuming without re-asking already-answered
   questions.
6. The finalize sequence's last act is a "memlog audit" — walking the accumulated log
   with the user before it is considered authoritative — the one point where a human
   reads the raw log rather than a derived artifact.

### Practitioner sentiment

- **2025-09-07, Hacker News (item 45156172):** "Pretty surprised BMAD-method wasn't
  mentioned. For my money it's by far the best Claude Code compliment [sic]" — positive,
  but **predates memlog by roughly nine months** (memlog shipped v6.9.0, per the
  CHANGELOG dated into the 2026-06/07 window). This praise is evidence for BMAD's
  general context-engineering reputation (docs-as-code, context sharding), not for the
  memlog mechanism specifically — cited here only to flag the recency mismatch, not as
  memlog endorsement.
- **No dated 2026 practitioner commentary specific to memlog reliability, drift, or
  bloat was found** despite three targeted searches (WebSearch queries on memlog state
  drift, decision-log complaints, and BMAD v6 review threads). The available secondary
  coverage (Ry Walker's BMAD research writeup, DeepWiki's auto-generated reference docs,
  a Swan Software case-study blog post) restates the project's own design claims
  ("returning to a project does not require re-explaining the plan when documents
  remain the source of truth") rather than reporting independent verification. This is
  a **gap, not a null result** — treat memlog's real-world reliability as
  under-evidenced externally, resting mainly on the project's own case studies and
  measured guardrail-ROI claims already captured in `bmad-method-analysis.md`
  (e.g., the 50–100%-catch-rate/19%-token-cost edge-case figure).

---

## GSD (Get Shit Done)

### Memory surfaces

| Surface | File shape | Writer | Cadence |
|---|---|---|---|
| `STATE.md` | Single mutable file, YAML frontmatter + markdown body, in `.planning/` | `gsd-tools.cjs` helpers (`buildStateFrontmatter`, `parseStateMd`), invoked by workflow/agent steps | Read at the start of every workflow; written after phase/task transitions — mutated in place, not appended |
| Global Learnings Store | Structured CRUD store *outside* `.planning/` (survives project cleanup) | Any phase, on completion (auto-copy) | Auto-injected into planner context at phase start; written at phase completion |
| Codebase Intelligence Store | `.planning/intel/` — structured JSON (files, exports, symbols, patterns, dependencies) | `gsd-intel-updater` agent, incremental updates | On-demand / incremental, opt-in |
| `ROADMAP.md` | Phase registry, markdown | `gsd-roadmapper`, updated per phase completion | Per phase |
| Phase artifacts | `CONTEXT.md`, `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md` per phase | Respective phase agent | Once per phase, per artifact |
| `config.json` | User preferences (model profiles, toggles) | Human, via `gsd-tools.cjs config-get/set` | Ad hoc |

### Memory model by type

- **Working/episodic memory:** `STATE.md` is GSD's central surface, and it is
  **structurally the opposite of the BMAD/Superpowers pattern**: it is a single mutable
  document with a small set of frontmatter fields (`active_phase`, `next_action`,
  `next_phases`, `progress`), reconciled and rewritten in place rather than appended to.
  It plays both working-memory and episodic-memory roles at once — it is read at every
  workflow start (working) and is the artifact that survives across sessions within one
  project (episodic).
- **Semantic memory: present and the richest of the three repos.** The Global Learnings
  Store is a genuine cross-session, cross-phase semantic layer — structured CRUD (not
  append-only), stored outside `.planning/` specifically so it survives project resets,
  auto-injected into planner context without human action. This is categorically beyond
  what either Superpowers or BMAD ships: neither has an automatic promotion path from
  one run's working memory into a durable, auto-recalled semantic store.
- **A second semantic-adjacent surface** — the Codebase Intelligence Store
  (`.planning/intel/`) — is structured *world-model* knowledge (symbols, exports,
  dependencies) rather than *decision* knowledge, closer to a cache than a memory in
  the episodic/semantic sense, but explicitly designed to avoid re-deriving the same
  facts every session.
- **Procedural memory:** static, same as the other two — 24 agent definitions and 70
  commands are authored, not learned. GSD's stall-detection mechanism
  (`gsd-stall-detection-revision-loop-escalation.md`) is the closest thing to adaptive
  behavior, but it operates on issue-count trajectory within one revision loop, not on
  memory of past runs.

**What's not handled, stated plainly:** GSD does not have an append-only decision
ledger comparable to memlog or the SDD progress ledger — `STATE.md` is reconciled, not
accumulated, and the framework provides explicit tooling (`gsd state validate`,
`gsd state sync --verify`) because that reconciliation is known to drift from
filesystem reality. GSD substitutes *self-healing mutable state* plus a *separate
structured semantic store* for the *single append-only log* the other two repos
converge on.

### Lifecycle trace of one entry

1. `/gsd:execute-phase` reads `STATE.md` at start: `active_phase`, `progress`,
   `next_action`.
2. Wave-based executor agents run tasks, each with an atomic commit; on completion,
   `SUMMARY.md` is written to `.planning/phases/{phase}/` and `STATE.md`'s frontmatter
   is rewritten in place (`buildStateFrontmatter`) to reflect the new progress counters
   and next action — this is a mutation, not an append.
3. Verifier reads `STATE.md` + `SUMMARY.md`, explicitly told not to trust the summary's
   claims, and checks the actual codebase (goal-backward verification).
4. On phase completion, learnings distilled during the phase are auto-copied to the
   Global Learnings Store (outside `.planning/`) and become available to the *next*
   phase's planner without a human re-supplying them.
5. `/gsd:next` reads `STATE.md` to route to the next logical step — this is the routing
   mechanism BMAD's spec-frontmatter state machine and Superpowers' progress ledger both
   also serve, but here the single artifact is both the router and the mutable memory.
6. If `STATE.md` drifts from what's actually on disk (crash mid-write, manual edit, a
   multi-runtime install exposing stale skills), `gsd state validate` detects the drift
   and `gsd state sync --verify` rebuilds `STATE.md` from the actual project state on
   disk — recovery is "recompute state from ground truth," not "replay an append-only
   log." This is the opposite recovery philosophy from Superpowers/BMAD, which recover
   by trusting the log over recollection; GSD recovers by trusting the filesystem over
   the state file.

### Practitioner sentiment

- **GSD's state-drift problem is project-acknowledged, not just externally observed:**
  the project ships `gsd state validate` / `gsd state sync` specifically because
  `STATE.md` fields can desynchronize from filesystem reality (documented in
  `docs/COMMANDS.md` and DeepWiki's troubleshooting reference, both current as of the
  2026-07-16 search). A known multi-runtime failure mode is explicitly documented: "a
  developer can update GSD in one runtime and still have stale or drifted GSD skills in
  the others," with no supported way to reconcile one canonical install across
  runtime-local skill roots.
- **2026-04 to 2026-05, GSD CHANGELOG (v1.28.0–v1.42.1):** multiple dated entries
  address `STATE.md` reliability directly — "STATE.md frontmatter status preserved when
  body Status field missing" (v1.28.0), "`state sync` command reconstructs STATE.md
  from actual project state… with `--verify` dry-run flag" (v1.32.0), "`parseStateMd()`
  now reads four new STATE.md frontmatter fields" (v1.41.0), "`buildStateFrontmatter`
  now counts nested plans… so repos using nested layout no longer get progress counters
  silently overwritten" (v1.42.1). Read together, this is a project iterating
  repeatedly on state-file correctness bugs over roughly two months — evidence the
  mutable-STATE.md design carries a real, recurring maintenance cost that the
  append-only alternative (by construction — no edit/delete subcommand) does not incur.
- **2026-04-01 to 2026-05-22, governance collapse (materially relevant context, not
  memory-mechanics sentiment per se):** original maintainer TÂCHES became unreachable
  around 2026-04-01, social accounts deleted, and a Solana token ($GSD) associated with
  the project was publicly linked to a rug-pull (~2026-05-21/22). The upstream repo
  `gsd-build/get-shit-done` is now **archived** (confirmed via `gh api`, `archived: true`,
  last push 2026-05-31). Community maintainer trek-e forked a continuation,
  `open-gsd/get-shit-done-redux` ("GSD-Core"), on 2026-05-22, mirroring all 394 branches
  and 229 tags bit-for-bit and stripping token/social references; it remains actively
  pushed as of 2026-07-16 (confirmed via `gh api`, `pushed_at: 2026-07-16`). The fork
  announcement makes **no changes to STATE.md or memory architecture** — it is a
  governance/branding fork, not a technical one, as of this survey. **This means GSD's
  memory design is currently frozen under new, less-established stewardship** — a
  materially different risk profile than Superpowers (Anthropic-marketplace-listed,
  eval-gated skill changes) or BMAD (continuously active, ~monthly releases through
  v6.10.0). Any spec decision citing GSD's STATE.md/Global-Learnings-Store design as a
  stable reference point should flag this provenance risk.

---

## Convergence Analysis

### Where the three genuinely converge (mechanism-level)

1. **A durable memory-bearing surface external to the conversation is universally
   necessary.** All three repos independently concluded that conversation memory
   (chat history) cannot be trusted to survive compaction, crashes, or session
   boundaries, and all three externalize a recovery-critical artifact to the
   filesystem: Superpowers' `progress.md`, BMAD's `.memlog.md`, GSD's `STATE.md`. This
   is the level at which "consensus" genuinely holds — not on file shape, but on the
   *necessity* of an out-of-context durable surface as the resume mechanism.
2. **Artifacts-as-derived-views is a second, narrower convergence.** BMAD's
   derive-don't-edit discipline (SPEC.md rendered from memlog, never hand-patched) and
   Superpowers' report/diff files (scratch, regenerated by scripts, not hand-maintained)
   both treat the *polished* artifact as downstream of the *log*-shaped source of
   truth. GSD is the exception here too: `STATE.md` is both the log-equivalent and the
   polished artifact in one file — there is no separate rendering step.
3. **"Trust the durable surface over your own recollection" is a shared operating
   rule**, stated near-verbatim in both Superpowers ("trust the ledger and git log over
   recollection") and BMAD's resume-by-reading-the-tail discipline — this is a
   convergent design *instruction to the agent*, not just a convergent artifact shape.

### Where they diverge

1. **Append-only vs mutable is a real fork, not a detail.** BMAD's memlog is append-only
   by construction (no edit/delete subcommand exists at the tool level — the strongest
   form of the invariant). Superpowers' progress ledger is append-only by convention
   (a controller *could* edit the file; nothing stops it, but the pattern is "append a
   line per task"). GSD's `STATE.md` is mutable by design, rewritten in place on every
   phase transition, and — as the changelog evidence shows — pays a recurring
   correctness-bug cost for that choice that the other two do not incur *in the same
   surface* (GSD's cost shows up as parsing/frontmatter bugs across ~15 dated changelog
   entries in two months; the append-only repos' cost shows up elsewhere — ledger bloat
   risk, blind-write drift — but not as this class of bug).
2. **Semantic memory is present in exactly one of the three, and it's the odd one out
   on append-only.** GSD's Global Learnings Store is the only automatic, cross-run,
   cross-project semantic layer among the three repos — and it is explicitly structured
   CRUD, not an append-only log. Superpowers has no semantic layer at all. BMAD's
   closest analogue (`project-context.md`) is human-authored standing context, not an
   accumulated one. If the spec wants an automatic promotion path from working memory
   into durable knowledge, none of the three converge on how to build it — GSD is the
   only one that built it, and it built it as the opposite pattern.
3. **Recovery philosophy diverges along the same fault line.** Superpowers/BMAD recover
   by trusting the log (plus git, in Superpowers' case) over the filesystem; GSD
   recovers by trusting the filesystem over its own state file (`state sync` rebuilds
   `STATE.md` from ground truth). These are not compatible recovery strategies — a spec
   that wants one canonical answer must pick a side, not average them.
4. **Run/scope granularity differs.** Superpowers' ledger is scoped to one SDD
   execution loop inside one worktree. BMAD's memlog is scoped to one run-folder, which
   can span several pipeline stages and skills over potentially days. GSD's `STATE.md`
   is scoped to the whole project across its full roadmap. None of the three treat "one
   memory surface, one scope size" the same way — the append-only convergence (point 1
   below) held despite this scope mismatch, which is itself informative: the *mechanism*
   converges independent of *scope*.

### Does "the append-only run log is de facto consensus" survive?

**Partially, and the qualification matters more than the headline.** The original
finding's evidence (BMAD memlog + Superpowers progress ledger) is accurately
characterized — those two really did converge independently on append-only,
resume-by-tail, trust-the-log-over-recollection working memory, from opposite
motivations (decision auditability vs. compaction recovery), and both are current,
actively maintained designs as of the versions analyzed (BMAD v6.10.0, 2026-07-03;
Superpowers v6.1.1, 2026-07-02). That part of the claim is solid.

What doesn't survive unqualified is the word "consensus" applied across the *category*
of process-harness repos rather than across the two repos that actually converged:

- **It is 2-of-3, not 3-of-3**, and the third (GSD) isn't a near-miss — it's a
  considered opposite (mutable, structured, filesystem-is-truth), shipped with its own
  self-healing tooling because its authors evidently found the mutable approach's
  drift cost acceptable against append-only's other costs (ledger bloat, blind-write
  drift — both named as failure modes in the KB finding itself).
- **The claim is scoped to working memory only.** Extend the lens to semantic memory
  and the picture inverts: GSD is the only repo with an automatic cross-run learnings
  store, and it rejected append-only for that surface too. There is no cross-repo
  convergence on *any* mechanism for promoting working memory into durable semantic
  memory — that remains an open design question the process-repo survey does not
  answer (consistent with A1's Gap G4 on supersession mechanisms).
- **External validation is asymmetric and thin.** Superpowers' ledger has the strongest
  practitioner-adjacent evidence — but it's the project's *own* stated incident
  ("the single most expensive failure observed"), not independent third-party
  confirmation that the fix works at scale. BMAD's memlog has essentially no dated,
  independent 2026 commentary at all — the HN praise available predates the mechanism
  by nine months and is about BMAD generally. GSD's mutable-state approach has the most
  concrete dated evidence of any of the three, but it's evidence of an ongoing
  correctness cost (repeated changelog fixes), not of the design succeeding.
- **GSD's governance collapse (April–May 2026) weakens it as a comparison point going
  forward**, independent of the memory-mechanics argument — a spec built partly on "GSD
  chose differently" should note that GSD's current form is a bit-for-bit community
  fork under new, unproven stewardship, not the actively-iterated project the original
  analysis (dated 2026-04-07, pre-collapse) characterized.

**Recommendation for the E1 spec:** treat "append-only run log as first accumulation
surface" (A1's Unknown-2 verdict) as well-supported for exactly the working-memory
layer it was evidenced on — this survey does not overturn that. But do not extend the
same append-only default to a future semantic/learnings layer without new evidence;
GSD is the only concrete precedent there, and it points the other way (structured CRUD,
not append-only log).
