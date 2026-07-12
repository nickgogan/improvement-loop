---
title: >-
  Engine restructure & harness program — master plan
id: "engine-restructure-program"
type: "plan"
category: "architecture-direction"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-07-12"
updated: "2026-07-12"
author: "claude"
gated_by: "nick"
tags:
  - "plan"
  - "agentic-os"
  - "portable-kernel"
  - "second-brain"
  - "session-ops"
  - "careerbuddy"
---

# Engine restructure & harness program

> **Living plan.** This is the master plan Nick requested on 2026-07-12 after the
> CareerBuddy analysis. It sequences the program: session-ops restructure → research
> grounding → substrate audit / second brain → user manual → structured interviewing →
> harness + generalize. Revisit checkpoints are built in (after Phase 1, after Phase 3/4)
> per Nick's stated flow: *"process the videos → look at the plan → maybe the manual →
> look at the plan again → structured interview → harness/generalize."*
> Nick gates all content decisions; this file records mechanics and sequencing.

## 1. Why this program exists

Three converging pressures, all surfaced 2026-07-12:

1. **Session ops are too heavy.** The engine records every session's outcome in four
   overlapping places (PROGRESS prose, a dated handoff file, a System Log entry, git).
   PROGRESS.md has become a session-history archive paid at every cold start. CareerBuddy
   (analyzed this session, clone at scratchpad) converged on a materially cheaper model:
   forward-only PROGRESS + HISTORY changelog + Conventional Commits, handoff = in-place
   reconcile, zero dated handoff files.
2. **The governance/PM substrate has accumulated clutter.** DDs, IB items, design notes
   (several 16–43KB deliberative monsters from April), System Log entries, handoffs,
   thin `knowledge/guides/`, concept docs split across two homes. Nick's verdict: audit
   what's worth keeping and where it lives; the existing guides are suspected too shallow
   to carry the system. A real **second brain for the engine's operations** may be needed.
3. **The portability vision sharpened.** Nick's articulation (this session, extending the
   agentic-OS direction note): **`governance/` becomes the portable kernel** of any
   agentic system — see §2. CareerBuddy demonstrates both the need (three milestone
   generations of portability tooling) and the wrong layout (export set by enumeration
   across `onboarding/` + `.github/` + root docs + `docs/`, guarded by sweeps).

## 2. Target end state (vision capture)

The full agentic-OS direction lives in
`project-management/design-notes/2026-06-22-agentic-os-direction.md`. This program adds
the **governance-as-portable-kernel** model on top:

- **`governance/` is the portable kernel** of any system the engine runs or produces:
  PRD · constitution (vision/mission/values/principles) · the point of the system · how
  it works · component inventory · harness description · **generalized forms** of every
  asset (skills, agents, rules, hooks) as markdown with adaptation commentary · one
  structured **YAML descriptor** indexing it all.
