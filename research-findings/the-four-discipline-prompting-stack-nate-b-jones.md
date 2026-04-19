---
notion_id: 32b1e08b-9b34-8137-86e9-db9102c34548
name: The Four-Discipline Prompting Stack (Nate B. Jones)
summary: 'Four layers building on each other: Prompt Craft -> Context Engineering -> Intent Engineering -> Specification Engineering. Your Notion workspace IS specification engineering; CLAUDE.md IS intent
  engineering.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Already Adopted
proposer_priority: null
applicability:
- General
adopted_in:
- Perplexity Skills
sources:
- nate-b-jones-videos-feb-mar-2026.md
proposals: null
date_discovered: '2026-03-09'
last_updated: 2026-04-08
related_findings:
  - file: "four-discipline-prompt-evaluator.md"
    rel: "extended-by"
  - file: "advanced-elicitation-techniques-library.md"
    rel: "same-problem"
pipeline_status: "raw"
consumed_by: []
---
# The Four-Discipline Prompting Stack (Nate B. Jones)

## What It Is
Nate B. Jones's framework organizes prompting work into four ascending disciplines: Prompt Craft (word-level instruction quality), Context Engineering (what information the model has access to), Intent Engineering (system-level design of agent goals and identity — what CLAUDE.md does), and Specification Engineering (structured knowledge systems that constrain and guide agent behavior — what a well-built Notion workspace does). Each layer depends on and amplifies the layers below it.

## Why It Matters
Most practitioners conflate all four disciplines into "prompting," which obscures where problems actually originate and where improvements will have the most leverage. The framework provides a diagnostic lens: a bad output might be a Prompt Craft failure, a Context failure, an Intent failure, or a Specification failure — each requiring a different fix.

## Why People Are Using It
Adopted as the rubric for the prompt-evaluator skill and used as the evaluative framework for every prompt assessed in the improvement loop. The framework's mapping to concrete artifacts (CLAUDE.md = intent engineering, Notion workspace = specification engineering) makes it immediately actionable rather than purely theoretical.

## Potential Improvements
The four disciplines could be embedded as an explicit checklist in Build Spec templates, prompting authors to address each layer when designing new agents or workflows. A scoring rubric per discipline would make improvement loop assessments more consistent and comparable over time.

## Potential Failure Modes
The main failure mode is treating the four disciplines as a sequential pipeline when they are actually iterative — a Specification Engineering change often requires revisiting Prompt Craft decisions made earlier. There is also a risk of over-engineering lower layers (obsessing over word choice) while neglecting higher-leverage layers like Intent and Specification.
