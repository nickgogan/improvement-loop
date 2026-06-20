---
notion_id: 30f1e08b-9b34-8129-833d-ce061685c815
title: "The Front Desk"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# The Front Desk

> **For agents:** The Front Desk is the CONTROL stage orchestrator. Before taking any action on an item, check the Front Desk logic: Is it triaged? Is it assigned? Is it prioritized? If not, run the triage sequence below before proceeding. The Front Desk is always-on for agents — you don't wait for a human ritual to process items.

---

## Core Decision

**DD-15:** The Front Desk is the CONTROL stage orchestrator — the active decision-making layer between capture and execution. It operates in hybrid mode: always-on for agents, PEA ritual-based for humans. Starts narrow (inbound triage) in WS2, expands to full coordination hub in WS3-WS4.

---

## What Is the Front Desk?

The three named components of the system map directly to ICOR stages:

| ICOR Stage | Component | Question It Answers | Action |
|-----------|-----------|-------------------|--------|
| **INPUT** | The Capturing Beast | Should this enter the system? | Filter, route personal vs. household |
| **CONTROL** | **The Front Desk** | Now that it's in, what happens to it? | Triage, prioritize, assign, coordinate |
| **OUTPUT** | The Execution Beast | How does the work get structured and done? | Goals → Projects → Tasks, PEA rhythm |
| **REFINE** | (System Reviews) | Is the system working? What needs to change? | Retrospectives, metric reviews, adjustments |

The Front Desk is **active, not passive**. The Command Center (DD-13) is a view layer — it shows you the state of the system. The Front Desk is an action layer — it makes decisions about what happens next.

> **Metaphor:** Think of a hotel. The Command Center is the lobby display board showing today's events. The Front Desk is the concierge who greets you, figures out what you need, and dispatches the right person to help.

---

## Operating Mode: Hybrid

The Front Desk operates differently for agents and humans:

| Actor | Mode | When | How |
|-------|------|------|-----|
| **Agents** | Always-on | Before any action on an untriaged item | Run the Triage Sequence (below) automatically. No human needed for routine decisions. |
| **Humans** | PEA ritual | Daily Plan (morning), Weekly Review, Quarterly Alignment | Review what agents have triaged. Override, reprioritize, or handle items that require human judgment. |

> **For agents:** You are expected to triage items proactively. If you encounter an item in Inbox status with no Owner, Priority, or Project assignment, run the Triage Sequence. Do not wait for a human to tell you. Flag items for human review only when the decision is ambiguous or high-stakes.

---

## Amendment Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-02-28 | Clarified: Step 2 now explicitly documents Assignee-setting alongside Owner per DD-12 two-layer model. Added note about Assignee lifecycle timing. | Formalizing that triage is where Assignee MAY be set for household items, but is NOT required at this stage. See DD-12 amendment. |
| 2026-03-17 | Updated Step 1 (Classify) Workstream row to specify that items should attach to an existing Ongoing project or flag for new Workstream creation per DD-26. Added Workstream routing note to Step 4 (Route) specifying Project relation linking for Workstream items. | Gap Resolution Decision Log — 2026-03-17 session. |

> **Note on Owner vs. Assignee at triage time:** Per DD-12's two-layer model, Owner is ALWAYS set during triage (Step 2). Assignee is OPTIONALLY set — for household items where the Area Lead or responsible person is obvious. If Assignee is not set at triage, it gets set later during the Family Meeting (DD-24 Phase 5) or daily planning. For personal items, Assignee is typically left empty at triage (the Owner is implicitly the doer until delegation occurs).

---

## The Triage Sequence

When an item arrives from the Capturing Beast (or is discovered untriaged), the Front Desk runs this sequence:

### Step 1: Classify

What kind of item is this?

| If it is... | Then... |
|-------------|---------|
| Actionable, single step, <=15 min | Mark as **Speedy**. Assign to next Speedy batch. |
| Actionable, single step, >15 min | Create **Task**. Proceed to Step 2. |
| Actionable, multi-step, has end date | Create **Project**. Proceed to Step 2. |
| Actionable, multi-step, no end date | Attach to existing **Workstream** (Ongoing project) as a Task or Operation. If no matching Workstream exists, flag for human review — a new Workstream may need to be created (see DD-26 Ongoing Lifecycle). |
| Reference / knowledge | Route to appropriate **Area** page or Notes database. Exit triage. |
| Not actionable, not reference | **Trash** or **Someday/Maybe**. Exit triage. |

### Step 2: Assign Owner

Who owns this?

| Signal | Assignment |
|--------|-----------|
| Item is clearly personal (Nick's career, John's health, etc.) | Assign to that person |
| Item falls under an Area with a designated Lead | Assign to the Lead |
| Item is household-wide (finances, apartment, shared projects) | Assign Owner = Household; Assignee = Area Lead (or flag for discussion) |
| Unclear | Flag for human review at next Daily Plan |

### Step 3: Prioritize

How urgent/important is this?

| Priority | Criteria | Response Time |
|----------|----------|---------------|
| **P1 — Urgent** | Deadline within 48 hours, or blocking other work | Today |
| **P2 — Important** | Tied to an active OKR or Key Result | This week |
| **P3 — Standard** | Useful but not time-sensitive | This sprint/cycle |
| **P4 — Low** | Nice to have, no deadline pressure | When bandwidth allows |

