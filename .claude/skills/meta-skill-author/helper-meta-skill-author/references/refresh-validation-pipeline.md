# Refresh Validation Pipeline

> Reference doc for the `helper-meta-skill-author` internal helper.
> Path basis: bare package paths (`SKILL.md`, `references/`, `adapters/`,
> `SOURCES.md`) are relative to the **target `meta-skill-author` package root**
> — i.e. `../` from this helper. The helper resolves them one level up.
> Detailed spec of the 5-step sandbox-first validation pipeline
> used in Apply mode. Portable across all five platforms
> (Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Perplexity).
> No platform-specific features referenced.
> Every substantive claim cites a finding from the master inventory.

---

## 1. The 5-Step Pipeline [sandbox-first-modification-validation]

Before any modification is committed to the live skill package, Apply
mode runs all five steps in order. The pipeline is derived from the
HyperAgents governance framework (ICLR 2026, Meta FAIR / UBC / Vector
Institute), which reported 78–92% of proposed modifications maintaining
or improving performance, forced rollbacks 8–22%, and undetected
regressions under 1% [sandbox-first-modification-validation].

Every step has a defined pass condition, a fail condition, and a
rollback trigger. Steps do not execute concurrently; Step N+1 does
not start until Step N passes.

---

### Step 1: Sandbox Isolation

**Purpose:** Prevent partial writes from corrupting the live package.
All edits happen in an isolated shadow directory. The live package
is read-only for the duration of the refresh run.

**Inputs:**
- The current live skill package (read-only source)
- The set of proposals approved for this Apply run

**Outputs:**
- `refresh-candidate/` — a full copy of the live skill package with
  the approved proposals applied as file edits

**Setup procedure:**
1. Copy the entire live skill package to `refresh-candidate/`
   (sibling of the live package, never inside it).
2. Apply each approved proposal as a file edit in `refresh-candidate/`.
3. Record the copy timestamp and the list of proposals applied in
   the run's audit log entry (§7).

**Pass condition:** `refresh-candidate/` exists, is a complete copy
of the live package, and all proposal edits have been applied without
file-system error.

**Fail condition:** Copy fails (disk space, permission error) or any
proposal edit produces a write error.

**Rollback trigger:** On fail, delete `refresh-candidate/` and
log the error. No changes have reached the live package; no rollback
of the live package is needed.

**Why sandbox-first:** Applying changes directly to the live package
and rolling back on failure risks partial state if the process is
interrupted. The sandbox guarantees the live package is never touched
until Step 5 approval [sandbox-first-modification-validation].

---

### Step 2: Deterministic Validation Gate

**Purpose:** Run mechanical checks before any LLM evaluation. Structural
violations caught here cost zero inference tokens and are 100%
reproducible [bmad-deterministic-skill-validator].

**Inputs:**
- The `refresh-candidate/` directory

**Outputs:**
- A structured validation report listing pass/fail per rule
- An overall PASS/FAIL verdict for this step

**Rules applied (19 rules across 6 categories, derived from BMAD
reference implementation [bmad-deterministic-skill-validator]):**

*Category 1 — Naming conventions:*
- SKILL.md file name must be uppercase (`SKILL.md`, not `skill.md`)
- Directory name must match the `name` frontmatter field
- `name` field: 1–64 chars, `[a-z0-9-]` only, no leading/trailing/
  consecutive hyphens, no reserved words (`anthropic`, `claude`),
  no XML angle brackets [skill-frontmatter-validation-rules]

*Category 2 — Variable usage:*
- No undeclared variables referenced in body
- No reserved words in description field
- Description field: non-empty, no XML tags [skill-frontmatter-validation-rules]

*Category 3 — Path references:*
- All `references/` and `adapters/` cross-references use relative paths
- No absolute file paths in SKILL.md body
- No internal implementation path leakage (PATH-05 encapsulation rule)

*Category 4 — Invocation syntax:*
- Correct skill invocation language (REF-03: no harness-specific
  invocation syntax in the portable layer)
- No Claude Code-only frontmatter extension fields in open-standard
  portable sections [skills-as-open-portable-standard]

*Category 5 — Sequence correctness:*
- Required sections present in canonical order
- SKILL.md body within 500-line limit [skill-as-directory-progressive-disclosure-three-levels]
- `description` field within 1,024-char limit [skill-description-structure-what-when-capabilities]

*Category 6 — Encapsulation boundaries:*
- No embedded context that duplicates content in `references/`
  (pointers over copies) [skill-as-package-export-with-references]
- Each `references/` file linked by relative path, not by content
  copy in the body
