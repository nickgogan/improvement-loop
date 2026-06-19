---
title: "Watched Blogs"
id: "watched-blogs-index"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-09"
updated: "2026-04-09"
author: "nick"
tags:
  - "catalog"
  - "content-monitoring"
  - "moc"
aliases:
  - "Watched Blogs MOC"
  - "Content Sources Registry"
---

# Watched Blogs

Registry of external blogs and content sources that MetaSystem monitors for new posts relevant to the research pipeline. Each entry tracks the blog's focus areas, author authority link, and a log of discovered posts.

This is the content-monitoring counterpart to [[watched-libraries-index|Watched Libraries]] (which monitors GitHub repos).

## How This Gets Updated

1. **Manual** — Nick adds a new blog to watch
2. **`/watch-blogs` skill** — periodically checks for new posts and produces triage reports
3. **research-loop** — may flag new content sources worth tracking

## Catalog

| Blog | Topics | Frequency | Last Checked | Status |
|------|--------|-----------|--------------|--------|
| [[anthropic-engineering\|Anthropic Engineering]] | context-engineering, claude-code | weekly | 2026-04-09 | active |
| [[anthropic-research\|Anthropic Research]] | evaluation, prompt-engineering, context-engineering | weekly | 2026-04-09 | active |
| [[simon-willison\|Simon Willison]] | tools, mcp, prompt-engineering | weekly | 2026-04-09 | active |
| [[latent-space\|Latent Space]] | orchestration, tools, agent-design | biweekly | 2026-04-09 | active |

## Dataview Query

```dataview
TABLE topics, check_frequency, last_checked_date, status
FROM "systems/improvement-loop/watched-blogs"
WHERE type = "watched-blog"
SORT last_checked_date DESC
```
