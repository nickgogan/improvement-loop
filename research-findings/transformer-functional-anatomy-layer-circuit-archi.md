---
notion_id: "32c1e08b-9b34-81d3-b75e-cfb686b9a481"
name: "Transformer Functional Anatomy -- Layer Circuit Architecture"
summary: "LLMs have genuine functional anatomy: early layers encode, middle layers reason in indivisible multi-layer circuits, late layers decode. Duplicating entire circuits improves performance without weight changes. Single-layer duplication fails because circuits must execute as complete units."
implementation_notes: "Mostly theoretical for us. But explains why longer thinking time works (more forward passes through reasoning circuits), why model size matters non-linearly, and why truncating reasoning is destructive."
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
proposals: []
date_discovered: "2026-03-23"
last_updated: "2026-03-23"
pipeline_status: "raw"
consumed_by: []
---

# Transformer Functional Anatomy -- Layer Circuit Architecture

## What It Is
A discovery that LLM transformer stacks are organized into functional regions analogous to brain anatomy. Through systematic layer duplication experiments, the study found that: (1) early layers act as encoders, (2) late layers act as decoders, (3) middle layers form indivisible multi-layer circuits. Duplicating a single middle layer hurts performance; duplicating an entire circuit improves it.

## Why It Matters
This changes how we think about model capabilities. The "reasoning cortex" isn't a uniform processing layer -- it's a collection of specialized circuits.

## Why People Are Using It
The RYS-XLarge model topped the HuggingFace Open LLM Leaderboard by duplicating just 7 middle layers of Qwen2-72B. All discovered on consumer hardware (2x RTX 4090).

## Potential Improvements
Fine-tuning junction layers could smooth the disjuncture. Automated circuit discovery tools could map any architecture.

## Potential Failure Modes
Bad circuit selection causes incoherent models. Circuit boundaries are model-specific. The method adds inference latency without adding new knowledge.
