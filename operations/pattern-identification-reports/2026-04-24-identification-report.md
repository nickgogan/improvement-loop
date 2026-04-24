---
title: "Artifact Identification Report — 2026-04-24 (Drift §1 Sweep)"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-24"
scope: "Session 62 drift sweep: 17 session-58 null-priority findings + content-derived-temporal-expiration-contradiction-resolution (session-57 null-priority carry-over). Directed by Nick's Q3 annotation on priority-reassessment-2026-04-23.md."
session: 62
agent: "Codifier"
findings_scanned: 18
findings_filtered: 0
methodology_note: "Inline classification rather than Sonnet-subagent batches. Rationale: in-session scope expansion after IB-149 primary scope; rubric held in context; 18 findings within single-pass classification budget. Trade: single-model-pass reduces classification diversity. Nick may re-run via subagent batches if deeper rigor is wanted before /extract-artifacts."
---

# Artifact Identification Report — 2026-04-24

**Scope:** 18 null-priority findings — the Drift §1 set from IB-149 + the Drift §2 carry-over. All are at `pipeline_status: raw`.

**Findings scanned:** 18 | **Filtered out:** 0 | **Classified:** 18

**Companion report:** `priority-reassessment-2026-04-23.md` (form classification happens here; priority proposal happens below under "Priority Proposal Addendum" — normally out of /identify-artifacts scope but folded in per Nick's same-session directive).

---

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 17 | 94% | 12 | 4 | 1 |
| rule | 1 | 6% | 0 | 1 | 0 |
| template | 0 | 0% | 0 | 0 | 0 |
| skill | 0 | 0% | 0 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |
| **total** | **18** | — | **12** | **5** | **1** |

*Note: one finding is flagged for HITL on evidence grounds, not form-ambiguity grounds.*

**Calibration check:** 94% pattern-classification is at the 92% steady-state baseline from session-22 calibration. Consistent with the batch's mix of governance/evaluation findings (which co-occur with rules more than context-engineering findings do).

---

## Nick's Decisions (2026-04-24) — Authoritative

The inline table `Status` columns and per-finding `Status` fields below are **superseded by this block**. `/extract-artifacts` should treat this block as the contract.

| # | Finding | Form | Decision | Rationale |
|---|---|---|---|---|
| 1 | external-benchmark-hosting-as-trust-mechanism | pattern | **APPROVED** | Auto |
| 2 | benchmark-dataset-deprecation-lifecycle | pattern | **APPROVED** | Auto |
| 3 | experimental-sandbox-labeling-discipline | pattern | **APPROVED** | Guided |
| 4 | ensemble-eval-majority-required-for-success | pattern | **APPROVED** | Guided |
| 5 | production-configuration-baseline-discipline | pattern | **APPROVED** | Guided |
| 6 | agentic-search-memory-retrieval-architecture | pattern | **DEFERRED** | Weak evidence (sandbox-only; not production-shipped). Re-evaluate when a second corroborating production source appears. |
| 7 | confirm-failure-first-tdd-agent-discipline | **rule** | **APPROVED** | Nick confirmed initial rule classification (not overridden to pattern). Guided tier. |
| 8 | personal-knowledge-hoard-as-agent-substrate | pattern | **APPROVED** | Auto |
| 9 | interactive-explanations-extend-linear-walkthroughs | pattern | **APPROVED** | Auto |
| 10 | subagent-scope-priority-ladder | pattern | **APPROVED** | Guided |
| 11 | inline-scoped-mcp-servers-per-subagent | pattern | **APPROVED** | Auto |
| 12 | subagent-persistent-memory-directory | pattern | **APPROVED** | Auto |
| 13 | capability-restricted-agent-spawning-via-allowlist | pattern | **APPROVED** | Auto |
| 14 | subagent-isolation-contract | pattern | **APPROVED** | Auto |
| 15 | foreground-vs-background-subagent-permission-models | pattern | **APPROVED** | Auto |
| 16 | five-durable-verticals-ai-cannot-replace | pattern | **APPROVED** | Auto |
| 17 | agent-native-app-store-emerging-category | pattern | **DEFERRED** | Weak evidence (thesis-only; no production instance). Re-evaluate when evidence matures. |
| 18 | content-derived-temporal-expiration-contradiction-resolution | pattern | **APPROVED** | Auto |

**Priority addendum approved as proposed.** 11 × P2, 7 × P3, zero P1.

**Guide-routing check:** Logged as next-session todo (see IL PROGRESS.md and session-62 SL).

---

## Candidates

### HITL — Needs Human Decision

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 17 | [[agent-native-app-store-emerging-category]] | pattern | LOW | — | PENDING |

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 3 | [[experimental-sandbox-labeling-discipline]] | pattern | MED | rule | PENDING |
| 4 | [[ensemble-eval-majority-required-for-success]] | pattern | MED | rule | PENDING |
| 5 | [[production-configuration-baseline-discipline]] | pattern | MED | rule | PENDING |
| 7 | [[confirm-failure-first-tdd-agent-discipline]] | rule | MED | pattern | PENDING |
| 10 | [[subagent-scope-priority-ladder]] | pattern | MED | — | PENDING |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[external-benchmark-hosting-as-trust-mechanism]] | pattern | HIGH | — | PENDING |
| 2 | [[benchmark-dataset-deprecation-lifecycle]] | pattern | HIGH | — | PENDING |
| 6 | [[agentic-search-memory-retrieval-architecture]] | pattern | HIGH | — | PENDING |
| 8 | [[personal-knowledge-hoard-as-agent-substrate]] | pattern | HIGH | — | PENDING |
| 9 | [[interactive-explanations-extend-linear-walkthroughs]] | pattern | HIGH | — | PENDING |
| 11 | [[inline-scoped-mcp-servers-per-subagent]] | pattern | HIGH | — | PENDING |
| 12 | [[subagent-persistent-memory-directory]] | pattern | HIGH | — | PENDING |
| 13 | [[capability-restricted-agent-spawning-via-allowlist]] | pattern | HIGH | rule | PENDING |
| 14 | [[subagent-isolation-contract]] | pattern | HIGH | — | PENDING |
| 15 | [[foreground-vs-background-subagent-permission-models]] | pattern | HIGH | — | PENDING |
| 16 | [[five-durable-verticals-ai-cannot-replace]] | pattern | HIGH | — | PENDING |
| 18 | [[content-derived-temporal-expiration-contradiction-resolution]] | pattern | HIGH | — | PENDING |

