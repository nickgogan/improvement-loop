---
title: "Work-Ticket Contract Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "work-ticket-contract-prompt-mode-vs-work-mode"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "handing off a unit of work between two agents, or between an agent and a human, where the receiving party cannot see the requester's chat history and needs the full context carried with the assignment"
    - "task-queue or ticket-based systems where multiple agents — possibly built on different vendors or harnesses — pick up work asynchronously off a shared queue"
    - "any workflow that currently hands off work as a free-form chat prompt but needs the result to be reviewable, acceptable, and buildable-upon later, not just a one-off answer"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a filled ticket is a coordination document; editing or discarding it costs nothing. Lifecycle-state transitions (claim, done, needs-input) are metadata changes, cheap to reverse by editing the ticket's status field."
  auditability: "high — each lifecycle transition (claim-lock, done receipt, needs-input escalation) is meant to leave a record on the ticket itself, so who worked on what, when, and with what evidence is visible by reading the ticket; auditability degrades sharply if receipts are allowed to be free-form assertions instead of verifiable evidence."
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Used in production by one practitioner running a mixed human plus multi-vendor agent team, including a demoed cross-vendor handoff where one agent authored a self-contained ticket that a different vendor's agent picked up on its own schedule. Not yet observed as a named, reusable template outside that one team's practice."
contract:
  preconditions: "Work is crossing a boundary where context cannot be assumed shared — from one agent to another agent, from an agent to a human, or from a human to an agent that will not see the requester's conversation. The work is substantial enough to need later review or audit, not a same-turn exchange. A shared store (queue, ticket tracker, or equivalent file-mediated location) exists that both the assigning and receiving party can read and write."
  invariants: "Every ticket states, at creation, all six fields: outcome, owner, sources, scope limits, definition of done, and receipt requirements. The ticket's lifecycle state is always one of a closed set (todo, working, needs-input, done) — never ambiguous or unstated. An agent claim-locks a ticket before starting work, so double-pickup is structurally prevented and progress is visible to other queue readers. Completion is always accompanied by a receipt — verifiable evidence of what was done — never accepted on the assignee's self-report alone. Ambiguity encountered mid-work always produces a needs-input transition carrying the exact blocking question, never a guess and never a silent stall."
  governance: "Owner: whoever defines the work-assignment or task-handoff schema for a given multi-agent or human-plus-agent system — e.g., the author of an orchestrator's task format, a shared task-queue schema, or a delegation protocol between agents. That owner is responsible for keeping the six required fields and three lifecycle states intact if the schema is adapted. Any downstream tooling that audits handoff schemas checks for presence of all six ticket fields and the closed lifecycle-state enum. For high-consequence or irreversible work, the definition-of-done and scope limits on a ticket should be reviewed by a human before the ticket is claimed."
  recovery: "If a claimed ticket produces no receipt and no needs-input escalation within the expected window, treat it as stalled — surface for human review rather than silently reassigning or re-claiming it. If a submitted receipt only asserts completion without verifiable evidence, treat the ticket as not-done and return it to todo pending re-work — self-report is explicitly insufficient. If needs-input tickets accumulate unanswered past a normal review cadence, that is queue rot; surface it in a periodic operational review rather than letting it sit as an invisible stall."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-orchestration"
  - "task-handoff"
  - "multi-agent-coordination"
---

# Work-Ticket Contract Template

**Source:** [[work-ticket-contract-prompt-mode-vs-work-mode]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{TICKET_ID}}` | string | Unique identifier for the ticket within the shared queue. |
| `{{OUTCOME}}` | string (result, not request) | What needs to happen, stated as a completed result — "X exists / Y is true" — not as a question or an instruction to answer something. |
| `{{OWNER}}` | string (agent or human identifier) | Who is assigned to do the work. |
| `{{SOURCES}}` | list of links/excerpts/files | The background material carried with the ticket, so the assignee doesn't need to read a chat transcript or ask for context that already exists. |
| `{{SCOPE_LIMITS}}` | string or list | What the assignee may do, and — explicitly — where it must stop. Boundaries the assignee should not cross without escalating. |
| `{{DEFINITION_OF_DONE}}` | string (acceptance condition) | The condition that, once true, means the outcome has been achieved. Should be checkable, not a vague description of effort. |
| `{{RECEIPT_REQUIREMENTS}}` | string (evidence type) | What the assignee must produce and attach when finished — e.g. a diff, a log, a screenshot, a link to the changed artifact. Not a self-report of "I did it." |
| `{{STATUS}}` | enum: `todo` \| `working` \| `needs-input` \| `done` | Current lifecycle state of the ticket. |
| `{{CLAIM_RECEIPT}}` | string, populated on claim | Who claimed the ticket and when — written the moment `{{STATUS}}` moves `todo` → `working`, so double-pickup is structurally impossible. |
| `{{DONE_RECEIPT}}` | string, populated on completion | The actual evidence satisfying `{{RECEIPT_REQUIREMENTS}}` — written the moment `{{STATUS}}` moves `working` → `done`. |
| `{{BLOCKING_QUESTION}}` | string, populated only when `{{STATUS}} == needs-input` | The exact question blocking progress. Specific enough that answering it unblocks the ticket without a follow-up round trip. |

## Body

```
TICKET: {{TICKET_ID}}
STATUS: {{STATUS}}

OUTCOME
{{OUTCOME}}

