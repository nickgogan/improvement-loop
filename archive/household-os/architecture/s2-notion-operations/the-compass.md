---
notion_id: 3101e08b-9b34-8160-a947-c711b190a0c8
title: "The Compass"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# The Compass

> **For agents:** The Compass is the REFINE stage orchestrator. It governs how the system improves itself. Before proposing changes to review cadences, health metrics, or system rituals, check this page for the canonical definitions. The Compass is the fourth named component alongside the Capturing Beast (Input), the Front Desk (Control), and the Execution Beast (Output).

---

## Amendment Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-02-28 | Clarified: "filtered by Owner" references in Daily Pulse and Notion Implementation updated to reflect DD-12 two-layer model. Personal execution views filter on Assignee, not Owner. | See DD-12 amendment (2026-02-28). |
| 2026-03-17 | Inserted new step 3 in Cadence 3 (Monthly Audit) referencing DD-28 monthly processing steps. Renumbered prior step 3 to step 4. | Gap Resolution Decision Log — 2026-03-17 session. |

---

## Core Decision

**DD-18:** The Compass is the REFINE stage orchestrator — the system's self-improvement engine. It operates through five review cadences, monitors six vital signs, enforces a time budget, and defines emergency response protocols.

---

## What Is the Compass?

The four named components of the system map to ICOR stages:

| ICOR Stage | Component | Question It Answers | Action |
|-----------|-----------|-------------------|--------|
| **INPUT** | The Capturing Beast | Should this enter the system? | Filter, route personal vs. household |
| **CONTROL** | The Front Desk | Now that it's in, what happens to it? | Triage, prioritize, assign, coordinate |
| **OUTPUT** | The Execution Beast | How does the work get structured and done? | Goals → Projects → Tasks, PEA rhythm |
| **REFINE** | **The Compass** | Is the system working? What needs to change? | Review, measure, rebalance, course-correct |

The Compass is **reflective, not reactive**. The Front Desk makes in-the-moment decisions about individual items. The Compass steps back and asks whether the *whole system* is pointing in the right direction.

> **Metaphor:** If the Execution Beast is the engine and the Front Desk is the steering wheel, the Compass is the navigation system — it tells you whether you're on course, how far you've drifted, and when you need to reroute.

---

## The Five Review Cadences

The Compass operates at five timescales, each building on the one below:

### Cadence 1: Daily Pulse (5 minutes)

**When:** Every morning
**Who:** Each partner individually
**Purpose:** Orient for the day. Not system maintenance — just awareness.

| Step | Action | Notion View |
|------|--------|-------------|
| 1 | Review today's calendar | Google Calendar (external) |
| 2 | Check My Day tasks | Tasks → My Day view (filtered by Assignee per DD-12 two-layer model) |
| 3 | Mark completions from yesterday | Tasks → My Day view |
| 4 | Set today's focus (1-3 items) | Tasks → My Day view → drag to top |

> **Design constraint:** The Daily Pulse must stay under 5 minutes. If it consistently takes longer, the system is too complex.

---

### Cadence 2: Weekly Family Meeting (60-90 minutes)

**When:** Weekly (day TBD by household)
**Who:** Both partners together
**Purpose:** The primary sync point. Part Control work, part Refine work.

| Phase | Duration | Activity | ICOR Stage |
|-------|----------|----------|-----------|
| **1. Inbox Processing** | ~20 min | Triage all captured items. Run Front Desk sequence on each. Clear the inbox to zero. | Control |
| **2. Project Review** | ~20 min | Walk through active projects. Ensure each has a next action. Flag stalled projects. Rebalance assignments. | Control + Output |
| **3. Goal Progress** | ~15 min | Check OKR Command Center. Are Key Results on pace? Any that need intervention? | Output + Refine |
| **4. Health Scan** | ~5 min | Check the six vital signs (below). Note any Yellow/Red indicators. | Refine |
| **5. Planning** | ~10 min | Set priorities for the coming week. Assign who's doing what. Record meeting notes. | Control + Output |

