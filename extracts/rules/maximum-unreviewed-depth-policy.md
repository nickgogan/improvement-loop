---
title: "Maximum Unreviewed Depth Policy — Review-Debt Cap Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "compound-review-debt-from-deferred-inspection"
identification_report: "agent-governance-and-trust.harvest-queue.md::compound-review-debt-from-deferred-inspection::rule::maximum-unreviewed-depth-policy"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "AI-assisted development workflows where agents produce changes faster than human reviewers can evaluate them in real time"
    - "branch-and-merge workflows where unreviewed work can accumulate on long-lived branches before reaching a review gate"
    - "any change pipeline that ships to a shared environment (production, staging, main) and accepts agent-generated work"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — relaxing or tightening the depth cap is a configuration change with no migration cost"
  auditability: "high when the depth cap is enforced by branch-protection or CI gates that compute the unreviewed-commit count automatically; medium when tracked manually; low when relied on by convention"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-observed in teams that hit batch-review pain and shifted to incremental review. No widely-published policy with a stated default depth; the cap parameter is per-organization."
contract:
  preconditions: "A change pipeline produces commits that flow toward a shared environment via review gates. The pipeline can be observed at branch-state granularity — the count of unreviewed commits since the last reviewed merge is computable. The team has authority to set and enforce a depth cap (a number, not a vibe)."
  invariants: "A maximum unreviewed depth `N` is stated in policy. At all times, the count of unreviewed agent-produced commits between any branch and the next merge gate toward production is ≤ `N`. When the count reaches `N`, further agent-produced commits to that branch are blocked at the gate; a review event must occur before the count can grow. The cap applies regardless of phase boundaries, milestone status, or scheduled review cadence — it is a hard ceiling, not a guideline."
  governance: "Owner: the policy that establishes branch protection, CI gates, or merge rules for the affected environment. The depth cap `N` is per-team; it must be a stated number, with stated reasoning for the value chosen, and a review cadence at which `N` is re-evaluated. Audit tooling reads each branch's commit history relative to the last reviewed merge and verifies the unreviewed-depth count. Exemptions (a single-author personal branch, a documentation-only branch with no production impact) must be declared explicitly with a stated scope."
  recovery: "If a branch is discovered with unreviewed depth > `N`: pause new work on that branch; trigger an immediate review (atomic if possible — review each commit; bulk if necessary — review the cumulative diff with explicit acknowledgment that review quality degrades with depth); record the overrun as a process incident, not a routine event. If the cap is being hit frequently across many branches: the cap is too low for current cadence, OR review capacity is insufficient — re-evaluate `N` upward only if review quality holds at the new depth, OR add review capacity. Never relax the cap as a substitute for review capacity. If a milestone or phase boundary lands between the cap and a planned review: do not let the boundary justify deferral; the cap fires regardless."
tags:
  - "extracted-artifact"
  - "rule"
  - "code-review"
  - "review-debt"
  - "branch-protection"
  - "compound-debt"
---

# Maximum Unreviewed Depth Policy — Review-Debt Cap Rule

