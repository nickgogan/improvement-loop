---
name: "Split Docs by Lifespan, Not Topic (Active / Decisions / Reference / Archive)"
summary: |-
  Partition project documentation by how long each document stays TRUE, not by what it
  is about: active/ (living plans, updated as you go), decisions/ (short records that
  freeze the why), reference/ (runbooks, registries, guides that don't expire), and
  archive/ (finished work stamped "do not follow"). The reason is agent-specific: a
  shipped plan left in the active pile confidently steers the AI at a target you
  already hit — "stale docs are worse than no docs. With no docs, the AI asks. With
  stale docs, it charges off the wrong way, certain that it's right." Moving finished
  work to a labeled archive is the cheap defense against being poisoned by your own
  history.
implementation_notes: |-
  Lands on a live engine concern: the vault has archives, generated docs, handoffs,
  and a growing CLAUDE.md surface, and the KB previously had nothing on docs-lifecycle
  partitioning. Concrete candidate deltas (future, Nick-gated — capture only): a
  lifespan lens in /maintain-docs drift detection (is anything in an active location
  actually finished?), and explicit do-not-follow stamps on archived plans/handoffs.
  The decisions/ quadrant is already adopted (DD system); the active-vs-archive
  lifecycle discipline is the partial gap.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "General"
  - "IL (docs lifecycle, /maintain-docs)"
adopted_in:
  - "Improvement Loop"
sources:
  - "the-folder-structure-that-makes-ai-build-better-software.md"
related_findings:
  - file: "bmad-v6-diataxis-documentation-and-llms-txt.md"
    rel: "same-problem"
  - file: "evergreen-vs-volatile-ingestion-rule.md"
    rel: "same-problem"
  - file: "claudemd-as-knowledge-base-traversal-guide.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A documentation-layer partition keyed on truth-lifespan, from Alex Brockway's
production folder skeleton (thin root router → rules layer → knowledge layer → docs
layer). The docs layer has four folders:

1. **active/** — living plans, work in flight, updated as you go.
2. **decisions/** — decision records: every time you choose between approaches (DB A
   over DB B, add/reject a library, change architecture), write a ~90-second note of
   what you chose and why. "Code shows what you did, never the why... The note freezes
   the why. Write it down and you never fight that battle twice."
3. **reference/** — runbooks, registries, integration guides; references that don't
   expire.
4. **archive/** — finished work kept for history, labeled in plain language: "do not
   follow."

The load-bearing rule is the transition: when a plan ships, it MOVES from active/ to
archive/ and gets stamped. Topic-based organization has no such transition — a
finished plan about the database sits next to a current one about the database, and
the agent can't tell which is true.

## Why It Matters

The failure mode is specific to AI readers and quietly severe: agents weight retrieved
docs as current truth. A week-old shipped plan still in active/ has the agent "building
toward a target you already hit and moved past," confidently wrong for sessions on
end. Lifespan partitioning makes staleness structural — location encodes trust — so
the router can safely say "read active/ for current work" without a per-document
freshness judgment.

## Why People Are Using It

Run daily on the author's production software stack; presented as the piece "most
people skip." The decisions/ quadrant matches long-standing ADR practice (and the
engine's own DD system); the lifespan framing extends it to the whole docs surface.

## Potential Alternatives

Diátaxis-style type-based splits (tutorial/how-to/reference/explanation — see the
BMAD finding) organize by reader intent, not truth-lifespan; the two can compose
(lifespan outer, type inner). Frontmatter status fields (status: done) encode the
same signal in metadata instead of location — but agents must be told to check the
field, whereas location gates what gets read at all.

## Potential Improvements

Automated lifecycle sweeps: flag active/ documents untouched for N weeks as
archive candidates. Stamp templates so "do not follow" is uniform and
router-recognizable.

## Potential Failure Modes

The transition is manual — forgetting to move a shipped plan reproduces exactly the
failure the structure exists to prevent (structure without habit is dead weight).
Over-archiving working references by lifespan-misclassification makes the agent
re-derive facts that were still true.
