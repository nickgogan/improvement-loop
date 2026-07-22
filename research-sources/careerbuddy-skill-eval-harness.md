---
name: CareerBuddy Skill-Eval Harness — meta-skill-eval, eval-cases schema, pass-rate ledger, MV46-MV48 design docs
source_type: "Repository"
status: Done
key_takeaways: CareerBuddy turned its document-only eval governance into an execution layer — a dedicated harness skill (meta-skill-eval) that runs per-skill structured eval-cases (trigger/execution/retirement tiers) through the real agent CLI in isolated per-trial contexts, appends fully-attributed rows (model, skill version, eval-set version, harness version, effort) to an append-only pass-rate ledger, checks eval sets against a live-capture phrasing corpus deterministically, and closes the subjective loop with typed human-score rows. Operator rulings from live runs — bias assertions as far toward deterministic checks as possible; no LLM judge until human-scored rows validate one; pure tool-wrapper skills excluded from paid runs — plus selective SkillsBench adoption (paired output uplift, typed failure taxonomy, oracle-validates-the-verifier). Notably, its research pass mined this engine's own published KB (guides, patterns, rules), making the corpus-contribution channel bidirectional.
relevance: High
added_by: Nick
tags: [skill-evals, eval-harness, pass-rate-ledger, model-provenance, corpus-drift, retirement, trigger-evals, careerbuddy]
url: https://github.com/nickgogan/CareerBuddy (.github/skills/meta-skill-eval/, system/plans/skill-eval-harness.md, system/ops/research/2026-07-20-skill-eval-sophistication.md, onboarding/manual/eval-harness.md)
authority: []
findings:
- attributed-pass-rate-ledger-with-model-provenance.md
- corpus-drift-sync-for-eval-sets.md
- llm-judge-calibration-activation-guard.md
- typed-output-failure-taxonomy-and-oracle-verifier-check.md
- paired-output-uplift-distinct-from-retirement-signal.md
date_added: '2026-07-22'
date_processed: '2026-07-22'
date_published: '2026-07-21'
---

# CareerBuddy Skill-Eval Harness — meta-skill-eval + eval-system design corpus

The skill-eval execution layer of CareerBuddy (Nick's single-agent cross-platform
system), intaken as a primary source for the engine's queue item 2
(eval sophistication). The corpus comprises: the `meta-skill-eval` harness skill
v2.0.0 (four modes — run / report / sync / score — around a single Python runner
driving the agent CLI as a subprocess, deny-by-default sandboxing, 3-trial default,
transcript-derived verdicts only); the structured `eval-cases.yaml` schema every
skill ships (should- and should-not-trigger cases with `expect_instead`, per-mode
Given/When/Then execution cases with positive and negative assertions); the
append-only attributed pass-rate ledger with capability→regression graduation,
saturation, and retirement labels; the MV46 design plan (harness options weighed —
microsoft/waza rejected with reasons — and operator rulings from first live runs:
model-policy with per-band effort pinning, deterministic-bias case authoring,
`harness: excluded` carve-out for pure tool-wrappers); and the 2026-07-20
skill-eval-sophistication research report (four-source convergence + SkillsBench /
LangChain / Anthropic / Hamel delta pass with explicit adopt/defer dispositions).

Two-way channel evidence: the research pass mined `nickgogan/improvement-loop`
(this engine's published mirror) for its eval guides, patterns, and rules — some of
which this engine had itself originally mined from CareerBuddy (the class carve-outs
rule). Both packages were imported into the engine 2026-07-22 (meta-skill-author
upstream sync 1.15.0→1.20.0; meta-skill-eval backend-ported to the Claude Code
CLI) — see the packages' ADAPTATION.md files.

Five findings extracted (dedup-aware: three-tier testing, grading hierarchy,
generator-assessor separation, and class carve-outs already exist in this KB and
are extended by cross-link, not duplicated).
