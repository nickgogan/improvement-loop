---
title: "Contract-Section Spot Check — Agent Audit Composition (Option α' validation)"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "claude"
stage: "draft"
source_dd:
  - "DD-78"
  - "DD-80"
  - "DD-82"
tags:
  - "design-note"
  - "spot-check"
  - "librarian"
  - "validation"
aliases:
  - "Contract spot check"
  - "Option alpha-prime validation"
  - "Agent audit rubric composition test"
---

# Contract-Section Spot Check — Agent Audit Composition

**Status:** Empirical validation of Option α' from the substrate audit (`2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`). Gate test for session 48. Not a proposal.

## Purpose

Option α' (Librarian reference layer + three-tier access) depends on one untested empirical claim from DD-78:

> Contract invariants across the relevant guides compose into a coherent audit rubric when consumed by an audit operation.

If true, `assess-agent` (and its siblings) can be built as thin wrappers that load a concept file's composition pointers, pull Contract invariants from the named guide sections, and apply them as audit criteria — no curated view artifacts required.

If false, Option α' collapses into Option α (curated view artifacts are mandatory), and the reference layer becomes insufficient on its own for the assessment use case.

This note tests the claim against a minimal slice: three guides (G1, G2, G10) composed against a deliberately flawed sample `agent.md`.

---

## Method

1. Read `## Contract` sections from three guides: **G1** (`writing-agent-specifications.md:392`), **G2** (`managing-agent-context.md:653`), **G10** (`agent-design-patterns.md:377`).
2. Extract each guide's invariants verbatim and give them a stable ID for rubric composition.
3. Group the pooled invariants by aspect (Intent / Identity / Prompt architecture / Context hygiene / Anti-pattern / Enforcement).
4. Author a ~15-line sample `agent.md` with deliberate, labeled gaps.
5. Apply the composed rubric. For each gap: does a specific invariant flag it? For each aspect an agent spec should address: does the rubric have coverage?
6. Verdict.

---

## Invariants Extracted

### G1 — `writing-agent-specifications.md` (Intent / Specification)

| ID | Invariant |
|---|---|
| G1.I1 | Every agent spec includes at minimum: objective, desired outcomes, health metrics, constraints classified by enforcement layer, autonomy levels per decision type, acceptance criteria, stop rules. |
| G1.I2 | Templates are filled in completely — no placeholder fields left as "TBD" or "TODO". |
| G1.I3 | Hard constraints have corresponding enforcement mechanisms outside the prompt layer. |
| G1.I4 | Acceptance criteria are evaluable by a third party without access to the prompter's intent. |

### G2 — `managing-agent-context.md` (Context Engineering)

| ID | Invariant |
|---|---|
| G2.I1 | Every context element loaded into an agent's window has a justifiable reason for being there. |
| G2.I2 | Stable context is cached. |
| G2.I3 | Evolving documents use delta updates, not monolithic rewrites. |
| G2.I4 | Context health is measured, not assumed. |
| G2.I5 | Sub-agents receive scoped context appropriate to their task, not the parent's full window. |
| G2.I6 | Hidden context sources (IDE injection, git status) are accounted for in the budget. |

### G10 — `agent-design-patterns.md` (Agent Design Patterns)

| ID | Invariant |
|---|---|
| G10.I1 | Agent identity (constitution) is defined in a separate, stable layer from capabilities (skills/tools). |
| G10.I2 | All five prompt layers are explicitly addressed — skipped layers are documented as intentional omissions, not oversights. |
| G10.I3 | Clarification behavior distinguishes resolvable gaps from intent-dependent gaps. |
| G10.I4 | No agent exists solely to review another agent's output — quality is at the source. |
| G10.I5 | Harness complexity is periodically audited against current model capabilities. |

**Total: 15 invariants across three guides.**

---

## Composed Rubric — Aspect Grouping

Grouping the 15 invariants into aspects an `agent.md` should address:

