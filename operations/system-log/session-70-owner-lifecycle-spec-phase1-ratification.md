---
title: "Session 70 — Owner: Lifecycle-Spec Phase-1 Ratification (DD-93/94/95)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Owner disposition)"
area: "governance / artifact-lifecycle / phase-1-ratification"
change_type: "Add"
milestone: null
rationale: "Ratified Phase 1 of the artifact lifecycle spec authored by Codifier on 2026-04-20 (`project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`) — three DDs that had sat behind a Nick-gate for six sessions. DD-93 codifies guide regeneration's preserved-section contract (canonical `## Nick's Annotations` + `<!-- PRESERVE -->` regions, post-regen regression test). DD-94 codifies guide companion changelog files in `extracts/guides/changelog/` with closed trigger-tag enum, ~10-line cap, most-recent-first append. DD-95 codifies `last_change_session` (int) + `last_change_sl` (validated SL stem) frontmatter on non-guide extracts with guides explicitly excluded. All three DDs accepted as-spec — no amendments. Three implementation IBs queued (IB-154, IB-155, IB-156). Schema (`_schema.yaml`) updated with the two DD-95 fields in a new `Lifecycle Tracking` block. 31-artifact retroactive backfill executed in-session per Nick directive (scope expansion from spec's deferred-IB framing). Phase-1 ratification unblocks G7 / G2 / G9 re-synthesis, the next-largest pending Codifier unit."
source_dd: "DD-29, DD-44, DD-78, DD-80, DD-81, DD-86, DD-92, DD-93, DD-94, DD-95"
timestamp: "2026-04-26T00:00:00Z"
session: 70
tags:
  - "system-log"
  - "owner"
  - "lifecycle-spec"
  - "phase-1"
  - "dd-ratification"
  - "schema-change"
  - "backfill"
telemetry:
  model: "claude-opus-4-7[1m]"
  tokens_consumed: "unknown"
  context_window_size: 1000000
  context_window_pct_peak: "unknown"
  turns: "~8"
  tool_calls: "~15"
  subagents: 0
  capture_quality: "estimated"
  harness: "claude-code-cli-cursor-macos"
  capture_note: "Owner walkthrough: read spec once, presented each DD's intent + frontmatter shape + acceptance criteria + open question, took Nick's ruling, filed. No propose-first cycle on the DDs themselves (Phase-1 ratification mandate per handoff)."
---

# Session 70 — Owner: Lifecycle-Spec Phase-1 Ratification (DD-93/94/95)

## Session Scope

**Primary:** Walk Nick through DD-X1 / DD-X3 / DD-X4 one at a time. For each: read spec section, present intent + frontmatter shape + acceptance criteria + any open question, take Nick's ruling, file the DD. After all three are filed, queue implementation IBs.

**Scope expansion mid-session:** Nick directed in-session execution of the DD-95 retroactive backfill rather than deferring it to IB-156. Surfaced as scope change in DD-95's body and IB-156's reduced scope; not a deviation.

**Out of scope:**
- Phase 2 DDs (DD-X2 source-drift detection, DD-X7 extension rubric).
- Phase 3 DDs (DD-X5 split, DD-X6 graduation, DD-X8 versioning, DD-X9 co-occurrence harvesting).
- G7 / G2 / G9 re-synthesis (becomes top unblocked once Phase-1 ratification lands; IB-154 + IB-155 implementation gates the next regen).
- `harness-engineering-third-evolution` raw → classified promotion (deferred per queue).

## Per-DD Ruling Table

| DD | Title | Ruling | Notes |
|---|---|---|---|
| **DD-93** | Guide regeneration preserves designated sections | **Accepted as-spec** | Dual-mechanism (canonical named section + `<!-- PRESERVE -->` regions) presented with open question on whether to narrow to one. Nick accepted dual. Post-regen regression test fails closed. |
| **DD-94** | Companion changelog files for guides | **Accepted as-spec** | Append direction confirmed: most-recent-first (top). Trigger-tag closed enum: `staleness-threshold` \| `nick-request` \| `dimension-rebalance` \| `finding-removed` \| `structural-edit`. `initial-synthesis` permitted only for retroactive stubs. ~10-line cap with 11-15 warning, >15 abort. |
| **DD-95** | Frontmatter `last_change_*` on non-guide extracts | **Accepted as-spec + scope expansion** | `last_change_session` (int) + `last_change_sl` (SL stem, validated). Both fields required; missing SL stem aborts write. Nick directed in-session backfill instead of deferring to IB. Schema (`_schema.yaml`) updated. |

