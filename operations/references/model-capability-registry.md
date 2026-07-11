---
name: Model Capability Registry
description: Coarse per-model+version capability profiles for agent work — what each model is known to be good/bad at, relative to named anchors. Living reference, refreshed intentionally via /research-loop D2/2.A scans. Every claim carries KB provenance.
last_updated: "2026-07-11 (session 129 — wanted-list profiles added from research-query: Kimi, DeepSeek, Qwen, Llama, Claude 5 family)"
refresh_contract: "Refreshed periodically and intentionally (Nick, session 129 — maintenance cost accepted). Refresh trigger: any /research-loop scan of D2 or 2.A that produces new model-capability findings. Each refresh updates per-entry last_reviewed. An entry whose last_reviewed predates two major release cycles for that provider is stale — treat as unverified."
---

# Model Capability Registry

**What this is.** Coarse, relative capability profiles per model+version — "X is as good as Y at coding but weak at Z" granularity, not benchmark tables. It exists so model-routing decisions and skill↔model-coupling metadata (agentic-OS direction) have one queryable reference instead of re-deriving from findings each time.

**Rules for entries:**

1. **Every claim is KB-grounded** — each entry cites the finding(s) it derives from. No entry is written from general knowledge or memory; if the KB lacks coverage, the model goes in the Unprofiled list instead.
2. **Coarse and relative.** Strengths/weaknesses stated against named anchor models, not raw scores. Raw benchmark data stays in the findings.
3. **Dated.** Every entry carries `as-of` (evidence date) and `last_reviewed`. Benchmarks are snapshots; an undated claim is a wrong claim waiting to happen.

---

## Anthropic / Claude line (as of Jun–Jul 2026; reviewed 2026-07-11)

> The March-2026 consensus entries for Claude (below, kept for history) are **superseded** by the
> Claude 5 / Sonnet 5 re-tiering. Coarse routing now: **Sonnet 5 = default agent workhorse; Opus 4.8
> = hard-reasoning value point; Fable 5 = long-horizon frontier at 2× Opus.**

