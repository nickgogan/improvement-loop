---
name: Advisory-Only Recommendations for Broad-Blast or Persistent Mutations
summary: 'A concrete autonomy-tier assignment: when the system notices that a particular setting, flag, or configuration change would help, it surfaces a recommendation but refuses to apply it automatically.
  Applies specifically to actions whose effects persist across the cluster, database, or environment (not just the current session/run) — because a quiet mutation of broadly-scoped, persistent state has
  a much larger blast radius than any single run''s output. Human must apply the change manually and record the rollback command.'
implementation_notes: 'Concrete instance of the ''Human-required'' tier from the autonomy-gradient framework, pinned to a specific class of action: broad-blast or persistent mutations. For MetaSystem, this
  is the pattern to apply whenever an agent could modify schema, governance docs, shared config, cross-system rules, or any state that outlives the current session. The benchmark or tool doing the recommending
  is still autonomous; only the mutation is gated.'
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: null
applicability:
- General
adopted_in:
- improvement-loop
sources: []
related_findings:
- file: autonomy-gradient-not-binary-delegation.md
  rel: extends
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: budget-governance-with-hard-stop.md
  rel: same-problem
- file: screen-as-permissions-model-agent-bypass-failure.md
  rel: same-problem
- file: nine-primitive-document-agent-skeleton.md
  rel: same-problem
- file: task-risk-gradient-for-verification-depth.md
  rel: same-problem
- file: agentic-maintenance-fleet-typed-safe-outputs.md
  rel: same-problem
- file: no-autonomous-lifecycle-mutation-principle.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-07-13'
pipeline_status: raw
consumed_by: []
tags:
- governance
- autonomy-tier
- human-gate
- memongo
---

# Advisory-Only Recommendations for Broad-Blast or Persistent Mutations

## What It Is

A pattern for handling actions where an automated system can identify a helpful change but has no authority to apply it — because the change's blast radius is too big for quiet automation.

Memongo's concrete instance: the benchmark's **query-governance** lane detects MongoDB query-shape settings that would plausibly improve performance (via `consider-setQuerySettings` candidates in the benchmark report). It surfaces these as recommendations. It does not apply them.

The reasoning is specific: MongoDB query settings are **cluster-scoped and persistent.** Changing one affects every future query on that cluster, not just the current benchmark run. A silent mutation of broad, durable state is categorically different from a silent mutation of ephemeral state — so the autonomy tier changes even if the same system could technically execute both.

The maintainer-facing contract:
1. **System recommends.** The benchmark logs candidate settings with context (query stats, explain output references).
2. **Human inspects.** Operator reviews query stats and `explain` output to validate the candidate.
3. **Human applies.** Operator runs the setting in the intended environment manually.
4. **Human records.** The applied setting plus its rollback command go into an operator log.
5. **Human reverses if needed.** `removeQuerySettings` is the documented rollback path.

The system is fully autonomous up to step 1 and fully hands-off after it.

## Why It Matters

For MetaSystem specifically: we already have a binary human gate (DD-29) that defaults to "human-required" for anything non-trivial. That's safe but coarse — it doesn't distinguish between "this change affects only this session" and "this change affects every future session across all systems." Advisory-only-for-persistent-mutations is a sharper rule that gives us the language to say: *the agent can recommend freely; mutation of state with persistent or cross-session blast radius requires explicit human application.*

Concrete places this maps cleanly onto MetaSystem:
- **Schema changes.** Claude Build already human-gates these (constitution rule). Advisory-only formalizes what the pre-gate state looks like: agent recommends the schema change with rationale; Nick applies (or declines).
- **Governance doc mutations.** DD filings, DD amendments, `.claude/rules/*.md` edits — all persistent, cross-session, broad-blast. Owner agent already operates this way in practice; the pattern names it.
- **Cross-system config** — shared settings, MCP server registrations, hook scripts. An agent noticing a better value should recommend, not apply.

The pattern complements the autonomy-gradient framework (parent finding: `[[autonomy-gradient-not-binary-delegation]]`) by providing the concrete criterion for the "Human-required" tier: mutation × persistent/broad-blast scope.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo) — see `[[memongo-analysis]]` for structural details. Specifically in `docs/benchmarks/benchmark-operating-contract.md` §Query governance policy. The contract explicitly labels `query-governance` as `advisory-only` in the `benchmarkReport` output envelope, so the tier assignment is machine-readable, not just prose.

The contract's rationale is quoted directly: *"MongoDB query settings are cluster-scoped and persistent. Treat any `consider-setQuerySettings` candidate as an operator review item."* The pattern is driven by the blast-radius property, not by distrust of the benchmark's judgment.

## Potential Alternatives

- **Full autonomy with rollback.** The system could apply the setting and roll back if metrics degrade. Works for low-blast-radius changes; fails for anything that touches shared state because other consumers experience the degraded window.
- **Proposal-first with time-boxed approval.** The system applies after N hours if no human objection. Middle-ground; introduces a new failure mode (the approval window elapsing at the wrong time) and still requires the human-observation infrastructure.
- **Binary allowlist.** List exactly which settings the system may flip. Works for narrow domains; brittle and doesn't scale to the space of "all possible future tuning candidates."

## Potential Improvements

- **Structured recommendation envelope.** Memongo's advisory-only signal is embedded in the benchmark report; it's not a standalone "recommendations I'd apply if I could" surface. A dedicated recommendations log (with severity, evidence, recommended command, rollback command) would make the pattern reusable outside the benchmark context.
- **Blast-radius classification service.** The pattern hinges on "is this change persistent/broadly-scoped?" Codifying that as a classifier (with inputs: state scope, mutation durability, consumer count) would let other MetaSystem components assign tiers consistently.

## Potential Failure Modes

- **Recommendation fatigue.** If the system generates many advisory-only recommendations and none are actioned, the signal becomes noise. Memongo's version is tied to benchmark runs, so cadence is bounded.
- **Misclassification of blast radius.** A change labeled "advisory-only" might actually be safe to apply automatically (over-gated); a change labeled "autonomous" might actually have hidden persistent effects (under-gated). The classification itself needs rigor.
- **Operator handoff quality.** The pattern only works if the operator actually inspects and records. A tired operator copy-pasting the recommended command without inspecting query stats breaks the contract silently.
