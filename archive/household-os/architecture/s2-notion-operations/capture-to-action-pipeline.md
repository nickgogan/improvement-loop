---
notion_id: 3101e08b-9b34-8129-a384-cd04115986fa
title: "Capture-to-Action Pipeline"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Capture-to-Action Pipeline

> **For agents:** This page defines the end-to-end flow of how information enters and moves through the Household Operating System. When processing captured items, follow this pipeline: Front Desk intake → Inbox landing → Human processing → Routing. Do not skip phases or conflate intake with processing.

---

## Core Decision

**DD-21:** The Capture-to-Action Pipeline defines the complete workflow from item capture through processing to final destination. The Front Desk (slackbot) handles intake by applying the Capturing Beast's 3-lens filter and depositing items into the correct inbox. Operators (Nick, JR, or jointly as Household) process their inboxes at appropriate cadences, routing items to one of five destinations.

---

## Pipeline Overview

The pipeline has three distinct phases, each with a clear owner:

| Phase | Component | Owner | Action |
|-------|-----------|-------|--------|
| **1. Intake** | Front Desk (slackbot) | Automated | Apply 3-lens filter, classify, deposit into correct inbox |
| **2. Landing** | Dual Inboxes | System | Items wait in Task Inbox or Note Inbox until processed |
| **3. Processing** | Human Triage | Nick, JR, or Household | Review, enrich metadata, route to final destination |

---

## Phase 1: Intake (The Front Desk Slackbot)

The Front Desk is the intake mechanism — a slackbot that receives items from any channel and deposits them into the system. It is informed by the Capturing Beast's design principles.

### How It Works

1. **Item arrives** — User sends a message, link, file, photo, voice memo, or forwarded email to the slackbot
2. **3-Lens Filter** — The bot applies the Capturing Beast's three lenses (Current Projects, Key Elements/Areas, Active Topics/Resources) to determine if the item should enter the system. If none match, the bot confirms the user wants to discard it.
3. **Quick Classification** — The bot asks two fast questions:
   - *"What's this about?"* → Maps to an Area (or Project if obvious)
   - *"Personal or Household?"* → Sets the Owner property
4. **Inbox Routing** — Based on the item's nature:
   - Actionable items → **Task Inbox** (new entry in Tasks database, Status = Inbox)
   - Informational items → **Note Inbox** (new entry in Notes database, Status = Inbox)
5. **Audit Log** — The bot logs every intake decision in the System Log (DD-11)

### The Capturing Beast's Role

The Capturing Beast (DD-10) is not a separate system component — it is the *design philosophy* that informs how the Front Desk slackbot behaves. Specifically:

- The 3-lens filter logic is encoded into the bot's classification rules
- The personal/household routing decision happens at capture time, not later
- The "discard by default" principle ensures the bot asks before accepting ambiguous items
- The bot's behavior should make the user feel like the Capturing Beast is actually filtering — saying no to noise, fast-tracking project-relevant items

### Intake Channels

All channels funnel through the same slackbot interface:

| Channel | How It Reaches the Bot |
|---------|----------------------|
| Manual message | User types directly to the bot in Slack |
| Forwarded email | User forwards to a dedicated email that posts to the bot |
| Web clip | Browser extension sends to bot via Slack integration |
| Voice memo | User sends audio message; bot transcribes and processes |
| Photo/file | User shares directly; bot prompts for classification |
| Notion Quick Capture | Existing UB3 Quick Capture page remains as an alternative direct-entry path (bypasses bot, items land directly in inboxes) |

---

## Phase 2: Landing (Dual Inboxes)

Items deposited by the Front Desk land in one of two inboxes, following the UB3 GTD pattern:

| Inbox | Database | Filter | Purpose |
|-------|----------|--------|---------|
| **Task Inbox** | Tasks | Status = Inbox | Actionable items awaiting processing |
| **Note Inbox** | Notes | Status = Inbox | Informational items awaiting processing |

These are not separate databases — they are **filtered views** of the existing UB3 Tasks and Notes databases, visible on the Quick Capture page. The Front Desk slackbot creates entries directly in these databases with Status = Inbox.

### Inbox Health

Inboxes should trend toward zero. The Compass (DD-18) monitors **Inbox Zero Delta** as one of its six vital signs:

- **Green:** Both inboxes at zero
- **Yellow:** Items sitting >24 hours
- **Red:** Items sitting >72 hours

---

## Phase 3: Processing (Human Triage)

Processing is a **human activity**. Operators work through their inboxes at cadences appropriate to each inbox type.

### Processing Cadence

| Inbox | Recommended Cadence | During Which Ritual |
|-------|--------------------|--------------------|
| Task Inbox | Daily | Daily Plan (morning PEA) |
| Note Inbox | 2-3x per week | Weekly Review or as-needed |

