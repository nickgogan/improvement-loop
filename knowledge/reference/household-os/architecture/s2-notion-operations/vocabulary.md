---
notion_id: 30f1e08b-9b34-8105-b8ed-cbf239e3e177
title: "Vocabulary"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Vocabulary

> **For agents:** This page defines canonical terms used throughout the Household Operating System. When interpreting user input or generating system content, map informal language to these precise definitions. Ambiguous terms should be clarified against this vocabulary.

## Core Framework Terms

| Term | Definition | Context |
|------|-----------|---------|
| **ICOR** | Input, Control, Output, Refine — the meta-framework that unifies all other methodologies. Based on systems theory. | Architecture-wide |
| **PARA** | Projects, Areas, Resources, Archives — the organizational taxonomy for all information. | Organization layer |
| **CODE** | Capture, Organize, Distill, Express — the knowledge lifecycle methodology. | Knowledge management |
| **OKR** | Objectives and Key Results — the goal-setting framework providing strategic alignment. | Strategic layer |
| **GTD-Lite** | Getting Things Done (simplified) — inbox processing and next-action execution without contexts or smart lists. | Execution layer |
| **OODA** | Observe, Orient, Decide, Act — rapid decision loop. Equivalent to ICOR at micro-scale (DD-04). | Decision-making |
| **Zettelkasten** | Atomic, linked note-taking method. Permanent notes, literature notes, fleeting notes, Maps of Content (MOCs). | Knowledge layer |

| Term | Definition | System Mapping |
|------|-----------|----------------|
| **Labor** (Arendt) | In Hannah Arendt's *The Human Condition*, Labor is the cyclical activity tied to biological necessity and maintenance of life. It produces nothing permanent — its products are consumed almost as soon as they appear. Labor never "completes"; it sustains. The defining quality is repetition: the task recurs because the need recurs. | Maps to the **Process hierarchy**: Workstreams and Operations. These are ongoing, never-completing bodies of work that maintain the household's steady state. Their value is measured by consistency and adherence, not by deliverables produced. |
| **Work** (Arendt) | In Arendt's framework, Work is the activity that fabricates durable artifacts — things that outlast the activity of making them. Work has a definite beginning and end. The craftsman starts with a plan, transforms material, and produces a finished object that persists in the world. | Maps to the **Deliverable hierarchy**: Projects and Tasks. These have clear start and end points, produce tangible outputs, and their progress is tracked toward completion. Goal progress is calculated from these elements. |

## System Concepts

