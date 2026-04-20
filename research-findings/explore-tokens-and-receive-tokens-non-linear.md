---
notion_id: 32b1e08b-9b34-81bf-a94e-ddc6f5723daa
name: 'Explore Tokens and Receive Tokens: Non-Linear Reasoning Injection'
summary: A novel architectural experiment injects 'explore tokens' between text slices that activate a secondary copy of the model to reason abstractly, then 'receive tokens' at the end that aggregate the
  exploration's findings back into the main generation. This is an attempt to add JEPA-style abstract reasoning to standard LLM text generation.
implementation_notes: null
category: Prompt Craft
evidence_strength: Weak (theoretical)
adoption_status: Not Yet Started
priority: P3
applicability:
- General
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: cot-fails-without-inductive-generalization.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Explore Tokens and Receive Tokens: Non-Linear Reasoning Injection

## What It Is
The presenter's research: take an input string, slice it into segments, insert 'explore tokens' between each slice. These explore tokens inject changes into a parallel secondary model ('side model') that reasons without the output-generation constraint. At the end of the string, 'receive tokens' aggregate what the exploratory model discovered back into the primary model's reasoning. The two models must learn a common latent language (via 'jetrack') to communicate their representations. The premise is that large language models with read/write scratch pads are Turing-complete (can simulate any computation) — but the challenge is prompting them to use that capability correctly.

## Why It Matters
If successful, this approach would give LLMs access to a less constrained reasoning process (the side model's abstract exploration) while preserving the output format humans need (text from the primary model). It's a potential bridge between LLM usability and JEPA-quality representations.

## Why People Are Using It
This is active research, not a deployed technique. Of marginal direct applicability to practitioners.

## Potential Alternatives
Extended thinking / chain-of-thought with explicit revision steps; multi-agent debate (one model proposes, another critiques); tree-of-thought / Monte Carlo tree search for LLM reasoning.

## Potential Improvements
The presenter acknowledges the primary challenge is getting the two models' latent spaces to communicate in a meaningful common language. Without solving this alignment problem, the architecture cannot function.

## Potential Failure Modes
The two models (primary and side) have fundamentally different optimization pressures — the primary is shaped by output pressure, the side is not. Getting them to develop a meaningful shared representation space is an unsolved research problem.
