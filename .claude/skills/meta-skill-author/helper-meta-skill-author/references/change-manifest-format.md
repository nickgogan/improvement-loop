# Change Manifest Format

> Reference doc for the `helper-meta-skill-author` internal helper.
> Path basis: bare package paths (`SKILL.md`, `references/`, `adapters/`,
> `SOURCES.md`) are relative to the **target `meta-skill-author` package root**
> — i.e. `../` from this helper. Manifests record target-relative paths so they
> stay portable; the helper resolves them one level up.
> Defines the schema for the change manifest produced by Detect mode
> and consumed by Propose mode. Portable across all five platforms
> (Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Perplexity).
> No platform-specific features referenced.
> Every substantive claim cites a finding from the master inventory.

---

## 1. Overview

A **change manifest** is a structured, versioned record of differences
detected between the current state of the research corpus or platform
documentation and the last known-good snapshot of the skill package.

Detect mode produces one manifest per refresh run. Propose mode
reads that manifest and generates a proposal for each `changes[]`
entry. Apply mode consumes the proposals but references the manifest
for rollback traceability.

### Why structured?

Three properties motivate machine-readable format over prose:

1. **Machine-readable** — Propose mode can iterate over `changes[]`
   entries programmatically and produce a proposal for each without
   re-parsing unstructured text.

2. **Diffable** — Manifests stored in `refresh-runs/` are themselves
   version-controlled files. Running a diff against two consecutive
   manifests shows exactly what the Detect run found vs. what the prior
   run found, enabling regression detection on the detection pass itself.

3. **Audit trail** — Every change that was detected, whether addressed
   or deferred, is on record. This satisfies the versioned audit log
   requirement that governs any meta-level modification to the skill
   package [sandbox-first-modification-validation]. Retention and
   rollback depend on the audit record being complete and immutable
   after the run closes [agent-action-reversibility-as-design-requirement].

---

## 2. Manifest Schema

Manifests are stored as YAML files. The full top-level schema:

```yaml
# change-manifest-YYYYMMDD-HHMM.yaml
---
manifest_version: "1.0"
run_id: "<uuid-or-deterministic-hash>"
snapshot_timestamp: "<ISO-8601 datetime with timezone>"
baseline_snapshot_ref: "<path-or-hash of the snapshot.yaml this run compared against>"
sources_checked:
  - source_type: corpus
    source_ref: "<relative path to research corpus directory>"
  - source_type: platform_doc
    source_ref: "<URL or path>"
  # ... one entry per source in the watchlist
run_mode: detect           # always "detect" for manifests (produced by Detect mode only)
changes: []                # array of change entries; schema defined below
summary:
  total_changes: 0
  by_type:
    added: 0
    removed: 0
    modified: 0
  by_artifact:
    inventory: 0
    "SKILL.md": 0
    "references/*": 0
    "adapters/*": 0
```

### 2.1 Top-Level Fields

| Field | Type | Description |
|-------|------|-------------|
| `manifest_version` | string | Schema version; increment on breaking schema changes |
| `run_id` | string | Unique identifier for this refresh run; used by the audit log |
| `snapshot_timestamp` | ISO-8601 string | When this Detect run started |
| `baseline_snapshot_ref` | string | Path or hash of the `snapshot.yaml` this run compared against |
| `sources_checked` | array | One entry per source from the watchlist that was checked this run |
| `run_mode` | string | Fixed value `"detect"` for manifests; prevents misuse of manifest files as output of other modes |
| `changes` | array | Zero or more change entries (schema: §2.2) |
| `summary` | object | Aggregate counts for quick scanning |

### 2.2 `changes[]` Entry Schema

Each entry in the `changes` array represents one discrete change
detected across the comparison:

```yaml
- id: "<slug — human-readable, unique within this manifest>"
  source_type: corpus          # one of: corpus | platform_doc | package_internal
  source_ref: "<filename, URL, or path of the changed source>"
  change_type: added           # one of: added | removed | modified
  affected_artifact:           # one of the paths below
    # inventory
    # SKILL.md
    # references/<filename>
    # adapters/<filename>
  brief_description: >
    One or two sentences describing what changed and why it may require
    a package update. Sufficient for a human to triage without reading
    the full diff.
  raw_diff: |                  # optional; present for "modified" entries only
    --- a/path
    +++ b/path
    @@ ... @@
    ...
  content_hash_before: "<sha256 or equivalent>"  # for modified entries
  content_hash_after:  "<sha256 or equivalent>"  # for modified/added entries
  addressed_by_proposal_id: null  # null until Propose mode links a proposal here
```

### 2.3 `source_type` Values

| Value | Meaning | Diff strategy |
|-------|---------|---------------|
| `corpus` | A finding file in the research corpus directory | File-hash + content-hash (§4.1) |
| `platform_doc` | An external platform documentation page or URL | Section content hash, URL anchor where stable (§4.2) |
| `package_internal` | A file inside the skill package itself (SKILL.md, references/, adapters/) | Line-level diff against last commit or snapshot (§4.3) |

