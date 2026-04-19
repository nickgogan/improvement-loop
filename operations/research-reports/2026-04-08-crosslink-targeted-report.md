---
title: "Targeted Crosslink Pass + Legacy Migration Report"
date: 2026-04-08
type: maintenance
scope: crosslink-quality
---

# Targeted Crosslink Pass + Legacy Migration Report — 2026-04-08

## Overview

Two objectives executed in parallel:
1. **Targeted crosslink pass** on Orchestration, Tool Integration, and cross-category isolates
2. **Legacy link type migration** — converting 149 untyped (flat string) `related_findings` entries to typed `{file, rel}` format

## Baseline (Start of Session)

| Metric | Value |
|--------|-------|
| Grade | A (95/100) |
| Total findings | 323 |
| Total crosslinks | 1,048 |
| Isolated findings | 77 (23.8%) |
| Untyped entries | 149 |
| Asymmetric links | 0 |
| Broken references | 0 |

## Objective 1: Targeted Crosslink Pass

### Pass 1 — Orchestration (150 pairs evaluated)
- **Pairs evaluated:** 150 (40 both-isolated, 94 within-category, 16 cross-category)
- **Agents dispatched:** 6 (25 pairs each)
- **Links proposed:** 6
- **Links approved:** 6 (0 rejected)
- **Type distribution:** 2 same-problem, 2 enables, 2 contradicts
- **Hit rate:** 4.0% (very strict — agents correctly rejected most Orchestration pairs where findings address different sub-problems)

Notable links:
- `aios-architecture` **contradicts** `specialization-theater` (role-based org vs. anti-role-based-org)
- `agent-architecture-layer-impermanence` **contradicts** `skills-as-markdown-sop-files` (impermanence thesis vs. encode-forever thesis)
- `bmad-dependency-graph` **enables** `bmad-help-adaptive-routing` (metadata enables routing)
- `bmad-method-v6` **enables** `correct-course` (framework enables its command)

**Result:** Orchestration isolation 32.5% → 18.2% (-14.3pp)

### Pass 2 — Tool Integration (150 pairs evaluated)
- **Pairs evaluated:** 150 (138 both-isolated, 12 cross-category)
- **Agents dispatched:** 6 (25 pairs each)
- **Links proposed:** 5
- **Links approved:** 4 (1 rejected: gws-cli ↔ stripe-cli — "different CLI tools for different domains" anti-pattern)
- **Type distribution:** 3 same-problem, 1 enables
- **Hit rate:** 3.3% (expected — many Tool Integration findings are domain-specific)

Notable links:
- `cli-anything-meta-tool` **same-problem** `dynamic-discovery-architecture` (both address meta-tooling/CLI generation)
- `claude-code-channels` **same-problem** `happy-engineering-mobile` (both address mobile Claude Code access)
- `dynamic-discovery` **enables** `gws-cli` (pattern enables its implementation)
- `cursor-claude-code-ide` **same-problem** `gpt-54-tool-search` (both address tool count/context budget)

**Result:** Tool Integration isolation 47.6% → 26.2% (-21.4pp)

### Pass 3 — Cross-Category Scatter (17 pairs evaluated)
- **Pairs evaluated:** 17 (manually curated cross-category pairs)
- **Agents dispatched:** 1
- **Links proposed:** 6
- **Links approved:** 6
- **Type distribution:** 3 same-problem, 2 extends, 1 enables

Notable links:
- `trajectory-engineering` **same-problem** `fork-subagent-parallel-trajectory` (cross: Context Eng → Orchestration)
- `llm-intuition-unreliability` **same-problem** `agent-self-reporting-unreliability` (within: Evaluation)
- `ralph-wiggum-execution` **extends** `ralph-loop-brute-force` (cross: Orchestration → Evaluation)
- `agent-cost-blowup` **extends** `model-tier-routing` (within: Orchestration)
- `fundamental-limits-embedding` **enables** `ace-rag-based-playbook` (cross: Context Eng → Memory Arch)
- `stacking-paul-carl` **same-problem** `multi-client-context-isolation` (within: Context Eng)

