---
notion_id: null
log_entry: |-
  Session 128: FOUNDATIONS.md generated spine map + foundational-DD criteria (DD-115)
actor: "Agent: Claude"
area: null
change_type: "Structure"
milestone: null
rationale: |-
  Nick raised acute governance-sprawl pain: ~80+ binding DDs with no way to tell which define the system's backbone, plus a foundational infra decision (DD-84 publish model) that was effectively un-findable. Ran a 3-lens Perplexity council (architect/maintainer/skeptic) which converged on a generated spine view over canonical DDs (never a hand-authored second source of truth). Built it, then Nick asked for explicit inclusion/exclusion criteria to guard against drift; codified them and ratified the 20-DD set against them. knowledge/ reconciliation (policy-in-disguise docs) deferred to the upcoming agent-vs-skill workflow discussion.
source_dd: "DD-115"
target_system: "improvement-loop"
timestamp: "2026-06-22T00:00:00.000Z"
---

## What Changed

- **`_schema.yaml`**: documented optional `foundational` field (curation flag; does not alter the decision).
- **20 DDs tagged** `foundational: true` (content-preserving insert, frontmatter still valid): DD-29, 36, 37, 41, 44, 47, 52, 53, 54, 55, 56, 59, 80, 82, 84, 86, 103, 104, 105, 108.
- **New** `operations/kb-maintenance-scripts/generate_foundations.py` (+ `--check` staleness mode); reuses `kb_parser`.
- **Generated** `governance/FOUNDATIONS.md` — spine map (id/title/category/path) with the inclusion/exclusion criteria in its header. Marked do-not-edit; DDs canonical.
- **Pointers** added to root `CLAUDE.md` and engine `CLAUDE.md` (referenced, not inlined — DD-74 budget).
- **Pre-commit hook** extended: now also runs `generate_foundations.py --check` to block drift between FOUNDATIONS.md and the flags.
- **DD-115** filed (Binding) — the spine-map decision + the C1–C5 / X1–X5 criteria + the ~20 displacement cap.

## Verification

- Generator: writes 20-DD map; `--check` returns 0 when in sync.
- All 20 tagged DDs re-validated through the frontmatter linter (exit 0).
- Pre-commit hook runs both checks (frontmatter validity + foundations staleness).

## Affected Items

- Decision content (which DDs are foundational) gated with Nick; criteria ratified "as-is".
- Deferred: `knowledge/` policy-in-disguise reconciliation (`capability-type-selection`, `research-to-codification-pipeline`, `upstream-dependency-spectrum`) and DD-109 revisit — pair with the agent-vs-skill topic.
