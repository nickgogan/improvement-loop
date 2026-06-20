---
notion_id: 3101e08b-9b34-81ad-b0e2-d80487685145
title: "UB3 Template Updates"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# UB3 Template Updates

> **For agents:** This page catalogs all Ultimate Brain 3.0 template updates that need to be applied to our copy. Since UB3 is a Notion template, updates are not automatic — each must be manually implemented. Check the Status column before making changes; some may already be present in our copy. Source: `UltimateBrainChangelog.pdf` in the workspace folder.

---

## Update 1: 2026-02-07 — Recurring Task Improvements, Notes <-> Tasks, and More

### 1A. Recurring Task Improvements (Enforce Schedule)

**Status:** Applied (IB-30, Feb 25 2026 — human steps)

**Databases affected:** Tasks

**Changes:**

**New property:** `Enforce Schedule` — Checkbox property in the Tasks database.

- Purpose: When checked on a recurring task, prevents the task from being pushed forward if it isn't completed on time. Instead, it will revert to its original schedule.
- Example: A task scheduled for every Monday with Enforce Schedule checked — if you don't complete it on Monday, it will still show next Monday as the next due date rather than pushing forward from when you last completed it.

**Updated formula:** `Next Due` formula must be replaced with the new version.

- The new formula incorporates the Enforce Schedule logic.
- The old formula only considered Postpone; the new one considers both Postpone and Enforce Schedule.

**Implementation steps:**

1. Open the Tasks database
2. Add a new Checkbox property called `Enforce Schedule`
3. Find the `Next Due` property (formula type)
4. Replace the entire formula with the new version from the upgrade guide
5. Test with a recurring task: create a task with a recurrence rule, check Enforce Schedule, and verify Next Due behaves correctly

**Formula (Next Due replacement):**
See upgrade guide in `UltimateBrainChangelog.pdf` pages 6-8 for the exact formula text. The formula is very long and must be copied exactly.

---

### 1B. Notes <-> Tasks Relation

**Status:** Applied (IB-31, Feb 25 2026 via MCP)

**Databases affected:** Tasks, Notes

---

### 1C. Books <-> Notes Relation

**Status:** Applied (IB-32, Feb 25 2026 via MCP)

**Databases affected:** Books, Notes

**Changes:**

**New relation:** Two-way relation between Books and Notes databases.

- Allows linking book entries to notes taken about them.
- Supports the Zettelkasten literature notes workflow.

**Implementation steps:**

1. Open the Books database
2. Add a new Relation property pointing to the Notes database
3. Name it `Notes` (on the Books side)
4. Enable "Show on Notes" — the reverse relation on the Notes side should be named `Books`
5. This creates a two-way link: Books <-> Notes

---

### 1D. Time Tracking Improvements (Recurring Tasks Fix)

**Status:** Applied (IB-33, Feb 25 2026 — human steps)

**Databases affected:** Tasks

**Changes:**

**Problem fixed:** Time tracking on recurring tasks was accumulating across all recurrences instead of resetting. When a recurring task was completed and re-created, the new instance carried over all previous work session time.

**New view:** `Non-Recurring Source` view in the Tasks database.

- Filters to show only non-recurring source tasks (i.e., the original templates for recurring tasks).
- Purpose: Makes it easier to find and manage the "source" recurring task entries.

**Updated formula:** Time tracking formulas updated to properly handle recurring task resets.

**Implementation steps:**

1. Open the Tasks database
2. Find the relevant time tracking formula properties
3. Update the formulas per the upgrade guide (see `UltimateBrainChangelog.pdf` pages 14-17)
4. Create a new view called `Non-Recurring Source` with the filter: `Recurring` is not checked AND `Type` is not "Recurring Source" (or equivalent filter from the guide)
5. Test: Create a recurring task, log work sessions, complete it, verify the new recurrence starts with zero time

---

## Update 2: 2025-01-23 — Time Tracking, Daily Planning, Sub-Tasks, and More

### 2A. Time Tracking System

**Status:** Already present (confirmed via schema audit Feb 23 2026 — IB-34)

**Databases affected:** Tasks, Work Sessions

**Changes:**
Major new time tracking capability with formula updates to the Tasks database. Includes new calculated properties for tracking time spent on tasks via the Work Sessions relation.

**Implementation steps:**
See `UltimateBrainChangelog.pdf` pages 18-20 for the detailed formula replacement guide. This involves updating multiple formula properties in the Tasks database.

---

### 2B. Daily Planning Properties

**Status:** Already present (confirmed via schema audit Feb 23 2026 — IB-35)

**Databases affected:** Tasks

**Changes:**

**Three new views/properties** for daily planning:

- `Energy` — Categorize tasks by energy level required (High Energy, Low Energy, etc.)
- `Location` — Where the task needs to be done
- `P/I` (Process/Immersive) — Whether the task is process work (routine, shallow) or immersive work (deep focus)

These replace the old `Contexts` property (which should be deleted if present).

**Implementation steps:**

1. Add Energy, Location, and P/I select properties to the Tasks database (if not present)
2. Create corresponding filtered views in the Daily Planning section
3. Delete the old `Contexts` property if it exists

---

### 2C. Track Tasks in Areas

**Status:** Applied (IB-36, Feb 25 2026 — human steps)

