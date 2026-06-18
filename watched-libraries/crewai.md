---
name: "CrewAI"
type: "watched-library"
repo_url: "https://github.com/crewaiinc/crewai"
description: "Multi-AI agent orchestration framework built on role-playing and collaborative intelligence. Agents have defined roles, goals, and backstories; they work in crews with sequential or hierarchical process execution, tool delegation, and memory."
spectrum_position: "cherry-pick"
what_we_use: "Role-based agent composition, crew orchestration topology, task delegation patterns, agent memory and learning primitives, tool delegation model"
local_derivations: []
last_evaluated_version: "v1.14.6"
last_evaluated_date: "2026-05-25"
maintainer: "crewaiinc"
status: "active"
tags:
  - "multi-agent"
  - "orchestration"
  - "role-playing"
  - "delegation"
  - "python"
  - "memory"
related_findings: []
related_sources: []
date_added: "2026-05-25"
---

## What It Does

Framework for orchestrating role-playing autonomous AI agents. Each agent has a defined role, goal, and backstory that shape its behavior. Agents are organized into "crews" that execute tasks via sequential or hierarchical processes. Features include tool delegation between agents, built-in memory (short-term, long-term, entity memory), and task decomposition with inter-task dependencies.

## What We Use From It

Cherry-pick patterns:
1. **Role-based agent composition** — How role/goal/backstory triplet defines agent behavior boundaries
2. **Crew orchestration topology** — Sequential vs hierarchical process execution, manager agent pattern
3. **Task delegation patterns** — How work flows between agents, delegation rules, and fallback behavior
4. **Agent memory primitives** — Short-term, long-term, and entity memory integration at the framework level
5. **Tool delegation model** — How tools are assigned to agents and delegated during execution

## Spectrum Rationale

**Cherry-pick** — CrewAI's role-based agent composition model directly parallels MetaSystem's agent persona pattern (constitution, boundaries, vibe). The crew orchestration topology (sequential/hierarchical processes) and delegation patterns offer concrete implementation references for multi-agent coordination. The memory primitives (short/long-term/entity) are relevant to IL's memory architecture research.

## Change Signals

Watch for:
- Memory architecture evolution (new memory types, persistence patterns)
- Delegation and orchestration pattern changes
- New process types beyond sequential/hierarchical
- Agent communication and handoff mechanisms
- Evaluation and quality patterns for crew outputs
- Context management within and across crews
