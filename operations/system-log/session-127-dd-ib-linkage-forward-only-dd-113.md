---
notion_id: null
log_entry: "Session 127: DD<->IB linkage made forward-only via source_dd (DD-113); ib_items retired"
actor: "Agent: Claude"
area: null
change_type: "Data Integrity"
milestone: null
rationale: "Closed the session-126 residual on the source_dd/ib_items asymmetry. Nick gated option B1 (forward-only linkage; reverse derived by query, no stored reverse field). Filed DD-113. Migration: source_dd rewritten to YAML-list form across all IB items (single->one-item list, comma-strings split, nulls preserved); 4 non-lossy reconciliations folding prior reverse claims into the forward link (IB-142->[DD-53,DD-60], IB-146->[DD-45,DD-81], IB-147->[DD-45,DD-77,DD-80], IB-170->[DD-111,DD-112]); ib_items field removed from all DD frontmatter; _schema.yaml updated (source_dd = SSOT, ib_items removed with do-not-reintroduce note); /dd, /track, /governance-audit skills updated to stop emitting/gathering ib_items."
source_dd: "DD-113"
target_system: "improvement-loop"
date: "2026-06-21"
---

## What Changed

- **DD-113 filed** — DD↔IB linkage is forward-only via `source_dd` (YAML list) on IB items; reverse view derived by query; `ib_items` retired.
- **63 IB files** — `source_dd` converted from scalar/comma-string to uniform YAML list (conforms to the schema's existing `array[string]` declaration).
- **4 reconciliations** — prior reverse `ib_items` claims folded non-lossily into `source_dd` (resolves the IB-147/IB-146 forward/reverse divergence).
- **81 DD files** — `ib_items` field removed from frontmatter.
- **`_schema.yaml`** — `source_dd` documented as single source of truth; `ib_items` removed with a do-not-reintroduce note.
- **Skills** — `/dd`, `/track`, `/governance-audit` no longer gather or emit `ib_items`; all point to the forward-only model.

## Query path (replaces the reverse field)

"Which IBs belong to DD-X?" → ripgrep `DD-X` across IB `source_dd` blocks (or an `/ib --dd DD-X` filter).
