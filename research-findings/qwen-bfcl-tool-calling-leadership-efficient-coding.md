---
name: "Qwen — BFCL-V4 Tool-Calling Leadership and Extreme-Efficiency Coding Agents"
summary: |-
  Qwen owns the tool-calling axis among open-weight lines as of mid-2026: Qwen3.7-Max leads the
  Berkeley Function Calling Leaderboard V4 outright at 0.750 (field average 0.611), Qwen3.5-397B-A17B
  is the top-ranked open-weight entry (0.729), and Qwen3.5-27B is the cheapest model within 10% of
  the leader (~$0.30/M input). On coding, Qwen3-Coder-Next (Mar 2026) is the efficiency outlier: 80B
  total but only 3B active parameters, scoring 70.6-71.3% on SWE-bench Verified across three
  different agent scaffolds (SWE-Agent, MiniSWE-Agent, OpenHands) — the same band as Sonnet 4.5-High
  and Kimi K2.5 with two orders of magnitude less active compute. Apache 2.0 across the whole
  open-weight line. Weak axes: below DeepSeek V4-Pro-Max and Opus-class on the hardest coding
  benchmarks; 32k-128k practical context (no extreme-context story); top-end reasoning less
  documented than DeepSeek's.
implementation_notes: |-
  Registry profile granularity: "Qwen ≈ best open-weight for structured tool calling (BFCL-V4 #1),
  near-frontier coding at tiny active compute (Coder-Next), Apache 2.0 — but not the choice for
  hardest-tier coding, extreme context, or olympiad reasoning." Routing rule that falls out of the
  open-weight trio: DeepSeek for reasoning/long-context, Qwen for tool-heavy orchestration and
  latency/cost-critical coding agents, Kimi for agentic-coding + deep-search swarms. Qwen3.6's
  thinking-preservation (retains reasoning context across turns) targets multi-turn coding sessions.
  Deployment: small Qwen3.x run on consumer hardware; Qwen3.7-Max FP8 is 500-700GB needing 4x
  H200-class clusters.
category: Model Selection
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: null
applicability:
- General
adopted_in: []
sources:
- llm-stats-bfcl-v4-leaderboard.md
- qwen3-coder-next-technical-report.md
related_findings:
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: extends
- file: kimi-k2-line-near-opus-coding-with-safety-gap.md
  rel: same-problem
- file: deepseek-v4-frontier-parity-mit-license.md
  rel: same-problem
- file: llama-fallen-behind-open-weight-agentic-lines.md
  rel: same-problem
proposals: []
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
pipeline_status: raw
consumed_by: []
---
# Qwen — BFCL-V4 Tool-Calling Leadership and Extreme-Efficiency Coding Agents

## What It Is

Alibaba's Qwen open-weight family (Apache 2.0), mid-2026 state:

- **BFCL-V4 (function/tool calling):** Qwen3.7-Max #1 at 0.750; Qwen3.7-Plus and Qwen3.5-397B-A17B
  tied #2 at 0.729 (the latter is the top open-weight); Qwen3.5-27B at 0.685 is the cheapest within
  10% of the leader. Field average: 0.611. Neither DeepSeek nor Llama appears on the leaderboard.
- **Qwen3-Coder-Next** (Mar 2026): hybrid-attention MoE, 80B total / 3B active; 70.6–71.3% SWE-bench
  Verified consistently across three scaffolds; competitive TerminalBench-2.0 relative to its
  active-compute footprint.
- **Qwen3.6:** agentic-coding upgrades + "thinking preservation" across conversation turns.
- Sizes span 0.6B (edge/CPU) to Qwen3.7-Max (multi-H200 clusters).

## Why It Matters

Tool calling is the one agent-critical axis where an open-weight line doesn't just approach but
*leads* the measured field. For agents that are mostly orchestration — RAG pipelines, multi-API
workflows, structured tool sequences — Qwen is the evidence-backed open choice, and the 27B model
makes that capability cheap.

## Why People Are Using It

BFCL-V4 leadership for tool-heavy systems; Coder-Next's cost/latency profile for production coding
agents (3B active = fast, cheap inference); Apache 2.0 (no Llama-style restrictions); consistent
scores across agent scaffolds suggesting robustness to harness choice.

## Potential Failure Modes

- Not the top-tier coding model: ~10 points below DeepSeek V4-Pro-Max / Opus 4.6-class on SWE-bench
  Verified; don't route hardest-tier engineering here.
- Context ceiling (32k–128k practical) rules out extreme long-horizon single-context sessions.
- Top-end reasoning benchmarks thin relative to DeepSeek's documentation.
- No published independent safety audit (shared open-weight caveat — external guardrails for
  autonomy).
