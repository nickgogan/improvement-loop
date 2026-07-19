---
title: "Four-Estimate Routing Test — Chat / Agent / Team / Human"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "four-estimate-agent-routing-test"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "someone with a task in front of them deciding whether to handle it in a chat, hand it to a single goal-directed agent, split it across a team of agents, or keep it entirely human"
    - "operators prone to over-deploying agents (or under-using them) who want a fast, tool-agnostic check before committing effort or spend"
    - "an orchestrator or routing layer choosing between a single-agent call and a fan-out of subagents for an incoming task"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — produces an advisory routing verdict; re-running it or overriding the verdict has no migration cost"
  auditability: "high — the verdict is one of four named classes and the four estimates behind it are recorded, so a reviewer can re-check each estimate against the task"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Productized by a practitioner as a free interactive tool alongside a video that demonstrated all three AI verdict classes with real spend (scheduling → single agent; multi-tool contract analysis → team; hiring decision → human). Distills repeated-sampling scaling-law and verifier-ceiling results into desk-level practice; not yet adopted by the extracting system."
contract:
  preconditions: "A specific task is in hand. The operator (or routing layer) can honestly estimate the task's four properties — size, independence, separation of concerns, and checkability."
  invariants: "The verdict is exactly one of four classes — chat / single agent with a goal / team of agents / human (no AI). A `team of agents` verdict is never issued without a named cheap checker satisfying the checkability estimate (fan-out with no verifier fails estimate 4). The four estimates describe the *work*, not the current tools, so the test survives tool churn. Size estimates are re-anchored to current context limits rather than treated as fixed."
  governance: "Advisory. The human — or the orchestrator embedding the test — owns the routing decision; the test never dispatches work itself. The two money dials (how often the task recurs, what a good answer is worth) sharpen the verdict but never override the anti-delegation edge: genuine judgment calls stay human."
  recovery: "If instinct disagrees with the verdict, treat the disagreement as signal — re-examine the estimates rather than rubber-stamping the verdict. If parts assumed independent turn out to share hidden state, re-estimate independence and step down from `team` to `single agent` or re-partition the work. If checking an answer is expensive, do not route to a `team` (extra attempts top out fast) — keep it single-agent or human. Re-anchor size estimates as model context limits grow."
tags:
  - "extracted-artifact"
  - "skill"
---

# Four-Estimate Routing Test — Chat / Agent / Team / Human

**Source:** [[four-estimate-agent-routing-test]]
**Form:** skill
**Extraction date:** 2026-07-19

> **Related skill (same family, composes in sequence):** [[seam-map-delegation-rubric]] **decomposes and partitions** a single workflow into human / AI / joint parts — its output is a seam map, and it makes no claim about *what shape* the AI-owned side should take. This test **classifies a whole task to a deployment vehicle** — chat / single agent / team / human. The two run in series, not as alternate modes of one skill: route the task to a vehicle first; if the verdict is `team of agents`, that is itself the input to a subsequent seam/decomposition partition. Ruled create-new (not a mode variant of the seam-map rubric) per the 2026-07-19 extension-proposals report — orthogonal, sequentially-composable members of the same "pre-deployment human/AI allocation" family.

## Purpose

A one-minute estimation pass that tells you whether a task on your desk is a **chat** task, a **single-agent** task, a **multi-agent (team)** task, or a **keep-it-human** task — so you stop guessing and stop over-deploying agents. Its most valuable output is often the reminder to keep a task human: for judgment calls (hires, naming, product direction), no frontier model beats an expert at the thing they are most expert in — the model is a wall to bounce ideas off, not the decision-maker.

The test is deliberately **tool-agnostic**: the four estimates describe the work, not the evolving tools, so the verdict survives tool churn.

## Inputs

- A specific task the operator (or a routing layer) is about to act on.
- Honest estimates of the task's four properties (below).
- Optionally, the two **money dials** — how often the task recurs, and what a good answer is worth — which sharpen the verdict but do not change the estimates.