Note: The Family Meeting straddles Control and Refine (per DD-08, Overlap Resolution #6 in the Framework Integration Map). Phases 1-2 are Control work. Phase 4 is pure Refine. Phases 3 and 5 bridge both.

---

### Cadence 3: Monthly Audit (15 minutes)

**When:** First Family Meeting of each month
**Who:** Both partners
**Purpose:** Spot trends. Catch drift before it becomes a crisis.

**Monthly audit protocol:**

1. **Trend review** — Check 4-week trends on: inbox count, active projects, time investment, OKR pacing
2. **Warning signal scan** — Run through the Behavioral Warning Signs checklist (see Emergency Protocols below)
3. **DD-28 monthly processing steps** — Execute the full monthly processing cadence from DD-28 Cadence 3: stale inbox sweep, orphan metadata check, stalled project detection, knowledge health check, batch archival, and cross-lane recognition.
4. **Decision rule:** 0-1 warnings = healthy (green). 2-3 warnings = discuss (yellow). 4+ warnings = trigger protocol (red).

---

### Cadence 4: Quarterly Deep Review (60 minutes)

**When:** End of each quarter
**Who:** Both partners
**Purpose:** Strategic course correction. The big-picture check.

**Quarterly protocol:**

1. **OKR Retrospective** — Score each Key Result: Achieved / Partially Achieved / Missed. Analyze what worked and what didn't.
2. **Project Velocity** — Projects started vs. completed this quarter. Is the ratio healthy?
3. **System ROI Check** — At ~10 hours/month on system maintenance, is the value received worth the investment?
4. **Failure Mode Assessment** — Review all five emergency protocol trigger conditions. Any close calls?
5. **Simplification Review** — Delete unused properties. Archive unused views. Reduce friction.
6. **Vision Alignment** — Read the household Vision aloud. Can every active project connect to it?
7. **Next Quarter Planning** — Set new OKRs. Cascade into Projects and Key Results.

---

### Cadence 5: Annual Reset (3 hours)

**When:** January or start of fiscal year
**Who:** Both partners
**Purpose:** Full system health check and strategic refresh.

**Annual protocol:**

1. Full year retrospective with adoption analysis
2. Zombie purge: archive all projects paused/deferred >6 months
3. System redesign decisions: for each major component, vote Keep / Abandon / Add
4. Vision refresh: rewrite or reaffirm the household Vision
5. Annual OKR setting: Yearly Objectives for the next 12 months

---

## The Six Vital Signs

The Compass monitors six metrics that indicate system health. Each has three zones:

| Vital Sign | Green (Healthy) | Yellow (Watch) | Red (Act Now) |
|-----------|-----------------|----------------|---------------|
| **Inbox Count** | <20 items | 20-30 items | >50 items |
| **Active Projects** | 3-7 projects | 8-10 projects | >15 projects |
| **Zombie Projects** (paused >30d) | <5 projects | 5-10 projects | >20 projects |
| **Projects Without Next Actions** | 0 | 1-3 projects | >5 projects |
| **Overdue Tasks** | <5 tasks | 5-10 tasks | >20 tasks |
| **OKR Progress** | On pace for quarter | <30% of expected | <15% of expected |

---

## Time Budget

The system must not become a burden. The Compass enforces a strict time budget.

**Weekly time target: <120 minutes total**

| Activity | Target | Notes |
|----------|--------|-------|
| Daily Pulse (7 days) | 35 min | ~5 min each morning |
| Family Meeting | 60 min | Target under 90 min |
| Ad-hoc system work | <30 min | Tweaks, cleanup, agent interactions |
| **Total** | **<120 min/week** | |

**Thresholds:**

- Green: <120 min/week — Healthy
- Yellow: 120-180 min/week — Creeping up, discuss why
- Red: >180 min/week for 3+ weeks — Trigger Protocol 1 (Too Heavy)

---

## Emergency Response Protocols

Five protocols for when the system shows signs of dysfunction. Each has a defined trigger and a structured response.

### Protocol 1: Too Heavy Syndrome

**Trigger:** Time investment >150 min/week for 3 consecutive weeks

**Response:**

1. Freeze new entries for 1 week
2. Emergency simplification meeting (60 min)
3. Implement 3 quick wins (delete unused properties, archive views, simplify dashboard)
4. Reduce Family Meeting to biweekly temporarily
5. Reassess in 2 weeks

### Protocol 2: Vision Drift

**Trigger:** <50% of active projects connect to Objectives OR can't articulate Vision

**Response:**

1. Vision refresh session (90 min)
2. Audit all projects for Vision connection
3. Realign OKRs
4. Add "Read Vision aloud" to every Quarterly Review

### Protocol 3: Project Stall Recovery

**Trigger:** 3+ projects in Planning status for >30 days with 0 tasks

**Response:**

1. Forced choice per project:
   - Define 3 next actions and move to In Progress, OR
   - Defer, OR
   - Archive
2. No fourth option. Decide now.

### Protocol 4: Zombie Apocalypse

**Trigger:** >20 Paused/Deferred projects OR >50 total projects

**Response:**

1. Dedicated 2-hour session
2. Rapid decision per project: Reactivate / Defer / Archive
3. Goal: reduce count by >50%

### Protocol 5: Life Disruption (Emergency Mode)

**Trigger:** Major life crisis (job loss, health emergency, move, etc.)

**Response:**

1. Reduce to 3 critical projects. Pause everything else.
2. Change Family Meeting to biweekly
3. Split responsibility so neither partner is overwhelmed
4. Document the emergency and decisions made
5. Schedule "System Reboot" session 3 months out

### Emergency Decision Card

Quick reference for which protocol to trigger:

| IF... | THEN... |
|-------|---------|
| Time >180 min/week for 3 weeks | Protocol 1 (Too Heavy) |
| Can't articulate Vision | Protocol 2 (Vision Drift) |
| 3+ projects stalled >30 days | Protocol 3 (Project Stall) |
| >20 zombie projects | Protocol 4 (Zombie Apocalypse) |
| Major life crisis | Protocol 5 (Life Disruption) |
| Either partner says "system isn't working" | STOP. 48-hour cooling period, then discuss. |

---

## Behavioral Warning Signs

Checked during the Monthly Audit. Each one signals potential system dysfunction:

- Either partner skipped 2+ consecutive Family Meetings
- One partner stopped updating tasks for >7 days
- Hearing "I'll just text you" more than system entries
- Weekly reviews consistently taking >30 min
- Ad-hoc system work >1 hour/week
- Defensive reactions when discussing overdue tasks
- Passive-aggressive task creation
- 3+ projects stuck in Planning for >30 days
- Starting more projects than finishing
- OKR progress <50% of expected pace

---

## System Integrity

System Integrity monitors the **technical health of the Notion workspace itself** — distinct from the productivity vital signs above. While the six vital signs track whether *people* are using the system well, System Integrity tracks whether *the system itself* is structurally sound.

### Why It Lives Here

System Integrity is an **action** — monitoring, detecting, diagnosing, recommending fixes. The Command Center (DD-19) merely *displays* a System Health indicator in its Mission Control vital signs strip. The Compass owns the monitoring logic because monitoring is a REFINE activity: observe the system's state, identify drift, and course-correct.

### Check Categories

| Category | What It Checks | Severity |
|----------|---------------|----------|
| **Broken Relations** | Database relations pointing to deleted or moved pages | High |
| **Orphaned Pages** | Pages with no parent or no inbound links from the Architecture | Medium |
| **Missing Properties** | Database entries missing required fields (Owner, Status, Priority) | High |
| **Automation Failures** | Notion automations or integrations that have stopped working | High |
| **Schema Drift** | Database properties that have diverged from their Design Decision spec | Medium |
| **Stale Content** | Architecture pages not updated in >90 days despite active development | Low |

### System Diagnostics Page

A dedicated page showing current System Integrity status:

- Pass / Warn / Fail indicators for each check category
- Detailed findings with links to affected pages
- Recommended fixes (actionable next steps)
- Last audit timestamp
- Linked from Mission Control's System Health indicator in the Command Center

### Audit Cadence

System Integrity checks run as part of the **Monthly Audit** (Cadence 3 above). During Step 2 (Warning signal scan), the auditor also runs a System Integrity sweep. Critical issues (broken relations, automation failures) may also be flagged ad-hoc by agents during normal operations.

### WS2 Scope

For WS2: manual System Integrity checks during Monthly Audit only. No automated monitoring. The System Diagnostics page is created but populated manually.

**Deferred to WS3-WS4:** Automated integrity scanning, agent-triggered alerts, historical trend tracking.

---

## Framework Integration

The Compass draws from multiple frameworks:

- **GTD-Lite Weekly Reflect** provides the inbox processing and project review mechanics (Phases 1-2 of Family Meeting)
- **OKR Quarterly + Annual Reviews** provide the strategic assessment cadence (Phases 3 and Cadences 4-5)
- **PARA Archive Management** provides the cleanup discipline (archiving stale projects, pruning resources)
- **Zettelkasten Evergreen Refinement** provides the knowledge hygiene layer (updating notes, expanding MOCs, pruning outdated ideas)
- **OODA loop-back** provides the continuous feedback mechanism (every Refine cycle feeds back to Input)

---

## Notion Implementation

The Compass needs these views and structures in Notion:

**System Health Dashboard** (future Command Center component):

- Vital Signs overview: 6 metrics with current values and zone colors
- Time investment: weekly actual vs. 120 min target
- Warning signals: count of active behavioral warnings

**Views required:**

- Tasks → Overdue view (filtered by Assignee per DD-12 two-layer model)
- Projects → Stalled view (Status = Planning, no tasks, >30 days old)
- Projects → Zombie view (Status = Paused, last edited >30 days ago)
- Projects → Without Next Actions view
- Goals → OKR Progress view (Key Results with % completion)
- System Log → Weekly digest view (last 7 days of system changes)

**Templates needed:**

- Family Meeting notes template (with the 5-phase agenda pre-filled)
- Monthly Audit template (with checklist and trend fields)
- Quarterly Deep Review template (with 7-step protocol)
- Annual Reset template (with 5-step protocol)

---

## WS2 Scope (Narrow Launch)

For WS2, the Compass handles:

- Daily Pulse (personal, each partner independently)
- Weekly Family Meeting (full 5-phase protocol)
- Monthly Health Scan (vital signs only)

**Not in WS2 scope** (deferred to WS3-WS4):

- Automated vital signs dashboard (manual checks initially)
- Time investment tracking (honor system initially)
- Quarterly/Annual review templates (use ad-hoc format initially)
- Emergency protocols (document exists, but no automated triggers)

---

## Evolution Roadmap

| Workstream | Compass Capability |
|-----------|-------------------|
| **WS2** | Daily Pulse, Weekly Family Meeting (full protocol), Monthly vital signs check (manual). Emergency protocols documented but not automated. |
| **WS3** | System Health Dashboard with live vital signs. Family Meeting notes template. |
| **WS4** | Automated warning signals: agent flags behavioral warnings during weekly review. Time investment tracking via Work Sessions data. Quarterly Review template. |
| **WS5** | Predictive health: agent identifies emerging risks before they trigger protocols. Annual Reset facilitation. Full dashboard with historical trends. |

---

## Interaction with Other Design Decisions

- **DD-06 (Output Elements / Execution Beast):** The Compass reviews the Execution Beast's output — project velocity, task completion, goal progress. PEA Align feeds into the Compass.
- **DD-08 (Family Meeting):** The Family Meeting is the Compass's primary weekly ritual. DD-08 established it; DD-18 formalizes its 5-phase structure.
- **DD-09 (Hybrid OKRs):** OKR progress is one of the six vital signs. Quarterly Reviews score Key Results.
- **DD-10 (Capturing Beast):** REFINE feedback loops back to INPUT — insights from reviews generate new captures.
- **DD-11 (System Log):** The Compass reads from the System Log to detect patterns and anomalies.
- **DD-12 (Workspace Architecture):** The System Health Dashboard lives in the Household Teamspace Command Center.
- **DD-15 (Front Desk):** The Compass audits Front Desk effectiveness — triage accuracy, routing quality, unprocessed items.