- `SOURCES.md`: every finding cited anywhere in the package must
  have an entry (completeness check; see §4)

**Pass condition:** All 19 rules pass in `refresh-candidate/`.

**Fail condition:** Any rule fails.

**Rollback trigger:** Delete `refresh-candidate/`. Report the failing
rules to the audit log. No LLM evaluation runs until structural
violations are resolved — fixing structural errors first prevents
misdiagnosing a structural problem as a semantic one [bmad-deterministic-skill-validator].

---

### Step 3: Regression Eval Gate [capability-vs-regression-eval-lifecycle]

**Purpose:** Confirm that the proposed changes do not cause any
previously-working behavior to degrade below the baseline threshold.

**Inputs:**
- `refresh-candidate/` (the modified package)
- The skill package's regression eval suite
- The baseline pass rate recorded at the last successful commit

**Outputs:**
- Per-eval pass/fail results
- Aggregate pass rate
- Delta from baseline

**Procedure:**
1. Run the full regression eval suite against `refresh-candidate/`.
   The executor must be a separate agent context from the one that
   generated the proposals — generator-assessor separation is required
   here [generator-assessor-separation-in-skill-iteration].
2. Compute the pass rate as `(passing evals) / (total regression evals)`.
3. Compare against the stored baseline pass rate.

**Pass condition:** Regression eval pass rate ≥ baseline pass rate
(the threshold is stored in `refresh-runs/snapshot.yaml` as
`regression_baseline_pass_rate`). A rate of ≥ 95% is the recommended
floor; if the baseline is already below 95%, use the baseline value.

**Fail condition:** Regression eval pass rate drops below baseline.

**Rollback trigger:** Delete `refresh-candidate/`. Log the failing
evals, the delta from baseline, and which proposals were applied.
This data is preserved in the run's audit log so Propose mode can
use it to identify which proposal caused the regression.

**New capability evals:** If any proposal introduces a new concept,
it must include at least one capability eval case. That capability
eval is not part of the regression suite until it graduates
(≥ 95% pass rate sustained over 3+ consecutive runs)
[capability-vs-regression-eval-lifecycle]. The capability eval must
pass at least once before the proposal is eligible for Apply mode.

**Why separate executor:** An executor that knows what changes were
proposed will structurally tend to confirm their correctness —
sycophancy bias documented in [holdout-validation-pattern-blind-regression].
The regression eval executor receives only the eval suite and the
`refresh-candidate/` package; it does not receive the proposals or
the authoring session context.

---

### Step 4: Held-Out Description Re-Validation
[skill-description-optimization-loop-held-out-test]

**Purpose:** If any `description` field was modified in any file in
`refresh-candidate/`, confirm the modified description does not
degrade triggering accuracy compared to the baseline description.

**Inputs:**
- The modified description(s) in `refresh-candidate/`
- The baseline description(s) from the live package
- The 20-query held-out eval set for the relevant skill(s) (stored at
  `refresh-runs/eval-sets/<skill-name>-description-eval.yaml`)

**Outputs:**
- Per-description TEST score (held-out 40% of the eval set)
- Pass/fail verdict per modified description

**Procedure:**
1. Check whether any `description` field differs between
   `refresh-candidate/` and the live package. If none differ, skip
   Step 4.
2. For each modified description, run the held-out description
   optimization check:
   - Use the pre-split 20-query eval set (8–10 should-trigger +
     8–10 should-not-trigger, 60/40 train/test split)
     [skill-description-optimization-loop-held-out-test]
   - Run each test-set query 3 times for reliability
   - Compare the new description's TEST score against the baseline
     description's TEST score
3. If the TEST score does not regress (new ≥ baseline): pass.
4. If the TEST score regresses: revert only the description change;
   keep the body change. The body can still be committed without the
   description change.

**Pass condition:** Every modified description's TEST score ≥ baseline
TEST score.

**Fail condition (partial rollback):** A modified description's TEST
score is below baseline. Only the description edit is reverted in
`refresh-candidate/`; the associated body edit is preserved. This
is the one step that applies a partial rollback rather than a full
rollback — the goal is to preserve body improvements while preventing
description degradation.

**Why TEST score, not train score:** A description optimized only on
the training set may perfectly trigger on training queries while failing
on held-out queries (overfitting). Selection by TEST score prevents
this. [skill-description-optimization-loop-held-out-test]

**Eval set location:** Each skill in the package must have a
description eval set at `refresh-runs/eval-sets/<skill-name>-description-eval.yaml`.
If the eval set is missing, this step is skipped with a warning
logged to the audit log. The refresher SKILL.md should flag missing
eval sets as a non-blocking issue requiring attention before the
next refresh run.

