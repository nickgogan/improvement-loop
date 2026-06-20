---
notion_id: 3101e08b-9b34-81a3-b840-cc6e1f1a80e4
title: "Operational Concepts"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Operational Concepts

> **For agents:** This page defines the vocabulary for how recurring work is structured, documented, and monitored. DD-06 defines *what work is* (the Output Elements hierarchy: Goal → Project → Workstream → Operation → Task/Speedy). This page defines *how recurring work is patterned*. When the user asks about routines, processes, standards, or SOPs, reference this page. When building monitoring widgets (Standards Check, System Integrity), use these definitions to determine what gets tracked and how.

## Design Decision

**DD-20:** The Operational Concepts hierarchy defines how recurring work is structured, documented, and monitored. Six concepts form a layered vocabulary. DD-06 defines what work IS; DD-20 defines how recurring work is PATTERNED.

---

## Two Complementary Hierarchies

The system has two distinct but connected hierarchies for understanding work:

| Hierarchy | Defined In | Answers | Concepts |
|-----------|-----------|---------|----------|
| **Output Elements** (DD-06) | The Execution Beast | "What is this work?" | Goal → Project → Task (deliverable) · Goal → Workstream → Operation (process) |
| **Operational Patterns** (DD-20) | This page | "How is this recurring work structured and monitored?" | Cadence → Routine → Standard / Process → Procedure → SOP |

They connect at the **Operation** level: an Operation (DD-06) is a recurring task within a Workstream — the process-oriented equivalent of a Task within a Project. An Operational Pattern (DD-20) describes how that recurring work is organized into rhythms, bundles, and documented instructions.

### The Dual Hierarchy (DD-06, amended 2026-03-01)

DD-06 now defines two parallel structures sharing the same Goal layer:

| Mode | Hierarchy | Progress Tracking |
|------|-----------|-------------------|
| **Deliverable** (finite work) | Goal → Project → Task | Drives Goal progress (completed / total) |
| **Process** (ongoing work) | Goal → Workstream → Operation | Alignment/visibility only — **excluded from Goal progress formula** |

Workstreams connect to Goals to answer "what ongoing work supports this Goal?" but never complete, so they don't contribute to the progress percentage. Workstream health is monitored qualitatively via the weekly Family Meeting (Phase 3 Workstream pulse), not via automated formulas.

### Project → Workstream relation (deferred)

Can a Project report into a Workstream? Conceptually yes — Labor sometimes reveals the need for Work (e.g., the "Home Maintenance" Workstream discovers a need for a "Renovate Bathroom" Project). However, both already connect to the same **Area** (Tag), which provides sufficient grouping. A direct Project → Workstream database relation is **deferred** until the Family Meeting Workstream pulse reveals a recurring need for it.

### Area pages as organizational hubs

Each Area (Tag) page serves as the single place to see everything happening in a domain — functioning like a Jira Epic board but without yearly duplication. The Area page surfaces both hierarchies side by side: active **Workstreams** (Labor — what we're sustaining), active **Projects** (Work — what we're building), connected **Goals** (the strategic why), and recent **Operations/Tasks** (atomic work). A **"This Year" date filter** provides yearly scoping. See DD-23 for the full Area page view pattern.

### Philosophical grounding: Arendt's Labor

The entire Operational Concepts hierarchy — Cadence, Routine, Standard, Process, Procedure, SOP — describes the structure of what Hannah Arendt called **labor** in *The Human Condition*: cyclical, never-ending activity that sustains life. The output is consumed and the process repeats. Cooking, cleaning, bill-paying, exercising — this is labor. It contrasts with **work** (Projects/Tasks in DD-06), which produces durable artifacts with a beginning and end. The system respects this distinction architecturally: labor (Workstreams/Operations) and work (Projects/Tasks) form parallel hierarchies with different rhythms, different success criteria, and different tracking mechanisms. See DD-06 "Philosophical grounding: Arendt's Labor vs. Work" for the full framing.

---

## The Operational Concepts Hierarchy

### Tier 1: Cadence

**Definition:** A recurring time rhythm at which activities happen.

**Examples:** Daily, weekly, bi-weekly, monthly, quarterly, annual.

**Already used in:** The Compass review cadences (Daily Pulse, Weekly Family Meeting, Monthly Audit, Quarterly Deep Review, Annual Reset), PEA rhythm (Plan-Execute-Align at daily/weekly/quarterly/annual scales).

**Key property:** Cadences are not "things" in the database — they're a classification applied to other concepts. A Standard has a cadence. A Routine happens on a cadence. A review follows a cadence.

---

### Tier 2: Routine

