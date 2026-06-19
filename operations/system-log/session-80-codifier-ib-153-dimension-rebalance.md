---
title: "Session 80 — Codifier: IB-153 dimension rebalance (Memory Architecture orphan retirement + Dim 2-5 name alignment)"
type: "system-log"
target_system:
  - "improvement-loop"
actor: "Claude (Codifier disposition)"
area: "research-findings / dimensions / guide-routing-table / dimension-rebalance"
change_type: "Update"
milestone: null
rationale: "IB-153 closure. The orphan `category: Memory Architecture` (41 findings, not registered as a top-level dimension) was retired by the session-63 introduction of Sub-dim 1.B (Memory Isolation and Topology) under Dimension 1 (Context Engineering); IB-153 carried the cleanup work. Executed `/dimension-rebalance` per its own procedure with human-gated proposal. Default Option A (all 41 → Context Engineering) was approved with 8 borderline re-routes to Agentic Systems (Dim 11) where the primary subject was vault-as-OS / personal-knowledge-store / org-memory-system pattern rather than memory mechanics. Bonus dimension-name alignment included on Nick's request: Dim 2-5 taxonomy block + section headers in research-dimensions.md, plus the Dimensions column in guide-routing-table.md, were aligned to the canonical long forms used in 100% of findings (Model→Model Selection, Prompt→Prompt Craft, Tools→Tool Integration, Intent→Intent Engineering). G7 row's Dimensions field stripped of 'Memory Architecture' per IB-153 acceptance. Two stale prose references to 'Memory Architecture dimension' (in librarian/second-brain.md and one finding's implementation_notes) updated to point at Sub-dim 1.A/1.B and Context Engineering. Final distribution: Context Engineering 132 (was 99, +33), Agentic Systems 29 (was 21, +8), Memory Architecture 0 (was 41). One atomic commit."
source_dd: null
date: "2026-04-27"
session: 80
tags:
  - "system-log"
  - "codifier"
  - "dimension-rebalance"
  - "ib-153"
  - "research-dimensions"
  - "guide-routing-table"
  - "memory-architecture-retirement"
  - "name-alignment"
---

# Session 80 — Codifier: IB-153 dimension rebalance

## Trigger

IB-153 was queued (session 63) as the cleanup follow-up to Sub-dim 1.B's introduction. Nick directed it as this session's work in lieu of the handoff-anticipated harvest-queue rulings batch. Per the IB acceptance:

1. Rebalance report produced (human gate).
2. Nick-approved changes applied to findings.
3. `guide-routing-table.md` G7 Dimensions field updated to drop "Memory Architecture".

Nick added one in-session ask: "address the Category-name variants issue this session as well" — the dimension-name short/long mismatch surfaced in the rebalance report's "Additional Drift" section.

## Rebalance report (Step 3)

Pre-rebalance distribution showed `Memory Architecture` orphaned at 41 findings (25 unquoted + 16 quoted YAML). 33 proposed to default Option A (Context Engineering); 8 borderlines flagged for Nick's review with Agentic Systems as the alternative.

**Borderlines (all approved for Agentic Systems):**

| Finding | Decided category | Why Agentic Systems wins |
|---|---|---|
| `flat-root-vault-with-property-based-organization` | Agentic Systems | Vault folder structure + YAML properties — directly matches Dim 11 "File-based personal OS architecture (folder structure, index files...)". |
| `karpathy-llm-knowledge-base-obsidian-rag` | Agentic Systems | Karpathy's Obsidian vault-as-OS pattern with ingest→compile→query→enhance cycle — canonical Dim 11. |
| `scale-threshold-heuristic-obsidian-vs-rag` | Agentic Systems | Decision framework for when to scale a vault-as-OS — operational system choice belongs in Dim 11. |
| `signal-capture-as-byproduct-of-work` | Agentic Systems | About *organizational behavior* / knowledge-system economics, not memory mechanics. |
| `composable-templates-for-lazy-capture` | Agentic Systems | Note-template design for personal vault — Dim 11 PKM pattern. |
| `compounding-knowledge-loop-internal-data` | Agentic Systems | Self-evolving wiki from session conversations — personal-OS compounding pattern. |
| `open-brain-personal-knowledge-store-pattern` | Agentic Systems | Already cross-referenced from G7 routing table as a representative Agentic Systems finding; consistent with that placement. |
| `org-world-model-three-architecture-patterns` | Agentic Systems | Three architectures for *organizational* world models — read as org-system pattern more than memory architecture. |

