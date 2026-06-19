---
title: "Consumer Abstractions Map"
type: "reference"
target_system:
  - "improvement-loop"
created: "2026-06-11"
updated: "2026-06-19"
author: "claude"
stage: "active"
tags:
  - "consumer-abstractions"
  - "rule-11"
  - "rule-12"
  - "demand-evidence"
  - "altitudes"
---

# Consumer Abstractions Map

Inventory of the abstractions the engine provides (or may provide) to its consumers — the audience archetypes 1–5 (Nick-builder, portfolio-presenter, practitioner-friend, builder-friend, employer-evaluator) and pilot-consumer projects (e.g., the sizing-engine). Each row carries demand evidence per IL rule 11 (abstractions must earn their keep). The map gates which abstractions the engine invests construction substrate in next; weak-evidence rows are future candidates, not committed scope.

The abstractions span two of the engine's three altitudes (DD-104). The **middle** altitude is per-artifact (one skill, one agent, one prompt); the **top** altitude is whole-system composition (the harness — the middle assessors composed). The top altitude consumes the middle: `/audit-artifacts` discovers per-artifact shapes and dispatches to the middle's `/assess-*` skills. There is no separate "MetaSystem" above the engine — the federation collapsed (DD-103); the engine is the sole system. The **bottom** altitude (research output — findings, watched-library reports, KB queries) is not a consumer build-target surface and is out of scope here.

## Demand-evidence framework

Per rule 11, every abstraction is rated against three criteria:

- **Concrete recurrence:** how many distinct consumer requests or build needs reference this abstraction (2–3+ minimum for strong evidence).
- **Multi-consumer benefit:** does more than one of the audience archetypes (1–5) measurably benefit?
- **Cost of absence:** is there an observable cost from *not* having the abstraction — duplication, ambiguity, re-litigation, missed audit gates?

Demand tiers:

- **Strong** — meets all three criteria. The engine commits §Composition + §Construction (per rule 12) and pairs `/assess-*`/`/audit-*` (audit) with `/design-*` (construction) skills.
- **Moderate** — meets two of three. The engine maintains §Composition for audit; defers §Construction until evidence promotes to strong.
- **Weak** — meets one criterion, or is aspirational / named-but-unobserved. Flagged as future candidate; no substrate work committed.

---

## Middle altitude — per-artifact abstractions

Concept docs in `operations/references/librarian/` (`skill.md`, `agent.md`, `prompt.md`, `memory.md`) are the configuration axes; `/assess-*` (audit) and `/design-*` (construction) skills wrap them.

### Strong demand — committed scope

| Abstraction | Concept doc | §Composition | §Construction | `/assess-*` | `/design-*` | Demand evidence |
|---|---|---|---|---|---|---|
| **Skill** | `librarian/skill.md` | ✅ | ✅ (session 107) | `/assess-skill` (active) | `/design-skill` (active) | Every engine skill is a SKILL.md; `/assess-skill` and `/design-skill` are both active. Multi-archetype: Nick-builder authors skills (1); practitioner-friend reuses (3); builder-friend asks how to author (4); employer-evaluator inspects (5). Cost of absence: every new skill would be authored from precedent + tacit knowledge, with no systematic Decision-sequence gate. |
| **Agent** | `librarian/agent.md` | ✅ (variant-aware) | ✅ (session 107) | `/assess-agent` (active) | `/design-agent` (active) | Every engine agent is an agent.md / CLAUDE.md / system prompt. `/assess-agent` and `/design-agent` are active. Multi-archetype: same as skill, plus higher blast radius (identity errors compound across every session). Cost of absence: agent design would have no systematic gate for variant selection, autonomy-envelope sizing, or HITL gating. |

### Moderate demand — audit only

| Abstraction | Concept doc | §Composition | §Construction | `/assess-*` | `/design-*` | Demand evidence |
|---|---|---|---|---|---|---|
| **Prompt** | `librarian/prompt.md` | ✅ | — (deferred per rule 11 + 12) | `/assess-prompt` (active; extends `/prompt-evaluator`) | — (not committed) | `/assess-prompt` is in use; demand for `/design-prompt` is moderate but not yet recurring. Workspace-root `/prompt-evaluator` + `/prompt-enhancer` already cover much of the design-time territory and overlap with the engine's authoring surface. Promotion to strong requires either (a) recurring `/design-prompt` consumer asks or (b) a decision to subsume the workspace-root prompt skills into the engine. Until promotion, §Construction is debt per rule 12 but not blocked. |

### Weak demand — aspirational adds (Nick-named, session 106)

| Abstraction | Concept doc | Demand evidence |
|---|---|---|
| **Governance** | — (none yet) | Nick named governance authoring (DDs, rules, constitutions, proposals) as a candidate for systematic Librarian coverage. Demand is currently one-off — DDs are bespoke; governance rules are sparse. Promote when 2–3 distinct "how should I structure a DD" or "how should I write a rule" consumer requests recur, or when `/translate-governance` needs Librarian backing. |
| **Security** | — (none yet) | Nick named security review surfaces (threat models, secrets handling, permission models, supply-chain checks) as an aspirational consumer-facing axis. Adjacent to G6 §Contract already, but no consumer-facing skill/concept-doc commitment yet. Promote when a top-altitude operation (`/audit-artifacts`, `/design-harness`) requires security as a first-class composable axis. |

### Weak demand — future candidates (not committed scope)

