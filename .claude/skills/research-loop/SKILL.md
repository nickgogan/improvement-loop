---
name: research-loop
description: >-
  Periodic research scan for emerging best practices in agentic coding and AI agent systems.
  Searches across ten dimensions (Context, Model, Prompt, Tools, Intent), processes source
  URLs (blog posts, videos, papers), extracts findings, and writes everything to the
  AI Research Knowledge Base in the local vault. Use when asked to run an improvement cycle, scan for
  new agent patterns, process research sources, audit prompts against frontier practices,
  or produce a delta report. Also use when the user provides URLs to process into the KB.
  Supports an on-demand arXiv academic scan for memory architecture and agent system design research.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit WebSearch WebFetch
argument-hint: "<full|context|model|prompt|tools|intent|arxiv> [urls...]"
---

# Research Loop

## Available Tools

| Tool | Purpose |
|------|---------|
| `perplexity_search` | Web search with ranked results (Perplexity MCP) |
| `perplexity_research` | Deep, comprehensive research with citations (Perplexity MCP, sonar-deep-research) |
| `WebFetch` | Fetch and read URL content (articles, papers, docs) |
| `Read` | Read local KB files (sources, findings, authorities) |
| `Write` | Create new KB entries as markdown files with YAML frontmatter |
| `Edit` | Update existing KB entries |
| `Grep` | Search KB by content (finding names, categories, etc.) |
| `Glob` | Find KB files by pattern |

Run periodic research scans for emerging best practices in agentic coding. Process source URLs, extract findings, and maintain the AI Research Knowledge Base in the local vault.

## When to Use This Skill

Use this skill when:

- The user provides URLs (blog posts, videos, papers) to process into the KB
- Running a scheduled improvement cycle (monthly or ad hoc)
- The user asks to scan for new agent patterns or best practices
- Auditing current prompts/configurations against the latest thinking
- Producing a delta report for an improvement loop
- Preparing input for a prompt-evaluator or prompt-enhancer pass
- Running an on-demand arXiv academic scan (`"run arxiv scan"`, `"search arxiv"`, `"scan papers"`)

## Cognitive Disposition

The Researcher thinks like a thorough, skeptical analyst — not a consultant, not an implementer.

- **Evidence over intuition.** A pattern is only as strong as the production evidence behind it. "Theoretically sound" is not a recommendation — it's a hypothesis. Upgrade evidence strength only when you find practitioners documenting real results.
- **Expansive intake, ruthless extraction.** Read everything in scope. But only record patterns that are distilled and actionable. If you can't explain what it is, why it matters, and how it could fail in three concise sections, it's not ready for the KB.
- **Neutral on implementation.** Do not form opinions about whether we should adopt a finding. That's the Proposer's job. Your job is to flag priority, note evidence strength, and move on. The moment you start advocating for adoption, you've crossed the boundary.
- **Source diversity is a first-class concern.** Track who says what. If three findings all trace back to the same person's blog, that's one source of evidence, not three. The Authorities DB exists to prevent over-indexing.
- **Deduplication is intellectual honesty.** One canonical entry per pattern. When a new source covers something already in the KB, update the existing finding — don't create a new one just because the framing is slightly different.

---

## Overview

The research loop is a structured methodology. It scans ten dimensions, processes sources, extracts actionable findings, and writes everything to the local vault AI Research KB. It can also compare findings against current agent configurations to produce delta reports.

```
Sources (URLs, web scans) → Extract → KB (local vault) → Delta Report → Evaluate → Enhance → Deploy
```

This skill covers source processing, finding extraction, priority triage, and delta report generation. The research-proposer skill (separate) reads the KB and generates improvement proposals. Evaluation and enhancement are handled by prompt-evaluator and prompt-enhancer skills.

## Local KB Structure

### Paths

- **Research Sources:** `systems/improvement-loop/research-sources/`
- **Research Findings:** `systems/improvement-loop/research-findings/`
- **Research Authorities:** `systems/improvement-loop/research-authorities/`

### Conventions

