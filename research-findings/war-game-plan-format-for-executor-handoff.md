---
name: War-Game Plan Format for Executor Handoff
summary: 'Plain English: our plans and handoffs describe the happy path; this format makes the plan

  itself carry the failure handling. Instead of a linear plan, the frontier model produces

  a war-game: every move states its expected observation (what you see if it worked), its

  most-likely failure signal, and the countermove; every fork gets an explicit trigger

  ("if you observe X, take route A"); assumptions recon could not resolve go to a

  blocked-variables ledger the human fills in; the document ends with abort conditions.

  The prompt also names the cheaper executor model that will run the brief so the war-game

  is tailored to that model''s documented behavior. Result: a cheaper model executes a

  pre-simulated decision tree instead of improvising when reality deviates.'
implementation_notes: 'P2: candidate enrichment for how the engine writes handoff and plan documents (via the

  pipeline, separately Nick-gated). Concrete deltas to consider: add expected-observation /

  failure-signal / countermove columns to plan steps; explicit abort conditions; a

  blocked-variables ledger replacing silent assumptions; name the executing

  model/agent so the plan is tailored to it. Demonstrated workflow: tasks/ + wargames/

  folders, success.md criteria file, ledger.md; bulk-draft all war-games in parallel

  ("draft all 10 before polishing any"), then loop-polish.'
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (handoff/plan documents)
- General
adopted_in: []
sources:
- do-this-before-you-lose-access-to-fable-5.md
related_findings:
- file: frontier-model-as-harness-designer.md
  rel: extends
- file: frontier-model-as-unknown-unknown-elicitor.md
  rel: same-problem
- file: planner-executor-deterministic-guardrails.md
  rel: same-problem
- file: plan-implement-session-separation-bias-removal.md
  rel: same-problem
- file: unknowns-reduction-phase-anchored-technique-set.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: raw
---

# War-Game Plan Format for Executor Handoff

## What It Is

A plan-artifact format that replaces linear plans with simulated execution. The authoring
prompt opens: "War-game order. You are not executing this mission, you are purely
war-gaming it," and states that "a cheaper executor model will run the brief below"
(naming the model, so the war-gamer can consult that model's documentation and tailor the
brief). The war-gamer then fights the mission on paper move by move. Required elements per
move: expected observation if it worked, expected observation if it didn't, most-likely
failure with its signals, and the countermove. Every fork carries a trigger condition.
Unresolvable assumptions are flagged to a blocked-variables ledger (placeholder variables
the human must supply). The document terminates with abort conditions — errors or missing
access that should stop execution entirely. The structure mirrors the agentic loop itself:
action, reaction, counteraction.

## Why It Matters

Even strong models produce plans that "assume linearity, a blue-sky scenario" — the plan
looks logical but doesn't say what to do when reality deviates. Executor models then
improvise at exactly the moments improvisation is most expensive (the last 20% of a
build). Pre-simulating the failure branches with the strongest available model converts
frontier intelligence into a durable artifact any cheaper model can execute. The human's
role is scoped explicitly: decide how deep to war-game (second/third/fourth-order
consequences) and fill the blocked-variables ledger.

## Why People Are Using It

Motivated by frontier-model access volatility and cost (Fable 5 leaving subscription
plans): capture the expensive model's judgment as reusable blueprints rather than spending
it on direct execution. Demonstrated end-to-end with a 10-project batch fanned out to
parallel agents.

## Potential Alternatives

Plain plan-then-execute (cheaper to author, fragile off the happy path); dynamic
advisor-executor consultation (handles deviations live at higher per-incident cost and
requires the frontier model to stay available); deterministic guardrails coded into the
harness (stronger enforcement, much higher build cost).

## Potential Improvements

Feed observed execution traces back into the war-game to prune branches that never fire;
standardize the ledger/abort-condition sections as a template; combine with an advisor
fallback for deviations the war-game didn't anticipate.

## Potential Failure Modes

Branch explosion — war-gaming every juncture to depth N is unbounded; the human must cap
depth. Simulated failures reflect the model's priors, not the actual environment — rare
real failures still fall outside the tree. Stale war-games drift as the codebase changes.
Executor-tailoring is only as good as the public documentation of the executor model. A
war-game that is 90% boilerplate branches can bury the few decision-relevant forks.