---

### Step 5: Diff Review and Versioned Commit

**Purpose:** Present the complete set of changes to the human for
approval before writing anything to the live package. Archive the
previous version as a named rollback target on approval.

**Inputs:**
- `refresh-candidate/` (fully validated in Steps 1–4)
- The live skill package (current state)
- The audit log entry for this run

**Outputs (on approval):**
- The live package updated with all changes from `refresh-candidate/`
- A named rollback target archived in `refresh-runs/`
- The audit log entry completed with approver identity and timestamp

**Outputs (on rejection):**
- `refresh-candidate/` deleted
- The audit log entry closed with rejection reason

**Procedure:**
1. Generate a PR-style unified diff between the live package and
   `refresh-candidate/`. Present it to the human in a format they
   will actually read (structured text, not a raw file dump)
   [html-output-as-human-in-the-loop-restorer].
2. Apply the HITL tier from each proposal's `hitl_tier` field to
   determine the required approval level:
   - `Full Autonomy`: no human approval required (proceed automatically)
   - `Guarded`: present diff; auto-approve unless human objects within
     a configurable window
   - `Proposal-first`: present diff; require explicit human approval
     before proceeding
   - `Human-required`: present diff; no proceed without explicit
     human sign-off; used for any change to SKILL.md frontmatter,
     SOURCES.md, or governance documents
     [agent-action-reversibility-as-design-requirement]
3. On approval: copy `refresh-candidate/` contents to the live
   package; archive the prior package state under a versioned name
   in `refresh-runs/rollback-targets/<timestamp>/`.
4. On rejection: delete `refresh-candidate/`; record rejection reason
   in the audit log.

**Pass condition:** Human approval received (or `Full Autonomy` tier
applies to all changes).

**Fail condition:** Human rejects, or the diff presentation step
fails.

**Rollback trigger:** On rejection, no live package changes occur.
`refresh-candidate/` is discarded. The audit log records the
decision. The manifest entries for the rejected proposals are
updated to `deferred` status.

---

## 2. Pass / Fail Decision Tree

```
APPLY MODE STARTS
      │
      ▼
Step 1: Sandbox Isolation
      │  FAIL → delete sandbox; log error; STOP
      │  PASS
      ▼
Step 2: Deterministic Validation Gate (19 rules)
      │  FAIL → delete sandbox; report failing rules; STOP
      │         (fix structural violations before re-running)
      │  PASS
      ▼
Step 3: Regression Eval Gate
      │  FAIL → delete sandbox; log failing evals + delta; STOP
      │         (identify which proposal caused regression;
      │          revise proposal before re-running)
      │  PASS
      ▼
Step 4: Description Re-Validation
      │  description unchanged → SKIP this step
      │  description changed, TEST score ≥ baseline → PASS
      │  description changed, TEST score < baseline →
      │         PARTIAL ROLLBACK: revert description edit only;
      │         body edit preserved; continue to Step 5
      ▼
Step 5: Diff Review
      │  Human rejects → delete sandbox; log decision; STOP
      │  Human approves (or Full Autonomy tier) →
      ▼
COMMIT: copy sandbox to live; archive rollback target;
        update audit log; update manifest entry status to "applied"
```

---

## 3. Rollback Procedure

Rollback is a design requirement, not a recovery option
[agent-action-reversibility-as-design-requirement].

### 3.1 Named Rollback Targets

Every successful Apply run archives the prior package state as a
named rollback target:

```
refresh-runs/
  rollback-targets/
    20260623-1430/        ← timestamp of the Apply run that replaced it
      SKILL.md
      references/
      adapters/
      SOURCES.md
      _rollback-meta.yaml ← records: run_id, proposals_applied, approver
```

### 3.2 Rollback Execution

To revert the live package to a rollback target:

1. Identify the rollback target directory in `refresh-runs/rollback-targets/`.
2. Confirm the rollback with human approval (always `Human-required`
   tier — reverting a commit is a persistent mutation of the skill
   package) [advisory-only-for-persistent-mutations].
3. Copy the rollback target contents to the live package directory,
   overwriting current contents.
4. Log the rollback in the audit log with: run_id being rolled back,
   rollback target timestamp, approver identity, and reason.

### 3.3 Automatic Rollback (Steps 1–3)

Steps 1–3 trigger automatic rollback of the sandbox (deleting
`refresh-candidate/`) on failure. This is not a rollback of the live
package — the live package was never touched. The term "rollback"
at Steps 1–3 means discarding the sandbox.

