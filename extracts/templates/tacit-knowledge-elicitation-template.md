---
title: "Tacit Knowledge Elicitation Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "tacit-knowledge-as-agent-delegation-barrier"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent designers interviewing a domain expert before building a delegation agent"
    - "anyone provisioning an agent constitution, user context file, or personal knowledge store from a human subject"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — template produces a document artifact; the interview is a one-time event with low rollback cost"
  auditability: "high when interview outputs are written to a persistent document that becomes the agent's context source; low when interview output stays in conversation"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "No known deployments. Sourced from practitioner analysis of OpenClaw installation failure patterns across hundreds of thousands of deployments."
contract:
  preconditions: "A domain expert (the subject) is available for a ~45-minute structured interview. An interviewer agent or human will conduct the session. The goal is to produce structured output that will provision an agent's context files."
  invariants: "All five layers are covered before the interview ends. Outputs are written to a persistent document — not left in conversation history. The output document is human-reviewed before being used to provision agent context."
  governance: "Owner: Any skill or workflow that provisions agent context files (soul.md, user.md, CLAUDE.md, knowledge stores) from human input. The template is a prerequisite step for those workflows. Output documents are human-gated before deployment to agent context."
  recovery: "If the subject cannot articulate a layer (common for tacit knowledge) → accept partial output; mark the layer as 'unelicited'; schedule a follow-up session after the subject observes themselves doing the relevant work. If the interview produces sparse output → supplement with observation (ask the subject to narrate while performing a real work task). If the output document is too dense for agent context → summarize per layer; keep the full document as a reference."
tags:
  - "extracted-artifact"
  - "template"
  - "tacit-knowledge"
  - "agent-design"
  - "elicitation"
---

# Tacit Knowledge Elicitation Template