### The Processing Decision Tree

For each item in an inbox, the operator asks a sequence of routing questions:

```
Item in Inbox
|
+-- Is this trash? -----------------> DELETE (remove from database)
|
+-- Is this a shared file ----------> GOOGLE DRIVE
|  (document, receipt, photo)?        Upload to Area folder in Drive
|                                     Create Drive Index entry (DD-22)
|
+-- Does this need deep ------------> HEPTABASE
|  thinking/synthesis?                Export/recreate in Heptabase
|                                     Create Reference Note stub (DD-22)
|
+-- Is this actionable? ------------> TASK (enrich and execute)
|                                     Apply full Front Desk triage:
|                                     Classify -> Assign -> Prioritize -> Route
|                                     (DD-15 Triage Sequence Steps 1-5)
|
+-- Is this reference/ ------------> NOTE (enrich and file)
   knowledge?                         Set Type, Area, Tags
                                      Link to relevant Project if applicable
```

### Five Routing Destinations

| # | Destination | What Goes There | Notion Artifact | Enrichment Needed |
|---|-------------|----------------|-----------------|-------------------|
| 1 | **Tasks** | Actionable items | Task entry (existing) | Owner, Area, Priority, Due Date, Project link |
| 2 | **Notes** | Reference, knowledge, meeting notes | Note entry (existing) | Type, Area, Tags |
| 3 | **Heptabase** | Deep synthesis, complex thinking, evergreen notes | Reference Note stub in Notes DB | Type = Reference, Tag = Heptabase, URL to Heptabase card |
| 4 | **Google Drive** | Shared files, documents, receipts, photos | Drive Index entry (DD-22) | Area, File Type, Drive URL |
| 5 | **Trash** | Noise, duplicates, outdated items | Deleted from database | None |

### Enrichment

Routing alone isn't enough — items need metadata to be useful in the system. The Front Desk's Triage Sequence (DD-15, Steps 1-5) provides the enrichment framework for actionable items. For reference items, minimum enrichment is Type + Area.

---

## Relationship to Existing Components

| Component | Role in Pipeline | Reference |
|-----------|-----------------|-----------|
| **The Capturing Beast** | Design philosophy informing the Front Desk's filter logic | DD-10 |
| **The Front Desk** | Intake mechanism (slackbot) + triage sequence used during processing | DD-15 |
| **The Execution Beast** | Receives processed Tasks and Projects for execution | DD-06 |
| **The Compass** | Monitors inbox health (Inbox Zero Delta) and processing cadence | DD-18 |
| **The Command Center** | Surfaces inbox counts and processing status in Mission Control | DD-19 |
| **External Content Index** | Defines how Heptabase and Google Drive items maintain Notion backlinks | DD-22 |
| **Quick Capture (UB3)** | Alternative direct-entry path; hosts the dual inbox views | UB3 existing |

---

## What This Resolves

- **IB-11** (Front Desk triage workflow) — Triage is fundamentally human judgment applied during processing, assisted by the Front Desk's Triage Sequence. Agents can pre-triage in always-on mode (DD-15), but final routing decisions for ambiguous items require human review.
- **IB-22** (Capturing Beast intake experience) — The Front Desk slackbot IS the intake experience. It applies the Capturing Beast's principles through a conversational Slack interface. Notion Quick Capture remains as an alternative direct-entry path.

---

## WS2 vs Later Scope

| WS2 (Now) | WS3+ (Later) |
|-----------|-------------|
| Slackbot receives and classifies items | Slackbot learns classification patterns |
| Manual 3-lens filter questions | Auto-detection of Project/Area relevance |
| Two inboxes (Task + Note) | Smart routing suggestions |
| Human processing at cadences | Agent pre-processing with human approval |
| Five routing destinations defined | Automated file upload to Drive |
| Basic audit logging | Triage accuracy analytics |

---

## Design Decision Interactions

- **DD-10** — Capturing Beast's 3-lens filter and personal/household routing, encoded into the Front Desk slackbot
- **DD-11** — System Log records every intake and processing decision
- **DD-13** — Household Teamspace houses the operational databases where items land
- **DD-14** — UB3 databases (Tasks, Notes) provide the inbox infrastructure
- **DD-15** — Front Desk Triage Sequence provides the enrichment framework during processing
- **DD-18** — The Compass monitors inbox health and processing cadence
- **DD-20** — Capture-to-Action is the first formally defined Workflow in the Operational Concepts hierarchy
- **DD-22** — External Content Index defines how items routed to Heptabase and Google Drive maintain Notion backlinks

---

*See also: The Capturing Beast · The Front Desk · The Execution Beast · The Compass · External Content Index · Vocabulary*
