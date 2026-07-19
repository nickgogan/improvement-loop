---
name: Four-Type Loop Trigger Taxonomy — Continuous, Cron, Event/Webhook, and the Poll-Then-Wake Combo
summary: |-
  Plain English: how a loop gets woken up matters as much as what it does once awake,
  and there are four distinct trigger shapes, not one. (1) Continuous — a while-loop
  that keeps working until a goal condition or budget is hit (Claude Code/Codex's
  native "go"/goal command); best for tasks with immediate feedback and a well-defined
  spec. (2) Cron/schedule — wake on a fixed interval (Claude Code's /loop, Codex
  automations); natively supported. (3) Event-based — wake on an external signal (new
  email, a server incident); best for things needing immediate handling, but neither
  Claude Code nor Codex support this natively — it requires standing up your own local
  daemon that exposes a webhook URL for external systems to call. (4) Combo/workflow —
  the most useful in practice: a cron-interval ticker runs a cheap deterministic script
  first to check programmatically whether there is real new work; only if so does it
  wake the expensive LLM agent. Production example: a support-inbox loop that polls
  Intercom every 30 minutes and skips the run entirely if nothing changed.
implementation_notes: |-
  The combo pattern is the concrete, generally-applicable cost lever: any of the
  engine's cron-shaped periodic skills (watch-blogs, watch-upstream) could gain a cheap
  pre-check step (e.g., compare a feed's last-modified/etag before invoking the
  research subagent) to skip no-op runs entirely, the same trade the source's
  support-inbox loop makes against Intercom. The event/webhook trigger type and its
  platform gap matter only if/when the engine wants true external-event-driven
  automation (e.g., react to a GitHub webhook rather than polling); today that would
  require the same self-hosted daemon the source describes, since neither Claude Code
  nor Codex expose native webhook ingestion (Anthropic's separate "Claude Routines"
  product does — see Potential Alternatives).
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (token-cost optimization for periodic/scheduled skills)
- General
adopted_in: []
sources:
- i-was-building-loops-wrong.md
related_findings:
- file: monitor-vs-loop-event-driven-vs-time-driven.md
  rel: extends
- file: claude-code-loop-in-session-cron-scheduling.md
  rel: same-problem
- file: headless-cron-composition-autonomous-scheduled-workflows.md
  rel: same-problem
- file: kairos-autonomous-background-daemon.md
  rel: same-problem
- file: claude-routines-webhook-triggered-pipeline-chaining.md
  rel: contrasts-with
- file: time-window-proactive-agent-loop.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: synthesized
consumed_by:
- autonomous-scheduled-agent-operation.md
- rules/deterministic-nodes-for-non-reasoning-steps.md
tags:
- orchestration
- loop-engineering
- trigger-design
- cost-optimization
- agentic-systems
---

# Four-Type Loop Trigger Taxonomy — Continuous, Cron, Event/Webhook, and the Poll-Then-Wake Combo

## What It Is

Four distinct ways to wake an autonomous loop, each fit to a different kind of work:

| # | Trigger | Mechanism | Best for | Native support |
|---|---------|-----------|----------|-----------------|
| 1 | Continuous | A while-loop: keep running until a goal condition, max turn count, or token budget is hit | Immediate-feedback tasks with a well-defined spec (bug fixing, implementing a specced feature) | Yes — Claude Code / Codex "go"/goal command |
| 2 | Cron/schedule | Wake on a fixed time interval | Periodic maintenance with no urgency | Yes — Claude Code `/loop`, Codex automations, cloud schedule |
| 3 | Event-based | Wake on an external signal (new email, server incident) | Work needing immediate handling | **No** — neither Claude Code nor Codex support this natively |
| 4 | Combo/workflow | Cron-interval ticker runs a cheap deterministic check first; only wakes the LLM agent if the check finds real new work | Cost-sensitive polling against a data source that changes rarely relative to the check interval | Requires a custom script; the LLM-wake step reuses trigger types 1/2 |

