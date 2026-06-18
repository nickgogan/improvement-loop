---
notion_id: 30f1e08b-9b34-81f1-bcd1-dcd35f77594c
title: "UB3 Integration Map"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# UB3 Integration Map

> **For agents:** This page maps Ultimate Brain 3.0 databases to the Household Operating System architecture. When working with any UB3 database, consult this page to understand which architectural concept it implements, which properties have been added, and how terminology maps between the two systems. The core rule: UB3 databases are the operational databases (DD-14). Do not create parallel databases.

## The Core Decision (DD-14)

**Extend Ultimate Brain 3.0, don't replace it.** UB3's databases have sophisticated formula properties, automations, views, and relations that represent significant design investment. The Household Operating System layers its architectural concepts on top of UB3's existing infrastructure through property additions and conceptual rebranding.

---

## Database Mapping

| Our Architecture | UB3 Database | Collection ID | Status |
|-----------------|-------------|---------------|--------|
| Tasks (Output) | Tasks | `2381e08b-9b34-81e3-87de-000b74035da5` | Extend |
| Projects (Output) | Projects | `2381e08b-9b34-811e-b029-000bbc2294b3` | Extend |
| OKRs (Control/Output) | Goals | `2381e08b-9b34-8180-afb4-000b56ce9265` | Extend |
| Areas (PARA taxonomy) | Tags | `2381e08b-9b34-81dc-8957-000be9e2df6b` | Keep as-is |
| Notes / Knowledge | Notes | `2381e08b-9b34-8141-8f8e-000b0a820342` | Extend |
| System Log (Refine) | *Does not exist* | — | Create new |
| Inbox (Input) | *Notes with Type = Inbox* | — | Option A chosen (IB-93) |
| Work Sessions | Work Sessions | `2381e08b-9b34-81ee-a999-000ba3e5290d` | Keep as-is |
| Milestones | Milestones | `2381e08b-9b34-81e3-8b75-000b45c8b697` | Keep as-is |
| People | People | `2381e08b-9b34-819f-82c9-000bab95114b` | Keep as-is |
| Books | Books + Reading Log + Genres | Various | Keep as-is |
| Recipes | Recipes + Recipe Tags + Meal Planner | Various | Keep as-is |

---

## Terminology Reconciliation

| Our Term | UB3 Term | Notes |
|----------|---------|-------|
| **Area** (PARA) | **Tag** (with Area type) | UB3 uses "Tags" as its PARA taxonomy. Tags with the Area template applied are our Areas. |
| **Workstream** (DD-06) | **Project** with Status = Ongoing | UB3's "Ongoing" project status is functionally identical to our Workstream concept. Workstreams are the process-oriented equivalent of Projects — they organize Operations (recurring Tasks) the way Projects organize Tasks (DD-06 dual hierarchy). Can connect to Goals for alignment/visibility but are **excluded from Goal progress tracking** (DD-25). |
| **Operation** (DD-06) | **Recurring Task** | UB3's recurrence system (Recur Interval, Recur Unit, Days) handles our Operations. Operations are the process-oriented equivalent of Tasks — the atomic unit of ongoing work within a Workstream (DD-06 dual hierarchy). |
| **Speedy** (DD-07) | **Type = Speedy** on Tasks | Type property added (IB-92). Values: Task, Speedy. |
| **Owner** (DD-09) | **Owner** (select) — replaces Visibility | Owner (Nick/JR/Household) added to all 8 DBs. Visibility migrated and hidden (IB-94). |
| **OKR** | **Goal** with Goal Type | Simplified hierarchy (DD-25 amendment 2026-03-01) uses **Yearly Objective only**. Key Result and Milestone values in Goal Type are dormant. Milestones tracked in separate Milestones DB. |
| **Capturing Beast** | **Quick Capture** · Notes intake | UB3's Quick Capture page is the entry point. Notes with Type = Inbox hold unprocessed captures (IB-93). |
| **Execution Beast** | **My Day** · **My Week** · Projects views | UB3's execution views (My Day, My Week, Process/GTD) implement the Execution Beast's PEA rhythm. |
| **Command Center** (DD-13) | **UB3 Dashboard** (partial) | UB3's home dashboard shows Tasks/Notes/Projects. Needs to evolve into or be replaced by the Command Center. |
| **GTD-Lite** (DD-05) | **Process (GTD)** page + Smart List | Already fully implemented in UB3 with Smart List (Do Next/Delegated/Someday) and the Process page. |

---

## Tasks Database: Current vs. Target

### What already exists and maps cleanly

