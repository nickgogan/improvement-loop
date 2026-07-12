---
name: "Cross-Vendor Adversarial Build/Attack Loop with Terminal Language-Polish Pass"
summary: |-
  Plain English: have one vendor's model build the artifact and a different vendor's model
  attack it, loop until clean, and only at the end run a language pass — so polish never
  hides weak substance. Concrete production loop: Codex builds the office artifact; Claude
  Opus 4.7 hostile-reviews it and generates an extremely detailed edit list; the list is
  piped back to Codex, which fixes everything into a new version; the same Opus thread
  re-checks ("did they do the job?"); repeat. Only toward the end does Opus run a
  language-polish pass (stripping LLM-isms like "you're absolutely right"). Cross-vendor
  pairing is deliberate — different training lineages mean less-correlated blind spots.
  Human time is repositioned to reading A-level output and making judgment calls, not
  producing drafts.
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "General"
adopted_in: []
sources:
  - "i-built-a-deck-with-ai-then-made-a-second-ai-attack-it.md"
related_findings:
  - file: "generator-assessor-separation-in-skill-iteration.md"
    rel: "extends"
  - file: "enumerate-dont-fix-hostile-reviewer-prompt.md"
    rel: "enabled-by"
  - file: "ralph-loop-brute-force-security-and-ui-testing.md"
    rel: "same-problem"
  - file: "context-pollution-same-window-verification-bias.md"
    rel: "same-problem"
  - file: "iterative-refinement-loop-with-quality-gate.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Cross-Vendor Adversarial Build/Attack Loop

## What It Is

A self-described "Ralph loop" for knowledge-work artifacts with three distinguishing
choices beyond generic build-review iteration:

1. **Cross-vendor role assignment.** Builder and attacker come from different vendors
   (Codex builds; Opus 4.7 attacks — "I like to play them off against each other"), chosen
   per strength: Codex for completeness in Excel models and argumentation, Claude for
   front-end polish and deck rendering.
2. **Asymmetric channels.** The attacker's persistent thread holds review state across
   rounds (it re-checks whether its previous edit list was satisfied); the builder receives
   only the edit list and produces new versions.
3. **Terminal language-polish pass.** Plain-English/LLM-ism cleanup runs only after
   substance converges — sequencing that prevents visual and verbal polish from hiding a
   weak argument (the same reason the deck workflow storyboards claims before rendering).

## Why It Matters

Third-corroboration territory for the engine's rule-10 separation stance, but with deltas
the existing findings don't carry: vendor diversity as a decorrelation lever (the KB's
separation findings separate *contexts*; this separates *training lineages*), the
review-state-vs-build-state channel asymmetry, and polish-last sequencing as an explicit
anti-deception measure. The economic frame is also crisp: the loop runs autonomously to
A-level quality so human attention is spent only on agree/disagree/final-polish judgment.

## Why People Are Using It

Production use in the author's document pipeline, scaled to ~8 simultaneous documents when
source repositories are clean. Hyperscaler contacts reportedly hadn't seen the models
composed this way.

## Potential Alternatives

Same-vendor fresh-context review (cheaper, one subscription, weaker decorrelation);
multi-critic councils (more perspectives per round, higher orchestration cost);
deterministic validators where the artifact admits them (spreadsheet recalculation checks).

## Potential Failure Modes

Two-vendor cost and operational surface. Convergence isn't guaranteed — builder and
attacker can oscillate on style disagreements; needs a round cap. The attacker thread's
context grows stale/polluted over many rounds. Vendor-strength assignments (who builds,
who attacks) are empirical and shift with every model release. Polish-last discipline
erodes under deadline pressure — running the polish early recreates the trust problem.
