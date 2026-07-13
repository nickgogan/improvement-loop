---
name: "GPT-5.6 Soul vs Fable 5 — One-Practitioner One-Shot Head-to-Head"
summary: |-
  One practitioner (Pat Simmons), three one-shot builds, same prompt to both models,
  deployed live: GPT-5.6 Soul won all three on thoroughness, design fidelity, and
  instruction-following at 3-6x Fable 5's wall-clock. App clone: Soul near-pixel parity
  in 2h51m vs Fable "underwhelming" in ~30m. Soul followed a staged-gate skill
  literally (pausing at each gate for confirmation) where Fable blew through it fast
  and shallow. Not a benchmark: n=1 per task, self-flagged buggy cost readouts — a
  practitioner head-to-head, useful as capability-profile signal only.
implementation_notes: |-
  Fills the model-capability registry's GPT-5.6 grounding gap — registry claims must be
  KB-grounded, and the GPT-5.6 line currently has no KB citation; the registry should
  cite this source (registry itself not edited in this pass). Treat cost figures as
  unreliable per the companion cost-observability finding.
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "i-made-gpt-56-and-fable-5-build-the-same-app.md"
related_findings:
  - file: "claude-5-family-retiers-claude-line.md"
    rel: "extends"
  - file: "harness-cost-readout-unreliability-independent-log-accounting.md"
    rel: "enabled-by"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# GPT-5.6 Soul vs Fable 5 — One-Practitioner One-Shot Head-to-Head

## What It Is

A same-prompt, one-shot (no revisions), deploy-live comparison across three tasks,
run in each model's native harness (Codex app for GPT-5.6 Soul high; Claude Code for
Fable 5 high effort):

| Task | Fable 5 | GPT-5.6 Soul | Winner |
|---|---|---|---|
| Shots.so pixel-clone (staged-gate skill) | ~30 min, ~$12 | 2h51m, ~$100 | Soul — near-identical UI, working exports/presets/animator vs Fable's sparse approximation |
| "Mischief" creative drop site | ~18 min, ~$20 | ~30 min, ~$5 (readout suspect) | Soul — multi-page interactive experience vs Fable's static single page |
| Underspecified NYC learning platform (one-shot + one feedback round) | 15-20 min, ~$95 (readout suspect) | 11 min + revisions, ~$11 | Closer; Soul better design, Fable better 3D map after feedback |

Capability-profile observations:

- **Soul trades wall-clock for thoroughness** (3-6x slower on the heavyweight task) and
  its thoroughness showed up as feature completeness and design fidelity.
- **Soul follows staged procedures literally**: given a clone skill with explicit gates
  ("say begin extraction to resume"), it stopped at each gate and waited; Fable ran the
  same skill straight through in 30 minutes. Literal gate-compliance cuts both ways —
  higher fidelity, much higher latency and babysitting.
- **Fable 5's one-shot weakness is pixel/design fidelity**, not speed or competence:
  fast, working, but visually and feature-wise shallow relative to the reference. Both
  models took the second-round feedback well.

## Why It Matters

The KB's Claude-line re-tiering finding has no GPT-5.6 counterpart; this is the first
KB-grounded signal on GPT-5.6 Soul's profile: a thoroughness/instruction-following
specialist at significant wall-clock cost. For routing intuitions: one-shot,
fidelity-critical, low-supervision builds favored Soul in this sample; fast iterative
loops favored Fable. It is capability *shape*, not capability *ranking* — n=1 per task.

## Why People Are Using It

The author is a serial model-stress-tester (prior Linear clone and model-comparison
videos) running real deployed builds rather than benchmark citations, and flags his own
measurement problems on camera — unusually honest for the genre.

## Potential Improvements

- Repeated trials per task (the repeated-sampling literature says n=1 is noise-heavy).
- Independent cost accounting from the start (ccusage-style), not harness readouts.
- Same-harness comparison to separate model effect from harness effect.

## Potential Failure Modes

- **Overgeneralizing from n=1.** Each observation is one sample of a stochastic system;
  the Soul-slower result even contradicted the author's expectations from benchmarks.
- **Harness confound.** Different harnesses (Codex vs Claude Code) mean the comparison
  is model+harness, not model alone.
- **Cost figures unreliable** — self-flagged; both harnesses showed inconsistent usage
  readouts on subscription plans.
