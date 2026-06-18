---
name: Provider-Adaptive Prompt Rendering for Model-Specific Context Formatting
summary: System-level prompt formatting adapts per model provider — line-numbered blocks for Anthropic models (which respond better to numbered references), standard formatting for others. Architectural response to the model-specificity problem — one memory substrate, multiple rendering strategies.
implementation_notes: null
category: Prompt Craft
evidence_strength: "Medium (practitioner-documented)"
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
related_findings:
- file: model-specific-context-file-sensitivity.md
  rel: extends
pipeline_status: raw
---

# Provider-Adaptive Prompt Rendering for Model-Specific Context Formatting

## What It Is

A prompt architecture where the underlying memory substrate remains provider-agnostic, but the rendering layer that converts memory blocks into system prompt text adapts per model provider. Specifically: Anthropic models receive line-numbered memory blocks (because Claude responds better to numbered line references), while other providers receive standard formatting. Summarizer model selection also varies by provider (Haiku 4.5 for Anthropic, GPT-5-mini for OpenAI, Gemini 2.5 Flash for Google). This acknowledges that optimal context formatting is model-specific while keeping the data layer universal.

## Why It Matters

The assumption that one prompt format works equally well across all models is empirically false. Models have different attention patterns, different sensitivity to formatting cues, and different strengths in referencing structured content. A rendering adapter layer lets systems optimize for each model's strengths without duplicating or forking the underlying memory architecture.

## Why People Are Using It

Observed in [Letta](https://github.com/letta-ai/letta) v0.16.8 — see [[letta-analysis]] for structural details. The pattern manifests as explicit provider branching in the prompt generation pipeline, with Anthropic-specific code paths that inject line numbers and warning text about line number usage rules. This is a production-validated response to observed behavioral differences across model families.

## Potential Alternatives

Single universal format optimized for the lowest common denominator (simpler but suboptimal for all). Per-model fine-tuning to normalize format sensitivity (expensive and not always available). A/B testing framework that discovers optimal formatting per model empirically (data-driven but requires traffic volume).

## Potential Improvements

Automated format discovery through eval-driven optimization rather than manual observation. A rendering plugin system that allows new provider-specific formatters to be added without modifying core code. Versioned format profiles that track which formatting works best for which model version, since model updates can change format sensitivity.

## Potential Failure Modes

Format assumptions become stale as models are updated (e.g., a future Claude version might not benefit from line numbers). Maintaining multiple rendering paths increases testing surface area. Provider detection logic can misroute if model identifiers change or new models are added. Over-optimization for one provider's quirks creates brittleness if that provider's API changes.
