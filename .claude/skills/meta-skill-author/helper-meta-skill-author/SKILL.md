---
name: helper-meta-skill-author
description: >
  Internal helper for the meta-skill-author skill — not invoked on its own.
  Detects when the parent meta-skill-author package has drifted from its
  underlying corpus and proposes validated updates. Use when new findings land
  in the improvement-loop research corpus, when platform documentation changes
  for any of the five target platforms (Claude Code, Cursor, Copilot, Codex,
  Perplexity), when scheduled refresh runs are due, or when the user says
  "refresh the meta-skill" or "check for stale claims". Three modes: Detect
  (diff corpus and platform docs against snapshot), Propose (classify each
  change as Confirms / Variant / New concept / Contradicts), Apply
  (sandbox-validated update with rollback). Never grades its own output —
  generator-assessor separation is required in Propose and Apply modes.
---

## §0 Orientation

This is an internal helper bundled inside the `meta-skill-author` skill; it is
not triggered independently. The parent `meta-skill-author` package encodes best
practices for authoring portable, cross-platform agent skills. Those practices
are grounded in a
research corpus (`findings-master-inventory.md`) and in the documentation of
five target platforms. Both sources change over time: new findings land,
platform docs update, and anti-patterns accumulate. Without an explicit refresh
mechanism the meta-skill silently drifts — its claims become stale, its
anti-pattern catalogue goes stale, and authors unknowingly follow superseded
guidance.

This skill is the answer to that drift. It operates in three strictly-separated
modes:

- **Detect** — Read sources and the current package; produce a change manifest.
  No file mutations.
- **Propose** — For each item in the manifest, classify the change and draft an
  edit. No file mutations.
- **Apply** — Execute approved proposals through a sandboxed, eval-gated
  pipeline. Mutations happen only in a shadow directory first; the live package
  is touched only after human approval.

Each mode ends with an explicit approval gate before the next begins.

**Critical invariant:** The refresher never grades its own output. The model
that drafts proposals in Propose mode must not be the model that assesses them.
Apply mode requires a separate audit pass before any file changes reach the live
package. [generator-assessor-separation-in-skill-iteration]

**Side-effect guard (always-on harnesses, e.g., GitHub Copilot):** tool
permissioning is weaker and there is no per-skill side-effect gate at runtime, so
this skill must never commit, push, deploy, or delete — and never write to the
live package outside the shadow sandbox — without the user's explicit approval.

**Path convention.** This helper lives *inside* the package it maintains. A
leading `../` always denotes the **parent `meta-skill-author` package** that this
helper audits and edits — its authored files are `../SKILL.md`, `../SOURCES.md`,
`../adapters/`, and `../references/` (e.g. `../references/platform-matrix.md`,
`../references/audit-rubric.md`, `../references/safety-gates.md`). Bare paths such
as `references/proposal-log.md` or `references/source-watchlist.md` are *this
helper's own* operational files. `findings-master-inventory.md` is the external
research corpus, outside both packages.

---

## §1 Detect Mode

**Purpose:** Compare the current meta-skill package state to its sources.
Output a structured change manifest. Do not mutate any file.

### 1.1 Snapshot current state

Before fetching anything external, record the current state of the package:

1. Compute a hash (or record last-modified timestamp) for each file in the
   parent package: `../SKILL.md`, every file under `../references/`, every file
   under `../adapters/`, `../SOURCES.md`.
2. Record the timestamp of the snapshot run.
3. Write snapshot metadata to
   `references/last-snapshot.md` (create if absent).

This snapshot is the baseline for all subsequent diffs. [bmad-deterministic-skill-validator]

### 1.2 Enumerate sources to check

Sources fall into two categories:

**Corpus sources** (local files):
- `findings-master-inventory.md` — the single source of truth for all claims
- Any extract files (`extract-B*.md`) present in the workspace

**Platform documentation sources** (remote URLs):
- Listed in `references/source-watchlist.md`
- Covers the five target platforms: Claude Code, Cursor, Copilot, Codex,
  Perplexity
- Do not fetch URLs not on the watchlist; unbounded web retrieval is an
  anti-pattern here

### 1.3 Detection procedure

For each source in the enumerated list:

1. Retrieve current content (file read for corpus; URL fetch for platform docs).
2. Diff against the last-snapshot version of that source (use stored hash or
   content from `references/last-snapshot.md`).
3. Classify each diff item:
   - **new** — content present in source but not reflected anywhere in the
     package
   - **removed** — content previously in source that has been retracted or
     deleted
   - **modified** — content changed in source (wording, numbers, URLs)
   - **unchanged** — no diff; skip

