---
notion_id: 30f1e08b-9b34-8169-9553-edd69e606bfe
title: "Workspace Architecture"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# Workspace Architecture

> **For agents:** This page defines the physical Notion workspace structure. All operational databases (tasks, projects, OKRs, System Log) live in the Household Teamspace and are the single source of truth. Never create parallel databases in private Teamspaces. Use the Owner property and filtered views to scope items to individuals — not workspace separation.

## The Core Decision (DD-12)

The Household Operating System runs in **one shared Notion workspace** with **three Teamspaces**:

| Teamspace | Visibility | What Lives Here | Who Can See |
|-----------|-----------|----------------|-------------|
| **Household** | Shared | System Documentation, Architecture, Area pages, all operational databases (tasks, projects, OKRs, System Log), Family Meeting dashboard | Both partners + agents |
| **Nick** | Private | Personal journal, career drafts, private notes, any "eyes only" pages | Nick only |
| **John** | Private | Personal journal, career drafts, private notes, any "eyes only" pages | John only |

---

## Why One Workspace

The entire architecture depends on items living in a **single relational graph**. Splitting into separate workspaces would break:

- **Cross-domain linking** — a personal OKR can't link to a Household Goal across workspaces
- **Unified search** — agents and humans need to find items regardless of Owner
- **The Owner property model** (DD-09) — filtering by Owner = Nick only works if Nick's items and Household items live in the same database
- **The System Log** (DD-11) — re-tagging an item from Personal to Household must happen within one database, not across workspace boundaries
- **Agent traversal** — an agent processing a Capturing Beast intake needs access to the full graph to route, tag, and link correctly

---

## What Goes Where

### Household Teamspace (shared)

This is where **all system infrastructure** lives:

| Content Type | Examples | Why Shared |
|-------------|---------|-----------|
| **System Documentation** | Architecture, ICOR, Vocabulary, Design Decisions | Both partners and agents must be able to read and reference system rules |
| **Operational Databases** | Tasks, Projects, OKRs, System Log, Inbox | Relational integrity — items must link to each other. Owner property handles personal scoping. |
| **Area Pages** | Finances, Health & Wellness, Household, Career | Areas are shared system infrastructure even when one partner is Lead (DD-09, Stewardship model) |
| **Shared Knowledge** | Wardrobe hub, recipe database, vendor contacts | Household knowledge that both partners use and contribute to |
| **Dashboards** | Family Meeting view, System Health, Area Health | Coordination and visibility across the household |

> **Key rule:** A task with Owner = Nick still lives in the shared Tasks database. It's Nick's task, but it exists in shared infrastructure so it can be linked, filtered, queried, and tracked by agents. The Owner property scopes it; the Teamspace does not.

### Private Teamspaces (Nick / John)

Private Teamspaces are for content that **doesn't need to be in the relational graph** and is genuinely personal:

| Content Type | Examples | Why Private |
|-------------|---------|-----------|
| **Personal journals** | Daily reflections, gratitude logs, freewriting | Intimate content that doesn't need to be actionable or linked |
| **Career drafts** | Resume iterations, interview prep, salary research | Sensitive professional material |
| **Personal reference** | Gift ideas for partner, surprise planning | Content that would be spoiled by shared visibility |
| **Scratch space** | Temporary notes, thinking-in-progress | Not yet ready for the system; may never be |

> **Key rule:** If a private page generates an actionable item (a task, a project, an OKR), that item goes into the shared database with the appropriate Owner tag. The private page can *link to* the database item, but the item itself lives in shared infrastructure.

---

## The Boundary Test

When deciding where something goes, apply this decision tree:

1. **Does it need to link to other system items?** (tasks, projects, OKRs, areas) → **Household Teamspace** (shared database, use Owner property)
2. **Could an agent need to see it?** → **Household Teamspace**
3. **Would your partner ever need to find it?** → **Household Teamspace**
4. **Is it genuinely private — journal, draft, surprise, scratch?** → **Private Teamspace**
5. **Not sure?** → **Default to Household Teamspace.** It's easier to ignore a shared item via filtered views than to move a private item into the graph later.

---

## How Filtered Views Create the Personal Experience

Even though everything operational lives in one shared workspace, each person's daily experience feels personal through **filtered views**:

| View | Filter Logic | What It Shows |
|------|-------------|---------------|
| **My Day** | Owner = Me OR Assignee = Me, Due = Today | Today's personal tasks + any Household items assigned to me |
| **My Projects** | Owner = Me | All my active projects |
| **My OKRs** | Owner = Me | Personal objectives and key results |
| **My Inbox** | Owner = Me OR Untagged | Personal captures awaiting processing |
| **Family Dashboard** | Owner = Household | Shared goals, joint projects, household operations |
| **Area Health** | Area = [selected], all Owners | Full picture of an Area regardless of who owns what |

The combination of **shared databases + Owner property + filtered views** gives each person their own focused workspace without sacrificing the relational power of the unified graph.

