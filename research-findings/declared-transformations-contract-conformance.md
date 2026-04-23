---
name: "Declared-Transformations Contract with Conformance Tests"
summary: "Turn a social contract (\"we never change your data\") into a test-enforced property. Each data-handling component declares the set of transformations it applies via a typed class attribute (e.g., `declared_transformations: ClassVar[frozenset[str]]`). A conformance test suite verifies that the component's output is reproducible from source by applying *only* the declared transformations — any undeclared transformation raises `TransformationViolationError`. Replaces verbal 'verbatim' / 'lossless' promises with machine-verified invariants."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: specification-as-governance-fourth-enforcement-philosophy.md
    rel: extends
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A four-part pattern for making data-handling promises machine-verifiable rather than socially-enforced:

1. **Reserved transformation vocabulary.** The spec publishes a set of named transformations with stable semantics (e.g., `utf8_replace_invalid`, `newline_normalize`, `line_trim`, `whitespace_trim`, `spellcheck_user`, `synthesized_marker`). These are the legal atomic operations any component may apply.
2. **Per-component declaration.** Every component that transforms data declares its set via a typed class attribute: `declared_transformations: ClassVar[frozenset[str]] = frozenset({"utf8_replace_invalid", "whitespace_trim"})`. An empty set means byte-preserving; a non-empty set means "lossy in exactly these ways."
3. **Reference implementations.** The spec ships reference implementations of every reserved transformation. Conformance tests use these to replay transformations on source bytes.
4. **Conformance test suite as invariant enforcement.** A pytest mixin (e.g., `AbstractSourceAdapterContractSuite`) runs two tests:
   - Byte-preserving round-trip (for components declaring the empty set): reassembling chunks must equal source bytes exactly.
   - Declared-transformation round-trip: applying only the declared transformations in order to source bytes must reproduce the component's output. Any divergence raises `TransformationViolationError`.

The verbal promise ("we preserve your data") becomes a property checked by CI. The spec explicitly states: *"This replaces the MISSION.md promise of 'verbatim always' with a stronger one: every adapter publishes what it does to your data, and the conformance suite verifies it hasn't lied."*

## Why It Matters

Any claim the IL or MetaSystem makes about agent behavior — "agents only write to X," "extraction is lossless," "the pipeline preserves Y," "this skill is read-only" — has the same structural weakness: it's a social contract. Social contracts erode under iteration pressure, get misremembered across sessions, and don't alert anyone when violated. This pattern converts such claims into tested properties.

For MetaSystem specifically:

- **Agent write boundaries** (DD-30, DD-82) — "Researcher writes to Findings, Sources, Authorities only" is a social contract. A declared-writes test at the agent boundary could verify it.
- **KB integrity claims** — "findings have evidence pointers and source links" is asserted in the Researcher agent constitution. A conformance test on the KB could enforce it.
- **Skill contract invariants** — each SKILL.md declares preconditions, invariants, governance. Today these are prose. Converting to tested properties requires a vocabulary for what a skill may/must do.

Extends [[specification-as-governance-fourth-enforcement-philosophy]] (LangGraph's conformance-suite pattern + n8n's spec-driven-development pattern): that finding identifies conformance tests as a fourth enforcement philosophy; this finding adds the specific mechanism of *declared transformations* as a first-class part of the contract, plus the explicit framing of converting an existing verbal promise into a tested property.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. The pattern is formalized in `docs/rfcs/002-source-adapter-plugin-spec.md` as part of the Source Adapter Plugin specification. The RFC itself is a full 700+-line formal spec with `spec_version: 1.0` as a loadable-compatibility boundary. §1.4 enumerates reserved transformation names with semantics; §2.1 declares `declared_transformations` as a `ClassVar[frozenset[str]]` attribute adapters must populate; §7.2 and §7.3 define the two conformance tests; `TransformationViolationError` is the failure mode.

The RFC also tracks *existing* MemPalace code against the contract: `mempalace/miner.py` declares `{"utf8_replace_invalid", "whitespace_trim"}`; `mempalace/convo_miner.py + normalize.py` declare 12+ transformations. Both are "honest after this spec lands because both are fully declared." The contract retroactively audits what the existing code actually does.

Closely related to LangGraph's `libs/checkpoint-conformance/` and n8n's spec-driven-development skill (both documented in [[specification-as-governance-fourth-enforcement-philosophy]]) — three independent repos now exhibit the specification-as-governance pattern.

## Potential Alternatives

- **Prose-only contracts.** CLAUDE.md, MISSION.md, agent constitutions. Readable but unverified; erode across sessions.
- **Structural enforcement via tool allowlists.** Coarse-grained; says "cannot call X" but not "if you touch Y, it must result in Z."
- **Code-review discipline.** Humans verify adherence at PR review time. Works at small scale; doesn't scale to frequent contributions or automated agents.
- **Runtime assertions.** Pre/post conditions checked at runtime. Effective for hot-path properties; noisy for invariants that must hold across all inputs.

## Potential Improvements

- **Allow custom transformation names with provided reference implementations.** RFC 002 does this: third-party adapters may declare names not in the reserved set, but must provide a reference implementation at `mempalace.sources.transforms.<adapter_name>_<transform_name>`. This keeps the contract extensible.
- **Generator-based property testing.** Hypothesis-style property tests over generated inputs would stress-test adapters beyond the hand-crafted fixtures, finding corner cases the fixture author didn't imagine.
- **Composable declared transformations.** Combinators (A-then-B, A-and-B-interleaved) that let declarations compose cleanly rather than requiring fresh names for every combination.

## Potential Failure Modes

- **Reference-implementation drift.** If the conformance suite's reference implementation of a transformation diverges from adapter implementations over time (e.g., both fix different edge cases), the suite fails for reasons unrelated to adapter correctness.
- **Over-claiming byte-preservation.** An adapter declaring the empty set must actually be byte-preserving. A subtle newline conversion that slips in silently breaks every downstream consumer that relied on the byte-preservation claim. The test suite must have comprehensive fixtures.
- **Under-declaring.** An adapter that performs a transformation not in the reserved vocabulary and forgets to declare a custom name would either (a) fail the suite, or (b) silently pass if the transformation happens to reproduce under other declared operations. The second case is harder to detect.
- **Coverage gap.** Conformance tests check properties over a fixture; properties that depend on inputs not in the fixture go unverified. Real-world adapters will encounter inputs the fixture author didn't imagine.
- **Semantic vs byte correctness.** `newline_normalize` + `whitespace_trim` preserves the semantic content but not the bytes. A downstream consumer expecting byte-exact recovery from a "declared_lossy" source will be disappointed despite the spec working as designed.