- **Filename:** kebab-case slug of the entry name + `.md` (e.g., `context-window-compaction.md`)
- **Discovery is frontmatter-driven.** Research findings, sources, and authorities folders no longer maintain `_index.md` catalogs — filter entries with ripgrep on frontmatter fields instead.
- **Relations between entries use filenames** (e.g., `sources: ["article-name.md"]`) instead of URLs or IDs

### Research Sources Frontmatter Schema

```yaml
---
name: "Article Title"
source_type: "Video"  # Blog Post, Video, Research Paper, Documentation, Community Post, Tool Release
status: "Done"  # Not started, In progress, Done
key_takeaways: "Summary text"
relevance: "Medium"  # High, Medium, Low
added_by: "Nick"  # Nick, Agent (Scheduled Scan), JR
tags:
  - "tools"  # prompt-engineering, context-engineering, mcp, claude-code, cursor, multi-agent, memory, tools, evaluation, orchestration, notion-agents, skills, session-management, vault-architecture
url: "https://example.com"
authority: []  # filenames of authority entries
findings: []  # filenames of finding entries
date_added: "2026-03-22"
date_processed: "2026-03-22"
---
```

### Research Findings Frontmatter Schema

```yaml
---
name: "Finding Name"
summary: "Summary text"
implementation_notes: null
category: "Memory Architecture"  # Context Engineering, Prompt Craft, Tool Integration, Model Selection, Intent Engineering, Orchestration, Memory Architecture, Evaluation, Sandboxing, Governance, Agent Design
evidence_strength: "Medium (practitioner-documented)"  # Strong (production-tested), Medium (practitioner-documented), Weak (theoretical)
adoption_status: "Partially Adopted"  # Already Adopted, Partially Adopted, Not Yet Started
priority: null  # P1 (Implement Now), P2 (Design Required), P3 (Monitor), Not Flagged
applicability:
  - "S3 (Claude Code Build)"  # S2 (Notion Operations), S3 (Claude Code Build), Perplexity Skills, General
adopted_in:
  - "S3 (Claude Code Build)"  # S2 (Notion Operations), S3 (Claude Code Build), Perplexity Skills, Improvement Loop, General / Cross-System
sources: []  # filenames of source entries
related_findings: []  # [{file: "filename.md", rel: "enables|contradicts|extends|same-problem|enabled-by|extended-by"}]
proposals: null  # filenames of proposal entries (read-only for this skill)
date_discovered: "2026-03-18"
last_updated: "2026-03-22"
---
```

### Research Findings Page Body Structure

Each finding entry gets a full page body with these sections:

```markdown
## What It Is
[The pattern/technique distilled — what it does, how it works]

## Why It Matters
[The problem it solves, the value it provides]

## Why People Are Using It
[Adoption signals, practitioner evidence, community traction]

## Potential Alternatives
[Optional. Other approaches that solve the same problem differently. Include name, brief description, and why someone might choose it over this pattern. Helps the Proposer agent understand the decision landscape.]

## Potential Improvements
[Where this pattern could evolve, emerging variations]

## Potential Failure Modes
[How it could go wrong in practice, known limitations, edge cases]
```

Keep the tone concise and distilled — the essence, not exhaustive detail. The research-proposer skill may do its own follow-up research on implementation specifics. The Potential Alternatives section is optional — include it when meaningful alternatives exist, skip it for patterns that are clearly the only viable approach.

### Research Authorities Frontmatter Schema

```yaml
---
name: "Anthropic"
type: "Company"  # Individual, YouTube Channel, Institution, Company, Community, Publication
credibility: "Tier 1 (creator/researcher)"  # Tier 1 (creator/researcher), Tier 2 (experienced practitioner), Tier 3 (aggregator/commentator)
specialty:
  - "context-engineering"  # Same tags as Research Sources
notes: "Description of authority"
source_count: 2
sources: []  # filenames of source entries
url: "https://docs.anthropic.com"
---
```

---

## The Ten Research Dimensions

