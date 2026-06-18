---
notion_id: 30f1e08b-9b34-8128-b2e6-f65baad6b020
title: "Household Teamspace Structure"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Household Teamspace Structure

> **For agents:** The Household Teamspace is where all operational data and system infrastructure lives. It has four top-level sections: Command Center, System Documentation, Areas, and Operational Databases. When creating new content, place it in the correct section. When looking for data, start at the Command Center or navigate directly to the relevant database. Never create top-level pages outside these four sections without human approval.

## The Four Sections (DD-13)

The Household Teamspace is organized into four top-level sections, each serving a distinct purpose:

| Section | Purpose | Primary Users | Update Frequency |
|---------|---------|-------------|-----------------|
| **Command Center** | Shared dashboard and daily home page | Both partners, daily | Dynamic — views refresh automatically from databases |
| **System Documentation** | Governance, architecture, system rules | Builders and agents during design; agents during operation | Stable — updated when design decisions change |
| **Areas** | Knowledge hubs organized by PARA Area | Both partners as needed; agents for context | Moderate — reference content grows over time |
| **Operational Databases** | Raw database infrastructure | Agents primarily; humans via views | Continuous — items created and modified daily |

---

## Command Center

**What it is:** The shared home page that both partners land on when they open Notion. It surfaces what matters right now — active goals, this week's priorities, recent activity, and quick links to personal views.

**Key design principle:** The Command Center is a **view layer, not a storage layer**. It owns no data. Everything it displays is pulled from databases that live in the Operational Databases section. This means the Command Center can evolve its layout freely without affecting the underlying data model.

**What it surfaces (at maturity):**

| Section | Source | Purpose |
|---------|--------|---------|
| Active Household OKRs | OKRs database, filtered: Owner = Household, Status = Active | What are we working toward as a household? |
| This Week's Priorities | Tasks database, filtered: Due = This Week, sorted by priority | What needs attention now? |
| Personal Quick Links | Links to My Day, My Inbox, My OKRs views | One-click access to personal filtered views |
| Recent System Log | System Log database, sorted: Timestamp descending, limit 10 | What just happened in the system? |
| Area Health Summary | Derived from Area pages and project status | Are any Areas falling behind? |
| Upcoming Deadlines | Tasks/Projects database, filtered: Due = Next 14 Days | What's coming? |
| Family Meeting Prep | Embedded view or link to meeting agenda template | Ready for the next coordination ritual |

> **For agents:** When asked to "show current priorities" or "what's happening this week," pull data from the Command Center's source databases using the filters above. Do not create standalone summary pages — the Command Center handles this through live views.

---

## System Documentation

**What it is:** The governance layer — how the system works, what the rules are, what decisions have been made. This is the existing System Documentation section, already well-built.

**Current contents:**

| Sub-section | Purpose |
|------------|---------|
| **Architecture** | Framework Integration Map, Capturing Beast, Execution Beast, Personal/Household Model, System Log spec, Workspace Architecture, this page, Vocabulary, Design Decisions database |
| **ICOR** | The meta-framework definition and stage mappings |
| **System Health Dashboard** | Metrics and status indicators |
| **2026-2030 Household Vision** | Strategic direction and archived vision history |

**Who uses it and when:**

- **Humans**: When designing new system components, debugging workflows, or onboarding a new partner to a concept
- **Agents**: On every operation — agents should read relevant Architecture pages before taking action in unfamiliar territory
- **Together during reviews**: When evaluating whether the system is working as designed (REFINE stage)

---

## Areas

**What it is:** Knowledge hubs organized by PARA Area. Each Area page serves as both a reference library and an operational gateway.

**Current Areas** *(per DD-23 as amended 2026-02-28, all Owner = Household):*

