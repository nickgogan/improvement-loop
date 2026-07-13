---
name: "Rules-Layer Collapse — Monolithic Dual Context Files plus On-Demand Priming (Counter-Signal)"
summary: |-
  Plain English: a live counter-example to the "layer your context files" convention —
  and fresh evidence that duplicated context files drift. Archon v0.5.0 deleted its
  11-file path-scoped `.claude/rules/` layer and consolidated everything into a
  979-line monolithic CLAUDE.md plus a root AGENTS.md near-mirror (964 lines) for
  non-Claude harnesses, replacing auto-loaded path-scoped rules with explicit
  `prime-*` slash commands (prime-backend, prime-frontend, prime-isolation,
  prime-workflows) that load domain context on demand. The trade: always-on token
  cost and larger blast radius per edit, in exchange for one canonical file and
  user/agent-initiated context assembly. The two mirror files have already observably
  drifted — AGENTS.md still opens with the superseded "single-developer tool"
  positioning while CLAUDE.md carries the new "governed agentic automation engine"
  identity — a concrete datapoint for the maintenance cost of duplicated context.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "path-scoped-guardrails-edit-time-prevention.md"
    rel: "contradicts"
  - file: "distributed-boundary-guides.md"
    rel: "contradicts"
  - file: "always-on-context-minimalism-pointer-only-entry.md"
    rel: "contradicts"
  - file: "cross-platform-context-file-strategy.md"
    rel: "extends"
  - file: "skill-flattening-outcome-prose-over-step-files.md"
    rel: "same-problem"
  - file: "memory-file-to-skill-migration.md"
    rel: "contradicts"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "context-engineering"
  - "claude-md"
  - "counter-signal"
  - "archon"
---

# Rules-Layer Collapse — Monolithic Dual Context Files plus On-Demand Priming (Counter-Signal)

## What It Is

Between v0.3.2 and v0.5.0, Archon reversed its context-layering strategy:

- **Deleted** the 11-file path-scoped `.claude/rules/` layer (v0.3.2's second context tier) and folded the domain constraints inline into `CLAUDE.md` (780 → 979 lines).
- **Added** a root `AGENTS.md` (964 lines) as a near-mirror of CLAUDE.md for harnesses that read the emerging AGENTS.md convention (Codex, OpenCode, Copilot).
- **Replaced** auto-loaded path-scoped rules with explicit `prime-*` slash commands (`prime`, `prime-backend`, `prime-frontend`, `prime-isolation`, `prime-workflows`) — on-demand domain context loading initiated by the user or agent, instead of harness-triggered injection.

The strategy went from three-tier (CLAUDE.md → path-scoped rules → agents) to two-tier (monolithic global file → agents) plus opt-in priming.

## Why It Matters

The KB's prevailing signal favors layered, scoped, minimal always-on context (path-scoped guardrails, distributed boundary guides, pointer-only entry files). A production repo deliberately walking that back is worth recording on its own terms: consolidation buys one canonical grep-able file, no rule-injection ordering surprises, and identical behavior regardless of which files an agent touches — at the price of ~1k lines of always-on context. The `prime-*` commands are the interesting synthesis: they keep *scoping* while dropping *automatic* injection, moving the loading decision from the harness to the participant.

The mirror-file drift is the second, sharper lesson: within one release cycle, CLAUDE.md and AGENTS.md diverged on the project's own identity statement (governed multi-user engine vs single-developer tool). Duplicated context files are a standing maintenance liability, and even a disciplined, CI-heavy repo drifted immediately — direct evidence for single-source-plus-generation over manual mirrors.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. The consolidation shipped alongside Archon's repositioning as a multi-harness platform (AGENTS.md serves Codex/OpenCode/Copilot); the maintainers evidently judged one canonical context file per harness easier to keep truthful than eleven scoped fragments — though the observed drift undercuts that judgment for the second file.

## Potential Alternatives

Path-scoped rules layers (the approach Archon abandoned). Distributed boundary guides with symlinked CLAUDE.md↔AGENTS.md (OpenClaw — gets the dual-convention coverage without drift). Generated mirrors: author once, build-step emits both files.

## Potential Improvements

A CI staleness check diffing CLAUDE.md vs AGENTS.md (Archon already runs generated-bundle staleness checks — the mirror is the obvious next target). Making `prime-*` invocation observable, so the team can see which domain contexts agents actually load.

## Potential Failure Modes

Always-on ~1k-line context competes with task context in every request. On-demand priming fails silently when the agent doesn't know it should prime (the discovery problem path-scoped injection solved). Mirror drift compounds: harnesses reading AGENTS.md operate under superseded constraints with no error surfaced.