Steps 4–5 involve no automatic rollback of the live package because
the live package is not modified until Step 5 approval.

### 3.4 Audit Log for Rollbacks

Every rollback (sandbox discard OR live package reversion) produces
a structured audit log entry (§7) that includes:

- The run ID that is being rolled back
- The step at which the decision was made
- The reason (failing rule, failing eval, human rejection)
- Whether the live package was affected (yes only for Step 5 rejections
  after approval was already granted — rare but must be logged)

---

## 4. Per-File Validation Rules

These rules are applied within Step 2 (deterministic gate) and
Step 3 (regression eval) to each specific file type in the package.

### 4.1 SKILL.md

| Rule | Constraint | Source |
|------|------------|--------|
| File length | ≤ 500 lines | [skill-as-directory-progressive-disclosure-three-levels] |
| `description` field | ≤ 1,024 chars; three-part structure (what + when + capabilities); no XML | [skill-description-structure-what-when-capabilities] |
| `description` + `when_to_use` combined (Claude Code only) | ≤ 1,536 chars | [skill-description-budget-context-overflow] |
| Every finding cited | Must appear in SOURCES.md | [skill-as-package-export-with-references] |
| No reasoning-model anti-patterns | No explicit CoT, few-shot examples, self-consistency, least-to-most, skeleton-of-thought | [reasoning-model-anti-pattern-prescribed-reasoning] |
| L0 abstract present | First ~100 tokens must stand alone as the skill orientation | [progressive-tiered-context-loading-convergence] |
| Stop Rules present | Explicit halting conditions required in body | [intent-engineering-framework-seven-part-agent-inten] |
| HITL tier declared | Each side-effect action must have an assigned tier | [agent-action-reversibility-as-design-requirement] |
| No prohibited frontmatter in portable sections | Open-standard fields only where portability is declared | [skills-as-open-portable-standard] |

### 4.2 Reference Documents (`references/`)

| Rule | Constraint | Source |
|------|------------|--------|
| Line range | Within the document's declared target range (see each doc's header) | [skill-as-directory-progressive-disclosure-three-levels] |
| Cross-references | All `references/` and `adapters/` paths resolve to actual files in the package | [skill-as-package-export-with-references] |
| Citation coverage | Every claim cites a finding via `[finding-filename]` | [bmad-deterministic-skill-validator] |
| No content duplication | Reference docs must not duplicate prose from SKILL.md body; pointers over copies | [skill-as-package-export-with-references] |

### 4.3 Adapter Documents (`adapters/`)

| Rule | Constraint | Source |
|------|------------|--------|
| Platform-matrix consistency | All platform claims must be consistent with `references/platform-matrix.md`; conflicting claims are flagged | [multi-ide-portability-via-installer-templates] |
| "Unknown — verify" labels | Any capability not confirmed by findings must carry the label "Unknown — verify against current docs" | [multi-ide-portability-via-installer-templates] |
| Portability constraint | Adapter docs must not introduce non-portable instructions into the portable layer body | [skills-as-open-portable-standard] |

### 4.4 SOURCES.md

| Rule | Constraint | Source |
|------|------------|--------|
| Completeness | Every `[finding-filename]` cited anywhere in the package must have a row in SOURCES.md | [skill-as-package-export-with-references] |
| URL freshness | Rows marked with stale URLs must be flagged (the refresher checks URLs with a HEAD request) | [benchmark-dataset-deprecation-lifecycle] |
| Multiply-cited sources table | Any source cited in ≥ 2 findings must appear in the multiply-cited sources table | [skill-as-package-export-with-references] |

---

## 5. Generator-Assessor Separation in the Pipeline
[generator-assessor-separation-in-skill-iteration]

The model running Apply (the generator-executor) must not be the
same context running the regression eval (the grader). This is the
load-bearing architectural rule for validation quality.

> "The skill-creator NEVER both generates and assesses the same
> artifact in the same context."
> [generator-assessor-separation-in-skill-iteration]

### 5.1 Five-Role Architecture Mapping

| Role | Context | Responsibility in Refresh Pipeline |
|------|---------|-------------------------------------|
| **Generator** | The authoring session that wrote the proposals | Drafts proposal edits; does not run evals |
| **Executor** | Apply mode — separate context | Applies edits in sandbox; does not evaluate correctness |
| **Grader** | Step 3 eval runner — fresh context | Runs regression eval suite against `refresh-candidate/`; does not know which proposals were applied |
| **Comparator** | Step 4 description validator | Runs blind A/B between old and new descriptions; receives only the descriptions, not the proposals |
| **Analyzer** | Audit log writer — fresh context | Explains why a step passed or failed; separates "what happened" from "why" |

