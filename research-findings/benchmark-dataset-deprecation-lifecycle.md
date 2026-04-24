---
name: "Benchmark Dataset Deprecation Lifecycle"
summary: "When a published benchmark's dataset is later found to contain noise that systematically distorts scores, maintainers ship a cleaned replacement dataset and deprecate the original (rather than silently updating in place). Every downstream score inherits a 'which revision was this?' audit question. Plain English: benchmarks aren't static. If the original dataset has bugs, the score everyone quoted last year may have been measuring noise instead of the system."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (benchmark-level governance — HF deprecation documented)"
adoption_status: "Not Yet Started"
priority: P3
applicability:
  - "General"
adopted_in: []
sources:
  - "huggingface-longmemeval-dataset.md"
related_findings:
  - file: retraction-log-as-governance-artifact.md
    rel: extends
  - file: tool-enforced-dev-heldout-split.md
    rel: same-problem
  - file: benchmark-operating-contract.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A benchmark-hygiene pattern applied at the dataset layer, not the scorer or leaderboard layer. When maintainers discover that the originally-published dataset contains noise — ambiguous history sessions, mislabeled ground-truth, distractor sessions that shift outcomes — they ship a new dataset under a different name (e.g., `longmemeval-cleaned`) and explicitly deprecate the original.

The lifecycle:
1. **Discovery** — the maintainers or the community find systematic noise (not one-off bugs) in the dataset.
2. **Cleaned replacement** — a separate, differently-named dataset is published with the noise removed.
3. **Deprecation flag on the original** — the original remains accessible for historical reproducibility but carries a deprecation notice pointing to the replacement.
4. **Publication of the diff** — ideally a delta doc explaining what was removed and why, so downstream consumers can retroactively audit which of their published scores were contaminated.

[[retraction-log-as-governance-artifact]] is the log-level instance (corrections to published results); this finding is the dataset-level instance (corrections to the measurement instrument itself). The relationship is a same-problem / extends: dataset deprecation is retraction-log applied to the benchmark data.

## Why It Matters

Every benchmark score has an implicit dataset-revision dependency. When `xiaowu0162/longmemeval` was deprecated in favor of `xiaowu0162/longmemeval-cleaned`, every pre-deprecation score — MemPalace's 96.6%, Supermemory's 85.0%, Mem0's 66.9%, Zep's 63.8% — became a potentially stale number depending on whether it was run on the noisy original or the cleaned successor. Without the deprecation flag, readers would not know to ask.

For MetaSystem's downstream use of evaluation:
- **`/prompt-evaluator` rubrics** may need to be deprecated and replaced when we discover evaluator drift; a deprecation lifecycle for rubrics is the natural extension.
- **IL guide-synthesis evidence**: findings that cite pre-deprecation benchmark scores need a revision-audit pass when the underlying dataset's deprecation status changes. This is the kind of drift [[feedback_token_economy.md]] warns about — numbers in prose that require per-session maintenance.
- **Memory-architecture design decisions** based on LongMemEval scores should cite the dataset revision, not just the number.

## Why People Are Using It

Observed on [HuggingFace's LongMemEval dataset page](https://huggingface.co/datasets/xiaowu0162/longmemeval) — see [[huggingface-longmemeval-dataset]] for the source entry. The dataset carries an explicit status marker: *"Deprecated — Replaced by longmemeval-cleaned. The original dataset contains noisy history sessions that interfere with answer correctness."* Maintained by the paper's first author (xiaowu0162), so this is an author-initiated correction, not a third-party fork.

The pattern is structurally similar to software package deprecation (semver major-version bumps with deprecation notices) applied to empirical research artifacts. Likely to spread as more benchmarks in the agent-evaluation space mature — LongMemEval is one of many 2024-2026 benchmarks that will face the same post-publication hygiene pressure.

## Potential Alternatives

- **Silently update the dataset in place.** Easy for the maintainer; catastrophic for anyone trying to reproduce past scores. Violates reproducibility norm.
- **Leave the dataset broken and publish errata.** Preserves historical reproducibility; does not help anyone running new evaluations.
- **Fork and maintain only the clean version.** Community forks often do this; lacks the original author's corroborating authority.
- **Publish cleaned as a version suffix** (`longmemeval-v2`, `longmemeval-2026-04`). Similar mechanics; the naming convention signals "same benchmark, fresher cut" rather than "new benchmark." Trade-off: blurs the boundary between cleaning and benchmark evolution.

## Potential Improvements

- **Include a per-question diff doc** that names which questions were removed and why. Downstream systems can then recompute their own historical scores on the pre-clean subset if they need backwards compatibility.
- **Tag each score with the dataset revision.** Leaderboards should record (system, score, dataset revision, judge model, date) as a 4-tuple, not just (system, score).
- **Scheduled re-runs on deprecation.** When a dataset is deprecated, the leaderboard should trigger re-runs for all listed systems against the cleaned version before publishing new rankings.
- **Formalize a benchmark deprecation SemVer.** `longmemeval-1.0` → `longmemeval-1.1` (data cleaning, scores comparable) vs `longmemeval-2.0` (task redefinition, scores not comparable). Today the difference is only in the README.

## Potential Failure Modes

- **Stale-score propagation through the literature.** Papers cite the pre-deprecation number; the citation persists for years after the deprecation. Mitigation: aggregators (like REM Labs) should annotate each listed score with its dataset revision.
- **Cleaned-version gaming.** Once the cleaning diff is public, systems can hand-tune for the differences, producing artificially higher cleaned-version scores. Mitigation: combine with [[tool-enforced-dev-heldout-split]] — clean the held-out set independently of the dev set, and don't publish the diff until after re-runs.
- **Deprecation fatigue.** If datasets deprecate often, readers stop tracking; deprecation starts to mean "stale but functional" rather than "flawed." Mitigation: clear severity tiers — "hygiene update" vs "methodology correction" vs "task redefinition."
- **Loss of comparability across the deprecation boundary.** A system published pre-deprecation can't easily be compared to one published post-deprecation. Mitigation: maintainers should re-run reference systems on the new dataset as part of the deprecation protocol.
