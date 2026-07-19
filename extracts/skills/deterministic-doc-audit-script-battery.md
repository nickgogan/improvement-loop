---
title: "Deterministic Documentation-Audit Script Battery"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "deterministic-doc-audit-battery"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-governance-and-trust.harvest-queue"
identification_report: "agent-governance-and-trust.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams maintaining a documentation or governance surface (indexes, registries, cross-references) across an agent-edited repository"
    - "repositories where doc-consistency rules — dead links, index bidirectionality, size budgets, data-boundary hygiene — can be checked mechanically rather than by judgment"
    - "workflows that want a read-only pre-edit or pre-commit gate instead of spending model tokens re-deriving consistency from memory each session"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — read-only script that emits a findings list and never modifies the tree; adopting or removing it carries no migration cost"
  auditability: "high — every check has a stable ID and prints [FAIL]/[warn] with an embedded remediation; the exit code is a binary gate and every result is reproducible by re-running the script"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented in a single production system running 16 live checks. A soft-cap/hard-cap line-budget commit hook (warn over one threshold, block over a second) is a partial instance of the same check shape."
contract:
  preconditions: "The repository has a documentation/governance surface whose rules can be expressed mechanically (registry membership, link resolution, index bidirectionality, size budgets, data-boundary patterns). A scripting runtime is available (the reference implementation is stdlib-only Python with deliberate line/regex parsing and no YAML dependency). Each rule is stable enough to encode as a pure function over the repo root."
  invariants: "The script is read-only and never modifies the tree. Every check carries a stable ID and a severity split (error vs. warn); only errors gate (exit 1), warnings inform (exit 0 remains allowed). Every failure message embeds its own remediation instruction. The script — not the model's memory — is the ground truth for consistency, and exit 0 is the gate. A check that parses to zero rows raises a meta-error rather than passing silently, so a doc reformat cannot mask a broken check as a green result."
  governance: "Owner: whoever owns the repository's documentation-governance policy. Check IDs and severities are a governance surface because downstream skills and commit messages reference the stable IDs — changing them is a deliberate decision, not a refactor. New checks are added deliberately and a retirement discipline prunes dead ones. The wrapping skill mandates 'audit before edit' (run the script first, never propose fixes from memory) and 're-run must exit 0' after applying fixes."
  recovery: "If a check breaks because a doc was reformatted (its regex no longer matches), the parsed-to-zero-rows meta-error flags it — fix the check or the doc; never accept the resulting false green. If exit 0 is reached but content correctness is still in doubt, pair the battery with an explicit judgment sweep, since structural consistency is not content truth. If checks accumulate past maintenance capacity, run a retirement pass to remove dead checks."
tags:
  - "extracted-artifact"
  - "skill"
  - "deterministic-enforcement"
  - "doc-governance"
  - "drift-detection"
---

# Deterministic Documentation-Audit Script Battery

**Source:** [[deterministic-doc-audit-battery]]
**Form:** skill
**Extraction date:** 2026-07-19

## Purpose

Enforce a repository's entire documentation-governance surface with one read-only script instead of asking a model, every session, whether the docs are still consistent. Any doc-consistency rule that *can* be a script *becomes* a script: a single file registers a flat list of named checks, each a pure function over the repo root, each printing `[FAIL]`/`[warn]` with a stable ID and an embedded fix instruction. Exit 0 is the gate. Model judgment is reserved for what a script genuinely cannot see (content truth), not for consistency a script answers exactly, for free, every run.

## Inputs

- The repository root (read access to the documentation/governance tree).
- A scripting runtime — the reference implementation is a single ~580-line stdlib-only Python file using deliberate line/regex parsing (no YAML dependency, so the parser itself never drifts against a library version).
- The set of doc-governance rules to encode, each expressible as a deterministic predicate over files/paths/contents.

## Outputs

- Exit code as the gate: `0` = clean (warnings permitted), `1` = one or more errors, `2` = usage error.
- A findings list: each finding names its stable check ID, its severity (`[FAIL]` vs. `[warn]`), and a remediation instruction telling the reader exactly which command or refresh resolves it.
- No tree mutation — the script only reports; fixing is a separate, human- or agent-driven act.

## Steps

