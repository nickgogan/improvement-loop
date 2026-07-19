---
title: "Cold-Start Regression Test — Fresh-Session Context-Wiring Check"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "cold-start-chain-and-cold-start-test"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "structuring-agent-context.harvest-queue"
identification_report: "structuring-agent-context.harvest-queue.md::cold-start-chain-and-cold-start-test::skill::cold-start-regression-test"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent systems whose sessions are stateless and must reach working state by loading documented context files, not by carrying over a prior conversation"
    - "teams that want a runnable pass/fail check on whether a brand-new session can state the system's purpose and next action from entry points alone"
    - "porting an agent system, or rewiring its context load path, onto a new harness or platform and needing an acceptance test that the wiring actually composes"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — the test only opens a fresh session, reads the documented entry points, and reports; it modifies no system state"
  auditability: "high — the cold-start echo is a concrete artifact (purpose, active-context pointer, next unit of work, live-vs-degraded wiring rows) checkable line-by-line against the system's control surface; pass/fail is externally verifiable when an independent reader grades it"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented as the standing wiring regression check for a single production system. A lightweight two-hop variant — one forward-only control file as the sole cold-start artifact plus a wake-up convention — is in partial use elsewhere; the full documented-load-chain form is not yet adopted."
contract:
  preconditions: "A documented, ordered load path exists from the platform's always-on entry file through to the task layer (entry file → active-context pointer → vision/architecture layer → control surfaces → method router → task capability). A control surface states the system's purpose and the current next unit of work as ground truth. A fresh session — no warm context — can be opened loading only the standard entry points. An independent reader (not the session that composed the context) is available to grade the echo."
  invariants: "The test loads ONLY the standard entry points — nothing pulled in by habit or warm-session carryover. The session that composes the context is never its own grader. A pass requires the fresh session to state, with zero guidance: the system's purpose, the active-context pointer, and the next unit of work (and, for install-acceptance runs, which wiring rows are live vs degraded). Any missing or misstated item is a fail. A fail localizes to the specific failing load-chain row, not a global restart."
  governance: "Owner: whoever maintains the system's context wiring and entry chain (workspace steward or library maintainer). The test runs in two occasions: as a periodic regression check on context-wiring health, and as the mandatory install-acceptance gate after any wiring change or harness/platform port. The test produces only a report and a failing-row pointer — it never autonomously modifies the system; repairs are a separate, gated act."
  recovery: "On fail: treat the install or wiring change as not done; return to the specific failing load-chain row, repair the pointer or content there, and re-run from a fresh session. If the echo passes but is suspected of self-assessment (the grader was the composing session), re-run with an independent reader and verify the stated next unit of work against the control surface directly. If a warm session masks a broken chain, only a truly fresh session exposes it — never grade from a session that has already loaded context by habit."
tags:
  - "extracted-artifact"
  - "skill"
  - "cold-start"
  - "context-engineering"
  - "regression-test"
  - "session-continuity"
---

# Cold-Start Regression Test — Fresh-Session Context-Wiring Check

**Source:** [[cold-start-chain-and-cold-start-test]]
**Form:** skill
**Extraction date:** 2026-07-19

## Purpose

Turn "is our context wiring healthy?" from a feeling into a runnable check. A stateless
agent system is only truly *disposable* — no session depending on a previous conversation —
if the path from zero context to working state is explicit and continuously tested. This
skill runs that test: a fresh session, loading only the standard entry points, must be able
to state the system's purpose and the next unit of work with zero guidance. The same
procedure, run as a "cold-start echo," doubles as the acceptance test for installing the
system on a new harness.

## Inputs

- **The standard entry points only.** The platform's always-on entry file plus the documented
  load chain it points into — and nothing else. No context loaded by habit, no warm-session
  carryover.
- **A fresh session.** An agent session with no prior conversational context.
- **The control surface as ground truth.** The file(s) that authoritatively declare the
  system's purpose and the current next unit of work, used to grade the echo.