4. Cross-reference each diff item against the package:
   - Which file(s) in the package reference this source or claim?
   - Is the claim still accurate given the diff?

### 1.4 Output: change manifest

Write `references/change-manifest.md` (see format spec in
`references/change-manifest-format.md`).

Each entry in the manifest must include:
- Source identifier (finding name or platform doc URL + section)
- Diff type (new / removed / modified)
- Affected package file(s), if known
- Raw diff excerpt (≤200 chars)

**Anti-patterns in Detect:**
- Do not interpret or evaluate changes — only enumerate them.
  [bmad-deterministic-skill-validator]
- Do not fetch URLs outside the watchlist.
- Do not mutate any package file. Even `references/last-snapshot.md` is written
  only after the manifest is complete and consistent.

---

## §2 Propose Mode

**Purpose:** For each item in the change manifest, classify the change and
draft a concrete edit proposal. No file mutations.

### 2.1 Four-change classification

Every manifest item receives exactly one of these four classifications:

| Class | Meaning | Required action |
|-------|---------|-----------------|
| **Confirms** | Change reinforces an existing claim | No rewrite; bump confidence label; record in proposal log |
| **Variant** | Change suggests different framing of an existing claim | Draft reframe of the target section; cite both old and new finding |
| **New concept** | Change introduces a concept not yet in the package | Draft addition to an existing section or propose a new reference doc |
| **Contradicts** | Change conflicts with an existing claim | Escalate; require human resolution before Apply proceeds |

Source: four-discipline audit pattern in inventory §5;
[generator-assessor-separation-in-skill-iteration]

### 2.2 Per-proposal payload

Each proposal entry must contain:

```
source:        <finding-name or URL + section>
target_file:   <../SKILL.md | ../references/<file>.md | ../adapters/<file>.md>
classification: <Confirms | Variant | New concept | Contradicts>
proposed_edit: |
  <diff-format text block>
confidence:    <high | medium | low>
hitl_tier:     <Guarded | Proposal-first | Human-required>
rationale:     <one sentence>
```

**Confidence rules:**
- `high` — two or more independent sources confirm the change
- `medium` — single source; no contradicting source found
- `low` — single source; at least one partially contradicting source exists

Single-source proposals must never receive `high` confidence. This guards
against the single-source anti-pattern catalogued in §5.

### 2.3 HITL tier assignment

Every proposal receives a tier before it may proceed to Apply.
Tier assignment uses the blast-radius × reversibility matrix:
[autonomy-gradient-not-binary-delegation]

| Proposal class | Default tier |
|----------------|-------------|
| Confirms | Guarded (apply, then log) |
| Typo / wording fix (no claim change) | Guarded |
| New concept added to an existing reference doc | Proposal-first (human approves) |
| Variant (reframe of existing claim) | Proposal-first |
| New concept requiring a new file | Proposal-first |
| Contradicts | Human-required (cannot proceed without explicit resolution) |
| Any change to `../SKILL.md` body | Proposal-first minimum |
| Any change to `../references/audit-rubric.md` or `../references/safety-gates.md` | Human-required |

Persistent changes to governance docs always require Human-required tier,
regardless of classification. [advisory-only-for-persistent-mutations]

### 2.4 Generator-assessor separation (mandatory)

The model context that drafts proposals must not be the context that grades
them. After the proposal log is complete:

1. **Generator pass** — produce all proposal payloads (current context).
2. **Assessor pass** — invoke a separate model context (or a fresh session)
   that receives only:
   - The proposal log
   - The relevant section of `../references/audit-rubric.md`
   - The relevant finding text
   The assessor scores each proposal against the four-discipline rubric and
   returns a per-proposal grade with a pass/fail verdict.
3. Only proposals that pass the assessor gate are eligible for Apply.
   [generator-assessor-separation-in-skill-iteration]

Convenience erosion is the primary failure mode: under time pressure, authors
skip the assessor pass and self-grade inline. The design must make separation
the path of least resistance — the proposal log file is not considered complete
until an assessor grade is attached to each row.

### 2.5 Output: proposal log

Write `references/proposal-log.md` — a Markdown table with one row per
proposal, sorted by HITL tier (Human-required first), then by confidence
(low first).

Columns: `source | target_file | class | confidence | hitl_tier | edit_summary | assessor_grade`

---

## §3 Apply Mode

**Purpose:** Execute approved proposals through the five-step validation
pipeline. Mutations happen first in a shadow directory; the live package is
updated only after all gates pass and the human explicitly approves.

