---
name: watch-upstream
description: >-
  Monitor watched libraries for upstream changes. Reads the watched-libraries
  registry, fetches latest changelogs/READMEs/releases from GitHub, diffs against
  stored snapshots, and produces a triage report with recommended actions (update entry,
  extract new findings, ignore). Use periodically or on-demand to keep the upstream
  dependency registry current.
user-invocable: true
allowed-tools: Read Grep Glob Edit Write WebFetch Agent
argument-hint: "[<library-name>...] [--all] [--dry-run]"
---

# Watch Upstream

Monitor watched libraries for upstream changes and produce triage reports.

## When to Use This Skill

- Periodically (monthly recommended) to check for upstream changes
- Before an identification/extraction run (`/identify-artifacts`, `/extract-artifacts`), to ensure watched-library data is current
- When the user mentions a library update or new release
- After adding a new watched-library entry

## What This Skill Does NOT Do

- **Does not create findings.** Findings extraction is `/research-loop`'s job. This skill flags when extraction may be warranted.
- **Does not modify spectrum positions.** Spectrum changes require a design decision.
- **Does not clone repos.** Structural analysis is `/repo-analyzer`'s job.

## Procedure

### Step 0: Determine Scope

Parse arguments to build the library list:

- **Explicit names:** `watch-upstream gsd bmad-method` — check these specific libraries.
- **`--all`:** Check all active libraries in the registry. This is the default if no args are given.
- **`--dry-run`:** Fetch and compare but don't update watched-library entries.

### Step 1: Load Registry State

1. Use `Glob` to list all `.md` files in `systems/improvement-loop/watched-libraries/` (excluding `_index.md`).
2. For each library in scope, use `Read` to load the full entry. Extract:
   - `name`
   - `repo_url`
   - `last_evaluated_version`
   - `last_evaluated_date`
   - `spectrum_position`
   - `what_we_use`
   - `status`
   - Change Log table (last row = most recent snapshot)
3. Build a lookup: `{ filename -> { name, repo_url, last_version, last_date, spectrum, what_we_use, status } }`

### Step 2: Fetch Upstream State

For each library, fetch current state from GitHub. Use parallel subagents (batches of 3-4) for throughput.

**Subagent prompt template:**

```
You are checking a GitHub repository for recent changes relevant to an AI agent system.

## Library
- Name: [name]
- Repo URL: [repo_url]
- Last evaluated version: [last_evaluated_version]
- Last evaluated date: [last_evaluated_date]
- What we use: [what_we_use]

## Instructions

1. Use WebFetch to fetch the GitHub releases page: [repo_url]/releases (or /releases/latest)
   - If no releases page, try: [repo_url]/blob/main/CHANGELOG.md
   - If no changelog, try: [repo_url]/blob/main/README.md
2. Identify the **current latest version** (tag, version number, or commit date).
3. Compare against the last evaluated version.
4. If there are changes since last evaluation, summarize:
   - Version delta (e.g., v1.33.0 -> v1.35.0)
   - Key changes (new features, breaking changes, deprecations)
   - Relevance to what we use from this library
5. If the repo is no longer maintained or archived, flag that.

## Output Format (strict JSON)
{"name": "[name]",
 "current_version": "vX.Y.Z or description",
 "version_delta": "v1.33.0 -> v1.35.0" or "no change",
 "changes_summary": "brief summary of changes since last eval",
 "relevance": "high|medium|low|none",
 "relevance_reason": "why these changes matter (or don't) for what we use",
 "repo_status": "active|archived|unmaintained|unknown",
 "recommended_action": "update-entry|extract-findings|update-and-extract|ignore|investigate"}
```

**Recommended action definitions:**

| Action | When |
|--------|------|
| `ignore` | No meaningful changes since last evaluation |
| `update-entry` | Version bumped but changes don't affect what we use. Update version/date in entry. |
| `extract-findings` | Changes include new patterns worth KB extraction. Queue for `/research-loop`. |
| `update-and-extract` | Both: update the entry metadata AND extract new findings. |
| `investigate` | Can't determine change impact from changelog alone. Manual review needed. |

### Step 3: Produce Triage Report

Save to `systems/improvement-loop/operations/research-reports/{date}-watch-upstream-triage.md`:

```markdown
# Watch Upstream Triage Report -- [Date]

## Summary
| Library | Spectrum | Last Version | Current Version | Delta | Action |
|---------|----------|--------------|-----------------|-------|--------|

## Changes Detail

### [Library Name] -- [action]
- **Version delta:** [old] -> [new]
- **Changes:** [summary]
- **Relevance:** [high/medium/low/none] -- [reason]
- **Recommended action:** [action]

[repeat for each library]

## Action Queue
### Update Entry (version bump only)
[list]

### Extract Findings (queue for /research-loop)
[list with specific URLs or changelog sections to process]

### Investigate (manual review needed)
[list with reason]

### No Action
[list]
```

**Stop here if `--dry-run` was specified.**

### Step 4: Update Watched-Library Entries

For each library with action `update-entry` or `update-and-extract`:

1. Use `Edit` to update frontmatter:
   - `last_evaluated_version` -> current version
   - `last_evaluated_date` -> today
2. Use `Edit` to append a new row to the Change Log table:
   - Date: today
   - Version: current version
   - Notes: brief summary of changes

### Step 5: Update Index

Use `Edit` to update the `_index.md` catalog table with new version numbers and dates for any libraries that were updated.

### Step 6: Summary

Report to the user:
- Libraries checked
- Libraries with changes
- Actions taken (entries updated, findings queued)
- Items needing manual attention

## Calibration Notes

- **GitHub rate limits apply.** If fetching fails, note it as `investigate` rather than retrying aggressively.
- **Version formats vary.** Some repos use semver (v1.33.0), some use dates (v2026.4.5), some use descriptive versions (v6 stable). Compare semantically, not lexically.
- **"No releases" is not "no changes."** Some repos use main-branch commits without tagged releases. Check the README or recent commit activity if the releases page is empty.
- **Relevance is scoped to what_we_use.** A major release that only affects features we don't use is `low` relevance. A minor patch to a feature we depend on is `high`.
- **Don't over-extract.** Minor version bumps with bugfix-only changelogs are `update-entry`, not `extract-findings`. Reserve extraction for feature additions, architectural changes, or new patterns.
- **Spectrum position informs urgency.** `wholesale` libraries (GSD) need immediate attention on any change. `cherry-pick` libraries need attention only when changes touch what we use. `evaluating` libraries need attention on major architecture shifts.
