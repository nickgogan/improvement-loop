---
name: Progressive/Tiered Context Loading Is Converging
summary: Four repos independently implement progressive context loading — loading minimal context first, expanding on demand. BMAD (L1/L2/L3), OpenViking (L0/L1/L2), DeerFlow (skill descriptions→full SKILL.md),
  Beads (SKILL.md→14 resource files). Strongest convergent signal in the registry.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: tiered-context-injection-over-monolithic-files.md
  rel: extends
- file: three-layer-context-chain-loading.md
  rel: same-problem
- file: three-tier-progressive-context-loading.md
  rel: extends
- file: progressive-skill-loading.md
  rel: extends
- file: gpt-54-tool-search-deferred-tool-loading.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: context-rot-attention-budget-depletion.md
  rel: same-problem
- file: document-sharding-for-context-efficiency.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---

## What It Is

A cross-repo convergence observation: four unrelated repos independently implement the same principle — load minimal context first, expand on demand with multiple resolution levels. Implementations differ but the pattern is identical:
- **BMAD**: L1 skill metadata (~100 tokens) → L2 skill body on activation → L3 step files just-in-time
- **OpenViking**: L0 abstract (~100 tokens) → L1 overview (~2k tokens) → L2 full content
- **DeerFlow**: Skill name+description at boot → full SKILL.md via `read_file` on demand
- **Beads**: SKILL.md thin entry point → 14 resource files fetched as needed

Combined with existing findings on tiered injection, chain-loading, and deferred tool loading, this pattern now has **6+ independent implementations** across the registry.

## Why It Matters

Convergent independent implementation is the strongest evidence that a pattern works. When four different orgs (with no shared ancestry) arrive at the same design principle, it's likely a genuine best practice rather than trend-following. This pattern directly addresses the fundamental context engineering problem: full context is too expensive, no context is too blind, and progressive loading threads the needle.

## Why People Are Using It

Cross-repo observation across 14 analyzed repos — see [[cross-repo-comparison]] for structural details. Observed independently in [BMAD Method](https://github.com/bmad-method/BMAD-METHOD), [OpenViking](https://github.com/volcengine/OpenViking), [DeerFlow](https://github.com/bytedance/deer-flow), and [Beads](https://github.com/gastownhall/beads). MetaSystem's `_index.md` files and skill description tables function as a partial implementation.

## Potential Alternatives

- Bulk loading (load everything upfront — simple but wasteful)
- Binary load/skip (either full file or nothing)
- RAG-only (vector search without tier structure)

## Potential Improvements

Standardize tier labels (L0/L1/L2) across MetaSystem. Generate L0 abstracts automatically for all context files. Apply to `_index.md` files — they already function as L0/L1 but without formal tier semantics.

## Potential Failure Modes

- Additional round-trips per tier add latency
- Tier generation quality depends on summarization
- Stale lower-tier representations if content changes
