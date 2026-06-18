---
name: "Context-First Build Sequencing for Agentic Systems"
summary: "When building an agentic system, invest in context infrastructure (business knowledge, voice profiles, domain documents) before building agent capabilities (skills, workflows, orchestration). 'Start with the business brain, not the agents.' Every agent feature is multiplied by the quality of the underlying context — and none work well without it. This is a build-ordering principle, not a capability description."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Already Adopted"
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "agentic-os-five-pillars-claude-code.md"
related_findings:
  - file: five-pillar-agentic-os-framework.md
    rel: enables
  - file: context-infrastructure-seven-level-maturity-model.md
    rel: extends
  - file: context-before-loop-initialization-sequence.md
    rel: same-problem
  - file: context-gap-task-vs-job.md
    rel: enables
  - file: skills-as-pointers-to-second-brain-files.md
    rel: enables
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "rules/fix-data-schema-before-automating.md"
  - building-agentic-systems.md
tags:
  - "session-95-reextract"
---
# Context-First Build Sequencing for Agentic Systems

## What It Is

A build-ordering principle for agentic systems: invest in context infrastructure before agent capabilities. The practitioner's specific sequencing recommendation:

1. **First:** Build the "business brain" — shared context folder containing brand voice, ICP documentation, positioning, client details, domain knowledge.
2. **Second:** Build skills that reference the business brain, not skills that embed their own context.
3. **Third:** Build interaction layers (UI, channels, dashboards).
4. **Fourth:** Build scheduled workflows that chain context-aware skills.
5. **Last:** Build multi-agent orchestration.

The practitioner explicitly warns against the common mistake: "Don't start with the agents. Don't start with the multi-agent orchestration. I made this same mistake." The key insight is multiplicative: every feature built on top of solid context infrastructure produces higher-quality outputs than the same feature built without it.

This is distinct from the five-pillar framework (which describes capabilities) — this is a sequencing constraint on how to build those capabilities.

## Why It Matters

Most agentic system builders start with the exciting parts (multi-agent orchestration, autonomous workflows, supervisor UIs) and bolt on context later. This leads to generic outputs that require constant manual correction. The context-first approach front-loads the investment that has the highest marginal return: once the business brain exists, every subsequent skill automatically produces contextually relevant outputs.

For MetaSystem, this validates the constitution-first approach: governance documents, vocabulary, principles, and system boundaries were established before agent skills were built. The IL research KB functions as the "business brain" for the improvement loop.

## Why People Are Using It

The practitioner rebuilt their system after three months of "getting this wrong" — initially building agents and orchestration first, then discovering that outputs were generic and required heavy manual intervention. Moving business context to the foundation layer and rebuilding skills to reference it eliminated most quality issues.

## Potential Improvements

The principle needs a concrete "readiness checklist" for the context layer: what minimum context must exist before building skills? The transcript implies brand voice + ICP + positioning + client details, but this varies by domain. A domain-agnostic minimum viable context checklist would make this actionable across use cases.

## Potential Failure Modes

Context-first can become analysis paralysis if the builder tries to document everything before building anything. The principle should include an MVP threshold: enough context to produce one good skill output, then iterate. Over-investing in context documentation before any skill exists means no feedback on whether the context is actually useful.
