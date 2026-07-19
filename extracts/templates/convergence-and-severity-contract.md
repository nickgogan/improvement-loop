---
title: "Convergence-and-Severity Contract"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "convergence-loop-optimizer-family-contract"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "eval-driven-improvement-loops.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams building more than one artifact optimizer (code, docs, prompts, skills, queries, UI, or similar) who want shared quality semantics instead of one-off audit-and-report tools"
    - "designers deciding what 'verified' means for a given artifact type before wiring an autonomous fix loop around it"
    - "systems with a router that dispatches to per-artifact-type optimizer members and wants one contract those members all honor"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "medium — the contract document itself is trivial to revise, but once optimizer members are built against it, changing severity definitions or the convergence criterion requires re-auditing every member for consistency"
  auditability: "high — severity levels, the fix/ship boundary, and the convergence stop condition are named and quantified per member in one table, so an outside reviewer can check whether a given optimizer run actually satisfied the contract"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented as a production system at a large enterprise, implemented as one shared contract with six per-artifact-type members (code, prose, prompts, skills, SQL, UI) dispatched through a single router; no adoption recorded in this system yet."
contract:
  preconditions: "More than one artifact-type optimizer is being built or is planned, so a shared contract has a genuine second consumer (a single one-off optimizer doesn't need this scaffold). Each artifact type has a definable verify gate — some deterministic or near-deterministic way to confirm a fix didn't regress anything (build+lint+tests, fact-check, held-out eval, EXPLAIN parity, or equivalent). A severity scale is acceptable as the shared fix/ship boundary across all member types."
  invariants: "Every member fills in all five contract slots: multi-pass audit (with its own lens set), severity rating on the shared five-level scale, fix-in-place for every Medium-or-higher finding, a verify gate specific to that artifact type, and a convergence loop that terminates on 'no Medium+ remains' or an iteration cap. The severity scale (Blocker > High > Medium > Low > Nit) and its Medium=fix-boundary / High=ship-boundary meaning are shared across all members — no member privately redefines what a severity level means. Re-audits inside the convergence loop are blind (fresh context) — a re-audit that remembers its own prior fixes is convergence theater, not verification. Fix-in-place is never enabled without its member's verify gate wired and working; an unverified auto-fix loop is a regression generator, not an optimizer."
  governance: "Owner: whoever owns the router/family (the team maintaining the shared contract document and the dispatch table). Adding a new member requires defining that member's lens set and verify gate against the existing contract, not inventing a parallel one. Changing the shared severity scale or convergence criterion is a contract-level change reviewed against every existing member, not a per-member decision."
  recovery: "If fix-in-place ships without a working verify gate → disable fix-in-place for that member until the gate exists; audit-only (report, no autonomous fix) is the safe fallback. If a re-audit inside the convergence loop is found to not be blind → fix the harness to force fresh context per pass before trusting further convergence claims from that member. If the iteration cap is hit without convergence → surface the remaining Medium+ findings explicitly rather than silently declaring success; do not raise the cap indefinitely without checking findings are still dropping materially per iteration. If severity definitions drift between members → realign to the shared scale before comparing or aggregating results across members."
tags:
  - "extracted-artifact"
  - "template"
  - "evaluation"
  - "convergence-loop"
  - "severity-scale"
  - "quality-gates"
---

# Convergence-and-Severity Contract

**Source:** [[convergence-loop-optimizer-family-contract]]
**Form:** template
**Extraction date:** 2026-07-19

A shared quality-engine contract that multiple per-artifact-type optimizers implement identically: multi-pass audit, a five-level severity rating, fix-in-place for Medium+ findings, a verify gate that backs out regressions, and a convergence loop with an explicit stop condition. One contract, stamped out per artifact type — the members differ only in *which lenses* and *what counts as verified*.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{FAMILY_NAME}}` | Name of the optimizer family (e.g., "deep-optimizer") | Yes |
| `{{MEMBER_N_NAME}}` | Name of member N (one row per artifact type the family optimizes) | Yes (≥1) |
| `{{MEMBER_N_TARGET}}` | What member N operates on (source files, prose docs, prompts, skills, queries, UI screens, …) | Per member |
| `{{MEMBER_N_LENS_N}}` | Name of one audit lens/pass for member N (structure, accuracy, voice, security, …) | Per member (≥1) |
| `{{MEMBER_N_VERIFY_GATE}}` | The concrete check that confirms a fix didn't regress this artifact type (build+lint+tests, fact-check, held-out eval, EXPLAIN parity, …) | Per member |
| `{{SEVERITY_SCALE}}` | The shared severity levels, ordered (default: Blocker > High > Medium > Low > Nit) | Yes |
| `{{FIX_BOUNDARY}}` | The severity level at/above which a finding is fixed rather than reported (default: Medium) | Yes |
| `{{SHIP_BOUNDARY}}` | The severity level at/above which shipment is withheld (default: High) | Yes |
| `{{ITERATION_CAP}}` | Base iteration cap for the convergence loop (e.g., 3) | Yes |
| `{{ITERATION_CAP_EXTENDED}}` | Extended cap if findings are still dropping materially per iteration (e.g., 5) | Optional |
| `{{PRODUCTIVE_DROP_THRESHOLD}}` | Minimum per-iteration finding-count drop that justifies extending the cap (e.g., "≥50%") | Optional |

## Body

```markdown
# {{FAMILY_NAME}} — Convergence-and-Severity Contract

