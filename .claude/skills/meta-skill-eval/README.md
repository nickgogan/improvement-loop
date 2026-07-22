# meta-skill-eval

The eval **execution layer** (MV46, epic E21): runs skill evals as programs
through the real Codex CLI and accounts for every result in an append-only,
fully-attributed ledger. Sibling to `meta-skill-author` — that skill authors
and scores skills; this one executes their eval sets.

## What it does

- **run** — executes a skill's `evals/eval-cases.yaml` (schema:
  [references/eval-cases-schema.md](references/eval-cases-schema.md)) through
  `codex exec --ephemeral --json` in isolated per-case contexts: trigger tier
  (should/should-NOT, verdict only from explicit JSONL skill-load events), execution tier (per-mode
  Given/When/Then with deterministic checks), retirement tier (skill omitted
  from an isolated workspace — does the model still need it?). Mutating tools
  are constrained by a read-only sandbox by default; 3-trial default; `--max-runs`
  cap aborts oversized plans. Current builds that expose no skill-load event
  record trigger evidence as unavailable rather than guessing from model prose.
- **report** — pass rates, capability→regression graduation, saturation and
  retirement flags, per skill × tier × model, computed from the ledger.
- **sync** — deterministic corpus-drift check against
  `system/ops/self/eval-candidates.md`; exit 1 on drift.

## Where results live

`system/ops/evals/` — `ledger.jsonl` (one row per case×trial: model,
skill/eval-set/harness versions, verdict, checks, transcript pointer) and
`transcripts/<run-id>/` (the evidence; read them — surprising scores are
grading-bug hypotheses first).

## Quick start

```bash
.venv/bin/python .github/skills/meta-skill-eval/scripts/eval_runner.py run --skill ops-doc-sync --model gpt-5.6-sol --dry-run
.venv/bin/python .github/skills/meta-skill-eval/scripts/eval_runner.py run --skill ops-doc-sync --model gpt-5.6-sol --trials 1
.venv/bin/python .github/skills/meta-skill-eval/scripts/eval_runner.py report
.venv/bin/python .github/skills/meta-skill-eval/scripts/eval_runner.py sync
```

## Requirements

Codex CLI with a logged-in user session, Python 3.11, and PyYAML. Paid runs name
the model explicitly unless an eval set deliberately pins one; personal Codex
settings are never copied into repository policy. Runs cost real tokens —
nothing here is ever scheduled.

## Design authority

`system/plans/skill-eval-harness.md` · intake
`system/ops/research/2026-07-20-skill-eval-sophistication.md` · epic E21.