### Step 4: Route

Where does this live?

| Item Type | Destination |
|-----------|-------------|
| Task | Tasks database → link to Project if applicable → set Due Date |
| Project | Projects database → link to Goal/Workstream → set Status = Planned |
| Reference Note | Notes database → link to Area Tag → set Type |
| Speedy | Tasks database → Smart List = Next → flag as Speedy |

> **Workstream routing note:** When routing a Task or Operation to a Workstream, always link it via the Project relation to the Workstream's Ongoing project entry in the Projects DB. This ensures the item appears in the Workstream's task list and is visible during Family Meeting Phase 3 Workstream pulse reviews. If the item belongs to an Area that has an active Workstream, prefer linking to that Workstream over leaving the item as a standalone task.

### Step 5: Log

Record the triage decision in the System Log (DD-11) for audit trail.

---

## Human Ritual Integration

The Front Desk plugs into existing PEA cadences:

| Ritual | Front Desk Activity | Cadence |
|--------|-------------------|---------|
| **Daily Plan** | Review overnight agent triage decisions. Override if needed. Process any items flagged for human review. Set today's priorities. | Every morning |
| **Weekly Review** | Audit the full Inbox. Verify no items are stuck. Review agent triage accuracy. Rebalance assignments between Nick and John if needed. | Weekly |
| **Family Meeting** | Review household-level items together. Discuss any items flagged as "needs partner input." Align on priorities for the coming week. | Weekly (DD-08) |
| **Quarterly Alignment** | Review Front Desk effectiveness metrics. Adjust triage rules. Update Area Lead assignments. Tune priority criteria against OKR progress. | Quarterly |

---

## WS2 Scope (Narrow Launch)

## Deferred Enrichment

The slackbot supports a two-phase capture pattern for moments when the user can't engage with follow-up questions (fleeting thoughts, mid-meeting ideas):

**How it works:**

1. User sends a raw message to the bot
2. Bot acknowledges and asks enrichment questions (type, area, priority, context)
3. **If user responds** → normal intake, item fully classified
4. **If user says "later"** → immediate deferral; item parked in inbox with raw text only; enrichment reminder queued
5. **If user doesn't respond within the timeout** → same as "later"; bot stops waiting and queues the reminder

**Configuration (per person):**

- **Enrichment timeout** — how long the bot waits for a response before auto-deferring (default: 30 minutes)
- **Reminder timing** — when the bot circles back to ask enrichment questions (options: 1 hour, end of day, next morning)

**Graceful degradation:** If the user never responds to the enrichment reminder either, the item remains in the inbox with raw text and gets processed at the next triage cadence (DD-28) with whatever context is available. Nothing gets lost.

For WS2, the Front Desk handles **inbound triage only**:

- Classify incoming items (Step 1)
- Assign Owner (Step 2)
- Set Priority (Step 3)
- Route to correct database/location (Step 4)
- Log decisions (Step 5)

**Not in WS2 scope** (deferred to WS3-WS4):

- Outbound notifications to partners
- Workload balancing / reassignment suggestions
- Escalation automation (overdue items, stuck projects)
- Cross-partner coordination protocols
- Agent-to-agent handoff orchestration

---

## Evolution Roadmap

| Workstream | Front Desk Capability |
|-----------|----------------------|
| **WS2** | Inbound triage: classify, assign, prioritize, route, log. Agent always-on mode. Human PEA rituals. |
| **WS3** | Add escalation rules: items untriaged >24h get flagged. Overdue tasks surface automatically. Weekly triage accuracy report. |
| **WS4** | Partner notifications: "John, Nick assigned you a P2 task in Kitchen Renovation." Workload dashboard showing each partner's current load. |
| **WS5** | Intelligent routing: agent suggests Owner based on historical patterns, current workload, and Area expertise. Human approves or overrides. |
| **WS6** | Full coordination hub: agent-to-agent handoffs, cross-project dependency tracking, proactive rebalancing suggestions. |

---

## Interaction with Other Design Decisions

- **DD-10 (Capturing Beast):** Front Desk receives items that pass the Capturing Beast's 3-lens filter. The Beast decides what gets *in*; the Front Desk decides what happens *next*.
- **DD-06 (Output Elements):** Front Desk classifies items into the Output Elements taxonomy (Goal/Project/Workstream/Operation/Task/Speedy).
- **DD-09 (Hybrid OKRs):** Priority scoring (Step 3) references active OKRs and Key Results.
- **DD-11 (System Log):** Every triage decision is logged for audit and pattern analysis.
- **DD-13 (Household Teamspace):** Front Desk operates within the Household Teamspace's Operational Databases.
- **DD-14 (UB3 Integration):** Triage uses UB3's existing database properties (Status, Priority, Smart List, Assignee, Owner).
- **DD-05 (GTD-Lite):** The Triage Sequence is essentially GTD's "What is it?" decision tree, formalized and made agent-executable.

---

## Companion Diagrams

- `DecisionLoop.png` — John Boyd's original OODA Loop (Observe → Orient → Decide → Act). The Front Desk's triage sequence is a formalized version of this loop, with Orient/Decide happening in Steps 1-3 and Act in Steps 4-5.
- `D2_ICOR_Flow_Integration.svg` — Shows the Front Desk's position in the overall information flow, between the Capturing Beast (Input) and the Execution Beast (Output).