| Abstraction | Notes |
|---|---|
| **Memory** | Concept doc exists at `librarian/memory.md` (§Composition only). Demand currently single-consumer (Memongo). Promote when a second consumer's memory architecture surfaces. |
| **Hook** | Harness mechanism; not a standalone author-target today. Promote if Variant B agent design surfaces hook authoring as a recurring scoped task. |
| **Workflow** | Composition of skills. Out of scope until the pipeline itself becomes a consumer (durable workflow state is a recurring symptom in G3b but not yet a build target). |
| **Tool** | Tool design is covered as an aspect of agent design (Variant B) via G5; no demand for a standalone `/design-tool` operation. |
| **Eval-suite** | Aspirational. Building agent evaluation suites is a guide topic (`extracts/guides/building-agent-evaluation-suites.harvest-queue.md`) but no consumer-facing skill demand yet. |
| **Subagent** | Subagents are agents with an invocation contract — covered by `agent.md` (Variant B with delegation); no separate concept doc warranted until coordination contracts become a recurring authoring topic. |
| **Context structure** | Aspect of agent design (G2a §Contract); not a standalone author-target. Promote if context-files design recurs as a scoped authoring task distinct from agent design. |

---

## Top altitude — whole-system abstractions

The top altitude composes the middle. Its abstraction is the **harness** — the whole-system shape the engine audits and (eventually) constructs. Concept doc: `knowledge/reference/harness.md` (§Construction), with §Composition substrate maintained at `operations/references/librarian/harness.md`. Operations are `/audit-artifacts` (audit) and `/design-harness` (construction, future).

### Strong demand — committed scope

| Abstraction | Concept doc | §Composition | §Construction | `/audit-*` | `/design-*` | Demand evidence |
|---|---|---|---|---|---|---|
| **Harness** | `knowledge/reference/harness.md` | pointer → `librarian/harness.md` (audit-time substrate) | ✅ (session 116) | `/audit-artifacts` v1 **stable** (sessions 114–115) | `/design-harness` queued | (a) `/audit-artifacts` shipped and ran twice (smoke-test + IL second canonical run); (b) `/design-harness` is the rule-10 constructive peer queued for next build; (c) sizing-engine pilot consumer provides concrete non-self-test demand — two §Construction gaps named (deviation semantics for multi-system comparison; multi-surface composition with forecasting on a comparison harness). Multi-archetype: Nick-builder (1) authors harnesses; portfolio-presenter (2) cites them; builder-friend (4) inspects discovery contract; employer-evaluator (5) reads summary. Cost of absence: every new harness gets ad-hoc structure with no whole-system gate. |

### Weak demand — future candidates (not committed scope)

| Abstraction | Notes |
|---|---|
| **System** | "System" as a first-class authored abstraction (distinct from the harness it runs in) has no consumer-facing skill demand today. `/audit-artifacts` treats the audited folder as a system but the construction unit is the harness. Promote if a consumer-facing `/audit-system-of-systems` or cross-harness composition skill surfaces. |
| **Composition-layer** | The composition layer (whole-system operations composing per-artifact operations) is the *pattern* `/audit-artifacts` instantiates. It is substrate, not an authored artifact. Promote if a second composition-layer skill surfaces and the layering pattern itself recurs as an authoring target. |
| **Multi-harness orchestration** | Surface area for orchestrating multiple harnesses with shared state or substrate. Sizing-engine pilot may surface this (forecasting + comparison as two harnesses). Promote if a pilot demands a standalone orchestration abstraction beyond `/design-harness`. |

---

## Altitude relationship (top ↔ middle)

| Altitude | Abstractions | Operations |
|---|---|---|
| Top — whole-system | harness | `/audit-artifacts`, `/design-harness` (queued) |
| Middle — per-artifact | skill, agent, prompt | `/assess-*`, `/design-*` |

When `/audit-artifacts` discovers a SKILL.md, it dispatches to the middle's `/assess-skill`. When `/design-harness` (queued) drafts a new harness that ships a skill, it will dispatch to `/design-skill` for the skill draft. The top composes; the middle provides the per-artifact intelligence. Rule 12 (audit/design symmetry) applies at both altitudes: every operation the substrate composes against must have audit and design halves. See `knowledge/reference/harness.md` §"Rule-12 audit/design symmetry verification" for the harness-level walkthrough.

## Promotion rules

- **Weak → Moderate:** at least one concrete consumer request OR one build target that depends on the abstraction.
- **Moderate → Strong:** 2–3+ recurring consumer requests OR a committed build target (e.g., a roadmap entry naming the `/design-*` or `/audit-*` skill) AND multi-archetype benefit.
- **Demotion:** if a strong-demand row goes 3+ months without invocation, demote and revisit substrate maintenance.

Promotions are Owner-authored proposals (Proposal-First tier) — they affect what the engine commits to maintaining and what consumer surface area expands.

## What this map does NOT govern

- Research findings, watched-library reports, sources — bottom-altitude research output, not consumer abstractions.
- Cross-system skills (`/prompt-evaluator`, `/governance-audit`, `/session-handoff`) — those live at workspace-root `.claude/skills/` and are not engine build targets.

## Cross-references

- IL governance rule 11 (abstractions must earn their keep) and rule 12 (audit/design symmetry): `systems/improvement-loop/governance/agent-rules.md`.
- Per-artifact concept docs: `systems/improvement-loop/operations/references/librarian/`.
- Harness concept doc (§Construction): `systems/improvement-loop/knowledge/reference/harness.md`; §Composition substrate: `operations/references/librarian/harness.md`.
- Operation specs that compose against per-artifact abstractions: `librarian/audit.md`, `librarian/design.md`.
- Three altitudes: DD-104. Single-engine collapse: DD-103.
- Audience archetypes 1–5: workspace `PROGRESS.md`.
