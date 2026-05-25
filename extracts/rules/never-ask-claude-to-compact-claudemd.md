---
title: "Evolving Load-Bearing Documents: No In-Place LLM Rewrite + Delta-Update Discipline"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "catastrophic-context-collapse-risk-during-claudemd"
contributing_sources:
  - ace-delta-updates-over-monolithic-rewrites
identification_report: "managing-agent-context.harvest-queue.md::catastrophic-context-collapse-risk-during-claudemd::rule::never-ask-claude-to-compact-claudemd"
extraction_date: "2026-04-27"
last_change_session: 103
last_change_sl: "session-103-codifier-complete-extract-artifacts-write-phase"
deployed: false
deployed_to: null
context:
  applies_to:
    - "any project that maintains a load-bearing evolving document consumed by an LLM-driven agent (CLAUDE.md, AGENTS.md, .cursorrules, system-prompt files, PROGRESS.md, playbooks, accumulated notes)"
    - "evolving documents where rule-loss or detail-loss has cumulative cost (each entry was added because of a past failure, learned constraint, or accumulated session signal)"
    - "AI-assisted workflows where the same load-bearing document is reused or extended across many sessions"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — once a context file is collapsed in place, prior content is lost unless version control had captured it pre-collapse; rolling back requires either git history or out-of-band backup"
  auditability: "high when version control captures context file changes (git diff before/after) and a session log records compaction-style invocations; medium when tracked manually; low when relied on by convention"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-tested through painful incidents. Practitioner-documented failure mode where post-collapse accuracy drops to ~57% of pre-collapse, often below the baseline of having no context file at all (because a sparse, inaccurate summary actively misleads the model)."
contract:
  preconditions: "A project maintains a load-bearing context file consumed by an LLM-driven agent (CLAUDE.md, AGENTS.md, system-prompt file, or equivalent). The context file accumulates rules over time, each typically added in response to a learned constraint. The model that consumes the context file has the technical capability to be invoked against the file itself (read its own context file as a target for summarization or rewriting)."
  invariants: "The model is never invoked to summarize, compact, condense, or rewrite a load-bearing evolving document in place. Compaction-style operations on such documents are performed by mechanisms whose failure mode is bounded — version-controlled diff review, ACE-style delta-update curation (append structured deltas, periodic non-LLM consolidation, grow-and-refine merge logic, multi-epoch refinement), /clear-then-rebuild from a frozen prior state, or human edit. The document is under version control with snapshots taken before any structural change so any in-place mutation is reversible. Sessions detect suspiciously-short load-bearing documents at start (compared to git history) and surface a warning. When the document needs to evolve, mutation occurs via append-then-consolidate (delta-updates), not via LLM-driven full rewrite."
  governance: "Owner: any policy or skill that touches the context file as a write-target. The rule must be embedded as a hard prohibition in: (a) skill definitions that operate on context files (no skill invokes the model with the context file as a summarization target); (b) session-start checks that compare current context file size to git-history baselines and flag collapse-shaped regressions; (c) project-policy documents that mention context-file maintenance. Audit verifies no compaction-style invocations have run against context files; verifies version-controlled snapshots exist; verifies bounded-failure-mode mechanisms (ACE, /clear-rebuild, human edit) are the only paths to reduce file size."
  recovery: "If a context file collapse is detected within the session: revert immediately from version control; investigate which invocation triggered the collapse; remove or amend the triggering pattern. If a collapse went unnoticed and propagated to subsequent sessions: revert from the last verified-good snapshot; treat all sessions between collapse and detection as having operated on a poisoned context (their outputs may need re-validation). If the file legitimately needs to shrink (genuine bloat, stale rules): use ACE-style voting curation, /clear-then-rebuild from explicit notes, or human edit — never an in-place model rewrite. If git history is unavailable and a collapse occurred: rebuild the context file from project artifacts (DDs, system log, prior commits' surrounding code) rather than trusting the collapsed version."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "claudemd"
  - "compaction"
  - "catastrophic-failure"
  - "ace"
  - "delta-updates"
  - "evolving-docs"
---

# Evolving Load-Bearing Documents: No In-Place LLM Rewrite + Delta-Update Discipline