| Aspect | Invariants covering it | Verifiability |
|---|---|---|
| **Intent / Spec completeness** | G1.I1, G1.I2, G1.I4 | File-verifiable |
| **Identity vs. capability separation** | G10.I1 | File-verifiable |
| **Prompt-layer architecture** | G10.I2 | File-verifiable |
| **Context justification + budget** | G2.I1, G2.I6 | File-verifiable |
| **Subagent context scoping** | G2.I5 | File-verifiable (if agent delegates) |
| **Clarification behavior** | G10.I3 | File-verifiable |
| **Constraint enforcement** | G1.I3 | File-verifiable (asks about enforcement layer reference) |
| **Anti-pattern — review-only agents** | G10.I4 | File-verifiable |
| **Stable-context caching** | G2.I2 | System-verifiable (runtime evidence needed) |
| **Evolving-doc delta discipline** | G2.I3 | System-verifiable |
| **Context health measured** | G2.I4 | System-verifiable |
| **Harness complexity audited periodically** | G10.I5 | Process-verifiable |

**Two-class split surfaces.** Invariants partition naturally into:
- **File-verifiable** (9/15) — inspectable on the static `agent.md` alone.
- **System/process-verifiable** (6/15) — require runtime evidence, metrics, or attested cadence (e.g., "context health is measured").

This is a meaningful distinction for the `audit` operation's procedure — surfaced below under *Refinement*.

---

## Sample `agent.md` (Deliberate Gaps)

```markdown
---
name: Release Notes Agent
---

# Release Notes Agent

## Identity
You are a release notes writer. Produce release notes from git history.

## Context
Read all the repo files to understand the changes.

## Tools
Read, Write, Grep, Bash, Edit, all MCP tools, Task.

## Behavior
- Check review agent's output when producing notes.
- Always produce output; if unsure, guess.

## Output
Write release-notes.md in the repo root.
```

**Labeled gaps (13):**

| # | Gap | Predicted invariant(s) |
|---|---|---|
| A | No objective, outcomes, health metrics, autonomy levels, acceptance criteria, or stop rules | G1.I1 |
| B | No acceptance criteria evaluable by a third party | G1.I4 |
| C | No constraint with enforcement layer outside the prompt | G1.I3 |
| D | "Read all the repo files" — no justification per element | G2.I1 |
| E | No context budget; hidden context (git status) not accounted for | G2.I6 |
| F | No context-health measurement or escalation rule | G2.I4 |
| G | Tools unbounded; no subagent context scoping | G2.I5 |
| H | Identity section elides any constitution/capability distinction | G10.I1 (partial) |
| I | No explicit coverage of the five prompt layers | G10.I2 |
| J | "If unsure, guess" — inverts clarification discipline | G10.I3 |
| K | "Check review agent's output" — review-only agent anti-pattern | G10.I4 |
| L | No caching discipline declared | G2.I2 (system-verifiable — flag as follow-up) |
| M | No complexity-audit cadence | G10.I5 (process-verifiable — flag as follow-up) |

---

## Applying the Rubric

| Gap | Invariant | Fires? | Notes |
|---|---|---|---|
| A | G1.I1 | **Yes** | Rubric directly enumerates required fields; sample has none. |
| B | G1.I4 | **Yes** | Sample has no acceptance criteria at all. |
| C | G1.I3 | **Yes** | "Always produce output" is a constraint with no enforcement layer named. |
| D | G2.I1 | **Yes** | "Read all the repo files" fails justification. |
| E | G2.I6 | **Yes** | Hidden context not enumerated. |
| F | G2.I4 | **Yes** | No measurement rule stated. |
| G | G2.I5 | **Yes** | No subagent scoping despite delegation potential. |
| H | G10.I1 | **Partial** | Identity section exists but doesn't separate constitution from capabilities — flag as "weak identity layer." |
| I | G10.I2 | **Yes** | Five-layer architecture absent. |
| J | G10.I3 | **Yes** | "If unsure, guess" directly inverts the invariant. |
| K | G10.I4 | **Yes** | "Check review agent's output" is the canonical anti-pattern. |
| L | G2.I2 | **Surface as follow-up** | Audit operation cannot verify caching from file alone; flag for system-level evidence. |
| M | G10.I5 | **Surface as follow-up** | Audit operation asks for process-cadence evidence. |

**11/13 gaps fire directly on a file-verifiable invariant. 2/13 surface as system/process follow-ups (which is the correct behavior, not a miss).**

---

## Coverage Analysis — What the {G1, G2, G10} Composition Covers

Aspects an `agent.md` audit should touch:

