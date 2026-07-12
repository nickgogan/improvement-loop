---
name: "Skill Popularity Is Not Skill Efficacy (177k-Star Skill Measured Worse)"
summary: |-
  Plain English: GitHub stars measure virality, not whether a skill helps — and the
  starkest data point yet says a wildly popular skill actively hurts. Kun Chen
  benchmarked a skill from the 177k-star "Android Skills" repo with Program Bench
  (end-to-end program-building eval) and measured +5% token usage with *worse* results.
  His rule of thumb: do not install any skill from the internet that claims to make your
  agent perform better but has published no rigorous evaluation of the claim. Two
  distinct risks compound: unvetted skills are a security surface (they can instruct the
  agent to run anything, leak keys/credentials), and even benign ones can degrade
  performance. "Their GitHub stars only tell you how popular they are, not whether they
  are actually helpful."
implementation_notes: |-
  Directly applicable to the engine's import path (e.g., the meta-skill-author import)
  and watched-libraries triage: popularity/star counts appear in our roster signals, and
  this finding says they carry zero efficacy information — require published eval
  evidence or run our own with/without baseline before adopting external skills. Candidate
  criteria-delta for /assess-skill intake of third-party skills.
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (skill imports, watched-libraries triage)"
  - "General"
adopted_in: []
sources:
  - "l8-principals-agentic-engineering-workflow.md"
related_findings:
  - file: "skill-security-audit-obligation.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

An adoption rule for third-party skills backed by a measured counterexample. The
measurement: a skill from a 177k-star repo, evaluated with Program Bench (agent builds
programs end-to-end), consumed 5% more tokens and produced worse results than no skill at
all. The diagnosis: most widely-shared skills "have not been rigorously evaluated and are
typically just some random guy who found something that worked for themselves and got it
to go viral" — often not even authored by the famous name attached to the repo. The rule:
no external skill claiming performance gains gets installed without published rigorous
evaluation (or a local eval of your own).

## Why It Matters

Skills are the primary distribution unit of agent capability right now, and the default
vetting signal — stars, virality, big-name association — is measurably uncorrelated with
value and can be anti-correlated. A skill is also always-consulted context (its
description) plus arbitrary instructions on invocation, so a bad one taxes every session
and can steer the agent worse than baseline. The security half is stricter still: skills
can instruct the agent to execute anything, so installation is a trust decision, not a
convenience.

## Why People Are Using It

Chen runs benchmarked evaluations (Program Bench) before adopting skills into a
production workflow shipping 40-50 changes/day; the same vet-before-adopt posture appears
in his tool-selection benchmarks (GitHub MCP vs CLI). The broader signal: skill
marketplaces are flooding with unevaluated artifacts, and practitioners with eval
infrastructure are starting to publish negative results.

## Potential Improvements

- A lightweight with/without A/B baseline as the minimum local eval before any skill
  import
- Efficacy metadata as a community norm: skills shipping their eval setup and results
  alongside the SKILL.md
- Extending the rule from skills to prompts, agents, and MCP servers — the same
  popularity/efficacy gap applies

## Potential Failure Modes

- One benchmark on one skill from one repo is thin grounds for the general claim — the
  direction is credible, the magnitude is anecdote
- Over-applied, the rule blocks genuinely useful skills whose authors simply never
  published evals; the remedy is running your own baseline, not blanket rejection
- Local evals can mismeasure: a skill can lose on a generic bench but win on the specific
  workflow it was written for
