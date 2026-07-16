# Co-occurrence Harvest Queue — Building Agentic Systems

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

Note: the prior queue for this guide was fully resolved and archived at
`archive/guides/building-agentic-systems.harvest-queue.md` (session-146 harvest-queue close).
Its resolved `(source_finding, target_form)` tuples suppress re-emission for the carried-over
findings; rows below come from the findings newly absorbed in the session-147 regen.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | template | [[machine-readable-system-contract-with-wiring-rows]] | "System-contract wiring-row schema (five fields)" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[invariant-column-as-contract-field]] | "Every wiring row must declare a binary-testable invariant" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[harness-adaptation-protocol-graded-capability-intersection]] | "Harness adaptation and install protocol" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[wiring-canon-abstract-then-adapt-doc-structure]] | "Three-section wiring-canon doc format" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[dr-research-to-skill-gated-pipeline]] | "Gap-aware research-to-capability pipeline" | dismiss as inline |
| 2026-07-16 | queued | rule | [[dr-research-to-skill-gated-pipeline]] | "Injection-scan all external content at the write boundary" | extract via /extract-artifacts |

## Per-row details

### machine-readable-system-contract-with-wiring-rows::template::system-contract-wiring-row-schema

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[machine-readable-system-contract-with-wiring-rows]]
- **Source excerpt:**
  > "Each wiring row carries five fields: `tier` (**required** = do not install without a
  > satisfier, checked before any adaptation cost is paid; **optional** = install and
  > record the degradation), `capabilities` (IDs from a controlled wiring vocabulary...),
  > `purpose`, `degradation` (always names its prose fallback...), and `invariant` — the
  > property that must survive *any* adaptation..."
- **Codifier's reading:** The five-field row structure is a structural scaffold meant for rendering — a fillable YAML shape with fixed slots, not a narrative pattern. Fits the template form's "structural form with placeholder fields" criterion; the guide already renders it as a `{{VARIABLE}}` template in Section 9.
- **Suggested headline:** system-contract-wiring-row-schema
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### invariant-column-as-contract-field::rule::wiring-rows-must-declare-testable-invariant

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[invariant-column-as-contract-field]]
- **Source excerpt:**
  > "the adaptation plan [must] state, per row, 'how the row's `invariant` is preserved
  > under your mechanism. The invariant is the acceptance test — the mechanism may be
  > anything your platform offers; the invariant may not bend.' ... the workspace doc
  > audit (C15) checks the contract has an invariant per row; it is one of five
  > negative-tested violation classes."
- **Codifier's reading:** Imperative and machine-enforceable — "every wiring row carries an invariant; invariants never bend under adaptation" is audit-checkable (the source system negative-tests it). Fits the rule form's machine-enforceable directive criterion.
- **Suggested headline:** wiring-rows-must-declare-testable-invariant
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### harness-adaptation-protocol-graded-capability-intersection::skill::harness-adaptation-install-protocol

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[harness-adaptation-protocol-graded-capability-intersection]]
- **Source excerpt:**
  > "A seven-step protocol addressed to 'you, the agent on the target platform'...
  > (1) read the contract, (2) inventory your platform's provides, (3) compute the
  > intersection, (4) propose an adaptation plan — human gate, (5) execute and write an
  > install report, (6) verify triggering via cold-start echo + skill trigger evals,
  > (7) verify behavior via invariant probes + skill smokes."
- **Codifier's reading:** A complete procedure with input (repo + system contract), output (install report + verification evidence), step-by-step structure, human gates, and termination — the skill form's invocation-contract shape. Directly relevant to the engine's portable-governance-kernel install path.
- **Suggested headline:** harness-adaptation-install-protocol
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### wiring-canon-abstract-then-adapt-doc-structure::template::three-section-wiring-canon-doc-format

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[wiring-canon-abstract-then-adapt-doc-structure]]
- **Source excerpt:**
  > "each written platform-agnostically with three fixed sections — **Canon** (the
  > requirement), **Adapter-delegated** (per-platform decisions, including the named
  > fallback when a platform lacks the mechanism), and **Harness-specific examples**
  > (labeled illustrations from the current install, never requirements). The folder
  > opens with an agent router stating who may use it and when."
- **Codifier's reading:** A fixed three-section document skeleton meant to be instantiated per wiring concern — structural scaffold for rendering, the template form's core criterion. The router-guard header is part of the same scaffold.
- **Suggested headline:** three-section-wiring-canon-doc-format
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### dr-research-to-skill-gated-pipeline::skill::gap-aware-research-to-capability-pipeline

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[dr-research-to-skill-gated-pipeline]]
- **Source excerpt:**
  > "`/dr <topic>` is the context-hub system's build engine: web research in, installed
  > and hub-routed skill out, with every step bounded by countable rules and gated by
  > independent verifiers. Six phases: Phase 0 — Concept analysis... Phase 1 — Research
  > to saturation... Phase 2 — Skill creation + gates... Phase 3 — Persist + register...
  > Phase 4 — Cross-pollination... Phase 5 — Concept-tree update."
- **Codifier's reading:** Full six-phase procedure with invocation contract, countable termination criteria, and gates — unambiguously skill-shaped. Recommend dismiss-as-inline because the engine already has this pipeline's counterpart (`/research-loop` → `/identify-artifacts` → `/extract-artifacts`); the finding's value is the gap analysis in its implementation notes, which is design input for those existing skills rather than a new engine skill.
- **Suggested headline:** gap-aware-research-to-capability-pipeline
- **Recommendation:** dismiss as inline
- **Resolution:**

### dr-research-to-skill-gated-pipeline::rule::injection-scan-at-write-boundary

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[dr-research-to-skill-gated-pipeline]]
- **Source excerpt:**
  > "**Security boundary.** All researched/web content is data; the injection scan at the
  > write boundary is non-negotiable — nothing unscanned reaches the installed skill
  > tree."
- **Codifier's reading:** Imperative, machine-enforceable directive ("nothing unscanned reaches the tree") with a clear enforcement point (the write boundary). The finding's implementation notes flag it as "directly adoptable for engine KB intake today" — a distinct rule-shaped candidate co-occurring inside a skill-shaped finding.
- **Suggested headline:** injection-scan-at-write-boundary
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
