---
name: watch-blogs
description: >-
  Monitor watched blogs for new posts relevant to the research pipeline. Reads the
  watched-blogs registry, searches for recent posts via RSS/Perplexity/WebFetch,
  compares against stored Post Logs, and produces a triage report with recommended
  actions. New posts with EXTRACT verdict get queued as research-source entries.
user-invocable: true
allowed-tools: Read Grep Glob Edit Write WebFetch Agent
argument-hint: "[<blog-name>...] [--all] [--dry-run]"
---

# Watch Blogs

Monitor watched blogs and content sources for new posts and produce triage reports.

## When to Use This Skill

- Periodically (weekly/biweekly recommended) to check for new blog posts
- Before a research-proposer run, to ensure content sources are current
- When the user mentions a blog post or new article
- After adding a new watched-blog entry

## What This Skill Does NOT Do

- **Does not extract findings.** Findings extraction is `/research-loop`'s job. This skill flags posts that may warrant extraction.
- **Does not create authorities.** Authority entries are created manually or by `/research-loop`.
- **Does not enforce check frequency.** The `check_frequency` field is advisory metadata for the operator.

## Procedure

### Step 0: Determine Scope

Parse arguments to build the blog list:

- **Explicit names:** `watch-blogs anthropic-engineering simon-willison` — check these specific blogs.
- **`--all`:** Check all active blogs in the registry. This is the default if no args are given.
- **`--dry-run`:** Discover new posts but don't update entries or create research sources.

### Step 1: Load Registry State

1. Use `Glob` to list all `.md` files in `systems/improvement-loop/watched-blogs/` (excluding `_index.md`).
2. For each blog in scope, use `Read` to load the full entry. Extract:
   - `name`
   - `blog_url`
   - `feed_url` (may be null)
   - `author`
   - `topics`
   - `last_checked_date`
   - `status`
   - Relevance Filter section (body text)
   - Post Log table (all URLs already seen)
3. Build a lookup: `{ filename -> { name, blog_url, feed_url, topics, last_checked_date, known_post_urls, relevance_filter } }`
4. Skip entries where `status` is `paused` or `retired` (unless explicitly named in args).

### Step 2: Fetch New Posts

For each blog, discover recent posts. Use parallel subagents (batches of 3-4) for throughput.

**Subagent prompt template:**

```
You are checking a blog/publication for new posts relevant to an AI agent research pipeline.

## Blog
- Name: [name]
- Blog URL: [blog_url]
- Feed URL: [feed_url or "none"]
- Topics we care about: [topics list]
- Last checked: [last_checked_date]
- Known post URLs (already in Post Log): [list of URLs from Post Log]

## Relevance Filter
[from the blog entry's Relevance Filter section]

## Instructions

1. **Discovery** (try in order, stop when you have results):
   a. If feed_url is provided: Use WebFetch on the feed URL. Parse the XML/Atom for
      <item> or <entry> elements. Extract title, URL, and pubDate/updated for posts
      after [last_checked_date].
   b. Use perplexity_search: "site:[blog_domain] [topics] after:[last_checked_date]"
      with recency filter set to "month".
   c. Use WebFetch on blog_url to scrape the main page for recent post links.

2. **Filter**: For each discovered post:
   - Is the post date after [last_checked_date]? If date is unknown, include it.
   - Does the title/topic match the relevance filter? Skip clearly off-topic posts.
   - Is the URL already in the known post URLs list? Skip if already seen.

3. **Quick triage**: For each new, relevant post:
   - Use WebFetch to read the first ~2000 characters of the post.
   - Count actionable patterns (named techniques, specific tools/configs, quantified
     results, workflows with concrete steps).
   - Estimate finding density.

4. **Output** (strict JSON):
{"blog_name": "[name]",
 "posts_found": [
   {"title": "Post Title",
    "url": "https://...",
    "date": "2026-04-08",
    "pattern_count": 3,
    "pattern_sketches": ["pattern 1", "pattern 2", "pattern 3"],
    "verdict": "EXTRACT|SKIP|DEFER",
    "reason": "brief explanation"}
 ],
 "blog_status": "active|inactive|dead",
 "fetch_method": "rss|perplexity|webfetch"}
```

