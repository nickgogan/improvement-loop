---
title: "Extension Proposal — claudemd-global-rule-cap → claudemd-minimum-viable-rule-only-add-globally-true-lines"
type: "extension-proposal"
target_system: "improvement-loop"
proposed_during: "session-82"
proposed_during_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
candidate_finding: "claudemd-context-rot-from-indiscriminate-rule-accu"
candidate_form: "rule"
candidate_headline: "claudemd-global-rule-cap"
candidate_harvest_row: "managing-agent-context.harvest-queue.md::claudemd-context-rot-from-indiscriminate-rule-accu::rule::claudemd-global-rule-cap"
primary_match_artifact: "claudemd-minimum-viable-rule-only-add-globally-true-lines.md"
primary_match_form: "rule"
status: "applied"
ruling: "Option A — merge as extension"
ruling_session: 84
ruling_session_sl: "session-84-codifier-reconcile-and-dd97-sweep"
applied_to: "claudemd-minimum-viable-rule-only-add-globally-true-lines"
governance: "DD-97 (calibration LLM-loose; propose-don't-decide invariant; auto-merge prohibition — Nick rules per proposal; this skill never auto-merges)"
date: "2026-04-27"
---

# Extension Proposal — claudemd-global-rule-cap

## Summary

Candidate rule `claudemd-global-rule-cap` (sourced from finding [[claudemd-context-rot-from-indiscriminate-rule-accu]]) overlaps with existing rule [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]. Both target CLAUDE.md bloat / context rot. The mechanisms are related but distinct, which raises the question: should the candidate be drafted as a standalone artifact, OR should it merge into the existing rule as a second enforcement mechanism (numeric cap as a structural backstop to the per-line global-truth test)?

This proposal recommends Nick rule. The skill does not auto-merge per DD-97.

## Existing Rule (Primary Match)

**Artifact:** [[claudemd-minimum-viable-rule-only-add-globally-true-lines]] (`extracts/rules/claudemd-minimum-viable-rule-only-add-globally-true-lines.md`)
**Source finding:** `claudemd-minimum-viable-rule-only-add-globally`
**Mechanism:** Per-line global-truth test. Before adding any line, apply the self-test: "Would I type this line into context manually at the start of nearly every coding session?" If no/sometimes → don't add.
**Stage:** specify (point of authorship)
**Enforcement surface:** at the moment a line is being added — a self-applied criterion or an audit when session-startup context utilization is unexpectedly high.

## Candidate Rule

**Source finding:** [[claudemd-context-rot-from-indiscriminate-rule-accu]]
**Source excerpt:** "As users add rules to CLAUDE.md each time something goes wrong, the file grows and loads in full at the start of every session. The accumulation of context noise gradually reduces instruction-following quality and increases hallucination rates... Keep CLAUDE.md to 3-5 globally true, universally relevant lines."
**Codifier's reading:** Imperative cap on CLAUDE.md global section; machine-enforceable via line-count check on the global Tier-0 section. The 60-80 line benchmark from Step 1 of the source guide is a softer band; the candidate rule names the harder Tier-0 cap (3-5 lines).
**Mechanism:** Numeric cap. Tier-0 (global): 3-5 lines. Tier-1 (per-project): 60-80 line band. Enforced as a line-count check, not a per-line quality test.
**Stage:** operate (ongoing volume monitoring)
**Enforcement surface:** at file-write time (rejects writes that exceed the cap) or as periodic audit (flags files past the cap).

## Overlap Analysis

| Dimension | Existing Rule | Candidate |
|-----------|---------------|-----------|
| Anti-pattern targeted | CLAUDE.md bloat / context rot | CLAUDE.md bloat / context rot |
| Mechanism | Per-line quality criterion | Numeric volume cap |
| When fired | Per addition (specify stage) | Per write or periodic audit (operate stage) |
| Detection signal | Line fails self-test | File line-count exceeds cap |
| Independent or layered | Independent — applies to each line | Layered — applies to total |
| Structural backstop | No (relies on operator discipline) | Yes (catches accumulated drift) |

Both are anti-bloat mechanisms. The candidate is a *backstop* to the existing rule: even if the per-line test is misapplied (operator slips, group disagreement, gradual relaxation), the cap catches accumulated drift.

## Three Possible Resolutions