---

## The Two Visibility Mechanisms

The system uses **two different mechanisms** to control who sees what, and understanding which one applies is the key to the whole architecture:

| Mechanism | Controls Visibility Of | How It Works |
|-----------|----------------------|-------------|
| **Teamspaces** | Unstructured content (pages, journals, drafts, freewriting) | Content in Nick's Teamspace is invisible to John and vice versa. Simple folder-level privacy. |
| **Database Properties + Filtered Views** | Structured content (tasks, projects, goals, notes, logs) | Everything lives in shared databases. The Owner property marks who it belongs to. Filtered Views (My Day, My Projects, My OKRs) show only your items. |

> **The mental model:** Teamspaces are like separate rooms in the house — your private office has a door. Database properties are like file labels in a shared filing cabinet — everything's in the same cabinet, but your name is on your folders, and you have a view that only shows you yours.

This means **Private Teamspaces end up being quite thin.** Most of what you do day-to-day — tasks, projects, goals, notes, captured ideas — is structured content that benefits from being in the relational graph. The private Teamspaces hold only genuinely personal, non-operational content: journals, drafts, surprises, scratch space.

---

## Common Questions

### "Should my personal projects and tasks go in the shared Teamspace?"

**Yes.** All projects and tasks — even personal ones like "Update resume" or "Research running shoes" — go into the shared UB3 databases in the Household Teamspace. The Owner property marks them as yours. A Filtered View like "My Projects" only shows items where Owner = You, so the experience feels personal even though the data is shared.

Why this matters: if personal tasks lived in your private Teamspace, an agent couldn't see the full picture when asked "what's on Nick's plate this week?" — it would need to look in two places. And a household project with tasks assigned to both of you would be impossible to manage if tasks were split across Teamspaces.

### "Should we duplicate Ultimate Brain into separate instances?"

**No.** UB3's power comes from its cross-database relations — tasks link to projects, projects link to goals, goals link to areas. If you had three separate UB3 instances:

- A household project couldn't link to both Nick's tasks AND John's tasks
- You'd constantly ask "which UB3 does this belong in?"
- Template updates, formula fixes, and property additions would need to happen three times
- Agents would lose the single source of truth

One UB3, shared databases, Owner property for scoping. That's the design.

### "Will Notion get slow with all this content in one place?"

Notion performance issues are real but typically caused by very large databases (10,000+ items), deeply chained formula/rollup chains, and heavy synced block usage — not by having multiple users or Teamspaces. A two-person household won't hit these limits for years. The real performance strategy is good hygiene: archive completed projects, keep formulas simple, don't over-chain rollups. The Architecture already supports this through the Archive page and regular system health reviews.

### "What if I have something private that generates a task?"

The private page stays in your Private Teamspace. The task it generates goes into the shared Tasks database with Owner = You. The private page can link to the task, but the task itself lives in shared infrastructure so it participates in the relational graph. Example: your private "Gift ideas for John" page might generate a task "Order anniversary present" — that task goes in the shared database (John doesn't browse your task list anyway, and you can mark it with a discreet name).

### "Can John see my tasks if he wants to?"

Technically yes — both partners have access to the shared databases. But the default views (My Day, My Projects, My OKRs) only show your own items. Seeing the other person's items requires deliberately switching to an unfiltered or "All" view. This is by design — the stewardship model (DD-09) means either partner should be able to step in fully if needed. The system favors transparency over isolation.

---

## Agent Behavior Rules

| Rule | Rationale |
|------|-----------|
| Agents operate exclusively in the **Household Teamspace** | All operational data lives here; agents don't need access to private journals |
| Agents must respect the **Owner property** when creating or modifying items | An agent processing Nick's Capturing Beast intake tags items Owner = Nick, not Household |
| Agents must **never create databases** in private Teamspaces | Prevents data fragmentation and broken relations |
| Agents can **read Area pages** regardless of Lead/Backup assignment | Stewardship over specialization — agents serve the household, not one person |
| When an agent encounters ambiguous ownership, it should **flag for human review** rather than guess | Incorrect Owner assignment is harder to fix than a brief delay |

---

## Interaction with Other Design Decisions

- **DD-09** (Personal/Household Model): The Owner property is the primary mechanism for personal scoping within the shared workspace. Teamspaces add a secondary privacy layer for non-operational content.
- **DD-10** (Capturing Beast Routing): Capture-time routing determines the Owner tag, which flows through the shared databases. The Teamspace is irrelevant to routing logic.
- **DD-11** (System Log): All System Log entries live in the Household Teamspace. Domain migration (re-tagging) is logged regardless of whether private pages reference the item.
- **DD-06** (Output Elements): All Output Elements (Goals, Projects, Workstreams, Operations, Tasks, Speedies) live in shared databases. No Output Element should ever be created in a private Teamspace.

---

*This page is authoritative. When questions arise about where content should live, apply the Boundary Test above. When in doubt, default to the Household Teamspace.*