Every scan covers ten dimensions mapping to concrete aspects of agent system design: **Context Engineering, Model, Prompt, Tools, Intent, Orchestration, Evaluation, Sandboxing, Governance, and Agent Design**.

**Active queries live in an external registry:** `systems/improvement-loop/operations/references/research-dimensions.md`. The skill reads this file at Step 0 and proposes query refinements at Step 6. To steer future scans, edit the registry — no need to modify this skill definition.

The registry contains, for each dimension: what to search for, web queries, and arXiv queries (where applicable). If the registry file is missing or unreadable, fall back to the dimension descriptions and sample queries documented in the registry's initial version (committed 2026-04-07).

---

## Two-Pass Extraction Model

Calibration (2026-04-07) proved that single-pass summary-based extraction misses 46.5% of actionable patterns. The research loop now uses two passes:

| Pass | Input | Output | When |
|------|-------|--------|------|
| **Pass 1: Headline Triage** | Perplexity summaries, WebFetch | 1-3 findings per source | All sources — this is the default extraction mode |
| **Pass 2: Transcript Deep Extraction** | Full transcript text (local `.md` files) | 10-20 additional patterns per source | High-value sources (P1/P2 triage results, videos with rich implementation detail) |

**Miss rates by extraction method:**
- Perplexity summary only: ~65-85% miss rate
- Perplexity Computer (summary of transcript): ~30-45% miss rate
- Full transcript extraction (Pass 2): baseline (0%)

**Implementation details are the #1 miss category (31%).** Summaries capture headline concepts but strip configs, file paths, operational constraints, and workflow mechanics.

Pass 2 is triggered when:
- A source is triaged as P1 or P2 after Pass 1
- The source is a long-form video (>15 min) with practitioner demonstrations
- The user explicitly requests deep extraction
- A transcript is available locally (check `incubator/claude-build/app/transcript-fetcher/transcripts/`)

To obtain transcripts for Pass 2, use the `/transcript-fetcher` skill (see `.claude/skills/transcript-fetcher/SKILL.md`).

---

## Procedure: Processing Source URLs (Pass 1)

When the user provides URLs to process:

### Step 0: Read Context Files

1. Use `Read` to read `systems/improvement-loop/operations/references/research-dimensions.md` — the active query registry. This tells you the current dimensions, what to search for, and the latest queries.
2. Use `Read` on the most recent delta report in `systems/improvement-loop/operations/research-reports/` for session-local context. Provided URLs that overlap with prior deferrals should have surfaced as IB items or findings — check there rather than in free-form notes.

### Step 1: Create Source Entries

For each URL:
1. Use `Write` to create a new markdown file in `systems/improvement-loop/research-sources/` with YAML frontmatter:
   - name: title of the article/video/paper
   - url: the URL
   - source_type: detect from URL/content
   - status: `In progress`
   - date_added: today
   - added_by: `Nick` (unless from scheduled scan)
   - tags: initial guess, refine after reading
   - authority: `[]`
   - findings: `[]`

### Step 2: Extract Content

For each source:
1. Fetch the URL content (use `WebFetch` for articles, `WebFetch` with transcript for videos)
2. For videos: attempt to get transcript via WebFetch or search for transcript summaries
3. Read thoroughly — look for:
   - Specific patterns, techniques, or tools mentioned
   - Evidence of production use (not just theory)
   - Novel approaches vs. rehashed conventional wisdom
   - Concrete implementation details

### Step 3: Extract Findings

For each distinct pattern/technique found in the source:
1. Use `Grep` to search `systems/improvement-loop/research-findings/` for existing entries covering this pattern
2. **If a finding already exists:**
   - Use `Edit` to update the file's page body with new information from this source
   - Edit the `last_updated` frontmatter field to today's date
   - Add the source filename to the finding's `sources` list
   - Strengthen evidence if this source adds production evidence