| Area | Type | Hub Contains |
|------|------|-------------|
| Career | Hybrid (shared + Nick + JR sub-tags) | Shared career strategy, individual career tracking via sub-tags |
| Character | Hybrid (shared + Nick + JR sub-tags) | Joint growth initiatives, individual development via sub-tags |
| Social | Hybrid (shared + Nick + JR sub-tags) | Shared social life, individual friendships via sub-tags |
| Wardrobe | Hybrid (shared + Nick + JR sub-tags) | Shared wardrobe research, individual style/measurements via sub-tags. DD-16 databases separate. |
| Beauty | Pure Household (Lead: JR) | Skincare, haircare, grooming routines, personal care products, beauty research |
| Finances | Pure Household | Budgeting, banking, investments, taxes, insurance |
| Health | Pure Household | Meal planning, fitness, medical records, health insurance, personal health goals |
| Household | Pure Household | Home management, maintenance, domestic operations |
| Legal | Pure Household | Contracts, estate planning, compliance |
| Relationship | Pure Household | Partnership health, couples planning, date nights |
| Travel | Pure Household | Trip planning, loyalty programs, passport management |

**Dual role of Area pages:**

1. **Knowledge hub** — Static reference content. The Wardrobe fabric glossary, financial account numbers, legal document storage. This content lives directly on or under the Area page.
2. **Operational gateway** — Embedded database views filtered by Area. "All tasks in Finances," "Active projects in Health & Wellness," "OKRs touching Household." These views pull from the shared Operational Databases.

As operational databases come online (WS2+), each Area page will gain embedded views that show operational activity for that Area. The Area page becomes a one-stop view of both what you know (knowledge) and what you're doing (operations) in that domain.

> **For agents:** Area pages are **Household** infrastructure, not personal. Even when one partner is Lead for an Area (Stewardship model), both partners and all agents can read and reference Area content. When creating reference content, place it under the appropriate Area. When creating actionable items, place them in Operational Databases with the Area property set correctly.

---

## Content Routing

**"I have something new — where does it go?"**

Use this decision tree when creating or saving content in Notion:

| If the content is... | Then it goes... | Examples |
|---------------------|----------------|---------|
| **Actionable or trackable** | In a UB3 database (Tasks, Projects, Goals, Notes, Work Sessions) with Owner and Area tag set | A task to research moisturizers, a project to redo the budget, a goal to run a half-marathon, a meeting note |
| **Standing reference content** | As a sub-page under the relevant Area page in the Tags DB | The household skincare routine, a packing list template, account credentials reference, fabric care guide |
| **System governance or architecture** | As a sub-page under System Documentation | A new Design Decision spec, a process document, the Handoff Prompt, the Implementation Playbook |
| **A dashboard or view layer** | Under the Command Center (or as a linked view on an existing page) | A new cockpit view, a weekly summary dashboard, a filtered task list |

### Key Principles

1. **Databases are for items you track and filter.** If you'll want to see it in My Day, filter by Area, or mark it Done — it's a database entry.
2. **Page hierarchy is for content you browse and reference.** If it's a living document, a how-to guide, or a reference sheet — it's a sub-page under an Area.
3. **Don't double up.** A skincare routine doesn't need both a Notes DB entry *and* an Area sub-page. Pick one home. For reference content, prefer the Area sub-page.
4. **Area pages are knowledge hubs.** Each Area's page in the Tags DB can have child pages underneath it. This is where standing reference material lives — organized by Area, browsable in the sidebar.
5. **Tags are for classification, not storage.** You tag a Task with "Beauty" so it appears in Beauty's filtered views. But the skincare routine document lives *under* the Beauty page as a child — no tag needed on it.

> **For agents:** When a user asks you to "save" or "create" something, use this routing table. If it's reference content (a guide, a list, a how-to), create it as a child page under the appropriate Area in the Tags DB. Do not create Notes DB entries for standing reference content unless the user specifically asks for a tagged note.

---

## Operational Databases

**What it is:** The raw database infrastructure where all actionable and trackable items live. These are Notion databases (not pages) that serve as the system's single source of truth for work.

