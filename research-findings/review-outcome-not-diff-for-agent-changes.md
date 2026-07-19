---
name: "Review the Outcome, Not the Diff, for Batched Agent Changes"
summary: |-
  Namespace's proposed shape of the human approval step once code generation and
  internal validation both run fast: the human's role narrows to one external-approval
  checkpoint judging intent-vs-result, not the code diff. Quote: the human "looks at not
  the code, but that this was the intent and this was the result" — where "result" is a
  demo video of the feature working, or the verdict of an automated critic (a
  security-focused LLM, an API-conformance-focused LLM) that already validated the
  change. Crucially, the reviewable unit is not necessarily one commit or PR — because
  too many agent-authored changes are in flight to review individually, review may
  cover multiple agents' work "semantically grouped into something that you as a human
  can manage." This sits downstream of, and depends on, the companion pre-merge
  reconciliation queue that batches concurrent changes before a human ever sees them.
implementation_notes: |-
  Useful as an audit lens, not a build task: review IL's existing human-gated skill
  outputs (MANIFEST.md files, staged-batch summaries, /audit-artifacts reports) against
  the intent-and-result framing to check whether Nick is ever implicitly asked to read
  a diff where a summary would serve — a good /system-audit or /simplify-context
  checklist addition rather than new infrastructure.
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "cicd-is-dead-continuous-compute-and-computers.md"
related_findings:
  - file: "pre-merge-reconciliation-queue.md"
    rel: "enabled-by"
  - file: "multi-perspective-review-council.md"
    rel: "same-problem"
  - file: "pre-code-validation-contracts-dual-blind-validators.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
tags:
  - "evaluation"
  - "ci-cd"
  - "governance"
---

## What It Is

Namespace's proposed shape of the human checkpoint once code generation and internal
(build/test) validation both run fast and mostly autonomously: the human is no longer
the one reading the diff. Direct quote: "the human comes in, where looks at not the
code, but that... this was the intent and this was the result." "Result" is exemplified
concretely — a demo video of the feature working, or the output of an automated critic
(a security-focused LLM, an API-conformance-focused LLM) that already evaluated the
change before the human sees it. The reviewable unit is explicitly not necessarily one
commit or one PR: because so many agent-authored changes are in flight, review may
cover multiple agents' work "semantically grouped into something that you as a human
can manage," precisely because there will be "way too many" individual changes for
one-at-a-time review. This pattern sits downstream of, and depends on, the companion
`pre-merge-reconciliation-queue` finding, which is what actually serializes and groups
the concurrent changes before a human ever sees them.

## Why It Matters for Us

This names, directly, the axis every human-gated pipeline eventually has to choose:
does the human read the change, or read what the change did? Diff-reading doesn't scale
past a handful of concurrent agents, and it also doesn't match what a human actually
needs to judge (did this do the right thing?) against what a diff shows (which lines
changed). The pattern has a concrete resonance with how several of this engine's own
human gates already work: a staged-batch MANIFEST — exactly the kind of artifact this
Pass-2-extraction task itself produces — is already an "intent + result" summary Nick
reviews instead of reading every line of every staged file up front. This finding names
that shape explicitly and traces *why* it becomes necessary at scale (volume), which is
useful vocabulary for checking whether IL's other gates (skill-run summaries, staged
extracts, batch manifests) are structured this way on purpose or by accident.

## Why People Are Using It

Same Namespace talk and team as the companion reconciliation-queue finding. The
automated-critic-in-the-loop half of the idea — a security-focused LLM or an
API-conformance LLM providing feedback the harness incorporates before a human ever
sees the change — is presented as already happening today at Namespace and its named
customers, not purely aspirational.

## Potential Alternatives

- **Traditional diff review** (line-by-line code review) — the default being
  displaced; still the right choice at low concurrency, or where the *mechanism*, not
  just the outcome, carries the risk (e.g., security-sensitive code where a
  plausible-looking result can hide a subtly wrong implementation).
- **Automated review only, no human step** — faster, but removes the human gate this
  engine's hard constraints require; the pattern as described keeps a human step, it
  just changes what the human looks at.
- **`multi-perspective-review-council`** (existing finding) — decomposes review by
  *dimension* (factual/safety/style) via specialized critics; this pattern decomposes by
  *object* (outcome vs. process) and by *volume* (batched vs. per-change). The two are
  compatible: a review council's critics could be exactly the "security-focused LLM" /
  "API-conformance LLM" that produce the outcome evidence a human then approves.

## Potential Improvements

Concretely testable for IL without new infrastructure: audit whether existing
skill-run gates (MANIFEST.md summaries, `/audit-artifacts` reports) are already
intent-and-result shaped, and flag any gate that still implicitly asks Nick to read a
raw diff rather than a summary.

## Potential Failure Modes

- **Gameable or shallow outcome evidence** — a demo video or a green automated-critic
  verdict can both be true while the underlying diff is fragile, over-fit to the shown
  case, or hides a maintainability cost; "the result looked right" is a weaker guarantee
  than a human reading the mechanism, especially for infrastructure or
  security-relevant changes.
- **Unspecified semantic grouping** — per the companion `pre-merge-reconciliation-queue`
  finding, how multiple agents' work gets batched into one reviewable unit is
  unaddressed in the source; a bad grouping heuristic undermines the whole premise of
  this pattern.
- **Unverified automated critics** — the security/conformance LLMs are themselves
  presented without any description of how their own verdicts are validated, an
  infinite-regress risk familiar from LLM-as-judge patterns elsewhere in the KB.
