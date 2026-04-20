---
notion_id: 32b1e08b-9b34-81cb-aedb-d52678b37132
name: Metaprompting / Karpathy Autoresearch for Build Specs
summary: 'Using an LLM to generate, test, and iteratively improve the prompts that other LLMs execute. Applied to Build Spec generation: a meta-prompt produces specs, tests them against evaluation criteria,
  and iterates autonomously — the Karpathy autoresearch loop.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P2
applicability:
- Perplexity Skills
adopted_in:
- Perplexity Skills
sources:
- karpathy-autoresearch-video.md
proposals: []
date_discovered: '2026-03-15'
last_updated: '2026-04-19'
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Metaprompting / Karpathy Autoresearch for Build Specs

## What It Is
Metaprompting is the practice of using an LLM to write and refine the prompts that other LLMs consume. The Karpathy autoresearch pattern extends this by closing the loop autonomously: a meta-prompt generates a candidate prompt, that prompt is executed and tested against evals, results are fed back to the meta-prompt, and the cycle repeats until acceptance criteria are met. The existing prompt-enhancer skill is a manual version of this pattern.

## Why It Matters
Hand-crafted prompts plateau quickly — human intuition about what works is limited and slow to iterate. Metaprompting shifts prompt optimization from a one-time authoring task to a continuous, testable engineering process, enabling Build Spec quality to compound over time.

## Why People Are Using It
Andrej Karpathy's autoresearch framing gave the pattern a widely-cited name, and production teams have applied it to systematic prompt improvement with measurable gains. The prompt-enhancer skill in the Perplexity Skills system represents a manual implementation that validates the core approach.

## Potential Improvements
Chaining a prompt-evaluator agent ahead of prompt-enhancer in an automated loop — with explicit, machine-checkable acceptance criteria — would make the pattern fully autonomous. This is the Phase 2.5 target in the current migration plan.

## Potential Failure Modes
Meta-prompts can optimize for proxy metrics rather than true quality — producing prompts that score well on evals but fail in production. Without carefully designed acceptance criteria that resist gaming, the loop converges on metric-satisfying outputs rather than genuinely useful ones.