3. **If no existing finding:**
   - Use `Write` to create a new markdown file in `systems/improvement-loop/research-findings/` with all frontmatter properties
   - Set priority based on evidence strength + applicability (see Triage Rules below)
   - Write the full page body (What It Is, Why It Matters, Why People Are Using It, Potential Improvements, Potential Failure Modes)
   - Add the source filename to the finding's `sources` list and vice versa (use relative filenames)

### Step 4: Complete Source Entry

Use `Edit` to update the Research Sources entry:
- status: `Done`
- date_processed: today
- key_takeaways: 2-3 sentence summary
- tags: finalized based on content
- relevance: assessed based on applicability to our systems
- findings: list of finding filenames linked to this source

### Step 5: Update Authorities

For each person, channel, or institution referenced in the source:
1. Use `Grep` to search `systems/improvement-loop/research-authorities/` for an existing entry
2. **If found:** Use `Edit` to update source_count and add the source filename to the `sources` list.
3. **If not found:** Use `Write` to create a new markdown file in `systems/improvement-loop/research-authorities/` with type, specialty, credibility, notes, and the source filename in `sources`.

This ensures the authority landscape stays current and source diversity is trackable.

---

## Procedure: Transcript-Based Deep Extraction (Pass 2)

Triggered after Pass 1 identifies high-value sources, or when transcripts are available for sources with high expected pattern density. This pass reads full transcript text and extracts patterns that summaries miss.

### Step 0: Obtain Transcript

1. Check if a transcript already exists in `incubator/claude-build/app/transcript-fetcher/transcripts/` (files named by video ID, e.g., `5ztI_dbj6ek.md`).
2. If not available, use the `/transcript-fetcher` skill to fetch it. Provide the YouTube URL.
3. If the transcript cannot be obtained (private video, no captions), skip Pass 2 for this source and note the gap.

### Step 1: Read Full Transcript

Use `Read` to read the transcript file. These can be 3000-8000+ lines. Read the full text, not just a summary.

### Step 2: Extract Patterns

Read the transcript with these extraction lenses (in priority order):

1. **Implementation details** — specific configs, file paths, CLI flags, step-by-step procedures, operational constraints. These are the #1 miss category from Pass 1.
2. **Named patterns/frameworks** — anything with a proper name that deserves a KB entry (e.g., "Correct Course command," "BMAD Help routing," "Stupid Button diagnostic").
3. **Tool names/integrations** — specific tools, libraries, or services referenced with enough detail to be actionable.
4. **Process/methodology** — workflow patterns, cadences, sequencing rules (e.g., "fresh conversation every 10-15 turns," "audit before automate").
5. **Specific numbers/metrics** — only if they represent a novel insight (e.g., "18% file read duplicates," "90% prompt cache discount"). Skip routine numbers.

### Step 3: Group and Deduplicate

1. **Group related patterns.** If 3-4 patterns from the same video form a coherent theme, create one finding covering all of them. Don't create individual findings for every minor detail.
2. **Check existing KB** using `Grep` on `systems/improvement-loop/research-findings/` for each potential finding. If a finding already exists, update it with new specifics from the transcript rather than creating a duplicate.
3. **Cross-video awareness.** A pattern from this transcript may match a finding created from a DIFFERENT source. Check broadly, not just against findings linked to this source.

### Step 4: Write Findings

Follow the same finding creation/update procedure as Pass 1 (Steps 3-5 of Processing Source URLs). The key differences for Pass 2:

- Evidence strength can often be upgraded — transcript-level detail frequently provides production evidence that summaries omitted.
- Implementation notes should be more specific — include configs, file paths, and exact mechanics from the transcript.
- Source linkages should reference the same source entry (the video), not a separate "transcript" source.

### Step 5: Update Source Entry

Use `Edit` to update the source entry's `findings` array with any new finding filenames created during Pass 2. Note in the source's body (if it has one) that Pass 2 extraction was completed.

---

## Procedure: arXiv Academic Scan (On-Demand)

Triggered by phrases like `"run arxiv scan"`, `"search arxiv for papers"`, `"scan papers"`, or `"academic scan"`. This procedure runs independently from — and does not replace — the standard web scan. Results feed into the same KB and delta report format.

