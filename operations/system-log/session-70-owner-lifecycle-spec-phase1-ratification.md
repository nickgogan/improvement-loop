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

## Cross-References

- **Lifecycle spec (frozen reference):** `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- **Filed DDs:** `project-management/design-decisions/DD-93.md`, `DD-94.md`, `DD-95.md`
- **Filed IBs:** `project-management/implementation-backlog/IB-154.md`, `IB-155.md`, `IB-156.md`
- **Schema:** `_schema.yaml` (Lifecycle Tracking block)
- **Predecessor SL:** `session-69-codifier-g3-entry15-fold-in.md`
- **Handoff input:** `operations/handoffs/handoff-prompt-session-70-owner-lifecycle-spec-phase1-unblock.md`
