---
notion_id: 32b1e08b-9b34-8148-960f-e9599bf235aa
name: Surface-Pattern Guardrails vs. Risk-Taxonomy Guardrails
summary: Guardrails that fire on surface language patterns (keywords, emotional tone) rather than the actual underlying risk taxonomy produce inverted safety outcomes — activating on low-risk emotional
  language while missing high-risk concrete threats.
implementation_notes: null
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- General
adopted_in: null
sources:
- chatgpt-health-identified-respiratory-failure-then.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Surface-Pattern Guardrails vs. Risk-Taxonomy Guardrails

## What It Is
Mount Sinai found that ChatGPT Health's crisis intervention system activated much more reliably for vague emotional distress language than for concrete, specific self-harm threats — the inverse of clinical risk. The guardrails were pattern-matching on surface language (emotional tone, keywords) rather than clinical risk taxonomy. This appears across agent domains: a DLP agent flags emails labeled 'confidential financial data' (even if they contain only public earnings) but misses an export of 50,000 customer records described as 'backup of project files.' An agent that tests as 'safe' may be testing for the appearance of safety (surface language patterns) rather than actual safety (correct risk classification). This distinction is one of the hardest eval problems to diagnose because the system will have seemingly valid justifications for its (wrong) safety assessments.

## Why It Matters
Guardrails designed for appearance-of-safety create false confidence that harm is being prevented when it is not. In high-stakes domains, this is more dangerous than having no guardrails at all.

## Why People Are Using It
Surface-pattern guardrails are easy to implement and easy to demonstrate. The actual risk taxonomy is domain-specific knowledge that requires expert input to encode.

## Potential Alternatives
Rule-based risk taxonomies (deterministic, auditable). Domain-expert-designed scenario libraries for guardrail evaluation. Two-layer approach: surface pattern as trigger, risk taxonomy evaluation as gate.

## Potential Improvements
Guardrail certification processes that require demonstration of detection for the actual worst-case scenarios, not just keyword-pattern tests. Expert-curated risk taxonomy libraries per domain.

## Potential Failure Modes
Risk taxonomies are complex and domain-specific — implementing them correctly requires deep domain expertise. Taxonomy-based guardrails may be over-broad if the taxonomy is not well-calibrated.
