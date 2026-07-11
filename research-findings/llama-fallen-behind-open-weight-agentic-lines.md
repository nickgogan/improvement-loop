---
name: "Meta Llama Has Fallen Behind DeepSeek/Qwen/Kimi for Agentic Work"
summary: |-
  As of mid-2026, Meta's Llama line is absent from the top of every major agentic leaderboard —
  SWE-bench variants, BFCL-V4 (tool calling), TerminalBench-2.0 — while DeepSeek (V4), Qwen (3.x),
  and Kimi (K2.6) occupy the open-weight frontier positions. Combined with Llama's custom license
  (registration requirement, no-training-competing-models clause) versus DeepSeek's MIT and Qwen's
  Apache 2.0, Llama has shifted from default open-weight choice to general-purpose baseline. Teams
  building agent systems on open weights now default to DeepSeek (reasoning/long-context), Qwen
  (tool calling/efficiency), or Kimi (agentic coding/deep search).
implementation_notes: |-
  Registry profile granularity: "Llama = general-purpose baseline with broad ecosystem support; not
  a competitive agent backbone in 2026; license adds legal overhead the alternatives don't have."
  Evidence caveat: this is partly absence-of-evidence (Llama missing from leaderboards rather than
  measured-and-losing), and Llama 4-specific benchmark data was not directly retrievable — hence
  Medium strength. Revisit if a Llama release re-enters the agentic leaderboards.
category: Model Selection
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: null
applicability:
- General
adopted_in: []
sources:
- llm-stats-bfcl-v4-leaderboard.md
- deepseek-v4-pro-model-card.md
related_findings:
- file: qwen-bfcl-tool-calling-leadership-efficient-coding.md
  rel: same-problem
- file: deepseek-v4-frontier-parity-mit-license.md
  rel: same-problem
- file: kimi-k2-line-near-opus-coding-with-safety-gap.md
  rel: same-problem
- file: open-source-model-parity-mistral-small-4.md
  rel: extends
proposals: []
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
pipeline_status: raw
consumed_by: []
---
# Meta Llama Has Fallen Behind DeepSeek/Qwen/Kimi for Agentic Work

## What It Is

A negative-space finding about the open-weight landscape: the line that defined open-weight LLMs in
2023–2024 no longer appears at the top of the benchmarks that define agent capability in 2026.
DeepSeek V3.2's technical report explicitly claims outperformance of the open-source field (which
included Llama-class models) on SWE-bench Verified and TerminalBench-2.0; BFCL-V4's 13 evaluated
models include four Qwen entries and zero Llama entries; swebench.com leaderboard tops are
DeepSeek/Kimi/closed-frontier territory.

## Why It Matters

Model-selection guidance that still treats "Llama" as the synonym for open-weight deployment is
stale. License terms compound the capability gap: MIT (DeepSeek) and Apache 2.0 (Qwen, Mistral)
permit unrestricted commercial embedding and fine-tuning; Llama's custom license requires
registration and prohibits training competing models — extra legal review for less capability.

## Why People Are Using It (still)

Ecosystem familiarity, extensive tooling integrations, solid general language performance. As a
non-agentic general baseline it remains serviceable.

## Potential Failure Modes

- Absence-of-evidence basis: Llama may simply be under-benchmarked on these leaderboards rather than
  uncompetitive; Llama-4-line specifics were not retrievable in this pass.
- Meta's resources make a leapfrog release possible at any time; this finding has a short shelf life
  and should be re-checked at the registry's refresh cadence.
