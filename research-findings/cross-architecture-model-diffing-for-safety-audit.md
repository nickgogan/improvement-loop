---
name: Cross-Architecture Model Diffing for Safety Auditing
summary: Dedicated Feature Crosscoder (DFC) enables cross-architecture model diffing to find behavioral differences between unrelated AI models. Three-section dictionary (shared, model-A-only, model-B-only)
  avoids false matches. Discovered embedded political alignment, copyright refusal mechanisms, and propaganda features across Llama, Qwen, GPT-OSS, and DeepSeek models.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General / Cross-System
adopted_in: []
sources:
- anthropic-ai-diff-tool.md
related_findings:
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: benchmark-signal-mismatch-optimization-gap.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---
# Cross-Architecture Model Diffing for Safety Auditing

## What It Is
Anthropic's Dedicated Feature Crosscoder (DFC) is a technique for finding behavioral differences between AI models with different architectures and training origins — analogous to a "diff" tool in software engineering. Prior model diffing techniques could only compare base vs. fine-tuned versions of the same model (same "language"). DFC handles the harder case of comparing completely unrelated models (different "languages").

DFC uses a three-section dictionary architecture:
1. **Shared dictionary**: Maps common concepts across both models (like translating "sun" to "soleil")
2. **Model A-only section**: Catalogs features unique to the first model
3. **Model B-only section**: Catalogs features unique to the second model

This avoids the false-match problem of standard crosscoders, which force imperfect alignments for unique concepts, missing genuinely novel features.

**Validation via steering**: Candidate features are tested by artificially suppressing or amplifying them during inference and observing output changes. For example, suppressing a censorship feature reduces censorship; amplifying it increases it — confirming causal behavioral control.

## Why It Matters
Traditional AI safety evaluations rely on human-authored benchmarks, which are reactive and miss "unknown unknowns" — emergent behaviors not anticipated by test designers. DFC provides a proactive screening tool: rather than guessing what to test for, it surfaces what is actually different between models. This is particularly important for:
- Auditing models from different organizations/countries for embedded biases or political alignment
- Monitoring model updates for unintended behavioral changes (e.g., sycophancy emergence)
- Regulatory compliance — providing systematic evidence of what a model does differently from competitors

## Why People Are Using It
Anthropic research (by Thomas Jiralerspong and Trenton Bricken). Key discoveries across four open-source models:

| Comparison | Exclusive Feature | Description |
|---|---|---|
| Llama-3.1-8B (Meta, US) vs. Qwen3-8B (Alibaba, China) | American Exceptionalism (Llama) | Controls assertions of US superiority; absent in Qwen |
| Qwen3-8B and DeepSeek-R1-0528-Qwen3-8B | CCP Alignment | Controls pro-government censorship and propaganda; absent in US models |
| GPT-OSS-20B (OpenAI) | Copyright Refusal Mechanism | Controls refusals to provide copyrighted material; absent in compared model |

Reproducibility: CCP Alignment rediscovered in 5/5 runs; American Exceptionalism in 4/5 runs.

## Potential Improvements
DFC currently flags thousands of candidate features requiring manual validation — it is a screening tool, not a complete solution. Automation of the validation step (beyond steering) would make it practical for continuous monitoring. Application to frontier models (the paper uses 8B-20B parameter models) and version-to-version diffs of the same model (detecting drift like the GPT-4o sycophancy incident) are natural next steps.

## Potential Failure Modes
DFC requires access to model internals (activations), making it inapplicable to closed-API models without cooperation from the provider. The technique surfaces structural differences but cannot determine whether those differences are deliberate training choices, emergent from data, or artifacts. The thousands of candidate features per diff create a needle-in-haystack problem that still requires expert human review. False positives from the shared dictionary forcing alignments where concepts are similar but not identical.
