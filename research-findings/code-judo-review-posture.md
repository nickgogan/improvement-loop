---
name: "Code Judo Review Posture — Hunt Deletions, Enforce Hard Size Blockers"
summary: |-
  A reviewer instructed to find "code judo" moves — behavior-preserving restructurings that delete whole layers, branches, or modes rather than polish them — produces structurally different feedback than one asked to find problems. Cursor pairs this posture with hard quantitative blockers (a PR pushing a file past 1000 lines is a presumptive rejection), giving the model an unambiguous tripwire it cannot hedge on. Useful to us as review-prompt vocabulary: name the ambition level explicitly and back it with at least one bright-line numeric rule.
implementation_notes: |-
  Flagged P2 as review-prompt design input, not for adoption of the skill itself. Two separable
  ideas to consider when designing or enhancing review/audit prompts: (1) the posture instruction —
  "assume there is often a code-judo move available; if you see a path to delete complexity rather
  than rearrange it, push hard for that path" — reframes review from defect-finding to
  simplification-hunting; (2) at least one hard quantitative blocker (Cursor's: file crossing 1000
  lines = presumptive rejection unless justified) anchors otherwise-subjective strictness. Aligns
  with the engine's existing "abstractions must earn their keep" rule (agent-rules.md rule 11) —
  same philosophy applied at code-review altitude.
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "cursor-team-kit-thermo-nuclear-review-skill.md"
related_findings:
  - file: "strictness-escalation-skill-architecture.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

# Code Judo Review Posture — Hunt Deletions, Enforce Hard Size Blockers

## What It Is

Two coupled review-prompt techniques from Cursor's thermo-nuclear-code-quality-review skill:

1. **The code-judo posture.** The reviewer is told to actively search for restructurings that preserve behavior while making the implementation dramatically simpler — "look for opportunities to reframe the change so that whole branches, helpers, modes, conditionals, or layers disappear entirely"; "prefer the solution that makes the code feel inevitable in hindsight." Crucially, the prompt asserts a prior: "assume there is often a code-judo move available." Preferred remedies are deletion-biased: delete a whole layer of indirection rather than polishing it; reframe the state model so conditionals disappear instead of getting centralized. Explicit anti-satisficing rules close the loop: "do not be satisfied with a merely cleaner version of the same messy idea if there is a plausible path to a much simpler idea."

2. **Hard quantitative blockers.** Alongside the qualitative posture sits a bright-line rule: a PR that pushes a file from under 1000 lines to over 1000 lines is a presumptive blocker — waivable only with a compelling structural justification. The number matters less than its existence: it gives the model one tripwire it cannot soften into a suggestion.

## Why It Matters

Review prompts that ask for "issues" get local nits; ones that assert a deletion-shaped prior get architecture-level findings. The asserted prior ("assume a judo move exists") counteracts the model's tendency to accept the diff's framing as given. The quantitative blocker complements it from the opposite direction: subjective ambition is hedgeable, a line count is not. Together they bracket the review between one un-hedgeable rule and one unbounded ambition target. This is the code-review-altitude expression of the engine's own "abstractions must earn their keep" doctrine.

## Why People Are Using It

Shipped and maintained in cursor/plugins as the team's opt-in harsh review mode. The posture addresses a widely felt failure of LLM review — cosmetic feedback on structurally poor diffs — by changing what the reviewer optimizes for rather than adding more checks.

## Potential Improvements

- Generalize the blocker template: any audit skill can carry one domain-appropriate bright-line rule (token budget ceilings, context-file line counts, frontmatter field limits) as its un-hedgeable anchor.
- Require the reviewer to state the judo move concretely (before/after shape) rather than gesturing at "this could be simpler", keeping ambition falsifiable.

## Potential Failure Modes

- **Judo hallucination**: the asserted prior pushes the model to invent restructurings that subtly change behavior; requiring a behavior-preservation argument per proposed move mitigates.
- **Blocker gaming**: bright-line rules invite mechanical evasion (splitting a file at 999 lines into two incoherent halves); the waiver clause ("compelling structural reason") is the escape valve and needs human judgment.
- **Scope creep in review**: deletion-hunting can turn a small PR review into a demand for unrelated refactors; the skill's own prioritized output ordering partially contains this.