| UB3 Property | Our Concept | Notes |
|-------------|------------|-------|
| Name | Task name | Direct map |
| Status (To Do/Doing/Done) | Task status | Direct map |
| Due | Due date | Direct map |
| Priority (Low/Medium/High) | Priority | Direct map |
| Project (relation) | Project link | Direct map to our Projects |
| Assignee (person) | Assignee (DD-09) | Already exists — who's doing the work |
| Smart List (Do Next/Delegated/Someday) | GTD-Lite lists | Direct map to DD-05 |
| My Day (checkbox) | My Day view filter | Direct map to Execution Beast daily execution |
| Energy (High/Low) | Daily prioritization | Useful for PEA rhythm — keep |
| Location (Home/Office/Errand) | Context filtering | GTD context — keep |
| P/I (Process/Immersive) | Work type | Maps to shallow vs. deep work — keep |
| Sub-Tasks (self-relation) | Task hierarchy | Keep — UB3's approach works |
| Recur Interval + Recur Unit + Days | Operations (DD-06) | Recurring tasks = our Operations concept |
| Work Sessions (relation) | Time tracking | Keep as-is |
| Labels (multi-select) | Kanban tags within Projects | Keep as-is |
| Key Result (relation to Goals) | OKR link | Connects standalone tasks to Goals (Yearly Objectives). Tasks within Projects do not use this (no-double-counting rule per DD-25). |
| Visibility (Shared/Nick-Private/JR-Private) | Legacy — being replaced by Owner | Migration complete (IB-94). Visibility hidden from all views. Property preserved for reference. |

### Properties added

| Property | Type | Values | Purpose | Status |
|----------|------|--------|---------|--------|
| **Owner** | Select | Nick, JR, Household | Replaces Visibility. Determines who this task belongs to (DD-09). | Done (IB-01) |
| **Type** | Select | Task, Speedy | Distinguishes standard tasks from quick items <=15 min (DD-07). Speedies get batched, not individually scheduled. | Done (IB-92) |
| **Waiting On** | Text | — | Records what you're waiting for when a task is delegated or blocked. | Done (IB-79) |
| **Notes** | Relation | — | Two-way relation to Notes DB. | Done (IB-31) |

### Properties to deprecate

| Property | Reason | Action |
|----------|--------|--------|
| **Visibility** | Replaced by Owner, which has cleaner semantics (ownership vs. visibility) and includes "Household" as a value. | Hidden from all views (IB-94). Property preserved for migration reference — do not delete. |
| **Shopping List** | Recipe-specific checkbox. Consider moving to Meal Planner relation instead. | Evaluate during WS2; low priority. |

---

## Projects Database: Current vs. Target

### What already exists and maps cleanly

| UB3 Property | Our Concept | Notes |
|-------------|------------|-------|
| Name | Project name | Direct map |
| Status (Planned/On Hold/Doing/Ongoing/Waiting on Input/Done/Deferred/Archived) | Project + Workstream status | "Ongoing" = Workstream (DD-06). Rich status set covers our needs. |
| Tag (relation to Tags) | Area link | This is UB3's PARA Area association. Direct map. |
| Goal (relation to Goals) | OKR link | Connects projects to goals/OKRs. Direct map. |
| Target Deadline | Target date | Direct map |
| Tasks (relation) | Task list | Direct map |
| Notes (relation) | Project notes | Direct map |
| Pulled Notes + Pulled Tags | Reference materials | UB3's elegant system for pulling in related knowledge. Keep. |
| People (relation) | Collaborators | Direct map |
| Progress (formula) | Completion % | Calculated from task status. Keep. |
| Time Tracked (formula) | Time investment | Rollup from Work Sessions. Keep. |
| Visibility | Legacy — being replaced by Owner | Migration complete (IB-94) |
| Workstream (relation to Tags) | Workstream link | Already exists! Maps to our Workstream concept. |
| Archived (checkbox) | Archive flag | Maps to PARA Archive stage. Keep. |

### Properties added

| Property | Type | Values | Purpose | Status |
|----------|------|--------|---------|--------|
| **Owner** | Select | Nick, JR, Household | Replaces Visibility (DD-09). | Done (IB-02) |
| **Waiting On** | Text | — | Records what you're waiting for when status is "Waiting on Input". | Done (IB-78) |

### Key insight: Projects with Status = "Ongoing" (Workstreams)

UB3 already has the concept of a Workstream — it's a Project with Status = "Ongoing." These are described in UB3 as "projects that collect and organize tasks meant to maintain an ongoing standard." This is a near-perfect match to our Workstream definition (DD-06): "Ongoing body of work with no fixed end date, tied to an Area." No structural changes needed — just conceptual recognition.

**The dual hierarchy (DD-06, amended 2026-03-01):** Workstreams are the process-oriented equivalent of Projects, organizing Operations (recurring Tasks) the way Projects organize Tasks. This creates two parallel structures: Deliverable (Goal → Project → Task) and Process (Goal → Workstream → Operation). Workstreams can connect to Goals for alignment/visibility but are **excluded from Goal progress tracking** (DD-25). Workstream health is monitored qualitatively via the Family Meeting Phase 3 Workstream pulse. Standard adherence tracking is a deferred future enhancement (DD-20).

