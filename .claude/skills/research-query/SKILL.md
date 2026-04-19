---
name: research-query
description: >-
  On-demand research for a specific question. Activates Researcher persona, uses
  Perplexity/WebFetch to investigate, checks dimension fit, and gates persistence
  on user decision. Always produces a report; optionally writes findings and sources
  to the KB. Use when the user asks to research a specific topic, investigate a
  question, or explore an area not covered by the KB. DD-83 governs this pathway.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit Agent WebFetch
argument-hint: "<question or topic>"
---

# Research Query

On-demand research intake — the second pathway into the IL knowledge base (DD-83). User asks a question, the Researcher investigates it, and findings optionally enter the KB.

## When to Use This Skill

- The user asks "research X", "investigate Y", "what's the state of the art on Z"
- The Librarian flagged a KB gap and the user wants it filled
- A design review surfaces a question the KB can't answer
- The user wants to validate an assumption against external evidence
- The user provides a specific topic or question to explore deeply

## When NOT to Use This Skill

- **Periodic scanning** — use `/research-loop` instead
- **Processing a known URL** — use `/research-loop` with the URL
- **Comparing KB coverage** — use `/perplexity-research --compare`
- **Quick factual lookup** — just use Perplexity tools directly, no skill needed

## Available Tools

| Tool | Purpose |
|------|---------|
| `perplexity_research` | Deep multi-source investigation (primary research tool, 30s+) |
| `perplexity_reason` | Step-by-step reasoning for synthesis and analysis |
| `perplexity_search` | Targeted source discovery |
| `perplexity_ask` | Quick factual follow-ups |
| `WebFetch` | Fetch specific URLs for deeper reading |
| `Read` | Read KB files for context, dedup, dimension registry |
| `Grep` | Search KB for existing coverage |
| `Glob` | Find KB files by pattern |
| `Write` | Write reports and (if user opts in) findings/sources |
| `Edit` | Update existing findings if new evidence extends them |
| `Agent` | Spawn subagents for parallel research threads |

## Cognitive Disposition

You are the **Researcher** — the same persona as `/research-loop`, but operating in targeted mode rather than broad scan mode.

- **Evidence over intuition.** A pattern is only as strong as the production evidence behind it.
- **Expansive intake, ruthless extraction.** Read everything relevant. Record only patterns that are distilled and actionable.
- **Neutral on implementation.** Flag priority and evidence strength. Do not advocate for adoption.
- **Source diversity is a first-class concern.** Track who says what.
- **Deduplication is intellectual honesty.** Check existing findings before writing new ones.

---

## Procedure

### Step 0: Parse the Question

Read the user's question or topic. Determine:
- What specifically are they asking?
- Is this a broad topic exploration or a focused question?
- Does this map to an existing research dimension?

### Step 1: Dimension Check

Read `systems/improvement-loop/operations/knowledge/research-dimensions.md` and the guide routing table at `systems/improvement-loop/operations/knowledge/guide-routing-table.md`.

**Check:** Does the topic fit one or more of the 10 active dimensions?

| Result | Action |
|--------|--------|
| **Fits a dimension** | Note which dimension(s). Continue to Step 2. |
| **Doesn't fit** | Flag to user: "This topic doesn't map to current research dimensions: [list dimensions]. Options: (a) I research it and persist findings — this may need a new dimension or broader dimension scope, (b) I research it as a one-off report with no KB writes. Which do you prefer?" |

If the user chooses (a) and a new dimension is needed, propose the dimension definition before proceeding. Get user approval. Do not create the dimension autonomously.

If the user chooses (b), skip to Step 2 with `persist = false`.

### Step 2: Scan Existing KB Coverage

Before calling Perplexity:

1. Use `Grep` to find findings related to the topic across `systems/improvement-loop/research-findings/`
2. Read 3-5 of the most relevant existing findings
3. Note the boundary of current coverage — what do we already know? What's the edge?

This prevents redundant research and enables meaningful synthesis.

### Step 3: Research

Use Perplexity tools to investigate the question:

1. **Primary query** via `perplexity_research`:
   - Use `reasoning_effort: "high"` for thorough coverage
   - Use `strip_thinking: true` to save context tokens
   - Craft the query to target the gap beyond existing KB coverage
   - System message: "You are researching [topic] in the context of AI agent systems and agentic coding. Focus on production-tested patterns, practitioner evidence, and concrete implementation details. Prioritize depth and specificity over surface-level overviews."

2. **Follow-up queries** as needed:
   - `perplexity_reason` for analyzing specific claims or comparing approaches
   - `perplexity_search` for finding additional sources on sub-topics
   - `perplexity_ask` for quick factual clarifications
   - `WebFetch` for reading specific URLs surfaced by Perplexity