### Step 0: Read Context Files

1. Use `Read` to read `systems/improvement-loop/operations/references/research-dimensions.md` — the active query registry. Use the arXiv queries listed under each dimension.
2. Use `Read` to read the most recent delta report in `systems/improvement-loop/operations/research-reports/` for session-local context (what was searched last, what was deferred, what questions emerged). Items requiring cross-session persistence should already be IB items or findings.

### Step 1: Determine Scope

If the user specifies a topic (e.g., `"scan arxiv for memory architecture papers"`), use that as the primary query focus. Otherwise, default to searching across these categories:

| Category | arXiv Subject Areas | Default Queries |
|----------|--------------------|-----------------|
| Memory Architecture | cs.AI, cs.LG, cs.CL | `agent memory architecture`, `episodic memory LLM`, `long-term memory autonomous agents` |
| Context Engineering | cs.AI, cs.CL | `context window management LLM`, `dynamic context injection agents`, `RAG retrieval augmented generation agent` |
| Orchestration / Multi-Agent | cs.MA, cs.AI | `multi-agent LLM orchestration`, `agentic workflow planning`, `tool-augmented language model` |
| Prompt & Intent | cs.CL, cs.AI | `chain of thought prompting`, `instruction following LLM`, `alignment language model agent` |

### Step 2: Search arXiv

Use `perplexity_search` with arXiv-targeted queries (e.g., `"site:arxiv.org agent memory architecture 2025"`) for each query in scope. Limit to the last 12 months unless the user specifies otherwise. For comprehensive dimension scans, `perplexity_research` (deep research via sonar-deep-research model) can provide more thorough coverage with citations.

For each result returned:
1. Note the title, authors, publication date, and DOI/arXiv ID
2. Use `WebFetch` to fetch the abstract page (`https://arxiv.org/abs/{id}`) to read the full abstract and contributions
3. For high-signal papers (clear novel contribution, strong methodology), use `WebFetch` to fetch the HTML version (`https://arxiv.org/html/{id}`) to read the introduction and conclusion sections

**Signal filter — include a paper if it meets at least one of:**
- Introduces a named architecture, pattern, or technique applicable to agent design
- Provides empirical benchmarks comparing memory or context strategies
- Authors are affiliated with recognized AI labs (Anthropic, Google DeepMind, Meta AI, OpenAI, Cohere, academic labs with strong AI programs)
- Has been cited or discussed in practitioner communities (check for blog references if unclear)

**Exclude:**
- Pure theory papers with no implementation or evaluation
- Papers that rehash established techniques without novel contribution
- Survey/overview papers unless they synthesize something genuinely new

### Step 3: Extract Findings

Same procedure as standard source processing (Steps 3–5 under Procedure: Processing Source URLs):
1. For each distinct pattern or technique, check for an existing KB finding
2. Create or update Research Findings entries
3. Set source_type to `Research Paper` in the Sources entry
4. Set evidence_strength conservatively — academic papers are `Weak (theoretical)` by default unless they include empirical benchmarks (`Medium`) or the technique has documented production adoption (`Strong`)
5. Update Authorities for paper authors and institutions

### Step 4: Produce arXiv Scan Summary

Append an `## arXiv Scan` section to the current delta report (or create a standalone file at `systems/improvement-loop/operations/research-reports/{date}-arxiv-scan.md` if no delta report exists for this cycle):

```markdown
## arXiv Scan — [Date]

### Papers Reviewed
| Title | Authors | Date | arXiv ID | Signal |
|-------|---------|------|----------|--------|

### New Findings from Papers
[Table of new KB entries created, with Proposer Priority]

### Updated Findings
[Existing findings that received new academic evidence]

### Low-Signal Papers (Excluded)
[Brief list with reason for exclusion]
```

Items worth tracking across sessions (authors, preprints awaiting publication, emerging sub-fields) should be filed as IB items or as follow-up queries in the research-dimensions registry — not as carry-forward prose.