No DD was amended or rejected. No spec sections were flagged for Phase-2 reconsideration.

## Per-IB Scope

| IB | DD | Scope | Priority |
|---|---|---|---|
| **IB-154** | DD-93 | `/synthesize-guide` preservation enforcement: capture preserved surfaces pre-regen; regenerate structural body; re-insert preserved content; post-regen byte-equality regression test; fail-closed on drift. 4 acceptance cases + 1 negative. Codifier scope. P2. |
| **IB-155** | DD-94 | Two work items: (a) `/synthesize-guide` companion-changelog appender — locate-or-create the `<guide-stem>.changelog.md` file, construct entry per DD-94 shape, enforce trigger-tag enum + line cap, insert at top. (b) Retroactive stub backfill for the 11 staged guides — one-time `## 2026-04-19 — Session 44 — initial-synthesis` stub per guide. Codifier scope. P2. |
| **IB-156** | DD-95 | Reduced scope: writer-side code change only — backfill executed in-session. `/extract-artifacts` populates both fields on every non-guide create + update; validates SL stem against `operations/system-log/`; aborts write on missing SL or unknown session number; never touches guide frontmatter. Codifier scope. P2. |

IB-154 + IB-155 are gating for G7 / G2 / G9 re-synthesis. IB-156 is independent.

## In-Session Backfill (DD-95 Phase-1 expansion)

Executed retroactive backfill of `last_change_session` + `last_change_sl` on 31 non-guide extracts. Patterns excluded (route to guides per DD-81); guides excluded (use companion changelog per DD-94).

**Scope:**
- `extracts/rules/` — 12 artifacts
- `extracts/skills/` — 12 artifacts
- `extracts/templates/` — 5 artifacts
- `extracts/agents/` — 2 artifacts
- **Total: 31 / 31 written; 0 backfill-gaps.**

**Session attribution (from git log evidence):**
- **Session 44** (`session-44-codifier-extraction-run`) — 26 artifacts. Bulk 2026-04-19 set + 2 from 2026-04-20 (`surgical-change-agent-scope`, `multi-agent-proportional-content-summarization`). Confirmed via "Session 44 extraction: reassessment (3 bumps) + 2 artifacts staged" commit.
- **Session 63** (`session-63-codifier-guide-routing-extract-dd92`) — 1 artifact (`confirm-failure-first-tdd`). Confirmed via DD-92's `Source` line naming this artifact as the session-63 reference implementation.
- **Session 66** (`session-66-codifier-ib-150-acceptance-test`) — 4 artifacts (`claudemd-minimum-viable-rule-only-add-globally-true-lines`, `explicit-permission-allow-listing-for-agent-resource-access`, `iterative-refinement-loop-with-quality-gate`, `task-to-file-routing-table-in-context-files`). All in commit "Session 66: close — IB-150 acceptance test PASS + bookkeeping fix".

All three SL stems verified to resolve to `operations/system-log/<stem>.md` before any writes. Insertion point: immediately after `extraction_date:` in artifact frontmatter (consistency anchor for DD-95 writer-side code in IB-156).

## Schema Update

`_schema.yaml` updated with a new `Lifecycle Tracking (non-guide extracts only — DD-95)` block adding:
- `last_change_session: integer`
- `last_change_sl: string` (SL filename stem; write-validated)

Block placed between Pipeline Tracking (research-finding only) and Session Telemetry. Comment block explicitly notes guide exclusion and the validation contract. Findings, sources, authorities, and guide-class extracts unaffected.

## Deviations

1. **Scope expansion: in-session DD-95 backfill.** Nick directed backfill of all 31 non-guide extracts to be done in this session rather than deferred to IB-156. Owner accepted (Nick gate satisfied), surfaced in DD-95 body and IB-156 notes, executed cleanly. Not a procedural deviation — explicit Nick directive expanding session scope.
2. **No spec rewrites.** Per handoff rule, the design note `2026-04-20-artifact-lifecycle-spec.md` was NOT edited. The DDs are the live governance; the design note remains a frozen reference.

## Drift Surfaced (Not Acted On)

