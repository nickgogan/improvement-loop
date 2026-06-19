---
title: "Design / Build / Deploy / Operate Pipeline"
id: "principles"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-03-22"
updated: "2026-04-04"
author: "nick"
source_dd:
  - "DD-45"
tags:
  - "pipeline"
  - "build-process"
  - "feedback-loop"
aliases:
  - "Build Pipeline"
  - "DBDO Pipeline"
---

# Design / Build / Deploy / Operate Pipeline

Every system built through this pipeline follows the same progression.

---

## The Pipeline

### 1. Brainstorm (Design)
Humans and agents identify components, modules, or systems that need to exist. Exploratory and divergent — map the problem space. Outputs are rough ideas, not specs.

### 2. Document Architecture (Design)
Ideas that survive brainstorming become architectural documentation. Design Decisions codify key choices: what exists, why it exists, how it relates to other parts.

### 3. Map to Implementation Backlog (Build)
Design Decisions generate IB items. Each is scoped to a single, well-bounded piece of work with clear acceptance criteria. Atomic enough for one agent, composable enough that a set produces a working capability.

### 4. Spec and Approve (Build)
Human-in-the-loop workflow converts IB items into executable Build Specs. The spec defines human steps, agent steps, verification checks, and rollback procedures.

### 5. Execute (Deploy)
Agents execute atomic work items following the Build Spec, verify their own work, and complete the Documentation Cascade. Human reviews at the Milestone level — end-to-end workflows and integration results.

### 6. Learn and Improve (Operate)
Every cycle produces learnings. System Log captures events. Playbook captures patterns. Improvement Loop researches frontier practices and proposes pipeline changes. Each cycle makes the next one faster.

---

## The Generalization Principle

This pipeline applies to any system where:
- Work can be described in structured documentation
- Work can be decomposed into agent-executable units
- A human can review integration results rather than individual steps
- Learnings can be captured structurally for future use

The system is **portable**. Given the right starting points (templates, reference architecture, skills, governance vocabulary), this pipeline can bootstrap a new domain without rebuilding infrastructure.

---

## The Feedback Loop

```
Household OS (operations) → Nick (observes) → IB items → Claude Build (builds schema) → Household OS (consumes updated schema)
```

The Improvement Loop accelerates this by researching frontier patterns and proposing changes proactively.

---

*Source: Distilled from the Intention & Trajectory page, originally extracted into the former s1-schema/ folder (now archived at `archive/household-os/archive/s1-extraction/` per DD-58).*