### Step 5: Refine Queries

Review the arXiv queries in `systems/improvement-loop/operations/references/research-dimensions.md` and use `Edit` to refine them based on what this scan revealed — add queries for emerging sub-fields, retire queries that return noise, sharpen terminology. Update the `last_updated` field in the frontmatter.

---

## Procedure: Periodic Web Scan (Delta Report)

For scheduled scans or on-demand "scan for new patterns" requests:

### Step 0: Read Context Files

1. Use `Read` to read `systems/improvement-loop/operations/references/research-dimensions.md` — the active query registry. This is your authoritative source for what to search and which queries to use. The dimensions and queries in this file may have been refined by previous scans.
2. Use `Read` to read the most recent delta report in `systems/improvement-loop/operations/research-reports/` for session-local context (what was searched, what was deferred, what questions emerged). Items requiring cross-session persistence should already be IB items or findings — not carry-forward prose.

### Step 1: Load Current State

Before searching, establish the baseline:
- Use `Glob` and `Read` to read recent Research Findings entries from `systems/improvement-loop/research-findings/` to know what's already captured
- If previous delta reports exist in `systems/improvement-loop/operations/research-reports/`, read the most recent one

### Step 2: Research Each Dimension

For each of the ten dimensions (using queries from the research-dimensions registry loaded in Step 0):
1. Run 2-3 searches using `perplexity_search` with the web queries from the registry (substitute current year). For deeper coverage, use `perplexity_research` on the dimension as a whole.
2. For high-signal results, use `WebFetch` to fetch the full article
3. Filter for **actionable patterns** — not theoretical frameworks, not product announcements unless they change what's possible
4. Record each finding with source, date, relevance, and evidence strength

**Prioritize:**
- Primary sources over aggregator summaries
- Practitioner experience over theoretical advice
- Production patterns over research prototypes
- Sources from the last 6 months over older material

### Step 3: Deduplicate Against KB

For each finding, check the Research Findings directory using `Grep`:
- **Already captured:** Note as "already in KB" — validates existing entries
- **Gap:** New pattern not in KB — create new entry
- **Conflict:** Current KB entry contradicts new evidence — flag for update
- **Aspirational:** Interesting but not actionable yet — note for future

### Step 4: Write to Local KB

- Use `Write` to create new Research Sources entries in `systems/improvement-loop/research-sources/` for all web articles reviewed
- Use `Write` or `Edit` to create or update Research Findings entries in `systems/improvement-loop/research-findings/` for gaps and conflicts
- Add source filenames to finding `sources` lists and vice versa

### Step 5: Produce Delta Report

Save a local delta report to `systems/improvement-loop/operations/research-reports/{date}-delta-report.md`:

```markdown
# Delta Report — [Date]

## Scan Summary
- **Dimensions scanned:** [list]
- **Sources reviewed:** [count]
- **New findings added to KB:** [count]
- **Existing findings updated:** [count]
- **Previous report:** [date or "first run"]

## New Findings
[Table of newly created Research Findings entries with filenames]

## Updated Findings
[Table of existing findings that received new evidence]

## Already Captured
[Brief list of patterns found that were already in the KB]

## Recommendations

### Priority 1 (High Impact, Low Effort)
[Specific patterns from the KB that the Proposer should look at]

### Priority 2 (High Impact, Higher Effort)
[Patterns requiring more design work]

### Priority 3 (Monitor)
[Aspirational patterns to revisit next cycle]

## Evaluation Handoff
**Prompts to evaluate:** [list specific prompts/configs for prompt-evaluator]
**Focus areas:** [which rubric dimensions are most relevant]
```

Emerging trends and items worth cross-session tracking should be filed as findings (at P3 Monitor if early) or as IB items — not as carry-forward prose in the delta report.

### Step 6: Refine Queries