## Outputs

- A single **routing verdict**: one of `chat`, `single agent with a goal`, `team of agents`, `human (no AI)`.
- The four estimates behind the verdict, recorded so the decision can be re-checked and re-anchored later.
- For a `team of agents` verdict: the named cheap checker that satisfies the checkability estimate (without one, the verdict is invalid — see Steps).

## Steps

### 1. Estimate size.
Is the task bigger than what one agent can hold at full quality? A calendar fits in a corner of a context window; a pile of a thousand documents does not. Re-anchor this to *current* context limits — what needed a team last quarter may fit one agent now.

### 2. Estimate independence.
Can the parts be done without knowing what the other parts did? Document piles split well — one reader per document, no cross-talk. Code splits only if files are organized into independent parts. Independence is easy to overestimate: parts that look separable often share hidden state.

### 3. Estimate separation of concerns.
Do any parts need *different minds*? A real critic who didn't write the draft; an overview by someone who didn't do the reading. If yes, a single agent cannot cover all the roles at once.

### 4. Estimate checkability.
Is checking an answer much cheaper than producing one? A test suite, an exit code, a source document to glance at. If checking is expensive, the value of extra attempts tops out fast — and a fan-out to many agents buys little.

### 5. Read out the verdict.
- Small problem → **chat**.
- Fits one context window and can check its own work → **single agent with a goal**.
- Bigger than one perspective, or needs separate minds → **team of agents** — but only if estimate 4 named a cheap checker; a fan-out with no verifier fails checkability and must not be routed to a team.
- Judgment call where expert instinct beats model instinct → **human, no AI**.

### 6. (Optional) Turn the money dials.
Fold in how often the task recurs and what a good answer is worth to sharpen a borderline verdict — a high-recurrence, high-value task justifies more machinery; a one-off low-value task justifies less. The dials never override the anti-delegation edge in step 5.

## Failure Modes

- **Size drift.** Estimates go stale as models improve — what needed a team last quarter fits one agent now. Mitigation: re-anchor size to current context limits, don't freeze it.
- **Independence overestimated.** Parts that look separable share hidden state, and the merged result contradicts itself. Mitigation: when a `team` result is incoherent, re-estimate independence and step down to single-agent or re-partition.
- **Checkability ignored on fan-out.** Routing to a team without a cheap checker wastes the extra attempts — the verifier ceiling caps their value. Mitigation: a `team` verdict is invalid without a named checker satisfying estimate 4.
- **Instinct-vs-test disagreement rubber-stamped.** Disagreement between the operator's instinct and the test's verdict is *signal, not noise* — rubber-stamping the verdict discards the learning. Mitigation: on disagreement, re-examine the estimates before acting.

## Contract

### Preconditions
A specific task is in hand. The operator (or routing layer) can honestly estimate the task's four properties — size, independence, separation of concerns, and checkability.

### Invariants
The verdict is exactly one of four classes — chat / single agent with a goal / team of agents / human (no AI). A `team of agents` verdict is never issued without a named cheap checker satisfying the checkability estimate (fan-out with no verifier fails estimate 4). The four estimates describe the *work*, not the current tools, so the test survives tool churn. Size estimates are re-anchored to current context limits rather than treated as fixed.

### Governance
Advisory. The human — or the orchestrator embedding the test — owns the routing decision; the test never dispatches work itself. The two money dials (how often the task recurs, what a good answer is worth) sharpen the verdict but never override the anti-delegation edge: genuine judgment calls stay human.

### Recovery
If instinct disagrees with the verdict, treat the disagreement as signal — re-examine the estimates rather than rubber-stamping the verdict. If parts assumed independent turn out to share hidden state, re-estimate independence and step down from `team` to `single agent` or re-partition the work. If checking an answer is expensive, do not route to a `team` (extra attempts top out fast) — keep it single-agent or human. Re-anchor size estimates as model context limits grow.
