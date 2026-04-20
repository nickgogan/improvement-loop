---
notion_id: null
log_entry: "DD-88 supersedes DD-72 — lifecycle aligned to DD-80 pipeline"
actor: "Agent: Claude"
area: null
change_type: "Governance"
milestone: null
rationale: "DD-72 governed the finding lifecycle under the Proposer pipeline (Research → Propose → Codify). DD-80 eliminated the Proposer stage but left DD-72's lifecycle orphaned — still Binding on paper, pointing to a deprecated workflow. DD-88 restates the lifecycle under the DD-80 pipeline (/identify-artifacts + /extract-artifacts / /synthesize-guide) and incorporates DD-81's pattern-vs-non-pattern routing. Also codifies the proposer_priority → priority field rename executed earlier in this session."
source_dd: "DD-88, DD-72, DD-80, DD-81, DD-44"
target_system: "Improvement Loop"
timestamp: "2026-04-20T00:00:00.000Z"
---

# DD-88 Supersedes DD-72 — Lifecycle Aligned to DD-80 Pipeline

## What Changed

- Created **DD-88** (Binding) — Research finding lifecycle under the post-DD-80 pipeline. Governs classification routing, P3 re-entry via `/reassess-priorities`, and form-split extraction/synthesis.
- Marked **DD-72** (Superseded by DD-88). Status transitioned from Binding to Superseded per DD-44. Added supersession callout at the top of DD-72 body. Retained as historical context.
- Codified the **`proposer_priority` → `priority`** field rename executed earlier in the session (commit `40b4021`) in DD-88's narrative.

## Why

DD-80 (2026-04-19) eliminated the Proposer stage and replaced it with `/identify-artifacts` + `/extract-artifacts`. Its "Effect on Prior DDs" table addressed DD-29, DD-30, DD-39, DD-41, DD-46, and DD-77 — but omitted DD-72. DD-72 remained Binding while describing a pipeline that no longer existed: "Queue for `/research-proposer`" in a world where `/research-proposer` is deprecated.

The session-44 field rename (`proposer_priority` → `priority`) surfaced the drift. Renaming without the governance update would have left DD-72's prose describing a deprecated workflow under a renamed field — stale on both axes.

DD-88 closes the gap by restating DD-72's intent (priority-governed lifecycle, no-downgrade rule, explicit exits) under DD-80's pipeline and incorporating DD-81's routing split (pattern forms → `/synthesize-guide`, non-pattern forms → `/extract-artifacts`).

## Substantive Changes vs. DD-72

1. **Form-split routing.** DD-72 treated all P1/P2 findings as proposal candidates. DD-88 splits by form: patterns aggregate into guides, non-patterns extract individually.
2. **P3 re-entry.** DD-72 implied P3 was terminal absent manual upgrade. DD-88 makes the evidence-driven upgrade path explicit via `/reassess-priorities`.
3. **Field name.** `proposer_priority` → `priority` (renamed in commit `40b4021`).

## Affected Items

- `systems/improvement-loop/project-management/design-decisions/DD-88.md` — created (Binding)
- `systems/improvement-loop/project-management/design-decisions/DD-72.md` — status → Superseded, `superseded_by: DD-88` added, supersession callout added to body
- This SL entry — logs the supersession for audit trail

## Cross-References to Update

No other Binding DDs reference DD-72 directly (verified via grep). No update needed to other DDs.

Skill docs and agent definitions referencing lifecycle semantics do not cite DD-72 or DD-88 by number — they describe the pipeline operationally and will naturally align with DD-88 going forward.

## Governance Compliance (DD-44)

- New DD has `supersedes: "DD-72"` in frontmatter ✓
- Superseded DD has Status transitioned to Superseded ✓
- Superseded DD has supersession callout at top of body ✓
- Both changes logged to System Log (this entry) ✓
- DD numbers preserved (not renumbered) ✓