**Result:** Context Eng 17.0% → 9.4%, Evaluation 13.3% → 8.9%

### Crosslink Pass Summary

| Metric | Value |
|--------|-------|
| Total pairs evaluated | 317 |
| Total links proposed | 17 |
| Total links approved | 16 + 1 fixed = 17 |
| Total links rejected | 1 |
| Hit rate | 5.4% |
| Type distribution | 8 same-problem, 4 enables, 2 contradicts, 2 extends, 1 same-problem(?) |

## Objective 2: Legacy Link Type Migration

### Approach
1. Identified 149 untyped entries across 61 files
2. Found 43 duplicate entries (untyped entry coexisting with typed entry for same target) — removed directly
3. Remaining 106 entries collapsed to 102 unique pairs
4. Dispatched 4 classification subagents (30/30/30/12 pairs each)
5. Applied migration with YAML-safe writer script

### Classification Results

| Type | Count | % |
|------|-------|---|
| same-problem | 57 | 55.9% |
| enables | 34 | 33.3% |
| extends | 9 | 8.8% |
| contradicts | 2 | 2.0% |

### Migration Stats

| Metric | Value |
|--------|-------|
| Untyped entries (start) | 149 |
| Duplicates removed | 43 |
| Pairs classified | 102 |
| Entries migrated | 102 |
| Untyped entries (end) | **0** |
| Files modified | ~90 |

## Post-Write Validation

### YAML Integrity
- 324 finding files validated with `yaml.safe_load`
- 0 parse errors
- 0 orphaned lines
- 0 malformed entries

### Crosslink Integrity
- 0 asymmetric links
- 0 broken references

### Content Validation (Stratified Sample)
- All 2 contradicts links verified correct
- All 4 enables links (from crosslink pass) verified correct
- All 2 extends links verified correct
- Migration enables (34 total) — sampled during quality review; enables rate (33%) higher than KB average (5%), flagged for future spot-check

## Final State

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Grade | A (95/100) | A (95/100) | — |
| Total crosslinks | 1,048 | 1,087 | +39 |
| Isolated findings | 77 (23.8%) | 50 (15.5%) | **-27 (-8.3pp)** |
| Untyped entries | 149 | 0 | **-149 (100%)** |
| same-problem | 627 | 728 | +101 |
| enables | 91 | 118 | +27 |
| enabled-by | 77 | 111 | +34 |
| extends | 52 | 62 | +10 |
| extended-by | 25 | 34 | +9 |
| contradicts | 27 | 34 | +7 |

### Category Isolation Improvement

| Category | Before | After | Change |
|----------|--------|-------|--------|
| Orchestration | 32.5% | 18.2% | **-14.3pp** |
| Tool Integration | 47.6% | 26.2% | **-21.4pp** |
| Context Engineering | 17.0% | 9.4% | **-7.6pp** |
| Evaluation | 13.3% | 8.9% | **-4.4pp** |
| Prompt Craft | 15.4% | 11.5% | -3.9pp |
| Model Selection | 50.0% | 50.0% | — |
| Sandboxing | 33.3% | 33.3% | — |

### Remaining Gaps
- **Model Selection (50%)**: 4 isolated of 8. These are highly specific (benchmark results, routing tables) with limited cross-category connections.
- **Sandboxing (33.3%)**: 2 isolated of 6. Small category.
- **Tool Integration (26.2%)**: Down from 47.6% but still above average. Remaining isolates are domain-specific CLI tools (FFmpeg, Playwright, Stripe, Supabase) that genuinely don't link to other findings.
- **Intent Engineering (21.4%)**: 3 isolated — niche findings that may benefit from future cross-category passes.

## Process Notes

- 17 subagents dispatched in parallel (12 crosslink evaluation + 4 migration classification + 1 cross-category)
- YAML-safe writer script used for all writes (Python yaml.safe_load/dump, no regex)
- Post-write validation confirmed 0 parse errors across all 324 files
- Anti-patterns working well: Tool Integration hit rate was 3.3% (agents correctly rejected "both are CLI tools" false positives)
- Migration enables rate (33%) is notably higher than the KB's historical 5% — worth spot-checking in a future session