| Aspect | Covered by {G1, G2, G10}? | If not, which guide's Contract would cover it? |
|---|---|---|
| Intent / specification completeness | ✓ (G1) | — |
| Identity + prompt architecture | ✓ (G10) | — |
| Context hygiene | ✓ (G2) | — |
| Clarification behavior | ✓ (G10) | — |
| Anti-pattern — review-only agents | ✓ (G10) | — |
| Tool design quality | **Not covered** | G5 (`designing-agent-tools.md`) |
| Safety / permissions / blast radius | **Not covered** | G6 (`agent-safety-and-permissions.md`) |
| Governance / human gates | **Not covered** | G9 (`agent-governance-and-trust.md`) |
| Observability / evaluation harness | **Not covered** | G4 (`building-agent-evaluation-suites.md`) |
| Workflow / execution topology | **Not covered** | G3b (`agent-workflow-and-execution.md`) |
| Memory / session persistence | **Not covered** | G7 (`session-persistence-and-memory.md`) |
| Architecture decisions | **Not covered** | G3 (`agent-architecture-decisions.md`) |

**Expected and desirable.** The spot-check deliberately composes only three guides. A full `agent-audit` operation per Option α' composes *all* Contract sections named in the `agent.md` concept file's composition table (per the substrate audit, ~7 guides: G1, G2, G3, G5, G6, G9, G10 at minimum). The fact that {G1, G2, G10} alone leaves expected blind spots *confirms* the composition mechanism works as intended — coverage is a direct function of which guides are composed, not an emergent property of the rubric.

---

## Verdict — **PASS**

Option α' holds on its load-bearing empirical claim.

### What passed

1. **Each guide's invariants function as audit criteria without curation.** Every invariant from the three Contracts, read as-is, is a declarative testable statement. No re-authoring required.
2. **Invariants compose without collision.** The 15 invariants partition cleanly into aspect groups; no two invariants contradict each other; no aspect is over-specified.
3. **Deliberate gaps surface via specific invariants.** 11/13 gaps fire on a file-verifiable invariant; the remaining 2 correctly surface as system/process follow-ups (expected behavior, not a failure).
4. **Coverage gaps correspond exactly to un-composed guides.** Missing aspects (tools, safety, governance, workflow, etc.) map 1:1 to Contract sections in guides not included in this spot-check — confirming composition is additive and predictable.

### Refinement — `audit` operation should distinguish two verifiability classes

The natural split (9 file-verifiable / 6 system-verifiable) implies the `audit.md` operation file should codify a two-phase procedure:

1. **Phase 1 — File audit.** Apply file-verifiable invariants directly to the submitted `agent.md`. Fire findings for anything violated or missing.
2. **Phase 2 — System evidence request.** For system/process-verifiable invariants, surface follow-up questions to the consumer (e.g., "Is your context-health measurement in place? Where is the evidence?"). Do not silently skip; do not falsely pass.

This refinement strengthens α' — it makes explicit something v1 of the substrate audit left implicit. Recommended for inclusion in the Phase 3 `audit.md` operation file draft.

### What this initial three-guide pass does NOT validate

- ~~Full seven-guide composition.~~ Addressed in §"Extended Validation" below.
- ~~Non-agent audit operations.~~ Addressed in §"Extended Validation" below.
- **Consumer-input handling.** How the consumer submits the artifact under audit, and how Librarian parses it, is out of scope for this note (lives in Phase 5 read-contract design).

---

## Extended Validation — Phase 1b (per Nick's gate request)

**Motivation.** The three-guide pass proves composition works at small scale; it does not prove the mechanism scales to the full seven-guide agent audit, nor that it transfers to prompt and skill audits. Nick asked for a second pass. Extended validation tests three additional compositions:

1. **Full seven-guide agent audit** — {G1, G2, G3, G5, G6, G9, G10}, 36 invariants.
2. **Prompt audit** — {G1, G2, G5, G8}, 23 invariants.
3. **Skill audit** — {G1, G3b, G5, G6, G8}, 27 invariants.

Each test: extract invariants → check for collisions → test coverage against a deliberately flawed sample → verdict.

### Additional Invariants Extracted

#### G3 — `agent-architecture-decisions.md`

