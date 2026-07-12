---
name: BMAD V6 Diataxis Documentation Framework
summary: BMAD V6 adopted the Diataxis framework (tutorials, how-to guides, explanations, reference) for its documentation site, making documentation a first-class citizen. Combined with llms-full.txt endpoint
  for agent-consumable docs.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-v6-is-finally-here.md
date_discovered: '2026-04-07'
last_updated: '2026-07-12'
related_findings:
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: docs-split-by-lifespan-not-topic.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---

## What It Is

BMAD V6 restructured its entire documentation using the Diataxis framework, which categorizes documentation into four distinct types: tutorials (learning-oriented), how-to guides (task-oriented), explanations (understanding-oriented), and reference (information-oriented). The documentation site at docs.bmadmethod.org also produces an llms-full.txt endpoint for direct AI agent consumption.

The Diataxis framework was explicitly named and credited in the video as the organizing principle. Documentation was described as a "first class citizen" in V6, contrasting with poor docs in previous versions.

## Why It Matters

Documentation quality directly impacts agent effectiveness -- agents consuming poorly structured docs waste tokens navigating irrelevant content. The four-type taxonomy forces authors to separate concerns: a tutorial does not try to be a reference, and vice versa. This reduces cognitive load for both human readers and AI agents consuming the docs.

## Why People Are Using It

BMAD's community contributors built the documentation site using Diataxis as the organizing principle. The framework is well-established in technical writing (created by Daniele Procida) and has been adopted by projects like Django, NumPy, and Gatsby. BMAD's adoption signals it is crossing over into AI/agent documentation contexts.

## Potential Improvements

Apply the Diataxis taxonomy to MetaSystem's own documentation -- governance docs are explanations/reference, skill docs are how-to guides, and onboarding flows are tutorials. Currently MetaSystem docs are not categorized by type.

## Potential Failure Modes

Over-rigid adherence to the four categories can create artificial splits. Some content naturally spans multiple types (e.g., a tutorial that also serves as a how-to). The framework works best when authors understand the intent behind each category rather than mechanically sorting.
