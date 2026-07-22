# Judge-verdict schema (v1) — MV48 D minimal

The typed shape for **non-deterministic scoring** wherever it happens in this
workspace — human scorecard scoring of `hitl` eval cases (the primary consumer, via
`eval_runner.py score`), and doc-level adoption by sibling skills that already score
subjectively (`profile-voice` voice scoring, `meta-skill-author` §2.2 assessor
grading). Deterministic-first stands (operator directive, 2026-07-20): this schema
never replaces check-registry assertions — it types the narrow subjective carve-out so
those verdicts can land in the ledger and trend.

```yaml
judge_verdict:
  version: 1              # schema version
  overall_pass: true      # binary — the only field graduation logic reads
  score: 82               # 0–100 against the named scorecard
  failure_category: null  # required on fail; enum in eval-cases-schema.md
  scorer: human           # human | model — v1 ships human-only; a model scorer
                          #   requires judge-model separation (explicit non-goal
                          #   until a surface needs it)
  scorecard: ".github/skills/profile-voice/references/scoring-rubric.md"
  checks:                 # per-check breakdown, mirrors the deterministic shape
    - id: human-scorecard
      pass: true
      note: "voice register consistent; two hedge-words flagged"
```

## Rules

- **A score row must reference a real run** — `eval_runner.py score` refuses run-id /
  case-id pairs absent from the ledger (never score imagined output).
- Score rows append with `verdict: human-scored` and full attribution (skill,
  eval-set, harness versions, model of the scored run); the ledger stays append-only —
  a re-score is a new row.
- `overall_pass` derives from `score >= pass-threshold` (default 70, per-invocation
  flag); the threshold used is implicit in the row's `overall_pass` — thresholds are
  policy, the score is the datum.
- Sibling adopters (profile-voice, §2.2 grading) emit this shape in their own
  artifacts; they do **not** write to this ledger — only `score` does, and only for
  hitl eval cases.

## Model-judge activation guard

V1 remains human-scored. A future model scorer is admitted only after:

1. enough human-labeled rows and written critiques exist for the target scorecard;
2. the model judge is evaluated blind against those rows in a separate context;
3. precision and recall are reported per failure class (raw agreement is insufficient
  when passes/failures are imbalanced); and
4. periodic human sampling remains in place after activation.

Until those conditions hold, model-judge automation is not a degradation — it is an
unvalidated source of labels and stays off.

## Non-goals (v1)

Judge-model separation, LLM-judge automation, versioned rubric registries — deferred
behind the activation guard above, not carried as an open Backlog item.