- **Harness materializations are derived, not authored.** `.claude/skills/`,
  `.github/skills/`, Cursor rules, an Omnigent/Agent-Bricks wrapper (extra permissioning,
  sandboxing, orchestration) are compile targets. Generalized↔installed drift detection
  is a first-class citizen (CareerBuddy's manifest-hash `--check` pattern).
- **Kernel-boundary litmus:** *if a downstream consumer would pull it, it's kernel; if
  only this instance needs it, it's state.* PROGRESS/HISTORY, ops byproducts, per-user
  data, and the engine's research KB are state; the kernel is the export unit **by
  construction**, not by sweep.
- **YAML/markdown contract** maps onto the direction note's what+how delivery model:
  YAML = the structured *what* (identity, type, capabilities, harness requirements,
  model coupling, receiver-relative tier semantics); markdown = the *how* (generalized
  content + adaptation commentary). This resolves the direction note's open
  assets-catalog question toward: a manifest, co-located in the kernel.
- **Upstream/downstream flow:** instance use → learnings update generalized governance
  files → push upstream → other instances pull downstream. A package-manager model for
  agentic systems; the engine is the registry steward.

End state: the engine itself is **harnessed** (a formal harness layer, not
agent-remembers-to-invoke-skills) and **generalized** (its own governance/ is a portable
kernel). Order of those two is deliberately open until Phase 4.

## 3. Program phases

### Phase 0 — Session-ops restructure *(greenlit 2026-07-12; execute before research)*

Adopt the CareerBuddy session-ops model. All items are instance-state under the kernel
litmus, so nothing here can be invalidated by later phases.

1. **Create `HISTORY.md`** (engine root): Keep-a-Changelog of shipped
   milestones/sessions, newest-first, with commit ranges. Backfill from the current
   PROGRESS.md Current Focus session paragraphs.
2. **Restructure `PROGRESS.md`** to a forward-only control surface: `Updated:` header
   (≤3-line summary) · Start here · North Star · Roadmap (one line per milestone) ·
   Current milestone (definition-of-done, scopes on a Shape-Up hill, single next unit of
   work) · Backlog/Icebox (absorbs Logged-for-future + prioritization queue) · Blockers
   (absorbs the "Open for Nick" gate list). Route-then-compact test governs every line.
3. **Rewrite `/session-handoff`** as reconcile-in-place (no dated files) — first
   CareerBuddy import: adapt `ops-session-handoff` (exportable; ships `ports/generic.md`
   + capability contract). Keeps its Process-Rule-2 ownership of PROGRESS.md. Rule-10
   assess pass after adaptation.
4. **Archive the dated handoffs** (`operations/handoffs/` → `archive/`); add the
   **wake-up idiom** to engine CLAUDE.md ("PROGRESS"/"continue" = read PROGRESS.md,
   proceed with next unit of work, no recital).
5. **Adopt Conventional Commits** with `Refs: <scope-slug>` footers; add a PROGRESS
   line-budget pre-commit check (C12 analog) beside the existing frontmatter/foundations
   checks.
6. **System Log narrowed role — Nick gate (DD-59 touchpoint):** recommended option (a):
   SL stops carrying session tracking (git + HISTORY carry it) and keeps only
   architectural/operational learnings that fit no DD. No DD supersession needed, scope
   note only.

**DoD:** a fresh session cold-starts from PROGRESS.md alone; no dated handoff is
authored; commit conventions + line-budget check live; Nick has ruled on SL.

### Phase 1 — Research grounding *(the very next thing after Phase 0)*

1. **Nick's YouTube links** on second brains / system setup / harness design: intake via
   `LINKS.md` (existing link-intake protocol) or in-chat → `/transcript-fetcher` →
   extraction into the KB (`/research-loop` Pass 2). These ground the second-brain and
   harness models before anything is built.
2. **CareerBuddy as a primary source:** intake the wiring canon (`onboarding/` docs
   01–08, wiring-manifest/system-contract patterns), `meta-skill-author` references
   (superset-spec, decision-sequence, audit-rubric, platform-matrix, skill-smells),
   the `ops-self-improve` store schema + promotion rules, the C1–C16 deterministic audit
   battery — plus the **5 corpus contributions CareerBuddy already queued for this
   engine** (`ops/self/improve-backlog.md`: invariant column as contract field,
   receiver-relative tier semantics, card-over-manifest fusion, Pi load-time trust-gate
   trio, prose-guard→policy-engine degradation).
3. **Named research dependencies** carried from the direction note: BMAD high-level
   skills, superpowers, Archon workflow shape, Nate B Jones' open skills framework,
   the #8 taxonomy/clustering repo (**name still pending from Nick**).

**DoD:** findings in the KB; delta report. → **Plan checkpoint #1: revisit this plan.**

### Phase 2 — Substrate audit & second-brain design *(scope: ops + knowledge layer)*

Audit everything that governs/remembers how the engine operates; the research KB
(findings/extracts/schematics) is audited **for placement only**, not content.

- **Per-class verdicts** (keep / distill / archive / re-home), classified against the
  kernel-vs-state litmus: DDs (Binding spine vs procedural), IB items, design notes
  (April monsters are prime distill-and-archive candidates), System Log (per Phase 0
  ruling), `knowledge/guides/` (shallow — merge, rebuild, or fold into kernel docs),
  concept-doc homes (DD-112 rule vs the kernel model).
- **Second-brain-for-operations design**, grounded in Phase 1 research; pattern-lift
  the `ops-self-improve` store model (append-only lessons keyed by owning surface,
  recurrence thresholds, shadow-sandbox validation, human-gated promotion, deterministic
  store check) — sized per Rule 11 against what the audit actually shows we drop today.
- Deterministic audit battery for whatever shape lands (ops-doc-sync pattern-lift).

**Nick gates:** every DD supersession, archive move, and the second-brain mechanism
itself (Rule 11 evidence required).

### Phase 3 — User manual *(Nick gates whether/when; contract partially set)*

Locked from session 133 pre-pivot: audience = **Nick-the-builder**, altitude = **both,
direction-bounded**. Home + length undecided. New input from this program: under the
kernel model, much of the manual's content ("the point of the system," "how it works,"
components) **is kernel content** — the manual may become the kernel's human-readable
layer rather than a standalone doc (CareerBuddy's `docs/` manual + its sync-audit tax is
the cautionary tale). → **Plan checkpoint #2 follows.**

