# Changelog — meta-skill-eval

All notable changes to this skill package. Semver; format per Keep a Changelog.

## [Unreleased]

## [2.0.0] — 2026-07-21

### Changed

- Replaced the Copilot subprocess backend with a Codex-native backend: one
  `codex exec --ephemeral --json` process per case/trial, isolated workspace,
  read-only sandbox by default, explicit model attribution, raw JSONL evidence,
  and schema-constrained final output.
- Trigger-dependent grading now fails closed as `error` when Codex exposes no
  structured skill-load event; agent self-report is never treated as evidence.
- Nonzero CLI exits and missing or malformed schema-final output are ungradeable
  `error` rows, never ordinary responses that deterministic checks might pass.
- Retirement masking now covers both `.github/skills` and `.agents/skills`.
- Removed repository-owned personal model bands/defaults. Paid runs require an
  explicit model unless an eval set intentionally pins one.

### Added

- `references/codex-output-schema.json` and deterministic Codex backend tests.

## [1.6.0] — 2026-07-20

### Added

- `report --paired`: latest matched execution vs skill-masked retirement output
  uplift by skill×model; case-id intersection prevents unmatched rosters from
  manufacturing a delta. Hermetic fixture covers known +50% uplift.
- Optional eval-set `value_class` (`capability-uplift` / `encoded-preference`) and
  per-case typed `failure_category`; failed deterministic and human-scored rows carry
  the fixed output-failure taxonomy.
- Oracle-verifier admission rule, final-output/trajectory/single-step diagnostic
  routing, and model-judge activation guard (human calibration + per-class
  precision/recall first), from the deferred-source delta pass.

### Changed

- Eval-investment policy is now output-first (MV47 prove → MV48 amendment):
  execution/output correctness and completeness first, adversarial/safety second,
  trigger accuracy third as a bounded one-trial routing smoke after description
  changes. Exhaustive trigger distributions are diagnostic, not release gates.

## [1.5.0] — 2026-07-20

### Added

- **score subcommand** (MV48 D minimal): human scorecard verdicts for `hitl` cases
  append as `human-scored` ledger rows under the judge-verdict schema v1
  (`references/judge-verdict-schema.md`); refuses run/case ids absent from the
  ledger. Subjective-class skills now trend in the ledger. `profile-voice` scoring
  adopts the verdict shape (doc-level).
- **Efficiency reads** (MV48 F): `report --efficiency` — avg duration + transcript
  size per skill×tier×model from existing rows/transcripts; `--sessions` adds
  real-usage tokens/credits regex-mined from the transcript archive. Zero new
  instrumentation.
- **Shared adversarial pack** (MV48 G): `run --skill _shared` executes
  `references/adversarial-pack.yaml` (injection-via-tool-output, scope-bypass,
  ban-term leakage probes) as a pre-install / pre-export gate — wired into
  ADAPTATION step 6 and the ops-doc-sync export-dry-run procedure. New
  `no_ban_terms` check in the registry (vacuous pass without a local ban file).

### Changed

- **Empty-corpus sync is a clean pass** (MV48 portability): fresh hosts (new
  user/machine) have no phrasing corpus — sync exits 0 with a notice instead of
  erroring; `test_sync_drift.py` gains the absent-corpus leg. Case `source:` hex8
  keys documented as provenance-only on receiving hosts (ADAPTATION note).
- Back-edge documented (MV48 `seam` scope, 2026-07-20): a failed execution case in
  the ledger is a capture-qualifying event for `ops-self-improve` (lesson against the
  failing skill, ledger row + transcript cited) — boundaries section; this skill only
  reports. Sibling change: ops-self-improve scan now invokes `sync` for drift
  detection instead of prose comparison. **Description changed: re-run trigger evals.**

### Fixed

- Version drift: SKILL.md metadata + capability-contract.yaml said 1.0.0 while the
  changelog was at 1.4.0 — aligned (found at MV48 seam scope).

## [1.4.0] — 2026-07-20

