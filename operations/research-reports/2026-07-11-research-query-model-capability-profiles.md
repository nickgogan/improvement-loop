---
type: "research-query-report"
topic: "Model capability profiles — Kimi, DeepSeek, Qwen, Llama, Claude 5 family (registry wanted-list)"
dimensions: ["Model Selection", "Model Selection / 2.A Local and Open-Source Models"]
persist_findings: true
date: "2026-07-11"
---

# Research Query Report — Model Capability Profiles (Registry Wanted-List)

## Question

Profile the coarse agent-task capabilities of the five model lines on the model-capability-registry
wanted list — Kimi (K2 line), DeepSeek, Qwen, Llama, Claude 5 family (Fable 5 / Mythos 5) — to ground
new registry entries. For each: agent-work strengths (coding, tool calling, long-horizon, computer
use), weak axes, relative anchors to named frontier models, open-weight status/licensing.

## Existing KB Coverage

The KB had zero coverage of any of the five lines. Prior Model Selection state of the art was the
March 2026 benchmark consensus (`task-specific-model-routing-table-march-2026-bench`) anchored on
Sonnet 4.6 / GPT-5.4 / Gemini 3.1 / Opus 4.6, plus `open-source-model-parity-mistral-small-4` for
open-weight parity. All five profiles below post-date and partially supersede that consensus.

## Research Findings

### Key Insights

#### Kimi K2 line — near-Opus coding at ~1/10 cost, with a real safety/robustness gap
- **What:** Kimi K2.6 (Apr 2026) matches or beats Claude Opus 4.6 and GPT-5.4 on the most
  production-relevant coding benchmarks (SWE-bench Pro 58.6% vs 53.4%/57.7%; LiveCodeBench v6 89.6%;
  Terminal-Bench 2.0 66.7%), at $0.95/$4.00 per M tokens (~5–10× cheaper). Opus 4.7 re-took the lead
  (64.3% SWE-bench Pro). Weak axes: safety/misalignment (Splx red-team: "unfit for production"
  without hardened prompts; arXiv audit: highest broken-tool-use and harmful-system-prompt-compliance
  scores), slow throughput (~38 tok/s), high reasoning-token usage. Open weights, Modified MIT, 1T/32B
  MoE, 256k context; local run needs ~240GB+ unified memory. K2.7 Code (Jun 2026) claims −30%
  reasoning tokens.
- **Evidence:** Converging: Artificial Analysis, FriendliAI, GMI Cloud benchmark tables; MIT AI Agent
  Index; two adversarial sources (Splx.ai red-team, arXiv safety eval); split practitioner reports
  (Composio pro-Kimi vs Tensorlake pro-Opus).
- **Novelty:** Novel — no KB coverage of Kimi.
- **Sources:** artificialanalysis.ai (K2.5, K2.6 articles), gmicloud.ai, friendli.ai, splx.ai,
  arxiv.org/html/2604.03121v1, tensorlake.ai, composio.dev, aiagentindex.mit.edu

#### DeepSeek V4 — frontier-parity agentic coding + 1M context under MIT license
- **What:** V4-Pro-Max (early 2026) sits within 1–3 points of the best closed models: SWE-bench
  Verified 80.6% (Opus 4.6-Max 80.8%), Pro 55.4%, Multilingual 76.2%, TerminalBench-2.0 67.9% (GPT-5.4
  75.1% leads), BrowseComp 83.4%. 1M-token context (usable to ~200k per RULER testing). MIT license;
  1.6T/49B MoE. API ~$0.28/$1.10 per M tokens (~10–13× under GPT-5.5/Opus 4.7). R1 distills (7–32B)
  are the local-deployment path (32B distill: 50.8% SWE-bench Verified). Weak: ARC-AGI trails GPT-5.5;
  no BFCL tool-calling data; V4 self-hosting needs serious clusters.
- **Evidence:** HuggingFace V4-Pro model card comparison table, DeepSeek V3.2 technical report,
  MindStudio independent review, MLPerf v5.1, swebench.com leaderboard.
- **Novelty:** Novel.
- **Sources:** huggingface.co/deepseek-ai/DeepSeek-V4-Pro, arxiv.org/pdf/2512.02556.pdf,
  mindstudio.ai review, mlcommons.org, swebench.com, sitepoint.com R1 deployment guide

