---
name: "Ponytail"
type: "watched-library"
repo_url: "https://github.com/DietrichGebert/ponytail"
description: |-
  Claude Code plugin that enforces a lazy-senior-dev token economy — YAGNI + code-reuse
  decision ladder before any code is written, diff review for over-engineering, and
  measured with/without deltas; vendor-claimed cuts up to 94% on over-build cases
spectrum_position: "evaluating"
what_we_use: |-
  Nothing adopted yet — evaluation candidate. The technique layer is already in the KB
  (seven-rung minimal-code decision ladder, on-demand vs always-on activation, measured
  delta + staging clone for AI refactors); the plugin itself is a candidate for the
  Reviewer/Gate role in the engine's planned standard coding-agent loop
local_derivations: []
last_evaluated_version: "v4.8.4 (2026-06-29)"
last_evaluated_date: "2026-07-12"
maintainer: "DietrichGebert"
status: "active"
tags:
  - "claude-code"
  - "skills"
  - "token-economy"
  - "code-review"
  - "yagni"
related_findings:
  - "seven-rung-minimal-code-decision-ladder.md"
  - "on-demand-vs-always-on-skill-activation.md"
  - "measured-delta-and-staging-clone-for-ai-refactors.md"
related_sources:
  - "claude-code-cuts-token-usage-by-94-percent.md"
  - "make-fable-5-80-percent-cheaper.md"
date_added: "2026-07-12"
---

## What It Does

Claude Code plugin (MIT, JavaScript, ~81.3k stars as of 2026-07-12, v4.8.4 released
2026-06-29) that makes the agent "think like the laziest senior dev in the room." Core
mechanism is a decision ladder evaluated before writing any code: does the feature need to
exist (YAGNI) → does it already exist in the codebase → stdlib → native platform feature →
installable dependency → one-line fix → only then minimal new code. Commands: `/ponytail`
(lite | full | ultra | off intensity levels), `/ponytail-review` (audit a diff for
over-engineering), `/ponytail-audit` (scan the whole repo), `/ponytail-debt` (collect
deferred shortcuts), `/ponytail-gain` (display measured with/without deltas). Benchmark
claims are vendor-published: up to 94% less code on single-shot over-build cases (the
date-picker example), 54% average LOC reduction (agentic baseline, n=12), tested on
Claude Haiku 4.5 only.

## What We Use From It

Nothing adopted yet. The technique behind the plugin is already extracted as findings —
the seven-rung minimal-code decision ladder, the on-demand-over-always-on activation
discipline (subcommands instead of a permanent system-prompt override, to avoid polluting
other skills), and measured-delta verification with a staging clone for risky AI-driven
refactors. What remains under evaluation is the plugin itself as a running component.

## Spectrum Rationale

Evaluating, not study: there is concrete adoption intent. **Nick (2026-07-12):** he
expects Ponytail to become part of a standard coding-agent loop the engine will create,
playing the Reviewer/Gate agent role — the diff-review/audit surface (`/ponytail-review`,
`/ponytail-audit`) gating what the builder agents produce. Held at evaluating rather than
cherry-pick because the benchmarks are vendor-claimed and Haiku-4.5-only (one
independent-ish corroboration in the KB via the "Make Fable 5 80% Cheaper" source);
promotion needs an on-our-workload delta measured with `/ponytail-gain` or equivalent.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-12 | v4.8.4 | Initial entry, Nick-approved (session 137). Repo verified via GitHub API: 81,260 stars, MIT. Nick expectation recorded: Reviewer/Gate role in the engine's planned standard coding-agent loop. |
