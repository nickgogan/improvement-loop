---
title: "Design / Build / Deploy / Operate Pipeline"
id: "dbdo-pipeline"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-03-22"
updated: "2026-06-21"
author: "nick"
source_dd:
  - "DD-103"
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
System operations → Nick (observes) → IB items → Build/evolve → System (consumes the change)
```

The cycle is closed within a single system: a system's operations surface needs, Nick observes them, those become IB items, the build/evolve step applies the change, and the system runs on the updated capability. The Improvement Loop accelerates this by researching frontier patterns and proposing changes proactively.

> **Federation note (DD-103, DD-106):** Earlier versions of this loop crossed system boundaries (Household OS → Claude Build → Household OS). That federation collapsed — the engine (`systems/improvement-loop/`) is the sole live system; Household OS moved to Notion as a *consumer* the engine helps design (DD-106), and Claude Build was retired. The loop above is now the engine's own design/build/deploy/operate cycle, and the same shape applies to any single system it bootstraps.

---

*Source: Distilled from the Intention & Trajectory page, originally extracted into the former s1-schema/ folder (now archived at `archive/household-os/archive/s1-extraction/` per DD-58). De-federated and re-anchored DD-45 → DD-103 in session 126.*
