---
title: "Extension Proposal — evolving-docs-use-delta-updates → never-ask-claude-to-compact-claudemd"
type: "extension-proposal"
target_system: "improvement-loop"
proposed_during: "session-83"
proposed_during_sl: "session-83-codifier-ib164-resume-extract-artifacts"
candidate_finding: "ace-delta-updates-over-monolithic-rewrites"
candidate_form: "rule"
candidate_headline: "evolving-docs-use-delta-updates"
candidate_harvest_row: "managing-agent-context.harvest-queue.md::ace-delta-updates-over-monolithic-rewrites::rule::evolving-docs-use-delta-updates"
primary_match_artifact: "never-ask-claude-to-compact-claudemd.md"
primary_match_form: "rule"
status: "proposed"
governance: "DD-97 (calibration LLM-loose; propose-don't-decide invariant; auto-merge prohibition — Nick rules per proposal; this skill never auto-merges)"
date: "2026-04-27"
---

# Extension Proposal — evolving-docs-use-delta-updates

## Summary

Candidate rule `evolving-docs-use-delta-updates` (sourced from finding [[ace-delta-updates-over-monolithic-rewrites]]) overlaps with existing rule [[never-ask-claude-to-compact-claudemd]]. Both target the same anti-pattern: LLM-driven monolithic rewrite of an evolving load-bearing document. The mechanisms are related — the existing rule already names "ACE-style voting curation" as a bounded-failure alternative; the candidate rule IS the ACE delta-update mechanism specification, generalized beyond CLAUDE.md to PROGRESS.md, playbooks, and other evolving context documents.

This proposal recommends Nick rule. The skill does not auto-merge per DD-97.

## Existing Rule (Primary Match)

**Artifact:** [[never-ask-claude-to-compact-claudemd]] (`extracts/rules/never-ask-claude-to-compact-claudemd.md`)
**Source finding:** `catastrophic-context-collapse-risk-during-claudemd`
**Anti-pattern:** Invoking the model to summarize/compact/rewrite its own context file in place; cumulative-probability collapse risk.
**Mechanism (negative-space):** Forbid LLM-as-summarization-target writes to the context file.
**Permitted alternatives (already named in invariant):** Version-controlled diff review, ACE-style voting curators, /clear-then-rebuild from a frozen prior state, human edit.
**Scope:** "Any context file whose loss-of-content has non-trivial cost" — primarily CLAUDE.md / AGENTS.md / system-prompt files.
**Stage:** operate
**Enforcement surface:** Pre-commit hook or skill-level check rejecting compaction-style invocations; session-start size-vs-history check.

## Candidate Rule

**Source finding:** [[ace-delta-updates-over-monolithic-rewrites]]
**Source excerpt (queue):** "When context documents change over time (playbooks, progress files, accumulated notes), update incrementally — append structured entries, then periodically consolidate. Never rewrite the full document with an LLM, as brevity bias silently drops domain-specific details."
**Codifier's reading (queue):** Imperative directive ("never rewrite full document with an LLM"); machine-enforceable via a hook that detects whole-document rewrites of designated long-lived files (CLAUDE.md, PROGRESS.md, playbooks) and warns. Fits rule form. The Delta Update Entry template (already in this guide) is the companion structural artifact.
**Anti-pattern:** Same anti-pattern as the existing rule — LLM rewriting an evolving document in place, with brevity bias silently dropping domain-specific details.
**Mechanism (positive-space):** Prescribe delta-update discipline — append structured incremental entries; periodically consolidate via lightweight non-LLM merge logic; multi-epoch refinement via grow-and-refine.
**Scope:** Generalized beyond CLAUDE.md to ALL evolving load-bearing context documents — playbooks, PROGRESS.md, accumulated notes, agent context files.
**Stage:** operate
**Enforcement surface:** Hook detecting whole-document rewrites of designated long-lived files; the structural alternative is the Delta Update Entry template (already embedded in G2).

## Overlap Analysis

| Dimension | Existing Rule | Candidate |
|-----------|---------------|-----------|
| Anti-pattern targeted | LLM in-place rewrite of context file (cumulative-collapse risk) | LLM in-place rewrite of evolving document (brevity-bias detail loss) |
| Framing | Negative-space (forbid compaction-style invocations) | Positive-space (prescribe delta-update mechanism) |
| Mechanism | "Don't ask LLM to compact"; bounded-failure alternatives include ACE | "Append-then-consolidate" — IS the ACE delta-update spec |
| Scope | CLAUDE.md / AGENTS.md / system-prompt files | All evolving load-bearing docs (CLAUDE.md, PROGRESS.md, playbooks, notes) |
| Failure mode cited | Catastrophic collapse to sparse summary (~57% accuracy floor) | Brevity bias silently drops domain-specific details |
| Already cross-referenced? | Existing rule names "ACE-style voting curators" as a permitted alternative within its invariant | Candidate's mechanism IS that alternative, fully specified |
| Structural relationship | Negative-space prohibition with permitted-alternatives clause | Positive-space mechanism that fills one of the existing rule's permitted-alternative slots |

The two rules are duals on the same anti-pattern. The existing rule says "don't do X; X-alternatives include ACE-style voting." The candidate rule says "do ACE-style delta-update; never do X." They share the anti-pattern, share one mechanism reference (ACE), and differ in framing (negative vs positive space) and scope (CLAUDE.md-shaped files vs all evolving docs).