1. **Register checks as pure functions.** Each check takes the repo root and returns findings; all checks live in one flat registry so the battery is enumerable and its coverage is visible at a glance.
2. **Assign each check a stable ID and severity.** IDs (e.g., `C1`…`C16`) are referenced by other skills and by commit messages, so they are treated as a stable contract. Severity splits errors (which gate) from warnings (which only inform).
3. **Embed remediation in every failure message.** A failure says not just *what* broke but *how to fix it* ("run the session-handoff routine", "refresh the manifest") so the reader never has to reverse-engineer the fix.
4. **Run read-only over the tree.** The script inspects; it never writes. This makes it safe to run anywhere, any number of times, including inside autonomous loops.
5. **Gate on exit 0.** Treat the script — not model memory — as ground truth. The wrapping skill enforces "audit before edit" (run first, don't propose fixes from memory) and "re-run must exit 0" after applying fixes.
6. **Guard the parser against silent breakage.** Any check that parses to zero rows emits a meta-error, so a doc reformat that breaks a regex surfaces loudly instead of passing as a false green.
7. **Maintain the battery.** Add checks deliberately; run a periodic retirement pass so dead checks don't accumulate maintenance cost.

### Representative check taxonomy (from the reference implementation)

Grouped by the drift class each catches — a menu to adapt, not a fixed set:

- **Index/registry completeness (bidirectional):** every registry entry exists on disk *and* every on-disk item is registered; skill/name-to-directory agreement; cookbook/manual coverage; artifact-matrix ↔ routing-table cross-reference in both directions.
- **Referential integrity:** relative links in critical-path docs resolve to real files; entry-point docs reference the required vision-layer anchors so the load-order chain stays intact.
- **Structural convention conformance:** required file pairs exist in key folders; repo root carries only whitelisted files; packaged/exportable units carry their required companion files; contract-file integrity (one wiring row per canon doc, controlled-vocabulary IDs).
- **Data-boundary hygiene (privacy/separability):** no user identifier leaks into an export set (full-id match errors, bare-name token warns); system-only docs ban user display names.
- **Token-economy budgets:** volatile count-like phrases in a living doc warn (metrics rot); a control-surface doc has a soft-cap line budget (warn) and a hard-cap (fail) — and the failure message says "compact," never "raise the cap."
- **Derived-content freshness:** hashes in a manifest match the live source files; any new path-scoped rule missing from the manifest also fails.

## Failure Modes

- **Regex encodes structure assumptions.** Checks parse table formats and heading names by pattern; a doc reformat can silently break parsing. Mitigation: the "parsed to zero rows" meta-error pattern — a check that finds nothing to parse fails loudly instead of passing.
- **Green proves structure, not truth.** Exit 0 confirms structural consistency only, not content correctness. Mitigation: pair the deterministic battery with an explicit judgment sweep for content-level truth.
- **Monotonic battery growth.** Without a retirement discipline, dead checks accumulate and raise maintenance cost. Mitigation: periodic prune pass.
- **ID churn breaks references.** Because IDs are cited by other skills and commit messages, renaming or renumbering checks silently breaks those references. Mitigation: treat IDs as a stable contract governed like any other interface.

## Contract

### Preconditions
The repository has a documentation/governance surface whose rules can be expressed mechanically (registry membership, link resolution, index bidirectionality, size budgets, data-boundary patterns). A scripting runtime is available (the reference implementation is stdlib-only Python with deliberate line/regex parsing and no YAML dependency). Each rule is stable enough to encode as a pure function over the repo root.

### Invariants
The script is read-only and never modifies the tree. Every check carries a stable ID and a severity split (error vs. warn); only errors gate (exit 1), warnings inform (exit 0 remains allowed). Every failure message embeds its own remediation instruction. The script — not the model's memory — is the ground truth for consistency, and exit 0 is the gate. A check that parses to zero rows raises a meta-error rather than passing silently, so a doc reformat cannot mask a broken check as a green result.

### Governance
Owner: whoever owns the repository's documentation-governance policy. Check IDs and severities are a governance surface because downstream skills and commit messages reference the stable IDs — changing them is a deliberate decision, not a refactor. New checks are added deliberately and a retirement discipline prunes dead ones. The wrapping skill mandates "audit before edit" (run the script first, never propose fixes from memory) and "re-run must exit 0" after applying fixes.

### Recovery
If a check breaks because a doc was reformatted (its regex no longer matches), the parsed-to-zero-rows meta-error flags it — fix the check or the doc; never accept the resulting false green. If exit 0 is reached but content correctness is still in doubt, pair the battery with an explicit judgment sweep, since structural consistency is not content truth. If checks accumulate past maintenance capacity, run a retirement pass to remove dead checks.
