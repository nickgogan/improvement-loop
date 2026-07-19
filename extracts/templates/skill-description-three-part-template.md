---
title: "Skill Description Three-Part Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "skill-description-structure-what-when-capabilities"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "model-resilient-prompt-engineering.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors writing or reviewing the description field of a skill definition consumed by an LLM-based routing or discovery mechanism"
    - "skill libraries where existing descriptions are vague, missing trigger context, or written for a human reader instead of the routing model"
    - "review or lint tooling checking skill descriptions before publication"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — a description-field edit; no migration cost, effective immediately on next discovery pass"
  auditability: "high — the three-part structure and the length/format constraints are checkable against the rendered description text; a lint pass can flag missing parts or vague language mechanically"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Codified in first-party skill-authoring guidance with worked good/bad examples; paired with an independently-documented 'pushy description' practice to counter under-triggering."
contract:
  preconditions: "A skill (or comparable discoverable capability) has a description field that an LLM uses to decide whether to invoke it, and that field has a length or format constraint (e.g., a character cap, no markup)."
  invariants: "Every description contains three identifiable parts, in order: what the capability does, when to use it (including natural trigger phrasing a user might say), and its key capabilities. The description stays within the platform's length limit and avoids disallowed markup. The description is written for the routing model's matching process, not as human-facing marketing copy."
  governance: "Owner: whoever authors or reviews the skill/capability definition. A description-quality lint or review checklist validates presence of all three parts and flags the named failure modes (too vague, missing triggers, too technical/no triggers) before publication. Naming and format constraints (kebab-case, no reserved words, no markup in frontmatter) are validated at the same review step."
  recovery: "If a skill under-triggers (users describe the need but the skill doesn't fire) → the when-part likely lacks natural trigger phrasing; add concrete phrases a user would actually say. If a skill over-triggers on unrelated requests → the when-part is too broad; narrow the trigger phrasing. If the description exceeds the length limit → trim capabilities detail before trimming the what/when parts, since those two carry the primary matching signal. If review finds a description that promises capabilities the skill's body doesn't deliver → fix the mismatch by narrowing the description or extending the body, not by leaving the mismatch in place."
tags:
  - "extracted-artifact"
  - "template"
  - "prompt-craft"
  - "skill-authoring"
---

# Skill Description Three-Part Template

**Source:** [[skill-description-structure-what-when-capabilities]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{WHAT}}` | string | One or two sentences stating what the capability does, in plain terms. |
| `{{WHEN}}` | string | Natural trigger phrasing — the actual words or situations a user would produce that should cause this capability to fire. Include multiple phrasings if the trigger space is varied. |
| `{{CAPABILITIES}}` | string (optional but recommended) | Specific things the capability can do, named concretely enough to give the routing model extra keywords to match against varied user phrasing. |
| `{{VALUE_PROPOSITION}}` | string (implicit, folded into WHAT) | The concrete outcome a user gets — avoid restating the capability name abstractly. |

## Body

```
{{WHAT}} Use when {{WHEN}}. {{CAPABILITIES}}
```

Worked pattern (paraphrased structure, not a literal example to copy verbatim):

```
[Does X for domain Y]. Use when [user says trigger phrase A], [asks for trigger phrase B],
or [describes situation C]. [Names 1-3 specific capabilities: handles sub-task 1,
sub-task 2, and sub-task 3].
```

**Named failure modes to avoid when filling the template:**

- *Too vague:* the WHAT slot names no concrete domain or output ("Helps with projects.").
- *Missing triggers:* the WHEN slot is absent or generic; no phrasing a user would actually say.
- *Too technical, no user triggers:* the description is written in implementation vocabulary rather than user-facing language, with no trigger phrasing at all.

**Optional escalation — "pushy" framing:** when a capability is known to under-trigger, append an explicit push: "Make sure to use this whenever the user mentions X, Y, Z, even if they don't explicitly ask." This is a deliberate counter to routing-model under-triggering bias, not part of the base three-part structure.

## Usage

Render this template once per skill/capability definition, at authoring time or when revising a description that isn't triggering reliably. The rendered description becomes the discovery-facing metadata field (e.g., a skill's `description` frontmatter). Validate against the platform's format constraints (length cap, disallowed markup, naming rules) after filling the slots — the three-part structure and the constraints are independent checks that both must pass.

## Variation Axis

The primary variation is **trigger breadth**: how wide or narrow the WHEN slot's phrasing is. Over-broad triggers ("use when the user mentions data, charts, files, work, or tasks") cause the capability to fire on unrelated requests; over-narrow triggers ("use when the user says this exact phrase") cause it to never fire in practice. Calibrate WHEN to the actual range of phrasings real users produce for this need — not the phrasing the author would use internally.

A secondary axis is **capability specificity**: naming capabilities as concrete sub-tasks (helps the routing model match varied phrasing) versus naming them as abstract value statements (reads well to a human but gives the routing model fewer keywords to match against).
