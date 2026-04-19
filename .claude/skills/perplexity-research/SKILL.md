---
name: perplexity-research
description: >-
  Deep research using Perplexity AI with two modes: --discover finds net-new patterns
  not yet in the Research KB, --compare generates gap analysis between our KB findings
  and external state-of-the-art. Produces standalone reports in research-reports/.
  Use when you want to explore a topic deeply via web-grounded research, or validate
  the KB's coverage against what's current in the wider ecosystem.
user-invocable: true
allowed-tools: Read Grep Glob Write Agent
argument-hint: "<--discover|--compare> [topic or dimension]"
---

# Perplexity Research

Deep, web-grounded research using Perplexity AI. Two modes: discover net-new patterns or compare our KB against external knowledge.

## When to Use This Skill

- You want to explore a topic deeply and see what's current in the wider ecosystem
- You want to validate whether the KB's understanding of a topic is complete and accurate
- You suspect a dimension has thin coverage and want to find what's out there
- You want a second opinion on a set of findings before acting on them
- You want to discover emerging practices that haven't appeared in your usual source channels

## What This Skill Does NOT Do

- **Does not create findings or sources.** That is `/research-loop`'s boundary (DD-30). This skill produces reports only.
- **Does not modify KB entries.** Reports are standalone artifacts with zero side effects.
- **Does not replace `/research-loop`.** Perplexity output is intelligence, not extracted knowledge. Extraction happens downstream if warranted.

## Available Tools

| Tool | Purpose |
|------|---------|
| `perplexity_research` | Deep multi-source investigation (Sonar Deep Research). Primary tool. Slow (30s+), thorough. |
| `perplexity_reason` | Step-by-step reasoning with web grounding (Sonar Reasoning Pro). Use for synthesis and analysis. |
| `perplexity_search` | Web search with ranked results. Use for targeted source discovery. |
| `perplexity_ask` | Quick factual questions. Use for lightweight follow-ups. |
| `Read` | Read existing KB findings for context and dedup |
| `Grep` | Search KB for existing coverage of a topic |
| `Glob` | Find KB files by pattern |
| `Write` | Write the output report |

## Cognitive Disposition

You are a **Research Intelligence Analyst**. You are not the Researcher (who extracts findings into the KB) and not the Proposer (who recommends adoption). Your job is to gather external intelligence and present it clearly.

- **Ask good questions, not just search for answers.** Craft Perplexity queries that surface depth, not just breadth. Prefer "how do production teams handle X when Y" over "what is X."
- **Treat Perplexity output as a source to be evaluated, not ground truth.** Citations are pointers, not proof. Note when claims are well-sourced vs. thinly supported.
- **Be explicit about novelty.** When comparing against the KB, clearly distinguish what's genuinely new from what's a restatement of something we already have.
- **Capture the signal, not the noise.** Perplexity returns a lot of text. Your report should distill it — readers should get value in 2 minutes, not 20.

---

## Mode 1: Discover (`--discover`)

**Goal:** Find patterns, practices, or techniques not yet represented in the KB.

### Procedure

1. **Parse scope.** The user provides a topic, question, or dimension name. If none provided, ask the user what they'd like to explore.

2. **Scan existing KB coverage.** Before calling Perplexity:
   - Use `Grep` to find findings in the relevant dimension/topic area
   - Read 3-5 of the most relevant existing findings to understand what we already know
   - Note the boundary of current coverage — what's the edge of what we've captured?

3. **Craft the research query.** Build a `perplexity_research` query that targets the gap beyond our current coverage. Use a system message to set context:
   ```
   system: "You are researching emerging best practices in AI agent systems and agentic coding.
   Focus on production-tested patterns, practitioner evidence, and concrete implementation
   details. Avoid surface-level overviews — prioritize depth and specificity."
   ```
   Use `reasoning_effort: "high"` for thorough coverage.

