---
notion_id: 3101e08b-9b34-81ca-ab4a-c07f0ac24a53
title: "The Command Center"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# The Command Center

> **For agents:** The Command Center is the shared home page of the Household Teamspace — the first thing both partners see when they open Notion. It is a **view layer** (DD-13): it owns no data, only surfaces filtered views from operational databases. When the user asks "what's happening?" or "what should I work on?", start here. When building new dashboard widgets, add them to the Command Center — never create standalone summary pages.

## Amendment Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-02-28 | Amended: "Mine" lens filter updated from Owner-based to Assignee-based per DD-12 two-layer model. "How Personal Views Work" section filled in. DD-12 cross-reference updated. | Owner (Select) cannot support dynamic "Me" filtering. Assignee (Person) enables per-user execution views. See DD-12 amendment. |
| 2026-03-01 | Amended: "Why This Works" section rewritten to clarify limits of dynamic filtering. Added naming convention ([Name]'s [Type]) per IB-10 discovery. Per-person view tabs are required for all personal views. | Full DD-12 compound filter requires hardcoded Owner name; Projects/Goals/Notes have no Assignee. "My X" naming is ambiguous on shared pages where both partners see the same tab bar. |

> **Note on filter references throughout this page:** Many table cells below still reference "Owner = Me" for the "Mine" lens. Per DD-12's two-layer model (amended 2026-02-28), the correct personal execution filter is: `(Assignee contains Me) OR (Owner = [self] AND Assignee is empty)`. The personal accountability filter is: `Owner = [self] OR (Owner = Household AND Assignee contains Me)`. "Ours" lens remains `Owner = Household`. The filter patterns in the "How Personal Views Work with Shared Databases" section below are authoritative.

## Design Decision

**DD-19:** The Command Center is the enhanced UB3 Dashboard page. It provides mission-level overview plus quick links to three personal Timescale Cockpits (My Day, My Week, My Year). Each cockpit shows a dual lens — "Mine" (Owner-filtered) and "Ours" (Household-filtered) — so each partner sees their personal work alongside household commitments at every timescale.

---

## Architecture Overview

The Command Center has two layers:

| Layer | What It Shows | Who Sees It |
|-------|-------------|-------------|
| **Mission Control** (top of page) | Household-wide overview: vital signs, household OKR progress, upcoming deadlines, recent System Log activity, quick actions | Both partners see the same content |
| **Personal Cockpits** (linked pages) | Three timescale views (My Day, My Week, My Year), each with "Mine" and "Ours" lenses | Each partner sees their own Owner-filtered views |

---

## The UB3 Dashboard Becomes the Command Center

The existing "Ultimate Brain for Notion" page is the Command Center. We enhance it, per DD-14's "extend don't replace" principle. The current UB3 structure maps naturally:

| Current UB3 Element | Command Center Role | Enhancement Needed |
|--------------------|--------------------|--------------------|
| Nav bar (Quick Capture, Tasks, Notes, Projects, Tags, Goals, Archive) | Keep as-is — fast navigation to raw database views | None for WS2 |
| Action Center (New Task, New Note, New Project buttons) | Keep as-is — primary capture entry points | None for WS2 |
| Common Views callout | Evolves into navigation hub for cockpits and key pages | Add My Day / My Week / My Year links prominently |
| Advanced Views callout | Consolidate into Common Views or keep as secondary nav | Minor restructuring |
| Inline Tasks/Notes/Projects/Tags views | Replace with Mission Control sections (see below) | Swap generic views for household-scoped dashboard views |
| OKR Command Center (linked page) | Becomes the strategic layer within Command Center hierarchy | Add Owner-filtered views (My OKRs vs. Household OKRs) |

---

## Mission Control Sections

These replace the current inline Tasks/Notes/Projects/Tags views on the UB3 Dashboard page. Each section pulls from shared operational databases using filtered views.

### 1. Vital Signs Strip

**Source:** Derived from The Compass (DD-18) vital signs definitions.
**Display:** A compact row of 6 indicators, each showing current status (Green/Yellow/Red).

| Vital Sign | Source Database | What It Shows |
|-----------|----------------|---------------|
| Inbox Zero Delta | Tasks (Inbox items) | How many unprocessed items are waiting |
| Task Completion Rate | Tasks | % of due tasks completed this week |
| OKR Cadence | Goals | Are quarterly check-ins happening on schedule? |
| Overdue Count | Tasks | Number of past-due tasks across both partners |
| Review Streak | Notes (journal entries) | Consecutive weeks with completed weekly reviews |
| Equity Index | Tasks + Projects | Task distribution balance between partners |

**Implementation note:** In WS2, this may start as a simple filtered view showing overdue/inbox counts. Full vital signs with color coding comes in WS4+ when formulas and rollups are mature.

### 2. Household OKR Snapshot

**Source:** Goals database, filtered: Owner = Household, Status = Active.
**Display:** Compact board or list showing current Yearly Goals with progress indicators (Projects/Tasks completion %). Optional Milestones shown as phase groupings when present.
**Links to:** OKR Command Center for full strategic view.

### 3. This Week's Priorities

**Source:** Tasks database, filtered: Due = This Week, sorted by Priority (P1 first).
**Display:** Combined view across both partners. Grouped by Owner so each partner can see the full household picture.
**Purpose:** "What needs attention across the whole household this week?"

### 4. Upcoming Deadlines

**Source:** Tasks + Projects databases, filtered: Due within next 14 days.
**Display:** Timeline or sorted list. Both partners' items visible, color-coded or grouped by Owner.
**Purpose:** "What's coming that we need to prepare for?"

### 5. Recent Activity Feed

**Source:** System Log database, sorted by Timestamp descending, limit 10.
**Display:** Compact feed showing what changed recently — new projects created, OKRs updated, system changes logged.
**Purpose:** "What just happened in our system?" Enables the partner who wasn't involved to stay informed.

### 6. Quick Navigation

**Display:** Card-style links to:

| Link | Target | Purpose |
|------|--------|---------|
| My Day | My Day cockpit (Owner-filtered) | Today's execution view |
| My Week | My Week cockpit (Owner-filtered) | Weekly planning and review |
| My Year | My Year cockpit (Owner-filtered) | Strategic and quarterly view |
| OKR Command Center | OKR Command Center page | Full strategic dashboard |
| Quick Capture | UB3 Quick Capture | Fast inbox entry |
| Family Meeting Prep | Meeting agenda template/view | Ready for coordination ritual |

---

## Timescale Cockpits: The Dual-Lens Pattern

Each person gets three timescale views. All three follow the same dual-lens pattern: a **"Mine"** section (Owner = Me) and an **"Ours"** section (Owner = Household, or all Owners combined). This means Nick and JR each see their personal work **and** the household context at every timescale.

### My Day (Daily Cockpit)

**Existing UB3 structure:** Plan → Execute → Wrap Up. This is the PEA rhythm — keep it.

**Enhancement: Dual lens on each section.**

| Section | "Mine" Lens | "Ours" Lens |
|---------|-------------|-------------|
| **Plan** | My tasks due today (Owner = Me, Due = Today) | Household tasks due today (Owner = Household, Due = Today) |
| **Execute** | My focus tasks, sorted by Energy/Priority | Partner's tasks today (read-only visibility — know what they're working on) |
| **Wrap Up** | My completed tasks today, journal entry | Household completions today |