**Verdict definitions (aligned with source-triage):**

| Verdict | When | Next Action |
|---------|------|-------------|
| `EXTRACT` | Post has 2+ actionable patterns not already in KB | Create research-source entry, queue for `/source-triage` or `/research-loop` |
| `SKIP` | Off-topic, thin content, or patterns already covered by KB | Log in Post Log as `triaged-skip` |
| `DEFER` | Paywall, dead link, can't determine pattern density | Log in Post Log as `triaged-defer` |

### Step 3: Produce Triage Report

Save to `systems/improvement-loop/operations/research-reports/{date}-watch-blogs-triage.md`:

```markdown
# Watch Blogs Triage Report -- [Date]

## Summary
| Blog | Last Checked | New Posts | EXTRACT | SKIP | DEFER | Fetch Method |
|------|-------------|-----------|---------|------|-------|--------------|

## New Posts Detail

### [Blog Name]
**Checked via:** [rss|perplexity|webfetch]

| Post | Date | Patterns | Verdict | Reason |
|------|------|----------|---------|--------|

[repeat for each blog with new posts]

## Action Queue

### Create Research Sources (EXTRACT verdicts)
[list with post title, URL, estimated pattern count]

### Deferred (manual review needed)
[list with reason]

### No Action (SKIP or no new posts)
[list]
```

**Stop here if `--dry-run` was specified.**

### Step 4: Create Research Source Entries

For each post with EXTRACT verdict:

1. Use `Write` to create a new file in `systems/improvement-loop/research-sources/`:
   ```yaml
   ---
   name: "Post Title"
   source_type: "Blog Post"
   status: "Not started"
   key_takeaways: ""
   relevance: ""
   added_by: "Agent (Watch Blogs)"
   tags: [inherited from blog's topics]
   url: "https://..."
   authority: [blog's author field, if set]
   findings: []
   date_added: "2026-04-09"
   ---
   ```
2. Filename: kebab-case slug of the post title + `.md`

### Step 5: Update Watched-Blog Entries

For each checked blog:

1. Use `Edit` to update frontmatter:
   - `last_checked_date` -> today
2. Use `Edit` to append new rows to the Post Log table for all discovered posts:
   - Date Found: today
   - Post Title: title
   - URL: post URL
   - Action: `source-created` (EXTRACT), `triaged-skip` (SKIP), or `triaged-defer` (DEFER)

If a blog was found to be inactive or dead, update `status` to `retired` and note in the triage report.

### Step 6: Update Index

Use `Edit` to update `watched-blogs/_index.md` catalog table with updated last-checked dates.

### Step 7: Summary

Report to the user:
- Blogs checked
- New posts discovered (total)
- Research sources created (EXTRACT count)
- Posts skipped / deferred
- Blogs needing manual attention
- **Suggested next step:** "Run `/source-triage` on newly created sources, or `/research-loop` directly for high-confidence EXTRACT posts"

## Calibration Notes

- **RSS is preferred when available.** It's deterministic, free, and gives structured metadata (dates, titles, URLs). Only fall back to Perplexity/WebFetch when `feed_url` is null.
- **Perplexity `site:` search has limits.** It may not surface all posts, especially for high-volume blogs. The recency filter helps narrow results.
- **Lean toward EXTRACT when uncertain.** A false EXTRACT (one wasted triage pass) is cheaper than a false SKIP (permanent finding loss).
- **Don't create sources for thin content.** Marketing announcements, product launches without technical depth, and "top 10 AI tools" listicles are SKIP.
- **Topics filter is for relevance, not exclusion.** A blog post may be relevant even if it doesn't match a listed topic exactly. Use judgment.
- **Post Log prevents re-processing.** Once a URL appears in the Post Log, it won't be flagged again on subsequent runs. This is the primary dedup mechanism.
- **check_frequency is advisory.** The skill doesn't enforce cadence — it always checks whatever blogs are in scope. The field helps the operator plan when to run the skill.