### Phase 4 — Structured interviewing → what we actually need and why

Adapt `ops-vision-to-plan` (second CareerBuddy import: exportable, Socratic elicitation,
per-section human gates, binary acceptance criteria) to interview Nick and produce the
engine's own kernel documents: **PRD, constitution, actors** — resolving the direction
note's open questions (garbled "Division, to a degree" fragment; governance/permissions
as layers vs cross-cutting). **Decide here: generalize-first vs harness-first.** Update
this plan accordingly.

### Phase 5 — Harness + generalize *(order per Phase 4)*

- **Harness the engine:** formal harness layer per the Phase 1 research + Phase 4 PRD —
  Claude Code is the first target runtime.
- **Generalize:** engine `governance/` becomes its own portable kernel (YAML descriptor +
  generalized asset forms + adaptation commentary incl. orchestration-layer targets like
  Omnigent).
- **Remaining imports land where needed:** `meta-skill-author` (import + adapt; the
  authoring/eval/port toolchain), `meta-harness-author` (pattern-lift — internal,
  topology-bound; its generalize→adapt→install→verify arc is the kernel compiler),
  drift-check tooling (manifest hash `--check`).

## 4. CareerBuddy skill dispositions *(per-skill verdict, locked 2026-07-12)*

| Skill | Verdict | Lands in | Why |
|---|---|---|---|
| `ops-session-handoff` | **Import + adapt** | Phase 0 | Exportable; ships ports + contract; direct replacement for dated-handoff model |
| `ops-vision-to-plan` | **Import + adapt** | Phase 4 | Exportable; the structured-interviewing engine for PRD/constitution |
| `meta-skill-author` | **Import + adapt** | Phase 5 | Exportable; authoring/eval/improve/port toolchain; richest package |
| `ops-self-improve` | **Pattern-lift** | Phase 2 | Internal, topology-bound; its store/promotion model is the second-brain prototype |
| `ops-doc-sync` | **Pattern-lift** | Phases 2/5 | Internal; C1–C16 deterministic-audit pattern generalizes, checks don't |
| `meta-harness-author` | **Pattern-lift** | Phase 5 | Internal; generalize→adapt→install→verify arc = the kernel compiler model |

Every import/adaptation gets a Rule-10 assess pass (`/assess-skill`) after landing.

## 5. Decisions locked (2026-07-12)

- Audit scope: **ops + knowledge layer** (KB audited for placement only).
- Import mode: **per-skill import vs pattern-lift** (table above).
- Ops restructure timing: **Phase 0, before research**.
- Plan home: **`operations/plans/`** (instance-state; PROGRESS roadmap points here).
- Manual contract (from session-133 pre-pivot): Nick-builder audience; both altitudes,
  direction-bounded.

## 6. Open questions (carried, not blocking Phase 0)

1. Generalize-first vs harness-first (→ Phase 4).
2. #8 taxonomy/clustering repo name (Nick input, → Phase 1).
3. The garbled "Division, to a degree" direction-note fragment (→ Phase 4 interview).
4. Manual home + length; manual-as-kernel-layer question (→ Phase 3).
5. System Log narrowed role (→ Phase 0, Nick gate).
6. Pre-existing carried gates: verbatim null→P3 reassessment; re-injection correction
   disposition; push of unpushed local commits; mirror question (subtree push vs
   retire); design-notes category ruling (now subsumed by the Phase 2 audit).

## 7. Plan maintenance

This file is the program's single plan of record. Update it at the two checkpoints
(post-Phase-1, post-Phase-3/4) and whenever a phase ships; PROGRESS.md carries only the
roadmap line + next unit of work. When Phase 2 re-homes plan/note categories, this file
moves with the ruling.
