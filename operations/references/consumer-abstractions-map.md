---
title: "Consumer Abstractions Map"
type: "reference"
target_system:
  - "improvement-loop"
created: "2026-06-11"
updated: "2026-06-11"
author: "claude"
stage: "active"
tags:
  - "consumer-abstractions"
  - "rule-11"
  - "demand-evidence"
---

# Consumer Abstractions Map

Inventory of the abstractions IL provides (or may provide) to its consumers — MetaSystem (the primary downstream consumer), Nick-as-builder, and other archetypes within the audience commitment (1–5 per workspace `PROGRESS.md`). Each row carries demand evidence per IL rule 11 (abstractions must earn their keep). The map gates which abstractions IL invests construction substrate in next; weak-evidence rows are future candidates, not committed scope.

## What this map governs

- **Concept docs** in `operations/references/librarian/` — substrate that Librarian operations (`audit`, `design`) compose against.
- **`/assess-*` and `/design-*` skill pairs** — consumer-facing skills that wrap the operations.
- **Eventual extraction targets** — what `/extract-artifacts` may stage for deployment to MetaSystem or another consumer.

Research output (findings, watched-library reports, KB queries) is not in scope here — that's the research pipeline, not the build-target surface.

## Demand-evidence framework

Per rule 11, every abstraction is rated against three criteria:

- **Concrete recurrence:** how many distinct consumer requests or build needs reference this abstraction (2–3+ minimum for strong evidence).
- **Multi-consumer benefit:** does more than one of the audience archetypes (1–5) measurably benefit?
- **Cost of absence:** is there an observable cost from *not* having the abstraction — duplication, ambiguity, re-litigation, missed audit gates?

Demand tiers:

- **Strong** — meets all three criteria. IL commits §Composition + §Construction (per rule 12) and pairs `/assess-*` + `/design-*` skills.
- **Moderate** — meets two of three. IL maintains §Composition for audit; defers §Construction until evidence promotes to strong.
- **Weak** — meets one criterion, or is aspirational / named-but-unobserved. Flagged as future candidate; no substrate work committed.

## Inventory

### Strong demand — committed scope

| Abstraction | Concept doc | §Composition | §Construction | `/assess-*` | `/design-*` | Demand evidence |
|---|---|---|---|---|---|---|
| **Skill** | `librarian/skill.md` | ✅ | ✅ (session 107) | `/assess-skill` (active) | `/design-skill` (planned — cross-system roadmap step D) | Every IL skill is a SKILL.md; `/assess-skill` is active; `/design-skill` is the upcoming consumer-facing build target. Multi-archetype: Nick-builder authors skills (1); practitioner-friend reuses (3); builder-friend asks how to author (4); employer-evaluator inspects (5). Cost of absence: every new skill is currently authored from precedent + tacit knowledge, with no systematic Decision-sequence gate. |
| **Agent** | `librarian/agent.md` | ✅ (variant-aware) | ✅ (session 107) | `/assess-agent` (active) | `/design-agent` (planned — cross-system roadmap step D) | Every IL agent + every upcoming MetaSystem agent is an agent.md / CLAUDE.md / system prompt. `/assess-agent` is active. Multi-archetype: same as skill, plus higher blast radius (identity errors compound across every session). Cost of absence: agent design currently has no systematic gate for variant selection, autonomy-envelope sizing, or HITL gating. |

### Moderate demand — audit only

| Abstraction | Concept doc | §Composition | §Construction | `/assess-*` | `/design-*` | Demand evidence |
|---|---|---|---|---|---|---|
| **Prompt** | `librarian/prompt.md` | ✅ | — (deferred per rule 11 + 12) | `/assess-prompt` (active; extends `/prompt-evaluator`) | — (not committed) | `/assess-prompt` is in use; demand for `/design-prompt` is moderate but not yet recurring. Workspace-root `/prompt-evaluator` + `/prompt-enhancer` already cover much of the design-time territory and overlap with IL's authoring surface. Promotion to strong requires either (a) recurring `/design-prompt` consumer asks or (b) a decision to subsume the workspace-root prompt skills into IL. Until promotion, §Construction is debt per rule 12 but not blocked. |