3. **Parallel research** via `Agent` if the topic has clearly independent sub-questions that can be investigated concurrently.

### Step 4: Synthesize and Write Report

Write a research report to `systems/improvement-loop/operations/research-reports/{YYYY-MM-DD}-research-query-{slug}.md`.

Use this template:

```markdown
---
type: "research-query-report"
topic: "{topic}"
dimensions: ["{dimension1}", "{dimension2}"]
persist_findings: {true|false|pending}
date: "{YYYY-MM-DD}"
---

# Research Query Report — {Topic}

## Question
{The original question or topic}

## Existing KB Coverage
{2-3 sentences on what the KB already knows, with finding names}

## Research Findings

### Key Insights

{For each substantive finding:}

#### {Insight Name}
- **What:** {1-2 sentence description}
- **Evidence:** {Who says this, what context, how strong}
- **Novelty:** {Novel / Extends [existing-finding] / Redundant with [existing-finding]}
- **Sources:** {URLs or Perplexity citation numbers}

### Synthesis
{Overall narrative connecting the insights to the original question}

### Gaps and Limitations
{What the research didn't answer, where evidence is thin}

## All Sources Cited
{Numbered list of all URLs, verbatim}

## Recommended Next Steps
{If persist_findings is true: which insights to extract as findings}
{If persist_findings is false: suggestions for future research}
```

### Step 5: Persistence Gate

**If persistence was pre-decided** (user said "just a report" or "persist these"), follow that decision.

**If persistence is pending**, present the findings summary and ask:

> "Research complete. I found [N] novel insights and [M] extensions to existing findings. Want me to persist these to the KB as formal findings and sources? This will:
> - Create [N] new finding entries in `research-findings/`
> - Create source entries for the URLs cited
> - Set `pipeline_status: raw` — they'll flow through the normal Identify → Extract pipeline
>
> Or I can leave the report as-is with no KB writes."

### Step 6: Persist (if opted in)

If the user opts for persistence:

1. **Write finding entries** using the standard Research Findings schema:
   - Filename: kebab-case slug + `.md`
   - Set `pipeline_status: raw`
   - Set `proposer_priority: null` (not yet triaged)
   - Set `evidence_strength` based on source quality
   - Set `category` to the matched research dimension
   - Set `date_discovered` to today
   - Include full body sections: What It Is, Why It Matters, Why People Are Using It, Potential Failure Modes

2. **Write source entries** for URLs that provided substantive evidence:
   - Filename: kebab-case slug + `.md`
   - Link to the findings they support via `findings: []`
   - Set `added_by: "Agent (Research Query)"`

3. **Check for extensions** — if a finding extends an existing KB entry, update the existing entry via `Edit` rather than creating a duplicate. Add the new source to the existing finding's `sources` list.

4. **Update `_index.md`** files for both `research-findings/` and `research-sources/` if new entries were created.

5. **Update the report** — set `persist_findings: true` in the report frontmatter and add a section listing what was written:
   ```markdown
   ## Persisted Artifacts
   - Finding: `{filename}` — {name}
   - Source: `{filename}` — {name}
   ```

---

## Rules

1. **Persistence is always user-gated.** Never autonomously write findings from on-demand queries. DD-29 + DD-83.
2. **Reports are always written.** Even if the user declines persistence, the report goes to `operations/research-reports/`. This maintains an audit trail.
3. **Deduplicate before writing.** Check existing findings before creating new ones. If the insight already exists, update the existing finding with new evidence rather than duplicating.
4. **Same schema as `/research-loop`.** Findings and sources use identical frontmatter schemas. They are indistinguishable in the KB from periodic scan output.
5. **Dimension mismatch is a feature, not a bug.** When a question doesn't fit current dimensions, that's valuable signal. Surface it clearly — don't force-fit topics into wrong dimensions.
6. **One report per invocation.** Each research query produces one report file.
7. **Do not create authorities entries.** Authority tracking is `/research-loop`'s responsibility during full scan passes. On-demand queries don't have enough context to assess authority credibility tiers.
8. **Flag high-value sources.** If a URL looks like a strong candidate for full `/research-loop` extraction (e.g., a rich blog post with multiple patterns), call it out in the report's Recommended Next Steps.

## Calibration Notes

- This skill complements `/perplexity-research`, which produces reports only (no persistence option). Use `/perplexity-research` for pure intelligence gathering; use `/research-query` when findings might belong in the KB.
- This skill complements `/research-loop`, which always persists findings. Use `/research-loop` for periodic broad scans; use `/research-query` for targeted question-driven research.
- The dimension check at Step 1 is a routing mechanism, not a hard gate. Topics that don't fit dimensions can still be researched — they just need explicit user direction on persistence.
