---
name: "North Star Drift Loop (Trajectory Extrapolation vs Locked Goals)"
summary: |-
  A periodic loop that checks whether accumulated activity actually points at declared
  goals. Four parts: lock in explicit North Star goals; analyze trajectory by reading
  Claude session history, ingested data, and loop results; forward-extrapolate ("if
  nothing changes, here's where you land in six months"); and, if drift is detected,
  surface what's pulling in that direction and propose direction changes. Goal-alignment
  drift detection — a different axis from source/doc drift.
implementation_notes: |-
  The engine has trajectory signals in CHARTER.md and a /detect-drift skill — but that
  skill detects source drift (extracts vs their sources), not goal drift. This pattern is
  a concrete recipe for a charter-alignment loop: read session history + System Log +
  loop reports, extrapolate the current trajectory, and diff it against the charter's
  trajectory signals. Design required: cadence, inputs, and how proposals route through
  the existing gate (report to Nick, never self-steer).
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (charter alignment)"
  - "General"
adopted_in: []
sources:
  - "8-claude-loops-to-build-10x-faster.md"
related_findings:
  - file: "session-history-mining-for-skill-discovery.md"
    rel: "enabled-by"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

"If the other loops are instruments, this loop is the compass." A scheduled loop that:

1. **Locks the North Star** — explicit, concrete goals (ship four paid products, land 12
   clients), captured once and treated as fixed reference points.
2. **Analyzes trajectory** — reads Claude session history, ingested data, and the results
   of other loops to establish what has actually been worked on.
3. **Forward-extrapolates** — summarizes as "if nothing changes, here's where you're
   going to land." The practitioner calls this the biggest kick-in-the-ass output.
4. **Proposes direction changes** — when drift is detected, names what is pulling in the
   drifting direction and proposes what to change.

## Why It Matters for Us

The engine's drift tooling is doc- and source-oriented (/detect-drift compares extracts
against their sources; /system-health compares docs against filesystem). Nothing compares
accumulated activity against CHARTER.md's trajectory signals. This is the missing third
drift axis: not "are the docs stale," but "is the work pointed at the goals." The
extrapolation step is what makes it actionable — a trajectory statement is falsifiable in
a way a raw activity summary is not.

## Why People Are Using It

Practitioner-demonstrated (Marchese, 2026-07). Single source, but the input side (session
history as trajectory evidence) is corroborated by his self-improving-system video and
other session-mining sources in the KB.

## Potential Improvements

- Anchoring extrapolation in quantitative loop outputs (run logs, System Log entries)
  rather than session prose alone.
- Distinguishing deliberate strategy changes from drift — goals themselves get revised;
  the loop needs a way to tell re-aiming from wandering.

## Potential Failure Modes

- Garbage extrapolation: session history over-represents what was easy to log, not what
  mattered.
- Goal lock-in: a rigid North Star file turns legitimate pivots into "drift" and nags
  against them.
- Judgment substitution: the proposal step can slide from surfacing drift to steering —
  in a governed system the output must stay advisory.