### Weak demand — aspirational adds (Nick-named, session 106)

| Abstraction | Concept doc | Demand evidence |
|---|---|---|
| **Governance** | — (none yet) | Nick named governance authoring (DDs, rules, constitutions, proposals) as a candidate for systematic Librarian coverage. Demand is currently one-off — DDs are bespoke; governance rules are sparse (12 rules in `agent-rules.md`). Promote when 2–3 distinct "how should I structure a DD" or "how should I write a rule" consumer requests recur, or when MetaSystem's `/translate-governance` analog needs Librarian backing. |
| **Security** | — (none yet) | Nick named security review surfaces (threat models, secrets handling, permission models, supply-chain checks) as an aspirational consumer-facing axis. Adjacent to G6 §Contract already, but no consumer-facing skill/concept-doc commitment yet. Promote when MetaSystem builds `/audit-artifacts` or `/design-harness` that requires security as a first-class composable axis (cross-system roadmap step G). |

### Weak demand — future candidates (not committed scope)

| Abstraction | Notes |
|---|---|
| **Memory** | Concept doc exists at `librarian/memory.md` (§Composition only). Demand currently single-consumer (Memongo). Promote when a second consumer's memory architecture surfaces. |
| **Hook** | Harness mechanism; not a standalone author-target today. Promote if Variant B agent design surfaces hook authoring as a recurring scoped task. |
| **Workflow** | Composition of skills. Out of scope until the IL pipeline itself becomes a consumer (durable workflow state is a recurring symptom in G3b but not yet a build target). |
| **Tool** | Tool design is covered as an aspect of agent design (Variant B) via G5; no demand for a standalone `/design-tool` operation. |
| **Eval-suite** | Aspirational. Building agent evaluation suites is a guide topic (`extracts/guides/building-agent-evaluation-suites.harvest-queue.md`) but no consumer-facing skill demand yet. |
| **Subagent** | Subagents are agents with an invocation contract — covered by `agent.md` (Variant B with delegation); no separate concept doc warranted until coordination contracts become a recurring authoring topic. |
| **Context structure** | Aspect of agent design (G2a §Contract); not a standalone author-target. Promote if context-files design recurs as a scoped authoring task distinct from agent design. |

## Promotion rules

- **Weak → Moderate:** at least one concrete consumer request OR one build target that depends on the abstraction.
- **Moderate → Strong:** 2–3+ recurring consumer requests OR a committed build target (e.g., a roadmap step naming the `/design-*` skill) AND multi-archetype benefit.
- **Demotion:** if a strong-demand row goes 3+ months without invocation, demote to moderate and revisit substrate maintenance.

Promotions are Owner-authored proposals (Proposal-First tier) — they affect what IL commits to maintaining and what consumer surface area expands.

## What this map does NOT govern

- Research findings, watched-library reports, sources — research output, not consumer abstractions.
- MetaSystem-side abstractions (harness, system-level audit). MetaSystem maintains its own equivalent map for its consumer surface (post-step-F per cross-system roadmap).
- Cross-system skills (`/prompt-evaluator`, `/governance-audit`, `/session-handoff`) — those live at workspace-root `.claude/skills/` and are not IL build targets.

## Cross-references

- IL governance rule 11 (abstractions must earn their keep) and rule 12 (audit/design symmetry): `systems/improvement-loop/governance/agent-rules.md`.
- Concept docs: `systems/improvement-loop/operations/references/librarian/`.
- Operation specs that compose against these abstractions: `librarian/audit.md`, `librarian/design.md`.
- Cross-system roadmap (steps D, E, F, G reference the build targets in this map): workspace `PROGRESS.md`.
- Audience archetypes 1–5 (Nick-builder, portfolio-presenter, practitioner-friend, builder-friend, employer-evaluator): workspace `PROGRESS.md` § Cross-System Roadmap.
