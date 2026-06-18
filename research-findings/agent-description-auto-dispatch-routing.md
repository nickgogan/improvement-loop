---
name: "Agent Description-Based Auto-Dispatch Routing"
summary: "Claude Code reads all agent definitions in the .claude/agents/ folder and automatically decides when to delegate tasks to custom sub-agents based on description matching — no explicit user instruction required. Agents are defined with a name, description, role context, and tool permissions, mirroring how skills work. Users can also explicitly request a specific agent."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "five-agentic-patterns-claude-code.md"
related_findings:
  - file: "context-aware-routing-skill-classifier-sub-skill.md"
    rel: "same-problem"
  - file: "progressive-skill-loading.md"
    rel: "same-problem"
  - file: "built-in-sub-agent-triad-explore-plan-general.md"
    rel: "extends"
  - file: "aios-architecture-folder-per-role-agent.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - agent-design-patterns.md
tags:
  - "session-95-reextract"
---

## What It Is

Claude Code supports custom sub-agents defined as files in the `.claude/agents/` folder. Each agent definition specifies:

- **Name**: How the agent is identified
- **Description**: What the agent does (e.g., "researches a single gray area decision and returns a structured comparison table with rationale")
- **Role context**: Specific instructions for the agent's behavior
- **Tool permissions**: Which tools the agent has access to

The dispatch mechanism has two modes:

1. **Automatic**: Claude reads the name and description of all agents in the folder and decides when to offload a task to a sub-agent based on description matching. If Claude determines a task matches an agent's description, it delegates automatically.

2. **Explicit**: The user can directly request a specific agent (e.g., "use the advisor-researcher agent for this task").

This mirrors how the built-in sub-agents (explore, plan, general-purpose) work, but extends the mechanism to user-defined agents. The GSD framework is cited as an example — it defines multiple agents in its agents folder, each with specialized roles that Claude dispatches to based on task type.

## Why It Matters

This pattern establishes **agent definitions as a harness-level routing mechanism**. Rather than building explicit routing logic, the harness builder defines agents with clear descriptions and lets the LLM's natural language understanding handle dispatch. This is simpler than programmatic routing but depends on description quality — vague descriptions lead to mis-routing.

For MetaSystem, this validates the agent-as-directory pattern (DD-82) and suggests that agent definitions in `.claude/agents/` serve a dual purpose: they provide behavior constraints for the agent AND routing signals for the dispatcher.

## Why People Are Using It

The description-based dispatch requires no code — it's purely declarative. Define an agent file, describe what it does, and Claude handles the routing. This makes agent composition accessible to non-programmers and allows rapid iteration on the agent roster.

## Potential Improvements

- Add routing confidence thresholds — only auto-dispatch when description match confidence exceeds a threshold
- Support agent composition rules (e.g., "always use agent A before agent B", "never use agent C for task type X")
- Provide dispatch audit logs showing which agent was selected and why

## Potential Failure Modes

- Ambiguous descriptions cause mis-routing (two agents with overlapping descriptions compete for the same task)
- No fallback mechanism when the auto-dispatched agent fails — the main agent may not know the task wasn't completed correctly
- Description-based matching is fragile to prompt phrasing — the same task phrased differently may route to different agents
- Token overhead from reading all agent descriptions at session start scales linearly with agent count
