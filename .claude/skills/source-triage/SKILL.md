---
name: source-triage
description: >-
  Quick-scan sources to estimate finding density and produce extract/skip/defer verdicts.
  Fetches content, compares against existing KB, and outputs a prioritized triage report.
  Use for Tier 3 (low-priority) sources from the quality audit, or to pre-screen new sources
  before committing to full research-loop extraction. Designed for parallel subagent execution.
user-invocable: true
allowed-tools: Read Grep Glob WebFetch Agent
argument-hint: "[<source-file>...] [--all-unlinked] [--tier <1|2|3>] [--dry-run]"
---

# Source Triage

Quick-scan research sources to estimate finding density and produce extract/skip/defer verdicts without performing full extraction.

## When to Use This Skill

- After a source quality audit identifies sources with zero linked findings
- Before committing to full `/research-loop` extraction on a batch of sources
- To triage newly added sources that haven't been processed yet
- To decide which sources are worth `/transcript-fetcher` + Pass 2 investment

## What This Skill Does NOT Do

- **Does not create findings.** That's `/research-loop`'s job.
- **Does not update source metadata** (beyond adding a triage note). Source status stays as-is.
- **Does not fetch transcripts.** For videos, it works from the source's `key_takeaways`, title, tags, and a quick web summary. If a transcript exists locally, it may skim it.

## Verdicts

Each source gets exactly one verdict:

| Verdict | Meaning | Next Action |
|---------|---------|-------------|
| **EXTRACT** | Source likely has 3+ unlinked findings. Worth full extraction. | Queue for `/research-loop` (Pass 1 for articles, Pass 2 for videos with transcripts) |
| **SKIP** | Source has <2 extractable findings, or findings already exist and cover it. | No further action. Note reason in triage report. |
| **DEFER** | Can't determine density from available information (paywall, dead link, insufficient summary). | Revisit manually or with different access method. |
| **LINK-ONLY** | Source's content is already captured by existing findings, but the source file isn't linked to them. | Queue for `/linkage-repair` instead of extraction. |

## Verdict Decision Tree

For each source, apply these tests in order:

```
1. Can I access the content?
   NO → DEFER (note: "inaccessible — [reason]")

2. Does the content contain actionable patterns?
   (A pattern is: a named technique, a specific tool/config, a quantified result,
    or a workflow with concrete steps. Opinions, overviews, and "X is important"
    are NOT patterns.)
   NO → SKIP (note: "no actionable patterns — [content type: opinion/overview/news]")

3. How many distinct patterns can I identify from a skim?
   0-1 → Check Step 4
   2   → Check Step 4, lean toward SKIP unless patterns are novel
   3+  → EXTRACT

4. Do existing KB findings already cover the patterns I found?
   ALL covered → LINK-ONLY (list the matching findings)
   SOME covered → If uncovered patterns ≥ 2: EXTRACT. If 1: SKIP.
   NONE covered → If patterns ≥ 2: EXTRACT. If 1: SKIP.
```

## Procedure

### Step 0: Determine Scope

Parse arguments to build the source list:

- **Explicit files:** `source-triage tool-shaped-objects.md agent-orchestrators-are-bad.md` — triage these specific sources.
- **`--all-unlinked`:** Find all sources with `findings: []` and triage them.
- **`--tier <n>`:** Read `systems/improvement-loop/operations/research-reports/2026-04-07-source-quality-audit.md` and triage sources in the specified tier.
- **No args:** Prompt for clarification.

### Step 1: Load KB Context

1. Use `Grep` to build a **lightweight dedup index** of existing findings — `name:` field only, plus a 10-word summary derived from the first sentence of `summary:`. Do NOT include full summaries — they blow token budgets at scale. Format: one line per finding, `filename | name | 10-word summary`.
2. For the specific sources being triaged, also grep findings for any that share tags or topic keywords with those sources — include full summaries only for these likely-overlap findings (targeted context, not blanket).
3. Note the current finding count per category (from a quick `category:` grep).

### Step 2: Batch Sources for Parallel Processing

Group sources into batches of 5-8. For each batch, launch a subagent with:

**Subagent prompt template:**

