---
name: "DeepSeek V4 — Frontier-Parity Agentic Coding and 1M Context Under MIT License"
summary: |-
  DeepSeek V4-Pro-Max (early 2026, MIT license, 1.6T/49B MoE) sits within 1-3 points of the best
  closed models on agentic coding: SWE-bench Verified 80.6% (Opus 4.6-Max: 80.8%), Pro 55.4%,
  Multilingual 76.2%, TerminalBench-2.0 67.9% (GPT-5.4-xHigh leads at 75.1%), BrowseComp 83.4%.
  1M-token context via hybrid sparse attention (independent RULER testing confirms strength to
  ~200k), at 27% of V3.2's FLOPs and 10% of its KV cache at 1M. API cost ~$0.28/$1.10 per M tokens —
  10-13x under GPT-5.5/Opus 4.7. The line spans local-friendly R1 distills (32B distill: 50.8%
  SWE-bench Verified, runs on one high-end consumer GPU quantized) up to V4-Pro. V3.2-Speciale took
  gold-medal results at IMO/IOI/ICPC 2025. Weak axes: ARC-AGI trails GPT-5.5; no BFCL tool-calling
  benchmark presence; V4 self-hosting needs serious multi-GPU clusters.
implementation_notes: |-
  Registry profile granularity: "V4-Pro-Max ≈ Opus 4.6-class at agentic coding and reasoning, leads
  open-weight field at long context (1M) and math/olympiad reasoning, ~1/10 API cost — but
  tool-calling reliability is undocumented (no BFCL) and terminal-agent work trails GPT-5.4."
  Deployment ladder: R1 distills 7B/14B/32B via Ollama/vLLM (Q4_K_M, ~4-20GB files) for local; V4
  via API (OpenAI- and Anthropic-compatible endpoints) or heavy self-host. MIT license = zero legal
  friction for fine-tuning/embedding in proprietary stacks — the regulated-industry angle from the
  Mistral Small 4 finding now extends to a frontier-parity model.
category: Model Selection
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: null
applicability:
- General
adopted_in: []
sources:
- deepseek-v4-pro-model-card.md
related_findings:
- file: open-source-model-parity-mistral-small-4.md
  rel: extends
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: extends
- file: kimi-k2-line-near-opus-coding-with-safety-gap.md
  rel: same-problem
- file: qwen-bfcl-tool-calling-leadership-efficient-coding.md
  rel: same-problem
proposals: []
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
pipeline_status: raw
consumed_by: []
---
# DeepSeek V4 — Frontier-Parity Agentic Coding and 1M Context Under MIT License

## What It Is

DeepSeek's open-weight line as of mid-2026, all MIT-licensed:

- **R1 series** (Jan 2025): RL-trained reasoning flagship + dense distills (7B–32B) that run locally;
  R1-Distill-Qwen-32B hits 50.8% SWE-bench Verified.
- **V3.2 / V3.2-Speciale** (Dec 2025): DeepSeek Sparse Attention; ~70% SWE-bench Verified (same band
  as GPT-5.2-Codex 72.8%, Sonnet 4.5-High 71.4%); Speciale variant matched Gemini 3.0 Pro on
  reasoning with gold medals at IMO/IOI/ICPC/CMO 2025.
- **V4-Pro / V4-Flash** (early 2026): 1.6T/49B and 284B/13B MoE, hybrid CSA+HCA attention, 1M-token
  default context. V4-Pro-Max benchmark row: SWE-bench Verified 80.6, Pro 55.4, Multilingual 76.2,
  TerminalBench-2.0 67.9, BrowseComp 83.4, MMLU-Pro 87.5, HMMT Feb-2026 95.2 — each within 1-3 points
  of the Opus 4.6-Max / GPT-5.4-xHigh / Gemini 3.1-Pro-High row.

## Why It Matters

This is the strongest open-weight option when reasoning quality and extreme context dominate —
math-heavy work, very large codebases, long agent sessions. MIT licensing plus a deployment ladder
from consumer GPU (R1 distills) to API-frontier (V4-Pro) makes it the most practically adoptable
frontier-class open line.

## Why People Are Using It

Frontier-parity benchmarks at ~1/10 cost; 1M context as default; MIT license for unrestricted
commercial embedding; OpenAI/Anthropic-compatible APIs; integrations shipped with Claude Code,
OpenClaw, OpenCode.

## Potential Failure Modes

- Tool-calling reliability is inferred (good TerminalBench/BrowseComp), not benchmarked — DeepSeek is
  absent from BFCL-V4; Qwen is the evidence-backed choice for heavy structured tool orchestration.
- Long-context quality degrades past ~200k despite the 1M window.
- ARC-AGI-style general reasoning trails GPT-5.5.
- No published independent safety audit (same caveat class as Kimi — assume external guardrails
  required for autonomy).
- V4-Pro self-hosting is enterprise-cluster territory; the "local" story is R1 distills at a much
  lower capability tier.