**Source:** [[tacit-knowledge-as-agent-delegation-barrier]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description |
|----------|-------------|
| `{{SUBJECT_NAME}}` | Name or role of the domain expert being interviewed |
| `{{SUBJECT_DOMAIN}}` | Domain or function (e.g., "enterprise sales", "data engineering", "product management") |
| `{{TARGET_AGENT_PURPOSE}}` | What the agent being provisioned is intended to do |
| `{{INTERVIEWER}}` | Name or role of whoever is conducting the interview (human or agent) |
| `{{OUTPUT_FILE}}` | Path or name of the file where interview output will be written |
| `{{SESSION_DATE}}` | Date of the elicitation session |

---

## Body

```markdown
# Tacit Knowledge Elicitation — {{SUBJECT_NAME}}

**Subject:** {{SUBJECT_NAME}}
**Domain:** {{SUBJECT_DOMAIN}}
**Target agent purpose:** {{TARGET_AGENT_PURPOSE}}
**Interviewer:** {{INTERVIEWER}}
**Date:** {{SESSION_DATE}}
**Output file:** {{OUTPUT_FILE}}

---

## Instructions for Interviewer

This is a five-layer elicitation (~45 minutes total). Move through each layer in order. For each question, prompt the subject to give specific examples, not generalizations. If the subject says "it depends," ask: "Give me the last three times you made this decision. Walk me through each one."

Write all outputs to {{OUTPUT_FILE}} before ending the session. Do not leave outputs in conversation history.

---

## Layer 1 — Operating Rhythms (~8 minutes)

**Purpose:** Surface the recurring cadences and rituals that structure the subject's work — the automatic scaffolding they rely on without consciously choosing it.

**Questions:**
- Walk me through a typical week in your role. What do you do first thing? What happens on Mondays vs. Fridays?
- What do you check or review before making any significant decision in your domain?
- What would fall apart if you missed a week of work — not because of your absence, but because of the rhythm you provide?

**Output:**
```
### Operating Rhythms

- Daily/weekly cadences: [fill in]
- Standard check-ins or data sources reviewed: [fill in]
- Rhythms that others depend on from this person: [fill in]
```

---

## Layer 2 — Recurring Decisions and Judgment Calls (~10 minutes)

**Purpose:** Surface the decision patterns that feel automatic to the subject — the judgment calls they make repeatedly without consciously running a decision process.

**Questions:**
- What decisions do you make regularly that someone junior would need a checklist for?
- Describe a decision you made this week that felt obvious to you. What made it obvious?
- When do you override the "standard approach" in your domain? What tells you that the standard doesn't apply?

**Output:**
```
### Recurring Decisions

| Decision | What triggers it | How it's resolved | When the standard doesn't apply |
|----------|-----------------|-------------------|----------------------------------|
| [fill in] | [fill in] | [fill in] | [fill in] |
```

---

## Layer 3 — Required Inputs and Dependencies (~8 minutes)

**Purpose:** Map the information flows the subject relies on — the inputs they implicitly assume are available when doing high-quality work.

**Questions:**
- What information do you need to do your best work that others don't automatically provide?
- What sources do you check that no one told you to check — you just know to check them?
- What would make your work noticeably worse if it was delayed or missing?

**Output:**
```
### Required Inputs

- Inputs that are assumed available: [fill in]
- Non-obvious sources checked regularly: [fill in]
- Dependencies that, if missing, degrade output quality: [fill in]
```

---

## Layer 4 — Recurring Friction Points (~8 minutes)

**Purpose:** Identify the recurring obstacles, workarounds, and time sinks that the subject has adapted to — the friction they absorb without naming.

**Questions:**
- What do you spend time on that feels like it shouldn't be your job?
- What do you redo or fix regularly that should have been done right the first time?
- What do you translate, clarify, or bridge between people or systems that wouldn't work without you doing it?

**Output:**
```
### Friction Points

- Recurring tasks that feel misassigned: [fill in]
- Regular rework or corrections: [fill in]
- Translation/bridging work done informally: [fill in]
```

---

## Layer 5 — Success Criteria (~8 minutes)

**Purpose:** Surface the subject's actual quality bar — the standards they apply that are not written down anywhere.

**Questions:**
- How do you know when your work is good? Not finished — good.
- What would make you uncomfortable handing something off without reviewing it first?
- Describe a piece of work you were proud of. What made it good?

**Output:**
```
### Success Criteria

- Quality markers the subject applies: [fill in]
- Conditions that require personal review before handoff: [fill in]
- Examples of high-quality output and what made them high-quality: [fill in]
```

---

## Synthesis (~3 minutes)

After all five layers, summarize the key patterns:

```
### Elicitation Summary

**Most valuable tacit knowledge surfaced:**
[1-3 bullet points]

**Layers with sparse output (likely still tacit):**
[List layers that produced thin output — these require observation or follow-up]

**Recommended follow-up:**
[Any sessions, observations, or supplementary methods needed]

**Provisioning recommendations:**
[Which outputs should go into which context files for {{TARGET_AGENT_PURPOSE}}]
```
```

---

## Usage

1. Fill in all `{{VARIABLES}}` before starting the interview.
2. Conduct layers in order. Do not skip layers — later layers often surface what earlier layers missed.
3. After each layer, read back your summary to the subject and ask: "Is anything missing or wrong?"
4. Write the output document before ending the session.
5. Human-review the output document before using it to provision any agent context file.

---

## Variation Axis

| Variation | When to use |
|-----------|-------------|
| **Observation supplement** | When the subject's outputs are sparse — ask them to narrate while performing a real work task; supplement written outputs with narration notes |
| **Async version** | When a live 45-minute session is not possible — send each layer as a written prompt and collect answers over 2-3 days; quality is lower but better than no elicitation |
| **Retrospective only** | When the subject has already been working with an agent and can reflect on what the agent got wrong — skip Layers 1-3 and focus on Layers 4-5 with incident examples |
| **Domain pair** | When two subjects share the same domain — run the elicitation on both; compare Layer 2 outputs to surface where judgment diverges |

---

## Contract

### Preconditions
A domain expert (the subject) is available for a ~45-minute structured interview. An interviewer agent or human will conduct the session. The goal is to produce structured output that will provision an agent's context files.

### Invariants
All five layers are covered before the interview ends. Outputs are written to a persistent document — not left in conversation history. The output document is human-reviewed before being used to provision agent context.

### Governance
Owner: Any skill or workflow that provisions agent context files (soul.md, user.md, CLAUDE.md, knowledge stores) from human input. The template is a prerequisite step for those workflows. Output documents are human-gated before deployment to agent context.

### Recovery
If the subject cannot articulate a layer (common for tacit knowledge) → accept partial output; mark the layer as "unelicited"; schedule a follow-up session after the subject observes themselves doing the relevant work. If the interview produces sparse output → supplement with observation (ask the subject to narrate while performing a real work task). If the output document is too dense for agent context → summarize per layer; keep the full document as a reference.