**Source:** [[compound-review-debt-from-deferred-inspection]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A change pipeline produces commits that flow toward a shared environment (production, staging, main) via review gates. Some or all commits are agent-produced — the volume of changes risks exceeding the rate at which human review can keep up. The team has authority to set and enforce branch-protection or merge-rule policies on the pipeline.

Scope of application: any pipeline where unreviewed work can accumulate between gates. Most relevant for AI-assisted workflows where agent throughput substantially exceeds human review throughput.

## Action

**Required:** State a maximum unreviewed depth `N` in policy — a specific number, with stated reasoning. Enforce at every branch protection or merge gate: the count of unreviewed commits since the last reviewed merge must remain ≤ `N`. When the count reaches `N`, further commits to that branch are blocked at the gate; a review event must complete before the count can grow.

The cap fires regardless of phase boundaries, milestone schedules, or planned review cadence. It is a structural ceiling on accumulated review debt, not a soft target.

**Forbidden:** Deferring review past the cap "just until the milestone." Letting the cap drift upward without re-evaluating whether review quality holds. Treating the cap as a per-author or per-feature limit rather than a per-branch invariant. Allowing exemptions to grow ambient (every branch claims to be exceptional).

## Boundary

Enforced at every branch protection or merge gate that leads toward a shared environment. Applies branch-by-branch — each branch carries its own unreviewed-depth count relative to the last reviewed merge.

Out of scope: single-author personal branches that never reach a shared environment, documentation-only branches with no production impact (when explicitly declared), and trivial mechanical commits that are out-of-scope per the broader change-policy (formatter output, lockfile regeneration). Exemptions must be explicit, not ambient.

## Enforcement

- **Mechanism:** A branch-protection rule, CI check, or merge-gate hook computes the unreviewed-depth count for the branch (commits since the last commit that received explicit review approval). If the count > `N`, the gate blocks further commits or merges until a review event resets the count.
- **Check (deterministic):** For every branch `B` targeting a shared environment: `unreviewed_depth(B) <= N`. Where `unreviewed_depth(B)` = commits between `B`'s tip and the last commit on `B`'s ancestry that has a review-approval marker. Any branch with depth > `N` → gate blocked.
- **Violation response:**
  - *Branch hits the cap:* block further commits to that branch; trigger review of the accumulated commits. Atomic review (per-commit) preserves quality; bulk review of the cumulative diff is the fallback when atomic is infeasible — but bulk review must be explicitly acknowledged as such, not labeled as if it were atomic.
  - *Cap exceeded due to gate-bypass or misconfiguration:* treat as a process incident; investigate the bypass path; close it.
  - *Cap hit frequently across many branches:* the cap is too low for the team's current cadence (relax it only if review quality holds at the new depth — verified, not assumed) OR review capacity is insufficient (add reviewers). Never relax the cap as a substitute for review capacity.
  - *Milestone or phase boundary arrives near the cap:* the cap still fires; the boundary does not earn deferral. If the team needs to ship before review, that need has to be reckoned with explicitly, not by quietly extending the cap.
- **Cannot be silently exempted:** A branch that grows past `N` without explicit policy exemption is in violation. The rule does not require the cap to be permanent — it requires the cap to be *stated, enforced, and re-evaluated deliberately*.

## Rationale

The rule exists because review cost compounds with depth. Each unreviewed change embeds assumptions that subsequent changes build on; reviewing a chain after the fact requires reconstructing the cascade of assumptions, which costs much more per commit than per-commit review at change time.

The math is asymmetric. Ten changes reviewed individually at 10 minutes each is 100 minutes; the same ten changes reviewed as a batch can take 180+ minutes because the reviewer must untangle interconnected assumptions and determine which were valid at each step. Deferring review feels efficient at submit time and turns out to be expensive at review time.

The cap is the structural fix. It bounds accumulated review debt to a number where atomic-or-near-atomic review remains feasible. The team picks `N` based on observed review quality at different depths — not on what feels comfortable to authors who don't bear the review cost.

The rule respects the legitimate desire for high agent throughput. The depth cap does not slow agent output; it bounds how much agent output can ship without review. Throughput stays high; review keeps pace by being incremental rather than batched.

The rule is the positive-space restatement of the deferred-review anti-pattern. Rather than enumerating ways batch review fails (assumption cascade, untangle cost, milestone-boundary deferral, "we'll review at the end"), the positive invariant is "unreviewed depth ≤ stated cap, always, everywhere." One rule, deterministic enforcement.

## Failure Modes

- **Cap drift upward.** Initial `N=3`; over time it relaxes to `N=10`, then `N=20`, without re-evaluating whether review quality holds. Mitigation: every cap change is a deliberate decision with stated reasoning; track review-quality metrics across cap changes; revert if quality degrades.
- **Exemption sprawl.** "This branch is special" becomes ambient; most branches claim exemption. Mitigation: exemptions are stated explicitly per branch with scope and duration; default is no exemption; periodic audit of granted exemptions.
- **Bulk-review-as-atomic theater.** Reviewer skims a 10-commit diff in 12 minutes, claims atomic review. Mitigation: atomic review requires per-commit traceability — a commit-by-commit walk with notes; bulk review is acknowledged as bulk and accepts the lower-quality signal.
- **Cap hits cause shipping pressure.** Team feels pressure to relax the cap when it blocks a high-priority change. Mitigation: relaxing under pressure is the worst time to do it — the pressure is itself a signal that review capacity is undersized; address capacity, not the cap.
- **Per-author cap confusion.** The cap is interpreted as "each author can have N unreviewed commits" rather than "each branch has N unreviewed commits total." Mitigation: state the cap unambiguously (per-branch); enforce per-branch; treat per-author bookkeeping as a separate concern.
- **Cap unrelated to actual review-cost curve.** The team picks `N=20` because that's roughly what feels manageable, but actual review quality degrades sharply past `N=5`. Mitigation: measure review-cost-per-commit at different depths; pick `N` where the cost-per-commit curve is still flat; revisit when conditions change (new tooling, larger team, different change profile).

## Contract

### Preconditions
A change pipeline produces commits that flow toward a shared environment via review gates. The pipeline can be observed at branch-state granularity — the count of unreviewed commits since the last reviewed merge is computable. The team has authority to set and enforce a depth cap (a number, not a vibe).

### Invariants
A maximum unreviewed depth `N` is stated in policy. At all times, the count of unreviewed agent-produced commits between any branch and the next merge gate toward production is ≤ `N`. When the count reaches `N`, further agent-produced commits to that branch are blocked at the gate; a review event must occur before the count can grow. The cap applies regardless of phase boundaries, milestone status, or scheduled review cadence — it is a hard ceiling, not a guideline.

### Governance
Owner: the policy that establishes branch protection, CI gates, or merge rules for the affected environment. The depth cap `N` is per-team; it must be a stated number, with stated reasoning for the value chosen, and a review cadence at which `N` is re-evaluated. Audit tooling reads each branch's commit history relative to the last reviewed merge and verifies the unreviewed-depth count. Exemptions (a single-author personal branch, a documentation-only branch with no production impact) must be declared explicitly with a stated scope.

### Recovery
If a branch is discovered with unreviewed depth > `N`: pause new work on that branch; trigger an immediate review (atomic if possible — review each commit; bulk if necessary — review the cumulative diff with explicit acknowledgment that review quality degrades with depth); record the overrun as a process incident, not a routine event. If the cap is being hit frequently across many branches: the cap is too low for current cadence, OR review capacity is insufficient — re-evaluate `N` upward only if review quality holds at the new depth, OR add review capacity. Never relax the cap as a substitute for review capacity. If a milestone or phase boundary lands between the cap and a planned review: do not let the boundary justify deferral; the cap fires regardless.