OWNER
{{OWNER}}

SOURCES
{{SOURCES}}

SCOPE LIMITS
{{SCOPE_LIMITS}}

DEFINITION OF DONE
{{DEFINITION_OF_DONE}}

RECEIPT REQUIREMENTS
{{RECEIPT_REQUIREMENTS}}

--- Lifecycle log (append-only) ---

[on claim]
CLAIM RECEIPT: {{CLAIM_RECEIPT}}

[on completion]
DONE RECEIPT: {{DONE_RECEIPT}}

[if blocked]
NEEDS-INPUT: {{BLOCKING_QUESTION}}
(ticket parks here; resumes with STATUS -> working once answered; the
question and its answer both stay on the ticket)
```

## Usage

Render this template at the moment work would otherwise be handed off as a free-form chat prompt, but the receiving party is a *different* agent, harness, or human who cannot see the requester's conversation and needs to be able to pick the work up on their own schedule — not synchronously in the same turn.

Fill all six top fields (outcome, owner, sources, scope limits, definition of done, receipt requirements) at ticket creation — before any assignee sees it. Leave the lifecycle log empty until the assignee acts:

1. **Claim.** The assignee moves `{{STATUS}}` from `todo` to `working` and writes `{{CLAIM_RECEIPT}}` in the same act. This is what makes double-pickup structurally impossible on a shared queue — a second reader sees the claim receipt and skips the ticket.
2. **Work or escalate.** The assignee does the work within `{{SCOPE_LIMITS}}`. If it hits real ambiguity — not a preference call it can reasonably make itself — it moves `{{STATUS}}` to `needs-input` and writes the exact `{{BLOCKING_QUESTION}}`, rather than guessing or silently stalling.
3. **Resolve and resume.** Whoever can answer the blocking question answers it on the ticket; `{{STATUS}}` returns to `working`; the question and its answer both remain in the lifecycle log for audit.
4. **Complete.** The assignee moves `{{STATUS}}` to `done` and writes `{{DONE_RECEIPT}}` — the actual evidence satisfying `{{RECEIPT_REQUIREMENTS}}`, not a restatement that the work is finished.

Do not accept a ticket as done without a receipt, and do not treat "I did it" as a receipt.

## Variation Axis

What drives a different rendering of this template:

- **Receipt type by work class.** `{{RECEIPT_REQUIREMENTS}}` and `{{DONE_RECEIPT}}` should be typed to the kind of work — a code change might require a diff or a passing test log; a research task might require a cited excerpt; a design task might require a screenshot or a link to the rendered artifact. Free-form receipts invite contract theater (a receipt that asserts rather than proves).
- **Ticket weight by loop size.** A single-operator loop (one person, one agent, no shared queue) doesn't need the claim-lock or needs-input machinery — the simpler ancestor is a five-field assignment (goal, sources, standard, permission boundary, proof-of-done) with no lifecycle states. Reach for the full ticket only once multiple agents or people share the same queue and double-pickup or silent stalls become real risks.
- **Escalation policy per ticket class.** High-consequence or irreversible tickets can carry an explicit escalation rule (e.g., "any scope change routes to needs-input automatically") embedded alongside `{{SCOPE_LIMITS}}`; low-stakes tickets can leave escalation to the assignee's judgment.
- **Queue review cadence.** How often `needs-input` tickets are swept for staleness is a variation point independent of the ticket schema itself — a fast-moving queue needs a tighter review cadence to avoid the tickets rotting invisibly.

## Contract

### Preconditions
Work is crossing a boundary where context cannot be assumed shared — from one agent to another agent, from an agent to a human, or from a human to an agent that will not see the requester's conversation. The work is substantial enough to need later review or audit, not a same-turn exchange. A shared store (queue, ticket tracker, or equivalent file-mediated location) exists that both the assigning and receiving party can read and write.

### Invariants
Every ticket states, at creation, all six fields: outcome, owner, sources, scope limits, definition of done, and receipt requirements. The ticket's lifecycle state is always one of a closed set (todo, working, needs-input, done) — never ambiguous or unstated. An agent claim-locks a ticket before starting work, so double-pickup is structurally prevented and progress is visible to other queue readers. Completion is always accompanied by a receipt — verifiable evidence of what was done — never accepted on the assignee's self-report alone. Ambiguity encountered mid-work always produces a needs-input transition carrying the exact blocking question, never a guess and never a silent stall.

### Governance
Owner: whoever defines the work-assignment or task-handoff schema for a given multi-agent or human-plus-agent system — e.g., the author of an orchestrator's task format, a shared task-queue schema, or a delegation protocol between agents. That owner is responsible for keeping the six required fields and three lifecycle states intact if the schema is adapted. Any downstream tooling that audits handoff schemas checks for presence of all six ticket fields and the closed lifecycle-state enum. For high-consequence or irreversible work, the definition-of-done and scope limits on a ticket should be reviewed by a human before the ticket is claimed.

### Recovery
If a claimed ticket produces no receipt and no needs-input escalation within the expected window, treat it as stalled — surface for human review rather than silently reassigning or re-claiming it. If a submitted receipt only asserts completion without verifiable evidence, treat the ticket as not-done and return it to todo pending re-work — self-report is explicitly insufficient. If needs-input tickets accumulate unanswered past a normal review cadence, that is queue rot; surface it in a periodic operational review rather than letting it sit as an invisible stall.