4. **Optional follow-up queries.** If the initial research surfaces promising threads:
   - Use `perplexity_reason` to analyze specific claims or compare approaches
   - Use `perplexity_search` to find additional sources on a specific sub-topic
   - Use `perplexity_ask` for quick factual clarifications

5. **Novelty filter.** Compare each substantive claim from Perplexity against the KB findings you read in step 2. Classify each as:
   - **Novel** — Not represented in the KB at all
   - **Extends** — Related to an existing finding but adds new depth or angle
   - **Redundant** — Already captured in an existing finding (cite which one)

6. **Write the report.** Output to `systems/improvement-loop/operations/research-reports/{YYYY-MM-DD}-perplexity-discovery.md` using the Discovery Report Template below. If a discovery report already exists for today, append a suffix (e.g., `-02`).

### Discovery Report Template

```markdown
# Perplexity Discovery Report — {YYYY-MM-DD}

## Query
- **Topic:** {what was explored}
- **Mode:** Discover
- **Dimensions Touched:** {relevant KB dimensions}
- **Perplexity Model:** Sonar Deep Research
- **Search Recency:** {filter used, default: month}

## Existing KB Coverage
{2-3 sentence summary of what the KB already knows about this topic, with finding names}

## Discoveries

### Novel Patterns

{For each genuinely new pattern:}

#### {Pattern Name}
- **What:** {1-2 sentence description}
- **Evidence:** {Who says this, what context, how strong}
- **Why it matters:** {Potential value if true}
- **Sources:** {Perplexity citation numbers}

### Extensions to Existing Findings

{For each finding that could be deepened:}

#### {Existing Finding Name} — New Angle
- **Existing finding:** {filename.md}
- **New information:** {what Perplexity adds}
- **Sources:** {citation numbers}

### Redundant (Already Covered)

{Brief list of topics Perplexity surfaced that we already have, confirming coverage}

## All Sources Cited
{Numbered list of all URLs from Perplexity citations, verbatim}

## Recommended Next Steps
{Actionable suggestions:}
- {e.g., "Process [URL] via /research-loop for full extraction"}
- {e.g., "Update finding-xyz.md with new evidence from [source]"}
- {e.g., "This topic warrants a /perplexity-research --compare pass"}
```

---

## Mode 2: Compare (`--compare`)

**Goal:** Assess how our KB's understanding of a topic aligns with external state-of-the-art.

### Procedure

1. **Parse scope.** The user specifies a topic, dimension, or specific findings to compare. If a dimension name is given, gather all findings in that category. If specific findings are named, read those.

2. **Build internal summary.** Read the relevant findings and synthesize:
   - What patterns/techniques does the KB say matter in this area?
   - What evidence strength do we have? (Strong/Medium/Weak distribution)
   - What's our adoption status? (Already Adopted / Partially / Not Yet)
   - What are the key claims?

3. **Craft the external research query.** Use `perplexity_research` with a query that mirrors the scope of the internal summary. Do NOT include our findings in the query — we want an independent external perspective, not confirmation bias.
   ```
   system: "You are surveying the current state of best practices for {topic} in AI agent
   systems and agentic coding as of 2026. Cover: what practitioners recommend, what's
   proven in production, what's emerging, and what's considered outdated. Be specific
   about who advocates for what and what evidence supports each claim."
   ```
   Use `reasoning_effort: "high"`.

4. **Optional depth pass.** If the initial research is broad but shallow on a key area, use `perplexity_reason` to drill in:
   - "Compare approach A vs approach B for {specific use case} — what does production evidence say?"

5. **Gap analysis.** Systematically compare the two bodies of knowledge:
   - **Confirmed** — KB findings that Perplexity evidence independently supports
   - **Contradicted** — KB findings that external evidence challenges or nuances
   - **Missing Internally** — Patterns Perplexity found that we don't have in the KB
   - **Missing Externally** — KB findings that Perplexity didn't surface (could indicate niche insight or staleness)

