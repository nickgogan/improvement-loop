---
name: YAML Templates with Embedded Elicitation Instructions
summary: Agent document templates that contain both the output structure (section outline) and embedded LLM instructions for how to collaboratively produce each section, including which advanced elicitation
  techniques to offer at each stage.
implementation_notes: MetaSystem's templates in meta-system/knowledge/templates/ define output structure but do not embed agent behavior instructions. Adding per-section elicitation prompts would implement
  this pattern.
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: enabled-by
- file: business-analyst-upstream-quality-gate.md
  rel: same-problem
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
pipeline_status: "extracted"
consumed_by:
  - "templates/yaml-templates-with-embedded-elicitation.md"
---
## What It Is

BMad Method agent templates are YAML files that contain two interleaved layers:

1. **Document outline** -- the sections and structure of the output artifact (e.g., project brief sections: executive summary, problem statement, target users)
2. **Embedded agent instructions** -- per-section guidance telling the LLM how to work with the human, which questions to ask, and which advanced elicitation techniques to offer at the end of each section

Brian describes this as "more powerful than any other method I've seen so far" because it prevents the LLM from producing a one-shot document dump. Instead, the template forces section-by-section collaborative production where the human reviews and refines each section before moving on. The document is built up incrementally in the file system as sections are completed.

Key behaviors embedded in templates:
- Section-specific questions derived from elicitation methods library
- Advanced elicitation menu at the end of each section (challenge scope, brainstorm alternatives, critical assumption testing, etc.)
- Automatic document persistence -- each section is written to the output file as it is approved
- Kickstart from prior artifacts (e.g., brainstorming output feeds into project brief template)

## Why It Matters

Traditional templates define WHAT to produce but not HOW to produce it collaboratively. The embedded instructions create a structured conversation protocol that prevents the common failure mode of the LLM generating a complete but shallow document in one pass.

## Why People Are Using It

Core mechanism of the BMad Method's document production pipeline. Used across all agent types (Analyst, PM, Architect). The section-by-section approach also mitigates context window pressure by producing incremental output.

## Potential Improvements

Template versioning and A/B testing of different elicitation instruction sets. Dynamic template selection based on project complexity. Integration with MetaSystem's skill YAML format.

## Potential Failure Modes

Over-prescribed templates can make simple documents tedious to produce. The embedded instructions consume template tokens even when the human wants a quick pass. Template maintenance burden increases with the number of agent types.

## Extraction Note — 2026-04-19
Extracted as **template**: [[yaml-templates-with-embedded-elicitation]] in `extracts/templates/`
