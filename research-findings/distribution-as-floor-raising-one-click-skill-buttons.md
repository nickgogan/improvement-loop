---
name: "Distribution as Floor-Raising: One-Click Headless Skill Buttons"
summary: |-
  Once skills and automations are validated, wrap each as a single button (web app or
  Obsidian-plugin command center) that invokes headless Claude Code (`claude -p`)
  behind the scenes — no terminal ever appears. Non-technical teammates and clients
  get the full power of the validated skill with one click or a voice command,
  outputs land in their (or the team's) vault. Chase AI frames this as a
  floor-raising mechanism for an organization: "it's like spinning them up on Claude
  Code without actually spinning them up on Claude Code."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "the-agentic-os-setup-that-will-10x-claude-code.md"
related_findings:
  - file: "headless-cron-composition-autonomous-scheduled-workflows.md"
    rel: "extends"
  - file: "orchestrator-headless-dispatch-context-isolation.md"
    rel: "same-problem"
  - file: "audit-skill-as-expert-harness-distribution-channel.md"
    rel: "same-problem"
  - file: "html-output-as-human-in-the-loop-restorer.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

Level 4 of Chase AI's agentic-OS construct: distribution of validated capability to
people who will never open a terminal. Mechanics:

- Each dashboard button maps to an existing skill/automation; clicking it runs a
  headless Claude Code invocation (`claude -p /skill-name`) — invisible, no terminal
  window, results written to the vault and surfaced in the UI.
- Delivery vehicles: a custom web app (easiest to distribute — GitHub repo/zip) or an
  Obsidian plugin command center (requires hands-on setup per user). Optional local
  voice model for spoken invocation and read-back, running fully on-device.
- Explicitly sequenced LAST: levels 1-2 (skill architecture + memory/state) are "90%
  of the value"; the button layer only wraps what's already validated.

Operational caveat recorded by the source: Anthropic briefly announced `claude -p`
would draw from API credits rather than the Max subscription, then walked it back —
at recording time headless still pulls from the subscription. The economics of this
pattern are policy-sensitive.

## Why It Matters

Names the adoption problem precisely: "99% of people just won't go there" — the
terminal (and even the desktop app) is a hard barrier for non-technical teammates and
clients. Buttonizing validated skills raises the organizational floor without training
anyone on the harness, and the "dashboard effect" changes how non-technical users
perceive the tool's trustworthiness. For client-service builders it converts a skill
library into a deliverable product.

## Why People Are Using It

Demonstrated live on the author's production dashboard (inbox-brief button → queued →
headless run → triaged threads with urgent items flagged, voice read-back). Same
distribution logic as the KB's audit-skill-as-distribution-channel finding: package
expert capability so consumers invoke it without understanding its internals.

## Potential Alternatives

Claude Desktop routines/scheduled tasks (no custom UI, but still Claude-branded
surfaces). Slack-bot fronting (meet users in chat instead of a dashboard). Hosted
agent platforms with per-seat access.

## Potential Improvements

Permission-scoped buttons (`--allowed-tools` per button) so distributed capability is
least-privilege by construction. Run receipts attached to each button press for
auditability.

## Potential Failure Modes

Subscription-policy risk: if headless invocations move to API pricing, the one-click
economics change abruptly. Distributing buttons distributes agency without
understanding — users can't diagnose a wrong output, so validation and receipts have
to carry the trust load. Obsidian-based command centers don't distribute cleanly
(per-user manual setup).