**Databases affected:** Tasks, Areas

**Changes:**

**New view:** `Active Tasks` view added to the Area template page.

- Shows all active tasks linked to that Area.
- Makes it easy to see what's happening in each life domain.

**New automation:** `Create Ongoing Project for Areas`

- Automatically creates a linked project for each Area.

**Implementation steps:**

1. In each Area template page, add a linked view of the Tasks database filtered by that Area's tag
2. Set up the automation per the guide

---

### 2D. Sub-Task Automations

**Status:** Applied (IB-37, Feb 25 2026 — human steps)

**Databases affected:** Tasks

**Changes:**

**Three new automations (disabled by default in new copies):**

1. **Task Done → Close All Open Sub-Tasks** — When a parent task is marked Done, all its sub-tasks are automatically marked Done
2. **Sync Parent/Sub-Task Projects & People** — When a sub-task is created, it inherits the Project and People from its parent task
3. **Change Project → Remove Parent Task** — When a sub-task's Project is changed to differ from its parent's Project, the parent-child link is removed

**Implementation steps:**

1. Check if these automations exist in the Tasks database
2. If not, create them per the guide
3. Enable the ones you want active (recommended: all three)

---

### 2E. Tweaks and Bug Fixes

**Status:** Applied (IB-38, Feb 23 2026 — human steps + schema audit)

**Databases affected:** Tasks, multiple views

**Changes:**

- **My Day** is now a pinned property in Tasks
- **Plan My Week → Recurring view** — Status column changed to Checkbox display
- **My Day → Wrap Up → Calendar** — Filters updated for My Day unchecked behavior
- **Deleted properties** (remove if present): `Next Due API`, `UTC`, `Recurring Tasks Divider`, `Contexts`
- **New property:** `Shopping List` — Checkbox in Tasks database
- **Set Completion Dates** and **Clear Completion Dates** automations — enabled by default
- **Clear Completion Date** automation updated

**Implementation steps:**

1. Audit which of these changes are already in our copy
2. Pin the My Day property if not pinned
3. Delete deprecated properties if they exist: Next Due API, UTC, Recurring Tasks Divider, Contexts
4. Add Shopping List checkbox if not present
5. Check and enable completion date automations
6. Update view filters per the guide

---

## Update 3: 2024-12-06 — Tags Renamed to Labels

### 3A. Tags → Labels Rename

**Status:** Already present (confirmed via schema audit Feb 23 2026 — IB-39)

**Databases affected:** Tasks

**Changes:**
The multi-select property `Tags` in the Tasks database was renamed to `Labels`. This is a simple rename — no data loss.

**Implementation steps:**

1. Check if the Tasks database has a property called `Tags` (multi-select)
2. If yes, rename it to `Labels`
3. If it's already called `Labels`, this update is already applied

---

## Audit Results (Feb 23 2026)

Audit performed by agent against live database schemas.

**Tasks database:**

- [x] `Energy` select — Present (High, Low)
- [x] `Location` select — Present (Home, Office, Errand)
- [x] `P/I` select — Present (Process, Immersive)
- [x] `Shopping List` checkbox — Present
- [x] `Labels` multi-select — Present (Tags → Labels rename already applied)
- [x] Time Tracking system — Sessions relation, Time Tracked formulas, Start/End buttons, Current Session, Time Tracking Status all present
- [x] Deprecated properties — None found (Next Due API, UTC, Recurring Tasks Divider, Contexts all absent)
- [x] `Enforce Schedule` checkbox — Applied (IB-30, Feb 25 2026)
- [x] `Notes` relation (→ Notes DB) — Applied (IB-31, Feb 25 2026)

**Books database:**

- [x] `Notes` relation (→ Notes DB) — Applied (IB-32, Feb 25 2026)

**Notes database:**

- [x] `Tasks` relation (→ Tasks DB) — Auto-created via DUAL (IB-31)
- [x] `Books` relation (→ Books DB) — Auto-created via DUAL (IB-32)

**Human-confirmed (cannot verify via API):**

- [x] Automations (Sub-Task, Completion Date, etc.) — User-confirmed (IB-37, IB-38, Feb 25 2026)
- [x] `Non-Recurring Source` view in Tasks — User-confirmed (IB-33, Feb 25 2026)
- [x] `Active Tasks` view in Area templates — User-confirmed (IB-36, Feb 25 2026)
- [x] Energy, Location, P/I filtered views in Daily Planning — User-confirmed (IB-35, Feb 23 2026)
- [x] Time tracking formula updates for recurring tasks (1D) — User-confirmed (IB-33, Feb 25 2026)

**Summary:** All updates applied. Feb 2026 items (1A-1D) completed Feb 25 2026. Jan 2025 and Dec 2024 updates were already present in our copy.

---

## Implementation Order

1. **Audit first** — Run the checklist above to determine current state
2. **Relations** (1B, 1C) — Simple, no formula risk
3. **Simple properties** (1A checkbox, 2B selects, 2E Shopping List, 3A rename) — Low risk
4. **Views** (1D, 2B, 2C) — Medium complexity
5. **Automations** (2D, 2E) — Review before enabling
6. **Formulas** (1A Next Due, 1D time tracking, 2A time tracking) — Highest risk, do last, test thoroughly
