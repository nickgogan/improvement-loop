---
name: "AutoGen"
type: "watched-library"
repo_url: "https://github.com/microsoft/autogen"
description: "Microsoft's framework for multi-agent AI applications that can act autonomously or work alongside humans. Features conversable agents, group chat orchestration, and flexible agent communication patterns. Now in maintenance mode — succeeded by microsoft/agent-framework."
spectrum_position: "monitor"
what_we_use: "Multi-agent conversation patterns, group chat orchestration topology, agent communication protocols, human-in-the-loop integration patterns"
local_derivations: []
last_evaluated_version: "v0.7.5"
last_evaluated_date: "2026-05-25"
maintainer: "microsoft"
status: "maintenance-mode"
tags:
  - "multi-agent"
  - "orchestration"
  - "conversation"
  - "microsoft"
  - "python"
  - "maintenance-mode"
related_findings: []
related_sources: []
date_added: "2026-05-25"
---

## What It Does

Microsoft's framework for creating multi-agent AI applications. Provides conversable agents that can participate in group chats, execute code, use tools, and interact with humans. Features include flexible conversation patterns (two-agent, group chat, hierarchical), human-in-the-loop integration, and code execution capabilities. The framework uses a message-passing architecture for agent communication.

**Note:** AutoGen is now in maintenance mode (community-managed). Microsoft has moved to a successor project (microsoft/agent-framework). Still valuable as a reference for multi-agent patterns given its wide adoption and research influence.

## What We Use From It

Monitor patterns:
1. **Multi-agent conversation patterns** — How agents communicate via message passing in structured conversations
2. **Group chat orchestration** — Speaker selection, round-robin, custom ordering in multi-agent discussions
3. **Agent communication protocols** — Message types, conversation threads, termination conditions
4. **Human-in-the-loop integration** — How human input is solicited and integrated mid-conversation

## Spectrum Rationale

**Monitor** — AutoGen is in maintenance mode and Microsoft is moving to a successor framework. However, its multi-agent conversation patterns and group chat orchestration model influenced many subsequent frameworks. Worth monitoring as a stable reference point for multi-agent communication patterns, though new features will not land. The successor framework (microsoft/agent-framework) may warrant its own entry when it matures.

## Change Signals

Watch for:
- Successor framework (microsoft/agent-framework) reaching stability
- Community-contributed patterns that emerge during maintenance mode
- Research papers building on AutoGen's conversation model
