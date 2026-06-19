---
title: "Deep Research Prompt — Research-to-Implementation Handoff Design"
id: "architect-handoff-deep-research-prompt"
type: "loop-report"
category: "research-prompt"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-10"
updated: "2026-04-10"
author: "claude"
tags:
  - "loop-report"
  - "deep-research"
  - "perplexity"
  - "architect-handoff"
  - "artifact-design"
aliases:
  - "Architect handoff research prompt"
---

# Deep Research Prompt — Research-to-Implementation Handoff Design

**Purpose:** Prompt for Perplexity Pro Deep Research mode. Investigates prior art for the proposer→architect artifact contract that the Improvement Loop pipeline currently lacks. Output of the Perplexity run should be saved alongside this file as `2026-04-10-architect-handoff-deep-research-results.md`.

**Origin:** Session 2026-04-10, artifact design conversation. The handoff opens with three candidate shapes for "where judgment about the form of the codified output lives" (form-agnostic proposer / form-deciding proposer / collaborative). External prior art is needed before committing to a shape.

---

## The Prompt

## Context
I'm designing the artifact contract between two roles in a knowledge-management pipeline for AI agent systems:
- A **Researcher/Proposer** that extracts patterns from external sources (papers, blog posts, repos, talks) into a structured knowledge base (~440 findings), then generates improvement proposals.
- A **per-system Architect** that consumes those proposals and produces system-specific implementation specs, which are then codified into reusable artifacts (patterns, guides, templates, skills, rules, agent personas).

The proposer stage exists. The architect role does not yet — I'm designing it now. The central question is the **artifact format between proposer and architect.**

## The Core Question
Where should judgment about the *form* of the codified output live?

1. **Form-agnostic proposer** — Proposer describes the problem and evidence; architect decides whether the answer is a pattern, skill, template, rule, agent, etc.
2. **Form-deciding proposer** — Proposer selects the form up front; architect executes within that choice.
3. **Collaborative / confidence-weighted** — Proposer proposes a form with a confidence level; architect can override with a written justification trail.

Each shape implies a different contract (light-then-heavy, heavy-then-light, or balanced-with-override-trail). I need prior art to inform the decision.

## What I Already Know (please do NOT rehash)
- Architectural Decision Records (ADRs) and RFC processes (IETF, Python PEPs, Rust RFCs).
- Dual-track Discovery/Delivery (Marty Cagan, Jeff Patton).
- Threat intel → detection engineering in general terms (STIX/TAXII).
- DIKW pyramid and classical knowledge management.
- Pattern language tradition (Alexander, GoF, PLoP).

I want **specialized or novel prior art** beyond these classics.

## Research Questions

1. **Prior art for research-to-codification pipelines.** Who has published systematic approaches to turning external research into reusable internal artifacts? Prioritize: AI/ML ops teams, platform engineering, developer-experience/DevRel, security detection engineering, pharmaceutical evidence synthesis, Cochrane-style evidence-to-guideline pipelines, and corporate R&D→product transfer frameworks.

2. **Artifact contracts between research and implementation roles.** What specific formats, schemas, or templates have been published or open-sourced for handing findings to implementers? Dig into: Sigma rules, YARA-L, OSCAL, SPIFFE/SPIRE trust bundles, ML experiment cards, model cards, datasheets for datasets, GRADE evidence profiles, Cochrane summary-of-findings tables.

3. **Who decides the form.** In frameworks where one role researches and another implements, who typically decides the *shape* of the output (pattern vs procedure vs constraint vs template)? Is there a named pattern for where this decision boundary sits? Any empirical comparisons of the tradeoffs?

4. **Multi-target handoffs.** When one research finding applies to multiple downstream systems with different constraints, how do mature organizations structure the handoff — fan out proposals per target, or produce one abstract spec that each target adapts? Examples with sources.

5. **Human gates at research/implementation boundaries.** What review rituals, decision logs, or approval artifacts sit at the boundary between "we learned X" and "we'll build Y"? I want rituals, not just tools.

6. **Conflict surfacing.** How do mature pipelines expose contradictions between research findings so downstream implementers see the tension rather than an averaged-out recommendation? Look for: disagreement encoding in systematic reviews, dissent mechanisms in standards bodies, "minority report" patterns.

7. **Known failure modes at this handoff.** What goes wrong in practice? Examples: researcher-implementer impedance mismatch, scope creep at codification, loss of evidentiary provenance, template-fitting bias, "too abstract to implement" vs "too specific to reuse."

## Desired Output

- A **comparative table** of at least 5 distinct prior-art approaches, columns: name, domain, researcher role, implementer role, artifact format, who decides form, conflict-handling mechanism, human-gate pattern, URL to specification.
- **Named patterns** with their canonical vocabulary — I want terms I can reuse.
- **Direct URLs** to specifications, templates, or case studies. Not vendor blog summaries. Prefer primary sources: standards documents, academic papers, open-source repositories, published frameworks.
- **A failure-modes section** with at least 4 documented cases and sources.
- **Explicit gaps** — questions the literature does not answer well. This is as valuable as the answers.

Prioritize depth on 3–5 strong examples over shallow coverage of 15. Cite everything with direct URLs.

---

## Usage Notes

- Paste the section above (from "## Context" through "Cite everything with direct URLs.") into Perplexity Pro → Deep Research.
- Expect a 30–60s run.
- If the result comes back shallow on any axis, retry with: *"Expand on items 2 and 6 with 3 more sources each."*
- Save the output as a sibling file named `2026-04-10-architect-handoff-deep-research-results.md` so the prompt and the results stay co-located for the artifact-design discussion.