---

## Details

### 1. external-benchmark-hosting-as-trust-mechanism

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, explicit-tradeoffs, multiple-alternatives
- **Co-occurrence:** none (one positive invariant exists — "external scoring" — but mechanism-level articulation is thin)
- **Rationale:** Center of gravity is the design philosophy of ceding scoring authority to infrastructure outside the vendor's control. Finding lists four alternatives (closed leaderboards, frameworks, self-reported, academic) and five failure modes — classic "it depends" character. Not a procedure (no ordered steps), not a binary constraint (no enforcement boundary at a named gate), not a template (no fillable backbone), not a role.
- **Status:** PENDING

### 2. benchmark-dataset-deprecation-lifecycle

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** lifecycle-shape, multiple-known-uses, tradeoffs
- **Co-occurrence:** none
- **Rationale:** Describes a 4-stage lifecycle (discovery → cleaned replacement → deprecation flag → publication of diff) as a design approach, not a procedure an agent would execute step-by-step. The shape generalizes across benchmarks, rubrics, and evaluators. Alternatives section (silent update, errata, fork, SemVer) establishes forces/tradeoffs. Pattern, not skill — no explicit invocation and the actor is a human maintainer, not an agent.
- **Status:** PENDING

### 3. experimental-sandbox-labeling-discipline

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** positive-space-governance, design-with-invariant, multiple-alternatives
- **Co-occurrence:** rule (the "any claim not in production config must carry an experimental label" invariant is a binary constraint at the publication boundary)
- **Rationale:** Center of gravity is the positive-space alternative to retraction-only governance. The finding explicitly frames itself as a bounded positive invariant vs unbounded rejection list. Pattern-form because the labeling *approach* generalizes; the specific syntax ("highly experimental") is an instance. Co-occurrence noted: the embedded invariant could be extracted as a rule in a governance ruleset.
- **Status:** PENDING

### 4. ensemble-eval-majority-required-for-success

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-space-taxonomy, tradeoffs, multiple-alternatives
- **Co-occurrence:** rule (the "never report union-of-successes as the accuracy" invariant at the evaluation-publication boundary)
- **Rationale:** Finding enumerates 4 aggregation rules (union, majority-vote, best-of-N, single-path) with tradeoffs. Design-space analysis is pattern-shaped. The load-bearing insight — "aggregate the way you ship" — is a philosophy with a rule as its mechanical instantiation. Pattern primary, rule secondary per DD-77.
- **Status:** PENDING

