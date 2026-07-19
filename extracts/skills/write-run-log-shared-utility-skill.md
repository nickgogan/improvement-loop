---
title: "Write-Run-Log Shared Utility Skill"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "ecosystem-monitoring-meta-loop"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "autonomous-scheduled-agent-operation.harvest-queue"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue.md::ecosystem-monitoring-meta-loop::skill::write-run-log-shared-utility-skill"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams operating a growing portfolio of scheduled or recurring automation loops that have no single place to see which loops are running, failing, or wasting resources"
    - "practitioners who want every automated job to emit a standardized run record so portfolio health can be read from one folder instead of inspecting each job separately"
    - "builders trying to make silently-failing or low-value recurring jobs visible enough to fix or retire before they quietly burn resources"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — appends a log row to a shared folder; no destructive action, and a bad entry is corrected by editing or deleting that one row"
  auditability: "high — every loop run produces a discrete, timestamped row in one folder; coverage and health are verifiable by reading the folder and cross-referencing against the discovered loop inventory"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented (Marchese, 2026-07) as the maintenance answer to automation-loop sprawl, framed as net resource-saving because it surfaces loops worth killing. Single-source; no production adoption recorded yet."
contract:
  preconditions: "A single shared run-log location exists and is writable. Loops follow a discoverable naming convention and each calls the utility once at run end. A standard log schema (loop name, timestamp, status, summary, key metrics) is defined and owned by the utility itself, not by individual callers."
  invariants: "The log is append-only — one row per run, never overwriting prior rows. All loops write through this single utility (no bespoke per-loop loggers), so the schema has exactly one owner and updating the utility updates logging everywhere. The loop inventory used for coverage checks is derived by scanning the naming convention, never maintained as a hand-edited registry."
  governance: "The utility and its log schema are owned by whoever stewards the automation portfolio; schema changes are made in the one utility and propagate to every caller. Adding or retiring a loop requires no registry edit — discovery is convention-based. Read-time health assessment (which loops to keep or kill) stays a human/steward decision; this skill only records, it never acts on the log."
  recovery: "If a loop stops emitting rows, the convention-based coverage scan flags it as dormant or unhealthy for investigation. If the shared log location is lost, it is rebuilt going forward — the log is an append-only record, not a source of truth. If schema drift appears across rows, reconcile callers back to the single utility-owned schema."
tags:
  - "extracted-artifact"
  - "skill"
---

# Write-Run-Log Shared Utility Skill

**Source:** [[ecosystem-monitoring-meta-loop]]
**Form:** skill
**Extraction date:** 2026-07-19

A single shared utility skill that every automation loop calls at the end of its run to write a standardized result row into one common log folder. Its job is observability by subtraction: once every loop reports to one place, the loops that are silently failing or producing nothing become visible enough to fix or turn off. Because all loops log through this one skill, updating the skill updates logging across the entire portfolio — the shared-utility update multiplier applied to run health.

## Inputs

- **Caller identity** — the invoking loop's name, following a discoverable naming convention (e.g. a `*-loop` suffix) so the loop inventory can be recovered by a scan rather than a registry.
- **Run outcome** — the result of the just-completed run: a status (`success` / `failure` / `no-op`), a run timestamp, a short result summary, and any available key metrics (items processed, cost/tokens, error count).
- **Shared log location** — the single well-known folder (or file) where all loops' rows accumulate. Configured once, identical for every caller.

## Outputs

- **One appended log row** in the shared run-log folder, keyed by caller name + timestamp, conforming to the utility-owned schema.
- Nothing else. The skill is a pure write utility — it records the run and returns; it does not read, aggregate, alert, or decide.

## Steps

1. Receive the run-outcome payload from the calling loop at run end.
2. Normalize the payload into the standard log schema (loop name, timestamp, status, summary, metrics). Missing optional fields are recorded as empty, never fabricated.
3. Append the row to the single shared run-log location. Never overwrite or mutate prior rows — the log is append-only.
4. Surface any write failure loudly (stderr or a secondary channel) rather than swallowing it, then return control to the caller. Health assessment — cross-referencing rows to see what is and isn't running well — is a separate read-time activity performed by a human, a steward, or a monitoring meta-loop, not by this skill.

## Failure Modes

- **Silent log-write failure.** If the write fails and the failure is swallowed, the skill re-creates the exact blind spot it exists to close. Write failures must themselves be surfaced; the calling loop's primary work should not depend on the log write succeeding.
- **Coverage gaps.** Loops that never call the utility are invisible in the log. Pair the skill with convention-based discovery: an auditor globs the naming convention to get the full inventory, then flags any discovered loop with no recent row as dormant or broken. Non-loop skills that happen to match the convention are false positives to prune.
- **Schema drift across callers.** If callers log ad-hoc shapes, the folder stops being queryable and health reads degrade to prose-scanning. Enforce a single schema owned by the utility so that changing the schema in one place changes it everywhere.
- **Unmonitored monitor.** The read-time health check that consumes this log is itself a loop and can fail silently; whatever consumes the log should appear in the log too.

## Contract

### Preconditions
A single shared run-log location exists and is writable. Loops follow a discoverable naming convention and each calls the utility once at run end. A standard log schema (loop name, timestamp, status, summary, key metrics) is defined and owned by the utility itself, not by individual callers.

### Invariants
The log is append-only — one row per run, never overwriting prior rows. All loops write through this single utility (no bespoke per-loop loggers), so the schema has exactly one owner and updating the utility updates logging everywhere. The loop inventory used for coverage checks is derived by scanning the naming convention, never maintained as a hand-edited registry.

### Governance
The utility and its log schema are owned by whoever stewards the automation portfolio; schema changes are made in the one utility and propagate to every caller. Adding or retiring a loop requires no registry edit — discovery is convention-based. Read-time health assessment (which loops to keep or kill) stays a human/steward decision; this skill only records, it never acts on the log.

### Recovery
If a loop stops emitting rows, the convention-based coverage scan flags it as dormant or unhealthy for investigation. If the shared log location is lost, it is rebuilt going forward — the log is an append-only record, not a source of truth. If schema drift appears across rows, reconcile callers back to the single utility-owned schema.
