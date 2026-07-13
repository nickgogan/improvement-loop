---
name: "Skills Portability Across SDK and Framework Boundaries"
summary: "Skills (SKILL.md files in a skills directory) function identically across coding agent SDKs and traditional agent frameworks. Practitioners demonstrate the same skills directory working in Claude Code SDK agents and custom Pydantic AI agents -- the capability layer is framework-agnostic, making skills the durable investment regardless of infrastructure choice."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "sdk-vs-framework-decision-ai-agents.md"
related_findings:
  - file: skills-as-markdown-sop-files-encode-processes.md
    rel: extends
  - file: progressive-skill-loading.md
    rel: same-problem
  - file: domain-expertise-loadable-context-sub-skill.md
    rel: same-problem
  - file: sdk-vs-framework-decision-for-agent-building.md
    rel: enables
  - file: capability-as-agent-composition-primitive.md
    rel: extended-by
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "designing-agent-tools.md"
  - "templates/framework-skill-integration-pattern.md"
tags:
  - "session-95-reextract"
---

## What It Is

Skills defined as SKILL.md files in a skills directory are portable across both batteries-included SDKs and traditional agent frameworks. Cole Medin demonstrates building a Pydantic AI agent with custom skills support that mirrors Claude Code's skill system: a skills directory containing SKILL.md files, a dynamic system prompt that enumerates available skills, and a tool that loads skill content on demand. The skills themselves are identical regardless of whether they run inside the Claude Agent SDK or a custom Pydantic AI agent.

The implementation pattern for frameworks: (1) scan the skills directory at startup to build a skill catalog, (2) inject skill names and descriptions into the system prompt dynamically, (3) provide a "load skill" tool that reads the full SKILL.md content when the agent needs it, (4) the agent follows the skill's instructions to make API calls or execute workflows.

## Why It Matters

Skills are emerging as the primary capability layer for AI agents, replacing direct tool definition. If skills are portable between SDKs and frameworks, they become the most durable investment in agent capability -- surviving infrastructure migrations. A practitioner who starts with the Claude Agent SDK for prototyping and later migrates to Pydantic AI for production can carry their entire skills library forward without modification.

This also means skills represent a framework-agnostic standard for encoding agent capabilities. Unlike tools (which have framework-specific APIs), MCP servers (which require protocol support), or custom code (which is tightly coupled to the agent implementation), skills are plain markdown files that any agent can read and follow.

## Why People Are Using It

- Same skills directory works in SDK and framework agents without modification
- Skills are the "most modern way to add capabilities into our AI agent" per practitioner experience
- Dynamic system prompt injection of skill catalogs keeps agents discoverable without context bloat
- Framework-based agents with skills achieve sub-second response times vs. 10+ seconds with SDK equivalents
- Skills investment compounds across infrastructure changes -- write once, run in any agent

## Potential Improvements

- Standardized skill manifest format that all frameworks can auto-discover
- Skill package managers for sharing and versioning across teams
- Automatic skill-to-tool compilation for frameworks that prefer native tool APIs
- Performance benchmarks comparing skill-based vs. native-tool architectures across frameworks

## Potential Failure Modes

- Skills that depend on SDK-specific features (built-in file search, specific tool names) fail silently in framework agents
- Dynamic system prompt injection of skill catalogs can bloat context in agents with many skills
- No standardized skill format means cross-team portability requires convention alignment
- Complex multi-step skills may execute differently across SDKs and frameworks due to different reasoning patterns
