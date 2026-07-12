---
name: "Agent Owner Card and Human-Facing Agent Registry"
summary: |-
  A seven-field owner card per agent that matters — name, owner, job, sources (what it
  reads), what it can do, what it can't do, and the failure mode to watch for — scaled up
  into a team-level agent roster: a plain list of the agents in use with owner, sources,
  permissions, review cadence, and known failure modes. Framed deliberately as "Google's
  A2A protocol, but for the humans": A2A gives agents introduction cards for each other;
  the owner card is the same certificate pointed at people. The claim: once an agent is
  visible on a roster it can be managed; invisible agents become shadow processes where
  work moves through tools and nobody can explain how the output got there.
implementation_notes: |-
  P2 because the field set is a concrete, near-zero-cost design input for two engine
  surfaces: (1) candidate criteria-delta for /assess-agent — does an agent artifact
  declare owner, job-in-one-sentence, diet/sources, can/can't boundaries, and a watched
  failure mode? — restructure-Phase-2 audit material, separately gated; (2) the engine's
  own agents/ directory + docs ownership map already approximate a registry; the delta is
  the per-agent watched-failure-mode and review-cadence fields. Evidence is a
  practitioner framework (no production data); the fuller checklist lives behind the
  author's Substack, not ingested.
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "you-cant-run-ai-agents-without-this.md"
related_findings:
  - file: "job-diet-boundaries-review-loop-operating-framework.md"
    rel: "extends"
  - file: "agent-management-tool-landscape-2026.md"
    rel: "same-problem"
  - file: "agent-identity-governance-enforcement-layer.md"
    rel: "same-problem"
  - file: "dri-rotation-pattern-time-bounded-sensemaking-ownership.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

Two artifacts, one thesis — "the fastest way to make an AI agent dangerous is to let
everyone use it and nobody own it":

**The owner card.** For every agent that matters, write down seven fields: name, owner,
job, sources (what it is allowed to read), what it can do, what it can't do, and the
failure mode you need to watch for. The card works at both scales — a team leader's
spreadsheet row and an individual's ownership certificate. A concrete distribution idea
from the source: a Slack channel of owner cards ("this is my agent, this is what it
does") that doubles as the company's human-readable agent directory.

**The registry/roster.** Not a big database — just the list of agents a team actually
uses (story-prep agent, release-note agent, call-summary agent, PR-review agent), each
carrying owner, sources, permissions, review cadence, and known failure modes. The
mechanism is visibility: a rostered agent can be managed; an unrostered one becomes a
shadow process.

The framing is explicitly parallel to Google's A2A protocol, which assumes agents need
introduction cards *for each other* — the owner card is the missing human-facing half,
"almost like a certificate for the agent." Companies doing agent-to-agent collaboration
through Slack need the human-legible registry layer on top for anyone to understand
what is running.

The cultural corollary: building an agent should earn no credit; owning one that
delivers value in a workflow should. Unowned examples given (HR calibration summarizer
pulling stale manager feedback — claimed real; recruiting scorecard drafter drifting
unaccountably; support triage agent misapplying a stale refund policy) all share the
same root cause: an AI team parachuted an agent into a target team and nobody there
owned it.

## Why It Matters

The KB documents the unowned-agent problem side extensively (dark code, agent sprawl,
shadow processes); this is the lightest-weight remedy artifact yet recorded — seven
fields and a list, no platform required. For the engine specifically: the four IL agents
have owners and job definitions, but no per-agent watched-failure-mode or review-cadence
field — and the owner-card field set reads almost directly as an audit checklist for
`/assess-agent` (whether an agent artifact *declares* these fields is file-verifiable).

## Why People Are Using It

The author claims companies with an ownership-registry mindset outperform
building-focused ones, and positions maintenance as the 2026 skill in the arc
prompting (2023) → delegation (2025) → maintenance (2026). Opinion-tier but consistent
with the KB's convergent unowned-agent findings and with regulatory pressure toward
demonstrable oversight.

## Potential Alternatives

- **Identity-governance infrastructure** (existing KB finding): the enforcement-grade
  version — policy-driven identity, audit trails. The owner card is the cultural/
  operational on-ramp, not a replacement.
- **Agent management platforms** (existing KB landscape finding): tooling-heavy;
  the card/roster works in a spreadsheet or Slack channel today.
- **A2A-style machine-readable agent cards:** solve agent-to-agent introduction, not
  human accountability.

## Potential Improvements

- Machine-readable owner cards (frontmatter on the agent definition file) so the
  registry is generated, not maintained — aligning with the engine's no-hardcoded-counts
  rule.
- Tie the card's watched-failure-mode field to the review loop's cadence: the review
  checks specifically for the declared failure mode.

## Potential Failure Modes

- **Registry rot:** a hand-maintained roster drifts from reality — the exact
  maintenance-burden pattern the engine avoids; generation from source-of-truth agent
  files is the countermeasure.
- **Card theater:** filling in seven fields without the owner actually reviewing —
  ownership on paper, not in practice.
- **Ownership without authority:** a named owner who cannot change the agent's sources
  or permissions can't act on what they observe.
