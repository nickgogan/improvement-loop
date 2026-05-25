---
name: "Claude Code Architecture Under the Hood (Leak Analysis)"
source_type: "Video"
status: "Done"
key_takeaways: "Engineering-focused breakdown of Claude Code architecture from the leak. Agent loop, 20+ tool registry, hooks as middleware, memory compaction, CLAUDE.md as onboarding doc, skills as reusable instruction sets, sub-agents as distributed worker nodes. Clean room rewrite from TS→Python→Rust in 24 hours. Corroborates existing findings from Nate B Jones analysis."
relevance: "High"
added_by: "Nick"
tags:
  - "claude-code"
  - "tools"
  - "context-engineering"
  - "memory"
url: "https://www.youtube.com/watch?v=szaszUEmjfU"
authority: []
findings:
  - "agent-harness-distributed-system-mental-model.md"
  - "brain-hands-decoupling-architecture.md"
  - "claude-code-12-agent-primitives.md"
  - "context-before-loop-initialization-sequence.md"
  - "framework-abstraction-tax-for-agents.md"
  - "ide-first-claude-code-with-deterministic-hooks.md"
  - "minimal-agent-harness-skeleton-three-primitives.md"
  - "subagent-as-uniform-tool-interface.md"
date_added: "2026-04-09"
date_processed: "2026-04-09"
---