### 5. production-configuration-baseline-discipline

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** positive-space-invariant, multiple-failure-modes, design-alternatives
- **Co-occurrence:** rule ("benchmark config must match production config" at the publication boundary)
- **Rationale:** Same structural shape as findings #3 and #4 — positive-space governance pattern with an embedded rule. Center of gravity is the design approach; the specific configuration requirements are instantiations. Third-party adjudicated evidence strengthens pattern status (multiple orgs now discuss this as a norm).
- **Status:** PENDING

### 6. agentic-search-memory-retrieval-architecture

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** architectural-shape, design-space-positioning
- **Co-occurrence:** none
- **Rationale:** Describes a memory-system architecture (ingestion / retrieval / answering with agent-driven stages). Explicitly positioned within a 4-pole design space (multi-store / single-store / verbatim / agentic). Pattern form — the architectural shape generalizes across specific implementations.
- **Flag:** Evidence is Low (single-vendor sandbox, not production-shipped). Form-classification is HIGH (unambiguous pattern); evidence-classification is weak. Nick may wish to defer extraction until production corroboration.
- **Status:** PENDING

### 7. confirm-failure-first-tdd-agent-discipline

- **Assigned form:** rule
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** must-language, deterministic-check, enforcement-boundary
- **Co-occurrence:** pattern (the broader "agents need discipline layers beyond human TDD" framing)
- **Rationale:** Center of gravity is the specific invariant — "agent MUST verify test fails before implementing." Explicit "MUST" language, deterministic boundary (between step 1 and step 2 of the TDD cycle), binary check (test fails / test passes). Could be pattern if we treat "agent-specific discipline layer" as the insight; I assign rule because the mechanism IS the insight — without the exact invariant, the finding reduces to "agents need discipline" which is not novel.
- **Note for Nick:** This is the only non-pattern classification in the batch. Override to pattern is plausible if Nick reads the center of gravity as "why agents need explicit discipline" rather than the specific invariant. Drop to guided tier surfaces this for human read.
- **Status:** PENDING

### 8. personal-knowledge-hoard-as-agent-substrate

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, four-properties, tradeoffs
- **Co-occurrence:** none
- **Rationale:** Four-property design approach for agent-reachable personal corpus. Has tradeoffs (sprawl, staleness, single-author fragility) and multiple alternatives (curated wiki, RAG, prompt libraries). Generalizes across scopes (personal, system, org). Pure pattern.
- **Status:** PENDING

### 9. interactive-explanations-extend-linear-walkthroughs

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** pairing-shape, complementary-not-substitute, axis-table
- **Co-occurrence:** none
- **Rationale:** Shape is the pairing — linear walkthrough + interactive explanation as complementary artifacts for different questions (structure vs behavior). Comparison axis table codifies when to use which. Pattern — generalizes across algorithms and documentation contexts.
- **Status:** PENDING

### 10. subagent-scope-priority-ladder

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** precedence-shape, specific-to-platform-but-generalizable
- **Co-occurrence:** none
- **Rationale:** Center of gravity is the design pattern "use deterministic priority ordering for scope resolution" — applied here to Claude Code subagents via 5-level ladder. TRAP 2 applies: the specific Anthropic 5-level table is an instantiation of a broader shape. Confidence MED because the finding's exposition leans heavily on the specific mechanism; could be read as rule-at-platform ("at this boundary the precedence IS X"). I classify as pattern because the shape transfers to other scope-resolution problems (IL skill distribution noted in finding body).
- **Status:** PENDING

### 11. inline-scoped-mcp-servers-per-subagent

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** context-economy-shape, lifecycle-scoped-resource
- **Co-occurrence:** none
- **Rationale:** Shape is "scope resource availability to the component that needs it; release at component boundary" — applied to MCP servers. Generalizes to any resource-scoping decision (permissions, skills, tool descriptions). Pattern.
- **Status:** PENDING

### 12. subagent-persistent-memory-directory

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** memory-shape, auto-curation-budget, tradeoffs
- **Co-occurrence:** none
- **Rationale:** The design approach is "filesystem-resident per-specialist memory with auto-curation at a fixed budget." The Claude Code feature is an instantiation; the shape generalizes to any long-lived specialist agent needing compounding knowledge. Four alternatives + six failure modes make it clear this is a pattern, not a mechanism.
- **Status:** PENDING