### 3.1 Inputs

- The proposal log (`references/proposal-log.md`), with assessor grades
  attached
- Human sign-off on all Proposal-first and Human-required items (explicit
  written approval required; advisory-only for these tiers is not sufficient)
- The current package state (hashed snapshot from Detect)

Guarded-tier items may proceed without explicit per-item approval, but must
appear in the diff for review before final commit.

### 3.2 Five-step pipeline

**Step 1 — Sandbox isolation** [sandbox-first-modification-validation]

Write all proposed edits to `refresh-candidate/` — a shadow copy of the
package directory. Do not touch the live package at any point during Steps 1–3.

Order of operations within the sandbox:
1. Update `findings-master-inventory.md` first (single source of truth).
2. Derive all downstream file changes from the updated inventory.
3. Update `../references/platform-matrix.md` if platform docs changed.
4. Regenerate or update `../adapters/` docs only after `../references/platform-matrix.md` is stable.

This mirrors the canonical-source + thin-adapter pattern:
[multi-ide-portability-via-installer-templates]

**Step 2 — Regression eval gate** [capability-vs-regression-eval-lifecycle]

Re-run the full regression eval suite against the sandbox copy. The suite must
pass at threshold (regression evals ≥ 95% pass rate) before proceeding.

- Capability evals (new behaviors being added) may start below threshold; they
  are not blockers.
- Regression evals (previously-passing behaviors) are hard blockers; a single
  regression below threshold stops Apply and routes back to Propose for
  reclassification. [capability-vs-regression-eval-lifecycle]

**Step 3 — Held-out re-validation** [skill-description-optimization-loop-held-out-test]

For any proposal that changes the `description` field of `../SKILL.md`:
- Re-run the description optimization loop on the sandbox copy.
- 20 eval queries, 60/40 train/test split, 3 runs per query, ≤ 5 iterations,
  select by TEST score.
- New description must match or exceed current TEST score to proceed.

For body-only changes that do not affect the description, this step is skipped.

**Step 4 — Diff for human review**

Produce a PR-style diff of all changes between the sandbox copy and the live
package. Present this diff to the user.

- Proposal-first and Human-required tier items require explicit written
  approval per item before Step 5.
- Guarded tier items require acknowledgement (user may batch-acknowledge).
- The diff document is the approval artifact; it must be preserved in
  `references/apply-log.md`.

**Step 5 — Versioned commit + rollback target** [agent-action-reversibility-as-design-requirement]

After approval:
1. Archive the current live package as a named rollback target:
   `refresh-rollback-<YYYYMMDD>/`
2. Copy sandbox contents to the live package.
3. Write a timestamped entry to `references/apply-log.md`:
   - Source diffs, proposals applied, approvals received, eval results,
     rollback target path.

The rollback bundle must remain accessible until the next Apply run completes
successfully.

### 3.3 ETH Zurich size constraint [context-file-instruction-bloat-eth-zurich]

Before finalizing Step 5, verify:
- `../SKILL.md` in the sandbox does not exceed 500 lines.
- No reference doc exceeds its documented target length.

If a new concept must be added and the size limit would be breached:
- Identify content to remove (outdated claims, superseded anti-patterns).
- Or move content from `../SKILL.md` body to a new or existing `../references/` doc,
  with a pointer in `../SKILL.md`.

Do not bypass the size gate; net-additive changes without corresponding
removals are an Apply anti-pattern.

### 3.4 Anti-patterns in Apply

- Do not apply a batch of Confirms-tier changes without sampling-based review
  (spot-check at least 20% of the batch). [sandbox-first-modification-validation]
- Do not bypass the regression eval gate even for changes described as "small"
  or "obviously safe."
- Do not update `../adapters/` before updating the canonical `../references/platform-matrix.md`.
- Do not let the live `findings-master-inventory.md` and `../SKILL.md` disagree
  after Apply completes.

---

## §4 Governance & Lifecycle

### 4.1 Cadence options

The user selects one operating cadence; the refresher does not self-schedule:

| Cadence | Trigger | Who runs Apply |
|---------|---------|----------------|
| **On-demand** | User phrase: "refresh the meta-skill" / "check for stale claims" | User |
| **Scheduled** | Periodic Detect + Propose; notification to user | User (manual Apply) |
| **Reactive** | A watched source in `references/source-watchlist.md` changes | Detect runs automatically; Propose + Apply require user initiation |

### 4.2 Audit log

