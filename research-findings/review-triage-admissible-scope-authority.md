---
name: "Review Triage with Admissible Scope Authority and Parent-Owned Severity"
summary: |-
  Plain English: when triaging review findings, define WHICH documents are even
  admissible as authority for calling something out-of-scope — and let only the
  original intent qualify, because if the spec's wording or the diff's shape is the
  only thing excluding a finding, that itself is evidence the spec is wrong. BMAD
  v6.10.0's unattended dev loop routes every review finding into exactly one of five
  categories (intent_gap / bad_spec / patch / defer / reject); only the verbatim intent
  may authorize defer/reject-as-out-of-scope — spec language, plan, and diff shape are
  inadmissible for that purpose. Complementarily, the parent orchestrator discards
  subagent-assigned severity outright, because reviewers operate under "by-design
  information asymmetry": severity is judged by consequence for the artifact's main
  consumer after reading surrounding source, context the reviewer never had.
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "controller-deauthorization-reviewer-independence.md"
    rel: "same-problem"
  - file: "enumerate-dont-fix-hostile-reviewer-prompt.md"
    rel: "same-problem"
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "evaluation"
  - "review-triage"
  - "authority-allocation"
---

# Review Triage with Admissible Scope Authority and Parent-Owned Severity

## What It Is

Two authority-allocation rules in the review-triage step of BMAD's unattended dev loop
(`bmad-dev-auto/step-04-review.md`):

1. **Admissible scope authority.** Every finding routes to exactly one of five
   categories: intent_gap, bad_spec, patch, defer, reject. Routing a finding
   out-of-scope (defer/reject) may be justified ONLY by the verbatim intent — the
   original statement of what the work is for. The spec's language, the plan, and the
   shape of the diff are explicitly inadmissible as scope authority; if only they
   exclude a finding, that is evidence of intent_gap or bad_spec, and the finding
   routes there instead of being dismissed.
2. **Parent-owned severity.** The orchestrator discards severity ratings assigned by
   reviewer subagents. Reviewers operate under "by-design information asymmetry" (they
   see a diff and a brief, not the system); severity is re-judged by the parent by
   consequence for the artifact's main consumer, after reading surrounding source.

## Why It Matters

Unattended loops die by quiet scope erosion: the cheapest response to an awkward
finding is "out of scope," and the documents most often cited for that dismissal (spec
wording, plan, diff shape) are the very artifacts whose defects the finding may be
exposing. Making intent the *only* admissible scope authority converts dismissals into
spec-defect signals — a self-correcting loop instead of a self-excusing one. The
severity rule is the same epistemics applied to ratings: judgment belongs to whoever
holds the context, and the design says explicitly who that is. Notably, this allocates
severity *to* the orchestrator while Superpowers' v6 forbids its controller from
pre-rating severity — the two systems agree the allocation must be explicit, and
disagree on where it lands (BMAD's parent re-judges after reviewers report;
Superpowers protects reviewer independence before they report).

## Why People Are Using It

Load-bearing in BMAD's dev-auto worker, where no human is present to catch scope
erosion; the triage log is append-only with loopback tracking so every routing decision
is auditable. Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Reviewer-owned severity** (Superpowers) — protects independence; costs the
  surrounding-context calibration the parent has.
- **Fixed severity rubrics** — consistent but context-blind; neither party judges
  consequence for the actual consumer.
- **Human triage of all findings** — the attended baseline this mechanism replaces.

## Potential Improvements

- Intent quality gates: the mechanism is only as good as the verbatim intent; a weak
  intent makes everything deferrable. Pairing with an intent-hardening step (idea
  forge) closes the loop.
- Cross-run analytics on routing distribution (a rising reject share flags erosion).

## Potential Failure Modes

- **Intent overload** — teams start stuffing implementation detail into intents to make
  them scope-authoritative, recreating the spec bloat the kernel avoided.
- **Parent overconfidence** — discarding reviewer severity assumes the parent actually
  reads surrounding source; skipped, it becomes unilateral downgrade authority.
- **Category gaming** — five buckets invite borderline findings to be routed to the
  cheapest bucket; the append-only triage log is the audit counterweight.