## Shared Contract
1. Multi-pass audit — independent lenses, run in parallel where possible.
2. Severity rating — every finding rated on: {{SEVERITY_SCALE}}.
3. Fix in place — every finding at or above {{FIX_BOUNDARY}} is fixed, not just reported.
4. Verify gate — re-check after fixing; any regressing change is backed out.
5. Convergence loop — re-audit (blind, fresh context) and repeat until no finding at or
   above {{FIX_BOUNDARY}} remains, or {{ITERATION_CAP}} iterations are hit
   (extend to {{ITERATION_CAP_EXTENDED}} while findings drop {{PRODUCTIVE_DROP_THRESHOLD}}
   per iteration).

Ship is withheld while any finding at or above {{SHIP_BOUNDARY}} remains unresolved.

## Members

| Member | Target | Lenses | Verify gate |
|---|---|---|---|
| {{MEMBER_1_NAME}} | {{MEMBER_1_TARGET}} | {{MEMBER_1_LENS_1}}, ... | {{MEMBER_1_VERIFY_GATE}} |
<!-- one row per member -->

## Router
A logic-free router selects the correct member for a given artifact; it contains no
optimization logic of its own.
```

## Usage

1. **Define the contract once, before members.** Write the shared five-slot contract (audit, severity, fix, verify, converge) before building any individual member — members should implement the contract, not each invent their own version of it.
2. **Give every member a real verify gate before enabling fix-in-place.** A member with fix-in-place but no verify gate is a regression generator, not an optimizer — audit-only is the safe default until the gate exists.
3. **Keep the severity scale shared, not per-member.** If one member's "High" means something different from another's, findings and ship/block decisions stop being comparable across the family.
4. **Force blind re-audits inside the loop.** A re-audit that remembers its own prior fixes converges because it stopped looking, not because the artifact is clean — run each convergence pass in fresh context.
5. **Let the iteration cap adapt to productivity, not run forever.** Extend past the base cap only while findings are still dropping materially; a loop that's stopped making progress should surface remaining findings rather than keep iterating.
6. **Add members against the existing contract, not beside it.** A new artifact type gets a lens set and a verify gate defined against the shared contract — not a parallel audit-and-fix tool that happens to look similar.

## Variation Axis

What drives different renderings of this scaffold:

- **Number of members.** A family with one artifact type in mind can still benefit from writing the contract explicitly (it constrains scope creep), but the router table is trivial; multi-member families are where the shared-contract payoff shows up most.
- **Verify-gate strength.** Deterministic gates (build+lint+tests, EXPLAIN parity) support more autonomous fix-in-place; softer gates (fact-check, held-out eval) may warrant a human checkpoint before the loop proceeds unattended.
- **Ship-boundary strictness.** Some deployments block shipment at High; others may only block at Blocker, treating High as a strong warning rather than a hard gate — a per-family policy choice.
- **Cross-model / independent-verifier option.** Families operating with higher autonomy may route the blind re-audit through a different model or a separate verifier process to decorrelate the check from the fixer (Goodhart guard); lower-autonomy families may accept same-model re-audits.

## Contract

### Preconditions
More than one artifact-type optimizer is being built or is planned, so a shared contract has a genuine second consumer (a single one-off optimizer doesn't need this scaffold). Each artifact type has a definable verify gate — some deterministic or near-deterministic way to confirm a fix didn't regress anything (build+lint+tests, fact-check, held-out eval, EXPLAIN parity, or equivalent). A severity scale is acceptable as the shared fix/ship boundary across all member types.

### Invariants
Every member fills in all five contract slots: multi-pass audit (with its own lens set), severity rating on the shared five-level scale, fix-in-place for every Medium-or-higher finding, a verify gate specific to that artifact type, and a convergence loop that terminates on "no Medium+ remains" or an iteration cap. The severity scale (Blocker > High > Medium > Low > Nit) and its Medium=fix-boundary / High=ship-boundary meaning are shared across all members — no member privately redefines what a severity level means. Re-audits inside the convergence loop are blind (fresh context) — a re-audit that remembers its own prior fixes is convergence theater, not verification. Fix-in-place is never enabled without its member's verify gate wired and working; an unverified auto-fix loop is a regression generator, not an optimizer.

### Governance
Owner: whoever owns the router/family (the team maintaining the shared contract document and the dispatch table). Adding a new member requires defining that member's lens set and verify gate against the existing contract, not inventing a parallel one. Changing the shared severity scale or convergence criterion is a contract-level change reviewed against every existing member, not a per-member decision.

### Recovery
If fix-in-place ships without a working verify gate → disable fix-in-place for that member until the gate exists; audit-only (report, no autonomous fix) is the safe fallback. If a re-audit inside the convergence loop is found to not be blind → fix the harness to force fresh context per pass before trusting further convergence claims from that member. If the iteration cap is hit without convergence → surface the remaining Medium+ findings explicitly rather than silently declaring success; do not raise the cap indefinitely without checking findings are still dropping materially per iteration. If severity definitions drift between members → realign to the shared scale before comparing or aggregating results across members.