## Additional drift surfaced (folded in this session per Nick)

`research-dimensions.md` taxonomy block (lines 33-46) and section headers used short forms (Dim 2 "Model", Dim 3 "Prompt", Dim 4 "Tools", Dim 5 "Intent") while 100% of findings had self-canonicalized to long forms (Model Selection / Prompt Craft / Tool Integration / Intent Engineering). The lower-cost direction was to align taxonomy to findings (vs editing 100+ finding files). `guide-routing-table.md` Dimensions column had similar short/long inconsistency (G1 "Intent, Context", G3 "Model", G5 "Tools", G7 "Context", G8 "Prompt, Model") and was aligned to long forms in the same pass.

YAML quoting inconsistency on `category:` values (quoted vs unquoted across findings) was flagged in the report but left as-is — out of scope, no behavioral impact, and per-file style preserved during this rebalance.

## Surfaces touched

- **41 findings**: `category:` rewritten (Memory Architecture → Context Engineering ×33 / Agentic Systems ×8); `last_updated` bumped to 2026-04-27. Per-file YAML quoting style preserved.
- **`guide-routing-table.md`**: G7 row Dimensions "Context, Orchestration, Memory Architecture" → "Context Engineering, Orchestration"; G1/G3/G5/G8 rows aligned to long forms.
- **`research-dimensions.md`**: taxonomy block + 4 section headers updated; `last_updated` field bumped with rationale.
- **`librarian/second-brain.md`** L74: "Memory Architecture + Context Engineering + Intent dimensions" → "Context Engineering (Sub-dim 1.A decay, 1.B isolation) and adjacent to Intent Engineering".
- **`agentic-speculation-…`** finding `implementation_notes`: stale reference to "broader Memory Architecture dimension" → "broader Context Engineering dimension (Sub-dim 1.A/1.B)".
- **`IB-153.md`**: status `Queued` → `Done`; notes appended with execution summary.

## Final distribution (post-rebalance)

| Category | Count | Δ from pre |
|---|---:|---:|
| Context Engineering | 132 | +33 |
| Orchestration | 105 | 0 |
| Evaluation | 75 | 0 |
| Tool Integration | 68 | 0 |
| Governance | 53 | 0 |
| Agent Design | 47 | 0 |
| Prompt Craft | 38 | 0 |
| Agentic Systems | 29 | +8 |
| Intent Engineering | 18 | 0 |
| Sandboxing | 14 | 0 |
| Model Selection | 9 | 0 |
| **Memory Architecture** | **0** | **−41** |

## Acceptance check

- [x] Rebalance report produced (Step 3 inline output, human-gated).
- [x] Nick-approved changes applied (33 + 8 reclassifications + last_updated bump).
- [x] `guide-routing-table.md` G7 Dimensions field updated to drop "Memory Architecture".
- [x] Bonus: Dim 2-5 name alignment across research-dimensions.md + routing-table Dimensions column.
- [x] Bonus: 2 stale prose references to "Memory Architecture dimension" updated.
- [x] IB-153 status set to Done with execution summary in notes.

## Logged-for-future / not done

- **YAML category-quoting inconsistency** (quoted vs unquoted variants across the KB) — noted in the rebalance report's "Additional Drift" but left out of scope. No behavioral impact; would be a separate hygiene pass if Nick wants normalization.
- **Agentic Systems "below 5-finding threshold" note** in `guide-routing-table.md` line 97 is now stale (29 findings ≥ 5). Not in IB-153 scope; left for a future pass that re-evaluates whether G11 should be proposed.
- **Sub-dim 1.B graduation criteria**: with 8 explicit isolation/topology findings in the cluster (the 2 seeds + 6 of the borderlines absorbed there), 1.B is below the ≥10-finding graduation threshold but moving in that direction. Continue monitoring.