**Definition:** A bundle of related activities that happen together on a cadence. A Routine groups multiple Operations, Tasks, and/or Standards into a coherent sequence.

**Examples:**

| Routine | Cadence | Contains | Owner |
|---------|---------|----------|-------|
| Morning Planning | Daily | Review calendar, check inbox, select today's tasks, journal intention | Personal |
| End-of-Day Wrap Up | Daily | Review completions, log blockers, prep tomorrow, journal reflection | Personal |
| Weekly Review | Weekly | Clear inbox, review overdue, assess weekly progress, plan next week | Personal |
| Family Meeting | Weekly | Household priorities, calendar coordination, equity check, shared planning | Household |
| Monthly Audit | Monthly | Review Standards adherence, assess Area health, check System Integrity, review budget | Household |
| Sunday Meal Prep | Weekly | Plan meals, check pantry, create grocery list, prep ingredients | Household |

**Relationship to DD-06:** A Routine is not a new work type — it's a *pattern* applied to existing work types. A Routine bundles Operations and Tasks into a sequence. In UB3, a Routine could be modeled as a Project with Status = Ongoing (Workstream) that contains recurring Tasks.

**Relationship to The Compass (DD-18):** Every Compass review cadence is a Routine. The Daily Pulse is a Routine. The Weekly Family Meeting is a Routine. The Compass defines *when and why* these happen; Routines define *what they contain*.

---

### Tier 3a: Standard

**Definition:** A specific, measurable recurring commitment with an explicit adherence target. A Standard says: "We commit to doing X at frequency Y, and we'll monitor whether we're hitting that target."

**Distinction from Operation:** An Operation (DD-06) is any recurring task. A Standard is an Operation that has been *elevated* — it has an explicit target and is actively monitored. Not every Operation is a Standard. "Take out trash weekly" is an Operation. "Go to gym 3x/week with 80% adherence target" is a Standard.

**Examples:**

| Standard | Owner | Cadence | Target | Metric |
|----------|-------|---------|--------|--------|
| Gym sessions | Personal | 3x/week | >=80% adherence | Sessions completed / sessions target |
| Quarterly deep clean | Household | 1x/quarter | 100% adherence | Completed yes/no |
| Monthly budget review | Household | 1x/month | 100% adherence | Completed yes/no |
| Daily reading | Personal | 30 min/day | >=70% of days | Days completed / days in period |
| Date night | Household | 2x/month | >=75% adherence | Dates completed / target |
| Weekly grocery run | Household | 1x/week | >=90% adherence | Completed count / weeks |
| Weekly review completion | Personal | 1x/week | 100% adherence | Completed yes/no (feeds Compass Review Streak vital sign) |

**Notion implementation:** Standards are recurring Tasks in the Tasks database with Label = "Standard". The recurring task mechanism handles frequency. The "Standard" label enables filtered views for the Standards Check widget. Adherence is calculated as: completed instances / expected instances over a time period.

**Monitoring (deferred):** The Standards Check widget (DD-19) and adherence formulas are a **potential future enhancement**. For now, Workstream health is monitored qualitatively during the weekly Family Meeting (Phase 3 Workstream pulse). Nick and JR check in on each active Workstream — healthy, needs attention, or adjusting — and capture notes in the meeting template. This lightweight approach avoids building adherence tracking infrastructure before the system is mature enough to benefit from it. If quantitative tracking becomes desirable later, Standards can be implemented by adding a "Standard" Label to recurring Tasks with adherence targets.

---

### Tier 3b: Process

**Definition:** A defined, repeatable sequence of steps that transforms an input into an output. A Process describes *how* something gets done, not *what* gets done.

**Distinction from Routine:** A Routine bundles *what* happens together. A Process describes *how* each thing is done. A Routine may contain multiple Processes. The "Weekly Review" Routine includes the "Inbox Processing" Process, the "Overdue Triage" Process, and the "Next Week Planning" Process.

**Examples of Processes already in the system:**

| Process | ICOR Stage | Input | Output | Defined In |
|---------|-----------|-------|--------|-----------|
| Triage Sequence | Control | Unprocessed inbox item | Classified, assigned, prioritized, routed item | The Front Desk (DD-15) |
| 3-Lens Capture Filter | Input | Incoming information | Accepted or rejected input | The Capturing Beast (DD-10) |
| PEA Cycle | Output | Prioritized backlog | Completed work + alignment feedback | The Execution Beast (DD-06) |
| OKR Scoring | Refine | Quarter's Key Results | Scored outcomes + lessons learned | The Compass (DD-18) |
| Emergency Response | Refine | Threshold breach | Corrective action taken | The Compass (DD-18) |

