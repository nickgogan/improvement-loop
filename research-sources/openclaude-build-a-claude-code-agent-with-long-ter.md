---
notion_id: 3351e08b-9b34-8128-bc43-d175553da3c6
name: 'OpenClaude: Build a Claude Code Agent with Long-Term Memory (Hindsight)'
source_type: Blog Post
status: Done
key_takeaways: 'Practical pattern for adding long-term conversational memory to Claude Code: pre-prompt recall injection + periodic post-turn retention to a structured memory store.'
relevance: High
added_by: Agent (Scheduled Scan)
tags:
- claude-code
- memory
- tools
- session-management
url: https://hindsight.vectorize.io/blog/2026/03/23/claude-code-telegram
authority: []
findings:
- claude-code-long-term-memory-via-pre-prompt-recall.md
- biomimetic-memory-auto-recall-over-tool-based.md
- memory-bank-isolation-per-agent-per-project.md
- structured-fact-extraction-from-conversations.md
date_added: '2026-04-01'
date_processed: '2026-04-07'
date_published: "2026-03-23"
---
# OpenClaude: Build a Claude Code Agent with Long-Term Memory (Hindsight)

Key patterns (from article):
- Before every prompt: query memory store for relevant items; inject into context.
- After responses (periodically): retain conversation chunks every N turns with overlap.
- Config knobs: retainEveryNTurns, retainOverlapTurns, recallBudget, recallMaxTokens.
- Cautions: permissions bypass risk; recall latency/timeouts; plugins require active session.