### 2.4 `affected_artifact` Values

The exact strings to use for each artifact type:

| Artifact | String value |
|----------|-------------|
| Master inventory or finding files | `inventory` |
| Main skill file | `SKILL.md` |
| Any reference document | `references/<filename>` (e.g. `references/platform-matrix.md`) |
| Any adapter document | `adapters/<filename>` (e.g. `adapters/cursor.md`) |

---

## 3. Example Manifest Entries

### 3.1 New Finding (added)

A new research finding appeared in the corpus that introduces a concept
not yet reflected in the skill package:

```yaml
- id: "new-finding-skill-cascade-eval-2026-0623"
  source_type: corpus
  source_ref: "research-findings/skill-cascade-eval-pattern.md"
  change_type: added
  affected_artifact: inventory
  brief_description: >
    New finding documents a cascading eval pattern where a parent skill's
    regression suite also runs all child skill evals. Not yet referenced
    anywhere in the package; may warrant a Propose entry for SKILL.md §2
    or audit-rubric.md.
  raw_diff: null
  content_hash_before: null
  content_hash_after: "sha256:a3f9..."
  addressed_by_proposal_id: null
```

### 3.2 Removed Finding (removed)

A finding that was previously cited in the package has been deleted from
the corpus (e.g. superseded by a renamed finding):

```yaml
- id: "removed-finding-old-eval-lifecycle-2026-0623"
  source_type: corpus
  source_ref: "research-findings/eval-lifecycle-v1.md"
  change_type: removed
  affected_artifact: inventory
  brief_description: >
    Finding eval-lifecycle-v1 was deleted from the corpus; it was cited
    in SKILL.md §2.3 and references/audit-rubric.md §7.1. Citations now
    resolve to a missing file. A proposal is needed to reroute them to
    the replacement finding capability-vs-regression-eval-lifecycle.
  raw_diff: null
  content_hash_before: "sha256:c1a2..."
  content_hash_after: null
  addressed_by_proposal_id: null
```

### 3.3 Modified Finding (modified)

An existing finding was updated, potentially changing a claim that is
cited in the package:

```yaml
- id: "modified-finding-sandbox-validation-2026-0623"
  source_type: corpus
  source_ref: "research-findings/sandbox-first-modification-validation.md"
  change_type: modified
  affected_artifact: references/refresh-validation-pipeline.md
  brief_description: >
    The sandbox-first-modification-validation finding updated the empirical
    commit rate range from 78-92% to 81-94%, and added a sixth step to
    the pipeline (post-commit smoke test). The pipeline spec in
    references/refresh-validation-pipeline.md cites the old five-step
    version; Step 5 description needs updating.
  raw_diff: |
    --- a/research-findings/sandbox-first-modification-validation.md
    +++ b/research-findings/sandbox-first-modification-validation.md
    @@ -12,7 +12,8 @@
    -  78–92% of proposed modifications maintain or improve performance
    +  81–94% of proposed modifications maintain or improve performance
    +  A sixth step (post-commit smoke test) was added to the pipeline.
  content_hash_before: "sha256:d4e5..."
  content_hash_after: "sha256:f6a7..."
  addressed_by_proposal_id: null
```

### 3.4 Platform Documentation Update (modified)

A platform documentation page changed in a way that may invalidate a
claim in one of the adapter files:

```yaml
- id: "platform-doc-cursor-rules-2026-0623"
  source_type: platform_doc
  source_ref: "https://docs.cursor.com/context/rules"
  change_type: modified
  affected_artifact: adapters/cursor.md
  brief_description: >
    Cursor docs updated the rules directory path from .cursorrules
    (root-level file) to .cursor/rules/ (directory format). The cursor.md
    adapter currently documents the old single-file pattern as the primary
    path. A proposal is needed to update §2.1 of adapters/cursor.md.
  raw_diff: |
    --- a/docs.cursor.com/context/rules [snapshot 2026-05-01]
    +++ b/docs.cursor.com/context/rules [snapshot 2026-06-23]
    @@ section "Context File Location" @@
    -  .cursorrules (project root)
    +  .cursor/rules/ directory (preferred); .cursorrules still supported
  content_hash_before: "sha256:b3c4..."
  content_hash_after: "sha256:e8d9..."
  addressed_by_proposal_id: null
```

---

## 4. Diff Computation Rules

### 4.1 Corpus Sources (research finding files)

For each file in the corpus directory:

1. Compute the **filename hash**: `sha256(<relative-path>)`. A change
   in filename hash means a file was added or removed.
2. Compute the **content hash**: `sha256(<file-content>)`. A change
   in content hash without a filename change is a `modified` entry.
3. Compare against the corresponding entry in `snapshot.yaml`
   (see §5.2 of `source-watchlist.md`).