| Term | Definition | Context |
|------|-----------|---------|
| **Capturing Beast** | The INPUT stage gatekeeper. Filters incoming information through 3 lenses before it enters the system. | ICOR Input |
| **Front Desk** | The CONTROL stage orchestrator. The active decision-making layer between capture and execution. Triages, prioritizes, assigns, and routes items. Always-on for agents, PEA ritual-based for humans. | ICOR Control |
| **Execution Beast** | The OUTPUT stage structural engine. Organizes all work through the Output Elements hierarchy and PEA rhythm. | ICOR Output |
| **The Compass** | The REFINE stage orchestrator. The system's self-improvement engine — runs five review cadences (Daily Pulse through Annual Reset), monitors six vital signs, tracks equity between partners, and triggers emergency protocols when thresholds are breached. | ICOR Refine |
| **Single Source of Truth (SSOT)** | Notion — the authoritative location for all actionable information and system state. | Architecture principle |
| **Core App** | The primary tool where most work happens (Notion). Receives designation per ICOR tool classification. | Tool architecture |
| **Satellite App** | Tools that extend the Core App for specialized functions (Google Workspace, Heptabase). | Tool architecture |
| **Utility App** | Single-purpose tools for specific tasks (scanner app, password manager). | Tool architecture |
| **PEA Rhythm** | Plan, Execute, Align — the fractal execution cadence at daily/weekly/quarterly/annual scales. | Execution |
| **Command Center** | The shared home page of the Household Teamspace, built on the enhanced UB3 Dashboard page. A view layer with two layers: Mission Control (household-wide vital signs, OKR snapshot, priorities, activity feed) and three personal Timescale Cockpits (My Day, My Week, My Year). Each cockpit uses a dual lens — "Mine" (Owner-filtered) and "Ours" (Household-filtered) — so each partner sees personal work alongside household commitments at every timescale. | DD-13, DD-19 |
| **Timescale Cockpit** | A personal view page that shows both "Mine" and "Ours" lenses at a specific timescale. Three cockpits exist: My Day (daily execution), My Week (weekly planning and review), My Year (strategic and quarterly). Built on existing UB3 pages enhanced with Owner-filtered views. | DD-19 |
| **Dual Lens** | The pattern of showing two filtered views side by side: "Mine" (Owner = Me) and "Ours" (Owner = Household or all Owners). Applied to every Timescale Cockpit so each partner sees personal and household context together. | DD-19 |
| **Mission Control** | The top section of the Command Center showing household-wide overview: vital signs strip, Household OKR snapshot, this week's priorities, upcoming deadlines, and recent activity feed. Both partners see the same content. | DD-19 |
| **Partner Pulse** | A compact strip in My Day showing what the other partner has on their plate today (task count, blockers). Enables coordination without interruption. Uses Owner != Me filter. | DD-19 |
| **Standard** | A specific, measurable recurring commitment with an explicit adherence target. Distinct from an Operation (DD-06): an Operation is any recurring task; a Standard is an Operation that has been *elevated* with a target and active monitoring. Tracked as recurring Tasks with Label = "Standard". Monitored via the Standards Check widget. Conceptually part of The Compass's self-monitoring. | DD-18, DD-19, DD-20 |
| **Goal Cascade Progress** | A rollup visualization showing how Yearly Objectives progress as their linked Projects and standalone Tasks are completed. Milestones (when present) provide optional grouping. Progress = completed work items (Projects at Done + standalone Tasks completed) / total work items. Fully automated. Surfaces in My Year cockpit and OKR Command Center. | DD-19 |
| **System Integrity** | The technical health of the Notion workspace itself — distinct from The Compass's productivity vital signs. Monitors broken relations, orphaned pages, missing properties, automation failures, schema drift, and stale content. Results written to the System Diagnostics page. Audited monthly as part of The Compass's Monthly Audit cadence. | DD-18 |
| **System Diagnostics** | A dedicated page showing current System Integrity status with pass/warn/fail indicators for each check category, detailed findings with links, recommended fixes, and last audit timestamp. Linked from Mission Control. | DD-18 |
| **Cadence** | A recurring time rhythm at which activities happen (daily, weekly, monthly, quarterly, annual). Not a "thing" in the database — a classification applied to Routines, Standards, and review cycles. The Compass review cadences and PEA rhythm are Cadences. | DD-18, DD-20 |
| **Routine** | A bundle of related activities that happen together on a Cadence. Groups multiple Operations, Tasks, and/or Standards into a coherent sequence. Examples: Morning Planning, Family Meeting, Weekly Review, Sunday Meal Prep. Every Compass review cadence is a Routine. | DD-20 |
| **Process** | A defined, repeatable sequence of steps that transforms an input into an output. Describes *how* something gets done. The Front Desk's Triage Sequence is a Process. The 3-Lens Capture Filter is a Process. The PEA Cycle is a Process. Distinct from the UB3 P/I property (Process/Immersive), which classifies task *depth*, not operational *pattern*. | DD-20 |
| **Procedure** | Documented step-by-step instructions for executing a Process. The "manual" for how to actually do it. Not every Process needs a Procedure immediately — start with Processes that both partners or agents must execute consistently. | DD-20 |
| **SOP (Standard Operating Procedure)** | A Procedure that has been formalized as binding and authoritative. The "this is how we always do it" version. Changing an SOP requires explicit agreement from both partners, similar to Design Decisions. Evolution path: Process → Procedure → SOP. | DD-20 |
| **Workflow** | The system-level path items take as they move across multiple Processes and ICOR stages. Describes the end-to-end journey, not individual steps. Examples: Capture-to-Action, Goal-to-Outcome, Knowledge Formation. Workflows are emergent — you don't build them directly; you build Processes and connect them. | DD-20 |
| **Triage Sequence** | The five-step Front Desk process: (1) Classify, (2) Assign Owner, (3) Prioritize (P1-P4), (4) Route to database/location, (5) Log in System Log. | DD-15 |
| **View Layer** | A page or dashboard that displays filtered content from databases without storing data itself. The Command Center and My Day/My Projects pages are view layers. Contrast with Action Layer. | DD-13 |
| **Action Layer** | A component that makes decisions and changes system state (e.g., the Front Desk). Contrast with View Layer, which only displays information. | DD-15 |
| **Operational Databases** | The shared databases that hold all actionable and trackable items: Inbox, Tasks, Projects, OKRs (Goals), System Log. These live in the Household Teamspace and use Owner/Assignee properties for personal scoping. | DD-13 |
| **Priority (P1-P4)** | P1 = Urgent (deadline within 48h or blocking). P2 = Important (tied to active OKR). P3 = Standard (useful, not time-sensitive). P4 = Low (nice to have). | DD-15 |
| **Three-Entry Pattern** | The structural mechanism for Hybrid Areas in the Tags database. A Hybrid Area gets three Tag entries: one shared parent (Owner = Household) and two personal Sub-Tags (Owner = Nick, Owner = JR) linked via Parent Tag. Ensures both shared resources and personal content are properly scoped. Max two levels deep. | DD-23 |
| **Hybrid Area** | A PARA Area containing both personal and household content. Uses the three-entry pattern. The four Hybrid Areas are: Career, Character Development, Health & Wellness, Social. | DD-23 |
| **Pure Household Area** | A PARA Area that is shared by default with a single Tag entry (Owner = Household). The five Pure Household Areas are: Finances, Home, Legal, Relationship, Travel. | |
| **Area Hub** | The view pattern where each Area (Tag) page functions as the single place to see everything happening in a domain — showing active Workstreams (Labor), active Projects (Work), connected Goals, and recent Operations/Tasks. Replaces the Jira Epic pattern (Area + Year) with a permanent page that uses a "This Year" date filter for yearly scoping instead of yearly duplication. | DD-23 |
| **Horizon** | A property on the Design Decisions database indicating design timeline: Immediate (active/ready), Near-term (designed but depends on other work), Deferred (intentionally postponed). Introduced by DD-23. | DD-23 |
| **Planning Queue** | A flat, priority-sorted view of all tasks available for commitment. No algorithmic suggestions — sorted by Priority (P1→P4), then Due Date. Each person pulls tasks from the Queue by setting Do Dates during their Plan beat. Lives in My Week. Intelligence layer (AI suggestions) deferred to future enhancement. | DD-24 |
| **Daily Beat** | One of three phases in the daily execution loop: Plan (~5-10 min morning), Execute (throughout day), Align (~3-5 min end of day). The PEA rhythm made concrete at the daily timescale. | DD-24 |
| **Configurable Unit Time** | The principle that each person chooses their own planning granularity — daily, weekly, or hybrid — without the system prescribing one. Daily planners pull tasks each morning; weekly planners pull at the Family Meeting. Same Planning Queue mechanism, different commitment horizon. | DD-24 |
| Strict Capture Discipline | The rule that during execution hours (Beat 2), all new items go to Quick Capture only — never directly onto the active task list. Prevents interrupt-driven work. The one exception: genuine emergencies evaluated through the OODA micro-loop. | DD-24 |
| **OKR Lifecycle** | The five-phase end-to-end journey of Goals: Set (create goals at yearly planning), Cascade (connect to Projects/Tasks and optional Milestones), Track (weekly pulse + monthly audit + quarterly review), Score (assess outcomes using Status property), Retire (archive completed/missed goals, roll forward ongoing ones). Operates across three primary timescales (annual, monthly, weekly) with quarterly reviews as deeper checkpoints. Quarterly Key Results layer is dormant — see DD-25. | DD-25 |
| **Quarterly Review & Planning** | A 60-90 min meeting held 4x/year where outgoing quarter's KRs are scored, yearly goal progress is assessed, incoming quarter's KRs are defined, and the backlog is re-prioritized. Quarterly goals need not be pre-planned at the annual level — they can emerge at this meeting. Aligns with Compass Cadence 4 (Quarterly Deep Review). | DD-25 |
| **Yearly Review & Planning** | The ~3-hour annual session (~January) where the household Vision is read or refreshed, prior year goals are scored and retired, new Yearly Goals and KPIs are set, and Q1 KR breakdown is attempted. Creates new Goal entries rather than reusing old ones to preserve historical record. Aligns with Compass Cadence 5 (Annual Reset). | DD-25 |
| **Project-Worthiness Test** | The decision heuristic for whether work should be organized as a Project: Does it involve multiple coordinated tasks, a shared deliverable, and a timeframe? Single tasks stay as tasks. 2-3 loosely related tasks stay as tasks linked to an Area. Recurring tasks with no end date become Workstreams or Operations, not standard projects. | DD-26 |
| **Stalled Project Detection** | A monitoring rule applied during the Monthly Audit: any project with Status = Doing and zero task completions in 14+ days is flagged as stalled. The owner must then decide: recommit, adjust approach, put on hold, or close out. Prevents projects from silently rotting in the active list. | DD-26 |
| **Batch Archival** | The practice of archiving completed projects (and other Done items) during Monthly Audit and Quarterly Review cadences rather than immediately after completion. Keeps recently finished work visible for reflection and celebration before moving it out of active views. | DD-26, DD-28 |
| **Archive (Notion)** | The first tier of the two-tier archival model. Items no longer active but still searchable and accessible within Notion. Completed projects, retired OKRs, old notes move here during Batch Archival. Content remains in the relational graph and can be queried. The "warm" archive. | DD-26, DD-28 |
| **Cold Storage** | The second tier of the two-tier archival model. Content exported from Notion to an external SSD for long-term preservation. Reduces Notion workspace size over time. Triggered during the Yearly Review (Annual Reset). A Notion index stub (via DD-22 Archive Index) remains so the system knows the content exists. The "cold" archive. | DD-22, DD-18 |
| **Deferred Enrichment** | A two-phase capture mode on the Front Desk slackbot. When a user can't engage with follow-up questions (mid-meeting, fleeting thought), the bot auto-defers after a configurable timeout and queues an enrichment reminder for later. The item is parked in the inbox with raw text. If the reminder is also ignored, the item gets processed at the next triage cadence (DD-28) with whatever context is available. Nothing gets lost. | DD-15 |
| **Active Knowledge Surface** | The role Notion plays in the knowledge formation flow: organized for retrieval, action, and operational use. Analogous to ICOR's Shallow Knowledge — not shallow in value, but optimized for quick access. All notes, reference material, meeting records, and Heptabase stubs live here. Notion knows about everything even when it doesn't contain everything. | DD-27 |
| **Deep Knowledge Workshop** | The role Heptabase plays in the knowledge formation flow: spatial canvas for synthesis, connection, and sustained cognitive work. Analogous to ICOR's Deep Knowledge — understanding that emerges from working with ideas over time. Notes go here when they need *thinking*, not just *storing*. | DD-27 |
| **Destination Decision** | The key fork in the Organize stage (CODE Stage 2): does this note need *thinking* or just *storing*? If storing → stays in Notion (Active Knowledge Surface). If thinking → goes to Heptabase (Deep Knowledge Workshop) with a Reference Note stub left in Notion. Most notes stay in Notion. | DD-27 |
| **Active Topics** | Resource tags (from the Tags DB) representing current areas of intellectual focus — topics the household is actively learning about, researching, or building knowledge in. Promoted and retired during Quarterly Review & Planning and Yearly Review & Planning meetings. No separate management process. | DD-27 |
| **Cross-Lane Transitions** | Items jumping between the knowledge lane (Notes) and the action lane (Tasks/Projects). Four patterns: Note → Task (note reveals an action), Note → Project Note (note links to a project), Idea Note → Project (idea matures past the project-worthiness test), Task → Note (task produces reusable knowledge). Transitions create new artifacts or add relations — the source item always stays. Reviews are the most common trigger for recognizing transitions. | DD-27 |
| **Speedy Batch** | A processing pattern where tasks classified as Speedies (<=15 min) during daily inbox processing are grouped together and executed in a single focused block during the Execute beat, rather than being scattered throughout the day. Prevents small tasks from fragmenting deep work focus. | DD-28, DD-06 |
| **Processing Cadences** | The three rhythms at which inbox processing occurs: Daily (Task Inbox to zero, personal items only), Weekly (Note Inbox to zero + action system sweep + Household items at Family Meeting), Monthly (stale sweep, orphan check, stalled detection, batch archival, cross-lane recognition within the Monthly Audit). | DD-28 |
| **Flag for Discussion** | A pattern used when inbox processing reveals an item needing partner input. Rather than blocking processing, the item is added to the Housekeeping Queue (DD-24 Phase 5) and resolved jointly at the next Family Meeting. Applies at all cadences. | DD-28, DD-24 |
| **Housekeeping Queue** | A filtered view in the Family Meeting page showing Tasks with Status = Blocked and Block Note = "Family Meeting". Serves as the catch-all agenda for items flagged during the week via the "Flag for Discussion" pattern (DD-28) that need joint partner discussion. Reviewed and resolved during Family Meeting Phase 5 (Commit). After resolution, items are unblocked (Status updated, Block Note cleared). | DD-24, DD-28 |