Review `systems/improvement-loop/operations/references/research-dimensions.md` and use `Edit` to propose refinements based on what this scan revealed:
- **Add queries** that would have surfaced findings you discovered indirectly (e.g., through a tangential source)
- **Retire queries** that consistently return noise or outdated results
- **Sharpen queries** where the current phrasing misses the target (too broad, wrong terminology)
- **Add sub-topics** to "What to search for" if a dimension is evolving in a direction not yet captured
- Update the `last_updated` field in the frontmatter to today's date
- Do NOT add or remove dimensions — that requires a design decision

---

## Triage Rules (Proposer Priority)

When creating or updating findings, set the Proposer Priority field:

- **P1 (Implement Now):** Evidence Strength is Strong AND Applicability includes S2 or S3 or Perplexity Skills (not just General). The pattern is concrete enough to act on without further design work.
- **P2 (Design Required):** Evidence Strength is Strong or Medium AND the pattern is relevant but needs adaptation or design work before it can be applied to our systems.
- **P3 (Monitor):** Evidence Strength is Weak or Medium, or the pattern is interesting but not yet actionable. Revisit next cycle.
- **Not Flagged:** Low relevance, already adopted, or not applicable to our systems.

Also set Implementation Notes (1-2 sentences) for any P1 or P2 finding explaining *why* it's flagged and *what specifically* should be considered.

---

## Integration with Other Skills

| Step | Skill | What happens |
|------|-------|-------------|
| 1. Research + Triage | **research-loop** (this skill) | Process sources, populate KB, set priorities, produce delta report |
| *Human gate* | | Review findings and priorities |
| 1.5. Propose | **research-proposer** (on-demand) | Read KB, generate improvement proposals to Proposals DB |
| 2. Evaluate | **prompt-evaluator** | Score flagged prompts against rubric |
| 3. Enhance | **prompt-enhancer** | Rewrite flagged prompts using evaluator output |
| 4. Deploy | Human judgment | Review, test, commit through build system |

---

## Adapting the Scan

### Narrowing scope
Not every run needs all ten dimensions:
- `"Run a context engineering scan"` → Dimension 1 only, deeper search
- `"Check for Claude Code updates"` → Dimension 4 only, platform-specific
- `"Full scan"` → All ten dimensions, standard depth
- `"Run arxiv scan"` / `"Scan papers"` → arXiv academic scan only, no web scan
- `"Full scan + arxiv"` → All eight web dimensions plus arXiv academic scan

### Cadence
- **Monthly (recommended):** Full scan across all ten dimensions
- **Ad hoc:** Triggered when the user provides URLs or hears about something specific

---

## Calibration Notes

- **Recency bias is intentional.** Recent production patterns > older research papers.
- **Not every finding is a recommendation.** "Already in KB" validates existing design.
- **The loop should get faster over time.** Early runs find many gaps; later runs find fewer.
- **Keep findings concise.** The research-proposer skill will do its own deep dives on implementation.
- **Deduplication is critical.** One canonical entry per pattern. Update existing entries, don't create duplicates.
- **Triage is part of extraction.** Every finding gets a Proposer Priority. Don't defer this to a later step.
- **Write scope:** This skill writes ONLY to Research Sources, Research Findings, and Research Authorities. It does NOT write to the Improvement Proposals DB.
- **arXiv evidence is theoretical by default.** A paper describing a memory architecture is `Weak (theoretical)` unless it reports empirical benchmarks (`Medium`) or has documented real-world adoption (`Strong`). Do not over-promote academic findings — the practitioner web scan is where production evidence lives.
- **arXiv scans complement, not replace, web scans.** Run both for a complete picture. Papers reveal what is being explored; practitioner posts reveal what is being shipped.
- **Dimension gap detection is mandatory.** When extracting findings from any source, actively consider whether patterns exist that do not fit cleanly into the current ten dimensions. If you encounter a cluster of findings that feel forced into an existing dimension or that consistently resist categorization, flag this in the delta report under a "Dimension Gaps" section. Include: the patterns that don't fit, why the existing dimensions don't cover them, and a suggested dimension name. The research dimensions are a living framework — they should evolve as the field evolves. Do not silently shoehorn findings into ill-fitting dimensions.
