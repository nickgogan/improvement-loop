---
name: "Using Claude Code: Session Management and 1M Context"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Anthropic's canonical decision matrix for Claude Code context management. Five tools — Continue, /rewind (Esc+Esc), /compact <hint>, /clear, Subagents — each mapped to a specific situation. Rewind over correction: rewind post-file-reads and re-prompt with learnings rather than saying 'that didn't work, try X.' Proactive /compact argument: 'model is at its least intelligent point when compacting,' so 1M context gives time to compact early. Subagent heuristic: 'will I need this tool output again, or just the conclusion?' Bad autocompact happens when model can't predict direction of work. /clear offers zero rot with user-controlled summary; /compact is model-driven, steerable via hint, but lossy. New /usage slash command mentioned."
relevance: "High"
added_by: "Nick"
tags:
  - "claude-code"
  - "context-engineering"
  - "session-management"
  - "orchestration"
url: "https://claude.com/blog/using-claude-code-session-management-and-1m-context"
authority:
  - "anthropic.md"
findings:
  - "claude-code-context-management-decision-matrix-five-tools.md"
  - "proactive-compaction-before-intelligence-degradation.md"
  - "trajectory-engineering-non-linear-session-forking.md"
  - "fork-subagent-parallel-trajectory-exploration.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
date_published: "2026-04-15"
---

# Using Claude Code: Session Management and 1M Context

Anthropic product blog post by Thariq Shihipar (Member of Technical Staff), April 15, 2026. Formalizes Claude Code's five context-management primitives into a decision matrix.

## Key Quotes Preserved

- Context rot: "Model performance degrades as context grows because attention gets spread across more tokens, and older, irrelevant content starts to distract."
- On bad autocompaction: "Bad compacts can happen when the model can't predict the direction your work is going."
- On rewind: "Rewind is often the better approach to correction."
- On compact timing: "Model is at its least intelligent point when compacting."
- On /clear: "Zero rot; you control exactly what carries forward."
- On subagent test: "Mental test: will I need this tool output again, or just the conclusion?"

## Decision Matrix (Transcribed)

| Situation | Tool | Rationale |
|-----------|------|-----------|
| Same task, relevant context | Continue | "Everything in the window is still load-bearing" |
| Wrong path taken | /rewind | "Keep useful file reads, drop failed attempt" |
| Bloated session with stale debugging | /compact <hint> | "Low effort; Claude decides what mattered" |
| Genuinely new task | /clear | "Zero rot; you control exactly what carries forward" |
| Next step generates excess output | Subagent | "Intermediate noise stays in child's context" |