## Output Elements

| Term | Definition | Key Distinction |
|------|-----------|-----------------|
| **Goal** | A Yearly Objective in the Goals database. Time-bound (usually 12 months). Can be contributed to by Projects, standalone Tasks, and optional Milestones. Progress is tracked automatically via Project/Task completion percentage. | Has a yearly timeframe and Owner. Cascades to Projects and Tasks. |
| **Milestone** | An optional organizational container in the Milestones DB, linked to a Yearly Objective. Groups Projects and Tasks into phases. Not every goal needs Milestones. Each Project or Task links to at most one Milestone. | Optional. Organizational grouping, not a progress formula driver. |
| **Project** | Multi-step effort with a deliverable and end date. Lives under a Goal or Area. Can optionally be linked to a Milestone for phasing. | Has an end date. Passes the project-worthiness test (DD-26). |
| **Workstream** | The process-oriented equivalent of a Project — an ongoing body of work that organizes recurring Operations the way a Project organizes Tasks. Lives in the Projects DB with Status = "Ongoing." Can optionally connect to a Goal for alignment and visibility, but is **excluded from Goal progress tracking** (because it never completes). Tied to an Area. Monitored qualitatively via Family Meeting Phase 3 Workstream pulse. Philosophically aligned with Arendt's concept of *Labor* (DD-06). | No end date; evolves continuously. Process hierarchy parallel to Project in the deliverable hierarchy. |
| **Operation** | The process-oriented equivalent of a Task — the atomic unit of recurring work within a Workstream. Handled by UB3's recurrence system (Recur Interval, Recur Unit, Days). Keeps the system running through cyclical maintenance. Philosophically aligned with Arendt's concept of *Labor* (DD-06). | Recurring; routine-based. Process hierarchy parallel to Task in the deliverable hierarchy. |
| **Task** | Single actionable step, 15+ minutes. Scheduled individually. Can belong to a Project OR link directly to a Goal as a standalone Task, never both. Has Owner (stewardship) and Assignee (execution) per DD-12. | Standard work unit. Either within a Project or standalone. |
| **Sub-Task** | A Task nested under a parent Task via Notion's parent-child relationship. Inherits Project and People from parent. Completing the parent auto-completes all sub-tasks. Optional — use at Owner's or Assignee's discretion when a Task has independently trackable sub-steps. | Optional nesting. Not used for Speedies. |
| **Speedy** | Actionable step under 15 minutes, low cognitive load (checking email, sending a text, paying a bill). Batched into Speedy blocks during low-energy windows. Always standalone — never a sub-task, never nested under a parent. | Batched by effort type, not individually scheduled. Never a sub-task. |

