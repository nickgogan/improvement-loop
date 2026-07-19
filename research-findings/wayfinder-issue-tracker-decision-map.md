---
name: "Wayfinder — Issue-Tracker Decision Map for Plans Too Big for One Session"
summary: |-
  Plain English: when an idea is too big to plan in one agent session, don't manage a long
  chat — externalize the plan as a map of decision tickets on the repo's issue tracker and
  work them one session at a time. Pocock's /wayfinder skill charts "a loose idea... too
  big for one agent session and wrapped in fog" as a parent GitHub issue with sub-issues,
  where each sub-issue is one *decision to make*, typed (research / grilling / prototype /
  task), scoped to the size of an agent session, and blocking-ordered (key decisions gate
  the rest). Closed tickets write their findings back onto the map; when the map is
  complete it feeds /to-spec. The map — not the chat — carries state, which removes
  session-handoff anxiety ("smart zone" management) and makes planning collaborative and
  team-shareable for free.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "pocock-skills-v1-1-wayfinder-research-implement.md"
related_findings:
  - file: "external-ticket-as-brainstorm-seed.md"
    rel: "same-problem"
  - file: "leg-work-amplification-hiding-future-steps.md"
    rel: "extends"
  - file: "everyday-default-flow-smart-zone-ticket-sizing.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-18"
pipeline_status: "raw"
---

# Wayfinder — Issue-Tracker Decision Map for Plans Too Big for One Session

## What It Is

A planning topology for work that exceeds one agent session's context or "smart zone." The
`/wayfinder` skill (Pocock skills v1.1) converts a foggy, oversized idea into a **shared
map on the repo's issue tracker**:

- A parent issue holds the map: the running record of decisions made and primary-source
  links back to the tickets that produced them.
- Each sub-issue is one **decision to be made**, deliberately scoped to the size of a
  single agent session.
- Sub-issues carry **blocking relationships** — key decisions must close before dependent
  ones open.
- Each ticket is **typed** by how its decision gets made:
  - **research** — AFK task; agent investigates primary sources and reports back,
  - **grilling** — needs an interactive interview session with the user,
  - **prototype** — "raise the fidelity of the discussion by making a cheap, rough,
    concrete artifact to react to" (outline, tech stub, UI logic); recommended whenever
    "how should it look / behave" is a key question — essentially anything front-end,
  - **task** — config, provisioning, data-shaping; needs neither decision nor automation.

Working the map is one-ticket-per-session; closing a session costs nothing because the
map, not the conversation, carries state. When all tickets close, the completed map feeds
`/to-spec` like any other planning input.

## Why It Matters

It resolves the multi-session planning problem by inverting where state lives: instead of
compressing chat state through handoffs, the durable artifact *is* the plan, in a medium
(issue tracker) that is collaborative, typed, and dependency-aware by construction. Two
transferable ideas stand out even for systems that keep their own planning stack: (1)
tickets scoped as *decisions*, not work items — session-sized decision quanta with
blocking order; (2) a type system that routes each decision to the right resolution mode
(autonomous research vs human interview vs prototype vs chore). The prototype type encodes
a further principle — cheap concrete artifacts raise discussion fidelity before spec.

Roster note: adopting `/wayfinder` itself was assessed and declined at triage (overlaps
the GSD suite and `/session-handoff`); this entry captures the pattern as KB substrate
only.

## Why People Are Using It

Pocock calls it the v1.1 feature he's "really, really excited about," uses it "for
literally everything, even non-coding stuff" (including planning his course), and
positions it as the recommended default over his own grill-with-docs for large plans.
Demonstrated live on the Sandcastle repo (AI SDK dependency spike).

## Potential Alternatives

Session-handoff compression (state summarized into a prompt — what it replaces; strains as
plans grow). Planning-directory conventions (GSD's .planning/, ROADMAP.md — same
externalization into files instead of tracker issues; less collaborative, no native
blocking semantics). Single mega-planning-session with compaction (stays inside the
context window's mercy).

## Potential Improvements

Typed-decision taxonomies beyond the four (e.g. spike-with-timebox, reversible-default).
Auto-generating the initial decision breakdown from a grilling transcript. Tracker-agnostic
backends (the pattern is GitHub-issues-shaped but nothing requires GitHub).

## Potential Failure Modes

- **Decomposition quality bounds everything**: a map whose tickets aren't really
  session-sized, or whose blocking order is wrong, serializes pain rather than removing it.
- **Map staleness**: decisions made out-of-band (in chat, in code) that never land on the
  map silently fork the source of truth.
- **Overhead below threshold**: for plans that *do* fit one session, the ceremony is pure
  tax — Pocock scopes it explicitly to too-big-for-one-session ideas.
- **Tracker coupling**: teams without issue-tracker discipline (or with noisy trackers)
  inherit that noise into their planning substrate.
