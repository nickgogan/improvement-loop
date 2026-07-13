---
name: "Skill Pruning Failure Modes — No-Op Deletion Test, Sediment, Duplication"
summary: |-
  Plain English: a bloated skill is a symptom, not the disease. Pocock's pruning pass names
  the three underlying failure modes and gives each a test. (1) Duplication — every part of
  the skill (including reference material) should have a single source of truth. (2)
  Sediment — accreted contributions on a shared doc that nobody feels brave enough to
  delete; the fix is structural (re-sort by branch, kill stale/irrelevant material dead).
  (3) No-ops — passages that appear to do something but don't change agent behavior; the
  test is the deletion test: "what would happen if you just deleted that paragraph?" If the
  agent would do it anyway from priors (e.g. "write a long detailed commit message"), the
  paragraph is a no-op and should go. No-ops are especially common in agent-written skills.
implementation_notes: |-
  Rubric-relevant for /assess-skill (a pruning axis): three binary-ish checks — duplicated
  content across skill files? sediment (material irrelevant to every branch, or stale)?
  no-op candidates (instructions restating model-default behavior)? The deletion test is
  cheap to run as a thought experiment during audit and empirically as an A/B. Nick-gated
  restructure Phase 2 decides substrate entry.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (assess-skill/design-skill substrate)"
  - "General"
adopted_in: []
sources:
  - "building-great-agent-skills-the-missing-manual.md"
related_findings:
  - file: "claudemd-as-signal-to-noise-problem-not-size-probl.md"
    rel: "same-problem"
  - file: "context-file-instruction-bloat-eth-zurich.md"
    rel: "same-problem"
  - file: "branch-analysis-externalization-rule-skill-reference.md"
    rel: "extends"
  - file: "tool-pruning-as-harness-maintenance.md"
    rel: "same-problem"
  - file: "skill-flattening-outcome-prose-over-step-files.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
  - "rules/deletion-test-for-no-op-instructions.md"
---

# Skill Pruning Failure Modes — No-Op Deletion Test, Sediment, Duplication

## What It Is

The pruning quarter of Pocock's skill checklist: massive skills are "usually a symptom of
something else going wrong," and the something-else comes in three named failure modes,
each with its own detection move:

1. **Duplication.** Every part of the skill — steps *and* reference material — should have
   a single source of truth. Watch for the same template or explainer covered in several
   places, including across reference files.
2. **Sediment.** The multi-contributor failure: people add their own material to a shared
   markdown file and "don't feel brave enough to delete and modify anyone else's," leaving
   accreted, often irrelevant or stale content. Remedy is structural first: check each
   addition against the skill's branches, move it to the right branch, or kill it dead if
   irrelevant or stale.
3. **No-ops.** Passages that appear to do something but don't influence behavior — common
   when an agent writes the skill. Detection is the **deletion test**: delete the
   paragraph mentally (or actually) and ask whether behavior would change. "Write a long
   detailed commit message" fails the test — the agent does that anyway from priors.

## Why It Matters

The KB already holds the *evidence* that context bloat degrades behavior (signal-to-noise
findings, ETH Zurich instruction-bloat) and the *budget* reasons to stay small (5K
post-compaction survival, per-token cost). This finding supplies the *audit taxonomy*: when
`/assess-skill` flags a skill as oversized, these three modes are the diagnosis menu, and
the deletion test is the only cheap, named procedure in the KB for distinguishing
instructions that earn their tokens from prior-restating filler. The no-op category also
connects to the meta-authoring-prior evidence: agent-written skills systematically produce
no-ops, so agent-authored artifacts deserve a harder deletion-test pass.

## Why People Are Using It

Pocock's answer to "how are your skills so small" is exactly these techniques — deletion
tests, leading-word compaction, no sediment, no irrelevance — applied across one of the
most-downloaded skill repos in circulation. Sediment is independently familiar to anyone
maintaining shared CLAUDE.md files; he names and operationalizes it.

## Potential Alternatives

Hard size caps (catch the symptom, not the cause). Periodic full rewrites (destroy
accumulated correctness along with sediment). Empirical A/B eval of every section
(rigorous but expensive; the deletion test is its cheap approximation).

## Potential Improvements

Automate the deletion test with with/without-section eval runs (pairs naturally with the
skill A/B baseline pattern already in the intake queue). A lint for prior-restating
phrases ("write clear code", "be thorough") as no-op candidates. Sediment dating: flag
sections untouched since N versions ago for review.

## Potential Failure Modes

- **False no-ops**: behavior that survives deletion under today's model may regress under
  a different model or in edge branches; the deletion test samples, it doesn't prove.
- **Over-pruning safety text**: hard constraints (security boundaries, gates) can look
  like no-ops precisely because they rarely bind — deleting them fails silently until the
  edge case arrives.
- **Sediment courage without governance**: "kill it dead" needs ownership rules on shared
  skills, or pruning wars replace sediment.

## Extraction Note — 2026-07-13
Extracted as **rule**: [[deletion-test-for-no-op-instructions]] in `extracts/rules/` (harvest-queue promotion, DD-101)