**The platform gap (trigger type 3).** Both Claude Code and Codex lack a native event/webhook trigger. To get one, the source's approach is a self-hosted local daemon process that exposes a URL — e.g., stand up a webhook endpoint (they mention Render as one hosting option) that receives external notifications and forwards them to the local agent. This is real infrastructure to run and maintain, not a config flag.

**The combo pattern in production.** Their support-inbox triage loop runs a ticker on an interval, but instead of invoking the agent immediately, a JavaScript pre-check script fetches recent updates from Intercom (the last 30 minutes). If there's nothing new, the run is skipped — no agent invocation, no token spend. If there is new work, the agent is invoked to handle it. This batches work and only pays the expensive-model cost when there's something to do, rather than paying it every tick regardless of state.

## Why It Matters

Trigger choice is a first-order cost and latency lever, independent of what the loop does once running — the same underlying agent logic can cost radically different amounts depending on whether it's invoked on every tick (cron) or only on confirmed new work (combo). The source frames this directly: "choosing the right trigger for the specific type of loop that you're running will really drive down the cost a lot." The four-way split also clarifies a confusion the source names explicitly: a lot of "loop" discourse conflates trigger types, making loops seem more interchangeable than they are — a continuous goal-loop and a cron-scheduled loop solve different problems and shouldn't be chosen by default/convenience.

## Why People Are Using It

Production-run at Super Divine for months across the four loop examples in the companion loop-contract finding. The combo trigger specifically was arrived at through an evolve session on the support-inbox loop (see `loop-contract-anatomy-and-evolve-session-cadence.md`) — it wasn't the original design, it was a self-proposed optimization after the loop had been running for a while.

## Potential Alternatives

- **Claude Code's Monitor tool** — genuinely push-based (zero polling), but scoped to watching a *local background process's* stdout stream within a session, not external systems. Different mechanism from the combo trigger's scheduled-poll-plus-cheap-check, though both share the goal of not paying full LLM cost on every check. See `monitor-vs-loop-event-driven-vs-time-driven.md`.
- **Claude Routines** (a separate Anthropic product from Claude Code) — natively supports webhook-triggered chaining between cloud-hosted routines, which is closer to true event-based triggering than anything in Claude Code or Codex today. Worth knowing the platform-gap claim is scoped to Claude Code/Codex specifically, not "Anthropic's tooling" broadly. See `claude-routines-webhook-triggered-pipeline-chaining.md`.
- **KAIROS** — an unreleased, feature-flagged Claude Code daemon that would (per source-leak analysis) natively watch GitHub webhooks and run proactive budget windows — i.e., Anthropic's own apparent answer to this exact gap, not yet shipped. See `kairos-autonomous-background-daemon.md`.

## Potential Improvements

- A standard library of cheap pre-check scripts per common data source (RSS/webhook feed last-modified, API etag, Intercom-style "updates since" endpoints) would make the combo pattern reusable rather than bespoke per loop.
- Combining trigger types 3 and 4: a webhook receiver that itself does a cheap relevance check before waking the agent, rather than waking on every webhook delivery.

## Potential Failure Modes

- The combo pattern's cheap check can itself drift out of sync with what the agent actually needs to know about (e.g., an Intercom filter that misses a category of update) — silent under-triggering is harder to notice than over-triggering, because nothing fires to prompt investigation.
- Standing up a self-hosted daemon for event triggers (trigger type 3) introduces a new always-on piece of infrastructure with its own uptime, security, and maintenance burden — exactly the kind of operational weight the other three trigger types avoid.
- Continuous (type 1) loops without a token/turn budget can run away; the source's framing assumes a budget is always set, but doesn't describe what enforces that discipline.

## Extraction Note — 2026-07-19
Merged into [[deterministic-nodes-for-non-reasoning-steps]] (added as the "Special Case: The Trigger/Wake Node" section). Session 152; DD-97 extend-existing ruling (Nick-delegated) — the combo-trigger claim is the same rule and mechanism (a non-reasoning node must be deterministic code) applied to the specific wake/trigger node of a scheduled loop, drawn from this finding as a sibling source in the same guide cluster.
