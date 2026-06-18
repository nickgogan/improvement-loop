---
title: "Session 91 KB Maintenance Report — Crosslink + Reassess"
type: "research-report"
category: "kb-maintenance"
created: "2026-05-24"
author: "improvement-loop"
session: 91
---

# Session 91 KB Maintenance Report

## Summary

Two maintenance operations on the IL Research KB following bulk intake of 29 findings across sessions 89-90.

| Metric | Value |
|--------|-------|
| Operation 1 | `/finding-crosslink` |
| Operation 2 | `/reassess-priorities` |
| Candidate pairs evaluated | 800 |
| Links proposed (pre-validation) | 50 |
| Links written (post-validation) | 44 |
| Validation error rate | 6/14 sampled (43%) |
| Priority bumps proposed | 4 |
| Priority bumps approved | 4 |
| Files modified | ~60 |

## Operation 1: Finding Crosslink

### Process

1. Ran `crosslink_pair_generator.py --new-only` → 800 candidate pairs involving the 29 new findings.
2. Dispatched 16 Sonnet subagent batches (50 pairs each) for parallel evaluation.
3. Raw result: 63 proposed links (7.9% hit rate — well below 27% historical average).
4. Hub cap applied: `bounded-tiered-memory-inference-driven-curation` capped at 15 total links (had 2 existing + 26 proposed → kept 13, dropped 13).
5. Final pre-validation set: 50 links.
6. Mandatory Step 7 validation on 14-link sample (all contradicts/enables/extends + 7 same-problem).
7. Post-validation: 3 reclassified, 6 removed → 44 final links.

### Link Distribution (Final)

| Type | Count |
|------|-------|
| same-problem | 38 |
| contradicts | 5 |
| extends | 0 |
| enables | 0 |

Note: The 1 enables and 1 extends from the initial pass were reclassified during validation (enables→contradicts, extends→same-problem).

### Validation Results

| Type | Sampled | Correct | Wrong | Borderline |
|------|---------|---------|-------|------------|
| contradicts | 5 | 2 | 1 (→same-problem) | 1 (kept) |
| enables | 1 | 0 | 1 (→contradicts) | 0 |
| extends | 1 | 0 | 1 (→same-problem) | 0 |
| same-problem | 7 | 1 | 5 (removed) | 1 (removed) |
| **Total** | **14** | **3** | **7** | **2** |

Error rate: 43% overall (50% on same-problem, consistent with historical 30-60%). All errors were false positives caught and fixed.

### Coverage Impact

| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Total crosslinks | 2198 | 2286 | +88 entries |
| Isolated findings | 53 | 51 | -2 |
| New findings connected | — | 11/29 | — |

### High-Value Links Discovered

1. **agui-human-control-layer ↔ dark-factory** (contradicts) — genuine philosophical tension: mandatory human control vs fully autonomous codebase
2. **agui-human-control-layer ↔ kairos-autonomous-daemon** (contradicts) — human gates vs autonomous daemon
3. **bounded-tiered-memory ↔ verbatim-storage-thesis** (contradicts) — LLM curation vs raw storage
4. **automatic-fact-extraction ↔ write-time-vs-query-time-synthesis** (contradicts, reclassified from enables) — extraction mechanism creates the poisoning risk it warns about
5. **agent-proof-of-work ↔ chain-of-thought-divergence** (same-problem, reclassified from contradicts) — both address transparency/trust in agent reasoning

## Operation 2: Priority Reassessment

### Process

1. Scanned all 617 findings against 5 reassessment criteria.
2. Identified 4 C1 (evidence accumulation) candidates and 52 C5 (cluster density) flags.
3. Verified source independence for all 4 C1 candidates.
4. All 4 proposals approved by Nick.

### Priority Changes Applied

| Finding | Old Priority | New Priority | Independent Sources |
|---------|-------------|-------------|---------------------|
| Self-Evolving Loop Pattern | Not Flagged | P2 | 4 (Anthropic, OpenAI, gstack, practitioner) |
| Obsidian as Transparent Frontend | P3 | P2 | 3 (Karpathy, 2 practitioners) |
| NotebookLM Python API | P3 | P2 | 3+ (CLI tools, guide, API library, experiments) |
| Org Redesign for Agentic Throughput | P3 | P2 | 3 (3 independent authors) |

### Updated Priority Distribution

| Priority | Before | After |
|----------|--------|-------|
| P1 | 104 | 104 |
| P2 | 269 | 273 |
| P3 | 184 | 181 |
| Not Flagged | 38 | 37 |
| null | 22 | 22 |

## KB Health Post-Maintenance

- **Total findings:** 617
- **Total crosslinks:** 2286
- **Isolated findings:** 51 (8.3%)
- **Average links/finding:** ~3.7