- **`_index.md` files in `extracts/{rules,skills,templates,agents}/`.** Per governance rule "Frontmatter is the source of truth," these were not updated to reflect the two new fields. Filtering by frontmatter (e.g., `grep "last_change_session" extracts/rules/*.md`) is the canonical query path.
- **`templates/tech-stack-pinning-table.md`** carries `created: '{{LAST_REVIEWED}}'` and `updated: '{{LAST_REVIEWED}}'` — placeholder values from a template-of-templates that were never resolved. Out of session-70 scope; flagged for future hygiene pass.

## Outcome

Phase-1 lifecycle ratification complete. The three DDs are now the live governance for guide regeneration safety, guide change-log capture, and non-guide artifact session-pointer maintenance. The next session can pick up either:
- **Codifier:** G7 / G2 / G9 re-synthesis (after IB-154 + IB-155 implementation), OR
- **Codifier:** IB-154 / IB-155 / IB-156 implementation if `/synthesize-guide` and `/extract-artifacts` are to be made compliant ahead of the re-synthesis.

The 31-artifact retroactive backfill makes the entire non-guide extract corpus DD-95-conformant from session 70 forward.

## Post-Phase-1 Governance Work (Nick Scope Expansion)

After Phase-1 close, Nick directed two additional governance items: DD-78 amendment (Contract triple-role) and DD-65 full supersession. Both were on the standing queue (DD-78 marked `[deferred]` until reference layer is more exercised; DD-65 marked "Position TBD"). Nick judged the reference-layer-exercise threshold met (sessions 47-49 + operational use in `/assess-skill`/`/assess-agent`) and authorized both.

### DD-78 Amendment — Contract Triple-Role

**Path:** In-place body amendment per DD-44 §When-to-Amend ("Minor refinement, same scope"). No new DD number.

**Substance:** Added new section `## Contract Triple-Role (amended 2026-04-26 per session-70 ratification)` between `## Why` and `## Related`. Names the three roles Contract sections do operationally:

1. **Artifact-self-governance** (original DD-78 role) — runtime semantics: preconditions, invariants, governance, recovery for the artifact when it fires.
2. **Emergent audit criteria** — `/assess-skill` and `/assess-agent` derive WHAT TO CHECK directly from Contract content. No separate audit-criteria schema; Contract IS the audit criteria.
3. **Audit-applicability gating** — Contract `preconditions` act as gates determining WHETHER audit checks fire ("Preconditions-as-gates pattern" in `operations/references/librarian/audit.md`).

**Provenance:** Roles 2 and 3 surfaced during the Librarian reference-layer build (sessions 47-49). The Contract triple-role flag in session-48 SL was the initial framing flag; session-49 SL UC-6.2 was the second; session-70 codifies. Three sessions of operational use cleared the "wait for recurrence" threshold from standing feedback principles.

**Frontmatter touch:** Added `updated: "2026-04-26"`. Status unchanged (Binding). `date: "2026-04-11"` preserved.

**Cross-References update:** Added the operational anchors (`audit.md`, `agent.md`, `2026-04-21-librarian-use-case-registry.md`) and the three SL provenance links (sessions 48, 49, 70).

**Outcome:** DD-78 is now self-describing for the consumer-side audit pathway. Future agent sessions reading DD-78 will encounter the triple-role property without needing to grep SLs to understand why Contract is the universal interface.

### DD-65 Supersession — Path B (No Successor)

**Path:** Status change + body callout per DD-44 §Mark-as-Superseded-no-successor ("DD no longer applies, no successor needed"). Two paths were presented to Nick (Path A: file successor DD; Path B: no-successor supersession). Nick chose Path B.

**Rationale presented:** Path A would require a new DD that recapitulates DD-80/82/83/86/89/91 + the local-first KB data model — duplicated content, conflicts with token-economy principle. Path B preserves history, marks DD-65 inactive for query purposes, points future readers to the live references already in place.

**Substance:**

