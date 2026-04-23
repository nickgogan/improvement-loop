---
name: "Anti-patterns — Simon Willison's Agentic Engineering Patterns Guide"
source_type: "Blog Post"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Single named anti-pattern specific to agentic engineering: inflicting unreviewed agent-generated code on collaborators via PRs. The core claim — opening PRs with 'hundreds (or thousands) of lines of code an agent produced for you' without personal verification outsources verification burden to reviewers. Positive contract: engineer must retain responsibility for initial validation; PRs must carry personally-verified commits. Concerns flagged indirectly: code that has never been executed is 'pure luck' if it works; agents write 'convincing looking' PR descriptions the author hasn't verified. Minor source — one anti-pattern; no standalone finding promoted (covered well enough by existing findings on agent self-reporting unreliability and human-in-the-loop verification)."
relevance: "Medium"
added_by: "Claude"
tags: ["governance", "agent-design", "code-review", "human-in-the-loop"]
url: "https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns/"
authority: ["simon-willison.md"]
findings: []
date_added: "2026-04-23"
---
