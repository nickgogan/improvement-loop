---
name: 'Work-Ticket Contract: Prompt Mode vs Work Mode'
summary: 'Plain English: when work moves between agents (or agent and human), a chat prompt is

  not enough — the handoff needs a contract. Nate B Jones''s Open Engine defines the

  work-ticket as the boundary object between "prompt mode" (asking an AI for an answer)

  and "work mode" (giving it a job the next agent can pick up): every ticket carries the

  outcome wanted, the owner, the source material, explicit scope limits ("where the agent

  should stop"), a definition of done, and what it must show when finished. Two contract

  mechanics complete it: the claim receipt (agent claim-locks the ticket, moves it to

  agent-working, and on completion leaves an auditable receipt proving what was done —

  distinct from asking the agent "did you do it?") and the needs-input escalation state

  (on ambiguity the agent doesn''t guess; it parks the ticket in needs-input carrying the

  exact blocking question, resumes when answered, and the audit trail stays on the

  ticket).'
implementation_notes: 'The engine''s pipeline is already file-mediated (pipeline_status handoffs, handoff

  protocol) but its handoff artifacts don''t carry a uniform contract: definition-of-done

  and proof-of-done are implicit, and there is no needs-input state — blocked subagents

  currently improvise. The ticket field set (outcome / owner / sources / scope limits /

  definition of done / receipt) is a candidate schema for the engine''s subagent task

  prompts and delta-report handoffs. Flagged at triage as a future harness-layer

  schematic candidate (Nick-gated).'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (handoff protocol, subagent task contracts)
- General
adopted_in: []
sources:
- i-was-the-only-thing-connecting-claude-chatgpt-codex.md
- codex-your-first-personal-ai-agent-delegation-loop.md
related_findings:
- file: chief-of-staff-home-base-thread.md
  rel: same-problem
- file: issue-based-agent-orchestration-replacing-markdown-plans.md
  rel: extends
- file: agent-self-reporting-unreliability-independent-eval.md
  rel: same-problem
- file: github-label-as-workflow-state.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
- templates/work-ticket-contract-template.md
---

## What It Is

The contract layer on top of a shared agent work queue. The queue itself (Linear, Jira,
Beads — anything both humans and agents can read/write) is established practice; the
contract is what makes an item on it transferable. Jones's distinction: "a prompt asks
for an answer; a ticket asks for a result to get done." A conformant work-ticket states:

- **Outcome** — what needs to happen, as a result, not a request
- **Owner** — who (human or agent) it is assigned to
- **Sources** — the background material carried with the work, so nothing depends on
  reading a chat transcript
- **Scope limits** — what the agent may do and where it must stop
- **Definition of done** — the acceptance condition
- **Receipt** — what it must show when finished

The lifecycle mechanics: an agent **claim-locks** the ticket before working (moves it
agent-todo → agent-working, leaves a claim receipt so double-pickup is impossible and
progress is visible); on completion it leaves a **done receipt** — auditable proof of
what was done, "not decoration," explicitly replacing trust in the agent's self-report;
on ambiguity it moves the ticket to **needs-input** carrying the exact blocking question,
so the human answers on the ticket and the audit trail stays in one place.

## Why It Matters

The bottleneck Jones names is not model capability but the boundary between agents — the
human as the "hallway" carrying state between harnesses. The contract is what lets work
cross that boundary without the human as copy-paste path: "output is what the AI returns
right now; work is what someone can review, accept, and build on." The three mechanics
map to three failure modes: no claim → duplicate work; no receipt → unverifiable
self-reported completion; no needs-input state → agents guessing at ambiguity or stalling
silently.

## Why People Are Using It

Jones uses it in production at home and with his team (mixed human + multi-vendor
agents); demoed cross-vendor delegation where a Codex agent authors a self-contained
ticket for a teammate's Claude agent, picked up on that agent's own heartbeat. The
pattern is vendor-neutral by construction — the ticket is where unintegrated agents
"talk," so no harness-to-harness integration is needed.

## Potential Alternatives

- Direct agent-to-agent protocols (A2A, MCP-based delegation) — richer but requires
  integration between specific harnesses; the ticket works across anything
- Shared markdown plan files — carry context but lack claim/state/receipt mechanics
- Chat/Slack as coordination bus — Jones explicitly rejects both as state managers

## Potential Improvements

- Typed receipt formats per work class (screenshot, diff, log, link) rather than
  free-form proof
- Escalation-rule fields so tickets carry their own gating policy (mirrors "create a
  product task only if it meets my escalation rule")
- Contract linting: reject tickets missing definition-of-done or scope limits at
  creation time

## Potential Failure Modes

- Contract theater: fields filled with boilerplate, receipts that assert rather than
  prove — the receipt is only as good as its verifiability
- Overhead on small tasks: full contract on trivial work pushes people back to prompt
  mode
- Queue rot: needs-input tickets that never get answered accumulate as invisible stalls
  unless the queue is actively reviewed
- The ticket carries context by copy — stale sources if upstream material changes while
  the ticket waits

## Lineage — five-element assignment contract (2026-06-12)

Jones's earlier Codex delegation-loop video carries the simpler ancestor of this
contract: give the agent five things — **a goal, sources, a standard, a permission
boundary, and the proof that it's done**. "That's the most basic way to set up a loop.
It's not a fancy prompt... a real assignment with real sources and a way to check the
results." The work-ticket (2026-07) is the same contract matured into a transferable
queue object — outcome/owner map to goal, scope limits to permission boundary,
definition-of-done + receipt to standard + proof — adding the lifecycle mechanics
(claim-lock, needs-input) that only matter once multiple agents share the queue. Newer
framing leads per the recency rule; the five-element version remains the right
starting shape for single-operator loops.

## Extraction Note — 2026-07-19
Extracted as **template**: [[work-ticket-contract-template]] in `extracts/templates/`