### Added

- **Sync fixture testability** (MV46 S3): `sync` gains `--corpus` / `--skills-dir`
  overrides so drift detection is hermetically testable;
  `scripts/test_sync_drift.py` seeds a red/green fixture (covered corpus → exit 0;
  seeded uncovered row → exit 1 with a DRIFT line) without touching the live
  corpus, skills tree, or ledger. Sync is now wired as doc-audit check C19
  (ops-doc-sync routes to it — drift is an audit failure, killing the MV45 S3
  drift class).

## [1.3.0] — 2026-07-20

### Added

- **Harness exclusion** (operator, at first fable run — killed mid-run): pure
  tool-wrapper script-core skills earn no paid LLM eval runs; correctness is
  binary script behavior owned by their own tests. `harness: excluded` in
  eval-cases.yaml; run mode refuses with the recorded reason. First excluded:
  tool-resume-render (its set bumped to v2, cases retained as trigger-shape
  documentation). Ledger rows from its three completed runs stand (append-only).

## [1.2.0] — 2026-07-20

### Added

- **Effort levels + pinned versions** (operator: "these matter"): model policy
  v2 pins band versions (sonnet→5, opus→4.8, operator-chosen from the CLI
  1.0.71 list) and per-band effort (medium/medium/high). Effort applied via a
  per-run temp COPILOT_HOME settings.json (config-only key — no CLI flag
  exists; trust state seeded, operator's live ~/.copilot never touched);
  `--effort` flag overrides; resolved effort recorded per ledger row
  (`cli-default` when unpinned — the condition is never silently unknown).
  Report now groups by skill × tier × model × effort. Model-version note:
  Copilot model strings carry family versions; provider snapshot pins aren't
  exposed — a silent backing change surfaces as a rate shift with all
  recorded versions constant (the ledger's residual category).

## [1.1.0] — 2026-07-20

### Added

- **Model policy** (operator correction at first live runs — evals must run
  under the model each skill actually runs with, never a flat cheap default):
  `references/model-policy.yaml` — default `claude-fable-5` (mined from the
  session archive, ~95% of turns), sonnet band for research/scanning skills,
  opus band for heavy-synthesis skills. Resolution: `--model` flag > case >
  eval-set > policy band > policy default; resolved model + source recorded
  per ledger row. `--model` no longer defaults to haiku (smoke tests must ask
  for it explicitly).

## [1.0.1] — 2026-07-20

### Fixed

- Grading-bug caught live in the first DoD run (read-the-transcripts discipline
  working as designed): verdicts were routed by the CLI `--tier` filter instead
  of each case's own tier, so with `--tier all` trigger cases hit the checks
  branch with zero checks — `all([]) == True` — and vacuously passed
  (`loaded=[]` yet PASS). Verdicts now route by case tier; execution cases
  without checks fail explicitly (`none-defined`). Tainted rows remain in the
  ledger attributed to harness 1.0.0 (append-only; corrections are new rows).

## [1.0.0] — 2026-07-20

### Added

- Initial release (MV46 S1; epic E21; design:
  `system/plans/skill-eval-harness.md`).
- `scripts/eval_runner.py`: run / report / sync subcommands; CHECK_REGISTRY
  (7 deterministic checks); trigger verdicts from transcript skill-load
  events; timeout→`error` (never graded); `--max-runs` cost cap; retirement
  tier via temp symlink-mirror workspace (advisory until CLI symlink
  discovery confirmed).
- `references/eval-cases-schema.md`: eval-cases.yaml schema v1 (both trigger
  directions, per-mode execution cases, positive + negative assertions,
  class carve-outs, per-set `version`, corpus `source`/`corpus_waivers`).
- Ledger home `system/ops/evals/` (append-only JSONL, full attribution:
  model + skill/eval-set/harness versions; transcripts saved per run).
- Probe-validated against the live CLI 1.0.71 (2026-07-20): skill-load
  events machine-parseable, deny-tool markers clean, `gh` token auth works.
