---
name: cleanup-cache
description: >-
  Monitor and clean up temporary/cache directories across IL workflows.
  Reports sizes of all gitignored temp paths, flags stale entries, and
  optionally purges with --purge. Read-only by default. Owner responsibility.
user-invocable: true
allowed-tools: Read Bash Glob
argument-hint: "[--purge] [--purge-stale <days>] [--target repo-cache|downloads|all]"
---

# Cleanup Cache

Monitor and optionally purge temporary files that accumulate across IL and workspace workflows.

## When to Use This Skill

- Periodically (monthly) to check if temp directories are growing
- Before large `/repo-analyzer` runs to reclaim disk space
- When disk usage feels high or Obsidian indexing is slow
- After a batch of `/repo-analyzer` runs to clean repos no longer in the watched-libraries registry

## When NOT to Use This Skill

- **To delete research artifacts, analysis docs, or KB entries.** Those are permanent.
- **To clean git objects.** Use `git gc` directly.

## Cognitive Disposition

You are the **Owner** performing routine maintenance. This is read-only by default — report what exists and recommend actions. Only delete when `--purge` or `--purge-stale` is explicitly passed.

## Available Tools

| Tool | Purpose |
|------|---------|
| `Bash` | `du`, `ls`, `find`, `rm` (only with --purge) |
| `Read` | Read watched-library entries to cross-reference cache contents |
| `Glob` | List files in target directories |

## Paths

Known temporary/cache directories in this workspace:

| Path | Created By | Self-Cleans? |
|------|-----------|--------------|
| `systems/improvement-loop/watched-libraries/_tmp/repo-cache/` | `/repo-analyzer` | No — reused across runs |
| `incubator/claude-build/app/pdf-to-markdown/_downloads/` | `/pdf-to-markdown` | Yes — cleans after each conversion |
| `incubator/claude-build/app/pdf-to-markdown/output/` | `/pdf-to-markdown` | No — persistent output |

The repo-cache is the primary cleanup target. The other directories are listed for completeness but rarely need intervention.

---

## Arguments

| Argument | Effect |
|----------|--------|
| *(no args)* | Report mode — scan all known temp directories, report sizes, flag stale items |
| `--target repo-cache` | Scope to repo-cache only |
| `--target downloads` | Scope to pdf-to-markdown downloads only |
| `--target all` | Scan everything (default for report mode) |
| `--purge` | Delete all contents of the targeted directory. **Requires user confirmation before executing.** |
| `--purge-stale <days>` | Delete only entries older than `<days>` days. Default threshold: 30 days. **Requires user confirmation.** |

---

## Procedure

### Step 1: Scan Temp Directories

Run `du -sh` on each known temp path. Collect:

- Total size per directory
- Entry count
- Per-entry sizes (for repo-cache, list each subdirectory)

```bash
du -sh systems/improvement-loop/watched-libraries/_tmp/repo-cache/ 2>/dev/null
du -sh systems/improvement-loop/watched-libraries/_tmp/repo-cache/*/ 2>/dev/null | sort -rh
du -sh incubator/claude-build/app/pdf-to-markdown/_downloads/ 2>/dev/null
du -sh incubator/claude-build/app/pdf-to-markdown/output/ 2>/dev/null
```

### Step 2: Cross-Reference Repo Cache Against Registry

For each directory in `repo-cache/`:

1. Read the watched-libraries registry: `Glob` for `systems/improvement-loop/watched-libraries/*.md` (excluding `_index.md` and `_tmp/`)
2. Check whether each cached repo slug matches an active watched-library entry
3. Flag **orphaned caches** — repos in cache that are no longer in the registry

Also check last-modified dates:

```bash
find systems/improvement-loop/watched-libraries/_tmp/repo-cache/ -maxdepth 1 -type d -not -name repo-cache | while read d; do
  echo "$(basename "$d") $(stat -f '%Sm' -t '%Y-%m-%d' "$d")"
done
```

### Step 3: Report

Output a table:

```
## Cache Status Report

| Directory | Size | Entries | Stale? | Orphaned? |
|-----------|------|---------|--------|-----------|
| repo-cache/ | XXX MB | N | Y/N | N orphans |
| _downloads/ | XXX KB | N | - | - |
| output/ | XXX KB | N | - | - |

### Repo Cache Detail

| Repo | Size | Last Modified | In Registry? | Recommendation |
|------|------|---------------|-------------|----------------|
| warp | 495M | 2026-05-24 | Yes | Keep / Purge |
| ... | ... | ... | ... | ... |

**Total reclaimable:** XXX MB
```

### Step 4: Purge (only with --purge or --purge-stale)

**Gate:** Before any deletion, print the exact `rm -rf` commands that will run and ask for explicit user confirmation. Do not proceed without a "yes."

If `--purge`:
- Delete all contents of the targeted directory
- Report freed space

If `--purge-stale <days>`:
- Delete only entries with last-modified date older than `<days>` days
- Report freed space and what was kept

After purging, re-run the size scan to confirm cleanup.

---

## Safety Constraints

1. **Never delete outside the known temp paths.** Only the directories listed in the Paths table are valid targets.
2. **Never delete the parent directory itself** — only its contents. The `_tmp/repo-cache/` directory should remain as an empty container.
3. **Always confirm before deleting.** Even with `--purge`, show the plan and wait for user approval.
4. **Report mode is the default.** If no `--purge` flag is passed, this skill is purely read-only.