### 13. capability-restricted-agent-spawning-via-allowlist

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** capability-based-security, allowlist-shape, delegation-scoping
- **Co-occurrence:** rule (the allowlist syntax itself embeds binary constraints)
- **Rationale:** Pattern is "capability allowlist for delegation scoping." Inherits from established capability-based security models. The Claude Code syntax is one instantiation; the shape (allowlist, not denylist; silent block; scope: main-thread only) applies to any delegation model.
- **Status:** PENDING

### 14. subagent-isolation-contract

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** isolation-design-approach, three-part-contract, impermanence-principle
- **Co-occurrence:** none
- **Rationale:** Three-part isolation contract described as design philosophy. Finding itself connects to the broader [[agent-architecture-layer-impermanence]] principle — explicit evidence of abstraction above the specific mechanism. Pattern.
- **Status:** PENDING

### 15. foreground-vs-background-subagent-permission-models

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** two-mode-design-space, safety-envelope-tradeoffs
- **Co-occurrence:** none
- **Rationale:** Design-space analysis separating "user available" from "user away" permission models. Two modes with distinct tradeoff profiles. Pattern — the mode split generalizes beyond Claude Code (any interactive vs batch permission model can adopt).
- **Status:** PENDING

### 16. five-durable-verticals-ai-cannot-replace

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** strategic-framework, five-part-taxonomy, positioning-heuristic
- **Co-occurrence:** none
- **Rationale:** Strategic framework for durability under foundation-model improvement. Heuristic/decision-framework character — explicitly "use this lens to evaluate positioning." Per rubric Calibration §4, strategic frameworks → pattern. HIGH confidence: no form ambiguity; the insight is the taxonomy and its application lens.
- **Status:** PENDING

### 17. agent-native-app-store-emerging-category

- **Assigned form:** pattern
- **Confidence:** LOW
- **Tier:** hitl
- **Reason codes:** thesis-not-implementation, forward-looking, weak-evidence
- **Co-occurrence:** none
- **Rationale:** Form classification is pattern (design-space hypothesis with five axes). Confidence LOW not because form is ambiguous but because **evidence is Weak** — the finding explicitly says "no production instance yet, thesis / practitioner hypothesis." Per §1 pattern exclusion signal: "Single-source evidence with no convergent adoption → not yet ready; leave as finding at P3." I honor that signal by sending to HITL rather than auto-classifying.
- **Recommendation to Nick:** Leave as-is at pattern form but consider not extracting until a second corroborating source emerges. Alternatively, reject from this identification run and revisit when evidence matures.
- **Status:** PENDING

### 18. content-derived-temporal-expiration-contradiction-resolution

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** memory-decay-design-approach, two-mechanism-pairing, design-space-positioning
- **Co-occurrence:** none
- **Rationale:** Described as one of three complementary strategies in the memory-decay design space. Has tradeoffs, failure modes, alternatives. Part of the decay-cluster sub-dimension now formalized in research-dimensions.md (2026-04-24 update). Pattern.
- **Status:** PENDING

---

## Guide Cluster Check (DD-81)

Pattern findings mapped to guide clusters per `operations/references/guide-routing-table.md`:

*Not executed in this run.* The routing table lookup is a separate pass that benefits from the priority-assigned set, not the null-priority intake. After Nick approves this batch and priorities are set, a pass over the newly-P2 findings would be the natural time to check routing. Flagged as a follow-up, not a blocker.

---

## Priority Proposal Addendum *(out of /identify-artifacts scope; folded in per Nick's same-session directive)*

Per the skill contract, `/identify-artifacts` does not assign priority — that flows from `/promote-findings` at intake. These 18 findings are null-priority because `/promote-findings` in sessions 57–58 did not emit a priority field (a separate upstream drift worth tracking). Below are proposed baseline priorities using the `/reassess-priorities` Criterion 1 rubric (single-source = P3 baseline unless evidence or cross-reference warrants P2).

