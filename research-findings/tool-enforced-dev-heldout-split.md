---
name: "Tool-Enforced Dev/Held-Out Benchmark Split with Teaching-to-the-Test Self-Disclosure"
summary: "Benchmark integrity as tool property, not social contract: the test set is physically split (e.g., 50 dev / 450 held-out), committed to the repo as a pinned seed, and the runner exposes CLI flags (`--dev-only`, `--held-out`) that prevent accidental contamination. When the team does overfit to specific test items, they disclose it publicly (naming the item hashes) and withdraw the inflated number from headline surfaces."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: benchmark-operating-contract.md
    rel: extends
  - file: cross-provider-benchmarking-framework.md
    rel: same-problem
  - file: external-benchmark-hosting-as-trust-mechanism.md
    rel: same-problem
  - file: benchmark-dataset-deprecation-lifecycle.md
    rel: same-problem
  - file: experimental-sandbox-labeling-discipline.md
    rel: same-problem
  - file: ensemble-eval-majority-required-for-success.md
    rel: same-problem
  - file: production-configuration-baseline-discipline.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A benchmark pipeline that enforces dev/held-out discipline at the tool layer rather than through documentation. Three combined mechanisms:

1. **Committed split file with pinned seed.** A JSON file in the repo (e.g., `benchmarks/lme_split_50_450.json`, seed=42) records which test items are dev vs held-out. Anyone running the benchmark gets the same split.
2. **CLI flags enforce the split.** The runner exposes `--dev-only`, `--held-out`, `--create-split`, `--split-file`. Running `--dev-only` touches only the 50 dev items (safe to iterate); running `--held-out` touches only the 450 held-out items (touch once; any iteration afterward contaminates them).
3. **Public self-disclosure when discipline slips.** When the team develops a fix by examining specific wrong-answer items (classic teaching-to-the-test), the benchmark doc names the item hashes (`d6233ab6`, `4dfccbf8`, `ceb54acb` in MemPalace's case), classifies the fix as teaching-to-the-test, and withdraws the inflated number from all headline surfaces — keeping only the clean held-out score.

## Why It Matters

Most benchmark discipline is social contract: "please don't tune on the test set." Social contracts erode as iteration pressure grows. A tool-enforced split makes the discipline cost-free to follow and expensive to break — you'd have to edit the runner itself to cheat. The self-disclosure pattern completes the loop: when the discipline does slip, the team's incentive is to confess and retract rather than hide, because hiding becomes a bigger reputational risk than the original contamination.

For any retrieval benchmark, eval loop, or prompt-tuning round the IL runs later, baking this in from the start prevents a class of subtle contamination. This extends the existing finding [[benchmark-operating-contract]] (Memongo) from a written invariant to a tool-enforced one with a retraction mechanism on top.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. `benchmarks/BENCHMARKS.md` §"Benchmark Integrity" explicitly states: "In a peer-reviewed paper this would be a significant methodological problem. We're disclosing it here rather than letting it sit unexamined." The 99.4% → 100% step was developed by examining three specific questions. The 100% number was withdrawn from README and website headlines (per [[retraction-log-as-governance-artifact]] entry 2026-04-14); the honest held-out score (98.4% R@5 on 450 unseen questions) is the published figure.

## Potential Alternatives

- **Written-only benchmark governance** — e.g., Memongo's `benchmark-operating-contract.md`. Strong invariants, no tool enforcement. Discipline is per-session.
- **Separate test harnesses** — running tuning on one tool and final evaluation on a different tool. Effective but adds friction.
- **External held-out sets** — the dataset maintainer holds the held-out split. Harder to self-serve in OSS projects.

## Potential Improvements

- Commit-level CI check that refuses a PR if the `--held-out` run has been invoked more than N times in the commit's branch history.
- Public dashboard that records the number of held-out runs per release, so contamination risk is visible.
- Require a retraction-log entry as part of the claim-publishing PR checklist (couples this finding with [[retraction-log-as-governance-artifact]]).

## Potential Failure Modes

- **Dev-set overfitting** — tuning freely on dev still produces optimistic estimates if the dev set is too small or not representative. MemPalace's 50/450 split is vulnerable here; the 1.6pp gap between dev (100%) and held-out (98.4%) is the measured contamination signal.
- **Retro-split contamination** — if the split is created after tuning has already occurred, the "held-out" set was effectively seen during development.
- **Flag bypass** — if the runner's default behavior runs on the full set, forgetting a flag silently contaminates. Safer default: require an explicit flag to run on the full set.
