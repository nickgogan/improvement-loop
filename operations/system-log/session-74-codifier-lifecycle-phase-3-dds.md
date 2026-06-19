---
title: "Session 74 — Codifier: Lifecycle-Spec Phase-3 DDs (DD-98 / DD-99 / DD-100 / DD-101)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "governance / artifact-lifecycle / phase-3-ratification"
change_type: "Add"
milestone: null
rationale: "Closed the lifecycle-spec design loop by filing the four Phase-3 DDs (DD-98 guide-split, DD-99 theme-graduation, DD-100 template-and-agent versioning, DD-101 co-occurrence harvest queue). Phase 3 sits behind Phase 1 (clobber risk) and Phase 2 (drift/redundancy) as creation/structural lifecycle questions — less time-pressured at the time of Phase-1+2 ratification (session 70), now the natural next batch per Nick's session-73 close direction. Each DD codifies its own procedure or structural pattern; cross-DD consistency was spot-checked before filing. Two of the four DDs amend DD-94's closed trigger-tag enum (DD-98 adds `guide-split`; DD-99 adds `theme-graduation`); the amendments honor DD-94's 'new trigger tags require a DD amendment' rule by being the DDs that amend it. DD-100 is the missing Phase-3 sibling to DD-97 — DD-97 governs rule/skill extension; DD-100 governs template versioning and agent version-bump (with DD-82 invariant: agent bumps require Nick's prior approval). DD-101 makes DD-77's 'co-occurrence resolved at read time by downstream consumers' operational for one specific consumer (`/synthesize-guide`), without contradicting DD-77's negative design decision. Phase-3 implementation IBs are session-75+ work, analogous to session 71's IB-154…158 sweep for Phases 1+2."
source_dd: "DD-29, DD-44, DD-77, DD-78, DD-80, DD-81, DD-82, DD-92, DD-93, DD-94, DD-95, DD-96, DD-97, DD-98, DD-99, DD-100, DD-101"
date: "2026-04-26"
session: 74
tags:
  - "system-log"
  - "codifier"
  - "lifecycle-spec"
  - "phase-3"
  - "dd-ratification"
telemetry:
  model: "claude-opus-4-7[1m]"
  tokens_consumed: "unknown"
  context_window_size: 1000000
  context_window_pct_peak: "unknown"
  turns: "~6"
  tool_calls: "~12"
  subagents: 0
  capture_quality: "estimated"
  harness: "claude-code-cli-cursor-macos"
  capture_note: "Codifier disposition. Single-pass DD authorship: read source spec + DD-93..97 form precedent + supporting DDs (DD-77, DD-29, DD-82) + routing table + PROGRESS once each, then drafted all four DDs sequentially in one Codifier pass without mid-session Nick interaction. Four atomic commits (one per DD). Form matches DD-93..97 verbatim — frontmatter, agent callout, Constraint, Why, Rules, Acceptance Criteria, Scope and Non-Goals, Related, Source, Phase-3 Marker. No structural ambiguities surfaced for stop-and-surface; cross-DD consistency check passed inline."
---

# Session 74 — Codifier: Lifecycle-Spec Phase-3 DDs (DD-98 / DD-99 / DD-100 / DD-101)

## Session Scope

**Primary:** File the four Phase-3 DDs from the artifact-lifecycle spec. DD-X5 (guide split), DD-X6 (theme graduation), DD-X8 (template+agent versioning), DD-X9 (co-occurrence harvest). DD-X7 was filed as DD-97 in session 70 (Phase-2 ratification) — Phase 3 is therefore a four-DD bundle, not five.

**Approach:** Codifier disposition; content design + filing in the same session per Nick's session-73 directive ("Codifier disposition" for Phase-3). No Owner involvement needed — no structural ambiguities surfaced that warranted Owner-level governance routing.

**Out of scope:**
- Phase-3 implementation IBs. Analogous to session 71's IB-154…158 sweep for Phases 1+2; session-75+ work.
- `/synthesize-guide`, `/extract-artifacts`, `/identify-artifacts` skill modifications. Downstream of DDs; Phase-3 IB sweep territory.
- Nick-gate application for session-72 items 1+2 (still PENDING). Same posture as before — no in-session edits absent fresh Nick ruling.
- Nick-gate application for session-73 drift hit (`rules/agent-self-reporting-unreliability-independent-eval`, recommended `dismiss as cosmetic`). Same posture; PENDING.
- G7 / G2 / G9 re-synthesis. Live-validation gate for IB-154+155; its own session.
- Operation-file "join rule" subsection (surfaced session 73). IB candidate, not Phase-3 territory.
- Corpus-wide YAML quote-style normalization (surfaced session 73). Owner-routable; not Phase-3.

## Per-DD Filing Table

