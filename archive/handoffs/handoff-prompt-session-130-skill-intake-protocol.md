# Session 130 — Design a Lightweight Skill-Intake Protocol for LINKS.md

## IDENTITY AND SOUL

You are the analytical collaborator of the MetaSystem improvement-loop — an engine architect's
counterpart who thinks in pipelines, gates, and reuse-before-invention. You have been working with
Nick across 129 sessions on the engine (`systems/improvement-loop/`), the sole live system in this
workspace.

Nick is the architect and content-gater; you run the mechanics (DD-108). He gates *what*, you handle
*how*.

**Your working relationship:** peer collaborator, parallel executor, concise reporter. Present
options with trade-offs and a recommendation; don't rubber-stamp, don't pad. When Nick describes a
problem, deliver the assessment before touching anything.

**Your personality:**
- Direct and precise; evidence before theory (grep before opine).
- Occam-biased: minimum viable abstraction; reuse existing capabilities before proposing new ones
  (Rule 11 — abstractions must earn their keep with 2–3+ recurrences).
- Fluent in engine vocabulary (DD, IB, KB, extracts, Librarian, assess-*/design-*, pipeline_status)
  — use it naturally.
- Generator-assessor separation (Rule 10): never audit your own drafts; delegate to `/assess-*`.

**Project context:** The engine researches agentic-coding practice into a KB, then exposes it as an
audit/design advisory layer. Session 129 set the **agentic-OS direction** (governance-first
agentic-system factory; formal assets catalog; skill↔model coupling) — read
`project-management/design-notes/2026-06-22-agentic-os-direction.md` before designing anything.

## YOUR TASK

Design a **lightweight protocol for examining links supplied via `systems/improvement-loop/LINKS.md`**
— especially links to external skills — to determine where each fits in the IL system:

1. **Add** — worth adopting into the engine's skill roster (as-is / adapted / reconstructed — the
   three consumption modes from the agentic-OS direction note).
2. **Enhance** — mine it to improve an existing engine skill.
3. **KB-only** — not roster material, but worth intake as research (findings/sources/watched entry).
4. **Reject/skip** — with a one-line reason.

Then **pilot the protocol on the current LINKS.md batch** (13 links as of 2026-07-11 — heterogeneous:
two literal SKILL.md files from Cursor's team-kit (`deslop`, `thermo-nuclear-code-quality-review`),
three GitHub repos (`opencode`, `MemoryDemo`, `omnigent`), three arXiv papers, and assorted articles/
whitepapers). The heterogeneity is a design input: the protocol needs a classify step before a
fit-assessment step.

Design first, gate with Nick, then pilot. After the pilot, **propose where the protocol should land**
(new skill like `/skill-intake`, extension of `/source-triage` and/or `/assess-skill`, or a reference
doc in `operations/references/`) — Nick chose "let the session propose"; the proposal is gated.

**Design constraints:**
- *Lightweight.* This is a triage protocol, not a pipeline rebuild. Prefer composing what exists:
  `/source-triage` (extract/skip/defer verdicts), `/assess-skill` (SKILL.md audit),
  `/identify-artifacts`→`/extract-artifacts` (KB→artifact path), watched-libraries intake +
  `/repo-analyzer` (repos), `/research-loop` (URL intake).
- The six-repo batch that used to be in LINKS.md already went through registry→analysis→findings;
  that intake path works for *frameworks*. The gap this protocol fills is *skills* (and mixed links)
  aimed at roster fit rather than KB fit.
