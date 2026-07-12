---
name: "Linear Walkthroughs — Simon Willison's Agentic Engineering Patterns Guide"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Agentic engineering pattern: coding agent produces a structured walkthrough document of an unfamiliar codebase (or one's own vibe-coded code) for comprehension. Simon's concrete example: used Claude Code + Opus 4.6 + Showboat tool to generate a 6-file walkthrough of a SwiftUI slide app he'd vibe-coded. Key anti-hallucination rule: explicitly instruct the agent to use 'sed or grep or cat' to extract code snippets rather than copy them manually — copying introduces hallucination risk. Showboat commands: 'showboat note' adds Markdown commentary, 'showboat exec' runs a shell command and embeds both the command and output into the doc. Use cases: onboarding to unfamiliar ecosystems, recovering knowledge from stale code, countering skill degradation from LLM-assisted development."
relevance: "High"
added_by: "Nick"
tags:
  - "context-engineering"
  - "prompt-engineering"
  - "agent-design"
  - "claude-code"
  - "documentation"
url: "https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/"
authority:
  - "simon-willison.md"
findings:
  - "agent-generated-codebase-walkthrough-for-onboarding.md"
  - "programmatic-snippet-extraction-via-shell-anti-hallucination.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
date_published: "2026-02-25"
---

# Linear Walkthroughs — Simon Willison

Entry in Simon Willison's "Agentic Engineering Patterns" guide. Created 25 Feb 2026; last modified 4 March 2026. Part of the "Understanding code" chapter group (counterpart: "Interactive explanations"). Previous chapter: "Agentic manual testing." Next: "Interactive explanations."

## Pattern Definition

A technique where a coding agent produces a structured, detailed walkthrough document explaining how a codebase functions. The agent reads source code and generates comprehensive Markdown that demonstrates understanding of the system's architecture and mechanics.

## Key Quotes Preserved

- "Sometimes it's useful to have a coding agent give you a structured walkthrough of a codebase."
- "Frontier models with the right agent harness can construct a detailed walkthrough to help understand how code works."
- "By telling it to use 'sed or grep or cat or whatever you need to include snippets of code' I ensured that Claude Code would not manually copy snippets, since that could introduce risk."
- Author testimony: "I learned a great deal about how SwiftUI apps are structured and absorbed some solid details about the Swift language itself just from reading this document."

## Tools Named

- Claude Code (web interface) with Opus 4.6
- Showboat — purpose-built tool for agents to embed notes + shell exec results into walkthrough docs
  - `showboat note` — add Markdown commentary
  - `showboat exec` — execute shell command, embed both command and output

## Concrete Example

Simon vibe-coded a SwiftUI slide-presentation app called "Present" (~40 minute project), then used Claude Code + Showboat to generate walkthrough.md explaining all Swift files. Output: github.com/simonw/present/blob/main/walkthrough.md.

## Use Cases Named

- Learning new ecosystems and language patterns
- Recovering knowledge from one's own stale/vibe-coded projects
- Countering skill degradation from LLM-assisted development
