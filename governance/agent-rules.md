---
title: "Agent Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-04-19"
author: "agent"
source_governance:
  - "systems/meta-system/governance/constitution.md"
  - "systems/meta-system/governance/fractal-pattern.md"
  - "systems/meta-system/governance/vocabulary.md"
source_sections:
  - "Design Philosophy (consumer feedback to producer)"
  - "The Agentic Layer"
  - "Agent & Skills vocabulary"
tags:
  - "governance"
  - "improvement-loop"
  - "agents"
  - "skills"
---

# Agent Rules — IL Governance

> Derived from: Constitution, Fractal Pattern (`systems/meta-system/governance/fractal-pattern.md`), Vocabulary (`systems/meta-system/governance/vocabulary.md`)
> Last reconciled: 2026-04-19

## Rules

1. **Agent-as-directory.** Each agent is a directory under `agents/` containing at minimum an `agent.md` definition file. The directory can grow to include `skills/`, `workflows/`, `templates/`, and `hooks/` as needs emerge. This follows the fractal pattern's agentic layer.
   - *Source:* Fractal Pattern — The Agentic Layer

2. **Every agent has a constitution.** The `agent.md` file defines: Core Truths, Boundaries, Vibe, Continuity, Disposition, Scope, Autonomy Table, Skill Inventory, Communication, and Contract. These sections are mandatory — an agent without a constitution is not a deployed agent.
   - *Source:* Fractal Pattern — The Agentic Layer; DD-86 (Owner pattern)

3. **Skills define agent behavior.** An agent's capabilities are expressed through skills (SKILL.md files in `.claude/skills/`). Each skill has a cognitive disposition, procedure, rules, and allowed tools. When a skill is loaded, the agent's disposition shifts to match.
   - *Source:* Vocabulary — Cognitive Disposition, Access Model, Scope Boundary

4. **Read/write boundaries are per-agent.** Each agent has defined read and write scopes in its Communication section. The Researcher writes findings, sources, and authorities. The Codifier writes to extracts. The Librarian is read-only. The Owner writes governance, docs, SL entries, and audit reports. Agents do not write outside their scope.
   - *Source:* Constitution — Boundary Rules; DD-30, DD-80

5. **Consumer feedback to producer.** When one agent consumes another's output and finds gaps, the consumer provides feedback — concrete gaps and natural language critique. Feedback goes to `feedback/` for the Owner to triage. This applies to both agent-to-agent and human-to-agent feedback.
   - *Source:* Constitution — Design Philosophy ("Consumer feedback to producer")

6. **Agents are peers, not hierarchical.** The Owner maintains agent constitutions (proposal-first) and system health, but does not supervise other agents at runtime. Each agent operates within its own scope and autonomy. No agent can modify another agent's constitution unilaterally.
   - *Source:* Owner Constitution — Boundaries ("NEVER promote your own autonomy tiers"); Out of Scope ("Runtime supervision")

7. **Engine definitions are subsets.** The `.claude/agents/` directory holds engine-facing subagent definitions (consumed by Claude Code). These are subsets of the full `agents/{name}/agent.md` definitions. Both coexist — the fractal `agents/` directory is canonical.
   - *Source:* Fractal Pattern — Relationship to Engine Directories

## Applicability Notes

These rules apply to all four IL agents. The Owner is responsible for maintaining agent constitutions and ensuring these rules are followed. Changes to agent constitutions are Proposal-First tier — the Owner drafts, Nick approves.
