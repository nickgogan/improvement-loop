---
title: "Values & Design Philosophy"
id: "values"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-03-22"
updated: "2026-04-04"
author: "nick"
source_dd:
  - "DD-32"
  - "DD-45"
tags:
  - "values"
  - "design-philosophy"
  - "boundary-rules"
  - "ownership"
aliases:
  - "Core Values"
  - "Design Philosophy"
---

# Values & Design Philosophy

These values govern all design decisions across every system in the Household OS. When in doubt, defer to these.

---

## Core Principles

- **Spec before build.** Always create a specification document outlining the structural-functional organization of a proposed solution. Only after explicit acceptance is it okay to proceed to implementation.
- **Complementary tools, not redundant ones.** Thoughtfully pair tools that complement each other to create a digital ecosystem that amplifies life and work styles — achieve more with less fuss.
- **Knowledge serves expression.** Knowledge formation should be in the service of some form of expression: projects, decisions, writing, getting a promotion, etc. Notes that don't lead somewhere are dead weight.
- **Shallow vs. deep thinking.** Distinguish shallow thinking (most things in Notion) from deep thinking (done in a dedicated system like Heptabase). Don't try to do deep synthesis in a tool built for task management.
- **Start lean, refine later.** Launch with the minimum viable version of each component. Complexity is earned through use, not anticipated in design.

---

## System Boundary Rules

1. **S2 reads and writes data within S1 schema.** S2 never modifies schema (no creating databases, no adding properties, no changing views).
2. **Schema changes only through S3** via Build Specs with Review Gates. Every structural modification goes through the Claude Code Build system.
3. **Nick is the bridge between S2 and S3.** No automated feedback loop exists. Nick observes S2 operations, translates observations into IB items, and feeds those to S3.
4. **JR's primary interface is S2** (Notion UI + Slack). JR has git access for browsing vault content, but does not operate S3.

---

## Ownership Matrix

| System | Created by | Operated by | Maintained by | Evolved by |
|--------|-----------|-------------|---------------|------------|
| **S1: Notion Schema** | S3 | S2 (agents + humans) | S3 | S3 (via IB items from Nick) |
| **S2: Notion Operations** | S3 | Custom Agents + Nick + JR | Nick | S3 (via Improvement Loop) |
| **S3: Claude Code Build** | Nick | Nick via Cursor | Nick + IL | Improvement Loop + Nick |
| **S4: Bootstrap** | Nick | Nick (once), JR (once) | Nick | Folded into S3 |

---

## Design Dimensions

These dimensions classify where any given piece of work or information belongs:

- Inner World vs. Outer World
- Shallow Work vs. Deep Work
- System of Record vs. System of Engagement
- Personal vs. Household
- Recurring/Maintenance vs. Deliverable

---

## What Makes This Work

1. **Atomic decomposition.** Work items are small enough that a single agent can complete one without needing full system context.
2. **Composability.** Atomic items combine into Milestones that produce working capabilities. Review at the Milestone boundary, not at the item level.
3. **Structural memory.** Everything learned is captured in databases and documentation, not in conversation history.
4. **Human-at-the-seams.** Humans make architectural decisions, review specs for high-risk work, and validate integration results.
5. **Self-improvement.** The Improvement Loop researches, proposes, and codifies improvements to the pipeline itself.

---

*Source: Distilled from Constitution and Intention & Trajectory pages in s1-schema/*
