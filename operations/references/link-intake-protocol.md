---
name: Link-Intake Triage Protocol
description: >-
  Triage procedure for heterogeneous LINKS.md batches (skills, repos, papers,
  articles) — classify each link, assess roster fit and KB fit, emit one of
  four verdicts (ADD / ENHANCE / KB-ONLY / REJECT) in a single gated report.
  Composes existing skills; builds nothing new. Landed as a reference doc per
  Rule 11 (n=1 recurrence); promotion trigger below.
status: >-
  superseded (promotion trigger fired at run 3, 2026-07-12, session 135;
  Nick-gated option 1 — promoted to the /link-intake skill at
  .claude/skills/link-intake/SKILL.md, which is now canonical; this doc is
  retained as history)
pilot_report: "operations/research-reports/2026-07-11-link-intake-triage.md"
---

> **SUPERSEDED 2026-07-12.** This protocol was promoted to the `/link-intake`
> orchestrator skill (`systems/improvement-loop/.claude/skills/link-intake/SKILL.md`)
> after its third stable-shape run. The skill is canonical and additionally encodes the
> run-3 learnings (recency-weighting, measured-experiment heuristic, fetch-before-probe
> rate-limit lesson, defer/Blocked retry queue). Do not execute this document.

# Link-Intake Triage Protocol

Triage lens for `systems/improvement-loop/LINKS.md` — Nick's rolling link queue. The existing
intake paths answer KB fit (`/source-triage` → `/research-loop`) and framework tracking
(watched-libraries → `/repo-analyzer`); this protocol adds the **roster question** — *should this
become or improve an engine skill?* — and routes everything else into those existing paths.

**Invocation:** manual. Run when Nick supplies a new LINKS.md batch. A run produces exactly one
report and changes nothing else.

## Step 1 — Classify (cheap: URL shape + title + README head, ~1 light fetch per link)

| Class | Signature | Track |
|---|---|---|
| SKILL | literal SKILL.md or skill directory | Roster track |
| REPO-SKILLBEARING | repo whose value is its skills/agents/prompts | Mine → each candidate skill enters the roster track |
| REPO-FRAMEWORK | repo that is a framework/tool/product | Watched-libraries routing |
| REPO-DEMO | reference/demo repo | KB routing or REJECT |
| PAPER / ARTICLE | arXiv, whitepaper, blog | KB track |

Ambiguous cases classify to the cheaper track with a note. Run the tracks as parallel subagents
(the pilot used three: roster / repo / KB).

## Step 2 — Per-track assessment

**Roster track** (SKILL links + skills mined from repos). Full fetch of the SKILL.md, then:
1. **Overlap** — grep the engine roster (`.claude/skills/`), workspace roster (root
   `.claude/skills/`), *and harness-provided capabilities* (built-in and plugin skills count as
   overlap — the pilot's `deslop` REJECT was subsumed by harness `/simplify` + `/code-review`).
2. **Quality/portability skim** — harness assumptions, tool dependencies, model coupling,
   structural soundness. Borrow `/assess-skill`'s lenses; do **not** run the full audit at triage
   time (it runs later, only on Nick-approved ADD candidates, per Rule 10). The pilot confirmed
   the skim is sufficient for a triage verdict.
3. **Value** — against the current prioritization queue in `PROGRESS.md`.

**KB track** (papers/articles). Apply `/source-triage`'s decision tree (pattern density vs KB
dedup): EXTRACT ⇒ KB-ONLY; SKIP ⇒ REJECT; inaccessible ⇒ REJECT with a "defer — [reason]" note
so it can be re-queued. Plus the **roster escalation question**: does the content define a
procedure an engine skill could embody, or a tool an engine skill should adopt? If yes, escalate
to ENHANCE/ADD consideration (the pilot's one ENHANCE — ast-grep outline — came from this
question, not from a SKILL-class link).

**Repo track.** Sub-classify (framework / skill-bearing / demo); check the watched-libraries
registry for existing coverage; **verify provenance** (org renames, corporate origin — the pilot
caught both an org rename and an unmarked Databricks project this way). Framework ⇒ KB-ONLY
routed to watched-libraries intake; demo ⇒ KB-ONLY as research-source, or REJECT.

**Dedup rule (pilot lesson):** subagents dedup against the **live findings corpus** (grep
`research-findings/` frontmatter directly), never against a snapshot index passed in the prompt —
the pilot's handed-off index was silently truncated.

## Verdict rubric — exactly one per link

| Verdict | Criteria | Metadata recorded |
|---|---|---|
| **ADD** | no roster overlap + real capability + relevant | consumption mode (as-is / adapted / reconstructed), source URL, upstream ref (commit/date), authoring model version if discoverable, proposed DD-109 placement |
| **ENHANCE** | overlaps an existing skill AND carries deltas ours lacks | target skill + the specific deltas |
| **KB-ONLY** | not roster material, but pattern-dense or track-worthy | intake path: research-source / watched-library (+`/repo-analyzer`) |
| **REJECT** | none of the above | one-line reason; "defer — [reason]" if inaccessible |

ADD metadata is the skill↔model-coupling provenance from the agentic-OS direction note
(`project-management/design-notes/2026-06-22-agentic-os-direction.md`) — recorded so a future
assets catalog can consume it; no catalog is built here.

## Gates and artifacts

- One report per run: `operations/research-reports/{date}-link-intake-triage.md` — verdict
  summary table, per-link rationales (plain English first), follow-up queue, protocol
  observations.
- The run itself is read-only beyond the report. Every ADD/ENHANCE execution is a separate
  per-link Nick gate; adopted or modified skills go through `/design-skill` / `/assess-skill` in
  fresh context (Rule 10). KB-ONLY items flow into the normal research pipeline with its
  existing gates.
- After Nick accepts the verdicts, processed links are removed from LINKS.md; the report is the
  audit trail.

## Landing status and promotion trigger

Landed as a reference doc, not a skill (Rule 11: one pilot run; the roster rubric — the novel
part — fired weakly on the pilot batch, and most of the protocol reduces to routing into
existing skills). **Promotion trigger:** if a third LINKS.md batch runs this protocol with the
shape stable, promote it — most likely as a thin `/link-intake` orchestrator skill; revisit
whether merging into `/source-triage` is natural at that point (today their inputs differ:
raw URLs pre-intake vs existing research-source files).
