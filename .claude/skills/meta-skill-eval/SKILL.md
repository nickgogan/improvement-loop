---
name: meta-skill-eval
description: >-
  Executes structured skill evals through the real Claude Code CLI in isolated
  contexts and appends version-attributed results to operations/evals/. Use to
  run trigger/execution/retirement cases, check pass rates or graduation,
  compare with-skill vs skill-masked output uplift, read efficiency, detect
  corpus drift, score a subjective (hitl) case, or run the shared adversarial
  pack before install/export. Four modes: run (paid, bounded, never scheduled),
  report (pass/paired/efficiency reads), sync (offline drift check; fresh hosts
  pass cleanly), score (human verdict → ledger). Trigger phrases: "run the
  evals", "eval run for X", "what's the pass rate", "check eval drift",
  "retirement check". Not for eval-set authoring/skill-quality method
  (meta-skill-author) or doc audits (ops-doc-sync).
license: MIT
compatibility: >-
  Requires the Claude Code CLI on PATH with a logged-in user session, Python 3
  + PyYAML, and subprocess execution.
  Without the CLI the run mode is inert; report and sync modes degrade
  gracefully (ledger reads and corpus checks are offline). Each optional
  capability carries a named degradation in capability-contract.yaml.
allowed-tools: Read, Bash(python*)
metadata:
  version: "2.0.0"
  upstream: "nickgogan/CareerBuddy .github/skills/meta-skill-eval @ 2.0.0"
  imported: "2026-07-22 — backend ported codex exec -> claude -p; engine notes in ADAPTATION.md"
---

## L0 abstract

Run skill evals through the real CLI and account for every result. One command
per mode, all in `scripts/eval_runner.py`: `run` executes a skill's
eval-cases (trigger / execution / retirement tiers) with denied-by-default
mutating tools, 3-trial default, and per-case fresh contexts, appending one
attributed row per case×trial to `system/ops/evals/ledger.jsonl`; `report`
answers pass-rate, graduation, saturation, retirement, and paired output-uplift
questions from the ledger (plus `--efficiency` duration/token reads); `sync` fails
deterministically when an eval set no longer covers the
real phrasings logged in the eval-candidates corpus (clean pass when no
corpus exists yet); `score` appends human scorecard verdicts for hitl cases
as attributed ledger rows (judge-verdict schema v1).

## Boundaries (owner map)

- **Eval-case authoring and skill-quality scoring** — `meta-skill-author` §2
  owns the method; this skill only executes what exists.
- **Corpus capture** — `/self-improve` owns `eval-candidates.md` (engine home:
  `operations/self/`); sync reads it, never writes it. **Back-edge (MV48):** a
  failed execution case in the ledger is a capture-qualifying event — after
  ruling out a grading bug (read the transcript), the lesson lands via
  `/self-improve` capture against the failing skill, citing the ledger row +
  transcript path; this skill only reports.
- **Case schema** — `references/eval-cases-schema.md` (v1): per-skill
  `evals/eval-cases.yaml`, both trigger directions, per-mode execution cases
  with positive *and* negative assertions, class carve-outs
  (objective / subjective / script-core), `version` field per set.
- **Design authority** — `system/plans/skill-eval-harness.md` (MV46).

## Mode contracts

All via `python3 systems/improvement-loop/.claude/skills/meta-skill-eval/scripts/eval_runner.py`:

- **run** `--skill X [--tier trigger|execution|retirement|all] [--cases ids]
  [--trials N] [--model M] [--timeout S] [--max-runs N] [--dry-run]` —
  outcome: ledger rows + saved transcripts under
  `operations/evals/transcripts/<run-id>/`; exit 0 only on all-pass. Trigger
  verdicts come from explicit structured skill-load evidence (`Skill` tool_use
  events in the stream-json transcript), never self-report. If an installed CLI
  build exposes no such evidence, trigger-dependent cases record `error` with
  `skill_evidence: unavailable` rather than manufacture a pass or failure.
  Timeouts record as `error`, never graded (absence of evidence is not an
  abstain pass); nonzero CLI exits and missing/malformed final-result output do
  the same. Every case/trial uses a fresh workspace with harness hooks and
  settings excluded; read-only cases run non-interactive with the mutating file
  tools disallowed. A case that explicitly allows `write` receives a copied
  workspace, never live-tree symlinks. Retirement tier omits the skill from
  both skill rosters (workspace + engine, DD-109).
  `--skill _shared`
  runs the **shared adversarial pack**
  (`references/adversarial-pack.yaml` — injection, scope-bypass, ban-term
  leakage probes): an explicit pre-install / pre-export gate, never scheduled.
