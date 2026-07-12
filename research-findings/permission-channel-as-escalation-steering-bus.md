---
name: "Permission Channel as a Universal Escalation and Steering Bus"
summary: |-
  Two independent production harnesses converge on the same move: whatever pipe already
  carries permission asks to the human becomes the general-purpose channel for everything
  that needs a human mid-run. omnigent escalates every ASK to the server that owns the
  elicitation channel (runners only fast-path local ALLOW/DENY); opencode routes doom-loop
  detection into a permission ask instead of an error, and lets a rejection carry feedback
  text that is injected back as steering. Anomaly escalation, approval, and course-correction
  all ride one bus. For us: design the human gate once, as infrastructure, and route every
  human-in-the-loop need through it instead of building per-feature interaction channels.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "mcp-elicitation-for-user-input.md"
    rel: "extends"
  - file: "interrupt-command-primitives-human-in-the-loop.md"
    rel: "same-problem"
  - file: "loop-detection-hash-based-sliding-window.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

A cross-repo synthesis: three mechanisms in two unrelated production harnesses that each widen the permission/approval channel into the harness's *only* human-interaction bus.

1. **omnigent — dual-evaluation ASK escalation** (`omnigent/runner/policy.py`): the runner-side policy gate fast-paths ALLOW and DENY locally, but any ASK is re-escalated to the server, because the server owns the one elicitation channel (web UI, terminal popups, tmux cost panes). Every policy type — cost checkpoints, blast-radius warnings, taint gates — surfaces to the human through that single pipe.
2. **opencode — doom-loop breaker as a permission** (`packages/opencode/src/session/processor.ts`): three identical consecutive tool calls trigger `permission.ask("doom_loop")` rather than an error. Pathology detection reuses the ask/allow/deny machinery — including "always allow" persistence — instead of inventing an anomaly-reporting channel.
3. **opencode — rejection with feedback as steering** (`packages/core/src/v1/permission.ts`): the reply schema distinguishes `RejectedError` (human said no) from `CorrectedError` (human said no *and* the attached message is injected back into the loop as course-correction). The gate doubles as the steering wheel.

The common shape: the permission channel already has what any human-in-the-loop feature needs — durable parking (turns wait on a verdict), UI surfacing on every client, verdict semantics, and audit trail — so escalation, anomaly handling, and steering are modeled *as verdicts* rather than as new channels.

## Why It Matters

Harnesses accumulate human-interaction needs one feature at a time — approvals, budget warnings, loop alarms, clarifications, corrections — and the default is one bespoke channel each, every one needing its own UI surfacing, persistence, and timeout story. The convergent alternative: build the ask-park-verdict pipe once, then express each need as a policy verdict on that pipe. Features inherit the bus's guarantees for free (a doom-loop ask can be answered from opencode's TUI or API identically; an omnigent cost ASK parks the turn durably server-side). The steering variant is the deepest consequence: once rejection can carry text back into the loop, the boundary between "permission gate" and "conversation" dissolves — the gate becomes the highest-signal place to steer, because the model is already stopped and attending to the verdict.

## Why People Are Using It

Independently observed in [omnigent](https://github.com/omnigent-ai/omnigent) v0.6.0.dev0 (alpha) and [opencode](https://github.com/anomalyco/opencode) dev branch (`34e5809`, 2026-07-11) — see [[omnigent-analysis]] and [[opencode-analysis]] for structural details. Two unrelated codebases, three mechanisms, one convergent architecture — stronger signal than any single instance.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Per-feature channels | Dedicated UI/flow per interaction type | When interaction modalities genuinely differ (e.g. OAuth redirects vs yes/no) |
| Interrupt/resume primitives | Graph-level pause with typed resume commands (LangGraph interrupt/Command) | Workflow engines where routing, not permission, is the native abstraction |
| Protocol-level elicitation | MCP elicitation as the standard pipe | Cross-product tool servers that can't assume one harness's permission layer |

## Potential Improvements

- Verdict taxonomy: as more features ride the bus, distinguish approval, anomaly-ack, and steering verdicts explicitly so analytics and timeout policies can differ per class
- Timeout defaults per rider (a doom-loop ask left unanswered should probably deny; a cost checkpoint might auto-approve at a threshold)

## Potential Failure Modes

- **Ask fatigue:** one bus means one attention budget — overloading it trains the human to click allow, degrading every rider at once
- **Semantics flattening:** forcing genuinely different interactions (clarification questions, multi-option choices) into allow/deny verdicts loses information
- **Bus as bottleneck:** if the channel's owner (omnigent's server) is down, every human-dependent path parks — fail-closed asymmetry needs to be designed per phase, as omnigent does
