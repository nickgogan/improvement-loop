---
id: "il-stream-0-step-d-design-skill-design-agent-authored"
title: "IL Stream 0 Step D — /design-skill and /design-agent authored under Librarian ownership"
date: "2026-06-11"
session: 110
system: "improvement-loop"
type: "milestone"
agents:
  - "Librarian"
  - "Owner"
tags:
  - "stream-0"
  - "stream-b"
  - "librarian"
  - "design-skills"
  - "construction-substrate"
  - "rule-10"
  - "rule-12"
related_artifacts:
  - ".claude/skills/design-skill/SKILL.md"
  - ".claude/skills/design-agent/SKILL.md"
  - "operations/references/librarian/design.md"
  - "operations/references/librarian/skill.md"
  - "operations/references/librarian/agent.md"
  - "agents/librarian/agent.md"
  - "CLAUDE.md"
roadmap_step: "Stream 0 Step D"
---

# IL Stream 0 Step D — Design Skills Authored

## Context

Cross-system roadmap step D: build IL design skills (`/design-skill`,
`/design-agent`) against substrate landed in step C. Two routed open
decisions resolved with Nick's gate before authoring; the design itself
composed cleanly against existing §Construction substrate without edits.

## Decisions Gated by Nick

### Decision 1 — Ownership: **Librarian**

`/design-skill` and `/design-agent` land under the Librarian agent's skill
inventory. Rationale:

- Symmetric peer of existing `/assess-skill` and `/assess-agent`, which
  self-identify as "Librarian's Audit disposition" and compose
  `audit.md × <concept>.md` from the Librarian reference layer.
- Rule 12 (audit/design symmetry) frames audit and design as bilingual
  readings of one substrate; pairing them under one agent preserves the
  symmetry at the agent-disposition level.
- `design.md` §Governance: "Design is read-only on the KB and on concept
  docs" — matches Librarian's read-only invariant. Default behavior is
  inline draft presentation, not deployment.
- Librarian Builder mode is triggered by "Help me design X" — exact shape
  of `/design-skill` and `/design-agent`.
- Phase 5 delegating to `/assess-*` is the Librarian invoking its own
  assessor in fresh subagent context — satisfies rule 10 within one agent's
  surface.

Counter-candidates rejected: Codifier (KB-finding input shape; writes to
`extracts/`; mismatched IO contract); Owner (steward disposition, not
consumer-advisory).

Pre-existing drift addressed in the same change: IL `CLAUDE.md` Librarian
Skills table and `agents/librarian/agent.md` Skill Inventory previously said
"no dedicated skills." Both updated to reflect actual deployed skills
(`/assess-skill`, `/assess-agent`, `/assess-prompt`, `/design-skill`,
`/design-agent`, `/detect-drift`).

### Decision 2 — Backfill scope: **Attempt design first; gate on hard gaps**

No §Construction backfill prerequisite. `/design-skill` and `/design-agent`
composed cleanly against existing `skill.md` and `agent.md` §Construction
substrate from session 107. No hard gaps surfaced during authoring;
session-109 substrate enrichment remains separate IB candidate work, gated
by Nick.

## Authored Artifacts

| Path | Composition | Phase 5 delegation |
|------|-------------|--------------------|
| `.claude/skills/design-skill/SKILL.md` | `design.md × skill.md` | `/assess-skill` via Agent subagent (rule 10) |
| `.claude/skills/design-agent/SKILL.md` | `design.md × agent.md` (variant-aware: A / B / C / overlaps) | `/assess-agent --variant <selected>` via Agent subagent (rule 10) |

Both skills follow the same 6-phase procedure shape from `design.md`:
parse → load substrate → elicit intent (Decision-sequence walk) → surface
authoring-time risks → draft → delegate audit → assemble report.

Hard gates honored in procedures:
- `/design-skill`: Safety-critical classification at Decision step 4 (per
  `skill.md` §Construction step 4).
- `/design-agent`: Variant selection at Decision step 1 (gates the rest);
  Variant C autonomy-envelope sizing at step 7; G9.I6 on any destructive-
  action path.

## Generator-Assessor Separation Pattern Used (Rule 10)

Both skills invoke their corresponding assess-* skill via the `Agent` tool
with `subagent_type: general-purpose` in a self-contained prompt. The draft
is written to a temp scratch path (`/tmp/design-{skill,agent}-draft-<ts>.md`)
solely for the subagent to read; the temp file is audit input, not a
deployment. The subagent invokes the assess-* skill in fresh context,
returning the full audit report which is embedded in the design report at
Phase 6.

This mirrors Anthropic's skill-creator pattern (captured session 109 in
`generator-assessor-separation-in-skill-iteration.md` — separate
`grader.md`, `comparator.md`, `analyzer.md` subagent definitions) without
copying its mechanics; the IL pattern uses our existing `/assess-*` skills
as the assessor surface.

## Rule 12 Symmetry Check

Both `/design-skill` and `/design-agent` consume the existing §Construction
substrate verbatim — no extensions, no new subsections, no anti-pattern
additions. Therefore no symmetric §Composition review was triggered.
Concept docs (`skill.md`, `agent.md`) are unchanged this session.

This validates that the §Construction substrate landed session 107 is
sufficient for the design pipeline without backfill — a useful evidence
data point on rule 11 ("abstractions must earn their keep") for the
deferred session-109 backfill candidates.

## Drift Fixes (Same Change)

- `systems/improvement-loop/CLAUDE.md` — Librarian Skills table populated.
- `systems/improvement-loop/agents/librarian/agent.md` — Skill Inventory
  populated; "Future skill candidates" updated to roadmap step E
  (`/ask-kb`, `/compare-repos`).

## Scope Adherence

- No DD creation.
- No edits to `design.md`, `audit.md`, `skill.md`, `agent.md`, or rule 12.
- No §Construction backfill prose (deferred — Nick gates per priority
  queue item 2).
- No `/identify-artifacts` or `/extract-artifacts` invocation against
  session-109 findings.
- No promotion of weak-demand abstractions in
  `consumer-abstractions-map.md`.

## Next

Cross-system roadmap step E — hoist Librarian capabilities to first-class
IL skills (`/ask-kb`, `/compare-repos`). Substrate exists in `librarian/`
reference layer and watched-libraries; step E formalizes the consumption
surface. Session 111 handoff targets this work.
