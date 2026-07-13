---
name: "Behavior Evals Externalized to Real-Session LLM-Judged Harness Runs"
summary: |-
  Plain English: if skills are code that shapes agent behavior, test them like code —
  in a separate eval repo that runs REAL harness sessions (actual tmux sessions of
  Claude Code / Codex executing the skills) and judges the transcripts with an LLM
  verifier, and require before/after eval evidence on any PR that changes skill
  content. Superpowers moved its behavior tests to a dedicated `superpowers-evals`
  repo using a "drill" framework; in-tree tests retain only plugin infrastructure.
  The externalization was itself failure-driven: the evals submodule briefly shipped
  inside v6.0.0 and was removed in v6.0.2 because it broke plugin installs. The v6.0.0
  SDD rewrite shipped with published eval results (~2x faster, ~50% fewer tokens at
  similar quality) — behavior changes argued with evidence, not taste.
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
  - file: "two-layer-ci-plus-llm-review-gate.md"
    rel: "same-problem"
  - file: "eval-rubric-carve-outs-subjective-and-script-core-skills.md"
    rel: "same-problem"
  - file: "unified-dual-verdict-reviewer.md"
    rel: "enables"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "evaluation"
  - "skill-testing"
  - "behavior-evals"
---

# Behavior Evals Externalized to Real-Session LLM-Judged Harness Runs

## What It Is

An eval architecture for instruction content, with three commitments:

1. **Real sessions, not unit fixtures.** The "drill" framework runs actual harness
   sessions (tmux-driven Claude Code and Codex) executing the skills under test, then
   judges compliance from the transcript with an LLM verifier. What is tested is the
   behavior the skill produces in the deployed environment, not string properties of
   the skill file.
2. **Externalized repo.** Behavior evals live in a separate `superpowers-evals` repo;
   the product repo's `tests/` covers only plugin infrastructure. The split is
   pragmatic, not aesthetic — shipping the evals submodule inside the plugin broke
   installs (v6.0.0 → removed v6.0.2) and eval dependencies/runtime don't belong in
   the distributed artifact.
3. **Eval-gated content changes.** Skill-content PRs require before/after eval
   evidence ("skills are code that shapes agent behavior"); the v6.0.0 review-
   architecture rewrite was justified with published eval numbers.

## Why It Matters

Prompt and skill changes are the largest untested surface in most agentic systems —
edited on intuition, verified by vibes, regressed silently. This is a worked example of
closing that gap with the same discipline code gets: a test harness that exercises the
real thing, a merge gate that demands evidence, and an infrastructure boundary that
keeps eval weight out of the shipped artifact. The real-session choice is the expensive
but honest half: skills fail through harness interaction (discovery, injection,
compaction), which fixture-based tests never see.

## Why People Are Using It

Adopted by a widely-installed multi-harness skill framework whose behavior content is
its entire product; the eval gate is written into its contributor governance
(CLAUDE.md). Source: Observed in
[superpowers](https://github.com/obra/superpowers) v6.1.1 — see
[[superpowers-analysis]] for structural details.

## Potential Alternatives

- **Two-layer CI (deterministic checks + LLM review of diffs)** — cheaper, catches
  structural regressions; never observes actual behavior.
- **In-repo eval suites** — simpler wiring; couples eval dependencies to the shipped
  artifact (the exact failure observed).
- **Dogfooding as testing** — maintainers using the skills daily; real sessions but no
  controlled comparisons or regression detection.

## Potential Improvements

- Cross-harness eval matrices (same drill, every supported harness) to catch
  harness-specific behavior drift — the vendor-neutral architecture makes this
  tractable.
- Cost management: real-session evals are expensive; selective triggering by content
  diff would keep the gate affordable.

## Potential Failure Modes

- **LLM-judge noise** — verifier verdicts vary; flaky behavior evals train
  maintainers to override the gate.
- **Eval-repo drift** — externalization means the evals can lag the skills they test;
  the gate is only real if CI actually runs the external suite per PR.
- **Session nondeterminism** — real harness runs differ run-to-run; distinguishing a
  regression from variance needs repetition budgets.
