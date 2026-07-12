---
name: 'DRI Rotation Pattern: Time-Bounded Sensemaking Ownership'
summary: Directly Responsible Individuals (DRIs) own a specific cross-cutting problem for a fixed term (e.g., 90 days) with full authority to pull resources, interpret data, and make direction calls within
  that domain. The expiration date prevents accumulation of middle management; rotation across domains builds cross-functional fluency. Block's proposed replacement for permanent middle management.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- unbundling-management-ai-age-routing-sensemaking.md
related_findings:
- file: management-unbundling-routing-sensemaking-accountability.md
  rel: same-problem
- file: ceo-mandatory-delegation-pattern.md
  rel: same-problem
- file: autonomy-gradient-not-binary-delegation.md
  rel: same-problem
- file: five-persistent-human-skills-agent-era-framework.md
  rel: same-problem
- file: agent-owner-card-human-facing-registry.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
---

## What It Is

A structural pattern from Jack Dorsey's proposed Block reorganization (2026). In a flat org where AI handles information routing, someone still needs to own sensemaking for each domain. The DRI pattern assigns this ownership explicitly:

**Core mechanics:**
- One person (the DRI) owns a specific cross-cutting problem (e.g., "merchant churn," "payment reliability") for a bounded period (Block's default: ~90 days).
- The DRI has **full authority** to pull resources from multiple teams to solve the problem — they are not just an executor but an interpreter and decision-maker for that problem space.
- The DRI determines what the data means, sets priority within the domain, and makes direction calls.
- At term end, ownership rotates. The time boundary explicitly prevents the DRI from becoming a permanent middle manager accumulating territory.
- Rotation across domains builds cross-functional fluency over time — a valuable side effect.

**Contrast with Kimi:** Sensemaking is concentrated in 5 co-founders each managing 50 direct reports. High cognitive load, not scalable, not transferable. DRI rotation distributes this load and skill.

**Contrast with traditional PM/EM:** Traditional ownership is indefinite, territory-building, and tied to headcount. DRI ownership is bounded, problem-focused, and authority-defined rather than headcount-defined.

**Player-coach complement:** Block pairs DRIs (who own sensemaking) with player-coaches (IC practitioners who also develop people and handle accountability/feedback). The player-coach role is explicitly stripped of routing and alignment responsibilities so it can focus on craft and care.

**Block's "world model":** AI handles routing by producing a persistent, machine-readable shared representation of the company's entire state that anyone can query. This is the precondition for DRI + player-coach to work — without AI-managed routing, the cognitive load would overwhelm both roles.

## Why It Matters

Most flat-org experiments fail because they remove management without explicitly reassigning the sensemaking and accountability functions. DRI rotation is a concrete mechanism for reassigning sensemaking at the level of the person closest to the problem, without recreating the permanent hierarchy that slows throughput.

For MetaSystem: The IL system has an implicit DRI problem — research findings accumulate without explicit ownership per domain. A DRI-style "topic steward" (e.g., owning Governance findings for one quarter) could reduce drift and improve synthesis quality.

For Claude Build: Spec authors already function as informal DRIs — a named person owns a Build Spec for its lifetime. Making this explicit (with authority, term, and rotation) could reduce the bottleneck created by all architectural sensemaking defaulting to Nick.

## Why People Are Using It

Block published the framework publicly (Jack Dorsey and Rolof Botha, 2026). The pattern is not yet in live production at Block — it is a proposed reorganization following a major headcount reduction. The analyst observing it notes this as the "sharpest structural innovation" in Block's model, specifically because it assigns sensemaking to the person closest to the problem rather than concentrating it at the top.

## Potential Improvements

- Term length (90 days vs. longer) is an open question. Shorter terms prevent territory accumulation but may be insufficient for deep context to develop in complex domains.
- An explicit handoff protocol between outgoing and incoming DRIs would prevent context loss at rotation.
- DRI authority over resource allocation (pull from multiple teams) requires organizational trust and clear conflict resolution when multiple DRIs compete for the same resource.
- Could be applied to agent systems: a named human "domain DRI" per agentic pipeline (e.g., owns the research extraction pipeline for one quarter), with explicit authority to rewrite prompts, change thresholds, or retire findings.

## Potential Failure Modes

- 90 days may be too short for domains requiring deep accumulated context (regulatory compliance, multi-year product strategy).
- Term rotation creates transition risk: domains may regress during handoff periods.
- Without strong organizational support, DRIs may lack real authority to pull resources and become accountability without power.
- The "no permanent middle manager" constraint may be bypassed by repeated DRI assignments to the same domain.
- Depends on the AI world model functioning correctly — if routing breaks, DRI cognitive load increases and the model collapses.