**New addition:** A compact "Partner Pulse" strip at the top — shows what your partner has on their plate today (task count, any blockers flagged). Enables coordination without interrupting.

### My Week (Weekly Cockpit)

**Existing UB3 structure:** Clear & Reset → Reflect & Set Intent → Plan the Week. This maps directly to The Compass's Weekly Family Meeting cadence.

**Enhancement: Dual lens on each section.**

| Section | "Mine" Lens | "Ours" Lens |
|---------|-------------|-------------|
| **Clear & Reset** | My overdue tasks, my orphaned items | Household overdue tasks, unassigned items |
| **Reflect & Set Intent** | My last week's completions, my weekly journal | Household progress on shared OKRs, equity check |
| **Plan the Week** | My tasks for next week, my project milestones | Household priorities for next week, Family Meeting agenda items |

**New addition:** An "Equity Check" widget in the Reflect section — shows task/project distribution between partners this week. Surfaces imbalance early.

### My Quarter (Campaign Cockpit)

**New cockpit — no UB3 equivalent.** This fills the gap between weekly tactical execution and yearly strategic direction. A quarter is the natural unit for reviewing Goal progress and campaign-level initiatives.

**Dual lens:**

| Section | "Mine" Lens | "Ours" Lens |
|---------|-------------|-------------|
| **Goal Progress** | My Yearly Goals with progress % (Projects at Done + standalone Tasks completed / total) | Household Yearly Goals with progress % |
| **Active Projects** | My active Projects contributing to Yearly Goals | Household active Projects contributing to shared Goals |
| **Standards Check** | My recurring commitments and their adherence this quarter (gym, reading, etc.) | Household recurring commitments and their adherence (deep cleans, budget reviews, date nights, etc.) |
| **Goal Cascade Progress** | Visual rollup: Yearly Goal → my Projects/standalone Tasks completion % | Visual rollup: Household Yearly Goals → Projects/standalone Tasks completion % |