| # | Finding | Evidence | Sources | Proposed priority | Rationale |
|---|---|---|---|---|---|
| 1 | external-benchmark-hosting-as-trust-mechanism | Low | 1 | **P3** | Single-vendor-documented; normative pattern but not yet corroborated |
| 2 | benchmark-dataset-deprecation-lifecycle | Medium | 1 | **P3** | Single source but concrete evidence; will likely corroborate |
| 3 | experimental-sandbox-labeling-discipline | Low | 1 | **P3** | Single-vendor; positive-space governance — track for convergence |
| 4 | ensemble-eval-majority-required-for-success | Medium | 1 + inferential | **P2** | Strong principle, wide applicability to IL's own `/assess-*` skills |
| 5 | production-configuration-baseline-discipline | Medium | 1 (third-party adjudicated) | **P2** | Third-party adjudication gives it more weight than single-vendor claims |
| 6 | agentic-search-memory-retrieval-architecture | Low | 1 (sandbox) | **P3** | Experimental; defer until production corroboration |
| 7 | confirm-failure-first-tdd-agent-discipline | Strong | 1 (Simon Willison) | **P2** | Strong evidence, directly applicable to IL's test-writing skills |
| 8 | personal-knowledge-hoard-as-agent-substrate | Medium | 1 (Simon Willison at scale) | **P2** | MetaSystem's own IL-KB is an instance; high applicability |
| 9 | interactive-explanations-extend-linear-walkthroughs | Medium | 1 (Simon Willison) | **P2** | Directly relevant to your visualization brainstorm (project memory) |
| 10 | subagent-scope-priority-ladder | Strong | 1 (Anthropic canonical) | **P2** | First-party canonical spec; governance primitive |
| 11 | inline-scoped-mcp-servers-per-subagent | Strong | 1 (Anthropic canonical) | **P2** | Directly applicable given workspace's ~10 MCP servers |
| 12 | subagent-persistent-memory-directory | Strong | 1 (Anthropic canonical) | **P2** | Aligns with Librarian encounter-log pattern; ready to instantiate |
| 13 | capability-restricted-agent-spawning-via-allowlist | Strong | 1 (Anthropic canonical) | **P2** | Governance primitive for future Owner → specialist orchestration |
| 14 | subagent-isolation-contract | Strong | 1 (Anthropic canonical) | **P2** | Foundational; informs every subagent decision downstream |
| 15 | foreground-vs-background-subagent-permission-models | Strong | 1 (Anthropic canonical) | **P2** | Operationally relevant for long-running IL skills |
| 16 | five-durable-verticals-ai-cannot-replace | Medium | 1 (Nate B. Jones) | **P3** | Strategic framework; useful lens but not a mechanism to adopt |
| 17 | agent-native-app-store-emerging-category | Weak | 1 (Nate B. Jones hypothesis) | **P3** | Thesis-level; monitor |
| 18 | content-derived-temporal-expiration-contradiction-resolution | Medium | 1 (Supermemory) | **P3** | Per Nick's hold on cluster normalization — baseline P3; cluster-level elevation is a separate future call |

**Summary:** 11 × P2, 7 × P3. Zero P1 (consistent with single-source baselines).

---

## Proposed Edits (Pending Approval)

### Form classification back-annotation (per Step 7 of /identify-artifacts)

Set `pipeline_status: classified` on all 18 findings regardless of approval tier. This is a pipeline-tracking field, not a content commitment — the `Status` field in this report governs extraction.

### Priority assignment (conditional on Nick's approval of addendum)

Apply the priorities from the addendum table as `priority: P2` or `priority: P3` on the corresponding finding files, with `last_updated: "2026-04-24"`.

---

## Open Questions for Nick

1. **Finding #7 (confirm-failure-first-tdd) classified as rule, not pattern.** Only non-pattern in the batch. Override to pattern is plausible if you read center of gravity as "why agents need explicit discipline." Called guided tier for your read.

2. **Finding #17 (agent-native-app-store) sent to HITL on evidence grounds.** Form is pattern; evidence is Weak. Options: (a) accept at LOW confidence and let it sit as classified-pending-extraction; (b) reject from this run until a second corroborating source arrives; (c) accept but mark `deferred` — no extraction until evidence matures.

3. **Finding #6 (agentic-search-memory-retrieval) is form-HIGH but evidence-Low.** Classified auto-tier, but you may want to treat it the same as #17 given sandbox-only evidence.

4. **Priority addendum: approve the table?** 10 × P2, 8 × P3. No P1 given single-source baselines. Edits wait on your go.

5. **Guide routing check skipped this run.** Would normally run after classification; skipped because baseline priorities aren't assigned yet. Natural follow-up after (4) is approved.

---

## Next Steps on Approval

1. Back-annotate `pipeline_status: classified` on the 18 findings.
2. If priority addendum approved: apply `priority:` edits + `last_updated: "2026-04-24"`.
3. Close IB-149 (`status: Done`).
4. File SL entry at `systems/improvement-loop/operations/system-log/session-62-codifier-ib-149-reassess.md` logging the full session's work.
5. Optionally: run guide-routing check over the newly-P2 patterns.