### Claude Fable 5 / Mythos 5 — Anthropic *(new frontier tier above Opus)*
- **Strong:** frontier coding (SWE-Bench Pro ~11 points over Opus 4.8; #1 FrontierCode); **long-horizon agentic work is the differentiator** — 3× Opus improvement with file-based memory, multi-week engineering jobs compressed to a day (Stripe 50M-line migration); 1M default context / 128k output.
- **Weak:** cost — $10/$50 per M, 2× Opus 4.8, 3–5× Sonnet; practitioners keep it off default paths and reserve it for long-horizon jobs. Mythos 5 = same model, restricted access (not plannable-for). Benchmark set still announcement-adjacent.
- **Grounding:** `claude-5-family-retiers-claude-line`

### Claude Sonnet 5 — Anthropic *(new mid-tier default)*
- **Strong:** near-Opus 4.8 on agentic benchmarks (terminal, computer use, coding) at Sonnet pricing ($3/$15; intro $2/$10 to Aug 31 2026); "most agentic Sonnet yet"; improved agentic safety profile over Sonnet 4.6.
- **Weak:** at max effort can be worse **and** costlier than Opus 4.8 at low/medium effort — effort level is a hidden routing variable; new tokenizer (+1.0–1.35× token counts) breaks naive price comparisons and may perturb prompt-length-sensitive skills (re-validate Sonnet-4.6-era skills — skill↔model coupling).
- **Grounding:** `claude-5-family-retiers-claude-line`

### Claude Opus 4.8 — Anthropic
- **Strong:** best long-multi-step-coding model below the Fable tier; the hard-reasoning value point at $5/$25 when Fable's cost/access isn't justified.
- **Weak:** clearly below Fable 5 on long-horizon and frontier coding (~11 points SWE-Bench Pro).
- **Grounding:** `claude-5-family-retiers-claude-line`

### Claude Sonnet 4.6 / Opus 4.6 — Anthropic *(superseded tier, March 2026 consensus)*
- Sonnet 4.6 was the routing-consensus leader for repo-level coding/knowledge work; Opus 4.6 showed parity at 3.5× cost ("Opus by default is a documented cost mistake" — now re-anchored by the entries above).
- **Grounding:** `task-specific-model-routing-table-march-2026-bench`, `claude-code-max-plan-subsidy-vs-api-cost-tool`

---

## Other frontier closed models (as of March 2026 consensus; reviewed 2026-06-22)

### GPT-5.4 — OpenAI
- **Strong:** computer use, browser automation, orchestration (WebArena-Verified leader at evidence date); terminal-agent work (TerminalBench-2.0 75.1% still tops the mid-2026 comparison rows).
- **Grounding:** `task-specific-model-routing-table-march-2026-bench`, `deepseek-v4-frontier-parity-mit-license`

### Gemini 3.1 Pro — Google
- **Strong:** abstract reasoning and long-horizon math (ARC-AGI-2 leader at evidence date); agentic browsing (BrowseComp leader in mid-2026 comparison rows).
- **Grounding:** `task-specific-model-routing-table-march-2026-bench`, `deepseek-v4-frontier-parity-mit-license`

### Gemini Flash — Google
- **Strong:** extraction/transformation and batch processing at the cost floor.
- **Weak:** not a candidate for complex agentic work.
- **Grounding:** `task-specific-model-routing-table-march-2026-bench`

---

## Open-weight lines (as of mid-2026; reviewed 2026-07-11)

> Coarse routing across the trio: **Kimi** for agentic coding + deep-search swarms at lowest cost;
> **DeepSeek** for reasoning + extreme context; **Qwen** for tool-heavy orchestration + efficiency.
> Shared caveat: none has a clean safety story — external guardrails are mandatory for autonomy.

### Kimi K2.6 / K2.7 Code (1T/32B MoE, Modified MIT) — Moonshot
- **Strong:** ≈ Opus 4.6 / GPT-5.4 at agentic coding (K2.6 led SWE-bench Pro at release; Opus 4.7 re-took the lead); **leads frontier closed models at deep research/browsing** (DeepSearchQA, BrowseComp agent-swarm); 256k context; ~5–10× cheaper than Opus; runs 300 parallel sub-agents on 4×H100 INT4.
- **Weak:** **measured safety gap** — red-teamed as unfit for production without hardened guardrails; highest broken-tool-use / harmful-system-prompt-compliance in its audit cohort; slow (~38 tok/s) and token-hungry; benchmark-vs-real-world split reported (Opus 4.7 "clearly won" one practitioner backend test). K2.7 Code claims −30% reasoning tokens, independent numbers pending.
- **Grounding:** `kimi-k2-line-near-opus-coding-with-safety-gap`

### DeepSeek V4-Pro / R1 distills (MIT) — DeepSeek
- **Strong:** V4-Pro-Max ≈ Opus 4.6-class on agentic coding (within 1–3 points across SWE-bench variants); **best open-weight reasoning** (V3.2-Speciale: IMO/IOI gold, ≈ Gemini 3.0 Pro); **1M-token context** (strong to ~200k measured); ~10–13× under GPT-5.5/Opus 4.7 on API cost; MIT = zero-friction embedding; R1 distills (7–32B) give a true local path.
- **Weak:** tool-calling reliability undocumented (absent from BFCL); terminal-agent work trails GPT-5.4; ARC-AGI-style general reasoning trails GPT-5.5; V4 self-hosting is cluster-scale; no published safety audit.
- **Grounding:** `deepseek-v4-frontier-parity-mit-license`

### Qwen 3.x / Qwen3-Coder-Next (Apache 2.0) — Alibaba
- **Strong:** **#1 at structured tool calling, period** (BFCL-V4 leader; top open-weight; cheapest-within-10% entry at 27B) — the evidence-backed open choice for orchestration-heavy agents; Coder-Next = near-frontier coding (Sonnet 4.5-band SWE-bench) at 3B active parameters — the efficiency outlier for latency/cost-critical coding agents; sizes from 0.6B edge to Max.
- **Weak:** ~10 points below V4-Pro-Max/Opus-class on hardest coding; 32k–128k practical context; top-end reasoning thinly documented; no published safety audit.
- **Grounding:** `qwen-bfcl-tool-calling-leadership-efficient-coding`

### Meta Llama (custom license) — Meta
- **Strong:** ecosystem breadth, tooling familiarity, serviceable general baseline.
- **Weak:** **absent from the top of every agentic leaderboard checked** (SWE-bench, BFCL-V4, TerminalBench); custom license (registration, no-training-competitors) adds legal overhead MIT/Apache alternatives don't have. Not a competitive agent backbone in 2026. (Absence-of-evidence basis — re-check at refresh.)
- **Grounding:** `llama-fallen-behind-open-weight-agentic-lines`

### Mistral Small 4 (22B, Apache 2.0) — Mistral *(open-weight)*
- **Strong:** first open-weight model with frontier-competitive general benchmarks at single-GPU deployable size; default where data cannot leave the machine at small scale.
- **Weak:** agentic-task parity unproven (tool use, multi-turn function calling); quantization may cliff on edge cases. For agent workloads the 2026 open-weight trio above now dominates it on evidence.
- **Grounding:** `open-source-model-parity-mistral-small-4`

---

## Cross-cutting cautions

- All models scored **0% on ARC-AGI-3** at the March-2026 evidence date — a shared capability ceiling reminder (`arc-agi-3-zero-percent-abstract-reasoning`).
- Release compression (`frontier-release-compression-march-2026`) means profiles age fast; trust `as-of` dates over model names. The Kimi↔Opus leapfrogging (K2.6 leads → Opus 4.7 re-leads, weeks apart) is the concrete demonstration.
- **Benchmark parity ≠ task parity.** Practitioner splits (Composio pro-Kimi vs Tensorlake pro-Opus on the same model pair) recur; treat registry profiles as routing priors, not guarantees.

---

## Unprofiled / wanted (no KB coverage yet — queue for next D2/2.A scan)

| Model | Why wanted | Requested |
|---|---|---|
| GLM line (4.7/5.x) | Recurs in mid-2026 comparison rows near the frontier (SWE-bench Pro 58.4, τ²-Bench 99.1) but has no dedicated profile evidence | session 129 research pass |
| GPT-5.5 / 5.6 | Appears as anchor in Claude/Kimi comparisons; no dedicated profile | session 129 research pass |

Adding a profile requires a KB finding first (research-loop or /research-query with persistence) — the registry never front-runs the KB.