---

## Goals Database: Current vs. Target (OKRs)

### What already exists and maps cleanly

| UB3 Property | Our Concept | Notes |
|-------------|------------|-------|
| Name | Goal/OKR name | Direct map |
| Goal Type (Yearly Objective/Key Result/Milestone) | OKR hierarchy | Simplified hierarchy uses **Yearly Objective only** (DD-25 amendment 2026-03-01). Key Result and Milestone values are **dormant**. Milestones tracked in separate Milestones DB. |
| Parent Goal (self-relation) | OKR nesting | Supports future KR nesting under Objectives if quarterly planning is added. Currently **dormant** — not used in simplified hierarchy. |
| Status (Dream/Active/Achieved) | Goal status | Direct map |
| Tag (relation to Tags) | Area link | Direct map to PARA Area |
| Projects (relation) | Linked projects | Direct map |
| Milestones (relation) | Milestone tracking | Direct map |
| Tasks (relation) | Direct task link | Standalone tasks link directly to Yearly Objectives. Tasks within Projects do not use this link (no-double-counting rule per DD-25). |
| Owner (person) | Person assignment | Existing person-type property for assigning who owns the goal. |
| Timeframe (select: 2026-2030 + quarterly) | Time horizon | Already supports multi-year and quarterly planning. Excellent. |
| Target Deadline | Deadline | Direct map |
| Workstream (relation to Tags) | Workstream link | Already exists |

### Properties added

| Property | Type | Values | Purpose | Status |
|----------|------|--------|---------|--------|
| **Owner** (select) | Select | Nick, JR, Household | Distinguishes Household goals from personal ones (DD-09). Owner = Household is the household level, Owner = Nick/JR is personal. No separate Level property needed. | Done (IB-03) |

### OKR structure already in UB3 — simplified hierarchy

The Goal Type property includes Yearly Objective, Key Result, and Milestone values. **The simplified hierarchy (DD-25, amended 2026-03-01) uses only Yearly Objective.** Key Result and Milestone values in Goal Type are **dormant** — retained for potential future quarterly planning but not actively used.

Combined with the Parent Goal self-relation and the Projects/Tasks relations, the working hierarchy is:

- **Yearly Objective** (Goals DB) → linked **Projects** (Projects DB) + standalone **Tasks** (Tasks DB), with optional **Milestones** (Milestones DB) for phasing

**Progress tracking:** Goal progress = completed work items (Projects at Done + standalone Tasks completed) / total work items. Fully automated, no manual updating required. **Workstreams are excluded** — they can connect to Goals via the Goals relation for alignment/visibility but do not count in the progress formula (DD-25 amendment 2026-03-01c).

**Milestones** are tracked in the separate Milestones DB (not via Goal Type). When present, they serve as optional organizational containers grouping Projects/Tasks into phases. A Milestone auto-completes when all its linked Projects/Tasks are done.

The Owner (select) property distinguishes Household goals from Personal goals (DD-09).

---

## Notes Database: Dual Role

UB3's Notes database serves multiple purposes through its Type property. Here's how each Type maps to our architecture:

| Note Type | Our Concept | ICOR Stage | Notes |
|-----------|------------|-----------|-------|
| Journal | Private Teamspace content | — | Consider moving to Private Teamspace pages (not database items) |
| Meeting | Knowledge capture | Input/Control | Family Meeting notes would be Household-owned |
| Web Clip | Reference material | Input | Captured knowledge from the web |
| Reference | PARA Resource | Control | Static reference material |
| Idea | Potential inbox item | Input | Could feed the Capturing Beast |
| Plan | Strategic document | Control | Planning documents |
| Voice Note | Capture | Input | Feeds into the Capturing Beast |
| Daily | Daily note/log | Refine | Daily reflection — could feed System Log |
| Book / Lecture | Learning notes | Input/Control | Knowledge capture from sources |
| Recipe | Household knowledge | — | Already handled by separate Recipe databases |
| **Inbox** | **Unprocessed capture** | **Input** | **Added (IB-93). Unprocessed captures live here until processed.** |

### The Inbox decision (resolved)

**Option A was chosen:** Use Notes with Type = "Inbox" (IB-93). Unprocessed captures live as Notes with Type=Inbox until they're processed (turned into Tasks, filed as Reference, etc.). This avoids creating a separate Inbox database. Will evaluate during WS3 whether a dedicated database is needed. The Capturing Beast routing logic works with this approach.

---

## New Databases to Create

### System Log (DD-11)

