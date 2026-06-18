---
name: "Context Assembly Cost as Strategy Blocker"
summary: "If every agent run reassembles business context from scratch — querying the same systems, rebuilding the same data picture — token costs scale linearly with run count rather than amortizing across runs. A 3x token cost multiplier can make an otherwise viable agent strategy economically unsustainable. Persistent context layers (cached business context, pre-assembled data views) are not optimization — they are viability requirements."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Strong (production-tested)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "lilly-incident-agent-security-permissions.md"
related_findings:
  - file: "agent-cost-blowup-mitigation-strategies.md"
    rel: "same-problem"
  - file: "prompt-caching-for-stable-agent-context.md"
    rel: "extends"
  - file: "push-vs-pull-context-loading.md"
    rel: "extends"
  - file: "budget-governance-with-hard-stop.md"
    rel: "same-problem"
  - file: "stupid-button-six-question-token-audit-diagnostic.md"
    rel: "same-problem"
  - file: "implementation-is-strategy-for-agentic-systems.md"
    rel: "extends"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "rules/persistent-context-layers-are-viability-requirements.md"
  - building-agentic-systems.md
tags:
  - "session-95-reextract"
---

# Context Assembly Cost as Strategy Blocker

## What It Is

A viability constraint for agentic systems: the cost of assembling business context for each agent run can make an otherwise sound strategy economically non-viable. The video source identifies this as one of the four tests that determine whether an agent strategy will actually work: "If every run reassembles the same business context from scratch and your token bill goes up by 3x, the strategy doesn't work."

**The cost structure:**

For a single agent run (e.g., "prepare the renewal brief for our largest customer"), the agent must:
1. Query the CRM for customer data
2. Pull support ticket history
3. Access contract management for terms
4. Retrieve product usage data
5. Fetch call transcripts
6. Search the internal wiki for relevant context

Each query consumes tokens (for the query itself and for processing the response). If this context assembly is repeated for every run — even when the underlying data hasn't changed — the token cost scales with run frequency, not data change frequency.

**The economics:**
- Human consultant: reads screens once, builds context mentally, no marginal cost per review
- Agent without persistent context: queries all systems, processes all responses, pays full token cost per run
- Agent with persistent context: queries only changed data, processes deltas, pays marginal cost per run

The gap between the second and third models can be the difference between viable and non-viable at enterprise scale.

## Why It Matters

The video source frames this as a strategic constraint, not an optimization opportunity. Pinecone's launch of Nexus is explicitly positioned as solving this: "Stop making your agent rebuild the business from scratch every time it runs." The market is recognizing that context assembly cost is a first-order viability question, not a second-order efficiency question.

For MetaSystem, this pattern already manifests in research-loop runs where the agent reads existing findings, sources, and dimensions before each extraction — context that could be cached or summarized rather than re-read from scratch. The prompt caching finding addresses part of this, but the broader principle is about persistent business context layers that survive across runs.

## Why People Are Using It

The six-vendor convergence in the source: SAP acquired Dreamio to bring a unified data layer to where business data lives. Pinecone launched Nexus for persistent context. These are multi-billion-dollar investments in solving the context assembly problem — evidence that the market considers it a strategy-level constraint.

## Potential Improvements

- Implement a "context freshness" model for MetaSystem research runs: pre-compute and cache stable context (dimension definitions, finding counts, authority lists) and only re-read changed items.
- Apply the token audit diagnostic (existing finding) specifically to context assembly: what percentage of tokens per run go to reading context that hasn't changed since the last run?
- Design a "context layer" for each agent workflow that persists between runs, with explicit invalidation triggers.

## Potential Failure Modes

- **Stale context**: Persistent context layers serve stale data if invalidation triggers are missed. The agent makes decisions based on outdated information.
- **Cache coherence complexity**: Maintaining a valid persistent context across multiple backend systems introduces distributed cache coherence problems — a well-known hard problem in distributed systems.
- **Premature optimization**: For low-frequency agent runs, the engineering cost of building persistent context may exceed the token cost savings. The pattern matters at scale, not for single-digit daily runs.