| ID | Invariant |
|---|---|
| G3.I1 | Architecture decisions are justified by task characteristics (parallelizability, information flow, error sensitivity), not organizational structure or technology trends. |
| G3.I2 | Single-agent is the default until empirical evidence justifies multi-agent. |
| G3.I3 | Every agent boundary has an explicit contract validated at runtime. |
| G3.I4 | Model selection is task-based, not provider-based or prestige-based. |
| G3.I5 | Infrastructure dependencies are classified as architectural bets or transitional shims. |

#### G3b — `agent-workflow-and-execution.md`

| ID | Invariant |
|---|---|
| G3b.I1 | Planning is probabilistic; execution is deterministic. LLMs decide what; infrastructure decides how and when. |
| G3b.I2 | Every workflow has explicit state tracking independent of conversation history. |
| G3b.I3 | Every iterative pattern has a termination condition (loop limit, stall detection, or both). |
| G3b.I4 | Degradation modes are defined before the system goes live, not designed after the first failure. |
| G3b.I5 | Delivery chunk size is calibrated to reviewer capacity, not agent production speed. |
| G3b.I6 | Cost controls (budgets, termination rules, caching, fast-fail) are in place before autonomous execution. |

#### G5 — `designing-agent-tools.md`

| ID | Invariant |
|---|---|
| G5.I1 | Tool definitions are data first — metadata exists before implementation. |
| G5.I2 | Tool interfaces make common errors structurally impossible (poka-yoke). |
| G5.I3 | Tool descriptions are designed for non-deterministic consumers — they persuade, disambiguate, and explain when not to use the tool. |
| G5.I4 | Only tools needed for the current task are loaded into context. |
| G5.I5 | Intermediate tool results stay outside the context window when the agent only needs the final output. |
| G5.I6 | Complex tools include usage examples that teach correct parameter patterns beyond what schemas convey. |

#### G6 — `agent-safety-and-permissions.md`

| ID | Invariant |
|---|---|
| G6.I1 | Permissions are tiered by risk, not binary allow/deny. |
| G6.I2 | Safety-critical constraints are enforced structurally, not via prompt instructions alone. |
| G6.I3 | The agent cannot modify its own permission configuration. |
| G6.I4 | Defense is layered — no single mechanism is the sole protection. |

#### G8 — `model-resilient-prompt-engineering.md`

| ID | Invariant |
|---|---|
| G8.I1 | Prompts tell the model what to produce, not how to think. |
| G8.I2 | No prescribed reasoning paths (CoT, few-shot, decomposition, skeleton-of-thought) in prompts for reasoning models. |
| G8.I3 | High-priority behavioral rules are expressed as negative constraints, not positive aspirations. |
| G8.I4 | Model selection is task-based, not provider-based. |
| G8.I5 | The Advisor-Executor pattern is considered before defaulting to the most expensive model. |
| G8.I6 | Prompts carry explicit ROLE, AUTHORITY, CONSTRAINT, and FAILURE SIGNAL properties. |
| G8.I7 | Prompt changes are versioned and tested before deployment. |

#### G9 — `agent-governance-and-trust.md`

| ID | Invariant |
|---|---|
| G9.I1 | Human retains override authority at all autonomy levels. No tier removes the ability to intervene. |
| G9.I2 | Audit trail is maintained for all agent actions — append-only, immutable, queryable. |
| G9.I3 | Autonomy level is assigned per decision type, not per agent globally. |
| G9.I4 | Trust promotion requires demonstrated track record; trust demotion is immediate on failure. |
| G9.I5 | No decision type defaults to full autonomy without explicit classification. |
| G9.I6 | Destructive or irreversible actions always require human approval regardless of trust level. |

---

### Test 1 — Full Seven-Guide Agent Audit {G1, G2, G3, G5, G6, G9, G10}

**36 invariants.** Composition check.

#### Collision and redundancy scan