4. If both hashes match: no entry. If content hash differs: one
   `modified` entry. If file appears new: one `added` entry. If
   file disappeared: one `removed` entry.

Edge case: file moves (rename with identical content) produce a
`removed` + `added` pair referencing the old and new paths respectively.
Do not attempt to merge these into a `renamed` type; the pair is sufficient
for Propose mode to decide whether the rename needs package updates.

### 4.2 Platform Documentation Sources

Platform docs change at the section level, not the file level. The diff
strategy operates on section content rather than full-page hashes:

1. For each watched URL in the watchlist, fetch the current content.
2. Identify stable anchors (URL fragment identifiers, e.g.
   `https://docs.cursor.com/context/rules#file-based-rules`). Where
   stable anchors exist, hash each anchored section independently.
3. Compare section hashes against `snapshot.yaml` entries for that URL.
4. A section hash change produces one `modified` entry with the URL
   and the anchor fragment as `source_ref`.

When a platform doc page has no stable anchors (JavaScript-rendered
content, no `id=` attributes), fall back to full-page content hash.
Record `anchor: none` in the snapshot entry to indicate this.

### 4.3 Package-Internal Sources

For files inside the skill package (SKILL.md, references/, adapters/):

1. Run a line-level diff against the last committed version or against
   the content recorded in `snapshot.yaml` (whichever is more recent).
2. Any non-whitespace line change produces a `modified` entry.
3. The `raw_diff` field carries the unified diff output (maximum 100
   lines; truncate with a note if longer).

Package-internal diffs are typically produced by comparing the live
package against the `refresh-candidate/` sandbox to detect
post-Apply divergence, or by comparing against the previous snapshot
to detect unintended out-of-band changes.

---

## 5. Conventions

### 5.1 File Naming

Manifest files follow this naming convention:

```
change-manifest-YYYYMMDD-HHMM.yaml
```

Example: `change-manifest-20260623-1430.yaml`

- Use UTC time for the `HHMM` component.
- Use `.yaml` extension (not `.yml`) for consistency with the snapshot
  file format.
- The filename is also used as a component in the `run_id` if no UUID
  generator is available: `run-20260623-1430`.

### 5.2 Storage Location

All manifests live in the `refresh-runs/` subdirectory, which sits as
a sibling of the parent skill package directory:

```
meta-skill-author/                       ← live skill package
  helper-meta-skill-author/              ← this internal helper
refresh-runs/                            ← manifests and snapshots
  snapshot.yaml                          ← current baseline hashes
  change-manifest-20260623-1430.yaml
  change-manifest-20260510-0900.yaml
  ...
```

`refresh-runs/` is committed to version control alongside the skill
package. This ensures the audit trail survives repository clones and
is visible in PR diffs.

### 5.3 Retention Policy

Keep a minimum of **12 consecutive manifests** at all times
[agent-action-reversibility-as-design-requirement]. This provides
roughly one year of monthly manifests, or three months of weekly ones.

When the 13th manifest would be added and the total would exceed 12,
delete the oldest. Exception: never delete a manifest that corresponds
to a named rollback target (see `refresh-validation-pipeline.md §3`).
Named rollback targets must be retained until explicitly cleared by a
human approval action.

---

## 6. Manifest → Proposal Linkage

When Propose mode generates a proposal that addresses a manifest entry,
it writes the proposal's ID back into the manifest entry's
`addressed_by_proposal_id` field. This creates a bidirectional
traceability chain:

- From the manifest: `addressed_by_proposal_id: "prop-20260623-1430-001"`
- From the proposal file: `manifest_entry_id: "new-finding-skill-cascade-eval-2026-0623"`

### 6.1 Lifecycle States

A manifest entry passes through these states:

| State | `addressed_by_proposal_id` value | Meaning |
|-------|----------------------------------|---------|
| `open` | `null` | Detected, not yet proposed |
| `proposed` | `"prop-<id>"` | Proposal exists; pending Apply |
| `applied` | `"prop-<id>"` | Proposal was applied and committed |
| `deferred` | `"deferred:<reason>"` | Human chose not to address this cycle |
| `superseded` | `"superseded-by:<newer-entry-id>"` | A later manifest entry covers this change |

The refresher writes the state into the manifest entry as a
`status` sub-field when it changes. Detect mode writes `open` on
creation; Propose mode writes `proposed`; Apply mode writes `applied`
on successful commit; human approval can write `deferred`.

### 6.2 Referential Integrity

Proposals reference manifest entries; manifest entries reference
proposals. The Apply mode validation step checks that no proposal
references a manifest entry that has been marked `superseded` or
`deferred`. If such a reference is found, Apply halts and requests
human review before continuing [sandbox-first-modification-validation].

---

*Citations: [bmad-deterministic-skill-validator] for deterministic structured output
(19-rule, 6-category validator pattern); [agent-action-reversibility-as-design-requirement]
for retention and rollback requirements; [sandbox-first-modification-validation]
for audit log completeness requirements.*
