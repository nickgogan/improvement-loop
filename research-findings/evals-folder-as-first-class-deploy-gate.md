---
name: "Evals as a First-Class Framework Folder Gating Deployment"
summary: |-
  Plain English: the test suite for an agent isn't a separate bolted-on project — it's
  just another named folder inside the agent itself, with the same status as its
  skills or tools — and the deploy step runs it automatically, expecting a clean pass
  before the update ships to production. Vercel's Eve gives evals this treatment
  explicitly: "evals is another thing you can just have a folder for in your agent...
  you can test certain behavior of your agent, making sure that you get green check
  marks across the board before you deploy that update of your agent to production."
  In the demo, running the eval suite is itself invoked the same way as everything
  else in the framework — by telling the coding agent, in natural language, to run it
  — and the deploy step ("Deploy this Eve agent") is shown automatically running a
  smoke test before confirming the deploy is complete.
implementation_notes: |-
  Direct structural parallel to the engine's own pipeline (Sources -> Extract -> KB ->
  [gate] -> Identify -> [gate] -> Extract -> [gate] -> Deploy, per IL CLAUDE.md): today
  the Deploy stage's only gate is Nick's manual review (DD-29); there is no automated
  eval layer checking a staged artifact before it reaches that human gate. Eve's
  pattern — evals as a named, first-class folder alongside skills/tools, run
  automatically at deploy time and expected to show green before the deploy proceeds —
  is a candidate shape for an automated pre-gate check on staged extracts/ artifacts
  (DD-80, DD-119): tightening what reaches Nick's review rather than replacing his
  gate. Cross-reference externalized-real-session-behavior-evals.md for a more
  mechanically-detailed version of the same eval-gated-deploy idea (real harness
  sessions, LLM-judged transcripts, PR-level gating) before treating this Eve-specific
  framing as more than corroborating evidence of the pattern's direction — both
  sources are Medium evidence, not proven-at-scale precedent.
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
  - "IL (extraction/deploy pipeline)"
adopted_in: []
sources:
  - "vercel-eve-file-system-agent-framework.md"
related_findings:
  - file: "externalized-real-session-behavior-evals.md"
    rel: "same-problem"
  - file: "four-layer-production-eval-stack-with-golden-traces.md"
    rel: "same-problem"
  - file: "acceptance-criteria-as-verifiable-eval-anchor.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "synthesized"
consumed_by:
  - verifying-agent-output.md
tags:
  - "evaluation"
  - "deploy-gate"
  - "agent-framework"
  - "ci-cd"
---

# Evals as a First-Class Framework Folder Gating Deployment

## What It Is

Eve gives evals the same structural status as skills, tools, or channels: a named
`evals` folder inside the agent, rather than a separately configured test project or CI
pipeline bolted on afterward. The presenter's framing: "evals is another thing you can
just have a folder for in your agent... making sure that you get green check marks
across the board before you deploy that update of your agent to production." In the
demo, invoking the eval suite happens the same way as every other Eve action — telling
the coding agent, in natural language, to run it ("it's yet another thing in the skill
that it can leverage to run that for you") — rather than through a separately learned
CI/test-runner interface. The deploy flow itself, triggered by telling the coding agent
"Deploy this Eve agent," is shown completing with an automatic smoke test ("it even ran
a smoke test to make sure we are good to go") confirmed running in the live demo; the
fuller evals-folder-as-blocking-gate mechanic is described by the presenter but not
independently demonstrated failing/blocking a deploy in this video.

## Why It Matters

This turns "did we test this before shipping" from a process/discipline question (did
the team remember to run the suite, is a separate CI pipeline configured correctly) into
a structural one (the folder exists or it doesn't; if it exists, the framework runs it
at deploy time). It lowers the ceremony cost of having eval coverage at all — which
matters because eval suites are exactly the kind of infrastructure teams skip when it is
optional overhead rather than a first-class citizen of the thing being built. It is also
another instance of Eve's general "define a folder, get framework behavior for free"
pattern (`agent-as-folder-compiled-to-manifest.md`) applied specifically to testing.

## Why People Are Using It

Same source; positioned as one of the production-reliability primitives (alongside
durable sessions, sandboxing, and human-in-the-loop approval — see the companion
findings from this source) that differentiate Eve from a bare agent loop. The demo
confirms an automatic smoke test runs at deploy time; the fuller evals-folder-as-gate
claim is consistent with Eve's general folder-convention pattern but not shown
end-to-end in this source.

## Potential Alternatives

- **Externalized eval repo with PR-level gating**
  (`externalized-real-session-behavior-evals.md`) — heavier-weight and more
  mechanically proven: real harness sessions, LLM-judged transcripts, before/after
  evidence required on any content-changing PR, deliberately decoupled from the shipped
  artifact (because bundling broke plugin installs in that case).
- **Four-layer production eval stack with golden traces**
  (`four-layer-production-eval-stack-with-golden-traces.md`) — a more elaborate,
  multi-layer architecture (tool correctness, scenario workflows, shadow/canary,
  online outcomes) largely evaluating post-deploy; complementary to Eve's pre-deploy
  gate rather than competing with it.
- **No automated evals, human review alone** — the engine's current deploy-gate state
  (DD-29): every staged artifact is reviewed by Nick, with no automated pre-check.

## Potential Improvements

The source does not specify the evals folder's test format, how "green check marks" are
computed, or whether the gate is hard-blocking versus advisory. A follow-up look at
Eve's actual eval-folder schema (via the verified upstream repo) would be needed before
adopting the shape wholesale.

## Potential Failure Modes

A folder-based eval gate is only as good as what is written into it — the folder's mere
presence proves nothing about coverage quality, the same false-confidence failure mode
already flagged in `externalized-real-session-behavior-evals.md` ("a spec that loads is
not an agent that behaves"). If the gate is advisory rather than hard-blocking, teams
under deadline pressure will ship past red checkmarks the same way they override any
other soft gate — this source does not establish which of the two Eve actually is.
