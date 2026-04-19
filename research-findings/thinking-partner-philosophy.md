---
name: "Thinking Partner Philosophy"
summary: "GSD's discuss-phase frames the agent-human relationship as 'user = founder/visionary, Claude = builder' — the agent does not explore WHAT to build (that is decided) but clarifies HOW to implement via gray-area questions, assumption extraction, and decision locking, producing CONTEXT.md with locked decisions."
implementation_notes: null
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-04-08"
last_updated: "2026-04-08"
pipeline_status: "raw"
consumed_by: []
---
# Thinking Partner Philosophy

## What It Is
GSD's discuss-phase explicitly scopes the agent-human collaboration. The user is framed as the "founder/visionary" — the person who has already decided what to build. The agent is the "builder" — responsible for clarifying HOW to implement, not WHAT to implement. The discussion extracts gray-area decisions, surfaces hidden assumptions, and locks implementation choices into a CONTEXT.md artifact. Phase goals are FIXED; the discussion clarifies implementation approach only.

## Why It Matters
Unbounded agent exploration is a common failure mode. Agents asked to "help build X" often drift into questioning whether X is the right thing to build, exploring alternative architectures, or suggesting scope changes. GSD's explicit framing prevents this by making the phase goal non-negotiable and focusing the agent's intelligence on the implementation path — where its technical knowledge is most valuable.

## Why People Are Using It
Observed in [GSD](https://github.com/gsd-build/get-shit-done) v1.33.0 — see [[gsd-analysis]] for structural details. The discuss-phase runs before planning, producing a CONTEXT.md that captures locked decisions, resolved ambiguities, and clarified constraints. This artifact feeds into the planning phase, ensuring the planner does not re-open settled questions.

## Potential Alternatives
Superpowers' brainstorming-as-design-gate approach explores WHAT to build through mandatory design presentation. BMAD's user-mediated skill selection lets the user pick the interaction mode. Free-form chat without role boundaries. Structured requirements elicitation templates that ask specific questions in a fixed order.

## Potential Improvements
Explicit assumption surfacing — the agent lists all assumptions it is making and asks the user to confirm or correct each one. Decision dependency tracking — showing which downstream decisions depend on which upstream locks, so the user understands the impact of each choice. Time-boxing the discussion phase to prevent over-analysis of implementation details.

## Potential Failure Modes
Over-constraining — if the user locks too many decisions during discussion, the implementer loses flexibility to make reasonable technical choices. Under-discussion — if the user rushes through, critical ambiguities remain unresolved and surface during execution. Role confusion — if the agent interprets "builder" as "only follow orders" rather than "think critically about implementation."
