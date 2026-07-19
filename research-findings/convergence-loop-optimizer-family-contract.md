---
name: Convergence-Loop Optimizer Family — One Shared Contract, One Router, Per-Artifact Members
summary: 'A family of six artifact optimizers (code, prose docs, prompts, skills, SQL, UI design) all implement one shared contract: multi-pass audit with distinct lenses, five-level severity rating (Blocker
  > High > Medium > Low > Nit), fix every Medium+ finding in place, verify-gate every fix (back out regressions), and loop until no Medium-or-higher finding remains or an iteration cap is hit (typically
  3, raised to 5 while findings still drop ≥50% per iteration). A logic-free router skill (deep-optimizer) picks the right member; each member differs only in lens set and verify gate.'
implementation_notes: 'The engine''s /assess-* skills implement the audit half of this contract (multi-lens findings with severity) but stop at reporting — no fix-in-place, no verify gate, no convergence
  criterion; "re-run until no Medium+ remains" is a concrete upgrade path that turns assessments from reports into quality gates while keeping generator-assessor separation (the verify gate and blind re-audit
  are exactly the independent-verifier discipline the engine already enforces via rule 10). The one-router-plus-members shape is also relevant to the asset-catalog form question: the family exposes ONE
  always-on description (the router) rather than six, which is the hub-and-spoke economics applied to a skill family — and it matches the engine''s existing dispatch-table pattern (route, never re-implement).
  The per-artifact verify-gate column (build+lint+tests for code, fact-check for prose, held-out eval for prompts, trigger+collision eval for skills, EXPLAIN parity for SQL) is a ready-made template for
  what "verify" means per engine artifact type.'
category: Evaluation
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: headless-multi-pass-iterative-review.md
  rel: same-problem
- file: self-improvement-dispatch-table-route-never-reimplement.md
  rel: same-problem
- file: skill-smells-triage-layer-before-full-audit.md
  rel: same-problem
- file: dr-research-to-skill-gated-pipeline.md
  rel: enables
pipeline_status: synthesized
consumed_by:
- eval-driven-improvement-loops.md
tags:
- convergence-loop
- severity-scale
- optimizer-family
- quality-gates
---

# Convergence-Loop Optimizer Family — One Shared Contract, One Router, Per-Artifact Members

## What It Is

A single quality-engine contract (defined once, in `convergence-and-severity.md`) that
six different artifact optimizers implement:

1. **Multi-pass audit** — each pass is a distinct *lens* (structure, accuracy, voice,
   security, …); independent passes run in parallel bundles.
2. **Severity rating** — every finding is rated `Blocker > High > Medium > Low > Nit`.
3. **Fix in place** — every Medium+ finding is fixed, not just reported.
4. **Verify gate** — re-render / build / lint / test / re-eval after fixing; any change
   that regresses is backed out.
5. **Convergence loop** — re-audit and repeat until **no Medium-or-higher finding
   remains** or a budget/iteration cap is hit (typically 3 iterations, raised to 5 if
   findings are still dropping ≥50% per iteration).

`deep-optimizer` is the family's router — it contains no optimization logic of its own
and only selects the right member:

| Member | Target | Passes | Verify gate |
|---|---|---|---|
| `code-deep-optimizer` (/cdo) | source files/repos | ~19 | build + lint + tests |
| `document-critique` (/ddo) | prose docs | 0–14 | fact-check + anti-AI-ism |
| `prompt-deep-optimizer` (/pdo) | production prompts | 16 | champion-challenger held-out eval |
| `skill-optimizer` (/sko) | SKILL.md files | 15 | trigger eval + collision check + sync |
| `deep-query-optimizer` (/dqo) | SQL | — | EXPLAIN plan + result parity |
| `design-deep-optimizer` (/deso) | UI/UX screens | 11 | re-render + contrast + axe |

## Why It Matters

Plain English: "audit" and "improve" are usually two separate, unreliable activities —
reports pile up, fixes regress things, and nobody knows when to stop. This contract fuses
them with an explicit termination condition ("no Medium+ remains") and an explicit safety
condition (verify gate backs out regressions). Defining the contract once and stamping
out per-artifact members means every artifact type in a system gets the same quality
semantics — the difference between members is only *which lenses* and *what counts as
verified*.

## How It Works

- **Severity is the control signal.** Medium is the fix/ignore boundary; High is the
  ship/block boundary (`skill-optimizer`'s sync gate withholds persistence while
  unresolved High findings remain, overridable only explicitly with `--sync-anyway`).
- **The convergence criterion is adaptive.** The cap starts at 3 iterations but extends
  to 5 while the loop is still productive (findings dropping ≥50% per iteration) — a
  budget rule that stops thrash without cutting off real progress.
- **Members carry load-bearing passes.** `skill-optimizer`'s Pass H (trigger-accuracy:
  ~60 headless probes, ≥9/10 positive, ≤1/10 false-positive) and Pass I (collision check
  against siblings) are the empirical checks behind the whole skill taxonomy. Pass H is
  explicitly flagged as a proxy metric — a gamed description can score high — so the
  blind claim-verification gate and anti-pattern checks remain *independent* verifiers
  (Goodhart guard).
- **A structural-only mode exists.** `--meta` runs wiring/registry/validation passes
  without content passes — used to register a skill, validate placement, fix naming, and
  seed deferral edges cheaply.
- **The cross-model gate** optionally routes the blind re-audit through a different
  frontier model (`--cross-model`), decorrelating the verifier from the generator.

## How It Could Fail

- **Fix-in-place without a real verify gate** converts an audit tool into a regression
  generator; the gate is what licenses autonomy.
- **Severity inflation/deflation** silently moves the fix and ship boundaries; the scale
  only works if severity definitions are shared across all members.
- **Convergence theater.** If re-audits are not blind (fresh context), the loop converges
  because the auditor remembers its own fixes, not because the artifact is clean.
