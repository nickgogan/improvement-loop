---
name: "Create Custom Subagents — Anthropic Claude Code Docs"
source_type: "Documentation"
status: "Done"
date_processed: "2026-04-23"
date_published: null
key_takeaways: "Canonical Anthropic documentation for subagents in Claude Code. Covers: (1) Built-in subagents (Explore, Plan, general-purpose, statusline-setup, Claude Code Guide) with model / tool / purpose per subagent. (2) Full frontmatter spec (name, description, tools, disallowedTools, model, permissionMode, maxTurns, skills, mcpServers, hooks, memory, background, effort, isolation, color, initialPrompt). (3) FIVE-LEVEL SCOPE PRIORITY LADDER for subagent resolution: Managed settings (1) > --agents CLI flag (2) > .claude/agents/ project (3) > ~/.claude/agents/ user (4) > Plugin agents/ (5, lowest). (4) Agent(agent_type) capability-allowlist syntax for restricting which subagents another agent can spawn. (5) Persistent subagent memory at ~/.claude/agent-memory/{name}/ with user/project/local scope; auto-curation prompt injects first 200 lines or 25KB. (6) Inline mcpServers scoped per-subagent to keep tool descriptions out of main context. (7) Skill preloading via skills: [...] field — full content injection at startup; subagents DO NOT inherit skills from parent. (8) Background vs foreground permission models: background pre-approves upfront and auto-denies everything else; foreground passes permission prompts through. (9) Plugin subagents cannot set hooks, mcpServers, permissionMode for security. (10) Subagents cannot spawn other subagents — infinite-nesting prevention by design. This doc replaces/formalizes the subagent-heuristic language from the earlier session-management blog."
relevance: "High"
added_by: "Claude"
tags: ["agent-design", "subagents", "claude-code", "orchestration", "governance", "canonical-source"]
url: "https://code.claude.com/docs/en/sub-agents"
authority: ["anthropic.md"]
findings:
  - "subagent-scope-priority-ladder.md"
  - "inline-scoped-mcp-servers-per-subagent.md"
  - "subagent-persistent-memory-directory.md"
  - "capability-restricted-agent-spawning-via-allowlist.md"
  - "subagent-isolation-contract.md"
  - "foreground-vs-background-subagent-permission-models.md"
date_added: "2026-04-23"
---
