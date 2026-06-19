---
title: "Session 121 — Phase 2 Slice 2: /detect-drift extended to schematics (date-basis contract)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "drift-detection / schematics / self-evolution-loop"
change_type: "Update"
milestone: null
rationale: "DD-107 §\"What this does NOT decide\" deferred bringing schematics into /detect-drift to the next slice; this is that slice (restructure plan §Phase 2 item 2). Schematics differ from extracts on two axes that required a contract choice: (1) location — they live in knowledge/schematics/, not extracts/, so scan.py gained a second scan root; (2) pointer shape + date basis — schematics carry an array grounded_in (not scalar source_finding) and have no extraction_date (curated, not extracted). The contract chosen and implemented: flag drift when any grounding finding's last_updated strictly post-dates the schematic's `updated` (its last-curation date). This is the natural mirror of the extract rule (finding.last_updated > artifact.extraction_date), substituting `updated` for `extraction_date`. No DD amendment needed — DD-107 anticipated this slice; this SL records the implemented date basis as the contract of record."
source_dd: "DD-29, DD-96, DD-107"
timestamp: "2026-06-18T00:00:00Z"
session: 121
tags:
  - "system-log"
  - "codifier"
  - "detect-drift"
  - "schematics"
  - "phase-2"
  - "self-evolution"
telemetry:
  model: "claude-opus-4-8[1m]"
  tokens_consumed: "unknown"
  context_window_size: 1000000
  context_window_pct_peak: "unknown"
  turns: "~1"
  tool_calls: "~25"
  subagents: 0
  capture_quality: "estimated"
  harness: "claude-code-cli-cursor-macos"
  capture_note: "Single execution turn. scan.py + SKILL.md + this SL in one atomic commit. Drift branch verified by temporary backdate of one schematic's `updated` (reverted), confirming 5 moved groundings flagged and the other schematic stayed clean."
---

# Session 121 — Phase 2 Slice 2: /detect-drift extended to schematics

## Scope (As Executed)

Extended `/detect-drift` to cover the schematic artifact form (DD-107), bringing the two seed
schematics into the engine's self-evolution loop. One coherent change:

1. **`scan.py`** — added `knowledge/schematics/` as a second scan root (alongside
   `extracts/{rules,skills,templates,agents}/`). For each schematic: parse the array `grounded_in`
   and the `updated` date; resolve each grounding to `research-findings/<stem>.md`; flag the
   schematic when **any** grounding's `last_updated > schematic.updated`. Emits a new
   `schematic_drift_hits` list (one hit per schematic, listing every moved grounding);
   `total_scanned` / `clean_count` / `per_form` now combine both roots. `schematics` is a valid
   `--include`/`--exclude` form and is in the default scan set.

2. **`SKILL.md`** — documented the second root, the array-pointer + `updated` date basis, a new
   two-value schematic Recommendation enum (`re-evaluate this schematic against its moved
   grounding` | `dismiss as cosmetic`), a `## Schematic Drift Hits` report section, plus Paths,
   Rules (rule 8), Failure Modes, and DD-107 in the DD table.

## The Date-Basis Contract (Decision of Record)

| | Extracts | Schematics |
|---|---|---|
| Scan root | `extracts/{form}/` | `knowledge/schematics/` |
| Source pointer | scalar `source_finding` | array `grounded_in` |
| Artifact baseline date | `extraction_date` | `updated` (last curation) |
| Drift condition | `finding.last_updated > extraction_date` | `finding.last_updated > updated` (any grounding) |
| Recommendation enum | re-run /extract-artifacts · dismiss · reclassify | re-evaluate schematic · dismiss |

Rationale: schematics are curated, not pipeline-extracted (DD-107), so they carry no
`extraction_date` and `/extract-artifacts` does not apply to them. `updated` is the timestamp that
bumps when a schematic is (re-)curated, so `finding.last_updated > updated` reads as "a grounding
moved after this schematic was last reconciled against its evidence" — the exact self-evolution
signal Phase 2 wants. Equal dates are not drift (strict `>`), consistent with the extract rule.

## Verification

- `--include schematics` against the live tree: 2 schematics enumerated, all 11 `grounded_in`
  findings resolve, 0 drift hits (all groundings' `last_updated` in April predate the 2026-06-18
  curation date), 0 enumeration gaps, 0 unresolvable sources.
- Drift branch proven by temporarily backdating `research-scanning-agent.md` `updated` to
  `2026-01-01`: 1 schematic hit with all 5 groundings flagged as moved; `codebase-audit-workcell`
  stayed clean. Change reverted (tree clean).
- Full default scan (all 5 forms): 123 scanned, 9 pre-existing rule drift hits (unchanged),
  schematics clean; counts reconcile (114 clean + 9 hits = 123).

## What's Pending Nick Gate

- **Merge `engine-collapse-phase-1` → main** — Phase 1 + cleanup + Phase 2 Slices 1–2 unmerged.
- **Next deferred Phase-2 items** (Rule 11 / demand-gated): execution-surface Librarian axis,
  Builder-mode demand→schematic matching, more seed schematics.