## Domains

| Term | Definition |
|------|-----------|
| **PKM** | Personal Knowledge Management — individual learning, notes, references |
| **PPM** | Personal Project Management — individual tasks, goals, execution |
| **HKM** | Household Knowledge Management — shared family knowledge, procedures, documentation |
| **HPM** | Household Project Management — shared family projects, goals, coordination |

## Stewardship Model

| Term | Definition |
|------|-----------|
| **Area Stewardship** | Each PARA Area has a Lead and a Backup. Both partners can perform any task; the Lead simply owns the rhythm. |
| **Lead** | The partner who owns the cadence and proactive management of an Area. |
| **Backup** | The partner who can step in fully, guided by the Area Brief. |
| **Area Brief** | A living document for each Area containing: current state, active projects, key contacts, recurring operations, and decision history. Enables seamless handoff. |
| **Stewardship over Specialization** | Core principle: partnership strengthens the individual, not creates dependencies. Either partner must be able to accomplish any task. |

## Workspace Architecture

| Term | Definition | Context |
|------|-----------|---------|
| **Teamspace** | A Notion organizational unit within a workspace that controls visibility and membership. The system uses three: Household (shared), Nick (private), John (private). | DD-12 |
| **Household Teamspace** | The shared Teamspace containing all System Documentation, operational databases, Area pages, and dashboards. This is where agents operate and where all relational data lives. | DD-12 |
| **Private Teamspace** | A personal Teamspace visible only to one partner. Holds journals, drafts, scratch space, and other non-operational content that doesn't need to be in the relational graph. | DD-12 |
| **Boundary Test** | The decision tree for determining where content lives: needs linking? → Household. Agent needs it? → Household. Partner might need it? → Household. Genuinely private? → Private. Unsure? → Default to Household. | DD-12 |
| **Filtered View** | A database view scoped by Owner, Assignee, or other properties. The primary mechanism for creating a personal experience within the shared workspace. Examples: My Day, My Projects, My OKRs. | DD-12 |