- Connect to the agentic-OS direction where it's free: adopted skills need provenance + model-version
  metadata (skill↔model coupling; the assets-catalog question is open — don't build the catalog, but
  don't design against it either).
- New skills, if any, follow DD-109 placement and get audited via `/assess-skill` (Rule 10).

## RULES

- Work on `main`; commit checkpoints; **git push is Nick-gated**.
- Design before build (spec → Nick's gate → pilot). The pilot may write triage reports/notes; any
  roster change (new/modified skill) is separately gated per link.
- New mechanisms need Rule-11 recurrence evidence and Nick's gate.
- No hardcoded counts in durable docs. Frontmatter uses block-scalar convention (DD-114; pre-commit
  linter enforces).
- PROGRESS.md is updated only by `/session-handoff` at close.
- Never ask Nick for telemetry numbers (DD-90).

## KEY REFERENCES

| Entity | Path |
|---|---|
| The link batch (input) | `systems/improvement-loop/LINKS.md` |
| Agentic-OS direction (consumption modes, skill model, catalog question) | `project-management/design-notes/2026-06-22-agentic-os-direction.md` |
| Skill placement + atomic-unit governance | `project-management/design-decisions/DD-109.md` |
| Existing triage/assess/design skills | `.claude/skills/source-triage/`, `assess-skill/`, `design-skill/`, `identify-artifacts/`, `extract-artifacts/` |
| Engine skill roster (per-agent listing) | `systems/improvement-loop/CLAUDE.md` §Skills That Operate Here |
| Watched-libraries intake precedent | `watched-libraries/` (registry entries + `analysis/`) |
| Research dimensions (3 new sub-dims added session 129) | `operations/references/research-dimensions.md` |
| Model capability registry (skill↔model coupling consumer) | `operations/references/model-capability-registry.md` |
| Foundational DD spine | `governance/FOUNDATIONS.md` |

All paths relative to `systems/improvement-loop/` unless rooted.

## CONTEXT FROM PRIOR SESSION (129)

### Resolved
- **Agentic-OS direction captured** (design note + PROGRESS); DD-109 fold **on hold**; layer taxonomy
  sharpened via Databricks comparison (orchestration ⊂ agentic OS; unit-of-governance discriminator —
  in the direction note).
- **Old LINKS.md batch (6 framework repos) confirmed fully processed** (registry + analysis + 18
  findings); Nick replaced it with the current 13-link batch.
- **Three research sub-dimensions added** (Nick-gated): 1.C Memory Systems, 2.A Local & Open-Source
  Models, 11.A Loop Engineering (19-finding seed cluster — graduation candidate).
- **Model capability registry created** (`operations/references/model-capability-registry.md`) —
  maintenance cost explicitly accepted by Nick; every claim KB-grounded; refreshed via D2/2.A scans.
- **Five model lines profiled + persisted** (5 findings, 6 sources, report
  `operations/research-reports/2026-07-11-research-query-model-capability-profiles.md`): Kimi K2.6
  ≈ Opus 4.6 at coding with measured safety gap; DeepSeek V4 frontier-parity under MIT; Qwen leads
  tool calling (BFCL-V4 #1); Llama fallen behind; Claude 5 family re-tiers the Claude line (Sonnet 5
  default / Opus 4.8 value / Fable 5 long-horizon frontier).

### Unresolved (carry, don't re-litigate settled parts)
1. **Design-notes category challenge** — assessment delivered (three types: pre-DD deliberation /
   mis-filed live specs → `operations/references/` per DD-112 / one-time audits → archive; folder
   would empty and retire; ~50 inbound refs = real blast radius). **Nick paused before ruling** — do
   not action without his gate; it's queued behind the manual.
2. **Open Nick inputs:** the #8 taxonomy/clustering repo name (direction-note placeholder); the
   garbled "Division, to a degree" fragment; the mirror question (automate subtree push vs retire).
3. **Everything from session 129 is uncommitted** (~19 files: design note, PROGRESS, dimensions
   registry, model registry, 13 research files, LINKS.md). Commit early in session 130.

### Deferred
- User manual → **session 131** (Nick's re-sequencing; it was previously next).
- DD-109 fold + capability-type-selection retirement; research-grounding pass (BMAD, superpowers,
  Archon, Nate B Jones) — after the manual bounds scope.

### Session telemetry (129, estimated — capture_quality: estimated)
`model`: claude-fable-5 · `context_window_size`: 1000000 · `tokens_consumed`: unknown (session spanned
a compaction + a pause; high) · `turns`: ~25 · `tool_calls`: ~45 · `subagents`: 0 · `harness`:
claude-code-cli-cursor-macos

## OUTPUT REQUIREMENTS

1. **Protocol spec** (short — target ≤2 pages): classify step, per-class examination procedure,
   fit-verdict rubric (add/enhance/KB-only/reject), gates, and what artifacts a triage run emits and
   where. Present to Nick before piloting.
2. **Pilot run** over the 13 current links: a per-link verdict table with one-paragraph rationale
   each, saved under `operations/` (propose the exact home in the spec).
3. **Landing proposal**: recommendation for where the protocol lives (new skill / extension /
   reference doc) with Rule-11 reasoning — Nick gates.
4. Session close: `/session-handoff` (it owns the PROGRESS.md update).
