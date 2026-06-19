---
title: "MetaSystem Capability Roadmap"
id: "meta-system-capability-roadmap"
type: "planning"
category: "roadmap"
target_system:
  - "improvement-loop"
stage: "accepted"
created: "2026-06-12"
updated: "2026-06-12"
author: "owner"
source_dd: []
tags:
  - "roadmap"
  - "meta-system"
  - "capabilities"
  - "step-g"
aliases:
  - "MetaSystem roadmap"
---

# MetaSystem Capability Roadmap

The MetaSystem-side analog of the workspace-level cross-system roadmap in `PROGRESS.md`. This document scopes the **step-G** build targets — the MetaSystem-owned capabilities composing IL substrate.

**Status:** Accepted (session 113). All five acceptance criteria ruled; gates resolved below. Step-G build begins with `/audit-artifacts` research/design phase.

---

## Why MetaSystem owns these capabilities

Per the cross-system framing: IL is the research engine + advisory layer over agentic *abstractions* (skill, agent, prompt). MetaSystem is the builder of *whole systems* — it consumes IL's audit and design surfaces and composes them into whole-system operations.

The two graduated systems own different scopes (per workspace `PROGRESS.md`):
- IL owns user-facing capabilities (1) audit artifact, (4) ask the KB, (5) compare watched repos.
- MetaSystem owns user-facing capabilities (2) audit whole system, (3) design harness.

Step F instantiated the MetaSystem Owner (IB-167). Step G builds (2) and (3).

---

## Target capabilities

### `/audit-artifacts`

**Plain English:** "Point this at a folder; tell me whether the agentic system inside it is well-formed."

**Composition shape:** A workspace-level skill that takes a local path as input, discovers what abstractions live there (skills under `.claude/skills/`, agents under `agents/` or `.claude/agents/`, prompts in known locations, etc.), and dispatches each to IL's `/assess-*` family. Aggregates per-artifact verdicts into a whole-system audit report.

**IL substrate consumed:**
- `/assess-skill` — audit SKILL.md files
- `/assess-agent` — audit agent.md / CLAUDE.md / system-prompt-style artifacts (variant-aware)
- `/assess-prompt` — audit standalone prompts
- KB Read-access for citation grounding

**Open design questions for step G:**
- Discovery contract: how does `/audit-artifacts` decide what to audit? Walks the local path looking for known shapes (`.claude/skills/*/SKILL.md`, `agents/*/agent.md`, etc.)? Or does it require an explicit manifest?
- Composition model: does it spawn IL `/assess-*` as subagents (rule 10 generator-assessor separation, inverted — here MetaSystem is the orchestrator, IL skills are the assessors), or invoke them inline?
- Output shape: per-artifact findings or whole-system score? Both?
- Whole-system invariants beyond per-artifact checks (cross-references, missing pairs, structural completeness) — does `/audit-artifacts` ADD checks IL `/assess-*` can't see, or is it purely composition?

### `/design-harness`

**Plain English:** "Walk me through designing a complete agentic harness — agents, skills, prompts, context, governance — and produce all the artifacts."

