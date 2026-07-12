---
name: "Legible / Executable / Verifiable — Agent-Readiness Triad"
summary: |-
  For agent loops to work unattended, the codebase (or work substrate) must satisfy three
  properties: legible — the agent can find what to change; executable — the environment
  runs without setup friction (dev server already up); and verifiable — there is a way to
  prove the work, e.g., a browser test that records a clip a human can actually watch.
  Agent-readiness is a property of the substrate, not the agent: the same loop succeeds
  or fails depending on whether the repo meets the triad.
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (substrate readiness)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "loop-engineering-explained-by-claude-code-creators.md"
related_findings:
  - file: "total-organizational-legibility-as-ai-prerequisite.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A three-property checklist for whether a work substrate is ready to have agent loops run
against it:

1. **Legible** — the agent can locate what to change: navigable structure, conventions
   written down, discoverable state.
2. **Executable** — the loop doesn't stall on environment friction: the dev server is
   already up, builds run, commands work without bespoke setup each cycle.
3. **Verifiable** — the agent has a way to *prove* the work, not claim it: the cited
   example is a browser test that records a clip you can actually watch — evidence a
   human can check in seconds.

The triad reframes loop failures as substrate failures: an agent loop on an illegible,
hard-to-run, unverifiable repo produces claims, not shippable work.

## Why It Matters for Us

The KB already holds legibility-as-AI-prerequisite at the organizational level; this
extends it into a three-part operational test and adds the two properties legibility
alone misses. The engine's substrate scores well on legible (frontmatter-driven
discovery, conventions) and partially on verifiable (validators, but only for structure —
content quality has no proof mechanism); "executable" maps to whether engine skills can
run end-to-end without manual setup. Useful as an audit lens for consumer systems in
/assess-* work: readiness questions about the *system being built for agents*, not the
agents.

## Why People Are Using It

Cloud Codes (2026-06-26), summarizing the June-2026 loop-engineering field-guide wave
(note: parts of that guide's provenance are secondhand — see the source entry).
Independent convergence with the KB's organizational-legibility and
environment-grounding findings.

## Potential Improvements

- Per-property scoring rather than pass/fail — substrates are unevenly ready, and the
  weakest property bounds loop autonomy.
- Artifact-type variants: what "executable" means for a knowledge base differs from a
  web app.

## Potential Failure Modes

- Verifiable-theater: recorded proof of the wrong behavior still looks like proof;
  verification artifacts need to encode the acceptance criteria, not just activity.
- Readiness debt treated as agent failure: teams blame the model and add prompt patches
  when the substrate is the problem.
