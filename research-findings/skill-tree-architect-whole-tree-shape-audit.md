---
name: 'Skill-Tree Architect — Whole-Tree Shape Audit as a Distinct Altitude from Per-Skill Optimization'
summary: 'One tool in the context-hub system (anonymized private repo) reasons about the ENTIRE skill tree rather than any one skill: it audits description-cap violations, hub balance (over-stuffed or too-thin hubs), and cross-hub placement (spokes that semantically belong under a different hub), detects clusters of ≥8 standalone siblings that should become a new hub, and decides when to split a hub, spawn a family, or relocate a spoke. It orchestrates existing build/fix scripts rather than reimplementing them, and the meta-tools themselves sit on an exclude list so the tooling never tries to reorganize its own operators. Division of labor: the per-skill optimizer fixes one skill''s content and edges; the architect rebalances the forest.'
implementation_notes: 'Independent corroboration of the engine''s three-altitude architecture (DD-104): per-artifact assess/design in the middle, whole-system composition on top. The architect is precisely what /audit-artifacts v1 ships without — its whole-system invariants slot is deliberately empty pending recurrence evidence (rule 11), and this finding supplies the first concrete production catalog of what whole-tree invariants look like: always-on description budget totals, family balance (over-stuffed/too-thin groupings), cross-placement (artifact filed under the wrong family), and consolidation candidates (≥N unclustered siblings). If the engine''s asset catalog adopts any taxonomy, these four checks are the maintenance layer that keeps it from rotting — and they are countable, so they fit the engine''s deterministic-enforcement direction (audit-placement.mjs / detect-candidates.mjs are plain scripts, with the agent only deciding what to DO about flags). The orchestrates-never-reimplements rule and the exclude-list for meta-tools are both directly transferable design details.'
category: Governance
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: hub-and-spoke-two-tier-skill-taxonomy.md
  rel: extends
- file: convergence-loop-optimizer-family-contract.md
  rel: same-problem
- file: deterministic-doc-audit-battery.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
tags:
- whole-tree-audit
- taxonomy-maintenance
- altitude-separation
- rebalancing
---

# Skill-Tree Architect — Whole-Tree Shape Audit as a Distinct Altitude

## What It Is

The only tool in the system that reasons about the **entire** skill tree rather than one
skill. It orchestrates (never reimplements) a small deterministic toolchain:

- **`audit-placement.mjs`** — scans every skill for description-cap violations (the
  1000/1536 two-tier caps), hub balance (hubs that are over-stuffed or too thin), and
  **cross-hub placement** (a spoke that semantically belongs under a different hub).
- **`detect-candidates.mjs`** — finds clusters of ≥8 homeless/standalone sibling skills
  that should become a new hub.

On those signals it decides when to **split a hub, spawn a new family, or relocate a
spoke**, then drives the existing build/fix scripts (`build.mjs`, `fix-crosshub.mjs`,
`referents.mjs`) to execute the reshape. The architect and the explorer are themselves on
`exclude-list.mjs` so the hubbing tooling never tries to hub its own operators.

**Division of labor:** the per-skill optimizer fixes *one* skill's content and seeds
*its* deferral edges; the architect rebalances the *forest* and fixes *cross-hub*
placement.

## Why It Matters

Plain English: a well-organized library of assets rots even when every individual asset
is good — families overgrow, new assets get filed under the wrong family, and standalone
strays accumulate until the index bloats. No amount of per-asset auditing catches this,
because the defects live *between* assets, not inside them. Treating whole-tree shape as
its own audit altitude, with its own tool and its own (countable) invariants, is the
maintenance contract that keeps a taxonomy honest as it scales.

The worked example is instructive: a bloated index audit flags six over-cap descriptions
(two High), one hub grown to 31 spokes (split candidate), one spoke under the wrong hub,
and nine standalone observability skills that should become a hub — four different defect
classes, none visible from inside any single skill.

## How It Works

- **Detection is scripted; judgment is scoped.** The two audit scripts produce flags
  deterministically; the architect's LLM-shaped work is only deciding what reshape to
  perform and sequencing the existing scripts to do it.
- **Reshapes end with edge repair.** Every relocation/split/spawn runs
  `referents.mjs --repair` afterward so deferral edges (`SKIP:` targets,
  `related_skills:`) never dangle.
- **Durability is a separate step.** A tree reshape touches the authoring tree only; it
  becomes durable when affected skills are re-persisted and the canonical pack is
  regenerated. A reshape that is never synced exists only on one laptop.
- **Self-exclusion.** The exclude list is a small but load-bearing guard: the reorganizer
  must not be a candidate for reorganization mid-run.

## How It Could Fail

- **Semantic placement judgment.** "Belongs under a different hub" is a model call
  wrapped in a script's flag; wrong relocations are strictly worse than misplacement
  (they invalidate learned habits and edges), which is why the reshape is driven, gated,
  and edge-repaired rather than auto-applied.
- **Threshold gaming.** Splitting at fixed thresholds (31 spokes, ≥8 candidates) without
  domain judgment can shear a coherent family into arbitrary halves.
