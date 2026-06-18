---
name: "Taste and Craft as Post-LLM Differentiator"
summary: "When coding LLMs commoditize first prototypes, the true differentiator becomes taste and craft -- how intuitive and well-designed the product is. Systematic dogfooding (weekly dedicated sessions, running internal experiments, shipping only a fraction) is the discipline that builds this taste muscle."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "problem-with-ai-agents-utori-compound-errors.md"
related_findings:
  - file: "visible-quality-as-trust-proxy-for-invisible-work.md"
    rel: "extends"
  - file: "five-persistent-human-skills-agent-era-framework.md"
    rel: "same-problem"
  - file: "architecture-literacy-as-ai-dev-differentiator.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
tags:
  - "session-95-reextract"
pipeline_status: "classified"
---

# Taste and Craft as Post-LLM Differentiator

## What It Is

A market thesis: "In a world where it's very easy to come up with first prototypes using these coding LLMs, the true differentiator is in taste and craft, in how intuitive and well-designed the product is." (Abhishek Das, Utori)

When the cost of building a first prototype drops to near zero (because coding LLMs can generate it), the competitive moat shifts from "can you build it" to "is it good." The ability to distinguish good from bad product experiences becomes the scarce, high-value skill.

Utori's operational practice: weekly 1-1.5 hour dogfooding sessions, running tens of internal experiments at any given time, shipping perhaps one to production users. "Constantly dogfooding our own product is a way to refine our own taste for what is good versus bad, what awesome or magical feels like. A lot of reps to build that muscle."

## Why It Matters

For agent harness builders, this means: the differentiation is not in which LLM you use or how many features your agent has. It is in the design quality of the agent experience -- how it handles errors, how it communicates uncertainty, how it structures its output, what it chooses to automate versus delegate. These are taste decisions that require iteration and direct experience with the product.

For MetaSystem, this suggests: Nick's direct experience using the IL pipeline, GSD skills, and governance tools is the taste-building mechanism. The regular cadence of sessions where Nick uses the system (not just reviews outputs) is how design quality improves. The system should be dog-fooded, not just operated.

## Why People Are Using It

Utori runs this as an explicit team practice. The framing is that taste is a muscle built through reps, not an innate quality. The 80/20 approach to feature prioritization also feeds into this -- combining what users explicitly ask for with intuition-driven features that make users "feel seen."

## Potential Improvements

Structured dogfooding with capture: document friction points, unexpected behaviors, and delight moments during dogfooding sessions and feed them into the product backlog. Compare internal dogfooding findings with external user feedback to calibrate intuition.

## Potential Failure Modes

Dogfooding bias: internal users develop workarounds and tolerance for issues that external users would not accept. Taste without constraint leads to over-engineering and gold-plating. The "feel seen" features may not actually matter to the user base if the builder's intuition is miscalibrated.