Every Detect / Propose / Apply run appends a timestamped entry to
`references/apply-log.md`. The entry includes:
- Run type and timestamp
- Source diffs (Detect)
- Proposal count by tier (Propose)
- Approvals received and changes applied (Apply)
- Eval results (Apply)

[sandbox-first-modification-validation]

### 4.3 Description drift maintenance [description-based-workflow-routing-lazy-dispatch]

- When the `../SKILL.md` body changes, re-evaluate whether the frontmatter
  description still accurately triggers on intended queries.
- When the description changes, re-run the description optimization loop
  (Step 3 of Apply).
- Description drift is a silent failure mode; it must be checked explicitly
  after every Apply run that modifies `../SKILL.md`.

### 4.4 Single source of truth

- `findings-master-inventory.md` is canonical; all package files derive from
  it.
- `../SOURCES.md` must be regenerated whenever the inventory changes.
- `../adapters/` docs must be regenerated whenever `../references/platform-matrix.md`
  changes.
- The inventory and `../SKILL.md` must never disagree after an Apply run.

---

## §5 Hard Constraints & Anti-Patterns

### 5.1 Hard constraints

| Constraint | Sourcing finding |
|-----------|-----------------|
| Never grade own output — generator-assessor separation is mandatory in Propose and Apply | [generator-assessor-separation-in-skill-iteration] |
| Never apply Contradicts-tier changes without explicit human resolution | [autonomy-gradient-not-binary-delegation] |
| Never bypass the regression eval gate, regardless of change size | [sandbox-first-modification-validation] |
| Never push `../SKILL.md` past 500 lines | [skill-as-directory-progressive-disclosure-three-levels] |
| Never include explicit CoT, few-shot examples, or decomposition scaffolding inside skill instructions | [reasoning-model-anti-pattern-prescribed-reasoning] |
| Never apply persistent mutations (governance docs, schemas) without Human-required tier approval | [advisory-only-for-persistent-mutations] |

### 5.2 Anti-patterns specific to refresher operations

- **Single-source confident claims** — a change supported by only one finding
  must receive `medium` or `low` confidence; never `high`.
- **Auto-applying batched Confirms changes without sampling** — even low-risk
  changes accumulate; spot-check 20% of any batch ≥ 5 items.
- **Updating adapters before the canonical source** — always update
  `../references/platform-matrix.md` first; `../adapters/` docs are derived outputs.
- **Inventory/`../SKILL.md` disagreement** — if the inventory says X and `../SKILL.md`
  says Y after Apply, the Apply run is not complete.
- **Skipping the assessor pass under deadline pressure** — this is the
  "convenience erosion" failure mode documented in
  [generator-assessor-separation-in-skill-iteration]; the proposal log is not
  considered complete without an assessor grade on each row.
- **Fetching unbounded web content** — only URLs in `references/source-watchlist.md`
  are legitimate Detect targets.

---

## §6 Outputs

### Detect mode outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Change manifest | `references/change-manifest.md` | Structured list of diffs; see `references/change-manifest-format.md` |
| Snapshot update | `references/last-snapshot.md` | Updated hashes and timestamps |
| Audit log entry | `references/apply-log.md` | Timestamped Detect run record |

### Propose mode outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Proposal log | `references/proposal-log.md` | Table of classified proposals with HITL tiers and assessor grades |
| Updated manifest | `references/change-manifest.md` | Each entry linked to its proposal row |
| Audit log entry | `references/apply-log.md` | Timestamped Propose run record |

### Apply mode outputs

| Artifact | Path | Description |
|----------|------|-------------|
| Updated package files | live package (post-approval) | All approved changes applied to canonical files |
| Diff document | `references/apply-log.md` | PR-style diff presented for human review |
| Updated inventory | `findings-master-inventory.md` | Updated first; all others derived |
| Rollback bundle | `refresh-rollback-<YYYYMMDD>/` | Full previous package state, archived |

---

## §7 Quick Reference

| Mode | Inputs | Outputs | HITL gate | Mutates live files? |
|------|--------|---------|-----------|---------------------|
| **Detect** | Corpus + platform docs + last snapshot | Change manifest | None | No |
| **Propose** | Change manifest | Proposal log (with assessor grades) | None (advisory) | No |
| **Apply** | Approved proposal log | Updated package + diff + rollback | Per-proposal tier | Yes (sandbox → live) |

**Approval gate summary:**

| Tier | Required before Apply |
|------|-----------------------|
| Guarded | Batch acknowledgement |
| Proposal-first | Explicit written approval per item |
| Human-required | Explicit written resolution of contradiction, then approval |
