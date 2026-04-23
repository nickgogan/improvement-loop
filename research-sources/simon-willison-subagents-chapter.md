---
name: "Subagents — Simon Willison's Agentic Engineering Patterns Guide"
source_type: "Blog Post"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Simon's chapter on subagents in his Agentic Engineering Patterns guide. Key insights: (1) A subagent is 'a fresh copy of itself' with a new context window; parent pauses until subagent returns. (2) Subagents are for managing token-heavy operations (test-running, doc-fetching, log-processing) and for parallelizable independent tasks. (3) Root-agent-sufficiency heuristic — 'the root agent is perfectly capable of debugging or reviewing its own output provided it has the tokens to spare.' Over-fragmentation across dozens of specialist subagents is the flagged anti-pattern. (4) Platforms supporting subagents: Claude Code (Explore, custom), OpenAI Codex, Gemini CLI, Mistral Vibe, OpenCode, VS Code, Cursor. (5) User-directed parallelism: prompts like 'Use subagents to find and update all templates affected by this change.' No unique anti-patterns beyond over-fragmentation. Primary value is grounding the general decision-rule, which Anthropic's own subagent docs (see anthropic-claude-code-subagents-docs.md) codify more formally."
relevance: "High"
added_by: "Claude"
tags: ["agent-design", "orchestration", "subagents", "claude-code", "context-engineering"]
url: "https://simonwillison.net/guides/agentic-engineering-patterns/subagents/"
authority: ["simon-willison.md"]
findings: []
date_added: "2026-04-23"
---