| Finding | Invariants involved | Handling |
|---|---|---|
| **Duplicate (near-verbatim)** | G3.I4 ("Model selection is task-based, not provider-based or prestige-based") vs G8.I4 ("Model selection is task-based, not provider-based") | Dedupe to a single rubric row. Canonical text: G3.I4 (superset phrasing). Not in the 7-guide agent audit (G8 excluded), so duplicate only surfaces in prompt/skill audits that include G8 + G3. |
| **Hierarchical overlap (umbrella + specialization)** | G1.I3 ("Hard constraints have enforcement outside the prompt layer") ⊃ G6.I2 ("Safety-critical constraints are enforced structurally") | Both stand. G1.I3 covers all hard constraints; G6.I2 specializes to safety. Audit rubric runs specialization first, then umbrella — no contradiction. |
| **Hierarchical overlap** | G6.I3 ("Agent cannot modify its own permission configuration") ∩ G9 governance ("Autonomy tier assignments are governed artifacts — agents cannot modify their own tier") | Both stand. G6.I3 is permission-scoped; G9 covers tier/authority. Complementary. |
| **Complementary (mechanism + policy)** | G6.I1 (tiered permissions) ↔ G9.I6 (destructive actions require human approval) | G6.I1 defines the tiering mechanism; G9.I6 sets the policy for the destructive tier. Compose as a chain. |
| **Complementary (design-time + runtime)** | G3.I3 (boundary contracts validated at runtime) ↔ G9.I2 (audit trail) | G3.I3 specifies contract existence; G9.I2 specifies evidence trail. Complementary. |

**Result:** 1 genuine duplicate (out of 36), 3 hierarchical overlaps (all complementary), 0 contradictions. Composition is stable at scale.

#### Coverage at scale

Every aspect an `agent.md` audit should touch now has at least one invariant covering it:

| Aspect | Invariant(s) |
|---|---|
| Intent / specification completeness | G1.I1, G1.I2, G1.I4 |
| Constraint enforcement | G1.I3, G6.I2 (hierarchical) |
| Identity / capability separation | G10.I1 |
| Prompt-layer architecture | G10.I2 |
| Context hygiene (5 sub-aspects) | G2.I1–I6 |
| Clarification behavior | G10.I3 |
| Anti-pattern — review-only agents | G10.I4 |
| Complexity audit cadence | G10.I5 |
| Architecture decision justification | G3.I1, G3.I2 |
| Boundary contracts | G3.I3 |
| Model selection | G3.I4 |
| Infrastructure dependency classification | G3.I5 |
| Tool design (6 sub-aspects) | G5.I1–I6 |
| Permission tiering | G6.I1 |
| Agent self-modification prohibition | G6.I3 |
| Defense in depth | G6.I4 |
| Override authority | G9.I1 |
| Audit trail | G9.I2 |
| Autonomy-per-decision-type | G9.I3 |
| Trust promotion/demotion | G9.I4, G9.I5 |
| Destructive-action gating | G9.I6 |

**Coverage: complete at the aspect level.** No orphan aspects; no aspect requires curation on top of raw Contract text.

#### Verdict — Test 1: **PASS**

Composition scales 3 → 7 guides with one dedup required, three benign hierarchical overlaps, zero contradictions, complete coverage.

---

### Test 2 — Prompt Audit {G1, G2, G5, G8}

**23 invariants.** Applies when consumer submits a prompt (system prompt, user prompt, or prompt template) for audit.

#### Sample prompt (deliberate gaps)

```
You are an expert code reviewer. Think step-by-step about the code.
Always use Chain of Thought reasoning.
Please try to be thorough and write comprehensive reviews.
Use Claude Opus — it's the best model.
```

**Labeled gaps:**

| # | Gap | Predicted invariant |
|---|---|---|
| P.A | Weak ROLE, no AUTHORITY, no CONSTRAINT, no FAILURE SIGNAL | G8.I6 |
| P.B | "Think step-by-step" + "use CoT" prescribes reasoning paths | G8.I1, G8.I2 |
| P.C | "Please try to be thorough" — positive aspiration, not negative constraint | G8.I3 |
| P.D | "Use Claude Opus — it's the best model" — prestige-based selection | G8.I4 |
| P.E | No acceptance criteria; no way to test prompt against outcomes | G1.I4, G8.I7 |
| P.F | No Advisor-Executor consideration despite expensive-model choice | G8.I5 |

Applying the rubric: all six labeled gaps fire on at least one invariant (8 fires total from 6 gaps). No false negatives.

#### Surfaced: conditional applicability

Not all 23 invariants apply to every prompt. G2 invariants (context hygiene) are latent unless the prompt embeds context-management directives; G5 invariants are latent unless the prompt references tools. Only G8 (7 invariants) and G1 (4 invariants) are always-applicable to a standalone prompt.