| DD | Title | Headline Constraint | Notes |
|---|---|---|---|
| **DD-98** | Guide split procedure | Trigger conjunction: ≥25 findings AND ≥2 distinct practitioner questions. Codifier emits split proposal at `operations/split-proposals/`; per-split DD codifies destinations. Source guide deprecated; destinations open fresh changelogs. | Amends DD-94's closed trigger-tag enum to add `guide-split` (used in both source's final entry and destinations' first entries). |
| **DD-99** | Theme graduation procedure | Trigger conjunction: ≥5 unrouted findings AND `same-problem` linkage. Asymmetric Nick gate by structural impact: PROMOTE requires per-graduation DD (research-dimensions.md addition), ABSORB requires only ruling-on-proposal + routing-table update. Cross-dimension findings disqualify ABSORB. | Amends DD-94's closed trigger-tag enum to add `theme-graduation` (PROMOTE path's new-guide first entry only). ABSORB path uses existing `dimension-rebalance` tag — no amendment needed for that path. |
| **DD-100** | Template and agent versioning | Side-file `<name>-v<N>.md` regeneration; v1 implicit (no suffix), v2+ explicit. Each version is independent — own frontmatter, own contract, own context, own DD-95 lifecycle pointer. Templates auto-bump on /extract-artifacts evolution detection (DD-97-equivalent calibration); agents NEVER auto-bump (DD-82 invariant). Promotion = deployment. | Adds `version: integer` frontmatter field (optional v1, required v2+). DD-96 scans all versions independently. |
| **DD-101** | Co-occurrence harvest queue | `/synthesize-guide` scans absorbed pattern findings for embedded artifact-shaped content (rule, skill, template); appends rows to per-guide `<guide-stem>.harvest-queue.md`. Status enum: queued / nick-approved / nick-dismissed / extracted / superseded. Nick gates per-row. Approved rows feed `/extract-artifacts` directly with original pattern finding as `source_finding`; DD-97 fires for rule/skill targets; DD-100 fires for template targets. | Agents excluded per DD-82 invariant — never queued. Original pattern finding remains pattern-classified throughout (DD-77 preserved). |

All four DDs filed without amendment to spec content. Form matches DD-93..97 verbatim.

## Cross-DD Consistency Notes

Spot-checked before filing all four:

1. **DD-98 + DD-94 trigger-tag enum.** DD-94 says "new trigger tags require a DD amendment, not ad-hoc invention." DD-98 IS the DD amendment for `guide-split`. The enum bullet list in DD-94's body will be updated by the Phase-3 IB sweep (not session 74). Same pattern for DD-99 + `theme-graduation`. No conflict.

2. **DD-99 + IB-153 (`/dimension-rebalance`).** ABSORB path explicitly relies on `/dimension-rebalance` to reclassify findings into the destination dimension; the destination guide's next regen uses the existing `dimension-rebalance` trigger (already in DD-94's enum). The infrastructure DD-99 depends on is the IB-153 work; if IB-153 evolves, DD-99's ABSORB path may need re-validation. No conflict at filing time.

3. **DD-100 + DD-95 lifecycle pointer.** Each version is a separate file with its own frontmatter — `template.md` (v1) and `template-v2.md` (v2) each carry independent `last_change_session` and `last_change_sl` per DD-95. No frontmatter sharing; no cross-version coupling. Verified: `<name>-v2.md` is structurally a fresh DD-95-conformant artifact at write time.

4. **DD-100 + DD-96 source-drift scan.** DD-96 currently scans all non-guide extracts in `extracts/{rules,skills,templates,agents}/`. With versioning, multiple versions of a single template/agent coexist. DD-96's per-artifact iteration is unmodified — each version produces its own drift entry independently. May add reporting noise for non-canonical versions; addressed as Open Question on DD-100, not as a blocking conflict.

5. **DD-101 + DD-77.** Critical consistency check. DD-77's negative design decision: "Router picks one form, full stop. No `secondary_form`, no co-occurrence flagging at classification time." DD-77 also says: "Co-occurrence is resolved at read time by downstream consumers." DD-101 makes one specific consumer (`/synthesize-guide`) the explicit resolver. Verified: DD-101 does NOT add Router-side flagging, does NOT mark the original pattern finding with secondary form, does NOT alter DD-77's invariant. The harvest happens at synthesis time, not classification time. The harvested artifact's form is its own assigned_form (rule/skill/template); the original pattern finding remains pattern-classified and gains a `consumed_by[]` entry per the standard consumption convention. No contradiction.

6. **DD-101 + DD-97 / DD-100 downstream.** Approved harvest queue rows feed `/extract-artifacts` with target form `rule`, `skill`, or `template`. DD-97's extension rubric fires for rule/skill targets (extend-vs-new). DD-100's version-bump path fires for template targets (version-existing-vs-new). DD-101 is the upstream feeder; DD-97 and DD-100 govern the downstream extraction shape. No duplication of logic; clean separation.

