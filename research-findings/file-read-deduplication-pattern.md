---
name: File Read Deduplication (18% Duplicate Reads, 2.6% Fleet Savings)
summary: 18% of all file reads in Claude Code are duplicates. A dedup system returns a one-line stub if the file is unchanged since last read, saving 2.6% of fleet-wide token costs.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in:
- S3 (Claude Code Build)
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: pointers-over-copies-in-context-files.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- rules/file-read-deduplication.md
---
## What It Is

A deduplication system for file read operations in agent sessions. When an agent requests a file it has already read in the current session, the system checks whether the file has changed since the last read. If unchanged, it returns a one-line stub confirming no change instead of re-reading the full file content. Production metrics from Claude Code show 18% of all file reads are duplicates.

## Why It Matters

Nearly 1 in 5 file reads wastes tokens re-reading unchanged content. For large files (configuration, schemas, reference docs), each duplicate read can cost hundreds or thousands of tokens. At fleet scale, Claude Code's dedup system saves 2.6% of all token costs — a significant optimization that requires no changes to agent logic or prompts.

## Why People Are Using It

The pattern is implemented internally in Claude Code's infrastructure. For custom agent harnesses, the same approach applies: track what files the agent has read, and intercept duplicate reads with a minimal stub response.

## Potential Improvements

- Track file content hashes or modification timestamps per session
- Return a standardized stub format (e.g., "File unchanged since last read at turn N")
- Extend the pattern to other read-heavy operations (API responses, database queries with stable results)
- Consider a TTL-based approach for long sessions where files may change externally

## Potential Failure Modes

- **Stale cache from external modification:** If a file is modified outside the agent session (by another process, a user edit, or a git operation), the dedup system may return a stale stub. Requires monitoring file system events or checking timestamps on each read.
- **Implementation complexity:** Tracking read history adds state management overhead to the agent harness. Must handle session boundaries, tool restarts, and concurrent file access.
- **False savings on small files:** Deduplicating reads of small files (a few lines) saves minimal tokens while adding complexity. The optimization is most valuable for large reference files.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[file-read-deduplication]] in `extracts/rules/`
