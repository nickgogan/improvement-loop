---
name: Task Risk Gradient for Calibrating Verification Depth
summary: 'Plain English: let AI help everywhere, but don''t give every task the same review burden —

  grade tasks by how much damage a wrong output does, and scale verification depth to that

  grade. The source''s gradient for document work: LOW risk = formatting, layout

  exploration, chart drafts, summary wording, consistency checks; MEDIUM = source

  attribution, data extraction; HIGH = numerical synthesis, financial calculations,

  regulatory/compliance language, and any claim that travels up to senior leadership for a

  decision. The gradient is orthogonal to model choice: the model helps at every level and

  is faster everywhere; only the human/hostile-review investment varies.'
implementation_notes: 'P2: a future /assess-* calibration idea (per the session-135 triage report) — assessor

  skills currently apply uniform depth per artifact; a risk-gradient input (which checks

  are load-bearing for this artifact class) could let audits spend depth where wrongness

  is consequential. Also composes with DD-108 supervised autonomy: gate placement by

  consequence, not by task type. Design work needed to translate the office-file gradient

  into engine artifact classes.'
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (assess-* calibration)
- General
adopted_in: []
sources:
- i-built-a-deck-with-ai-then-made-a-second-ai-attack-it.md
related_findings:
- file: generator-assessor-separation-in-skill-iteration.md
  rel: extends
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: advisory-only-for-persistent-mutations.md
  rel: same-problem
- file: task-complexity-tiering-quick-campaign-deep-build.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- verifying-agent-output.md
- templates/task-risk-gradient-rubric.md
---

# Task Risk Gradient for Calibrating Verification Depth

## What It Is

A rubric that assigns verification effort by consequence-of-error rather than by task or
tool. In the source's office-document domain: low risk (formatting, layout exploration,
chart drafts, summary wording, consistency checks — wrongness is cheap and visible),
medium risk (source attribution, data extraction — wrongness propagates but is traceable),
high risk (numerical synthesis, financial calculations, regulatory/compliance language,
claims that travel to leadership — wrongness is expensive, invisible, and mobile). The
operating rule: "let the model help everywhere... now, don't give every task the same
review burden depending on the risk."

## Why It Matters

Most verification guidance in the KB is binary (verify / trust) or role-based (human gates
at stage boundaries). This adds the missing budget dimension: verification depth is a
scarce resource, and uniform depth means over-reviewing chart drafts while under-reviewing
the one number that will be quoted in a board meeting. The "claims that travel" criterion
is the sharpest piece — risk follows the artifact's downstream mobility, not its local
complexity.

## Why People Are Using It

Operationalized inside the author's production build/attack loop to decide where the human
gate stays mandatory ("the human gate can stay on the consequential claims, the numbers
that travel, the calls that become an important decision").

## Potential Improvements

Per-domain gradients (code: generated tests vs auth logic; governance: prose polish vs
binding rule text). Making mobility explicit — tag claims/values with where they will be
reused, and review the high-mobility ones hardest.

## Potential Failure Modes

Misclassification is the whole risk: a "low-risk" summary wording change that alters a
number's meaning slips under the light review tier. Gradients drift — what was low-stakes
becomes load-bearing when an artifact gets promoted (a scratch model becomes the board
model). Teams game the gradient under deadline pressure by classifying optimistically.

## Extraction Note — 2026-07-19
Extracted as **template**: [[task-risk-gradient-rubric]] in `extracts/templates/`