### 5.2 Convenience Erosion Governance

Under deadline pressure, the most common failure is running the
regression eval in the same context as the executor — collapsing the
Grader role. The pipeline design must make separation the path of
least resistance [generator-assessor-separation-in-skill-iteration]:

- The Grader context must be launched with a separate invocation
  and must receive the eval suite and `refresh-candidate/` as inputs;
  it must not receive the proposal text or the authoring session.
- If the platform does not support separate invocations (e.g., no
  subagent spawn), record this limitation in the run's audit log
  and flag it as a governance gap for human review.

---

## 6. ETH Zurich Token-Overhead Constraint Check
[context-file-instruction-bloat-eth-zurich][reasoning-token-overhead-from-context-files]

ETH Zurich (438 tasks, 4 agents) found that context files increase
reasoning token usage by 14–22% and reduce success rates by ~3%,
even when written by humans [context-file-instruction-bloat-eth-zurich].

Any net token addition to a file in the package must be justified.

### 6.1 Token-Overhead Gate

This check runs as part of Step 2 (deterministic validation gate).

**Rule:** Any net addition that increases a file's token count by
more than 10% compared to the baseline must include a corresponding
removal from the same file or from a related file in the same
proposal. A proposal may not continuously grow the package without
pruning.

**Concrete check:**
1. Estimate the token count of each modified file in `refresh-candidate/`
   vs. the live package (character count ÷ 4 is an acceptable proxy).
2. For each file where the new version is more than 10% larger
   (in estimated tokens) than the baseline, check whether the proposal
   includes a removal of at least equivalent size.
3. If no corresponding removal: the proposal is flagged in the Step 2
   validation report. It does not automatically fail (it is a warning,
   not an error), but the Step 5 diff review will surface it to the
   human explicitly.

**Justification pathway:** The proposal author may annotate the proposal
with `token_overhead_justified: true` and a reason. The annotation
is recorded in the audit log but does not bypass human review at
Step 5 — the human sees the flag and the justification.

### 6.2 File-Level Budget Caps

| File | Hard cap | Source |
|------|----------|--------|
| SKILL.md | 500 lines | [skill-as-directory-progressive-disclosure-three-levels] |
| Description field | 1,024 chars | [skill-description-structure-what-when-capabilities] |
| Reference docs | Per-doc target range (in each doc's header) | per-document |
| Adapter docs | No hard cap; soft target 200–300 lines per adapter | per-document |

---

## 7. Audit Log Schema

Every Apply run produces one audit log entry in
`refresh-runs/audit-log.yaml`. Entries are append-only; never edited
after the run closes.

```yaml
- run_id: "<uuid-or-deterministic-hash>"
  timestamp: "<ISO-8601 datetime>"
  mode: apply
  manifest_ref: "change-manifest-YYYYMMDD-HHMM.yaml"
  proposals_applied:
    - "<proposal-id-1>"
    - "<proposal-id-2>"
  step_results:
    step_1_sandbox: pass    # pass | fail
    step_2_deterministic: pass
    step_3_regression:
      verdict: pass          # pass | fail
      pass_rate: 0.97
      baseline_pass_rate: 0.95
      delta: +0.02
    step_4_description:
      verdict: pass          # pass | skip | partial_rollback
      descriptions_checked: 1
      descriptions_reverted: 0
    step_5_diff_review:
      verdict: approved      # approved | rejected
      approver: "<identity or 'full-autonomy-tier'>"
      rejection_reason: null
  outcome: committed         # committed | rolled_back | deferred
  rollback_target: "refresh-runs/rollback-targets/20260623-1430/"
  notes: ""
```

**Audit log integrity:** Entries in `audit-log.yaml` must never be
edited or deleted after the run closes. New entries are appended
only. If a log entry contains an error, annotate it with a
`correction_note` field; do not overwrite the original values.

---

*Citations: [sandbox-first-modification-validation] for the 5-step pipeline design;
[bmad-deterministic-skill-validator] for the 19-rule deterministic validator pattern;
[capability-vs-regression-eval-lifecycle] for regression eval architecture;
[skill-description-optimization-loop-held-out-test] for held-out description validation;
[generator-assessor-separation-in-skill-iteration] for five-role separation architecture;
[context-file-instruction-bloat-eth-zurich] and [reasoning-token-overhead-from-context-files]
for the ETH Zurich token-overhead constraint;
[agent-action-reversibility-as-design-requirement] for the rollback procedure design requirement.*
