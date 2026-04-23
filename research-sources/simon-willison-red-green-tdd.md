---
name: "Red/green TDD — Simon Willison's Agentic Engineering Patterns"
source_type: "Blog Post"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Simon's adaptation of red/green TDD for coding agents. Core load-bearing discipline (distinct from textbook TDD): AGENT MUST CONFIRM THE RED STATE before moving to green — 'It's important to confirm that the tests fail before implementing the code to make them pass.' Reason: without the red-verification step, agents risk writing tests that already pass, defeating the purpose of validating new implementation. Simon notes 'every good model understands red/green TDD as shorthand' for the full three-phase cycle. Sample prompt: 'Build a Python function to extract headers from a markdown string. Use red/green TDD.' Explicit anti-pattern: omitting test-failure verification."
relevance: "High"
added_by: "Claude"
tags: ["evaluation", "agent-design", "test-driven-development", "claude-code"]
url: "https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/"
authority: ["simon-willison.md"]
findings:
  - "confirm-failure-first-tdd-agent-discipline.md"
date_added: "2026-04-23"
---
