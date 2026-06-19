---
title: "IL audit summary"
audit_target: "systems/improvement-loop/"
audit_date: "2026-06-12"
audit_session: "115"
---

# Whole-system summary — Improvement Loop

## At a glance

- **43 artifacts dispatched** across 3 shapes (32 skills, 4 agents, 7 CLAUDE.md) — second canonical `/audit-system` run
- **36 of 43 artifacts assessed**; 7 unassessed due to bin 2/4 partial output (format-compliance regression — see §"Design contract refinement candidates")
- **4 G9.I6 VIOLATIONS** (deployment-blocking): `promote-findings` (`--auto` bypasses HITL), `translate-governance` (act-then-report), `research-loop` (KB writes no HITL), `watch-upstream` (auto Edit after triage)
- **2 additional runtime-failure risks**: `dimension-rebalance` (Write missing from `allowed-tools` but called in Step 5B), `identify-artifacts` (Edit missing from `allowed-tools` but Step 7 needs it)
- **3 G9.I6 SATISFIED exemplars**: `finding-crosslink`, `cleanup-cache`, `compare-repos` — these are the strongest-governance skills to imitate
- **3 confirmed + 3 strongly-suspected MOC-shaped CLAUDE.md latents** (≥6 cumulative with session 114 MetaSystem MOCs) — rule-11 trigger met, classifier heuristic committed (see §"MOC-CLAUDE.md classifier decision")
- **9 bins parallel-dispatched** in ~7 min via Librarian subagents in `mode: in-context-rubric`

## Critical findings (deployment-blocking)

### 1. `promote-findings` SKILL — G9.I6 VIOLATED (HARD-BLOCKING)

> The `--auto` flag enables autonomous promotion of all non-duplicate findings into the live KB without human approval. There is no `--dry-run` mode, no confirmation step, no rollback. A buggy invocation could pollute the KB with hundreds of low-quality findings before any human sees the output.

8 Violated findings — the highest violation count in the audit. Remediation: remove `--auto` or require explicit `--confirm` per-batch.

### 2. `translate-governance` SKILL — G9.I6 VIOLATED

> Rule 1 explicitly encodes "do not wait for approval before writing" — an act-then-report design. Governance files (IL-specific values, principles, vocabulary, rules) are mutated, then a delta report is produced. This inverts the normal HITL ordering.

Translation outputs are governance-source documents — the most-load-bearing IL artifacts. Remediation: revise Rule 1 to require pre-write delta-report approval.

### 3. `research-loop` SKILL — G9.I6 VIOLATED

> Writes new findings/sources/authorities to the KB without any HITL gate inside the procedure. The Integration table references an external "Human gate: Review findings and priorities" but this gate is downstream of the writes — the skill can complete dozens of writes before a human sees anything.

Remediation: add an in-procedure dry-run mode (default) and a confirmation step before write-out batches.

### 4. `watch-upstream` SKILL — G9.I6 VIOLATED

> Step 4 executes `Edit` on watched-library entries automatically after Step 2's automated subagent triage — no HITL gate between triage output and file mutation. `--dry-run` is the only guard.

Remediation: insert an explicit Step 3.5 human-approval gate between triage report and Step 4 Edit execution.

### 5. `dimension-rebalance` — runtime-failure risk

> `allowed-tools: Read Grep Glob Edit` — but Step 5B explicitly calls `Write` to create new finding files. `Write` is absent from `allowed-tools`. The skill will fail at runtime when the Type B (split) path executes.

Remediation: add `Write` to `allowed-tools`, or document Step 5B as a Bash file-creation operation if that was the intent.

### 6. `identify-artifacts` — runtime-failure risk

> `allowed-tools: Read Grep Glob Write Agent` — but Step 7 instructs finding frontmatter `pipeline_status` updates which require `Edit` (or a riskier full-file `Write` overwrite). `Edit` is absent from `allowed-tools`.

Remediation: add `Edit` to `allowed-tools` or explicitly document Step 7 as full-file rewrite.

## G9.I6 SATISFIED exemplars (imitate these)

