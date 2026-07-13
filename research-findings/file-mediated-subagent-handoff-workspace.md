---
name: "File-Mediated Subagent Handoff Workspace"
summary: |-
  Plain English: don't paste task text, reports, or diffs into subagent dispatch
  prompts — write them to files in a runtime scratch workspace and dispatch paths,
  because "everything you paste into a dispatch prompt stays resident in your context
  for the rest of the session." Superpowers v6.0.0 inverted its own v5 doctrine
  ("paste the full text of the task") with three shell scripts — `task-brief`,
  `review-package`, `sdd-workspace` — that write task briefs, implementer reports, and
  review diffs into a self-ignoring `.superpowers/sdd/` working-tree workspace (outside
  `.git/`, which harnesses write-protect); dispatch prompts carry file paths plus a
  thin prose frame, briefs are extracted per task so no subagent ever reads the whole
  plan, and implementer returns are capped under 15 lines with detail in the report
  file. BMAD v6.10.0 converges independently: reviewer subagents write full output to
  files and return only verdict + top findings + path ("the parent never holds full
  review text"), and its loop/worker modules communicate solely through spec files.
implementation_notes: |-
  Strong independent corroboration of the engine's own file-mediated handoff protocol
  (agents/handoff-protocol.md) and the session-137 ruling that skill passes return
  only report path + 5-line summary. The deltas worth noting: scripted workspace
  creation (deterministic tooling writes the files, not the orchestrator's prose),
  per-task brief extraction (subagents never see the whole plan), and the documented
  anti-pattern evidence (a 42k-char dispatch that was 99% pasted history).
  Priority upgraded P3 → P2 (reassessment 2026-07-13, Nick-accepted): C4 three-way
  independent convergence (superpowers, BMAD, Archon sidecars) + C3 — the engine's
  handoff-protocol.md and session-137 path+summary ruling are a live adopted variant.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "superpowers-plugin-spec-driven-sub-agent-orchestra.md"
    rel: "extends"
  - file: "subagent-isolation-contract.md"
    rel: "same-problem"
  - file: "typed-node-output-sidecars-by-type-artifact-discovery.md"
    rel: "same-problem"
  - file: "sub-agent-context-isolation-for-parallel-complex.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
tags:
  - "context-engineering"
  - "subagent-handoffs"
  - "cross-repo-convergence"
---

# File-Mediated Subagent Handoff Workspace

## What It Is

A handoff substrate for orchestrator/subagent workflows:

1. **A runtime scratch workspace.** `.superpowers/sdd/` is created at runtime by a
   script, self-ignoring via its own `.gitignore`, per-worktree, and deliberately
   outside `.git/` (harnesses write-protect it — the v6.0.3 fix). It holds task
   briefs, implementer reports, review packages, and the progress ledger.
2. **Scripts write the files, dispatches carry paths.** `task-brief PLAN N` extracts
   task N into `task-N-brief.md` (no subagent ever reads the whole plan);
   `review-package BASE HEAD` emits commit list + stat + `-U10` diff readable in one
   call. A dispatch prompt is one line of scene-setting, the brief path ("read this
   first — it is your requirements"), interfaces from earlier tasks, and the
   report-file path + contract.
3. **Thin returns.** Implementer return messages are capped under 15 lines; detail
   lives in the report file. The documented rationale is context residency:
   everything pasted into a dispatch stays in the orchestrator's context for the rest
   of the session (observed anti-pattern: a 42k-char dispatch, 99% pasted history).

BMAD converges on the same protocol from its own direction: reviewer and
reconciliation subagents write full output to `review-{slug}.md` files and return
compact summaries; the bmad-loop orchestrator and dev-auto worker communicate solely
through story-spec files across separately-installed modules.

## Why It Matters

Two heavily-used frameworks independently abandoned pasted-content handoffs for
file-mediated ones, and one of them documented the reversal of its own prior doctrine
with cost evidence. That convergence marks file mediation as the load-bearing answer to
orchestrator context economy: the orchestrator's context holds routing state, not
artifact bodies. The scripted-workspace detail is the transferable increment —
deterministic tools, not LLM prose, assemble the handoff files, which makes brief
extraction and diff packaging reliable and cheap.

## Why People Are Using It

Core of Superpowers' v6.0.0 SDD rewrite (eval-backed, ~2x faster / ~50% fewer tokens
for the flow overall); canonical across BMAD's reviewer gates and its unattended loop.
Sources: Observed in [superpowers](https://github.com/obra/superpowers) v6.1.1 — see
[[superpowers-analysis]] — and [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
v6.10.0 — see [[bmad-method-analysis]].

## Potential Alternatives

- **Paste-full-text dispatches** — the superseded doctrine; still simplest for tiny
  one-shot tasks with no report path.
- **Typed sidecar outputs** (Archon node sidecars) — the engine-enforced version:
  outputs typed and discoverable by schema rather than by convention.
- **Shared memory stores / databases** — richer queries, heavier infrastructure, loses
  git-diffable plain text.

## Potential Improvements

- Workspace lifecycle tooling: retention, cleanup, and "what's stale" reporting for
  scratch workspaces (they survive compaction but also survive relevance).
- Contract linting: verify a dispatch names every file the subagent must read/write.

## Potential Failure Modes

- **Path-trust failures** — a subagent that skips reading the brief file executes on
  vibes; the dispatch must make the read mandatory and verifiable.
- **Workspace destruction** — `git clean -fdx` erases the substrate (documented; git
  log is the recovery source).
- **Convention drift across components** — file-name/section contracts between
  separately-installed modules (BMAD's loop/worker) version independently and can skew.
