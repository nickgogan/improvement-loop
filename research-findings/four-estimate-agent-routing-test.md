---
name: Four-Estimate Agent Routing Test (Chat / Agent / Team / Human)
summary: 'Plain English: a one-minute test that tells you whether a task on your desk is a chat

  task, a single-agent task, a multi-agent task, or a keep-it-human task — so you stop

  guessing and stop over-deploying agents. Estimate four things: (1) size — is the task

  bigger than one agent can hold at full quality? (2) independence — can the parts be

  done without knowing what the other parts did? (3) separation of concerns — do any

  parts need to be done by different minds (critic who didn''t write the draft)?

  (4) checkability — is checking an answer much cheaper than producing one? The verdict

  routes to chat, one agent with a goal, a team of agents, or human judgment (no AI).

  Deliberately tool-agnostic: the estimates describe the work, not the evolving tools.'
implementation_notes: 'P2 — flagged as a Phase 4 interview / IB-176 design input (per the accepted

  2026-07-13 link-intake triage): a candidate rubric for the engine''s routine

  chat-vs-subagent-vs-fan-out routing decision, not a roster item on one source. The

  checkability estimate connects directly to the verifier-ceiling finding: fan-out

  without a named cheap checker fails estimate 4.'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (task routing, subagent dispatch)
- General
adopted_in: []
sources:
- 1-6m-agents-registered-for-openclaw-and-did-nothing.md
related_findings:
- file: repeated-sampling-scaling-law-and-verifier-ceiling.md
  rel: enabled-by
- file: two-constraint-decomposition-memory-vs-eval.md
  rel: same-problem
- file: effort-scaling-rules-embedded-in-orchestrator.md
  rel: same-problem
- file: human-ai-seam-identification-three-question-rubric.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-13'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
- skills/four-estimate-routing-test-skill.md
---

# Four-Estimate Agent Routing Test (Chat / Agent / Team / Human)

## What It Is

A one-minute estimation pass over any task, built on the repeated-sampling law and the
two-constraint decomposition theory:

1. **Size** — is the task bigger than what one agent can hold at full quality? (A
   calendar fits in a corner of a context window; a pile of a thousand documents does
   not.)
2. **Independence** — can the parts be done without knowing what the other parts did?
   (Document piles split well — one reader per document, no cross-talk. Coding splits
   only if files are organized into independent parts.)
3. **Separation of concerns** — do any parts need different minds? (A real critic who
   didn't write the draft; an overview by someone who didn't do the reading.)
4. **Checkability** — is checking an answer much cheaper than producing one? (Test
   suite, exit code, a source document to glance at. If checking is expensive, the
   value of extra attempts tops out fast.)

Verdicts: small problem → **chat**; fits one context window and checks its own work →
**single agent with a goal**; bigger than one perspective or needs separate minds →
**team of agents**; judgment call where expert instinct beats model instinct → **human,
no AI**. Jones's productized version adds two money dials — how often the task recurs
and what a good answer is worth — and demonstrates all three verdict classes on camera
(scheduling → single agent; 40-tool contract/usage/renewal analysis → team; hiring
decision → human).

The explicit anti-delegation edge matters: for judgment calls (hires, naming, product
direction), "no frontier model is going to beat an expert at the thing they are most
expert in" — models are a wall to bounce ideas off, not a decision-maker. The test's
most valuable output is often the reminder to keep a task human.

## Why It Matters

The post-OpenClaw framing: 1.6M agents registered for an agent social network at its
peak and most never ran a single task — people have intelligence on tap and no
instrument for matching tasks to it. Thinking is now metered (priced per token, buyable
tonight for a problem discovered this afternoon), and "which task in my week is worth
$50 of purchased thought" is a managerial instinct nobody grew up with. The four
estimates are the durable part: they describe the work, not the tools, so the test
survives tool churn.

## Why People Are Using It

Jones ran all three of his example tasks with real money and showed the runs and the
bills on camera; the test distills the Stanford scaling/ceiling results and Anthropic's
production multi-agent findings into desk-level practice. Shipped as a free interactive
tool alongside the video.

## Potential Alternatives

- Anthropic-style effort-scaling rules embedded in an orchestrator prompt (tiered
  subagent/tool-call budgets by query class) — automates the same judgment inside the
  system rather than at the human's desk.
- Default-to-chat with escalation on failure — cheaper to start, but wastes the cases
  where a team was needed from the outset and burns trust on visible failures.

## Potential Improvements

- Calibration data: track routing verdicts vs outcomes to learn where the one-minute
  estimates misjudge (especially hidden dependence between "independent" parts).
- Fold the two money dials (recurrence, value of a good answer) into engine skill
  triggers, which currently encode neither.

## Potential Failure Modes

- Size estimates drift as models improve — what needed a team last quarter fits one
  agent now; the test needs periodic re-anchoring to current context limits.
- Independence is easy to overestimate: parts that look separable share hidden state,
  and the merged result contradicts itself.
- Disagreement between instinct and test is signal, not noise — rubber-stamping the
  tool's verdict discards the learning opportunity Jones explicitly calls out.

## Extraction Note — 2026-07-19
Extracted as **skill**: [[four-estimate-routing-test-skill]] in `extracts/skills/` (harvest-queue promotion, DD-101). The DD-97 corpus scan matched [[seam-map-delegation-rubric]]; ruled **create new (false positive)** per the 2026-07-19 extension-proposals report — orthogonal, sequentially-composable sibling (route task → vehicle; if team, partition the work), not a mode variant of the seam-map rubric.
