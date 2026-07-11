---
name: Strictness-Escalation Skill Architecture
summary: 'When we want a review or audit skill to be genuinely demanding rather than politely suggestive, this is a proven structural recipe: layer a core prompt with numbered non-negotiable standards,
  per-change review questions, an aggressive-flag list, preferred remedies, tone calibration via literal example phrases, prioritized output ordering, and an explicit approval bar that separates presumptive
  blockers from waivable concerns. Cursor''s shipped thermo-nuclear-code-quality-review skill demonstrates the full stack in one prompt-only SKILL.md. Directly reusable as a design template for our own
  assess-* and audit-grade skills.'
implementation_notes: 'Flagged P2 because this is a skill-design exemplar for the assess-skill/design-skill substrate,

  not a skill to adopt as-is (it overlaps the harness /code-review and targets app-code diffs).

  Consider folding the eight-layer scaffold into design-skill''s Template skeleton as an optional

  "strict-mode overlay": (1) core prompt, (2) numbered non-negotiable standards, (3) per-change

  review questions, (4) aggressive-flag list, (5) preferred remedies, (6) tone calibration with

  literal example phrases, (7) prioritized output ordering, (8) approval bar with presumptive

  blockers vs waivable concerns. The tone-calibration layer (verbatim phrases the reviewer should

  emit) is the least common and most transferable piece — it pins register without vague adverbs.'
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- cursor-team-kit-thermo-nuclear-review-skill.md
related_findings:
- file: code-judo-review-posture.md
  rel: extended-by
proposals: null
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
---

# Strictness-Escalation Skill Architecture

## What It Is

An eight-layer prompt architecture for skills that must hold an unusually high bar, demonstrated end-to-end in Cursor's `thermo-nuclear-code-quality-review` skill (cursor/plugins, cursor-team-kit). The layers escalate from intent to enforcement:

1. **Core prompt** — a short baseline directive ("perform a deep code quality audit... measure twice, cut once").
2. **Numbered non-negotiable standards** — explicit review rules (0–7), each with sub-bullets that convert principle into checkable behavior.
3. **Per-change review questions** — a question battery the reviewer must ask of every meaningful change.
4. **Aggressive-flag list** — concrete trigger conditions that must escalate ("a file crossing 1000 lines due to the PR", "one-off booleans, nullable modes, or flags").
5. **Preferred remedies** — the suggestion vocabulary the reviewer should reach for, biased toward deletion over polish.
6. **Tone calibration via literal example phrases** — verbatim sentences the reviewer is expected to emit ("this pushes the file past 1k lines. can we decompose this first?"), pinning register far more precisely than adjectives like "be direct".
7. **Prioritized output ordering** — a 7-level severity ordering plus an anti-flooding rule (fewer high-conviction comments over cosmetic lists).
8. **Explicit approval bar** — conditions for approval, then a named set of *presumptive blockers* the author must justify to waive, cleanly separating blocking from advisory findings.

## Why It Matters

Most "be strict" prompts fail by leaving strictness as an adverb; the model regresses to polite hedging. This architecture operationalizes strictness at every layer where it can leak: what to check (standards + questions), when to escalate (flag list), what to say (remedies + literal phrases), how to rank (output ordering), and when to withhold approval (approval bar with blocker/waivable split). For the engine, it is a reference topology for `/assess-skill`, `/assess-agent`, and any future audit-grade skill where findings must not soften into suggestions.

## Why People Are Using It

Shipped in Cursor's official plugins repo (cursor-team-kit), maintained on main. Cursor's team uses it as an opt-in harsh review mode; the layered structure makes the skill fully portable prompt-only content with no model coupling.

## Potential Improvements

- Parameterize the strictness dial (standards on/off, blocker set selection) so one skill body serves normal and thermo-nuclear modes.
- Add a machine-readable blocker manifest so downstream automation can distinguish blocking from waivable findings without parsing prose.
- Pair with an evidence requirement per flag (file:line citation) to keep aggression grounded.

## Potential Failure Modes

- **False-positive aggression**: an aggressive-flag list without evidence requirements produces confident escalation on borderline cases; the anti-flooding rule mitigates but does not eliminate this.
- **Tone drift on long outputs**: literal phrase calibration anchors early output; late findings may still soften. Reinforcing tone in the output-ordering section helps.
- **Blocker inflation**: adding blockers over time without pruning turns the approval bar into a de facto rejection of all change; the blocker set needs the same lifecycle governance as any rule set.
