---
notion_id: null
log_entry: "Tier 1 Anthropic blog extraction: 15 new findings, 7 updated"
actor: "Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "Processed all 6 Tier 1 Anthropic engineering posts through /research-loop. Created 15 new findings (4 at P1, 7 at P2, 2 at P3, 2 Already Adopted), updated 7 existing findings with Anthropic as additional source, created 6 source entries, and updated Anthropic authority to 8 sources."
source_dd: null
target_system: "improvement-loop"
date: "2026-04-09"
---

## What Changed

- 6 source entries created and completed (all status: Done, relevance: High)
- 15 new findings created across 5 categories:
  - **Evaluation (5):** pass@k vs pass^k, capability vs regression lifecycle, eval-driven tool iteration, balanced positive/negative sets, (eval-driven tool iteration loop)
  - **Tool Integration (3):** search-over-list design, non-deterministic tool contract, poka-yoke error-proofing
  - **Context Engineering (3):** context rot/attention budget, hybrid upfront+JIT architecture, response format enum
  - **Agent Design (3):** harness simplification, framework abstraction tax, ground-truth feedback loops
  - **Orchestration (2):** sprint contract negotiation, cost concentration in generation
- 7 existing findings updated with Anthropic source: builder-validator chain, eval-driven development, explore-plan-implement-commit, agent self-reporting unreliability, context pollution, IDE-first hooks, skills 2.0
- Anthropic authority updated: 8 sources, expanded specialties (tools, evaluation, orchestration, claude-code)

## P1 Findings (Implement Now)

1. **pass@k vs pass^k** — MetaSystem verification loops should choose which metric applies
2. **Context Rot** — Validates aggressive context hygiene; every unnecessary token degrades performance
3. **Poka-Yoke Tool Interfaces** — Audit tool parameters for structural error prevention
4. **Ground-Truth Feedback Loops** — Validates test-before-build and verification-first principles

## Affected Items

- `systems/improvement-loop/research-sources/anthropic-*.md` — 6 new source entries
- `systems/improvement-loop/research-findings/` — 15 new, 7 updated
- `systems/improvement-loop/research-authorities/anthropic.md` — updated