This database does not exist in UB3 and must be created from scratch. See the System Log spec page for the full schema. It should be created in the same location as the other UB3 databases (under Databases & Components) and linked from the Command Center.

### Command Center Page (DD-13)

The current UB3 Dashboard page shows Tasks, Notes, Projects, and Tags inline. Two approaches for the Command Center:

**Option A: Evolve the UB3 Dashboard** — Add Household OKR views, System Log embed, Area Health section, and personal quick links to the existing dashboard page. Pro: one home page, less navigation. Con: may get crowded; mixes UB3 navigation with household operations.

**Option B: Create a separate Command Center** — New page that embeds UB3 database views in the Command Center layout. The UB3 Dashboard remains accessible but is no longer the primary landing page. Pro: clean design matching our spec. Con: two "home" pages.

**Recommendation:** Option B. Build a new Command Center page with the layout from the Household Teamspace Structure spec. Keep the UB3 Dashboard as a "power user" page for deep database access. Set the Command Center as each person's sidebar favorite.

---

## WS2 Implementation Sequence

Phased approach to avoid breaking existing functionality:

| Phase | Action | Risk | Status |
|-------|--------|------|--------|
| **2.1** | Add Owner (select) to Tasks, Projects, Goals, Notes, Tags, People, Work Sessions, Reading Logs. | Low — new properties don't affect existing views | Done (IB-01, 02, 03, 03b-03e) |
| **2.2** | Migrate Visibility values to Owner (Shared→Household, Nick-Private→Nick, John-Private→JR) | Medium — bulk update | Done (IB-94 — human steps completed 2026-02-28) |
| **2.3** | Add Type (Task/Speedy) to Tasks | Low — new property | Done (IB-92) |
| **2.4** | Add "Inbox" option to Notes Type property | Low | Done (IB-93) |
| **2.5** | Create System Log database with full schema from spec | None — new database | Queued (IB-09) |
| **2.6** | Build Command Center page with embedded views | None — new page | Queued (IB-08) |
| **2.7** | Create Area-specific views in each Area page (filtered by Tag/Area). Each Area page becomes an **organizational hub** showing both hierarchies: active Workstreams (Labor), active Projects (Work), connected Goals, and recent Operations/Tasks. Include a **"This Year" date filter** for yearly scoping. This replaces the Jira Epic pattern (Area + Year) with a permanent Area page that uses date filtering instead of yearly duplication. See DD-23 for the full Area hub pattern. | Low | Queued |
| **2.8** | Hide deprecated Visibility property from all views | Low | Done (IB-94) |
| **2.9** | Create filtered personal views (My Day by Owner, My Projects by Owner, My OKRs by Owner) | Low | Queued |
| **2.10** | Update UB3 Dashboard to link to Command Center | Low | Queued |

---

## Interaction with Other Design Decisions

- **DD-06** (Output Elements): Tasks database = Tasks + Speedies (via Type property) + Operations (via recurrence). Projects database = Projects + Workstreams (via Status = Ongoing). Goals database = Yearly Objectives (via Goal Type = Yearly Objective). Key Result and Milestone values in Goal Type are dormant (DD-25 amendment 2026-03-01). Milestones tracked in separate Milestones DB. **Dual hierarchy:** Deliverable (Goal → Project → Task) and Process (Goal → Workstream → Operation). Workstreams connect to Goals for alignment only — excluded from progress formula. **Project → Workstream relation deferred** — the shared Area tag provides sufficient grouping between Projects spawned by ongoing work and their parent Workstreams.
- **DD-07** (Speedies): Implemented by adding Type = Speedy to the Tasks database (IB-92). Speedies get batched into Speedy blocks rather than individually scheduled.
- **DD-09** (Personal/Household Model): Owner (select) property added to all 8 DBs. Visibility migrated to Owner and hidden (IB-94). Filtered views create the personal experience.
- **DD-10** (Capturing Beast): Quick Capture page is the entry point. Notes with Type = Inbox hold unprocessed captures (IB-93).
- **DD-11** (System Log): To be created as a new database alongside UB3's existing databases (IB-09).
- **DD-12** (Workspace Architecture): All UB3 databases live in the Household Teamspace. No databases in Private Teamspaces.
- **DD-13** (Teamspace Structure): UB3 databases = the Operational Databases section. Command Center to be built as a new page with embedded UB3 views (IB-08).

---

*Updated 2026-03-01. This page is authoritative for the WS2 integration. Area pages serve as organizational hubs showing both hierarchies with "This Year" date filters (see DD-23, Phase 2.7). Project → Workstream relation deferred — Area tag provides sufficient grouping. When modifying UB3 databases, follow the implementation sequence above. When in doubt about whether a UB3 concept maps to an architectural concept, consult the Terminology Reconciliation table.*
