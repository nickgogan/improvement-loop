---
title: "Context Curation Over Context Stuffing"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "context-curation-over-context-stuffing"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent operates within a bounded context window; the available information exceeds what the context window can hold without quality degradation."
  invariants: "Context is curated by a human or explicit policy before injection; every item in the context window has a justifiable reason for being there."
  governance: "Context inventories are periodically audited for signal-to-noise ratio; curation criteria are documented and versioned."
  recovery: "If over-pruning causes hallucinations or missed information, restore excluded content from retrieval and re-curate with broader inclusion criteria."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Context Curation Over Context Stuffing

**Source:** [[context-curation-over-context-stuffing]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams building agent systems default to loading all available information into the context window, assuming more context produces better output. In practice, indiscriminate context loading degrades output quality -- the agent's attention is diluted by irrelevant material, conflicting signals create ambiguity, and the model spends capacity resolving contradictions that should have been resolved by the human during curation.

## Forces

- **Availability bias:** It is easier to dump everything into the context than to decide what belongs. Curation requires judgment and effort.
- **Fear of omission:** Teams worry that excluding context will cause the agent to miss critical information or hallucinate.
- **Context window size illusion:** Large context windows (200k-1M tokens) create the impression that capacity is not a constraint. But attention quality degrades long before the window fills.
- **Prompt vs. context leverage:** The prompt itself is a rounding error (~200 tokens). The real leverage is in the other 99.98% -- the information environment the agent operates inside.
- **Staleness risk:** Summarized or curated context can become stale if not maintained, creating a different failure mode (misleading rather than diluted context).

## Solution

Treat context engineering as an information design discipline. Curate what enters the context window with the same rigor applied to API design or database schema:

**Include (high-signal, stable):**
- System prompts and agent instructions
- Tool definitions scoped to the current task
- Curated RAG sources from authoritative origins only
- Persistent memory (distilled cross-session knowledge, not raw history)
- Conventions (how the org writes, builds, tests, ships)

**Exclude or defer to retrieval (low-signal, volatile, redundant):**
- Verbose documentation retrievable on demand
- Historical context irrelevant to the current task
- Redundant information already captured in conventions
- Low-confidence or contradictory sources

**Operational discipline:**
- Audit each context source for signal-to-noise ratio before inclusion.
- Move stable conventions into short, high-signal rule files rather than verbose documentation.
- Use retrieval (tool calls, file reads, search) for volatile or task-specific details rather than pre-loading them.
- Periodically review context inventories for drift, staleness, and redundancy.

## Consequences

**Positive:**
- Higher output quality from reduced attention dilution and fewer conflicting signals.
- Lower token costs from smaller context payloads.
- Faster agent responses from less material to process.
- Forces teams to make explicit decisions about what information matters, improving overall system understanding.

**Negative:**
- **Over-pruning risk:** Removing too much context causes hallucinations or missed information. The cure can be worse than the disease if curation is too aggressive.
- **Curation cost:** The upfront effort of curating context is higher than dumping everything in. Teams under time pressure may skip it.
- **Stale summaries:** Summarized conventions that are not updated become misleading context -- a different failure mode than stuffing, but equally damaging.
- **Judgment dependency:** Effective curation requires domain expertise to distinguish signal from noise. Poor judgment produces poor curation.

## Known Uses

- **Post-Feb-2026 prompting framework** -- Documents "we loaded everything and quality got worse" as one of the five most common agent failure modes. Prescribes explicit context curation as the fix.
- **MetaSystem CLAUDE.md and skill files** -- Partially adopted. Skills load variable amounts of context; some are tightly curated, others are verbose. The pattern provides the rubric for systematic audit and improvement.
- **Community CLAUDE.md convergence** -- Practitioners replacing verbose context files with minimal 60-80 line versions after observing quality improvements (corroborated by ETH Zurich empirical data).

## Contract

### Preconditions
- The agent operates within a bounded context window (all current LLMs).
- The available information exceeds what can be loaded without quality degradation.
- Someone with domain expertise is available to make curation decisions.

### Invariants
- Every item in the context window has a justifiable reason for being there. No context is included "just in case."
- Context is curated by a human or explicit policy before injection -- not dumped in bulk.
- Retrieval mechanisms exist for information excluded from the static context, so it remains accessible on demand.

### Governance
- Context inventories are periodically audited for signal-to-noise ratio, staleness, and redundancy.
- Curation criteria are documented and versioned so decisions are traceable and revisable.
- Changes to context composition are tracked (what was added, removed, or summarized, and why).

### Recovery
- If over-pruning causes hallucinations or missed information, restore excluded content from retrieval and re-curate with broader inclusion criteria.
- If summarized conventions become stale, the original verbose source is available for re-summarization.
- If curation criteria prove too aggressive or too permissive, they can be revised without rebuilding the entire context from scratch.
