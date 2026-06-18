---
title: "Agent-Generated Codebase Walkthrough for Onboarding"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "agent-generated-codebase-walkthrough-for-onboarding"
extraction_date: "2026-05-25"
last_change_session: 94
last_change_sl: "session-94-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Developers or teams onboarding to a codebase they did not write, needing a readable explanation without a full manual read"
    - "Engineers recovering understanding of their own code written months ago or built rapidly without documentation"
    - "Agent sessions that need to quickly build a mental model of an unfamiliar project at session start"
    - "Any project where code has evolved faster than its documentation and the gap needs to be closed systematically"
    - "Teams that want periodic drift detection: if a regenerated walkthrough differs materially from the last, code has evolved in ways that deserve attention"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — produces a Markdown document; no source code or system state is modified"
  auditability: "Medium — embedded snippets are directly checkable against source files; correctness of architecture commentary requires human review"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "The agent has read access to all source files in the target directory. Shell execution (sed, grep, cat) is available for programmatic snippet extraction. An output path is provided and writable."
  invariants: "All code snippets are programmatically extracted from actual source files, never paraphrased. Every file matching the filter is covered or explicitly noted as out-of-scope. Architecture summary is written after all per-file sections."
  governance: "Owner: team or agent responsible for onboarding documentation. Re-generation cadence and scope are decided per project. Walkthrough accuracy is auditable by spot-checking embedded snippets against source."
  recovery: "Extraction fails for a file: log, skip, mark extraction-failed in manifest — do not hallucinate. Context window exhausted: emit partial walkthrough with warning listing uncovered files. Section mischaracterizes a module: re-run extraction for that file only and replace the section."
tags:
  - "extracted-artifact"
  - "skill"
---

# Agent-Generated Codebase Walkthrough for Onboarding

**Source:** [[agent-generated-codebase-walkthrough-for-onboarding]]
**Form:** skill
**Extraction date:** 2026-05-25

A skill where a coding agent reads an entire codebase and produces a structured Markdown document — the "linear walkthrough" — that explains the system file by file. Originated in Simon Willison's Agentic Engineering Patterns guide, demonstrated on a SwiftUI slide app using Claude Code + Opus 4.6 + Showboat harness.

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `target_directory` | string | Yes | Root path of the codebase to walk through. |
| `output_path` | string | Yes | Where to write the walkthrough Markdown file. |
| `file_filter` | string | No | Glob or extension filter (e.g., `*.swift`, `*.py`). Defaults to all source files. |
| `extraction_method` | enum | No | `programmatic` (sed/grep/cat) or `manual`. Default: `programmatic`. |
| `scope` | string | No | `full` for a monolithic walkthrough or `module:<name>` for a targeted sub-walkthrough. Default: `full`. |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `walkthrough.md` | markdown | Structured file-by-file explanation of the codebase. Includes embedded code snippets, architecture commentary, and key interaction notes. |
| `walkthrough_manifest.json` | JSON | Optional: metadata recording which files were covered, agent model used, and generation timestamp. Used for drift detection on re-runs. |

## Steps

### Step 1: File Discovery
- Enumerate all source files in `target_directory` matching `file_filter`.
- Sort files by logical order: entry points first, then core modules, then utilities.
- Log the file list for inclusion in the manifest.

### Step 2: Context Assembly
- For each file, use `grep`, `sed`, or `cat` (programmatic mode) to extract key signatures, type definitions, and interaction points.
- Never copy snippets by hand — always programmatically extract to prevent hallucination.
- Assemble per-file context blocks.

### Step 3: Walkthrough Generation
- For each file in discovery order:
  - Write a section headed by the file name.
  - Explain the file's role in the architecture.
  - Include extracted code snippets (not paraphrases) for key definitions.
  - Note interactions with other files.
- Emit sections sequentially to `output_path`.

### Step 4: Architecture Summary
- After the file-by-file sections, add a system-level summary:
  - Data flow between key modules.
  - Entry points and their call chains.
  - Any surprising or non-obvious patterns.

### Step 5: Manifest Write (Optional)
- If `walkthrough_manifest.json` is requested: record file count, files covered, model used, timestamp.
- Manifest enables drift detection: if a re-run produces a materially different walkthrough, the delta flags code evolution deserving attention.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Agent hallucinates architecture | Snippets in the output do not match file contents | Enforce programmatic extraction (Step 2); reject walkthroughs with no embedded snippets |
| Walkthrough rot | Code changes; walkthrough is not regenerated | Set a regeneration cadence tied to major change sets; use manifest timestamps |
| Scope too large (>20 files) | Walkthrough becomes unreadably long; context window stressed | Switch to `scope: module:<name>` and produce per-module walkthroughs |
| Missing shell execution capability | No sed/grep/cat available | Fail explicitly rather than falling back to manual copy |
| Context window exhaustion | Agent cannot hold all file contents | Process files in batches; emit an incomplete-coverage warning in the manifest |

## Contract

### Preconditions
The agent has read access to all source files in the target directory. Shell execution (sed, grep, cat) is available for programmatic snippet extraction. An output path is provided and writable.

### Invariants
All code snippets embedded in the walkthrough are programmatically extracted from actual source files, never paraphrased or recalled from memory. The walkthrough covers every file matching the filter; omitted files are explicitly noted as out-of-scope, not silently dropped. Architecture summary is written after all per-file sections are complete.

### Governance
Owner: the team or agent responsible for onboarding documentation. Re-generation cadence and scope (full vs. module) are decided per project. Walkthrough accuracy is auditable by spot-checking embedded snippets against source.

### Recovery
If programmatic extraction fails for a file: log the failure, skip the file, mark it as `extraction-failed` in the manifest. Do not hallucinate. If context window is exhausted before all files are processed: emit a partial walkthrough with an explicit warning section listing uncovered files. If the walkthrough manifestly mischaracterizes a module: re-run Steps 2-3 for that file only, replacing the affected section.