## Wardrobe System

| Term | Definition | Context |
|------|-----------|---------|
| **Wardrobe Items** | Database of every garment, shoe, and accessory owned by each person. The atomic building blocks of outfits. Each item has Owner, Category, Style Segment, Season, Formality, and Condition properties. | DD-16 |
| **Outfits** | Database of curated, proven combinations of Wardrobe Items + Fragrance. The primary query surface for "what should I wear today?" Filtered by weather, occasion, mood, location, and style segment. | DD-16 |
| **Fragrance Library** | Unified reference of all personal and home fragrances with queryable properties. Personal fragrances pair with Outfits; home fragrances pair with rooms and occasions. | DD-16 |
| **Style Segment** | A personal aesthetic category that groups compatible garments. Nick: Ruggedly Refined, Activewear, Loungewear, Professional. John: Traditional, Workwear, Sporty, Experimental. Items within the same segment pair naturally. | DD-16 |
| **Pair With** | A self-relation on the Outfits database linking one partner's outfit to the other's complementary look. Used for coordinated date night, event, or going-out-together recommendations. | DD-16 |

## Reference Libraries

| Term | Definition | Context |
|------|-----------|---------|
| **Reference Library** | A structured catalog of things the household owns, consumes, or stores. The PARA Resources layer. Not action-oriented — these are stable knowledge that other system components query. | DD-17 |
| **Archive (SSD)** | Catalog of digital files stored on the external SSD. Enables finding files by type, category, and owner without plugging in and browsing. Properties: Name, File Type, Category, Owner, Path, Date Archived, Size. | DD-17 |
| **Clarkson Storage** | Inventory of physical items in the storage unit at 77 Clarkson Ave. Enables answering "do we have one?" without visiting the unit. Properties: Name, Category, Owner, Location in Unit, Condition, Photo. | DD-17 |
| **Clarkson Active** | Inventory of significant items currently in use at home — furniture, appliances, electronics, fixtures. Properties: Name, Category, Room, Owner, Brand, Condition, Photo. | DD-17 |
| **Business Ideas** | Running catalog of business venture ideas Nick and John have had over time. Preserves early-stage thinking without cluttering active projects. Properties: Name, Status (Idea/Exploring/On Hold/Abandoned), Owner, Domain, Enthusiasm, Summary, Date Added, Notes. | DD-17 |