**New additions:**

- **Goal Cascade Progress widget** — shows how Yearly Goals are progressing as their linked Projects and standalone Tasks get completed. Goal progress = completed work items (Projects at Done + standalone Tasks completed) / total work items. Fully automated. When Milestones are used, they provide optional grouping but do not change the progress formula. Surfaces in both My Quarter and My Year.
- **Standards Check widget** — shows adherence to recurring commitments ("Standards") that aren't OKRs but represent operating norms the household wants to maintain. Standards are tracked as recurring Tasks with a "Standard" label. The widget shows completion rate over the quarter for each Standard. See Standards section below for full design.

### My Year (Strategic Cockpit)

**Existing UB3 structure:** Current Priorities callout, This Quarter view, This Year view.

**Enhancement: Dual lens on strategic content.**

| Section | "Mine" Lens | "Ours" Lens |
|---------|-------------|-------------|
| **Current Priorities** | My top 3 personal priorities this quarter | Household top 3 priorities this quarter |
| **This Quarter** | My Yearly Goals with Project/Task completion progress | Household Yearly Goals with progress |
| **This Year** | My Yearly Goals with cascade progress % (Projects/Tasks completion) | Household Yearly Goals with cascade progress %, shared Vision reference |

**New addition:** A **Goal Cascade Progress widget** (same as My Quarter) showing full-year rollup from Yearly Goals down through Projects and standalone Tasks. Complements The Compass's OKR Cadence vital sign.

---

## How Personal Views Work with Shared Databases

All operational databases live in the shared Household Teamspace (DD-12, DD-13). Personal views are created by filtering on the **two-layer responsibility model** (DD-12, amended 2026-02-28):

### For Task Views (My Day, Planning Queue, etc.)

Tasks have both Owner (Select) and Assignee (Person). Personal execution views use a compound filter:

**`(Assignee contains Me) OR (Owner = [self] AND Assignee is empty)`**

This shows: tasks explicitly assigned to me (from any Owner, including Household) + my own tasks that haven't been delegated. It excludes: my tasks delegated to agents, and household tasks not yet claimed by anyone.

### For Project and Goal Views (My Projects, My OKRs, etc.)