### Option A — Merge as extension (recommended for review)

Amend the existing rule to include the numeric cap as a second enforcement mechanism. The merged rule would carry both:
- Per-line global-truth test (specify stage)
- Numeric cap (operate stage; Tier-0: 3-5 lines, Tier-1: 60-80 line band)

The merged rule's title might shift (e.g., "CLAUDE.md Anti-Bloat Discipline — Per-Line Test + Volume Cap"). The candidate's source finding would be added to the existing rule's frontmatter `source_finding` (or noted as a contributing source).

**Pros:** Single rule covering one anti-pattern; complementary mechanisms in one place; reduces rule-count fragmentation.
**Cons:** Larger artifact; per-line test and volume cap fire at different stages, which is mildly awkward to express in a single rule's stage field.

### Option B — Separate rule

Draft `claudemd-global-rule-cap` as an independent artifact. The existing rule covers the per-line test; the new rule covers the volume cap. The two cross-reference each other via `related_findings` or body-level `See also`.

**Pros:** Each rule has one mechanism, one stage, one enforcement surface — cleaner separation.
**Cons:** Two artifacts targeting the same anti-pattern; cross-reference burden; possible drift between them.

### Option C — Reject the candidate as redundant

Treat the candidate's volume-cap recommendation as inline guidance covered implicitly by the existing rule's per-line test (with strict application, lines stay few; the cap is descriptive of the test's outcome, not an independent mechanism). Mark the queue row as nick-dismissed.

**Pros:** Smallest artifact set; the existing rule, strictly applied, suffices.
**Cons:** Discards the structural backstop; in practice the per-line test alone has been observed to drift; the cap is an independent operate-stage signal that the per-line test misses.

## Recommendation

The Codifier recommendation is **Option A (merge as extension)** but the calibration here is genuinely LLM-loose; reasonable readers could prefer Option B or even Option C. Nick rules.

## Procedure for Application (per DD-97)

If Nick rules **Option A (merge)**: manually amend `extracts/rules/claudemd-minimum-viable-rule-only-add-globally-true-lines.md` to integrate the volume cap (the skill does not auto-merge per DD-97 v1; auto-merge is prohibited at Step 1.7). After the manual merge lands, re-invoke `/extract-artifacts --harvest-row managing-agent-context.harvest-queue.md::claudemd-context-rot-from-indiscriminate-rule-accu::rule::claudemd-global-rule-cap` (or via the IB-166-amended argument shape) so Step 4.8 flips the queue row Status to `extracted` and Resolution to `merged into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]`.

If Nick rules **Option B (separate)**: re-invoke `/extract-artifacts --harvest-row ...` against this row WITH the explicit ruling that no extension applies; the skill drafts and writes `claudemd-global-rule-cap.md` as a standalone artifact; Step 4.8 flips Status to `extracted` and Resolution to `extracted to [[claudemd-global-rule-cap]]`.

If Nick rules **Option C (dismiss)**: invoke `/extract-artifacts --harvest-dismiss managing-agent-context.harvest-queue.md::claudemd-context-rot-from-indiscriminate-rule-accu::rule::claudemd-global-rule-cap`; Step 4.8 Branch A flips Status to `nick-dismissed` and Resolution to `dismissed`.

## Status

**Applied 2026-04-27 (Session 84) — Option A.** Nick ruled Option A (merge as extension) on this proposal as part of the session-84 sweep ruling on three accumulated DD-97 Branch-C proposals. The existing rule [[claudemd-minimum-viable-rule-only-add-globally-true-lines]] was manually amended to add the volume-cap mechanism (Tier-0: 3-5 lines; Tier-1: 60-80 line band) as an operate-stage backstop alongside the per-line global-truth test. Frontmatter `last_change_session` bumped to 84; `last_change_sl` set to `session-84-codifier-reconcile-and-dd97-sweep`; `contributing_sources` field added pointing to the candidate finding. Queue row `managing-agent-context.harvest-queue.md::claudemd-context-rot-from-indiscriminate-rule-accu::rule::claudemd-global-rule-cap` flipped from `nick-approved` to `extracted` with Resolution `merged into [[claudemd-minimum-viable-rule-only-add-globally-true-lines]]`. Source finding `consumed_by[]` extended with the merged-into artifact.
