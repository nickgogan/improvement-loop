---
name: Oneshot Infrastructure Setup Prompt Pattern
summary: 'A single comprehensive prompt given to Claude Code that handles entire infrastructure setup: installing tools, updating storage paths, updating models from outdated defaults, and fixing known
  bugs. Treats Claude Code as an infrastructure automation agent — one prompt bootstraps a complete working system.'
implementation_notes: Distinct from interactive setup because it front-loads all decisions and known fixes.
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-code-plus-rag-anything.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
---
# Oneshot Infrastructure Setup Prompt Pattern

## What It Is
A prompt engineering pattern where a single, comprehensive prompt is given to Claude Code that contains all information needed to bootstrap a complete working system from scratch. The prompt includes: which tools to install, what storage paths to configure, which default model values to override (because defaults are often outdated), and which known bugs to fix preemptively. Rather than an interactive back-and-forth setup conversation, all decisions are front-loaded into one prompt that Claude Code executes end to end.

## Why It Matters
Interactive setup conversations are fragile — each back-and-forth step can introduce errors, and the conversation context accumulates noise that degrades later steps. A oneshot prompt eliminates this by compressing all setup decisions into a single, reviewable, repeatable artifact. It also serves as living documentation of the complete system configuration, making it reproducible across machines or after a clean reinstall.

## Why People Are Using It
Chase AI demonstrates using a single prompt to set up the entire RAG-Anything + LightRAG + MinerU stack, including installing dependencies, configuring Docker storage paths, updating the default embedding model from an outdated value, and patching a known bug in the codebase. The prompt is reusable and shareable as a setup recipe.

## Potential Improvements
The pattern would benefit from a validation step at the end that verifies each component was installed and configured correctly, rather than assuming success. Parameterizing the prompt (e.g., with environment-specific variables for paths and model names) would make it portable across different machines. Version-pinning dependencies in the prompt would prevent drift when the prompt is reused weeks or months later.

## Potential Failure Modes
A single monolithic prompt can fail partway through, leaving the system in a partially configured state that is harder to debug than a clean failure. If any assumption in the prompt is wrong (e.g., a bug fix that was already patched upstream), the prompt may introduce regressions. The pattern encourages "set and forget" — practitioners may not notice when upstream changes invalidate parts of their setup prompt.