**Planned databases:**

| Database | ICOR Stage | Purpose | Key Properties |
|----------|-----------|---------|----------------|
| **Inbox** | Input | Raw captures from the Capturing Beast awaiting processing | Owner, Source, Capture Date, Status (Unprocessed/Processed/Discarded) |
| **Tasks** | Output | Individual actionable items (Tasks and Speedies) | Owner, Assignee, Area, Project, Due Date, Priority, Status, Type (Task/Speedy) |
| **Projects** | Output | Multi-step initiatives with defined outcomes | Owner, Area, Workstream, Status, Start Date, Target Date, OKR Link |
| **OKRs** | Control/Output | Objectives and Key Results at Household and Personal levels | Owner, Level (Household/Personal), Time Horizon, Status, Parent Goal |
| **System Log** | Refine | Audit trail of all significant system changes | Log Entry, Change Type, Actor, Affected Item, Old Value, New Value, Rationale, Timestamp, Area |

> **For agents:** These databases are the **only** place where actionable items should be created. Never create tasks, projects, or OKRs as standalone Notion pages outside these databases. Every item must have an Owner property set. When in doubt about which database an item belongs in, check the Capturing Beast routing rules and Execution Beast taxonomy.

**Note on Ultimate Brain 3.0:** The existing Thomas Frank template includes its own database structure (Tasks, Projects, Notes, etc.). During WS2, these will need to be reconciled — either adopted as-is with property additions, migrated into new databases matching the architecture specs, or bridged with relations. This reconciliation is a WS2 deliverable.

---

## Evolution Roadmap

| Workstream | Command Center | System Documentation | Areas | Operational Databases |
|-----------|---------------|---------------------|-------|----------------------|
| **WS1** (Framework Reconciliation) | Placeholder with curated links | Rich and growing — primary focus of current work | Reference content reorganized (done) | Not yet created |
| **WS2** (Database Buildout) | First embedded views appear (OKRs, Tasks) | Stable; updated as new DDs emerge | Gain embedded operational views per Area | Created and populated; Ultimate Brain reconciliation |
| **WS3** (Workflows) | Inbox count, Capturing Beast status, PEA rhythm widgets | Capturing Beast and Execution Beast specs finalized | Area Briefs created for stewardship handoffs | Inbox database operational; workflow automations wired |
| **WS4** (Automation) | Agent activity feed, automated priority surfacing | Agent behavior rules refined from real usage | Area Health metrics automated | Agent read/write patterns established |
| **WS5** (Reviews & Rituals) | Family Meeting prep auto-generated, review dashboards | REFINE stage documentation mature | Area review cadences embedded | Review-related views and rollups added |
| **WS6** (Optimization) | Fully dynamic, personalized, agent-enhanced | Living document with version history | Mature knowledge + operations hubs | Schema optimized based on real usage patterns |

---

## Interaction with Other Design Decisions

- **DD-12** (Workspace Architecture): This page details the internal structure of the Household Teamspace defined in DD-12. The Command Center, System Documentation, Areas, and Operational Databases all live within the shared Teamspace.
- **DD-09** (Personal/Household Model): The Owner property is how personal items are scoped within the shared Operational Databases. The Command Center uses Owner filters to show personal quick links.
- **DD-06** (Output Elements): The Operational Databases section implements the Output Elements taxonomy — Tasks and Speedies in the Tasks database, Projects in the Projects database, Goals as OKRs.
- **DD-10** (Capturing Beast): The Inbox database in Operational Databases is where the Capturing Beast routes raw captures. The Command Center surfaces unprocessed inbox items.
- **DD-11** (System Log): The System Log database lives in Operational Databases. The Command Center surfaces recent log entries for visibility.

---

*This page is authoritative. When questions arise about where new content should live within the Household Teamspace, use the four-section model and the descriptions above. When building new features, consult the Evolution Roadmap to understand what's expected at each stage.*