**Source:** [[catastrophic-context-collapse-risk-during-claudemd]]
**Contributing source:** [[ace-delta-updates-over-monolithic-rewrites]] (delta-update mechanism + scope generalization, session 84)
**Source (additional):** [[write-time-vs-query-time-synthesis-kb-poisoning]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A project maintains a load-bearing evolving document consumed by an LLM-driven agent — including but not limited to CLAUDE.md, AGENTS.md, system-prompt files, `PROGRESS.md`, playbooks, accumulated session notes, or any other document that accrues operational signal over time. The document accumulates rules, constraints, decisions, or session deltas, each typically added in response to a learned failure, governance need, or session outcome. A team member or skill is contemplating "compacting," "summarizing," or otherwise rewriting the document in place because it has grown — OR is contemplating how to update the document as it continues to accumulate content.

Scope of application: any evolving load-bearing document whose loss-of-content has non-trivial cost. This explicitly includes **accumulated knowledge indices and search layers** — KB finding files, indexed source catalogs, and retrieval-layer artifacts where LLM-reprocessing introduces write-time synthesis poisoning (see [[write-time-vs-query-time-synthesis-kb-poisoning]]). Does not apply to ephemeral session notes, scratchpad memory, or files that are explicitly designed to be rebuilt from sources.

## Action

**Required (negative-space — no in-place LLM rewrite):** Compact, condense, or restructure a load-bearing evolving document only via mechanisms whose failure mode is bounded — version-controlled diff review with human approval, ACE-style delta-update curation (specified in the next subsection), `/clear`-then-rebuild from explicit notes, or direct human edit. Always snapshot to version control before any structural change. At session start, compare the current document size to its git-history baseline and surface a warning if it appears suddenly compressed.

**Required (positive-space — delta-update mechanism):** When the document needs to evolve, prefer the delta-update path:

1. **Append structured delta entries.** New rules, decisions, session signals, or rule refinements are appended as discrete entries with their own structural anchor (date, session, source, type). Each entry is independently citable and revertable.
2. **Periodic non-LLM consolidation.** Consolidation passes are performed by lightweight deterministic logic (or human edit) — never by invoking an LLM as the merge mechanism. Deterministic merge avoids brevity-bias detail loss; the merge preserves every entry's source attribution and rationale.
3. **Grow-and-refine.** Manage expansion and redundancy by merging or pruning entries based on explicit semantic-similarity rules (deterministic) or human review. The grow-and-refine pass is itself a deterministic operation; LLM input may be solicited as advisory but never as the writer.
4. **Multi-epoch refinement.** The same content can be revisited across sessions to progressively strengthen or rebalance entries — each pass is additive (a new delta entry) rather than rewriting prior entries in place.

The delta-update mechanism is the *named, specified* alternative to LLM-driven rewrite. Voting curation, /clear-rebuild, and human edit remain valid bounded-failure alternatives but are coarser; delta-update is the canonical evolving-document discipline.

**Forbidden:** Invoking the model with the document as a summarization, condensation, or rewrite target — for example, "summarize this CLAUDE.md," "compact PROGRESS.md," "rewrite this playbook for clarity," or any prompt whose response is intended to be the new document content. Even with careful framing, the LLM has a small-but-fixed per-attempt probability of catastrophically collapsing the document to a sparse summary (cumulative probability across attempts), AND every LLM-driven rewrite is subject to brevity bias that silently drops domain-specific details — even when no catastrophic collapse occurs. Each LLM rewrite either succeeds with subtle detail loss (silent erosion) or destroys accumulated content entirely (catastrophic collapse).

## Boundary

Enforced wherever a load-bearing evolving document can be written. Applies to interactive sessions, automated maintenance scripts, scheduled compaction jobs, and skill definitions that touch evolving documents as write-targets — including CLAUDE.md/AGENTS.md/system-prompt files, PROGRESS.md, playbooks, and accumulated notes.

Out of scope: read-only model interactions with the document (loading it as input, querying it for information without writing back). The rule fires only when the model's output is intended to replace or modify the document in place.

## Enforcement

- **Mechanism:** A pre-commit hook or skill-level check rejects invocations that pass the context file as a summarization-style argument to the model. Session-start hooks compare current context file size to its git-history high-water mark; significant unexplained shrinkage triggers a warning. Skill definitions that touch context files declare their write-mechanism explicitly (must be one of: ACE-style voting, /clear-rebuild, human edit, version-controlled diff approval).
- **Check (deterministic):** For every write `W` to the context file: `W.mechanism in {ACE-voting, clear-rebuild, human-edit, diff-approval}` AND `pre_W_snapshot_in_version_control == true`. For every session start: `current_file_size >= git_history_p10_size` (where p10 is the 10th-percentile size over recent history; a file below p10 may be a collapse). Any branch false → write blocked or warning surfaced.
- **Violation response:**
  - *Compaction-style invocation attempted:* block at the skill or hook level; surface the rule's reasoning; offer the bounded-failure alternatives.
  - *Collapse detected at session start:* surface a high-visibility warning; offer revert-from-git as the first action; do not proceed with the session until the user explicitly acknowledges the file's current state.
  - *Collapse detected mid-session:* revert from version control; investigate the triggering invocation; if no version control was in place, treat the file as poisoned and rebuild from project artifacts.
  - *Bounded-failure mechanism produced unintended shrinkage:* the mechanism is itself the unit of failure-handling — ACE voting that produces low-stability output is rejected; /clear-rebuild that produces a thin file is the user's edit; treat each mechanism's failure on its own terms.
- **Cannot be silently exempted:** "I'll compact carefully this once" is the failure path. The rule does not require zero context-file maintenance; it requires that maintenance use bounded-failure mechanisms.

## Rationale

The rule exists because LLM-driven full-document rewrite has TWO failure modes — one catastrophic, one subtle — and both compose at the corpus level.

**Catastrophic collapse** is the unbounded failure mode for full-document rewrites of context-shaped files (CLAUDE.md, AGENTS.md). Most compaction attempts succeed. A small-but-fixed fraction collapse the file to a sparse summary that is *worse than no context at all* — because a sparse-and-inaccurate summary actively misleads the model, dropping accuracy below the no-context baseline. The cumulative probability is the structural problem: a 3% per-attempt collapse rate (with each subsequent compaction increasing the rate by 0.25%) means a team that compacts every few weeks will eventually collapse — guaranteed, just not on any particular day. The failure is silent: the team continues with a poisoned context without knowing why output quality dropped.

**Brevity-bias detail loss** is the parallel failure mode that fires on every LLM-driven rewrite, not just catastrophic ones. Even when collapse doesn't occur, the LLM's brevity prior silently drops domain-specific details — operational nuances, session context, edge-case rules — in favor of concise summaries. This failure compounds across iterations: each rewrite preserves the ~80% of content that "feels important" and silently elides the rest. After several iterations, the document is half its original information density even though no single rewrite "broke" anything visibly. The ACE finding's metric — 86.9% lower adaptation latency and 83.6% lower rollout cost when delta-updates are used instead — quantifies how costly the rewrite path is even at non-catastrophic baselines.

The bounded-failure alternatives change the risk profile. Version-controlled diff review surfaces collapse before commit. ACE-style delta-update curation eliminates LLM-driven merge entirely (the merge logic is deterministic, not LLM-driven). `/clear`-then-rebuild starts from explicit notes, not from the LLM's interpretation of the current file. Human edit has the same risk profile as any human edit. None of these have the unbounded LLM-rewrite failure.

The rule is the positive-space restatement of the LLM-rewrites-evolving-document anti-pattern. Rather than enumerating ways failure manifests (sudden file shrinkage, accuracy drops post-rewrite, silent detail loss across iterations, mysterious agent regression), the positive invariant is "load-bearing evolving documents are written only by bounded-failure mechanisms — the canonical mechanism is delta-update curation; the LLM never rewrites the document in place." One rule, deterministic enforcement, broad scope.

### Additional Evidence

The write-time vs query-time synthesis finding ([[write-time-vs-query-time-synthesis-kb-poisoning]]) extends the no-LLM-reprocessing invariant to knowledge base write-time synthesis poisoning. When LLM-authored content (summaries, concept articles, cross-references) is re-indexed into a KB alongside source documents, unverifiable information enters the retrieval corpus. Subsequent LLM responses reason from prior LLM outputs rather than originals — circular reinforcement disconnected from ground truth. A vendor contract specifying "net 30, 2% discount within 10 days" becomes "standard net-30 terms with early-payment discounts" after write-time synthesis: the specifics are gone and cannot be recovered from the summary. This is the same failure mode as CLAUDE.md brevity-bias detail loss, applied to accumulated knowledge indices and search layers. The three principles the finding establishes — immutable originals, structure over prose, query-time synthesis — are the KB-layer analog of this rule's delta-update discipline: extracted structure (not LLM-authored narrative) serves as the navigation layer; synthesis happens at query time from originals, not at write time from prior LLM responses.

## Failure Modes

- **"It worked last time."** The team has compacted N times successfully and concludes the rule is overkill. Mitigation: cumulative probability is the structural property; the rule's value is that you never find out you were the next failure until you are. Rolls of the dice add up.
- **Bounded-failure mechanism becomes ceremony.** ACE voting or /clear-rebuild is treated as bureaucracy; people skip to direct LLM compaction "for speed." Mitigation: the mechanisms exist to bound failure, not slow work; if they feel slow, optimize the mechanism, do not relax the rule.
- **Subtle compaction via unrelated invocations.** A general "clean up my project" prompt asks the model to also tidy CLAUDE.md, sneaking compaction into a non-compaction request. Mitigation: any model-driven write to the context file is compaction regardless of how the prompt was phrased; the check fires on the write target, not the prompt intent.
- **Version control gaps.** The context file is not under version control, or snapshots before structural changes aren't taken. Mitigation: version control is a precondition for the rule's recovery path; treat lack of version control as a separate violation that has to be fixed before the rule can be safely enforced.
- **Session-start false-positive warnings.** Legitimate human edits trigger collapse warnings. Mitigation: the warning is informational; humans acknowledge or dismiss it; the warning's value is catching silent collapse, not preventing legitimate edits.
- **Cross-tool compaction.** A separate AI tool is asked to compact the context file (claiming the rule only applies to one model). Mitigation: the rule is about context-file-as-LLM-write-target regardless of which model writes it; cross-tool LLM compaction has the same failure mode.
- **Brevity bias on smaller-than-collapse rewrites.** Even when the LLM doesn't catastrophically collapse, brevity bias silently drops domain-specific details across iterations — the document's information density quietly halves over several "successful" rewrites. Mitigation: delta-update is the structural alternative; never invoke LLM as the merge mechanism, even when the rewrite is framed as "small" or "tidy-up." The deterministic-merge path eliminates this failure mode by construction.
- **"Just consolidate it for me" framing.** A user invokes the model to consolidate accumulated delta entries (e.g., "merge these PROGRESS.md session entries into a clean summary"). Mitigation: consolidation is a bounded-failure operation only when the merge logic is deterministic — i.e., human edit, scripted merge, or ACE-style voting curation with stability check. LLM-driven consolidation re-introduces brevity bias; framing it as "consolidate" instead of "compact" doesn't change the failure mode.

## Contract

### Preconditions
A project maintains a load-bearing context file consumed by an LLM-driven agent (CLAUDE.md, AGENTS.md, system-prompt file, or equivalent). The context file accumulates rules over time, each typically added in response to a learned constraint. The model that consumes the context file has the technical capability to be invoked against the file itself (read its own context file as a target for summarization or rewriting).

### Invariants
The model is never invoked to summarize, compact, condense, or rewrite a load-bearing evolving document in place. Compaction-style operations on such documents are performed by mechanisms whose failure mode is bounded — version-controlled diff review, ACE-style delta-update curation (append structured deltas, periodic non-LLM consolidation, grow-and-refine merge logic, multi-epoch refinement), /clear-then-rebuild from a frozen prior state, or human edit. The document is under version control with snapshots taken before any structural change so any in-place mutation is reversible. Sessions detect suspiciously-short load-bearing documents at start (compared to git history) and surface a warning. When the document needs to evolve, mutation occurs via append-then-consolidate (delta-updates), not via LLM-driven full rewrite.

### Governance
Owner: any policy or skill that touches the context file as a write-target. The rule must be embedded as a hard prohibition in: (a) skill definitions that operate on context files (no skill invokes the model with the context file as a summarization target); (b) session-start checks that compare current context file size to git-history baselines and flag collapse-shaped regressions; (c) project-policy documents that mention context-file maintenance. Audit verifies no compaction-style invocations have run against context files; verifies version-controlled snapshots exist; verifies bounded-failure-mode mechanisms (ACE, /clear-rebuild, human edit) are the only paths to reduce file size.

### Recovery
If a context file collapse is detected within the session: revert immediately from version control; investigate which invocation triggered the collapse; remove or amend the triggering pattern. If a collapse went unnoticed and propagated to subsequent sessions: revert from the last verified-good snapshot; treat all sessions between collapse and detection as having operated on a poisoned context (their outputs may need re-validation). If the file legitimately needs to shrink (genuine bloat, stale rules): use ACE-style voting curation, /clear-then-rebuild from explicit notes, or human edit — never an in-place model rewrite. If git history is unavailable and a collapse occurred: rebuild the context file from project artifacts (DDs, system log, prior commits' surrounding code) rather than trusting the collapsed version.