- **report** `[--skill X] [--paired | --efficiency [--sessions]]` — outcome: per
  skill×tier×model table — latest
  pass rate, run count, lifecycle label (capability → regression at two
  consecutive full-pass runs; saturated at three; retirement signal at
  ≥ 80% skill-masked pass rate). `--efficiency` (MV48 F) switches to
  efficiency reads — avg duration + transcript size per group from existing
  ledger rows/transcripts; `--sessions` adds real-usage tokens/credits mined
  from the transcript archive (skipped cleanly on hosts without one). Zero new
  instrumentation; efficiency is a read, never a gate. `--paired` compares the
  latest matched execution and skill-masked retirement rows by case id and reports
  output uplift; unmatched rosters never manufacture a delta. Read-only.
- **sync** `[--skill X]` — outcome: per-skill drift verdict; a corpus row is
  covered when its session key appears in a case `source` or in
  `corpus_waivers`. Exit 1 on any drift (audit-hookable). An absent/empty
  corpus is a **clean pass** (MV48 portability): fresh hosts start with no
  real-phrasing corpus; coverage accrues from their first capture.
- **score** `--run-id R --case C --score 0-100 [--pass-threshold N]
  [--scorecard PTR] [--failure-category C] [--note …]` — outcome: one
  `human-scored` ledger row
  under the judge-verdict schema v1 (`references/judge-verdict-schema.md`)
  referencing a real prior run (refuses otherwise — never score imagined
  output). Closes the hitl loop: subjective-class skills trend in the ledger
  like everyone else.

## Constraints

- **Every run is real tokens.** Default scope one skill; `--max-runs` (default
  30) aborts oversized plans *before* the first run; full-corpus sweeps are an
  explicit human ask; nothing is ever scheduled (no CI loops — G9 declined).
- **Invest output-first.** Execution/output correctness and completeness are the
  primary evidence; adversarial/safety is second; trigger accuracy is a bounded
  routing smoke. Description changes call for one-trial representative trigger
  sampling first — never an exhaustive trigger sweep as a release gate.
- **Side-effect-free by default:** read-only cases run non-interactive with
  Write/Edit disallowed (un-allowlisted tools auto-deny in print mode); only a
  case whose `allow_tools` names `write` runs acceptEdits inside an isolated
  copied workspace. Grade transcript evidence, not produced artifacts
  (script-core carve-out).
- **Ledger is append-only.** Never rewrite or prune `ledger.jsonl`; corrections
  are new rows. Volatile pass-rate numbers never get copied into tracked docs —
  run `report` when a number is needed.
- **Dogfooding flag:** running this skill's own eval set is self-referential —
  say so in the output and treat verdicts as advisory.
- **Read the transcripts:** a surprising score (high or low) is a grading-bug
  hypothesis first; the transcript is saved for exactly that.

## Stop rules

Halt and ask the human when: the planned run count exceeds `--max-runs`; the
Claude Code CLI is missing; CLI authentication fails (never mock results); a
run would need a broader sandbox than the case's declared `allow_tools`
relaxation; or repeated timeouts suggest a systemic harness problem rather
than a case problem.

## Reversibility & HITL tiers

| Action | Reversibility | Tier |
|--------|---------------|------|
| dry-run, report, sync | Read-only | Full autonomy |
| run (tokens spent, ledger append, transcripts saved) | Irreversible spend, reversible files | Guarded — human names the skill or approves the plan |
| Raising --max-runs / multi-skill sweeps | Irreversible spend | Human-required |
| Editing eval-cases.yaml, C16 rules, or the ledger by hand | Governance / evidence | Out of scope here — meta-skill-author / ops-doc-sync gates |

## Acceptance (per engagement, binary)

- Requested mode ran to a zero/non-zero exit with the contract above.
- Every executed case has a ledger row with full attribution (model,
  skill/eval-set/harness versions) and a saved transcript.
- No ungated write outside `system/ops/evals/` and temp dirs.