**Key insight:** We already have several Processes defined in the Architecture — they just aren't labeled as "Processes" yet. DD-20 gives them that formal label and establishes the pattern for defining new ones.

**Notion implementation:** Processes don't need their own database. They're documented as content within Architecture pages (for system-level Processes) or as Notes with Type = Reference (for operational Processes). The important thing is that each Process has a clear input, output, and sequence of steps.

---

### Tier 4: Procedure

**Definition:** The documented, step-by-step instructions for executing a Process. If a Process says "triage incoming items," the Procedure says "Step 1: Check if it's actionable. Step 2: If yes, assign an Owner. Step 3: Set priority using the P1-P4 scale. Step 4: Route to the appropriate database..."

**Distinction from Process:** A Process is the *concept* — what happens and why. A Procedure is the *documentation* — how to actually do it, step by step. You can understand a Process without reading the Procedure. You need the Procedure to execute it consistently.

**Examples:**

| Process | Procedure Would Document | Who Uses It |
|---------|-------------------------|-------------|
| Triage Sequence | Exact steps for classifying, assigning, prioritizing, routing, and logging each item type | Agents + humans during weekly review |
| Weekly Review | Checklist for Clear & Reset, Reflect & Set Intent, Plan the Week with specific views to check | Each partner during personal review |
| Family Meeting | Agenda template, equity check steps, calendar coordination protocol, decision recording format | Both partners during weekly meeting |
| Quarterly Deep Review | OKR scoring methodology, Area health assessment checklist, Standard adherence review steps, next quarter planning framework | Both partners during quarterly review |
| New Project Setup | Steps for creating a Project entry, linking to Goal, assigning Owner, setting up initial Tasks, choosing Area | Agents + humans |

**Notion implementation:** Procedures are documented as Notes (Type = Reference) or as template content within the relevant cockpit page. For example, My Week's "Clear & Reset" section could contain or link to the Weekly Review Procedure.

**When to create Procedures:** Not every Process needs a written Procedure immediately. Start with Procedures for Processes that both partners need to execute consistently (Family Meeting, Weekly Review) or that agents need to follow (Triage Sequence). Add Procedures for other Processes as needed.

---

### Tier 5: SOP (Standard Operating Procedure)

**Definition:** A Procedure that has been formalized as **binding and authoritative**. An SOP is the "this is how we always do it" version of a Procedure. It's been tested, refined, and agreed upon by both partners.

**Distinction from Procedure:** A Procedure can be informal, evolving, or a first draft. An SOP has been reviewed, approved, and is considered the canonical way to do something. Changing an SOP requires explicit agreement (similar to how Design Decisions are binding).

**Examples of potential SOPs:**

- How to process the Family Meeting agenda
- How to onboard a new PARA Area
- How to respond to a financial emergency
- How to hand off Area stewardship between partners
- How to set up quarterly OKRs

**Notion implementation:** SOPs are documented as Architecture pages or Notes with a special callout indicating their binding status. They reference the Process they formalize and include a version date.

**Evolution path:** Process → Procedure (documented) → SOP (binding). Not every Process becomes an SOP. Most will stay as Procedures or even undocumented Processes until they need formalization.

---

### System-Level Concept: Workflow

**Definition:** The system-level path that items take as they move across multiple Processes and ICOR stages. A Workflow describes the end-to-end journey, not the individual steps.

**Examples:**

| Workflow | Path | Processes Involved |
|----------|------|--------------------|
| Capture-to-Action | Information enters → gets filtered → gets triaged → gets executed → gets reviewed | 3-Lens Filter → Triage Sequence → PEA Cycle → Review |
| Goal-to-Outcome | Yearly Objective set → Key Results defined → Projects created → Tasks executed → Progress reviewed | OKR Setting → Project Setup → PEA Cycle → OKR Scoring |
| Knowledge Formation | Information captured → organized → distilled → expressed | CODE stages: Capture → Organize → Distill → Express |
| System Improvement | Vital signs monitored → issues detected → response triggered → fix applied → verified | Compass Monitoring → Emergency Response → System Integrity Check |

**Key insight:** Workflows are emergent — they describe how the ICOR pipeline moves items through the system. You don't "build" a Workflow; you build the Processes and connect them. The Workflow is the resulting path. Workflow health is monitored by checking that items are flowing (not stuck, not lost, not bottlenecked).

---

## How the Concepts Connect

```
Cadence (time rhythm)
  +-- Routine (bundle of activities on that cadence)
        +-- Standard (measurable commitment with adherence target)
        |     +-- Tracked as: recurring Task with Label = "Standard"
        |     +-- Monitored via: Standards Check widget (DD-19)
        +-- Process (repeatable sequence of steps)
              +-- Procedure (documented instructions)
                    +-- SOP (binding, authoritative Procedure)

Workflow = the system-level path across multiple Processes
```

