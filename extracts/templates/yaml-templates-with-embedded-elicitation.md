---
title: "YAML Templates with Embedded Elicitation Instructions"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "yaml-templates-with-embedded-elicitation-instructions"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "collaborative document production workflows where human judgment is required at each section"
    - "specification and design artifacts that must not be one-shot drafted (briefs, architecture docs, PRDs)"
    - "human-in-the-loop document authoring sessions in agentic coding or design pipelines"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — the template is a YAML file; removal or replacement has no downstream migration cost"
  auditability: "high — section-by-section acceptance is explicit; each approved section is written to disk immediately, leaving an auditable incremental record"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Core mechanism of the BMad Method document production pipeline, used across Analyst, PM, and Architect agent types. No adoption within this system at time of extraction."
contract:
  preconditions: "SECTIONS variable is fully populated with at least one entry. OUTPUT_FILE_PATH is writable. If PRIOR_ARTIFACTS is non-empty, all listed files exist. The human is available for turn-based interaction."
  invariants: "Agent writes each approved section immediately upon acceptance. Elicitation menu is presented after every section draft. Agent does not advance without explicit human signal. agent_instructions block is never removed or summarized."
  governance: "Owner: Improvement Loop (research origin), Meta-System knowledge/templates/ (codification home). Changes to agent_instructions or section-by-section protocol require Nick authorization."
  recovery: "If agent produces one-shot output: discard, start fresh context, verify agent_instructions is present. If agent skips elicitation menu: interrupt, re-present menu. If OUTPUT_FILE_PATH not writable: resolve before loading template."
tags:
  - "extracted-artifact"
  - "template"
---

# YAML Templates with Embedded Elicitation Instructions

**Source:** [[yaml-templates-with-embedded-elicitation-instructions]]
**Form:** template
**Extraction date:** 2026-04-19

## Variables

| Variable | Type | Description |
|----------|------|-------------|
| `{{ARTIFACT_NAME}}` | string | Name of the document this template produces |
| `{{ARTIFACT_PURPOSE}}` | string | What the produced document is used for and who reads it |
| `{{PRIOR_ARTIFACTS}}` | markdown list | Upstream documents the agent should read before starting |
| `{{SECTIONS}}` | YAML block | Ordered list of document sections with questions and elicitation menus |
| `{{OUTPUT_FILE_PATH}}` | string | Where the document is persisted as each section is approved |
| `{{KICKSTART_INSTRUCTIONS}}` | string | How to ingest prior artifacts before the first section |

### SECTIONS Entry Structure

```yaml
- name: "<Section Title>"
  description: "<What this section covers>"
  questions:
    - "<Question 1>"
    - "<Question 2>"
  elicitation_menu:
    - label: "Challenge Scope"
      instruction: "Re-examine boundaries. Ask: what if we did half? What if twice as much?"
    - label: "Brainstorm Alternatives"
      instruction: "Generate three alternative approaches. Present without advocating."
    - label: "Critical Assumption Test"
      instruction: "Surface the top two assumptions. Ask human to confirm or challenge."
    - label: "Stakeholder Reversal"
      instruction: "Argue from the perspective of someone who would oppose this section."
    - label: "Accept and Continue"
      instruction: "Write approved section to {{OUTPUT_FILE_PATH}} and advance."
```

## Body

```yaml
# {{ARTIFACT_NAME}} Template
# Purpose: {{ARTIFACT_PURPOSE}}
# Output: {{OUTPUT_FILE_PATH}}

agent_instructions: |
  You are producing {{ARTIFACT_NAME}} collaboratively with the human.
  Do NOT generate the entire document in one pass.
  Work section by section. For each section:
    1. Read the section description.
    2. Ask the section questions.
    3. Wait for human responses.
    4. Draft the section based on responses.
    5. Present the draft and offer the elicitation menu.
    6. Incorporate feedback or proceed when "Accept and Continue" is selected.
    7. Write the approved section to {{OUTPUT_FILE_PATH}} immediately.
    8. Advance to the next section.
  When all sections are complete, present the full document path and summarize open questions.

kickstart: |
  {{KICKSTART_INSTRUCTIONS}}

prior_artifacts:
{{PRIOR_ARTIFACTS}}

sections:
{{SECTIONS}}
```

## Usage

Used when the goal is a collaboratively produced document — not a one-shot draft. Load the rendered YAML into the agent's context at session start.

Use this template when:
- The output document requires human judgment at each stage
- A one-shot draft would be shallow or miss unstated constraints
- The human wants to iterate on each section before the next begins

Do not use when:
- The human explicitly requests a quick single-pass draft
- The document is purely mechanical with no judgment required
- Token budget is severely constrained

## Variation Axis

1. **Section count and depth** — Simple artifacts (2-3 sections) produce lightweight templates. Complex artifacts (8+) require careful sequencing.
2. **Elicitation menu composition** — Menu entries should be tailored to the cognitive task of each section. Generic menus reduce quality.
3. **Prior artifact density** — When populated, kickstart instructions must specify exactly what to extract — not just "read these files."

## Contract

### Preconditions
SECTIONS variable is fully populated with at least one entry. OUTPUT_FILE_PATH is writable. If PRIOR_ARTIFACTS is non-empty, all listed files exist. The human is available for turn-based interaction.

### Invariants
Agent writes each approved section immediately upon acceptance. Elicitation menu is presented after every section draft. Agent does not advance without explicit human signal. agent_instructions block is never removed or summarized.

### Governance
Owner: Improvement Loop (research origin), Meta-System knowledge/templates/ (codification home). Changes to agent_instructions or section-by-section protocol require Nick authorization.

### Recovery
If agent produces one-shot output: discard, start fresh context, verify agent_instructions is present. If agent skips elicitation menu: interrupt, re-present menu. If OUTPUT_FILE_PATH not writable: resolve before loading template.