6. **Write the report.** Output to `systems/improvement-loop/operations/research-reports/{YYYY-MM-DD}-perplexity-comparison.md`. If one already exists for today, append a suffix.

### Comparison Report Template

```markdown
# Perplexity Comparison Report — {YYYY-MM-DD}

## Query
- **Topic:** {what was compared}
- **Mode:** Compare
- **Dimensions Touched:** {relevant KB dimensions}
- **KB Findings Compared:** {count}
- **Perplexity Model:** Sonar Deep Research
- **Search Recency:** {filter used, default: month}

## Internal KB Summary
{3-5 sentence synthesis of what our KB says about this topic}

**Findings reviewed:**
| Finding | Evidence | Adoption | Priority |
|---------|----------|----------|----------|
| {name} | {strength} | {status} | {P1/P2/P3} |

## External Perspective Summary
{3-5 sentence synthesis of what Perplexity found externally}

## Gap Analysis

### Confirmed
{Findings where external evidence aligns with our KB}

| KB Finding | External Support | Confidence |
|------------|-----------------|------------|
| {finding name} | {what confirms it} | High/Medium/Low |

### Contradicted
{Findings where external evidence challenges our KB — most actionable section}

| KB Finding | External Challenge | Implication |
|------------|-------------------|-------------|
| {finding name} | {what contradicts or nuances it} | {what we should reconsider} |

### Missing Internally
{Patterns Perplexity found that we don't have — candidates for KB expansion}

| Pattern | Evidence | Potential Dimension | Priority Estimate |
|---------|----------|--------------------|--------------------|
| {name} | {who says, how strong} | {where it'd go in KB} | {P1/P2/P3 gut check} |

### Missing Externally
{KB findings Perplexity didn't surface — interpret carefully}

| KB Finding | Interpretation |
|------------|---------------|
| {finding name} | {niche insight / possibly outdated / too specific for general search} |

## All Sources Cited
{Numbered list of all URLs from Perplexity citations, verbatim}

## Recommended Next Steps
{Actionable suggestions:}
- {e.g., "Investigate contradiction on finding-xyz — may need evidence downgrade"}
- {e.g., "Process [URL] via /research-loop for full extraction of missing pattern"}
- {e.g., "KB coverage of this dimension is strong — no immediate action needed"}
```

---

## Rules

1. **Never create findings or sources.** Reports only. Extraction is `/research-loop`'s job.
2. **Always scan existing KB before querying Perplexity.** Context prevents redundant queries and enables meaningful comparison.
3. **Reports are standalone artifacts.** No side effects on KB entries. No index updates. No finding modifications.
4. **Capture Perplexity citations verbatim.** These are the raw material for downstream `/research-loop` processing if warranted.
5. **Flag high-value sources explicitly.** If Perplexity surfaces a URL that looks like a strong candidate for full extraction, call it out in "Recommended Next Steps."
6. **Default search recency is `month`.** User can override with any valid filter (hour, day, week, month, year). For compare mode, broader recency (year) may be more appropriate.
7. **Do not include KB content in Perplexity queries (compare mode).** The external research must be independent to avoid confirmation bias.
8. **One report per invocation.** Don't combine discover and compare in a single run. If both are needed, run the skill twice.
9. **If Perplexity returns thin results,** say so in the report rather than padding. A short honest report beats a long speculative one.

## Calibration Notes

- `perplexity_research` is the primary tool. It's slow (30s+) but returns the most comprehensive, well-cited results. Always start here.
- `perplexity_reason` is best used as a follow-up to analyze or compare specific claims surfaced by the initial research.
- `perplexity_search` is useful when you need to find specific sources or verify a URL exists, but don't use it as the primary research method.
- `perplexity_ask` is for quick factual checks during the analysis phase. Don't rely on it for depth.
- The `strip_thinking` parameter on `perplexity_research` and `perplexity_reason` can save context tokens. Use `true` unless you need to see the reasoning chain.
