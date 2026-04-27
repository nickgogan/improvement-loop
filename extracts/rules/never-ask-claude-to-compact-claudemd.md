---
title: "Never Ask the Model to Compact Its Own Context File — Catastrophic-Collapse Prevention Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "catastrophic-context-collapse-risk-during-claudemd"
identification_report: "managing-agent-context.harvest-queue.md::catastrophic-context-collapse-risk-during-claudemd::rule::never-ask-claude-to-compact-claudemd"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "any project that maintains an LLM-readable context file (CLAUDE.md, AGENTS.md, .cursorrules, system-prompt files) as load-bearing input to coding agents"
    - "context files where rule-loss has cumulative cost (each rule was added because of a past failure or learned constraint)"
    - "AI-assisted workflows where the same context file is reused across many sessions"
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
  invariants: "The model is never invoked to summarize, compact, condense, or rewrite its own context file in place. Compaction-style operations on the context file are performed by mechanisms whose failure mode is bounded — version-controlled diff review, ACE-style voting curators, /clear-then-rebuild from a frozen prior state, or human edit. The context file is under version control with snapshots taken before any structural change so any in-place mutation is reversible. Sessions detect suspiciously-short context files at start (compared to git history) and surface a warning."
  governance: "Owner: any policy or skill that touches the context file as a write-target. The rule must be embedded as a hard prohibition in: (a) skill definitions that operate on context files (no skill invokes the model with the context file as a summarization target); (b) session-start checks that compare current context file size to git-history baselines and flag collapse-shaped regressions; (c) project-policy documents that mention context-file maintenance. Audit verifies no compaction-style invocations have run against context files; verifies version-controlled snapshots exist; verifies bounded-failure-mode mechanisms (ACE, /clear-rebuild, human edit) are the only paths to reduce file size."
  recovery: "If a context file collapse is detected within the session: revert immediately from version control; investigate which invocation triggered the collapse; remove or amend the triggering pattern. If a collapse went unnoticed and propagated to subsequent sessions: revert from the last verified-good snapshot; treat all sessions between collapse and detection as having operated on a poisoned context (their outputs may need re-validation). If the file legitimately needs to shrink (genuine bloat, stale rules): use ACE-style voting curation, /clear-then-rebuild from explicit notes, or human edit — never an in-place model rewrite. If git history is unavailable and a collapse occurred: rebuild the context file from project artifacts (DDs, system log, prior commits' surrounding code) rather than trusting the collapsed version."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "claudemd"
  - "compaction"
  - "catastrophic-failure"
---

# Never Ask the Model to Compact Its Own Context File — Catastrophic-Collapse Prevention Rule