- **An independent grader.** A reader that is not the session which composed the context
  (self-assessment is disqualified — see Failure Modes).

## Outputs

- **A pass/fail verdict** on whether the fresh session reached working state from entry points
  alone.
- **The cold-start echo report:** the system's purpose, the active-context pointer, the next
  unit of work, and — for install-acceptance runs — which wiring rows are live vs degraded.
- **On failure: the failing load-chain row(s)** to return to and repair.

## Steps

1. **Open a fresh session.** No warm context. Load only the standard entry points.
2. **Follow the documented load chain hop by hop.** Entry file → active-context pointer →
   vision/architecture layer → control surfaces → method router → the capability for the task
   at hand. Only the first hop is platform-specific; every hop after is a file-to-file pointer
   and should move unchanged across harnesses.
3. **Produce the echo.** With zero guidance, state the system's purpose, the active-context
   pointer, and the next unit of work. For an install-acceptance run, also state which wiring
   rows are live vs degraded.
4. **Grade against the control surface — independently.** Verify each echoed item against the
   control surface using a reader that is not the composing session. The stated next unit of
   work must match the control surface's ground truth.
5. **On any missing or misstated item, localize and repair.** Mark the install/wiring as not
   done, return to the specific failing load-chain row, repair the pointer or content there,
   and re-run from step 1. Do not patch by loading extra context — that hides the break.
6. **Run at the two trigger occasions.** Periodically as a wiring-health regression check, and
   as the mandatory acceptance gate after any wiring change or harness/platform port.

## Failure Modes

- **Warm-session masking.** Context loaded by habit in warm sessions can hide a broken chain
  for weeks — the test only guards what the entry points actually reach. Mitigation: run from a
  genuinely fresh session; never grade from a session that has already loaded context by habit.
- **Self-assessment lie.** The echo can pass while lying if the grader is the same session that
  composed the context. Mitigation: grade with an independent reader and verify the stated next
  unit of work against the control surface directly.
- **Untested surface area.** The test only exercises what the standard entry points reach;
  anything off the documented chain is never verified. Mitigation: ensure load-bearing context
  is on the chain, not reachable only by habit.
- **Chain bloat.** A load chain with too many hops reintroduces the ramp-up cost the pattern
  exists to kill. Mitigation: keep the chain short; each hop must earn its place.

## Contract

### Preconditions
A documented, ordered load path exists from the platform's always-on entry file through to the
task layer (entry file → active-context pointer → vision/architecture layer → control surfaces →
method router → task capability). A control surface states the system's purpose and the current
next unit of work as ground truth. A fresh session — no warm context — can be opened loading only
the standard entry points. An independent reader (not the session that composed the context) is
available to grade the echo.

### Invariants
The test loads ONLY the standard entry points — nothing pulled in by habit or warm-session
carryover. The session that composes the context is never its own grader. A pass requires the
fresh session to state, with zero guidance: the system's purpose, the active-context pointer, and
the next unit of work (and, for install-acceptance runs, which wiring rows are live vs degraded).
Any missing or misstated item is a fail. A fail localizes to the specific failing load-chain row,
not a global restart.

### Governance
Owner: whoever maintains the system's context wiring and entry chain (workspace steward or library
maintainer). The test runs in two occasions: as a periodic regression check on context-wiring
health, and as the mandatory install-acceptance gate after any wiring change or harness/platform
port. The test produces only a report and a failing-row pointer — it never autonomously modifies
the system; repairs are a separate, gated act.

### Recovery
On fail: treat the install or wiring change as not done; return to the specific failing load-chain
row, repair the pointer or content there, and re-run from a fresh session. If the echo passes but
is suspected of self-assessment (the grader was the composing session), re-run with an independent
reader and verify the stated next unit of work against the control surface directly. If a warm
session masks a broken chain, only a truly fresh session exposes it — never grade from a session
that has already loaded context by habit.
