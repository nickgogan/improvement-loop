---
notion_id: 30f1e08b-9b34-81db-84fd-fd5ee0b02206
title: "Personal / Household Model"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Personal / Household Model

> **For agents:** This page defines how the system distinguishes between personal and household context. Every item in the system has an Owner (Nick, JR, or Household) and an Area. These two properties together determine visibility, routing, and ritual scope. When creating or modifying items, always set both. When an item is re-tagged from personal to household (or vice versa), log the change in the System Log.

## The Core Problem

This system serves two individuals and one household simultaneously. Nick and JR each have personal goals, knowledge, and rhythms. They also share a household with joint responsibilities, finances, and a common vision. The system must serve both modes without feeling like two separate systems duct-taped together, or one monolith where personal items are lost in shared noise.

---

## The Four Domains

The system operates across four domains defined by two axes:

| | **Knowledge** | **Action** |
|---|---|---|
| **Personal** | PKM — individual learning, notes, references | PPM — individual tasks, goals, execution |
| **Household** | HKM — shared knowledge, procedures, documentation | HPM — shared projects, goals, coordination |

Every item in the system belongs to exactly one domain at any given time. Domain is determined by the combination of **Owner** and **item type** (knowledge vs. action).

---

## The Owner Property

The Owner field is the primary mechanism for personal/household separation. It appears on every core database (Tasks, Projects, Notes, OKRs) and takes one of three values:

| Value | Meaning | Example |
|-------|---------|---------|
| **Nick** | Owned and primarily managed by Nick | "Research language learning apps" |
| **JR** | Owned and primarily managed by JR | "Review investment portfolio" |
| **Household** | Shared responsibility, governed by Area stewardship (Lead + Backup) | "File joint tax return" |

### Rules

- Every item must have an Owner. No orphans.
- Household items additionally have a **Lead** (the person who owns the cadence) and a **Backup** (who can step in), inherited from the Area's stewardship assignment.
- The Owner field is what powers personal filtered views ("My Day", "My Projects", "My OKRs").
- Household items appear in both partners' views when they are the Lead or Backup for that Area.

---

## The Area as Boundary

