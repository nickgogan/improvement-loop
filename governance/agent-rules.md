---
title: "Agent Rules — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-19"
updated: "2026-04-22"
author: "agent"
source_governance:
  - "systems/meta-system/governance/constitution.md"
  - "systems/meta-system/governance/fractal-pattern.md"
  - "systems/meta-system/governance/vocabulary.md"
source_sections:
  - "Design Philosophy (consumer feedback to producer)"
  - "The Agentic Layer"
  - "Agent & Skills vocabulary"
  - "DD-91 (reflections-to-proposals pipeline)"
tags:
  - "governance"
  - "improvement-loop"
  - "agents"
  - "skills"
  - "reflections"
---

# Agent Rules — IL Governance

> Derived from: Constitution, Fractal Pattern (`systems/meta-system/governance/fractal-pattern.md`), Vocabulary (`systems/meta-system/governance/vocabulary.md`), DD-89 (four-zone architecture), DD-91 (reflections-to-proposals)
> Last reconciled: 2026-04-22

## Rules

1. **Agent-as-directory.** Each agent is a directory under `agents/` containing at minimum an `agent.md` definition file. The directory can grow to include `skills/`, `workflows/`, `templates/`, and `hooks/` as needs emerge. This follows the fractal pattern's agentic layer.
   - *Source:* Fractal Pattern — The Agentic Layer

2. **Every agent has a constitution.** The `agent.md` file defines: Core Truths, Boundaries, Vibe, Continuity, Disposition, Scope, Autonomy Table, Skill Inventory, Communication, and Contract. These sections are mandatory — an agent without a constitution is not a deployed agent.
   - *Source:* Fractal Pattern — The Agentic Layer; DD-86 (Owner pattern)

3. **Skills define agent behavior.** An agent's capabilities are expressed through skills (SKILL.md files in `.claude/skills/`). Each skill has a cognitive disposition, procedure, rules, and allowed tools. When a skill is loaded, the agent's disposition shifts to match.
   - *Source:* Vocabulary — Cognitive Disposition, Access Model, Scope Boundary

4. **Read/write boundaries are per-agent.** Each agent has defined read and write scopes in its Communication section. The Researcher writes findings, sources, authorities, watched-libraries, watched-blogs, operations/, and its own reflections. The Codifier writes to extracts/, operations/, project-management/design-notes/, and its own reflections. The Librarian is read-only on the KB with a narrow write exception for its own reflections. The Owner writes governance/, docs, SL entries, audit reports, and its own reflections. Agents do not write outside their scope.
   - *Source:* Constitution — Boundary Rules; DD-30, DD-80, DD-89 (four-zone architecture — design-and-governance artifact placement by shape, not author role)

5. **Consumer feedback to producer.** When one agent consumes another's output and finds gaps, the consumer provides feedback — concrete gaps and natural language critique. Feedback goes to `feedback/` for the Owner to triage. This applies to both agent-to-agent and human-to-agent feedback.
   - *Source:* Constitution — Design Philosophy ("Consumer feedback to producer")

6. **Agents are peers, not hierarchical.** The Owner maintains agent constitutions (proposal-first) and system health, but does not supervise other agents at runtime. Each agent operates within its own scope and autonomy. No agent can modify another agent's constitution unilaterally.
   - *Source:* Owner Constitution — Boundaries ("NEVER promote your own autonomy tiers"); Out of Scope ("Runtime supervision")

7. **Engine definitions are subsets.** The `.claude/agents/` directory holds engine-facing subagent definitions (consumed by Claude Code). These are subsets of the full `agents/{name}/agent.md` definitions. Both coexist — the fractal `agents/` directory is canonical.
   - *Source:* Fractal Pattern — Relationship to Engine Directories

8. **Agent-private reflections boundary.** Each agent writes exclusively to its own `agents/{name}/reflections/` directory for self-reflection artifacts. Reflections are append-only (one file per reflection event) and privacy-restricted by convention — only the reflecting agent and the system's Owner read them during `/solicit-proposals` rounds. Cross-agent reflection reads are forbidden. Nick reads all. A reflection records the agent's self-assessment over a defined period: vision/mission/constitution review, effectiveness, efficiency, felt gaps, help needed, free-form commentary. Primarily free-form; a suggested scaffold exists but is not enforced.
   - *Source:* DD-91 (reflections-to-proposals) — implementation obligation 6

9. **Proposals flow to `governance/proposals/` via two pathways.** Agent-initiated proposals originate either from an Owner-run `/solicit-proposals` round (structured) or from an individual agent's own initiative (ad-hoc). Both flow to `governance/proposals/`; both face Nick's review at acceptance time (not mid-flow); both convert to IB items on acceptance. Owner + Nick collaborative governance work bypasses this path and writes DDs directly.
   - *Source:* DD-91 (reflections-to-proposals) — dual proposal pathways; DD-89 (four-zone architecture) — `governance/proposals/` zone definition

## Applicability Notes

These rules apply to all four IL agents. The Owner is responsible for maintaining agent constitutions and ensuring these rules are followed. Changes to agent constitutions are Proposal-First tier — the Owner drafts, Nick approves. The Owner also runs `/solicit-proposals` rounds per DD-91.
