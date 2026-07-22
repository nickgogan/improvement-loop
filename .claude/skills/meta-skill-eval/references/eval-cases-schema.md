# eval-cases.yaml schema (v1)

One structured eval-set per skill at `.github/skills/<skill>/evals/eval-cases.yaml`.
Supersedes the prose `trigger-eval.md` (C16 amendment shipped at MV46 S2; the prose
sets were migrated and deleted — they live in git history before the S2 commit).
Parsed by `scripts/eval_runner.py`; design:
`system/plans/skill-eval-harness.md`.

```yaml
skill: tool-resume-render   # must match the directory name
version: 1                  # eval-SET version — bump on any semantic case change
updated: 2026-07-20         # date of the last semantic change — ALWAYS set with
                            # a version bump (paired rule; enables staleness
                            # queries; git holds the full forensic trail)
class: script-core          # objective | subjective | script-core (carve-out routing)
value_class: ""             # optional: capability-uplift | encoded-preference;
                            # selects the baseline question, not runner behavior
harness: ""                 # `excluded` = no paid LLM runs for this skill — pure
                            # tool-wrappers whose correctness is binary script
                            # behavior (operator-gated per skill; run mode refuses)
model: ""                   # optional set-level override; default resolves via
                            # references/model-policy.yaml (run under the model the
                            # skill actually runs with — never a flat cheap default)
corpus_waivers: []          # hex8 session keys from eval-candidates.md rows that
                            # deliberately have no case (reason in a YAML comment)
cases:
  - id: t01                 # unique in file; t* trigger, x* execution by convention
    tier: trigger           # trigger | execution
    query: "Render the finalized resume to PDF"
    should_trigger: true    # trigger tier only; false = should-NOT (near-miss)
    expect_instead: ""      # abstain cases: the sibling skill that should serve
    source: ""              # provenance: corpus hex8 key, "trigger-eval.md #3",
                            # or "synthetic" — sync mode matches corpus keys here
    note: canonical

  - id: x01
    tier: execution
    mode: render            # the skill mode this case exercises (per-mode coverage)
    given: A finalized clean resume markdown exists in a role folder
    when: Asked for page fit via a rendered PDF
    query: "How many pages is my resume? Can you render it as a PDF?"
    allow_tools: []         # default: Codex read-only sandbox. Shell reads remain
                            # available; list "write" only with a comment justifying
                            # an isolated workspace-write trial.
    hitl: false             # true = subjective carve-out: run executes, checks
                            # advisory, human scores via the named scorecard
    scorecard: ""           # subjective skills: pointer to their qualitative rubric
    failure_category: specification-violation
                # optional expected category if this case fails
    checks:                 # ALL must pass (binary verdict; outcome-not-path)
      - {check: skill_loaded, skill: tool-resume-render}
      - {check: response_contains, pattern: "render_resume\\.py"}
    source: "probe 2026-07-20"
    note: shell denied -> guidance path is the correct degraded outcome
```

## Check registry (deterministic, grows from real needs only)

| check | params | passes when |
|---|---|---|
| `skill_loaded` | `skill` | Codex JSONL records an explicit structured skill-load event for it |
| `skill_not_loaded` | `skill` | explicit structured skill-load evidence exists and omits it |
| `transcript_contains` | `pattern` (regex) | pattern found in the full transcript |
| `transcript_not_contains` | `pattern` | pattern absent from the transcript |
| `response_contains` | `pattern` | pattern found in the final response (stdout) |
| `response_not_contains` | `pattern` | pattern absent from the final response |
| `exit_zero` | — | CLI exit code 0 |
| `no_ban_terms` | — | no term from the host-local `.github/export-ban-terms.txt` appears in response or transcript (vacuous pass when the file is absent — nothing private to leak); leakage-probe primitive (MV48 G) |