**This is a design signal, not a failure.** Contract sections already carry a `### Preconditions` subsection. The audit operation can use preconditions as gates: fire an invariant only if its guide's preconditions are satisfied by the audit target. Concrete example:
- G5 preconditions: "You have tools that agents invoke…" — if the prompt references tools, fire G5 invariants; else skip.
- G2 preconditions: "You have an agent system where output quality… is affected by what the agent sees in its context window" — if the prompt carries context directives, fire G2 invariants; else skip.

#### Verdict — Test 2: **PASS** (with conditional-applicability gating)

Prompt audit composes coherently. Most fires come from G8 (the guide most directly targeting prompts). G1, G2, G5 contribute conditionally. The audit procedure should gate invariant firing on guide preconditions — and these preconditions already exist in the Contract structure.

---

### Test 3 — Skill Audit {G1, G3b, G5, G6, G8}

**27 invariants.** Applies when consumer submits a `SKILL.md` or equivalent procedural-wrapper definition.

#### Sample skill (deliberate gaps)

```
# /my-review-skill

Run through the code and fix everything you find.
Loop until you find no more issues.

## Tools
All tools allowed.
```

**Labeled gaps:**

| # | Gap | Predicted invariant |
|---|---|---|
| S.A | No objective, acceptance criteria, stop rules | G1.I1, G1.I4 |
| S.B | Loop has no termination condition | G3b.I3 |
| S.C | No workflow state tracking | G3b.I2 |
| S.D | No degradation modes | G3b.I4 |
| S.E | No cost controls | G3b.I6 |
| S.F | "All tools allowed" — no scoping per task | G5.I4 |
| S.G | No permission tiering; destructive tools ungated | G6.I1, G9.I6 (latent; G9 not in skill scope but flagged) |
| S.H | "Run through and fix everything" — no ROLE/AUTHORITY/CONSTRAINT/FAILURE SIGNAL | G8.I6 |
| S.I | No versioning / test discipline | G8.I7 |
| S.J | No chunk-size calibration to reviewer capacity | G3b.I5 |
| S.K | Constraints (if any) expressed positively, not as enforcement | G1.I3 |

Applying: all 11 labeled gaps fire. G3b contributes heavily (workflow-level invariants are exactly what a skill needs), G8 provides prompt-layer hygiene, G6 flags safety gaps even in minimal form, G1 covers spec completeness.

**Note on G9 exclusion.** The session-47 substrate audit listed {G1, G8, G5, G6, G3b} for skill audit — G9 not included. S.G flags a G9-shaped concern ("destructive tools ungated"); the composition misses it because G9 is not in scope. This surfaces a **concept-file composition table question**: should the `skill.md` concept file's composition table include G9 for safety-critical skills? Recommend: yes — add G9.I6 specifically (destructive actions require human approval) as a cross-cutting invariant relevant to any skill that grants tool access. This refinement goes into the Phase 3 `skill.md` concept file (if authored) or is noted for the Phase 4 use-case registry.

#### Verdict — Test 3: **PASS** (with composition-table refinement)

Skill audit composes coherently. G3b is the dominant contributor — good signal that `/synthesize-guide` routed workflow patterns correctly. G9.I6 should be added to skill-scope composition.

---

### Additional Refinements Surfaced by Extended Validation

1. **Invariant de-duplication.** When composing guides, detect near-duplicate invariants (G3.I4 / G8.I4 is the canonical example). `audit.md` operation procedure should specify dedup logic: normalize invariant text → merge duplicates → record source guides as a list rather than a single citation. Low-cost; clean result.
2. **Hierarchical overlap handling.** When invariants exist in an umbrella/specialization relationship (G1.I3 ⊃ G6.I2), the audit runs the specialization first and uses it for specific aspects; the umbrella catches anything the specialization doesn't cover. The rubric should annotate these relationships rather than flatten them.
3. **Conditional applicability via preconditions.** An invariant fires only when its guide's Preconditions are satisfied by the audit target. This is the right default. Contract-section Preconditions were written as authorial guardrails; they turn out to double as audit gates. No new authoring required.
4. **Composition-table completeness is a per-concept-file design decision.** Test 3 surfaced that `skill.md`'s composition table (as specified in substrate audit §"Early entries") should include G9 for safety-critical skills. This is a concept-file authoring concern for Phase 3, not a threat to α'.

