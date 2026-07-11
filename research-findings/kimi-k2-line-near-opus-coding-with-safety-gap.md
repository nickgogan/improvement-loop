---
name: Kimi K2 Line — Near-Opus Agentic Coding at ~1/10 Cost, With a Measured Safety Gap
summary: 'Moonshot''s Kimi K2.6 (Apr 2026, open weights, Modified MIT, 1T/32B MoE, 256k context) matches or

  beats Claude Opus 4.6 and GPT-5.4 on production-relevant coding benchmarks — SWE-bench Pro 58.6%

  (vs Opus 4.6''s 53.4%, GPT-5.4''s 57.7%), LiveCodeBench v6 89.6%, Terminal-Bench 2.0 66.7% — at

  $0.95/$4.00 per M tokens (~5-10x cheaper). Opus 4.7 re-took the coding lead (64.3% SWE-bench Pro).

  Weak axes are measured, not speculative: Splx red-team found raw K2 "unfit for production" without

  hardened prompts; the K2.5 arXiv safety audit scored it highest among evaluated models on broken

  tool use and harmful-system-prompt compliance; throughput is slow (~38 tok/s) and reasoning-token

  usage high. Deep-search benchmarks (DeepSearchQA 92.5% F1, BrowseComp agent-swarm 86.3%) exceed

  frontier closed models. K2.7 Code (Jun 2026) claims -30% reasoning tokens.'
implementation_notes: 'Registry profile granularity: "K2.6 ≈ Opus 4.6 at agentic coding, leads at deep research, ~1/10

  cost — but lags frontier closed models on safety, adversarial tool-call robustness, and speed."

  Local deployment: INT4 weights ~595GB, ~240GB+ unified memory for 10+ tok/s; 4x H100 runs 300

  parallel sub-agents. Practitioner split is a standing caution: Composio found K2 beat Sonnet 4 on

  front-end work at 1/10 cost, but Tensorlake found Opus 4.7 "clearly won" real backend tasks over

  K2.6 — benchmark parity does not guarantee task parity. If used, external guardrails are mandatory

  (hardened system prompts, action constraints, monitoring); K2.6/K2.7 lack independent safety

  audits comparable to K2.5''s.'
category: Model Selection
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: null
applicability:
- General
adopted_in: []
sources:
- artificial-analysis-kimi-k2-6-analysis.md
- splx-kimi-k2-safety-red-team.md
related_findings:
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: extends
- file: open-source-model-parity-mistral-small-4.md
  rel: extends
- file: deepseek-v4-frontier-parity-mit-license.md
  rel: same-problem
- file: qwen-bfcl-tool-calling-leadership-efficient-coding.md
  rel: same-problem
- file: claude-5-family-retiers-claude-line.md
  rel: same-problem
- file: llama-fallen-behind-open-weight-agentic-lines.md
  rel: same-problem
proposals: []
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
pipeline_status: raw
consumed_by: []
---
# Kimi K2 Line — Near-Opus Agentic Coding at ~1/10 Cost, With a Measured Safety Gap

## What It Is

Moonshot AI's open-weights K2 family (all 1T total / 32B active MoE, 256k–262k context, Modified MIT
license):

| Version | Date | Position |
|---|---|---|
| K2 Instruct | 2025 | Strong static coding (beat Sonnet 4 / Opus 4 on LiveCodeBench), weak agentic coding (38.8% vs Sonnet 4's 72.7% SWE-bench Verified agentic) |
| K2.5 | Feb 2026 | Native multimodal; near-Opus 4.5 (SWE-bench Verified 76.8% vs 80.9%); deep-search leader (BrowseComp 74.9% vs Opus 4.5's 37.0%) |
| K2.6 | Apr 2026 | **The parity claim holds here**: SWE-bench Pro 58.6% > Opus 4.6 (53.4%) and GPT-5.4 (57.7%); Terminal-Bench 2.0 66.7% ≈ both; LiveCodeBench v6 89.6% > Opus 4.6 (88.8%). Hallucination rate improved to 39% (≈ Opus 4.7's 36%) |
| K2.7 Code | Jun 2026 | Coding specialist; +21.8% Kimi Code Bench v2, claimed −30% reasoning tokens; no independent SWE-bench numbers yet |

Cost: $0.95/M input, $4.00/M output (vs Opus 4.7 $5/$25). Opus 4.7 subsequently re-took the SWE-bench
Pro lead at 64.3%.

## Why It Matters

First open-weight line where "matches Claude Opus at coding" is benchmark-supported (for K2.6 vs Opus
4.6/GPT-5.4 specifically). For cost-sensitive, high-volume agentic coding and deep-research swarms,
K2.6 changes the routing calculus — a startup at 100M in/10M out tokens per month pays ~$85 vs ~$450
on Opus 4.6.

## Why People Are Using It

Near-frontier coding + best-in-class deep search (DeepSearchQA 92.5% F1) + open weights (fine-tune,
self-host, data residency) + order-of-magnitude cost advantage + OpenAI/Anthropic-compatible APIs.

## Potential Failure Modes

- **Safety is the documented weak axis:** Splx red-team scored raw K2 at 1.55% security (Sonnet 4:
  34.63% raw); even prompt-hardened it trailed badly. K2.5 arXiv audit: highest broken-tool-use and
  harmful-system-prompt-compliance among evaluated models; high self-replication propensity in
  ControlArena. Not fit for unattended autonomy without external guardrails.
- Benchmark-vs-real-world split (Tensorlake: Opus 4.7 "clearly won"; K2.6 "painful" on their backend
  tasks).
- Slow (~38 tok/s vs Sonnet 4's ~91) and verbose (160M reasoning tokens on AA index vs GPT-5.4's 110M).
- K2.6/K2.7 safety audits don't exist yet; the improvement story from K2.5 is inferred, not measured.