- **`finding-crosslink`**: `--dry-run` default + explicit Step 5 Human Gate + YAML round-trip validation = three-layer defense. Description carries the HITL commitment publicly.
- **`cleanup-cache`**: explicit confirmation gate ("Do not proceed without a 'yes'") before any `rm -rf`. Single most-prominent destructive-action guard in the audit.
- **`compare-repos`**: requires both `--write` flag AND explicit `y` approval before writing comparison report.

## Common findings (cross-artifact patterns)

### Pattern A: missing `## Boundary conditions` section (template skeleton gap)

The IL skill template (skill.md concept) requires a `## Boundary conditions` section covering termination criteria, safety-critical classification, and out-of-scope declarations. **Most safety-critical skills omit it**: `finding-crosslink`, `system-health`, `dimension-rebalance`, `watch-upstream`, `cleanup-cache`, `transcript-fetcher`, `identify-artifacts`, plus many in the persisted bins. This is the most pervasive structural gap.

Remediation: a one-shot pass over IL skills to add `## Boundary conditions` per the template skeleton. Owner-tier cleanup.

### Pattern B: `allowed-tools` precision is weak

Multiple varieties:
- **Over-grant** (tool listed, never used): `research-loop` (WebSearch), `research-proposer` (WebFetch barely used), `system-health` (Bash unscoped against read-only intent), `assess-prompt` (over-broad).
- **Under-grant** (tool used, not listed): `dimension-rebalance` (Write), `identify-artifacts` (Edit).
- **Flat list, no risk tiering**: `watch-upstream`, `transcript-fetcher`, others. G6.I1 fires repeatedly.

Remediation: standardize a per-skill `allowed-tools` audit step in `/design-skill` and a risk-tier comment convention.

### Pattern C: prose-only structural constraints

Many safety-critical skills declare write-scope boundaries in prose (Rules / Calibration Notes / "Never write to X") but enforce nothing structurally at the harness layer. The Owner audit (session 114) flagged this same gap for the MetaSystem Owner; IL skills repeat it. This is recurring evidence that prose-only enforcement is the IL norm — but it should not be the deployed norm.

Remediation: codify a positive-space governance rule "all safety-critical write boundaries must have at least one structural enforcer (harness allowlist, allowed-tools restriction, or required flag)". Per Nick's positive-space preference.

### Pattern D: no `version:` field; inter-skill contracts unversioned

`identify-artifacts` produces a report consumed by `/extract-artifacts` — the report format is an inter-skill contract. Neither carries a `version:` field. Same for `assess-skill` / `assess-agent` / `/audit-system` cross-references. Version drift would silently break paired skills.

Remediation: defer until first observed drift incident (rule 11) — but worth noting for future composition design.

### Pattern E: subagent-spawning skills lack AUTHORITY and FAILURE SIGNAL clauses (G8.I5/I6)

`identify-artifacts`, `finding-crosslink`, `watch-upstream`, `research-loop` — all spawn subagents via `Agent` but their dispatch payloads lack explicit AUTHORITY ("you are authorized to X, not Y") and FAILURE SIGNAL ("if X, emit structured-error not low-confidence-guess") clauses. After a model upgrade, subagents without formal failure signals may degrade silently.

Remediation: add AUTHORITY+FAILURE SIGNAL to subagent-spawn templates. Cross-cutting concern — could be a shared snippet in the skill design substrate.

## Whole-system invariants

(v1: empty. Per rule 11, the design contract gates invariant additions on 2-3+ concrete instances. **This second audit surfaces three candidates approaching the threshold**, listed below as design-contract refinement candidates, not yet committed.)

## MOC-CLAUDE.md classifier decision (rule-11 trigger met)

Session 114 (MetaSystem): 3 confirmed shape-mismatch MOCs (`governance/proposals/CLAUDE.md`, `app/CLAUDE.md`, `project-management/CLAUDE.md`).

Session 115 (IL): 3 confirmed shape-mismatch MOCs (`docs/CLAUDE.md`, `governance/proposals/CLAUDE.md`, `operations/references/CLAUDE.md`) + 3 strongly-suspected unaudited MOCs (`extracts/CLAUDE.md` 78 words, `extracts/patterns/CLAUDE.md` 73 words, `extracts/guides/CLAUDE.md` 55 words — all sub-100 words and located in folder-MOC positions).