Negative assertions (what bad looks like — ban-terms, invented evidence, skipped
gates) are first-class: use `*_not_contains` seeded from the lessons store + L-3
corpus. Trigger tier needs no `checks` — the verdict is the explicit skill-load
event vs `should_trigger`. If the installed Codex build exposes no such event,
the result is `error`/unavailable, never inferred from agent prose.

## Output-failure taxonomy

Execution cases may declare one `failure_category`; failed ledger rows record it.
Subjective failures set the same field through `score --failure-category` (default:
`below-threshold-quality`). Allowed values:

- `incomplete-solution` — artifact exists but required components are absent
- `missing-output` — no requested artifact or answer
- `specification-violation` — output exists but violates an explicit contract
- `below-threshold-quality` — subjective quality misses the approved scorecard
- `domain-knowledge-gap` — procedure/output uses incorrect domain knowledge
- `safety-or-governance` — a gate, confidentiality rule, or side-effect guard fails
- `runtime-error` — harness/agent execution did not produce gradeable evidence
- `uncategorized` — legacy/default only; author new cases with a narrow category

When deterministic artifact verification is feasible, case authoring also supplies a
known-good oracle artifact/run and proves it passes every verifier. A verifier that
cannot pass its oracle is broken evidence, not a hard eval. Keep checks parsimonious
and distinct.

## Class carve-outs

- **objective** — full checks; the default.
- **subjective** — output quality is human-scored: mark execution cases
  `hitl: true` + `scorecard:` pointer; deterministic checks still guard
  structure/ban-terms; the harness records the run and flags for human scoring.
  The human score lands via `eval_runner.py score` as a `human-scored` ledger
  row under the judge-verdict schema v1 (`judge-verdict-schema.md`, MV48 D) —
  subjective skills trend in the ledger too.
- **script-core** — tier-2 correctness belongs to the script's own tests;
  execution cases here only assert the skill routes to its script correctly.
  The extreme of this class — a **pure tool wrapper** (thin operating model
  around one deterministic script) — may be `harness: excluded` entirely
  (operator call, per skill): its pass/fail is "did the script run when
  invoked," observable free in real usage; paid LLM runs add nothing.

## Grading rules (inherited from the design)

- Binary verdicts; grade outcomes, not step sequences.
- **Deterministic-first (operator directive, 2026-07-20):** prefer check-registry
  assertions (regex/string/exit-code) over `hitl`/scorecard scoring wherever a
  behavior can be pinned textually; the subjective carve-out covers output
  *quality* only — structure, ban-terms, and gate-firing assert deterministically
  on every class.
- **Output-first investment (operator correction, 2026-07-20):** prioritize
  execution/output correctness and completeness; adversarial/safety second; trigger
  accuracy third as a bounded routing smoke. After description changes, sample
  changed/representative trigger cases at one trial. Use 3-trial trigger distributions
  only for a specific routing investigation, never as a release gate.
- Execution/adversarial runs default 3 trials; read distributions, not single runs.
- **Diagnostic routing:** final output is the primary score. Inspect trajectories for
  failures, surprising passes, case graduation, and model/harness changes; use ordered
  subsequence/step checks only where the procedure is genuinely deterministic. Sample
  less once review stops revealing new failure categories. Single-step checks localize
  critical boundaries but never substitute for end-to-end output evaluation.
- Every run is isolated (fresh CLI context per case×trial).
- Ledger rows carry model + skill/eval-set/harness versions — full attribution.
- Model resolution: `--model` flag > case/set `model:` > optional policy default.
  The repository policy intentionally has no default, so paid runs normally
  require `--model`; both model and resolution source are recorded per ledger row.
- Portability (MV48): `sync` passes cleanly on a host with an absent/empty
  corpus (fresh user/machine — coverage accrues from first capture); exported
  `source:` hex8 keys are provenance-only and unresolvable on receiving hosts.
  Cases ship in the export set — zero user-specific content, enforced by the
  separability scan (audit C6 + export dry-run, `.yaml` covered).