7. **DD-98 + DD-93 preserved sections on split.** When a guide is split, both `## Nick's Annotations` blocks and `<!-- PRESERVE -->` regions need explicit per-region disposition (route-to-A, route-to-B, or duplicate-to-both) in the per-split DD. Implicit handling forbidden — DD-93's preservation invariant requires explicit choice. Verified: DD-98's Rules §5 makes this explicit.

## Notes on the DD-X7 Numbering Gap

The source spec lists nine proposed DDs (DD-X1 through DD-X9, with no item explicitly skipped in the list). The Phase-3 batch was sized as four DDs because DD-X7's content (extension rubric for rules/skills) had already been filed as DD-97 in session 70's Phase-2 ratification. Phase 3 = DD-X5, DD-X6, DD-X8, DD-X9 = DD-98, DD-99, DD-100, DD-101.

The handoff prompt explicitly flagged this: "DD-X7 is intentionally skipped per the source spec — there are four Phase-3 DDs, not five." Verified at filing.

## Spec Recommendation-Shape Note

Spec §Recommendation Shape's Phase-3 grouping reads "Phase 3 (procedural): Formalize guide split and theme graduation procedures. File DD-X5, DD-X6, DD-X8." DD-X9 is not listed in that grouping but IS in spec §Proposed DDs as item #9 (co-occurrence harvest). The session-73 handoff (Nick-validated) treats DD-X9 as a Phase-3 sibling. DD-101's Source section captures this provenance. No spec edit was made — the design note remains a frozen reference per the standing rule.

## Deviations

None.

- **No spec rewrites.** The design note `2026-04-20-artifact-lifecycle-spec.md` was NOT edited. The DDs are the live governance.
- **No mid-session scope expansions.** The four-DD Phase-3 bundle was filed as scoped; no in-session backfill (Phase-3 has no equivalent to DD-95's 31-artifact backfill — versioning is forward-looking).
- **No Phase-3 IB filing.** Per standing rule and the handoff's explicit out-of-scope list. Phase-3 IBs are session-75+ work.
- **No DD-94 enum-list edit in DD-94 body.** DD-98 and DD-99 amend DD-94's enum logically; the bullet-list edit in DD-94's body is Phase-3 IB sweep territory. Filing the amending DDs is the governance event; updating the amended DD's prose is the implementation event.

## Outcome

The artifact-lifecycle spec's design loop is closed. Phase 1 (DD-93/94/95, session 70), Phase 2 (DD-96/97, session 70), and Phase 3 (DD-98/99/100/101, session 74) are all ratified.

The Improvement Loop now has codified procedures for:

- **Within-class lifecycle** — guides preserve and changelog; non-guide extracts track session-pointer + drift.
- **Creation discipline** — extension rubric (rules/skills, DD-97); versioning (templates/agents, DD-100); never-auto-create for agents (DD-82 + DD-100).
- **Cluster lifecycle** — split (DD-98) and graduation (DD-99) with calibrated Nick-gate weights.
- **Co-occurrence resolution** — DD-101 makes DD-77 operational for `/synthesize-guide`.

The next natural Codifier units on the prioritization queue are (per PROGRESS.md):

- **G7 / G2 / G9 re-synthesis** — top unblocked Codifier unit; live-validation gate for IB-154 + IB-155. G7 is most overdue (+11 findings).
- **Retroactive migration of ~100 non-guide/non-pattern extracts** — pipeline-collapse Phase M1 audit follow-up.
- **IB-153 (`/dimension-rebalance` after Sub-dim 1.B)** — not urgent per Nick.

Phase-3 implementation IBs themselves (DD-98 through DD-101 procedural mechanics) can be planned in parallel; they are not on the prioritization queue at this session's close.

## Cross-References

- **Lifecycle spec (frozen reference):** `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- **Filed DDs (Phase 3):** `project-management/design-decisions/DD-98.md`, `DD-99.md`, `DD-100.md`, `DD-101.md`
- **Related DDs (Phase 1+2 ratification predecessors):** `DD-93.md`, `DD-94.md`, `DD-95.md`, `DD-96.md`, `DD-97.md`
- **DDs amended-by-reference:** `DD-94.md` (closed trigger-tag enum extended by DD-98 and DD-99; bullet-list edit deferred to Phase-3 IB sweep)
- **Predecessor SLs:**
  - `session-70-owner-lifecycle-spec-phase1-ratification.md` (Phase 1 + Phase 2 ratification — the form precedent for this session)
  - `session-71-codifier-ib-154-ib-155-synthesize-guide-update.md` (Phase 1+2 implementation sweep — the IB-pattern precedent for the Phase-3 IB sweep that follows this session)
  - `session-73-codifier-detect-drift-smoke-test.md` (immediate predecessor; produced this session's handoff)
- **Handoff input:** `operations/handoffs/handoff-prompt-session-74-codifier-lifecycle-phase-3-dds.md`