**Source:** [[catastrophic-context-collapse-risk-during-claudemd]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A project maintains a load-bearing context file (CLAUDE.md, AGENTS.md, system-prompt file, or equivalent) that is consumed by an LLM-driven agent on every session. The file accumulates rules and constraints over time, each typically added in response to a learned failure or governance need. A team member or skill is contemplating "compacting" or "summarizing" the file because it has grown.

Scope of application: any context file whose loss-of-content has non-trivial cost. Does not apply to ephemeral session notes, scratchpad memory, or files that are explicitly designed to be rebuilt from sources.

## Action

**Required:** Compact the context file only via mechanisms whose failure mode is bounded — version-controlled diff review with human approval, ACE-style voting curation (multi-pass with stability check), `/clear`-then-rebuild from explicit notes, or direct human edit. Always snapshot to version control before any structural change. At session start, compare the current file size to its git-history baseline and surface a warning if the file appears suddenly compressed.

**Forbidden:** Invoking the model with the context file as a summarization or rewrite target — for example, "summarize this CLAUDE.md," "compact this for me," or any prompt whose response is intended to be the new file content. Even with careful framing, the LLM has a small-but-fixed per-attempt probability of catastrophically collapsing the file to a sparse summary, with cumulative probability across attempts. Each compaction either succeeds (small win) or destroys accumulated context entirely.

## Boundary

Enforced wherever the context file can be written. Applies to interactive sessions, automated maintenance scripts, scheduled compaction jobs, and skill definitions that touch context files as write-targets.

Out of scope: read-only model interactions with the context file (loading it as input, querying it for information without writing back). The rule fires only when the model's output is intended to replace or modify the context file in place.

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

The rule exists because LLM-driven compaction has an unbounded failure mode. Most compaction attempts succeed. A small-but-fixed fraction catastrophically collapse the file to a sparse summary that is *worse than no context at all* — because a sparse-and-inaccurate summary actively misleads the model, dropping accuracy below the no-context baseline.

The cumulative probability is the structural problem. A 3% per-attempt collapse rate (with each subsequent compaction increasing the rate by 0.25%) means a team that compacts every few weeks will eventually collapse — guaranteed, just not on any particular day. The failure is silent: the team continues with a poisoned context without knowing why output quality dropped.

The bounded-failure alternatives change the risk profile. Version-controlled diff review surfaces collapse before commit. ACE-style voting curators have a stability check (does the curated output match across passes?). `/clear`-then-rebuild starts from explicit notes, not from the LLM's interpretation of the current file. Human edit has the same risk profile as any human edit. None of these have the unbounded LLM-compaction failure.

The rule is the positive-space restatement of the model-summarizes-its-own-context anti-pattern. Rather than enumerating ways collapse manifests (sudden file shrinkage, accuracy drops post-compaction, mysterious agent regression), the positive invariant is "context file is written only by bounded-failure mechanisms; the LLM never summarizes itself in place." One rule, deterministic enforcement.

## Failure Modes

- **"It worked last time."** The team has compacted N times successfully and concludes the rule is overkill. Mitigation: cumulative probability is the structural property; the rule's value is that you never find out you were the next failure until you are. Rolls of the dice add up.
- **Bounded-failure mechanism becomes ceremony.** ACE voting or /clear-rebuild is treated as bureaucracy; people skip to direct LLM compaction "for speed." Mitigation: the mechanisms exist to bound failure, not slow work; if they feel slow, optimize the mechanism, do not relax the rule.
- **Subtle compaction via unrelated invocations.** A general "clean up my project" prompt asks the model to also tidy CLAUDE.md, sneaking compaction into a non-compaction request. Mitigation: any model-driven write to the context file is compaction regardless of how the prompt was phrased; the check fires on the write target, not the prompt intent.
- **Version control gaps.** The context file is not under version control, or snapshots before structural changes aren't taken. Mitigation: version control is a precondition for the rule's recovery path; treat lack of version control as a separate violation that has to be fixed before the rule can be safely enforced.
- **Session-start false-positive warnings.** Legitimate human edits trigger collapse warnings. Mitigation: the warning is informational; humans acknowledge or dismiss it; the warning's value is catching silent collapse, not preventing legitimate edits.
- **Cross-tool compaction.** A separate AI tool is asked to compact the context file (claiming the rule only applies to one model). Mitigation: the rule is about context-file-as-LLM-write-target regardless of which model writes it; cross-tool LLM compaction has the same failure mode.

## Contract

### Preconditions
A project maintains a load-bearing context file consumed by an LLM-driven agent (CLAUDE.md, AGENTS.md, system-prompt file, or equivalent). The context file accumulates rules over time, each typically added in response to a learned constraint. The model that consumes the context file has the technical capability to be invoked against the file itself (read its own context file as a target for summarization or rewriting).

### Invariants
The model is never invoked to summarize, compact, condense, or rewrite its own context file in place. Compaction-style operations on the context file are performed by mechanisms whose failure mode is bounded — version-controlled diff review, ACE-style voting curators, /clear-then-rebuild from a frozen prior state, or human edit. The context file is under version control with snapshots taken before any structural change so any in-place mutation is reversible. Sessions detect suspiciously-short context files at start (compared to git history) and surface a warning.

### Governance
Owner: any policy or skill that touches the context file as a write-target. The rule must be embedded as a hard prohibition in: (a) skill definitions that operate on context files (no skill invokes the model with the context file as a summarization target); (b) session-start checks that compare current context file size to git-history baselines and flag collapse-shaped regressions; (c) project-policy documents that mention context-file maintenance. Audit verifies no compaction-style invocations have run against context files; verifies version-controlled snapshots exist; verifies bounded-failure-mode mechanisms (ACE, /clear-rebuild, human edit) are the only paths to reduce file size.

### Recovery
If a context file collapse is detected within the session: revert immediately from version control; investigate which invocation triggered the collapse; remove or amend the triggering pattern. If a collapse went unnoticed and propagated to subsequent sessions: revert from the last verified-good snapshot; treat all sessions between collapse and detection as having operated on a poisoned context (their outputs may need re-validation). If the file legitimately needs to shrink (genuine bloat, stale rules): use ACE-style voting curation, /clear-then-rebuild from explicit notes, or human edit — never an in-place model rewrite. If git history is unavailable and a collapse occurred: rebuild the context file from project artifacts (DDs, system log, prior commits' surrounding code) rather than trusting the collapsed version.
