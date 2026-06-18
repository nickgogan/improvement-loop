---
name: Thesis-Anchored Multi-Question Prompting for Knowledge Work
summary: 'With frontier models (Opus 4.7, GPT-5.5), optimal input for deep knowledge work is a series of open questions anchored to an explicit, falsifiable user thesis. Without the thesis anchor, the model
  either mirrors the user''s opinion back or dives depth-first into one data source instead of synthesizing across all inputs. Three structural elements: stated directional thesis the model is invited to
  challenge, named data artifacts the model must engage with, and explicit exclusion of out-of-scope context.'
implementation_notes: Could apply to MetaSystem's research-query skill — when Nick asks to investigate a topic, structuring the prompt with a falsifiable thesis + named artifacts + scope exclusions might
  yield better synthesis than open-ended questions.
category: Prompt Craft
evidence_strength: Anecdotal
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- opus-4-7-prompting-style-obsolete.md
proposals: null
date_discovered: '2026-05-24'
last_updated: '2026-05-24'
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: bidirectional-prompting-for-spec-creation.md
  rel: same-problem
pipeline_status: raw
tags:
- prompt-engineering
- context-engineering
---

# Thesis-Anchored Multi-Question Prompting for Knowledge Work

## What It Is

A prompting pattern for frontier models: instead of task specifications, provide a series of open questions anchored to an explicit, falsifiable thesis (the "flashlight center"). The thesis invites the model to push back rather than confirm. Named data artifacts force engagement with specific sources. Explicit scope exclusions prevent depth-first diving into one irrelevant source.

## Why It Matters

Two failure modes this pattern prevents: (1) "wild rambling opinion" where the model mirrors the user's thesis rather than examining data; (2) unguided multi-file synthesis defaulting to depth-first on the first salient hit. The pattern is model-dependent — claimed to be effective on Opus 4.7 and GPT-5.5 but not on older models that lack multi-directional synthesis capability.

## How It Could Fail

Model-capability-dependent — degrades on older models. No benchmarks cited. The falsifiable thesis framing requires the user to have a directional hypothesis, which may not exist for genuinely exploratory questions.
