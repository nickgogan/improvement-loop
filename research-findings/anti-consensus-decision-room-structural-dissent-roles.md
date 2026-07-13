---
name: "Anti-Consensus Decision Room with Structural Dissent Roles"
summary: |-
  Plain English: when you want AI personas to pressure-test a decision, don't ask for
  "devil's advocates" — build the room out of roles that are structurally incapable of
  agreeing, forbid consensus mechanics outright, and isolate their contexts so one
  shared window can't homogenize them. BMAD v6.10.0's party-mode ships an
  "Anti-Consensus Club": four structural dissent roles — Wildcard (option generator),
  Level (claim checker), Killjoy (loop stopper), Splinter (consensus challenger) —
  whose scene instructions forbid voting, declaring consensus, or speaking with
  authority. The scene-level meta-instructions recommend running voices as subagents
  "because separate context windows make it less likely that one shared context will
  make every voice agree too quickly" — context isolation deployed as a debiasing
  mechanism. The room ships `memory = false` by design: decision rooms start fresh.
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "anti-bias-protocol-for-llm-ideation.md"
    rel: "same-problem"
  - file: "gstack-spec-team-parallel-research-agents.md"
    rel: "same-problem"
  - file: "agent-self-reporting-unreliability-independent-eval.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "agent-design"
  - "debiasing"
  - "multi-persona"
---

# Anti-Consensus Decision Room with Structural Dissent Roles

## What It Is

A configured persona party purpose-built to resist LLM agreeableness, with three
design layers:

1. **Structural dissent roles.** The four members are defined by the *function* of
   their dissent, not a personality: Wildcard generates options, Level checks claims,
   Killjoy stops loops, Splinter challenges any forming consensus. Each role's job
   description makes premature agreement a failure of the role.
2. **Forbidden consensus mechanics.** Scene instructions prohibit voting, declaring
   consensus, or speaking with authority — the room cannot produce the social
   artifacts of agreement even if the voices converge.
3. **Context isolation as debiasing.** The recommended run mode is subagents with
   separate context windows, explicitly because one shared context tends to make every
   voice agree too quickly. Party memory is disabled (`memory = false`) so each
   decision room starts without accumulated alignment.

(party-mode `customize.toml`; four run modes degrade gracefully from agent-team to
inline voicing.)

## Why It Matters

Multi-persona review theater is common and mostly fake: N voices sampled from one
context converge fast, and "play a skeptic" instructions erode over turns. This design
attacks the failure at all three levels — role structure, interaction rules, and
*infrastructure* (separate context windows). The infrastructure move is the notable
one: it treats shared context as a bias vector and buys independence with isolation,
the same reasoning that motivates independent evaluators elsewhere in the KB, applied
to deliberation.

## Why People Are Using It

Shipped as a configured party group in BMAD's party-mode with scene-level
meta-instructions; part of the v6.x critical-thinking layer whose output is better
judgment rather than artifacts. Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Single adversarial reviewer** — cheaper, covers claim-checking but not
  option-generation or loop-stopping; one voice fatigues.
- **Parallel independent research agents** (gstack spec teams) — independence via
  parallel tasking rather than role structure; converges on synthesis, not decision
  pressure.
- **Ideation anti-bias protocols** (domain-shift rules) — debiases generation breadth,
  not decision convergence.

## Potential Improvements

- Measuring the isolation claim: agreement-rate deltas between shared-context and
  subagent runs would turn the design rationale into evidence.
- Role-set tuning per decision type (irreversible decisions may want a second
  Level-style checker).

## Potential Failure Modes

- **Dissent theater** — roles can perform disagreement without changing the decision;
  the room needs an integrator who is accountable for what dissent altered.
- **Cost multiplication** — four isolated subagent contexts per decision is expensive
  for routine choices; stakes calibration is required.
- **Paralysis by Killjoy** — structurally-mandated dissent with no consensus mechanics
  can leave decisions unresolved; the human remains the closer by design.
