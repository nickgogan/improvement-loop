---
title: "Constitution"
id: "constitution"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-03-22"
updated: "2026-04-05"
author: "nick"
source_dd:
  - "DD-32"
  - "DD-45"
tags:
  - "constitution"
  - "boundary-rules"
  - "ownership"
  - "design-philosophy"
aliases:
  - "The Constitution"
  - "System Governance"
_provenance:
  notion_id: "32b1e08b-9b34-811c-a283-d87a9089bd5c"
  parent: "System Governance"
  extracted: "2026-04-04"
---

> **For agents:** This is the governing document for the entire Household Operating System. Read this before any architectural work, system modification, or design decision. It defines what systems exist, how they relate, and what principles guide all design choices. For system-specific architecture, navigate to the appropriate system section under Architecture.

---

## The Three Systems

The Household Operating System is governed by three distinct systems with clear ownership boundaries. The original four-system model (S1–S4, established March 16, 2026) was consolidated into three systems on April 5, 2026 (DD-57, DD-58). The S-number naming scheme is retired; systems use descriptive names.

### System Definitions

| System | Nature | Primary Owner | Runtime |
|---|---|---|---|
| **Household OS** | The product — frameworks, operations, knowledge base | Nick + JR + Agents | Notion + Slack |
| **Claude Build** | Build system — produces schema and infrastructure | Nick via Cursor/Claude Code | Local dev env |
| **Improvement Loop** | Self-improvement — research, proposals, codification | Nick + Agents | Local dev env |

### Boundary Rules

1. **Household OS reads and writes data within its own schema.** Household OS never modifies schema structure (no creating databases, no adding properties, no changing views).
2. **Schema changes only through Claude Build** via Build Specs with Review Gates. Every structural modification goes through the Claude Build system.
3. **Nick is the bridge between Household OS and Claude Build.** No automated feedback loop exists. Nick observes Household OS operations, translates observations into IB items, and feeds those to Claude Build.
4. **JR's primary interface is Household OS** (Notion UI + Slack). JR has git access to the shared Tier 2 repo for browsing vault content, but does not operate Claude Build.

### Ownership Matrix

| System | Created by | Operated by | Maintained by | Evolved by |
|---|---|---|---|---|
| **Household OS** | Claude Build (schema + configs) | Custom Agents + Nick + JR | Nick (monitors, tunes) + Claude Build (schema changes) | Claude Build (via IB items from Nick) |
| **Claude Build** | Nick (vault setup) | Nick via Cursor | Nick + Improvement Loop | Improvement Loop + Nick |
| **Improvement Loop** | Nick | Nick + Agents | Nick | Self-improving via research cycle |

> **Note on S-numbers:** The original four systems were S1-Schema, S2-Operations, S3-Build, S4-Bootstrap. S1 and S2 merged into Household OS (DD-58). S4 was folded into S3. The S-number scheme itself is retired (DD-57). Historical references to S-numbers in existing DDs are preserved as-is.

### Feedback Loop

Household OS -> Nick (observes) -> IB items -> Claude Build

---

## Design Philosophy

These principles govern all design decisions across every system. When in doubt, defer to these.

- **Spec before build.** Always create a specification document outlining the structural-functional organization of a proposed solution. Only after explicit acceptance is it okay to proceed to implementation.
- **Complementary tools, not redundant ones.** Thoughtfully pair tools that complement each other to create a digital ecosystem that amplifies life and work styles -- achieve more with less fuss.
- **Knowledge serves expression.** Knowledge formation should be in the service of some form of expression: projects, decisions, writing, getting a promotion, etc. Notes that don't lead somewhere are dead weight.
- **Shallow vs. deep thinking.** Distinguish shallow thinking (most things in Notion) from deep thinking (done in a dedicated system like Heptabase). Don't try to do deep synthesis in a tool built for task management.
- **Start lean, refine later.** Launch with the minimum viable version of each component. Complexity is earned through use, not anticipated in design.
- **Consumer feedback to producer.** When one agent consumes another agent's output, the consumer provides feedback to the producer — concrete gaps ("I needed X but didn't get it") and natural language critique. Both humans and downstream agents are consumers; both feedback channels improve the producer. Structured scoring rubrics may emerge from accumulated feedback over time, but are not imposed upfront.

### Design Dimensions

These dimensions help classify where any given piece of work or information belongs:

- Inner World vs. Outer World
- Shallow Work vs. Deep Work
- System of Record vs. System of Engagement
- Personal vs. Household
- Recurring/Maintenance vs. Deliverable

---

## Provenance

This page was created on March 22, 2026 by merging the Four-System Separation Model page and the Design Philosophy section from the Architecture hub. The original Four-System Separation Model page was created from the reconciliation of the v6 Migration Intelligence Report, the Four-System Architecture document, and a live Notion workspace audit conducted on March 16, 2026.

### Companion Document

The full analysis (20 pages) lives as **four-system-architecture.pdf** in Google Drive. That document contains the detailed boundary pair analysis, interface contracts, Handoff Prompt section mapping, and decision matrix.