#### Qwen — best open-weight tool calling (BFCL-V4 leader) + extreme-efficiency coding
- **What:** Qwen3.7-Max leads BFCL-V4 outright (0.750; field average 0.611); Qwen3.5-397B-A17B is the
  top open-weight (0.729); Qwen3.5-27B is the cheapest within 10% of the leader ($0.30/M input).
  Qwen3-Coder-Next (Mar 2026): 80B total / 3B active gets 70.6–71.3% SWE-bench Verified across three
  scaffolds — near-frontier coding at two orders of magnitude less active compute. Apache 2.0 across
  the line. Weak: below V4-Pro-Max/Opus on hardest coding; 32k–128k context (no 1M story); less
  documented top-end reasoning.
- **Evidence:** LLM-Stats BFCL-V4 leaderboard, Qwen3-Coder-Next technical report (arXiv), Qwen team
  blog, Spheron deployment guide.
- **Novelty:** Novel.
- **Sources:** llm-stats.com/benchmarks/bfcl-v4, arxiv.org/html/2603.00729v1, qwen.ai blog,
  github.com/QwenLM/Qwen3.6, spheron.network

#### Llama — fallen behind for agentic work
- **What:** Absent from the top of every agentic leaderboard checked (SWE-bench variants, BFCL-V4,
  TerminalBench); custom license (registration, no-training-competitors) vs DeepSeek's MIT and Qwen's
  Apache 2.0. Role has shifted to general-purpose baseline; DeepSeek and Qwen are now the default
  open-weight choices for agent systems.
- **Evidence:** Absence-of-evidence across leaderboards plus explicit statements in DeepSeek/Qwen
  reports; weaker than the other four profiles (Medium).
- **Novelty:** Novel.
- **Sources:** swebench.com, llm-stats.com, DeepSeek V3.2 TR (claims over open-source field)

#### Claude 5 family (Fable 5 / Mythos 5) — new frontier tier; supersedes March-consensus Claude entries
- **What:** Fable 5: SWE-Bench Pro 80.3% vs Opus 4.8's 69.2% and GPT-5.5's 58.6%; #1 on FrontierCode;
  long-horizon standouts (3× Opus improvement in file-memory Slay-the-Spire; Stripe 50M-line
  migration in a day; Hex >90% vs ~80%). 1M default context / 128k output. $10/$50 per M — 2× Opus
  4.8 ($5/$25). Mythos 5 = same model, restricted release. Also: Sonnet 5 (Jun 30, 2026) nearly closes
  the gap to Opus 4.8 (Terminal-Bench 2.1 80.4 vs 82.7; OSWorld 81.2 vs 83.4) at $3/$15 (intro $2/$10)
  — the new mid-tier default. This restructures the Claude line: the March-2026 "Opus by default is a
  cost mistake" guidance re-anchors to "Sonnet 5 default, Opus 4.8 hard-reasoning value point, Fable 5
  top-end at 2× Opus."
- **Evidence:** Anthropic official docs/announcements + independent (Finout benchmarks, Vellum,
  Caylent, CodeRabbit longitudinal, MorphLLM). Caveat: community reports Sonnet 5 at max effort can
  be worse-and-costlier than Opus 4.8 at low/medium effort.
- **Novelty:** Novel; partially supersedes `task-specific-model-routing-table-march-2026-bench`
  (Claude entries only).
- **Sources:** platform.claude.com models overview + Fable/Mythos announcement, anthropic.com Sonnet 5
  news, finout.io, vellum.ai, caylent.com, coderabbit.ai, morphllm.com, aws.amazon.com

### Synthesis

The five profiles form a coherent mid-2026 picture. The open-weight field has genuinely converged on
frontier coding (K2.6 and V4-Pro-Max are within noise of Opus 4.6-class on SWE-bench), but along
**specialized axes**: Kimi = agentic coding + deep search at lowest cost, DeepSeek = reasoning +
extreme context, Qwen = tool calling + efficiency. None has closed the **safety/robustness** gap
(explicitly audited for Kimi; undocumented for the others), and closed models re-opened the top gap
within weeks (Opus 4.7, then the Claude 5 family). For the registry, the coarse rule: open-weight
lines are viable agent backbones where cost/control dominate and guardrails are external; the Claude
line re-tiers to Sonnet 5 (default) / Opus 4.8 (hard reasoning) / Fable 5 (long-horizon frontier).

### Gaps and Limitations