```
You are triaging research sources for a knowledge base. For each source, determine whether
it's worth full extraction by estimating how many NEW, actionable findings it contains.

## What Counts as a Finding
A finding is a distinct, actionable pattern that an AI agent builder could apply:
- A named technique or framework with concrete steps
- A specific tool, config, or integration with implementation details
- A quantified result or benchmark with methodology
- A workflow pattern with clear inputs/outputs

NOT findings: opinions, vague claims ("X is important"), news announcements without
technical detail, rehashed conventional wisdom.

## Decision Tree
[include the full verdict decision tree from above]

## Existing KB Findings (lightweight dedup index)
[include the lightweight index built in Step 1: filename | name | 10-word summary]

## Likely-Overlap Findings (full summaries for targeted dedup)
[include full summaries ONLY for findings that share tags/keywords with this batch's sources]

## Sources to Triage
[for each source in this batch:]
- **Filename:** [EXACT source filename as it exists on disk — use this verbatim in output]
- Name: [source name]
- Type: [source_type]
- URL: [url]
- Key Takeaways: [key_takeaways from frontmatter]
- Tags: [tags]
- Current Linked Findings: [count]

## Instructions
For each source:
1. If it has a URL, use WebFetch to skim the content (read first 3000 chars for articles,
   abstract/intro for papers). For videos without transcripts, rely on key_takeaways + title.
2. Identify distinct actionable patterns (bullet list, 1 line each).
   - A pattern must be **actionable** — a named technique, specific tool/config, quantified
     result, or workflow with concrete steps. Data points ("X launched", "Y raised funding")
     and incremental details on already-covered patterns do NOT count as novel patterns.
3. Check each pattern against the existing KB findings index.
4. Apply the decision tree. Output your verdict.

## Output Format (one per source, strict JSON)
IMPORTANT: The "filename" field MUST be the exact source filename provided above. Do NOT
invent or modify filenames.

{"filename": "exact-source-filename-from-above.md", "verdict": "EXTRACT|SKIP|DEFER|LINK-ONLY",
 "patterns_found": 3, "patterns_novel": 2, "patterns_covered": 1,
 "matched_findings": ["existing-finding-1.md"],
 "reason": "brief explanation",
 "pattern_sketches": ["pattern 1 name", "pattern 2 name", "pattern 3 name"]}
```

### Step 3: Collect and Compile Results

1. Gather all subagent outputs.
2. Parse JSON results.
3. Sort by verdict priority: EXTRACT first, then LINK-ONLY, then DEFER, then SKIP.
4. Within EXTRACT, sort by `patterns_novel` descending (highest-yield first).

### Step 4: Produce Triage Report

Save to `systems/improvement-loop/operations/research-reports/{date}-source-triage.md`:

```markdown
# Source Triage Report — [Date]

## Summary
| Verdict | Count | Est. Novel Patterns |
|---------|-------|---------------------|
| EXTRACT | X | ~Y |
| LINK-ONLY | X | 0 |
| DEFER | X | unknown |
| SKIP | X | 0 |
| **Total** | **X** | **~Y** |

## EXTRACT — Queue for /research-loop
| Source | Type | Novel Patterns | Pattern Sketches |
|--------|------|---------------|-----------------|

## LINK-ONLY — Queue for /linkage-repair
| Source | Matched Findings | Action |
|--------|-----------------|--------|

## DEFER — Needs Manual Review
| Source | Reason |
|--------|--------|

## SKIP — No Further Action
| Source | Reason |
|--------|--------|
```

### Step 5: Update Source Files (optional, if not --dry-run)

For each triaged source, add a triage note to the source file body (not frontmatter):

```markdown
## Triage Note — [Date]
**Verdict:** EXTRACT | SKIP | DEFER | LINK-ONLY
**Reason:** [brief reason]
**Novel patterns identified:** [count] — [pattern sketches]
```

This provides an audit trail so future sessions know the source was evaluated.

## Heuristics by Source Type

These are starting points, not hard rules. Override based on actual content.

| Source Type | Expected Findings (if high-relevance) | Expected Findings (if medium-relevance) | SKIP Threshold |
|-------------|--------------------------------------|----------------------------------------|----------------|
| Video (>15 min) | 5-15 | 2-5 | <2 novel after KB dedup |
| Blog Post (long-form) | 3-8 | 1-3 | <2 novel after KB dedup |
| Blog Post (short/news) | 1-2 | 0-1 | <1 novel |
| Research Paper | 2-5 | 1-2 | <1 novel (unless high rigor) |
| Documentation | 2-6 | 1-2 | <1 novel |
| Tool Release | 1-3 | 0-1 | <1 novel |

## Calibration Notes

- **Speed over depth.** This is triage, not extraction. Spend 30-60 seconds per source, not 5 minutes. Skim, don't read.
- **Lean toward EXTRACT when uncertain.** A false EXTRACT costs one wasted extraction pass. A false SKIP permanently loses findings. When the content looks moderately rich, say EXTRACT.
- **The KB dedup step is critical.** A source with 5 patterns but 4 already in the KB is a SKIP (or LINK-ONLY), not an EXTRACT. Always check.
- **Videos without transcripts get lower confidence.** If you're triaging from `key_takeaways` only, note this in the reason. The verdict may change once a transcript is available.
- **LINK-ONLY is high value.** Discovering that existing findings should be linked to unlinked sources is a win — it fixes the KB's traceability without requiring new extraction work.
- **Don't read full articles for SKIP candidates.** If the title, takeaways, and first 500 chars clearly indicate opinion/overview content, SKIP without fetching the full text. Save tokens for EXTRACT candidates.
