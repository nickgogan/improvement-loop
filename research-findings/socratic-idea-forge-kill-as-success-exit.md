---
name: "Socratic Idea Forge with Kill-as-Success Exit Taxonomy"
summary: |-
  Plain English: pressure-test ideas "while changing your mind is still cheap," with a
  skill whose three exits — Hardened, Killed, Clearer — are ALL success outcomes, so
  the AI never steers the conversation toward "shall we build it?". BMAD v6.10.0's
  bmad-forge-idea runs Socratic interrogation of the user's idea under an explicit
  anti-sycophancy protocol ("praise is noise"; in attack mode never agree until the
  user ends the mode), one question at a time, with two-voice mechanics (one installed
  persona plus one generated outside voice, varied to prevent dominance). Artifact
  production (forged-idea.md) is optional; the memlog vocabulary includes `crack`,
  `kill`, and `lock` entry types, so the decision trail records what broke, what died,
  and what was settled.
implementation_notes: null
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "gstack-office-hours-socratic-discovery-pipeline.md"
    rel: "same-problem"
  - file: "anti-bias-protocol-for-llm-ideation.md"
    rel: "same-problem"
  - file: "anti-consensus-decision-room-structural-dissent-roles.md"
    rel: "same-problem"
  - file: "append-only-run-log-as-working-memory.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "intent-engineering"
  - "prompt-craft"
  - "ideation"
---

# Socratic Idea Forge with Kill-as-Success Exit Taxonomy

## What It Is

A pre-pipeline critical-thinking skill (phase 0, optional) whose design centers on not
biasing the user toward building:

1. **Three-exit taxonomy where killing wins too.** Valid exits are Idea Hardened,
   Idea Killed, and Idea Clearer — with explicit instruction not to steer toward
   "shall we build it?". Killing an idea cheaply is framed as the skill doing its job.
2. **Anti-sycophancy protocol.** "Praise is noise"; agreement is allowed only when it
   helps thinking; in attack mode the agent never agrees until the user ends the mode.
3. **Interrogation mechanics.** One question at a time; attack/defend modes; two-voice
   design (an installed persona plus one generated outside voice, varied to prevent a
   single voice dominating).
4. **Decision-trail vocabulary.** Memlog entry types include `crack` (a flaw found),
   `kill`, and `lock` (a settled point) — the pressure-test's outcome is auditable even
   when no artifact is produced; `forged-idea.md` is optional.

## Why It Matters

LLMs are structurally biased toward helping users proceed — every ideation conversation
drifts toward a build plan. Making "Killed" a first-class success exit is the cheapest
possible intervention against sunk-cost pipelines: it prices idea-death at the moment
it costs nothing, before specs, plans, and code accumulate commitment. The
kill-vocabulary in the log matters for organizational memory: killed ideas leave a
record of *why*, which is what prevents their resurrection unexamined.

## Why People Are Using It

Shipped as the entry point of BMAD's v6.x critical-thinking layer — reasoning skills
whose output is "better judgment, not artifacts." Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Socratic discovery pipelines** (gstack office-hours) — similar interrogation shape,
  but aimed at extracting requirements toward a build, not at possibly killing it.
- **Brainstorm-first workflows** (Superpowers brainstorming) — design pressure exists
  but the exit is always a spec; no kill taxonomy.
- **Human-only gate reviews** — the same function performed late, when killing is
  expensive.

## Potential Improvements

- Exit-rate telemetry: the skill's health metric is a nonzero kill rate — all-Hardened
  outcomes suggest the anti-sycophancy protocol is eroding.
- Reusable crack/kill/lock vocabulary across other deliberative skills.

## Potential Failure Modes

- **Sycophancy regression** — the protocol is prose; long sessions and agreeable models
  erode attack mode without measurement.
- **Performative severity** — an agent can manufacture cracks to seem rigorous,
  killing viable ideas; the user-ends-the-mode rule is the counterweight.
- **Gate fatigue** — mandatory forging of trivial ideas teaches users to skip the
  skill entirely; optionality is load-bearing.