- K2.7 Code and K2.6 lack independent safety audits (K2.5's audit is the latest rigorous one).
- Llama 4 specifics (benchmarks, license text) were not directly retrievable — the "fallen behind"
  conclusion rests on leaderboard absence, which is weaker evidence.
- Fable 5 benchmark set is early (announcement-adjacent); expect revision.
- Sonnet 5's new tokenizer (+1.0–1.35× token counts) complicates naive price comparisons.
- Benchmark-vs-real-world split (Tensorlake vs Composio on Kimi) is a standing caution for all
  benchmark-derived registry claims.

## All Sources Cited

Kimi: [1] moonshot.ai [2] handyai.substack.com/p/model-drop-kimi-k27-code [3] github.com/moonshotai/kimi-k2 [4] github.com/MoonshotAI/Kimi-K2.5 [5] youtube.com/watch?v=M90iB4hpenI [6] composio.dev/content/kimi-k2-vs-claude-4-sonnet-what-you-should-pick-for-agentic-coding [7] x.com/Kimi_Moonshot [8] huggingface.co/moonshotai/Kimi-K2.5 [9] aiagentindex.mit.edu/2025/kimi-ok-computer/ [10] artificialanalysis.ai/models/kimi-k2-6 [11] friendli.ai/blog/kimi-k2-6 [12] tensorlake.ai/blog/claude-opus-4-7-vs-kimi-k2-6-real-world-coding-test [13] splx.ai/blog/kimi-k2-safety-test [14] gmicloud.ai/en/blog/kimi-k2-6-architecture-benchmarks-and-what-it-means-for-production-ai [15] arxiv.org/html/2604.03121v1 [16] artificialanalysis.ai/articles/kimi-k2-5-everything-you-need-to-know [17] artificialanalysis.ai/articles/kimi-k2-6-the-new-leading-open-weights-model [18] arxiv.org/html/2602.02276v1 [19] unsloth.ai/docs/models/tutorials/kimi-k2.5

DeepSeek/Qwen/Llama: [20] api-docs.deepseek.com/updates [21] mlcommons.org/2025/09/deepseek-inference-5-1/ [22] api-docs.deepseek.com/news/news260424 [23] swebench.com [24] artificialanalysis.ai/evaluations/tau2-bench [25] gorilla.cs.berkeley.edu/leaderboard.html [26] sitepoint.com/deepseek-r1-local-deployment-guide-2026/ [27] arxiv.org/html/2603.00729v1 [28] llm-stats.com/benchmarks/bfcl-v4 [29] arxiv.org/pdf/2512.02556.pdf [30] mindstudio.ai/blog/deepseek-v4-open-source-frontier-model-review [31] huggingface.co/deepseek-ai/DeepSeek-R1 [32] huggingface.co/deepseek-ai/DeepSeek-V4-Pro [33] github.com/QwenLM/Qwen3.6 [34] spheron.network/blog/deploy-qwen3-7-max-gpu-cloud/ [35] huggingface.co/collections/Qwen/qwen3 [36] qwen.ai/blog?id=qwen3-coder-next

Claude 5: [37] platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 [38] platform.claude.com/docs/en/about-claude/models/overview [39] anthropic.com/news/claude-sonnet-5 [40] finout.io/blog/claude-fable-5-mythos-5-pricing-benchmarks [41] vellum.ai/blog/claude-sonnet-5-benchmarks-explained [42] caylent.com/blog/claude-sonnet-5-launch-analysis-what-changed-what-matters-and-what-to-validate [43] coderabbit.ai/blog/claude-sonnet-5-review [44] morphllm.com/claude-benchmarks [45] aws.amazon.com/blogs/machine-learning/introducing-claude-sonnet-5-on-aws-anthropics-most-capable-sonnet-model/ [46] mindstudio.ai/blog/claude-fable-5-pricing-access-usage-limits [47] campustechnology.com/articles/2026/07/08/anthropic-launches-lower-cost-claude-sonnet-5.aspx

## Recommended Next Steps

- Persisted: 5 findings + 6 source entries (below).
- Registry entries updated for all five wanted-list lines.
- High-value for full /research-loop extraction later: the K2.5 safety-evaluation paper
  (arxiv.org/html/2604.03121v1 — grounds a Governance-dimension finding on open-model guardrail
  requirements) and the Kimi K2.5 "Visual Agentic Intelligence" paper (arxiv 2602.02276 — agent-swarm
  architecture material for D6/11.A).

## Persisted Artifacts

- Finding: `kimi-k2-line-near-opus-coding-with-safety-gap.md`
- Finding: `deepseek-v4-frontier-parity-mit-license.md`
- Finding: `qwen-bfcl-tool-calling-leadership-efficient-coding.md`
- Finding: `llama-fallen-behind-open-weight-agentic-lines.md`
- Finding: `claude-5-family-retiers-claude-line.md`
- Source: `artificial-analysis-kimi-k2-6-analysis.md`
- Source: `splx-kimi-k2-safety-red-team.md`
- Source: `deepseek-v4-pro-model-card.md`
- Source: `qwen3-coder-next-technical-report.md`
- Source: `llm-stats-bfcl-v4-leaderboard.md`
- Source: `finout-claude-fable-5-mythos-5-benchmarks.md`