**Concrete example:**

- **Cadence:** Weekly
- **Routine:** Family Meeting
- **Standards within it:** "Hold Family Meeting every week" (adherence target: 100%)
- **Processes within it:** Calendar Coordination, Equity Check, Shared Planning
- **Procedure:** The documented Family Meeting agenda and facilitation guide
- **SOP:** (future) The binding, finalized version of that Procedure
- **Workflow it feeds:** The broader Household Coordination workflow

---

## Widget Implications

This hierarchy directly informs what the Command Center widgets (DD-19) track:

| Widget | Operational Concept Tracked | Cockpit Location |
|--------|---------------------------|------------------|
| **Standards Check** | Standards — adherence rate for each Standard over the period. **Deferred** — Workstream health monitored via Family Meeting Phase 3 instead. | My Quarter, My Week (future) |
| **Goal Cascade Progress** | Workflow — how the Goal-to-Outcome workflow is progressing | My Quarter, My Year |
| **Vital Signs Strip** | Multiple — Review Streak tracks Routine adherence, Inbox Zero Delta tracks Workflow throughput | Mission Control |
| **System Diagnostics** | Workflow health — are items flowing correctly through the system? | Mission Control (link) |
| **Equity Check** | Standards + Routines — are household commitments balanced between partners? | My Week |
| **Review Cadence templates** | Routines — structured checklists for each Compass review cadence | All cockpits |

---

## Interaction with Existing Design Decisions

| DD | Relationship |
|----|-------------|
| DD-06 | Output Elements define *what work is* through two parallel hierarchies: Deliverable (Goal → Project → Task) and Process (Goal → Workstream → Operation). Operational Concepts define *how recurring work is patterned*. Operations (DD-06) are the bridge — they're the recurring tasks within Workstreams that can optionally be elevated to Standards (DD-20, deferred). |
| DD-08 | Family Meeting is both a Routine (DD-20) and a CONTROL ritual (DD-08). DD-20 defines its structural components; DD-08 defines its governance role. |
| DD-15 | The Front Desk's Triage Sequence is a Process (DD-20). When we document the step-by-step triage instructions, that becomes a Procedure. |
| DD-18 | The Compass's five review cadences are Routines (DD-20) that happen on Cadences. Emergency Protocols are Processes. Some Standards feed Compass vital signs directly. |
| DD-19 | The Command Center's Standards Check widget monitors Standards. The System Diagnostics page monitors Workflow health. Review cadence templates structure Routines. |

---

## What Gets Built Now vs. Later

| Now (DD-20 scope) | Later (workflow design phase) |
|--------------------|------------------------------|
| Define the vocabulary and hierarchy | Design the actual Procedures for each Process |
| Establish the dual hierarchy parallel (Deliverable vs. Process) and Family Meeting Workstream pulse as the monitoring mechanism | Build Standards tracking infrastructure (Label = "Standard", adherence formulas, Standards Check widget). Identify which Operations should be elevated to Standards |
| Name the existing Processes (Triage, PEA, 3-Lens, etc.) | Write the Procedures for each Process |
| Define widget connection points | Build the actual widgets and views |
| Classify which concepts are Routines vs. Standards vs. Processes | Determine which Procedures should become SOPs |
| Inform template metadata requirements | Design the templates themselves |

---

## Template Metadata Implications

When we eventually design templates for Notes, Tasks, Projects, etc., the Operational Concepts hierarchy tells us what metadata those templates need:

- **Task templates** for Standards need: the "Standard" Label, recurrence settings, and a way to track adherence
- **Note templates** for Procedures need: Process name reference, step numbering, input/output fields, and a binding status indicator (Procedure vs. SOP)
- **Routine templates** (for review cockpits) need: cadence, checklist of component activities, links to relevant views, and completion tracking
- **Project templates** for Workstreams that contain Standards need: linked Standards list and adherence dashboard

This is why we define the vocabulary first — the template metadata falls out naturally from understanding what these concepts are.

---

*DD-06 tells you what the work is (through two parallel hierarchies: Deliverable and Process). DD-20 tells you how recurring work is organized into rhythms, bundles, and documented instructions. Together, they give the system a complete vocabulary for both one-time and ongoing work.*

*Updated 2026-03-01. Standard tracking deferred — Family Meeting Phase 3 Workstream pulse serves as interim monitoring mechanism. Project → Workstream relation deferred — Area tag provides sufficient grouping. Area pages serve as organizational hubs showing both hierarchies (see DD-23).*
