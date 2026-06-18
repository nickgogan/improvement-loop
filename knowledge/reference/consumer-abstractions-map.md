---
title: "MetaSystem Consumer Abstractions Map"
type: "reference"
target_system:
  - "meta-system"
created: "2026-06-15"
updated: "2026-06-15"
author: "claude"
stage: "active"
tags:
  - "consumer-abstractions"
  - "rule-11"
  - "rule-12"
  - "harness"
  - "demand-evidence"
---

# MetaSystem Consumer Abstractions Map

Inventory of the abstractions **MetaSystem** maintains for its consumers — Nick-as-builder, pilot-consumer projects (e.g., the sizing-engine), and the audience archetypes 1–5 declared in the workspace `PROGRESS.md`. Each row carries demand evidence per IL rule 11 (abstractions must earn their keep). The map gates which abstractions MetaSystem invests construction substrate in next.

This is the parallel to IL's `systems/improvement-loop/operations/references/consumer-abstractions-map.md`. Where IL maintains per-artifact substrate (skill, agent, prompt), MetaSystem maintains whole-system substrate (harness) that composes over IL's per-artifact assessors and constructors.

## What this map governs

- **Concept docs** in `systems/improvement-loop/knowledge/reference/` — substrate that MetaSystem operations (`/audit-system`, `/design-harness`) compose against.
- **`/audit-*` and `/design-*` skill pairs at the harness level** — consumer-facing skills that wrap the operations.
- **The MetaSystem–IL split.** IL owns per-artifact `/assess-*` and `/design-*`; MetaSystem owns whole-system `/audit-system` and `/design-harness` that compose IL's assessors and constructors.

What this map does **not** govern: IL-owned abstractions (skill, agent, prompt) — those live in IL's map. Research output, knowledge vault stewardship, governance source docs — those are MetaSystem-internal but not consumer abstractions.

## Demand-evidence framework

Same framework as IL's map (rule 11). Three criteria per abstraction:

- **Concrete recurrence:** ≥2–3 distinct consumer requests or build needs reference this abstraction.
- **Multi-consumer benefit:** more than one archetype (1–5) measurably benefits.
- **Cost of absence:** observable cost from *not* having the abstraction.

Tiers:

- **Strong** — meets all three. MetaSystem commits §Construction + §Composition pointer; pairs `/audit-*` + `/design-*` skills.
- **Moderate** — meets two. §Composition only; defer §Construction.
- **Weak** — meets one or aspirational. Future candidate; no committed scope.

## Inventory

### Strong demand — committed scope

| Abstraction | Concept doc | §Composition | §Construction | `/audit-*` | `/design-*` | Demand evidence |
|---|---|---|---|---|---|---|
| **Harness** | `knowledge/reference/harness.md` (this commit) | pointer → IL `librarian/harness.md` (IL-owned audit-time substrate) | ✅ (this commit — session 116) | `/audit-system` v1 **stable** (sessions 114–115) | `/design-harness` queued (cross-system roadmap step G) | (a) `/audit-system` shipped and ran twice (MetaSystem self-audit + IL second canonical run); (b) `/design-harness` is the rule-10 constructive peer queued for next build; (c) sizing-engine pilot consumer (priority-queue item 5) provides concrete non-self-test demand — two specific §Construction gaps already named (deviation semantics for multi-system comparison; multi-surface composition with forecasting layered on a comparison harness). Multi-archetype: Nick-builder (1) authors harnesses; portfolio-presenter (2) cites them; builder-friend (4) inspects discovery contract; employer-evaluator (5) reads summary. Cost of absence: every new harness gets ad-hoc structure with no whole-system gate. |

### Moderate demand — audit only

_None at this commit._ Future candidates listed below are weak.

### Weak demand — future candidates (not committed scope)

| Abstraction | Notes |
|---|---|
| **System** | "System" as a first-class authored abstraction (distinct from the harness it runs in) has no consumer-facing skill demand today. `/audit-system` treats the audited folder as a system but the construction unit is the harness. Promote if a consumer-facing `/audit-system-of-systems` or cross-harness composition skill surfaces. |
| **Composition-layer** | The composition layer (whole-system operations composing IL per-artifact operations) is the *pattern* `/audit-system` instantiates. It is substrate, not an authored artifact. Promote if a second composition-layer skill surfaces and the layering pattern itself recurs as a authoring target. |
| **Multi-harness orchestration** | Surface area for orchestrating multiple harnesses with shared state or shared substrate. Sizing-engine pilot may surface this (forecasting + comparison as two harnesses). Promote if pilot demands a standalone orchestration abstraction beyond `/design-harness`. |

## Promotion rules

Same shape as IL's map:

- **Weak → Moderate:** at least one concrete consumer request OR one build target that depends on the abstraction.
- **Moderate → Strong:** 2–3+ recurring consumer requests OR a committed build target naming the `/design-*` or `/audit-*` skill AND multi-archetype benefit.
- **Demotion:** if a strong-demand row goes 3+ months without invocation, demote and revisit substrate maintenance.

Promotions are Owner-authored proposals (Proposal-First tier).

## The MetaSystem–IL split (for orientation)

| Layer | Maintained by | Abstractions | Operations |
|---|---|---|---|
| Per-artifact | IL | skill, agent, prompt | `/assess-*`, `/design-*` |
| Whole-system / harness | MetaSystem | harness | `/audit-system`, `/design-harness` (queued) |

When `/audit-system` discovers a SKILL.md, it dispatches to IL `/assess-skill`. When `/design-harness` (queued) drafts a new harness that ships a skill, it will dispatch to IL `/design-skill` for the skill draft. MetaSystem composes; IL provides the per-artifact intelligence.

Rule 12 (audit/design symmetry) applies at both layers: every harness operation IL substrate composes against must have audit and design halves. See `harness.md` §"Rule-12 audit/design symmetry verification" for the harness-level walkthrough.

## Cross-references

- IL consumer-abstractions-map (parallel map for per-artifact abstractions): `systems/improvement-loop/operations/references/consumer-abstractions-map.md`
- Harness concept doc (this commit): `systems/improvement-loop/knowledge/reference/harness.md`
- IL harness concept doc (§Composition substrate): `systems/improvement-loop/operations/references/librarian/harness.md`
- `/audit-system` SKILL.md: `systems/meta-system/.claude/skills/audit-system/SKILL.md`
- `/audit-system` design contract: `systems/meta-system/project-management/design-notes/2026-06-12-audit-system-design-contract.md`
- IL rules 10/11/12: `systems/improvement-loop/governance/agent-rules.md`
- Cross-system roadmap and audience archetypes 1–5: workspace `PROGRESS.md`