- **Frontmatter:** `status: "Binding"` → `status: "Superseded"`. Added `updated: "2026-04-26"`. `supersedes: "DD-35"` preserved (DD-65's own predecessor link).
- **Body callout** added at top, before existing "For agents" line. Enumerates piecewise supersession:
  - **Skill inventory + 4-agent architecture:** DD-82
  - **Pipeline:** DD-80
  - **On-demand research:** DD-83
  - **Owner autonomy:** DD-86
  - **Reference layer architecture:** DD-89 (four-zone)
  - **Reflections-to-proposals:** DD-91
  - **Local-first KB data model + Perplexity toolchain:** `systems/improvement-loop/CLAUDE.md` + DD-29 + DD-49
- **Body content preserved.** Per DD-44 §1 ("Never delete or renumber a DD"), the 2026-04-06 snapshot remains as historical record.

**Cross-reference scan (DD-44 §Rollout step 5):** Searched all DD files for references to DD-65. The only non-self reference is `DD-35.md`, which is itself already Superseded (DD-35 has `status: "Superseded"` and `superseded_by: "DD-65"`). No active Binding DDs reference DD-65. The supersession chain `DD-35 → DD-65 → [piecewise]` is preserved without further edits.

**Outcome:** DD-65 is now filtered out of `status: "Binding"` queries. The active IL state is fully described by the union of DD-80/82/83/86/89/91 + IL CLAUDE.md + `_schema.yaml`. The 2026-04-06 historical snapshot remains accessible for provenance.

### Per-Action Summary

| Action | DD | Mechanic | Result |
|---|---|---|---|
| Amend | DD-78 | In-place body section + Cross-Refs update + `updated:` field | Status remains Binding; triple-role framing now self-described |
| Supersede | DD-65 | Status change + body callout + `updated:` field | Status now Superseded; piecewise supersession chain enumerated |

No new DD numbers consumed. Two existing DDs touched in-place per their respective DD-44 paths.

## Lifecycle-Spec Phase-2 Ratification (Nick Scope Expansion)

After the post-Phase-1 governance items (DD-78 amendment + DD-65 supersession), Nick directed Phase-2 of the lifecycle spec — the two remaining non-guide-lifecycle DDs (DD-X2 source drift detection, DD-X7 extension rubric for rules / skills). Per spec §Recommendation Shape, Phase 2 was the natural next batch ahead of Phase 3 (which addresses creation/structural questions and is deferred).

### DD-96 (DD-X2) — Source Drift Detection

**Substance:** Non-guide extracts (rules / skills / templates / agents) are scanned on-demand for source drift. Trigger: `source_finding.updated > artifact.extraction_date` (strict; equal dates not drift). Response: emit drift report at `operations/drift-reports/<YYYY-MM-DD>-source-drift.md` with closed three-value Recommendation enum (`re-run /extract-artifacts on this finding` | `dismiss as cosmetic` | `reclassify`). Read-only invariant — scan never modifies artifacts; never auto-re-extracts. Nick gates re-extraction.

**Trigger mechanism — three options considered, (a) selected:** (a) on-demand new skill (cheapest mechanism cost; matches IL operational rhythm), (b) embedded in `/extract-artifacts` (couples concerns), (c) periodic (premature operational discipline). Initial draft proposed Curator ownership (mistaken read of Nick's directive); corrected to Codifier ownership per Nick's clarification — drift detection is Codifier's territory, not the planned Vault Curator's broader vault-integrity scope.

**Producer/consumer pairing with DD-95:** DD-95 records when an artifact changed (last_change_session pointer); DD-96 detects when source content changed. Together they cover both sides of the drift window for non-guide extracts.

**No-autonomous-regen invariant:** intentionally rejected the natural temptation to re-extract on detected drift. Source updates are not always artifact-relevant; the DD-29 stage-boundary gate is structural. Report-only matches the gate.

**Frontmatter:** `target_system: "Improvement Loop"`, `scope_category: "Process"`, status Binding from filing. New directory `operations/drift-reports/` will be created on first scan run (IB-157 implementation work).

### DD-97 (DD-X7) — Extension Rubric for Rules / Skills

**Substance:** Before drafting a new rule or skill artifact, `/extract-artifacts` scans the matching `extracts/{rules,skills}/` directory for semantically similar artifacts. On match, emit a structured extension proposal (candidate + existing artifact + diff sketch + Codifier recommendation from closed enum: `extend existing` | `create new (false positive)` | `parameterize as mode variant`). Skill does NOT auto-merge; Nick rules per proposal. No-match path unchanged from current behavior.

**Per-class extension shape:**
- **Rule:** append a row to existing rule's "Evidence" section; body wording delta optional (Codifier proposes; Nick gates).
- **Skill:** add mode flag to existing skill's invocation contract; original behavior remains default; new variant documented as mode option.

**Templates and agents are out of scope** — templates use versioning per future DD-X8 (deferred Phase 3); agents never auto-create per spec §2.3 (DD-82 governs the 4-agent architecture).

**Calibration — Open Question 5 resolution.** Three calibrations were presented: (i) LLM judgment, loose; (ii) ContractSpec-overlap structured; (iii) hybrid (both signals required). Nick selected **(i)**. Rationale: starting strict and loosening on observed under-firing is harder than starting loose and tightening on observed false-positive volume. Nick gate is the structural backstop — false positives cost one read, not a corpus violation. Promotion to (ii) or (iii) requires a follow-up DD if false-positive volume justifies it.

**Why now (vs deferring on the "tolerate one-off" principle):** corpus is at 12 rules + 12 skills today; mechanism cost is low while corpus is small. Same logical pattern as DD-94 (companion changelogs) — install discipline before volume forces a retrofit. Past 50 of either form, manual review burden compounds.

### Per-DD Phase-2 Ruling Table

| DD | Title | Ruling | Notes |
|---|---|---|---|
| **DD-96** | Source drift detection (non-guide extracts) | **Accepted as-spec, calibration (a) on-demand** | First-draft ownership corrected from Curator → Codifier per Nick clarification. No structural changes. |
| **DD-97** | Extension rubric for rules / skills | **Accepted as-spec, calibration (i) LLM-loose** | Open Q5 resolved in favor of loose recall + Nick-gate backstop. Calibration tightening deferred to follow-up DD if needed. |

### Per-IB Phase-2 Scope

| IB | DD | Scope | Priority |
|---|---|---|---|
| **IB-157** | DD-96 | Build new on-demand `/detect-drift` skill at `.claude/skills/detect-drift/SKILL.md`. Procedure: enumerate non-guide extracts; resolve `source_finding`; compare dates; emit drift entries (closed Recommendation enum) at `operations/drift-reports/<YYYY-MM-DD>-source-drift.md`. Read-only invariant. 6 acceptance cases. Codifier scope. P2. New directory created on first scan. |
| **IB-158** | DD-97 | Update `.claude/skills/extract-artifacts/SKILL.md` to add corpus-scan step before drafting rule or skill artifacts. LLM-loose semantic-similarity check. Emit structured extension proposal on match (candidate + existing artifact + diff sketch + recommendation). Templates/agents skip the rubric. No-match path unchanged. 6 acceptance cases. Codifier scope. P2. |

Both IBs are unblocked (no upstream dependencies). IB-157 builds a new skill; IB-158 modifies an existing skill.

### Phase-2 Summary

| Action | DD | Mechanic | Result |
|---|---|---|---|
| File | DD-96 | New DD; Codifier ownership; on-demand trigger; report-only | Source drift detection is now codified. Producer-side counterpart to DD-95's consumer-side pointer. |
| File | DD-97 | New DD; LLM-loose calibration (i); propose-don't-decide; Nick-gate merge | Extension rubric prevents redundant artifacts at corpus scale. Templates/agents deferred to Phase 3. |

**Out of scope for session 70:** Phase 3 (DD-X5 split, DD-X6 graduation, DD-X8 versioning, DD-X9 co-occurrence harvesting) remains deferred per spec §Recommendation Shape. Phase 3 addresses creation/structural lifecycle questions; less time-pressured than Phase 1 (clobber risk) or Phase 2 (drift / redundancy).

## Cross-References

- **Lifecycle spec (frozen reference):** `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- **Filed DDs (Phase 1):** `project-management/design-decisions/DD-93.md`, `DD-94.md`, `DD-95.md`
- **Filed DDs (Phase 2):** `project-management/design-decisions/DD-96.md`, `DD-97.md`
- **Filed IBs:** `project-management/implementation-backlog/IB-154.md`, `IB-155.md`, `IB-156.md`, `IB-157.md`, `IB-158.md`
- **Amended DD:** `project-management/design-decisions/DD-78.md` (Contract triple-role)
- **Superseded DD:** `../meta-system/project-management/design-decisions/DD-65.md`
- **Schema:** `_schema.yaml` (Lifecycle Tracking block)
- **Predecessor SL:** `session-69-codifier-g3-entry15-fold-in.md`
- **Handoff input:** `operations/handoffs/handoff-prompt-session-70-owner-lifecycle-spec-phase1-unblock.md`