**Composition shape:** Interview-driven, multi-artifact output. Walks a harness design Decision sequence (broader than IL's per-artifact `design.md × {skill,agent}.md` compositions), produces multiple staged artifacts that together constitute a harness.

**IL substrate consumed:**
- `/design-skill` — draft SKILL.md from intent
- `/design-agent` — draft agent.md from intent (variant-aware)
- IL guides (G1, G3b, G5, G6, G8, G9, G10) for cross-cutting concerns
- KB Read-access for citation grounding
- Possibly an unwritten `/design-prompt` if standalone prompts are part of the harness output

**Open design questions for step G:**
- Decision sequence: what does the harness-level Construction sequence look like? Per finding `harness.md` flagged for §Construction backfill (workspace PROGRESS.md priority queue item 2), this substrate is partial.
- Multi-artifact orchestration: does `/design-harness` invoke `/design-skill` and `/design-agent` per artifact, or compose their templates inline?
- Staging: where do harness drafts land? `extracts/harnesses/` (new staging area)?
- Audit hand-off: per rule 10, the constructive skill delegates its quality check to an assessor peer in fresh context. The assessor here is `/audit-artifacts` — does `/design-harness` invoke `/audit-artifacts` against its own staged output before returning?

---

## Dependencies

### Hard prerequisites (must exist before step G can complete)

| Dependency | Current state | Owner |
|------------|---------------|-------|
| IL `/assess-skill`, `/assess-agent`, `/assess-prompt` | ✅ Active (step A) | IL |
| IL `/design-skill`, `/design-agent` | ✅ Active (step D) | IL |
| IL KB substrate (findings, guides, watched-libraries) | ✅ Active | IL |
| IL Librarian agent (subagent invocability) | ✅ Active | IL |
| MetaSystem Owner agent | ✅ Active (step F, session 112) | MetaSystem |
| `harness.md` §Construction substrate | ⚠️ Flagged for backfill (workspace PROGRESS.md priority queue item 2) | IL |

### Soft prerequisites (would improve step G but not block)

- IL Owner skill family parameterized for cross-system use (currently IL-hardcoded; deferred IB items filed session 112)
- Workspace-root mirror or symlink decision for engine subagents (pending empirical harness-discovery test)
- A documented harness-level §Construction Decision sequence (could be drafted during step G if substrate emerges, or pre-built if Nick gates item 2)

### Out of scope for this roadmap

- Building `/audit-artifacts` or `/design-harness` themselves — those are step G.
- Authoring MetaSystem-specific concept docs (e.g., `harness.md` §Construction backfill). Rule 11 — defer until consumer demand justifies; step G itself is the test.
- Promoting IL rules 10 and 11 to MetaSystem constitution — Nick deferred until a second cross-system instance surfaces.
- Touching the cross-system roadmap structure itself (workspace `PROGRESS.md`).
- Building vault-curator or knowledge-indexer agents (IB-142) — separate sequence after step G stabilizes.

---

## Sequencing assumptions (not committed)

Surfaced for Nick's gate; do not act on these until step G is approved.

1. **`/audit-artifacts` before `/design-harness`** — symmetry argument from IL rule 10: the constructive skill delegates its quality check to the assessor peer. If `/design-harness` is to delegate to `/audit-artifacts` per rule 10, the assessor must exist first.
2. **Harness §Construction substrate before `/design-harness`** — if Nick gates item 2 of the workspace priority queue (backfill `harness.md` §Construction from session 109 findings), it lands as substrate before `/design-harness` consumes it. If Nick defers item 2, step G builds `/design-harness` on partial substrate and surfaces gaps as evidence for backfill later.
3. **Discovery contract for `/audit-artifacts` written first** — what counts as an "auditable artifact in a local path" is the load-bearing decision for the skill; everything else follows.

These are working hypotheses, not commitments. Step G's planning conversation will revisit.

---

## Risks and open questions

- **Audit/design symmetry at the harness level.** IL rule 12 says concept docs carrying §Composition but not §Construction (or vice versa) are in debt. At the harness level, the analog would be: does `/audit-artifacts` (composition) without `/design-harness` (construction), or vice versa, leave the MetaSystem in debt? My read: yes, by rule 12's reasoning. Step G plans should build both, even if sequenced.
- **Multi-artifact staging story is unwritten.** IL's `extracts/` has per-form staging (`agents/`, `skills/`, `rules/`, `templates/`, `patterns/`). For a harness that bundles multiple forms, staging may need a new convention (e.g., `extracts/harnesses/{name}/` containing nested per-form staged artifacts). Decide during step G.
- **`/audit-artifacts` may demand whole-system invariants IL `/assess-*` can't see.** Cross-reference integrity, missing-pair detection, fractal-pattern compliance per DD-52, governance-source freshness — these are MetaSystem-shaped checks. `/audit-artifacts` may end up authoring its own check set rather than purely composing IL skills. Rule 11 applies: build only what evidence demands.
- **Audience archetypes affect output shape.** Archetypes 1–5 (Nick-builder, portfolio-presenter, practitioner-friend, builder-friend, employer-evaluator) consume audit/design output differently. `/audit-artifacts`'s report shape and `/design-harness`'s artifact density both depend on which archetypes are primary. Decide before step G.

---

## Acceptance criteria for this roadmap (gate to step G)

**Resolved session 113:**

1. ✅ `/audit-artifacts` and `/design-harness` confirmed as step-G targets — no scope changes.
2. ✅ Open design questions gated:
   - **`/audit-artifacts` discovery contract:** auto-detect by known shapes on input; the manifest is part of the *output* (structural inventory deliverable alongside per-artifact findings and whole-system summary). Re-audit pattern: diff new manifest against old, surface drift as first-class signal.
   - **`/audit-artifacts` composition model:** spawn IL `/assess-*` skills in fresh subagent context (rule-10 inverted — MetaSystem orchestrates; IL Librarian acts as assessor subagent invoking the relevant skill).
   - **`/audit-artifacts` output shape:** three artifacts — manifest, per-artifact findings, whole-system summary.
   - **`/audit-artifacts` whole-system invariants:** start as pure composition; add MetaSystem-specific checks only as recurring evidence demands (rule 11).
   - **`/design-harness` design questions:** gated when that build begins (session 115+); not pre-gated.
3. ✅ Soft-prereq decisions:
   - **Harness `§Construction` backfill:** backfill before `/design-harness` build (priority queue item 3 elevated to side-quest preceding `/design-harness`). `/audit-artifacts` may proceed in parallel — does not depend on this.
   - **IL Owner skill parameterization (IB-168):** keep deferred; trigger on recurring evidence (rule 11 compliant).
   - **Workspace-root mirror decision:** resolved sub-task 1 — symlink at `.claude/agents/meta-system-owner.md → ../../systems/meta-system/.claude/agents/owner.md`; harness empirically follows symlink and dedupes when both reachable via walk-up.
4. ✅ Audience archetypes: default 1–5 (Nick-builder, portfolio-presenter, practitioner-friend, builder-friend, employer-evaluator). Archetypes 6 (org-scale) and 7 (machine-callable) explicitly out of scope.
5. ✅ Sequencing approved as drafted:
   - `/audit-artifacts` before `/design-harness` (rule-10 symmetry: constructive skill delegates to assessor peer).
   - Discovery contract (here: input-side auto-detect + output-side manifest) is the load-bearing first decision for `/audit-artifacts`.
   - Harness `§Construction` backfill lands before `/design-harness` build.
