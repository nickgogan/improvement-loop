---
name: Persuasion-Engineered Skill Design
summary: Superpowers explicitly applies 7 persuasion principles from Meincke et al. (2025, N=28,000) to skill design — authority, commitment, scarcity, social proof, reciprocity, liking, unity — documenting
  33%→72% compliance improvement. Shows the most research-backed approach to making agents follow rules across all analyzed repos.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---
# Persuasion-Engineered Skill Design

## What It Is
Superpowers explicitly applies seven persuasion principles from Meincke et al. (2025, N=28,000) to the design of every skill: authority, commitment, scarcity, social proof, reciprocity, liking, and unity. This is documented in `writing-skills/persuasion-principles.md` within the repo. Concrete applications include: "94% PR rejection rate" as social proof to motivate thorough reviews, "human partner" language for liking/unity, and Iron Laws for authority/commitment framing. The documented result is a compliance improvement from 33% to 72%.

## Why It Matters
Most agent frameworks tell agents what to do via imperative instructions. Superpowers asks a different question: how do you make agents WANT to follow rules? The answer draws from academic persuasion research applied to LLM behavior. This is a fundamentally different approach to governance — psychological rather than structural — and the documented compliance improvement suggests it works.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. Every discipline-enforcing skill in the framework applies these principles. The approach is systematic, not ad hoc — there is a documented methodology for skill authors to follow when writing new skills. Other analyzed repos (GSD, BMAD, OpenClaw, Paperclip, gstack, mem0) rely on structural enforcement (gates, allowlists, validation) rather than persuasion engineering.

## Potential Alternatives
Structural enforcement via tool allowlists and phase gates (GSD's approach). Validation-based enforcement where outputs are checked against schemas (BMAD). Constitutional AI-style constraint embedding. Simple imperative rules with no persuasion framing. Fine-tuning models for specific compliance behaviors.

## Potential Improvements
A/B testing different persuasion framings to measure which principles have the strongest effect on specific models. Model-specific persuasion tuning — different models may respond differently to authority vs. social proof. Combining persuasion engineering with structural enforcement for defense-in-depth compliance.

## Potential Failure Modes
Model updates may change susceptibility to specific persuasion techniques, requiring recalibration. Over-reliance on persuasion without structural enforcement creates a single-layer defense — if the model ignores the framing, there is no backup. The compliance numbers (33%→72%) are self-reported by the framework author and may not generalize across different task types or models.