> **Superseded:** The Area table below is a simplified original reference. The authoritative Area taxonomy is now defined in **DD-23 (Area Taxonomy & Tags Enhancement)**, which specifies 19 Area entries across four orientation types (Pure Personal, Pure Household, Hybrid, Shared Parent) with full Lead/Backup stewardship assignments. See [DD-23 spec page](https://www.notion.so/3101e08b9b3481639c5ad82cbaf72dd1) for the current definitions.

Areas carry an inherent personal/household orientation:

| Area | Orientation | Lead | Backup |
|------|------------|------|--------|
| Career | Personal (one per person) | Self | Partner |
| Character Development | Personal (one per person) | Self | Partner |
| Health & Wellness | Household | TBD | TBD |
| Finances | Household | TBD | TBD |
| Household | Household | TBD | TBD |
| Legal | Household | TBD | TBD |

Hybrid Areas contain both personal and household items. The Owner field on each item disambiguates.

---

## OKR Structure (DD-09, DD-25)

The goal hierarchy follows a simplified hybrid model (DD-25 amendment 2026-03-01):

```
Shared Household Vision (2026-2030)
+-- Household Yearly Goals (Owner = Household)
|   +-- Projects (Owner = Household)
|   +-- Standalone Tasks (Owner = Household)
|   +-- Optional Milestones (grouping Projects/Tasks into phases)
+-- Nick's Yearly Goals (parallel track)
|   +-- Nick's Projects & standalone Tasks (Owner = Nick)
|   +-- Optional Milestones
+-- JR's Yearly Goals (parallel track)
    +-- JR's Projects & standalone Tasks (Owner = JR)
    +-- Optional Milestones
```

- Household Goals cascade from the shared Vision.
- Personal Goals are a parallel track, not subordinate to household Goals.
- When a personal Goal serves a household Goal, an explicit **link relation** connects them (e.g., Nick's "Pass Romanian language exam" links to Household's "Secure Romanian citizenship").
- Neither track is subordinate to the other.
- **Progress tracking:** Goal progress = completed work items (Projects at Done + standalone Tasks completed) / total work items. Fully automated.
- **Milestones** are optional organizational containers (Milestones DB). When present, they group Projects/Tasks into phases. A Milestone auto-completes when all its linked items are done. Milestones do not change the progress formula.
- **Dormant:** The Quarterly Key Result layer (Goal Type = "Key Result") is retained in the Goals DB schema but not actively used. It can be activated later if quarterly planning is needed.

---

## Capturing Beast: Personal/Household Routing (DD-10)

The intake experience (Slackbot or similar) distinguishes personal from household at capture time:

```
Input arrives
  -> 3-Lens Filter (Current Projects? Key Areas? Active Topics?)
  -> Pass? -> Personal or Household?
      -> Personal -> route to personal inbox (Owner = self)
      -> Household -> route to household inbox (Owner = Household)
  -> Fail all 3 lenses? -> Discard
```

This routing happens at the moment of capture, not deferred to the Control stage. The Slackbot can ask two fast questions: "What's this about?" (maps to Area) and "Personal or household?" (maps to Owner).

---

## Re-tagging and Domain Migration

Items sometimes change domain — what starts as personal research becomes a household project, or a household task gets delegated to one person.

### Rules for re-tagging

- **Re-tag the Owner field** on the original item. Do not create a duplicate.
- **Log the change** in the System Log with: item, old Owner, new Owner, who made the change, when, and why.
- **Update Area** if the re-tag also changes the relevant Area (e.g., personal health research → household grocery planning).
- **Preserve provenance** — the System Log entry serves as the audit trail. The item itself reflects only its current state.

### Common re-tag scenarios

| Scenario | From | To | Example |
|----------|------|----|---------|
| Personal research becomes shared | PKM → HKM | Nick → Household | Supplement research → household shopping list |
| Shared task delegated | HPM → PPM | Household → Nick | "Call insurance company" assigned to Nick |
| Personal goal serves household | PPM stays PPM | Link added (no re-tag) | Nick's language exam links to household citizenship OKR |

Note: delegation (assigning a household task to a person) is not a re-tag — the item stays Owner = Household but gets an **Assignee** = Nick. Re-tagging changes the fundamental ownership. Delegation changes who's doing the work.

---

## Views That Matter

**Naming convention (IB-10, 2026-03-01):** All personal view tabs use the pattern "[Name]'s [Type]" — e.g., "Nick's Tasks", "JR's Notes" — rather than "My X". This avoids ambiguity on shared pages where both partners see the same tab bar. Page names (My Day, My Week, etc.) remain unchanged — they describe the timescale concept, not a person's lens.

### Personal views (per person)

- **[Name]'s Tasks** (on My Day) — Personal tasks + tasks assigned to me. Filtered by (Assignee contains Me) OR (Owner = [self] AND Assignee is empty). See DD-12 Personal Execution pattern.
- **[Name]'s Notes** (on My Day) — Personal notes + household notes. Filtered by Owner = [self] OR Owner = Household.
- **[Name]'s Projects** (on Projects page) — Personal projects + household projects. Filtered by Owner = [self] OR Owner = Household.
- **[Name]'s OKRs** (on Goals page) — Personal OKR track + household objectives. Filtered by Owner = [self] OR Owner = Household.
- **Weekly Review** — Personal REFINE ritual scope.

### Household views (shared)

- **Family Meeting Dashboard** — All Household-owned projects, OKRs, and flagged cross-boundary items.
- **Area Health** — All Areas with Lead/Backup assignments, status, last review date.
- **System Log** — Recent changes across the whole system.

### Agent context

Agents have access to all domains but must be context-aware. When operating on behalf of a person, agents filter to that person's scope. When operating on household items, agents respect the Lead/Backup model and log all actions.

---

## Key Distinctions

| Concept | Meaning | Not to be confused with |
|---------|---------|------------------------|
| **Owner** | Who the item fundamentally belongs to (Nick, JR, Household) | Assignee |
| **Assignee** | Who is currently doing the work on a Household item | Owner |
| **Lead** | The steward of an Area's cadence and proactive management | The only person who can do work in that Area |
| **Re-tag** | Changing the Owner (domain migration) | Delegation |
| **Link** | Explicit relationship between personal and household OKRs | Merging or duplicating |

---

*Design Decisions: DD-09 (hybrid OKR structure), DD-10 (personal/household routing at capture), DD-11 (audit trail as system primitive), DD-23 (Area taxonomy & Tags enhancement)*

*See also: The Capturing Beast · Vocabulary · System Log*
