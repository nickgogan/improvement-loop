---
title: "Strict-Mode Review-Skill Overlay"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "strictness-escalation-skill-architecture"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "model-resilient-prompt-engineering.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "authors designing a review or audit skill that needs to hold a genuinely high bar rather than produce polite, hedged suggestions"
    - "existing review/audit skills that have drifted into softness — findings phrased as suggestions, no clear approval boundary"
    - "skill-design toolchains that want an optional 'strict mode' overlay separate from a skill's baseline, more permissive behavior"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — a prompt-only overlay; can be removed or toggled off with no data migration"
  auditability: "high — each of the eight layers is a discrete, inspectable block in the skill's prompt; presence and content of each layer can be checked directly against the rendered skill definition"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Demonstrated end-to-end in a shipped, officially-maintained code-quality-review skill, used as an opt-in harsh review mode; portable prompt-only content with no model coupling."
contract:
  preconditions: "A review or audit skill is being authored or revised, and the desired behavior is a demanding, blocker-oriented review posture rather than a permissive, suggestion-only one. The skill has (or can be given) a baseline prompt that this overlay escalates."
  invariants: "All eight layers are present and each does the job specific to it — no layer is replaced by a vaguer substitute (e.g., a single adjective like 'be strict' does not substitute for the tone-calibration layer's literal example phrases). The approval-bar layer names an explicit set of presumptive blockers distinct from waivable concerns; a review skill using this overlay does not conflate the two. The tone-calibration layer uses literal example sentences, not adjectives, to pin register."
  governance: "Owner: whoever authors the review/audit skill this overlay is applied to. When used as an optional overlay on a shared skill-design template, the base template and the strict-mode layers are maintained together so drift between the base skeleton and the overlay's assumptions doesn't accumulate. The blocker set (layer 8) needs periodic review — adding blockers without pruning turns the approval bar into a de facto rejection of all changes over time."
  recovery: "If the review skill's findings soften into suggestions despite this overlay → check the tone-calibration layer (6) for missing or diluted literal phrases; adjectival strictness language elsewhere in the prompt does not substitute for it. If the aggressive-flag list (4) produces confident escalation on borderline cases without evidence → pair each flag with an evidence requirement (e.g., a file:line citation) before it fires. If tone drifts on long outputs (early findings are sharp, later ones soften) → reinforce tone expectations in the output-ordering layer (7), not only at the top of the prompt. If the approval bar (8) has accumulated blockers to the point of de facto blocking all changes → review and prune the blocker set; treat it as a governed list with the same lifecycle discipline as any rule set."
tags:
  - "extracted-artifact"
  - "template"
  - "skill-authoring"
  - "review-audit"
  - "strictness"
---

# Strict-Mode Review-Skill Overlay

**Source:** [[strictness-escalation-skill-architecture]]
**Form:** template
**Extraction date:** 2026-07-19

An eight-layer prompt scaffold for review or audit skills that must hold a demanding bar rather than default to polite, hedged suggestions. Escalates strictness from intent through to a concrete approval boundary, one layer at a time — each layer closes off a specific place strictness tends to leak.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{CORE_PROMPT}}` | Short baseline directive stating the review's overall posture (e.g., "perform a deep quality audit — measure twice, cut once") | Yes |
| `{{STANDARD_N}}` | One numbered non-negotiable standard, with sub-bullets converting the principle into checkable behavior | Yes (≥1) |
| `{{REVIEW_QUESTION_N}}` | One question the reviewer must ask of every meaningful change | Yes (≥1) |
| `{{FLAG_TRIGGER_N}}` | One concrete trigger condition that must escalate a finding (e.g., "a file crossing N lines due to this change") | Yes (≥1) |
| `{{PREFERRED_REMEDY_N}}` | One entry in the suggestion vocabulary the reviewer should reach for, biased toward the strongest fix (e.g., deletion over polish) | Yes (≥1) |
| `{{TONE_EXAMPLE_N}}` | One verbatim example sentence the reviewer is expected to emit — not an adjective, an actual phrase | Yes (≥2 recommended) |
| `{{SEVERITY_LEVEL_N}}` | One rung in the prioritized output ordering (e.g., a 5-7 level severity scale) | Yes (≥3) |
| `{{ANTI_FLOODING_RULE}}` | The rule limiting output volume (e.g., "prefer fewer high-conviction comments over a cosmetic list") | Yes |
| `{{APPROVAL_CONDITION}}` | What must be true for the change to be approved | Yes |
| `{{BLOCKER_N}}` | One named presumptive blocker the author must justify to waive | Yes (≥1) |
| `{{WAIVABLE_N}}` | One named advisory/waivable concern, distinct from blockers | Optional |

## Body

```markdown
## Core Prompt
{{CORE_PROMPT}}

## Non-Negotiable Standards
0. {{STANDARD_0}}
   - [sub-bullets converting principle into checkable behavior]
1. {{STANDARD_1}}
<!-- one numbered standard per line, each with sub-bullets -->

## Per-Change Review Questions
- {{REVIEW_QUESTION_1}}
- {{REVIEW_QUESTION_2}}
<!-- the question battery asked of every meaningful change -->

## Aggressive-Flag List
- {{FLAG_TRIGGER_1}} → escalate
- {{FLAG_TRIGGER_2}} → escalate
<!-- concrete trigger conditions, not vague heuristics -->

## Preferred Remedies
- {{PREFERRED_REMEDY_1}}
<!-- suggestion vocabulary, biased toward the strongest available fix -->

## Tone Calibration
Emit findings in this register — literal phrases, not adjectives:
- "{{TONE_EXAMPLE_1}}"
- "{{TONE_EXAMPLE_2}}"

## Prioritized Output Ordering
Severity scale (highest first): {{SEVERITY_LEVEL_1}} > {{SEVERITY_LEVEL_2}} > ...
{{ANTI_FLOODING_RULE}}

## Approval Bar
Approve when: {{APPROVAL_CONDITION}}
Presumptive blockers (must be justified to waive):
- {{BLOCKER_1}}
Waivable concerns (advisory only):
- {{WAIVABLE_1}}
```

## Usage

Apply this overlay on top of a review or audit skill's baseline template when the desired posture is genuinely demanding rather than suggestive. Fill each layer in order — the layers build on each other: standards and questions define *what* to check, the flag list defines *when* to escalate, remedies and tone calibration define *what to say*, output ordering defines *how to rank* findings, and the approval bar defines *when to withhold approval*. Treat this as an optional strict-mode variant a skill-design template can apply, not a requirement for every review skill — many review contexts want the skill's baseline, more permissive posture instead.

## Variation Axis

What drives different renderings of this overlay:

- **Blocker-set size and composition.** A narrow blocker set keeps the approval bar meaningful; a blocker set that grows without pruning turns the bar into a de facto rejection of nearly everything. Calibrate to the actual risk tolerance of what's being reviewed.
- **Evidence requirement on flags.** Pairing the aggressive-flag list with a mandatory evidence citation (file:line) keeps escalation grounded; omitting it trades rigor for speed but risks false-positive aggression on borderline cases.
- **Tone example count and specificity.** More literal tone examples anchor register more precisely across a long output; fewer examples risk tone drift on later findings unless reinforced in the output-ordering layer.
- **Domain of application.** The scaffold was demonstrated on application-code diffs but is domain-agnostic prompt structure — the same eight layers can be re-parameterized for prose, configuration, or any artifact type a review skill audits.