## UB3 Terminology Reconciliation

> **For agents:** When processing user input or UB3 database content, map these UB3-native terms to their system equivalents. Both terms remain valid; the UB3 term is what appears in the database, the system term is what appears in Architecture documentation.

| UB3 Term | System Equivalent | Notes |
|----------|-------------------|-------|
| **Tag** (UB3 database) | **Area** (PARA) | UB3 Tags database functions as PARA Areas. Tags are the organizational containers for all content. |
| **Ongoing** (Project Status) | **Workstream** | A Project with Status = "Ongoing" is a Workstream — the process-oriented equivalent of a Project. Organizes recurring Operations. Can connect to a Goal for alignment but is **excluded from Goal progress tracking**. Part of the Process hierarchy (Arendt's *Labor*). See DD-06 dual hierarchy. |
| **Smart List** (Task property) | **GTD-Lite context** | UB3's Smart List property (Next, Waiting, Someday/Maybe) maps to GTD processing categories within the execution layer. |
| **Quick Capture** (UB3 view) | **Capturing Beast entry point** | UB3's Quick Capture view is the primary intake for the Capturing Beast. Items land here before the 3-lens filter routes them. |
| **Goal Type** (Goals property) | **OKR hierarchy level (simplified)** | Values: Yearly Objective (active), Key Result (**dormant** — reserved for future quarterly scoping), Milestone (not actively used — separate Milestones DB is the primary mechanism). In the current system, all goal entries use Goal Type = "Yearly Objective". See DD-25 amendment log for the simplification decision. |

## Design Decision Shorthand

| Code | Meaning |
|------|---------|
| **DD-01** | ICOR is the meta-framework; all others nest within it |
| **DD-02** | PARA provides the universal organizational taxonomy across all ICOR stages |
| **DD-03** | CODE maps to ICOR stages (Capture→Input, Organize→Control, Distill→Control/Output, Express→Output) |
| **DD-04** | OODA is ICOR at micro-scale, not a separate framework |
| **DD-05** | GTD-Lite provides the execution methodology within OUTPUT, not a parallel system |
| **DD-06** | Output Elements taxonomy (Goal/Project/Workstream/Operation/Task/Speedy) is binding |
| **DD-07** | Speedies (<=15 min) are a distinct work type, batched not individually scheduled |
| **DD-08** | Family Meeting is the primary CONTROL ritual; Weekly Review is personal only |
| **DD-09** | Hybrid OKR structure: shared Household Vision/OKRs at top, personal OKRs as parallel track, explicit links when personal serves household |
| **DD-10** | The Capturing Beast's 3-lens filter is the design blueprint for how the Front Desk slackbot operates at intake. Personal/household routing happens during intake, not deferred to Control. The Beast defines WHAT to filter; the Front Desk slackbot (DD-15, DD-21) implements HOW |
| **DD-11** | Audit trail is a system primitive; System Log database records all significant changes |
| **DD-12** | Single shared Notion workspace with three Teamspaces (Nick private, John private, Household shared); all operational databases in Household Teamspace; Owner property for scoping, not workspace separation |
| **DD-13** | Four-section Household Teamspace structure: Command Center (view layer), System Documentation, Areas, Operational Databases |
| **DD-14** | Extend UB3, don't replace — add Owner/Type/Level properties to existing databases; map UB3 terminology to system vocabulary |
| **DD-15** | The Front Desk has two roles: (1) Intake — the slackbot captures items, applies the Capturing Beast's 3-lens filter, and routes to Task Inbox or Note Inbox; (2) Triage Framework — the decision protocol humans use during processing cadences to prioritize, assign, and route items to final destinations. Slackbot is always-on; human processing follows PEA cadences. Starts narrow in WS2, expands to full coordination in WS3-WS4. |
| **DD-16** | Three-database wardrobe system: Wardrobe Items, Outfits, Fragrance Library. Per-person with coordinated pairing support. Outfits are the primary query surface for daily recommendations. |
| **DD-17** | Six Reference Libraries as the PARA Resources layer: Recipes (UB3), Books (UB3), Business Ideas (venture ideas catalog), Archive SSD (digital files), Clarkson Storage (storage unit inventory), Clarkson Active (home inventory). Start basic, expand later. |
| **DD-18** | The Compass is the REFINE stage orchestrator — five review cadences (Daily Pulse, Weekly Family Meeting, Monthly Audit, Quarterly Deep Review, Annual Reset), six vital signs with Green/Yellow/Red thresholds, equity tracking, time budget (120 min/week), six emergency response protocols, and System Integrity monitoring (workspace technical health via System Diagnostics page). |
| **DD-19** | The Command Center is the enhanced UB3 Dashboard — shared home with Mission Control (vital signs, household OKRs, priorities, activity feed, System Health indicator) plus four personal Timescale Cockpits (My Day, My Week, My Quarter, My Year). Each cockpit uses a dual lens: "Mine" (Owner = Me) and "Ours" (Owner = Household). My Quarter introduces Goal Cascade Progress and Standards Check. System Integrity monitoring is owned by DD-18 (The Compass); the Command Center displays a System Health indicator linking to the System Diagnostics page. |
| **DD-20** | Operational Concepts hierarchy: Cadence (time rhythm), Routine (activity bundle on a cadence), Standard (measurable recurring commitment), Process (repeatable step sequence), Procedure (documented instructions), SOP (binding Procedure). DD-06 = what work IS; DD-20 = how recurring work is PATTERNED. Workflows are emergent system-level paths across Processes. |
| **DD-21** | Capture-to-Action Pipeline — the end-to-end workflow from item capture (Front Desk slackbot) through dual inboxes (Task Inbox + Note Inbox) to human processing at cadences and five routing destinations (Tasks, Notes, Heptabase, Google Drive, Trash). Links DD-10 (what to capture), DD-15 (how to triage), and DD-22 (external content) into a single flow. |
| **DD-22** | External Content Index — how Notion maintains index-of-record for content stored outside Notion: Drive Index database (Area-scoped Google Drive links), Archive Index database (SSD cold storage catalog), and Heptabase Reference Note stubs. Notion is the SSOT for *where* things are, even when the content lives elsewhere. |
| **DD-23** | Area Taxonomy & Tags Enhancement — nine PARA Areas organized as four Hybrid (Career, Character Development, Health & Wellness, Social) and five Pure Household (Finances, Home, Legal, Relationship, Travel). Hybrid Areas use a three-entry pattern: shared parent (Owner = Household) + personal Sub-Tags (Owner = Nick, Owner = JR). Tags database gets Owner, Lead, and Backup properties. Area Briefs live in each Tag entry's page body. Technology folded into Home + Finances. Style deferred. |
| **DD-24** | The Daily & Weekly Execution Loop — three daily beats (Plan, Execute, Align) at configurable granularity (daily or weekly per person), connected by a flat priority-sorted Planning Queue. Weekly Family Meeting on Saturday/Sunday with integrated personal review (five phases: Personal Review, Review, Assess, Triage + Coordinate, Commit). Strict capture discipline: Quick Capture only during execution hours. OODA micro-loop for genuine emergencies only. |
| **DD-25** | The Goal Lifecycle (simplified) — five phases (Set, Cascade, Track, Score, Retire) across three primary timescales (annual, monthly, weekly) with quarterly reviews as deeper checkpoints. Yearly Review & Planning sets Goals and KPIs. Quarterly Reviews assess progress and course-correct. Monthly Audits are pivot points. Weekly Family Meeting Phase 3 provides the pulse check. Quarterly Key Results layer is **dormant** — reserved for future use if the household needs quarterly scoping. Progress tracked automatically via Project/Task completion percentage. Milestones are optional organizational containers for phasing work. Sub-Tasks are optional at Owner/Assignee discretion. Speedies are always standalone, never sub-tasks. Vision page lives at UB3 teamspace top level. |
| **DD-26** | The Project Lifecycle — six phases (Inception, Setup, Execution, Review, Completion, Archival). Two entry paths: top-down (OKR cascade, KR → Project) or bottom-up (emergent need recognized during triage). Project-worthiness test: multiple coordinated tasks + shared deliverable + timeframe. Status flow adds To Review for important items needing sign-off. Waiting On text property tracks blockers. Stalled detection at 14 days with no task completions. Batch archival during Monthly Audit and Quarterly Review. Ongoing-status projects are Workstreams with a modified lifecycle (no Target Deadline, no Completion phase). |
| **DD-27** | The Knowledge Formation Flow — CODE pipeline (Capture → Organize → Distill → Express) across two knowledge layers. Notion = Active Knowledge Surface (retrieval, operations). Heptabase = Deep Knowledge Workshop (synthesis, connection). Two paths: Reference Knowledge (C→O→done, most notes) stays in Notion; Synthesized Knowledge (C→O→D→E, fewer notes, highest value) flows through Heptabase. Destination Decision at Organize stage determines routing. Active Topics managed at Quarterly and Yearly reviews. Knowledge must serve an ultimate purpose — not accumulated for its own sake. |
| **DD-28** | The Triage & Processing Mechanics — operator's manual for inbox processing at three cadences. Daily: Task Inbox to zero, classify Speedies for batched execution, pull from Planning Queue. Weekly: Note Inbox to zero via DD-27 Organize Checklist, action system sweep, Household items jointly at Family Meeting. Monthly: stale inbox sweep, orphan metadata check, stalled project detection, batch archival, cross-lane recognition. Items needing partner input flagged via Housekeeping Queue (DD-24 Phase 5). No two-minute rule — quick items use the Speedy batch pattern instead. |
| **System Log** | The unified audit trail database for all significant system activity. Records changes across eight categories: Operational Events, Stewardship Changes, Design Decisions, Implementation, Schema Changes, System Configuration, Failure Patterns, and Documentation Updates. Each entry captures who, when, and why via lean database properties (for filtering/reporting) and type-specific page content templates (for detail). Distinct from the Implementation Playbook (curated agent-facing failure reference) and Design Decisions database (constitutional architectural choices). | DD-11 |

---

*This vocabulary is authoritative. When terms conflict with external framework definitions, the definitions on this page govern within our system.*