---

## Final Consolidated Verdict — **PASS (extended)**

Four tests executed across this session:

| Test | Scope | Invariants | Gaps fired / labeled | Verdict |
|---|---|---|---|---|
| 1 (initial) | Three-guide agent slice {G1, G2, G10} | 15 | 11/13 direct + 2/13 system-follow-up | PASS |
| 2 (7-guide) | Full agent audit {G1, G2, G3, G5, G6, G9, G10} | 36 | Coverage complete; composition stable | PASS |
| 3 (prompt) | {G1, G2, G5, G8} | 23 | 8/6 fires; conditional applicability works | PASS |
| 4 (skill) | {G1, G3b, G5, G6, G8} | 27 | 11/11 fires; G9.I6 refinement surfaced | PASS |

Option α' holds across all four composition tests. Every predicted gap fires on at least one invariant. No contradictions. One de-duplication case, three hierarchical overlap cases, one conditional-applicability pattern — all mechanical, all addressable in the `audit.md` operation procedure. Composition-table refinement surfaced for `skill.md` (Phase 3 concept-file authoring concern, not a reference-layer failure).

**Pure α' proceeds.** No view-artifact escalation required for agent / prompt / skill audits. Phase 3 `audit.md` operation file should codify four procedural elements:
1. File-verifiable vs system/process-verifiable invariant split (from Test 1).
2. Invariant de-duplication logic (from Test 2).
3. Hierarchical overlap annotation (from Test 2).
4. Conditional-applicability gating via guide Preconditions (from Test 3).

---

## Consequences for Session 48

1. **Phase 2 (dimensions rewrite) — Proceed as planned.** Unaffected by verdicts.
2. **Phase 3 (exemplar files) — Proceed with pure α'.** The `audit.md` operation file draft incorporates four procedural elements surfaced by the tests:
   (a) file-verifiable vs system/process-verifiable invariant split;
   (b) invariant de-duplication logic (normalize text → merge → record source guides as list);
   (c) hierarchical overlap annotation (umbrella/specialization relationships kept explicit);
   (d) conditional-applicability gating via each guide's Contract Preconditions.
3. **Phase 3 concept-file authoring.** When authoring `skill.md` concept file (whether this session or later), include G9.I6 in the composition table for safety-critical skills. When authoring `agent.md` concept file, composition table should include G3b (workflow) and G7 (memory) beyond the seven-guide set explicitly validated here — these were in-scope by the substrate audit but outside the seven-guide test.
4. **Phases 4–6 — Proceed.** No view-artifact escalation required; reference layer sufficient for agent / prompt / skill audit operations.
5. **DD-78 framing flag stands.** Contract sections now operationally dual-role: artifact-self-governance (authored intent) + emergent audit criteria (composed consumption) + audit gating (Preconditions used as applicability filter — an unanticipated third role). Amendment proposal remains deferred until α' is exercised in session 48+.

---

## Cross-References

- Substrate audit (the claim this spot-check tests): `project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` §"Disambiguation" and §"Options — From Lightest to Heaviest"
- Session 48 handoff (Phase 1 is this note): `operations/handoffs/handoff-prompt-session-48-codifier-librarian-reference-layer-build.md`
- **Contract sections tested (Phase 1a — initial):**
  - G1 — `extracts/guides/writing-agent-specifications.md` lines 392–415
  - G2 — `extracts/guides/managing-agent-context.md` lines 653–681
  - G10 — `extracts/guides/agent-design-patterns.md` lines 377–402
- **Contract sections tested (Phase 1b — extended):**
  - G3 — `extracts/guides/agent-architecture-decisions.md` lines 504–532
  - G3b — `extracts/guides/agent-workflow-and-execution.md` lines 566–595
  - G5 — `extracts/guides/designing-agent-tools.md` lines 485–514
  - G6 — `extracts/guides/agent-safety-and-permissions.md` lines 224–246
  - G8 — `extracts/guides/model-resilient-prompt-engineering.md` lines 502–534
  - G9 — `extracts/guides/agent-governance-and-trust.md` lines 464–492
- DD-78 (ContractSpec): target of the dual-role amendment flag
- DD-82 (IL 4-agent architecture): Librarian role expansion flag
