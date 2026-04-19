---
name: Brevity Constraints Reverse LLM Performance Hierarchies
summary: Research paper shows that forcing LLMs to produce brief responses improves accuracy by 26 percentage points and can cause smaller models to outperform larger ones. Larger models suffer from spontaneous
  scale-dependent verbosity — RLHF training rewards thoroughness, which introduces error accumulation through over-elaboration.
implementation_notes: Add conciseness constraints to system prompts. Even a simple 'be concise, no filler' line in CLAUDE.md may improve output quality, not just save tokens.
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- caveman-brevity-constraints-llm-performance.md
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: contradicts
- file: negative-constraints-as-probabilistic-output-collapse.md
  rel: same-problem
- file: star-commands-for-explicit-output-format-override.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: "synthesized"
consumed_by:
  - "model-resilient-prompt-engineering.md"
---

## What It Is
A research paper ("Brevity Constraints Reverse Performance Hierarchies in Language Models," March 2026) evaluated 31 models across 1,500 problems and found that on ~8% of problems, larger LLMs underperformed smaller ones by 28 percentage points despite having 100x more parameters. The mechanism is "spontaneous scale-dependent verbosity" — larger models, trained via RLHF to be thorough, over-elaborate their responses, talking themselves into wrong answers. Constraining output brevity improved accuracy by 26 percentage points and reduced performance gaps by up to 2/3. The Caveman Claude skill operationalizes this by forcing Claude Code to produce terse output, saving ~4-5% of total session tokens (not the 75% claimed in the repo — that figure applies only to prose responses, which are a small fraction of total output).

## Why It Matters
If verbosity degrades reasoning quality, then the default behavior of frontier models (producing long, thorough explanations) may actively hurt correctness on certain problem types. This has direct implications for system prompt design and output format specifications.

## Why People Are Using It
The Caveman repo gained 5,000 GitHub stars in 72 hours. Practitioners are attracted by the dual benefit: token savings (real but modest at ~4-5% of total session) and potential quality improvements. The research backing gives it credibility beyond a meme.

## Potential Alternatives
- Adding `"Be concise. No filler."` to CLAUDE.md (simpler, no skill needed)
- Output format constraints (JSON, structured schemas) that naturally limit verbosity
- Model-specific tuning of `max_tokens` parameter

## Potential Improvements
- Testing whether frontier models (Opus, GPT-5.4) exhibit the same verbosity-accuracy tradeoff as the open-weight models in the study
- Identifying which problem types benefit most from brevity constraints
- Dynamic brevity — verbose for planning, terse for execution

## Potential Failure Modes
- Over-compression could strip necessary reasoning steps for complex multi-step problems
- Brevity constraints may conflict with chain-of-thought reasoning, which benefits from elaboration
- The study used open-weight models; the effect size on frontier models is unknown
