---
notion_id: 30f1e08b-9b34-81b3-a057-d55359f2dc09
title: "The Capturing Beast"
parent: "S2: Notion Operations Architecture"
extracted: "2026-04-04"
---

# The Capturing Beast

> **For agents:** The Capturing Beast is the Input stage gatekeeper. When processing incoming information (emails, captures, web clips), apply the three-lens filter below to determine if the item should enter the system. If none of the three lenses match, the item should be discarded or consciously deferred.

## What Is It?

The Capturing Beast is ICOR's mental model for filtering what enters the system. It sits at the boundary between the world and the Inbox. Its job is to **say no to most things** — preventing the system from becoming a museum of unprocessed information.

Every piece of incoming information must pass through three lenses. If it passes any one lens, it enters. If none, it's discarded.

---

## The Three Lenses

### Lens 1: Current Projects

**Does this relate to something we are actively working on?**

If yes: the item enters immediately, **fast-tracked toward Output**. It routes directly to the relevant Project and may create a Task. This prevents project-relevant information from getting buried in the Inbox.

*Example: An email from the Romanian consulate arrives. The "Romania Citizenship Application" project is active. This email fast-tracks to that project.*

### Lens 2: Key Elements (Areas)

**Does this relate to one of our six Areas of ongoing responsibility?**

The six Areas: Health, Finances, Legal, Career, Household, Character.

If yes: the item enters for **Control-stage processing**. It may become a task, a reference note, or a trigger for a new project. It needs to be clarified (GTD) and organized (CODE) before it goes anywhere.

*Example: A newsletter about tax law changes. It relates to Finances. It enters the Inbox for processing at the next Family Meeting.*

### Lens 3: Active Topics (Resources)

**Is this relevant to a topic we are deliberately exploring right now?**

Active Topics are PARA Resources currently marked as Favorite/Active in Notion. These are things you're researching or learning about — not obligations, but chosen interests.

If yes: the item enters for **knowledge development** in the Control stage. It will likely become a Reference Note or feed into a Heptabase permanent note.

*Example: An article about Stoic philosophy. If "Stoic Philosophy" is an active Resource tag, it enters. If not, it doesn't — even if it's interesting.*

### None of the Above: Discard

**This is not failure — this is the system working correctly.** Not everything deserves to take up space in the system. Discarding confidently is a skill.

---

## Personal / Household Routing (DD-10)

After an item passes the 3-lens filter, one more routing decision happens at capture time:

**Is this personal or household?**

This decision is made *at the point of capture*, not deferred to the Control stage. A dedicated intake experience (Slackbot or similar) asks two fast questions:

1. "What's this about?" → maps to an Area
2. "Personal or household?" → sets the Owner property

Routing:

- **Personal** → route to personal inbox (Owner = self)
- **Household** → route to household inbox (Owner = Household)

The Slackbot logs every routing decision in the System Log as an Agent Action, providing an audit trail of what entered the system and how it was classified.

If unsure, default to **personal**. It's easier to promote something to household during Control than to demote something that was prematurely shared.

---

## Design Implications

- The **Active Topics list** needs to be a maintained, visible view in Notion: Tags where Type = Resource AND Favorite = true (or a custom "Active" property)
- The Capturing Beast only works if you **know** what your current projects, areas, and active topics are
- This filter applies equally to humans manually capturing and to AI agents processing inbox items
- An agent processing inbox items should check these three lenses in order before accepting an item into the system

---

*Design Decisions: DD-01 (ICOR is the meta-framework), DD-10 (personal/household routing at capture), DD-11 (audit trail)*

*See also: Personal / Household Model · System Log · Vocabulary*

---

> **DD-12 Cross-Reference (2026-02-28):** The Capturing Beast sets **Owner** at capture time. This is correct — Owner defines accountability/stewardship and is the first property set. **Assignee** (execution layer) is NOT set at capture; it is set later during triage (DD-15), Family Meeting (DD-24 Phase 5), or daily planning. See DD-12's two-layer responsibility model for the full Owner/Assignee lifecycle.
