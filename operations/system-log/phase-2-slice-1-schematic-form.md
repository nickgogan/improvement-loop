---
title: "Session 120 — Phase 2 Slice 1: schematic artifact form defined + 2 seeds"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Owner disposition)"
area: "knowledge/schematics"
change_type: "Design"
milestone: "Engine-collapse Phase 2"
rationale: "Defined the engine's top-altitude artifact form (the schematic — an evidence-grounded demand->configuration blueprint with a required evaluation/feedback layer) that DD-104 had named but deferred, and validated it with two seeds drawn from clusters the engine actually operates. Lean slice per Charter; drift-integration and demand-gated work deferred."
source_dd:
  - "DD-104"
  - "DD-107"
timestamp: "2026-06-18"
session: 120
tags:
  - "system-log"
  - "schematic"
  - "phase-2"
---

## Session Scope

Phase 2 Slice 1 of the engine collapse. After the post-Phase-1 cleanup sweep (memories,
`target_system` vocab, guide reframe, priority queue) landed earlier in the session, Nick
greenlit Phase 2 and chose the **lean** scope: define the schematic form, seed it, codify it —
defer the rest. Plan mode → approved plan → executed in two atomic commits.

## What Changed

- **The schematic form (Commit 1, `d8af4dc`).** `_schema.yaml` registers `schematic` (type CV),
  `system-design` (category CV), and schematic-only fields `altitude` / `maturity` /
  `grounded_in` / `composed_of`. New `knowledge/schematics/_index.md` (Dataview catalog) and
  `knowledge/templates/schematic-template.md` (the form contract: Demand → Configuration
  [capability+memory core → coordination → autonomy 5-level → deployment surface] → Evaluation &
  feedback [required] → Grounding & composition → Risk & maturity). **DD-107** codifies the form
  and the curated-not-extracted boundary (schematics are not wired into the Form Router).
- **Two seed schematics (Commit 2).** `research-scanning-agent` (middle altitude — the engine's
  own research-loop) and `codebase-audit-workcell` (top altitude — `/audit-system`'s multi-agent
  fan-out). Both grounded in real findings (11 `grounded_in` links, all resolve).

## Key Decisions

1. **Lean slice over full Phase 2** (Nick-gated) — Charter "ship minimum viable." Deferred:
   `/detect-drift` extension (next slice, once schematics exist to drift), the execution-surface
   Librarian axis (weak demand per consumer-abstractions-map — Rule 11), and Builder-mode
   demand→schematic matching (needs a populated library first).
2. **Curated, not pipeline-extracted** (DD-107) — schematics capture recurring clusters, so they
   are deliberately out of scope for `/identify-artifacts` / `/extract-artifacts`.
3. **Seeds = engine-internal clusters** (Nick-gated) — research-loop and `/audit-system`, chosen
   because the engine operates them, so grounding and eval/feedback layers are real, not speculative.

## Artifacts Produced

| # | Type | Path |
|---|------|------|
| 1 | schema | `_schema.yaml` (schematic type + fields) |
| 2 | governance | `knowledge/schematics/_index.md` |
| 3 | template | `knowledge/templates/schematic-template.md` |
| 4 | DD | `project-management/design-decisions/DD-107.md` |
| 5 | schematic | `knowledge/schematics/research-scanning-agent.md` |
| 6 | schematic | `knowledge/schematics/codebase-audit-workcell.md` |

## Verification

Schema CVs present; both seeds carry all required sections incl. non-empty Evaluation & feedback;
all 11 `grounded_in` stems resolve to real findings; `composed_of` skills exist; Dataview query
scoped correctly. Branch `engine-collapse-phase-1` (unmerged — Nick's call).