Projects and Goals have Owner only — no Assignee (they're stewardship containers, not execution items). Personal accountability views use:

**`Owner = [self] OR (Owner = Household AND Assignee contains Me)`**

For Projects specifically, since Projects don't have Assignee, the filter simplifies to `Owner = [self]` for the "Mine" lens. Household projects appear in the "Ours" lens (`Owner = Household`).

### The "Ours" Lens

Across all databases and timescales, the "Ours" lens is simply:

**`Owner = Household`**

This shows all household items regardless of assignee — the strategic/coordination view used during Family Meetings and for household-wide oversight.

### Why This Works — and Its Limits

The `Person contains Me` filter on Assignee is **dynamic** — it resolves to the currently logged-in user. This means the Assignee clause of the compound filter works identically for both partners from a single view definition.

**However**, the full DD-12 Personal Execution filter is: `(Assignee contains Me) OR (Owner = [self] AND Assignee is empty)`. The Owner fallback clause requires a **hardcoded person name** (e.g., "Nick" or "JR") because Owner is a Select property, not a Person property. This means Task views still require per-person view tabs despite the dynamic Assignee clause.

For Projects, Goals, and Notes — which have Owner only, no Assignee — all personal views require hardcoded name filters and therefore per-person view tabs.

**Naming convention (established by IB-10):** All personal view tabs use the pattern "[Name]'s [Type]" — e.g., "Nick's Tasks", "JR's Notes" — rather than "My X". This avoids ambiguity on shared pages where both partners see the same tab bar. Page names (My Day, My Week, etc.) remain unchanged.

---

## Standards: Recurring Commitments That Aren't Goals

Standards are distinct from OKRs. OKRs are aspirational stretch targets; Standards are **recurring commitments you want to maintain** — the operating norms of your life and household.

**Examples of Standards:**

| Standard | Owner | Frequency | Metric |
|----------|-------|-----------|--------|
| Go to gym | Personal | 3x/week | Sessions completed / target |
| Quarterly deep clean | Household | 1x/quarter | Completed yes/no |
| Monthly budget review | Household | 1x/month | Completed yes/no |
| Read 30 min/day | Personal | Daily | Days completed / target |
| Date night | Household | 2x/month | Completed count / target |
| Meal prep Sunday | Household | 1x/week | Completed yes/no |

**How Standards are tracked:** Standards are recurring Tasks in the UB3 Tasks database with the Label "Standard". This reuses existing infrastructure — no new database needed. The recurring task mechanism already handles frequency. The "Standard" label allows filtered views that isolate Standards from regular tasks.

**Standards Check widget:** Surfaces in My Quarter and My Week cockpits. Shows:

- Each Standard with its target frequency
- Adherence rate over the period (e.g., "Gym: 10/12 sessions this quarter = 83%")
- Green/Yellow/Red indicator based on adherence thresholds (e.g., >80% Green, 60-80% Yellow, <60% Red)

**Architectural home:** Standards as a *concept* live in The Compass (DD-18) — they're part of the system's self-monitoring. Standards as *data* live in the Tasks database. Standards as *views* appear in the Timescale Cockpits.

---

## System Integrity

> **Note:** System Integrity monitoring (workspace technical health) is defined in **DD-18 (The Compass)**, not here. The Command Center merely *displays* a System Health indicator in the Mission Control vital signs strip, linking to the System Diagnostics page maintained by The Compass. See The Compass spec for the full monitoring logic, check categories, and diagnostics page design.

---

## Interaction with Other Design Decisions

| DD | Relationship |
|----|-------------|
| DD-13 | Defines the Command Center as one of four Household Teamspace sections. DD-19 specifies what goes inside it. |
| DD-12 | Workspace Architecture: two-layer responsibility model (Owner for accountability, Assignee for execution). Command Center uses Assignee-based filters for personal "Mine" views and Owner-based filters for "Ours" views. See DD-12 amendment (2026-02-28). |
| DD-14 | Extend UB3, don't replace. The UB3 Dashboard page is kept and enhanced, not rebuilt. |
| DD-09 | Hybrid OKR structure (simplified hierarchy — DD-25 amendment 2026-03-01). The Command Center surfaces both Household and Personal Yearly Goals via Owner filters. Progress tracked via Project/Task completion. |
| DD-18 | The Compass defines the vital signs that the Mission Control strip displays. Review cadences map to cockpit timescales. |
| DD-08 | Family Meeting is the primary coordination ritual. My Week's "Ours" lens serves as the Family Meeting prep surface. |
| DD-15 | Front Desk triage routes items that appear in Command Center views. Inbox count in Vital Signs strip reflects Front Desk throughput. |

---

## Key Principle: View Layer, Not Storage Layer

The Command Center and all cockpits are pure view layers. They display filtered content from shared operational databases. This means:

- Changing the Command Center layout never affects the underlying data
- New views can be added or rearranged freely
- Both partners see the same structural page but different filtered content
- Agents should never write data to the Command Center — they write to databases, and the Command Center reflects the changes automatically

---

*The Command Center is the system's face. It answers the question every productivity system must answer: "What should I pay attention to right now?" The dual-lens pattern ensures that question is always answered in context — personal context and household context, at every timescale.*
