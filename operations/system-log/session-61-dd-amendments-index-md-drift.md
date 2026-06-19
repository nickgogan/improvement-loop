---
notion_id: null
log_entry: "Session 61: DD amendments closing _index.md drift (DD-55, DD-56, DD-65, DD-74, IB-142)"
actor: "Agent: Claude (Nick-sanctioned in-session)"
area: null
change_type: "Governance Amendment"
milestone: null
rationale: "The session-61 _index.md cleanup sweep left four Design Decisions and one IB item out of sync with the new reality. Each DD's text said _index.md catalogs existed or had to be maintained; catalogs no longer exist for most governance folders. Per DD-44's 'minor refinement, same scope' amendment path, each was updated in-place with an amendment footnote rather than superseded via a new DD number."
source_dd: "DD-44"
target_system: "Cross-System"
timestamp: "2026-04-23T00:00:00.000Z"
---

## What Changed

### DD-55 (DD Distribution)
Migration Notes bullet updated — the line about each destination folder having an `_index.md` listing its DDs was marked amended with strikethrough + footnote. New reality: discovery via `/track dd list`, `/dd list`, or ripgrep on frontmatter.

### DD-56 (IB Distribution)
Same shape as DD-55 — Migration Notes bullet about `_index.md` per folder amended with strikethrough + footnote. Discovery via `/track ib list`, `/ib list`, or ripgrep.

### DD-65 (IL Skill Composition)
Local KB Data Model table: removed the `Index` column (all four rows pointed at `_index.md`, all removed). The "After any create/update: Update the corresponding `_index.md`" bullet was rewritten as a Discovery bullet pointing at frontmatter as source of truth.

Also added a note flagging that DD-65's skill inventory (6 skills, April 6) is substantially drifted from current state (24+ skills across 4 agents per DD-82). The skill-inventory portion is effectively superseded piecewise by DD-80, DD-82, DD-83, DD-86, DD-89, DD-91. A formal DD-65 supersession is a larger piece of work — not addressed here.

### DD-74 (Context File Hygiene)
- Decision text (frontmatter `decision:` field) rewritten: the phrase "`_index.md` updates are not blocking" replaced with "Frontmatter on individual artifacts is the source of truth for governance data; catalog files (_index.md) are optional and limited to Dataview-driven live views or load-bearing substrate maps".
- `amended: "2026-04-23"` field added to frontmatter.
- Agent callout updated to match.
- "`_index.md` Is Not Blocking" section replaced with "Frontmatter Is the Source of Truth (amended 2026-04-23)" — reframed in positive-space per the positive-space governance principle. Includes amendment-history note.

### IB-142 (Meta-System Agents Design)
Vault-curator agent scope revised: the "maintains `_index.md` catalogs" responsibility removed. Remaining scope (frontmatter validation, cross-reference integrity, stale-content flagging) preserved. Body gains a "Scope Revision (2026-04-23)" section explaining the change.

## Why Amendment (Not Supersession)

Per DD-44, the "Minor refinement, same scope" path uses body-level amendments logged to the System Log rather than a new DD number. All five changes:
- Preserve the original DD's core decision (DD-55, DD-56, DD-74) or its historical structure (DD-65)
- Address implementation-detail drift, not a direction change
- Log to SL for traceability per DD-44 rollout requirements

DD-65's skill-inventory drift is a separate matter — its scope is broader than this sweep and warrants its own future session.

## Affected Files

- `systems/meta-system/project-management/design-decisions/DD-55.md`
- `systems/meta-system/project-management/design-decisions/DD-56.md`
- `systems/meta-system/project-management/design-decisions/DD-65.md`
- `systems/meta-system/project-management/design-decisions/DD-74.md`
- `systems/meta-system/project-management/implementation-backlog/IB-142.md`

## Cross-References

- Precursor SL: `session-61-index-md-cleanup-sweep.md` (the sweep that created this drift)
- Handoff: `operations/handoff-prompts/handoff-prompt-index-md-full-cleanup.md`
- Authority: DD-44 (amendment vs. supersession rules)