## Three Possible Resolutions

### Option A — Merge as extension (recommended for review)

Amend the existing rule [[never-ask-claude-to-compact-claudemd]] to:
1. Generalize its scope from "context files" (CLAUDE.md / AGENTS.md / system-prompt) to "load-bearing evolving documents" (adding PROGRESS.md, playbooks, accumulated notes).
2. Promote the "ACE-style voting curators" mention from a passing reference inside the invariant to a fully-specified positive-space sub-rule with the delta-update mechanism: append structured entries, periodic non-LLM consolidation, grow-and-refine merge logic, multi-epoch adaptation.
3. Update the title to reflect the broader scope, e.g., "Evolving Load-Bearing Documents — No In-Place LLM Rewrite + Delta-Update Discipline."
4. Add `ace-delta-updates-over-monolithic-rewrites` as a contributing source.

The merged rule would carry both the negative-space prohibition (do not invoke LLM to compact) and the positive-space prescription (use delta-updates as the canonical alternative). The existing "Permitted alternatives" list remains intact — delta-update becomes the *named, specified* alternative; voting/clear-rebuild/human-edit remain valid.

**Pros:** Single rule for one anti-pattern; combines negative-space prohibition with positive-space mechanism; eliminates rule-count fragmentation and cross-reference burden; reflects that the two findings co-cite each other in the KB graph (`enables` / `enabled-by`).
**Cons:** Larger artifact; the merged rule must distinguish CLAUDE.md-specific failure cases (catastrophic collapse, ~57% floor) from general evolving-doc failure cases (brevity-bias detail loss); risk of muddying the ContextSpec `applies_to` if scope generalization is sloppy.

### Option B — Separate rule

Draft `evolving-docs-use-delta-updates` as an independent artifact. The existing rule covers the negative-space prohibition for CLAUDE.md-shaped files; the new rule covers the positive-space delta-update mechanism for all evolving docs. The two cross-reference each other via `related_findings` and a body-level `See also` block.

**Pros:** Each rule has one mechanism, one framing, one primary anti-pattern angle — cleaner separation; preserves the existing rule's tight CLAUDE.md focus; the candidate stands as the canonical delta-update mechanism specification.
**Cons:** Two artifacts targeting the same anti-pattern; cross-reference burden; possible drift between them; consumers reading one rule may miss the complementary one.

### Option C — Reject the candidate as redundant

Treat the candidate's prescription as inline guidance covered by the existing rule's "permitted alternatives" clause (which already names ACE-style voting curators as an acceptable mechanism). Mark the queue row as nick-dismissed. The G2 guide already embeds the Delta Update Entry template inline as the structural companion.

**Pros:** Smallest artifact set; the existing rule plus the inline G2 template suffices; avoids generalizing the existing rule's scope.
**Cons:** The existing rule's reference to ACE is one phrase inside its invariant; consumers may not extract the operational mechanism (append-then-consolidate, grow-and-refine) from that single mention; the candidate rule names the mechanism with enough specificity that hooks and skill definitions can target it; the broader scope (PROGRESS.md, playbooks) is genuinely different from the existing rule's CLAUDE.md focus.

## Recommendation

The Codifier recommendation is **Option A (merge as extension)**. The two findings are explicit duals in the KB (`ace-delta-updates-over-monolithic-rewrites` lists `catastrophic-context-collapse-risk-during-claudemd` as `enables`, and the latter would naturally list the former as `enabled-by`). Merging produces a single rule that names the anti-pattern AND the canonical mechanism, with scope broadened to cover evolving-doc patterns generally. The calibration is LLM-loose; Option B is reasonable if Nick prefers tight per-rule scope.

Nick rules.

## Procedure for Application (per DD-97)

If Nick rules **Option A (merge)**: manually amend `extracts/rules/never-ask-claude-to-compact-claudemd.md` to (i) generalize scope to evolving load-bearing documents, (ii) add the delta-update mechanism as a named positive-space sub-rule, (iii) add `ace-delta-updates-over-monolithic-rewrites` to a contributing-sources field, (iv) update title if appropriate (the skill does not auto-merge per DD-97 v1; auto-merge is prohibited at Step 1.7). After the manual merge lands, re-invoke `/extract-artifacts --harvest-row managing-agent-context.harvest-queue.md::ace-delta-updates-over-monolithic-rewrites::rule::evolving-docs-use-delta-updates` so Step 4.8 flips the queue row Status to `extracted` and Resolution to `merged into [[never-ask-claude-to-compact-claudemd]]`.

If Nick rules **Option B (separate)**: re-invoke `/extract-artifacts --harvest-row ...` against this row WITH the explicit ruling that no extension applies; the skill drafts and writes `evolving-docs-use-delta-updates.md` as a standalone artifact; Step 4.8 flips Status to `extracted` and Resolution to `extracted to [[evolving-docs-use-delta-updates]]`.

If Nick rules **Option C (dismiss)**: invoke `/extract-artifacts --harvest-dismiss managing-agent-context.harvest-queue.md::ace-delta-updates-over-monolithic-rewrites::rule::evolving-docs-use-delta-updates`; Step 4.8 Branch A flips Status to `nick-dismissed` and Resolution to `dismissed`.

## Status

Pending Nick's ruling. Queue row remains `nick-approved` (per DD-101 Branch C); Resolution remains blank in the queue file pending merge or alternative resolution. This proposal is the audit-trail record of the extension scan.