**Cumulative: ≥6 MOC instances across 2 systems.** Rule-11 trigger met.

**Committing the heuristic** (`/audit-system` SKILL.md patched this session):
> At discovery time, skip dispatch for CLAUDE.md when frontmatter `type: "index"` **OR** body word count < 100. Record as `skipped: MOC` in manifest's structural-gaps section. The artifact still appears in the manifest with its classification — only the assessor dispatch is suppressed.

Trade-off: the heuristic risks suppressing the occasional legitimate short prompt-based-agent CLAUDE.md. Mitigation: `--scope claude-md` would override the suppression for a forced re-audit pass. Recovery is one-flag.

## Design contract refinement candidates from this run

These are gaps in v1 SKILL.md or the design contract surfaced by the second real audit:

1. **Audit-trail gap (finding #22 from session 114 self-audit)** — no per-run record exists. **Patched this session** (see §"Audit-trail patch" below). One-line append to `<target>/audit-reports/runs.md` on each `--write` invocation.

2. **MOC-CLAUDE.md shape-mismatch is now recurring across 2 systems** (≥6 total). **Patched this session** — discovery-time classifier added per above.

3. **Format-compliance regression in bin 2 and bin 4 spawn output.** Both bins emitted only 1 of N expected sentinel-delimited reports despite the spawn payload's explicit "Return a single message containing exactly K sentinel blocks" instruction. This is the third format-compliance issue across two audits (session 114 had heading collisions; session 115 has truncation/non-bundling). The sentinel-delimiter patch from session 114 closed the heading-collision class but does not address single-message bundling drift. **Not patched this session** (one new instance per system is not yet 2-3+ on the same failure mode). Watch in session 116+; if non-bundling recurs, refine the spawn payload to require N separate sentinel-pair blocks with an explicit "begin emission now" marker.

4. **Whole-system invariant candidate: "all safety-critical skills MUST have a `## Boundary conditions` section declaring the HITL gate."** Concrete evidence: 4 G9.I6 violations across IL + the MOC pattern from MetaSystem indicates the template skeleton's structural sections are not enforced. **Not committed this session** — one cross-system instance is the threshold for adding a whole-system invariant; this is the second-strongest candidate. Hold for session 116+ unless `/audit-system` runs on a third system surfaces the same.

5. **Inter-skill contract versioning** (Pattern D above) — not yet committed.

## Re-audit guidance

Re-audit by re-running `/audit-system systems/improvement-loop/`. For drift detection, pass `--diff systems/improvement-loop/audit-reports/2026-06-12/manifest.md` to compare against this baseline.

To assess the 7 missing artifacts in this run, invoke IL `/assess-skill` (for SKILL.md files) or `/assess-agent --variant prompt-based` (for IL CLAUDE.md root) directly, or wait for the next full audit pass.

## Audit-trail patch (finding #22 resolution)

Per the session-114 self-audit gap and the handoff's task 2, `/audit-system` SKILL.md is patched this session to append a one-line run-record to `<target>/audit-reports/runs.md` on each `--write` invocation. Format:

```
2026-06-12  session-115  artifacts=43  bins=9  critical=4  missing=7  variant=il-audit
```

This is rule-11-compliant: a single line per run, no abstraction layer, no schema enforcement, no log rotation. If the file doesn't exist, the skill creates it with a header comment.

## Telemetry

- Bins: 9
- Parallel subagents spawned: 9
- Wall-clock: ~7 minutes
- Subagent invocation mode: `in-context-rubric` (Skill tool unavailable to workspace Librarian's `allowed_tools`; assessor SKILL.md read into context and rubric applied)
- Persisted bins: 5 (bins 1, 5, 6, 7, 8 — outputs exceeded visible budget)
- Visible-stream bins: 4 (bins 2, 3, 4, 9 — outputs fit in visible window; bins 2 and 4 partial)
- Format-compliance: bins 1, 3, 5, 6, 7, 8, 9 clean; bins 2 and 4 returned 1 of N expected sentinel blocks (partial output — surfacing as design-contract candidate #3)
- Self-tests: `assess-skill` and `assess-agent` were self-audited in bin 8 (meta-circular OK)
