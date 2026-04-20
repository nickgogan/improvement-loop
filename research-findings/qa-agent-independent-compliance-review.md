---
name: QA Agent as Independent Compliance Reviewer in Fresh Context
summary: A dedicated QA agent (Quinn in BMad) that reviews completed stories in a brand-new context window, checking source code against story requirements, architecture compliance, and coding standards
  -- catching issues the dev agent cannot see due to its own context bias.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: business-analyst-upstream-quality-gate.md
  rel: same-problem
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
- file: builder-validator-chain-pattern.md
  rel: extends
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- agents/qa-agent-independent-compliance-review.md
---
## What It Is

After the Developer agent completes a story (status: ready-for-review), a QA agent (Quinn) is loaded in a **fresh context window** to review the implementation. The QA agent:

1. Reads the story file (requirements, acceptance criteria, implementation tasks)
2. Reads the project source code and any changes made by the dev agent
3. Checks compliance against architecture docs, coding standards, and source tree constraints
4. Reports issues, improvements, and compliance check results
5. Leaves notes in a dedicated QA section of the story file

Critical design decisions:
- Fresh context is mandatory -- the QA agent must not share the dev agent's conversation history, ensuring independent review
- Brian recommends using the strongest available model (Opus) for QA, even more than for development, because "this is the critical piece that makes sure the agent didn't go off the rails"
- QA reviews should be combined with manual human testing for comprehensive coverage
- The QA agent can catch structural issues (files in wrong directories, missing documentation, dependency violations) that the dev agent introduced

## Why It Matters

Self-review is inherently biased -- a dev agent reviewing its own work in the same context window will rationalize its own decisions. Fresh-context QA review provides an independent verification layer that catches compliance violations, architectural drift, and implementation errors. Nate B Jones provides a production-scale cautionary tale: a $14K voice agent that appeared to work correctly but had never had its data schemas validated by an independent reviewer. The agent self-reported success while producing unusable, unstructured records. Jones's principle -- "have an independent perspective, preferably automated, that tells you if the agent got the job done correctly" -- is exactly the QA-in-fresh-context pattern applied at the organizational level.

## Why People Are Using It

BMad Method includes QA as a standard pipeline stage. The pattern maps to traditional software QA practices where a different person reviews the code. Using the strongest model for QA inverts the typical pattern of using expensive models for generation and cheap models for review.

## Potential Improvements

Automated QA checklists generated from architecture docs. Integration with test execution results. QA agent could produce regression test suggestions for future stories.

## Potential Failure Modes

QA agent may flag false positives if it misunderstands the story context. The fresh context means QA lacks awareness of dev decisions and tradeoffs made during implementation. Simple stories may not justify the overhead of a separate QA pass.

## Extraction Note — 2026-04-19
Extracted as **agent**: [[qa-agent-independent-compliance-review]] in `extracts/agents/`
