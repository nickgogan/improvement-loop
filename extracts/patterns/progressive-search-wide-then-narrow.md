---
title: "Progressive Search: Wide-Then-Narrow"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "progressive-search-wide-then-narrow"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent has access to a search tool (web, knowledge base, or file system) and the information landscape for the query is not already fully mapped."
  invariants: "The first search query in any research task is broad and short. Narrowing occurs only after evaluating broad results. No specific-query-first without an explicit override."
  governance: "Search strategy (broad-first vs. targeted) is declared in the agent prompt or task spec. Overrides to skip the broad phase require justification in the task context."
  recovery: "If broad queries return zero useful results after 2 attempts, switch to targeted queries with explicit domain terms. Log the failed broad queries to inform future search vocabulary."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Progressive Search: Wide-Then-Narrow

**Source:** [[progressive-search-wide-then-narrow]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

LLM agents tasked with research or information retrieval default to generating long, highly specific search queries that mirror how the model would phrase the question in natural language. These verbose queries frequently return zero results or miss relevant sources because they over-constrain the search space before the agent understands what information actually exists. The agent wastes its search budget on increasingly desperate reformulations of the same over-specific query.

## Forces

- **Specificity vs. discovery.** Specific queries find exact answers fast when you know they exist. But for research tasks, you often do not know what exists, and specificity precludes discovery.
- **Efficiency vs. coverage.** Broad queries return more results but require filtering. Narrow queries return fewer results but may miss the best sources entirely.
- **Search budget vs. exploration depth.** Each search call costs tokens and time. Spending the budget on broad queries may leave nothing for targeted follow-ups. Spending it on narrow queries may never find the right neighborhood.
- **Agent confidence vs. information topology.** The agent believes it knows what to search for, but the actual information landscape (what sources exist, in what format, under what terminology) is unknown until probed.

## Solution

Structure agent search behavior as a two-phase progressive narrowing:

**Phase 1 -- Broad scan:**
1. Start with short, general queries (2-4 words) that describe the topic area, not the specific question.
2. Evaluate results for: what sources exist, what terminology the domain uses, what formats are available (blogs, papers, docs, videos).
3. Map the information topology -- where is the knowledge concentrated?

**Phase 2 -- Targeted dive:**
4. Narrow queries using domain-specific terminology discovered in Phase 1.
5. Target the specific sources, authors, or formats identified as high-value.
6. Iterate within the narrowed space until the question is answered or sources are exhausted.

Implementation in agent prompts:
- Explicitly instruct the agent: "Start with short, broad queries. Assess what exists before narrowing."
- Optionally set a minimum of 1-2 broad queries before any narrow query is permitted.
- Combine with parallel search (multiple broad queries simultaneously) to accelerate Phase 1.

## Consequences

**Positive:**
- Discovers the actual information topology before committing search budget to specific paths.
- Surfaces sources the agent would never find with specific queries (different terminology, unexpected formats, adjacent topics).
- Mirrors expert human research behavior, producing more reliable coverage.
- When combined with parallel subagent search, reduces complex query resolution time by up to 90% (Anthropic production data).

**Negative:**
- Broad queries return noisy results that require filtering effort.
- Adds at least one extra search round before targeted queries begin, increasing minimum latency.
- The broad-to-narrow transition requires judgment about when enough landscape mapping has occurred -- the agent may linger too long in broad mode or transition too early.
- For well-understood domains where the agent already knows the terminology and source locations, the broad phase is wasted effort.

## Known Uses

- Anthropic's production multi-agent research system uses this as a core search strategy.
- Combined with parallel tool calling (3+ tools per subagent, 3-5 subagents per query) in Anthropic's research pipeline.
- Expert human researchers naturally follow this pattern -- librarians call it "reference interview before search."

## Contract

### Preconditions
The agent has access to a search tool (web search, knowledge base, or file system search) and the information landscape for the current query is not already fully mapped from prior work.

### Invariants
The first search query in any new research task is broad and short (2-4 words, topic-level). Narrowing to specific queries occurs only after evaluating results from at least one broad query. No specific-query-first execution without an explicit override in the task spec.

### Governance
The search strategy (progressive broad-first vs. direct targeted) is declared in the agent prompt or task specification. Overrides that skip the broad phase require explicit justification in the task context (e.g., "domain is already mapped from prior research").

### Recovery
If broad queries return zero useful results after 2 attempts with different broad formulations, switch to targeted queries using explicit domain terminology. Log the failed broad queries and the terms that eventually worked to inform future search vocabulary and prompt tuning.
