---
title: "Session 101 Delta Report — LINKS.md Repo Intake"
type: "delta-report"
session: 101
date: "2026-05-25"
agent: "researcher"
---

# Session 101 Delta Report — LINKS.md Repo Intake

## Summary

Processed 6 GitHub repos from LINKS.md into the watched-libraries registry, ran structural analysis on all 6, and promoted 17 findings into the KB. Also processed 2 standalone URLs (arXiv paper + Oracle blog).

## Inputs Processed

### LINKS.md Repos (6)

| Repo | Spectrum | Version | Findings Promoted |
|------|----------|---------|-------------------|
| google/adk-python | cherry-pick | v2.0.0 | 1 |
| crewaiinc/crewai | cherry-pick | v1.14.6 | 0 (10 candidates, all duplicate or partial) |
| letta-ai/letta | cherry-pick | v0.16.8 | 7 |
| langflow-ai/langflow | monitor | v1.9.3 | 5 |
| significant-gravitas/autogpt | cherry-pick | v0.5.0 | 4 |
| microsoft/autogen | monitor | v0.7.5 | 1 |

### Standalone URLs (2)

| URL | Action |
|-----|--------|
| arxiv.org/abs/2504.19413 (Mem0 paper) | Source created + existing finding evidence upgraded (Medium → Strong) |
| blogs.oracle.com — Agent Memory Amnesia | Source created + 1 new finding (converged-memory-substrate) |

## Artifacts Created

| Type | Count | Details |
|------|-------|---------|
| Watched-library entries | 6 | langflow, adk-python, autogpt, autogen, crewai, letta |
| Analysis docs | 6 | One per repo, all 5 dimensions + research dimension mapping |
| Research sources | 2 | arxiv-2504-19413, oracle-agent-memory-amnesia-blog |
| Research findings (new) | 22 | 17 from individual analyses + 1 from Oracle blog + 4 from cross-repo comparison |
| Research findings (updated) | 3 | triple-storage-memory-architecture (evidence → Strong), declarative-tool-rule-engine (cross-repo corroboration), sleeptime-background-memory-agent (cross-repo corroboration) |
| Cross-repo comparison | 1 | Regenerated with 29 repos (up from 15), 7 new cross-repo findings identified |

## Findings Promoted (18 new)

### Context Engineering (7)
1. `event-to-llm-context-orchestration.md` — ADK-Python
2. `git-backed-memory-versioning.md` — Letta
3. `memory-block-labeled-semantic-container.md` — Letta
4. `multi-modal-summarization-strategy-taxonomy.md` — Letta
5. `per-section-context-window-budget-tracking.md` — Letta
6. `sleeptime-background-memory-agent.md` — Letta
7. `converged-memory-substrate-vs-patchwork.md` — Oracle blog

### Prompt Craft (1)
8. `provider-adaptive-prompt-rendering.md` — Letta

### Governance (5)
9. `battle-scar-anti-pattern-documentation.md` — Langflow
10. `component-as-contract-immutability.md` — Langflow
11. `expand-contract-database-migration-pattern.md` — Langflow
12. `thread-resolution-integrity-rule.md` — AutoGPT
13. `convergence-loop-dual-clean-poll-exit.md` — AutoGPT

### Orchestration (3)
14. `ledger-based-orchestration-stall-detection.md` — AutoGen
15. `fleet-orchestration-tmux-state-file.md` — AutoGPT
16. `agent-self-recovery-from-context-compaction.md` — AutoGPT

### Tool Integration (2)
17. `declarative-tool-rule-engine-dual-enforcement.md` — Letta
18. `policy-guarded-tool-execution.md` — Langflow

## Dedup Statistics

- 52 total candidates evaluated across 6 analyses
- 16 genuinely new (promoted)
- 14 partial matches (not promoted — incremental detail, not distinct patterns)
- 22 duplicates (already in KB)
- Dedup rate: 69% (36/52 overlapped with existing KB)

## KB Totals (Post-Session)

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Research findings | ~717 | 739 | +22 |
| Research sources | ~177 | 179 | +2 |
| Watched libraries | 25 | 31 | +6 |
| Analysis docs | 24 | 30 | +6 |
| Cross-repo comparison | 15 repos | 29 repos | +14 repos covered |

## Cross-Repo Comparison Findings (4 promoted)

19. `graph-execution-engine-convergence-six-repos.md` — 6 repos converge on graph execution, diverge on semantics
20. `event-bus-observability-three-approaches.md` — bus vs event-sourcing vs hooks taxonomy
21. `a2a-protocol-adoption-landscape-fragmented.md` — 3 protocols across 4 repos, standardization incomplete
22. `skill-anatomy-convergence-20-of-29-repos.md` — SKILL.md is de facto standard (69% adoption), remaining innovation in 4 areas

## Notes

- Repo cache is 1.9GB at `watched-libraries/_tmp/repo-cache/`. Gitignored. Consider `/cleanup-cache --purge` if disk space is a concern.
- AutoGen is in maintenance mode (community-managed). Successor: microsoft/agent-framework. Worth adding when it matures.
- Letta yielded the most findings (7/17) — memory-centric architecture is highly relevant to IL's Dimension 1 research.
- CrewAI yielded 0 net-new findings despite 10 candidates — high overlap with existing KB patterns from earlier intake rounds.
- Cross-repo comparison now covers 29 repos with 30 total cross-repo findings (CR-1 through CR-30).
- Analysis doc candidates still need `→` promotion annotations per /promote-findings Step 6 (deferred — mechanical edit, no decision value).
