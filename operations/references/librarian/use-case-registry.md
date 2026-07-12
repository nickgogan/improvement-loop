---
title: "Librarian Use-Case Registry — (Concept, Operation) Decomposition"
type: "operational-reference"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-07-12"
author: "claude"
stage: "draft"
source_dd:
  - "DD-77"
  - "DD-78"
  - "DD-80"
  - "DD-81"
  - "DD-82"
  - "DD-86"
tags:
  - "design-note"
  - "librarian"
  - "use-case-registry"
  - "reference-layer"
aliases:
  - "Use case registry"
  - "Librarian use cases"
  - "Concept-operation map"
---

# Librarian Use-Case Registry — (Concept, Operation) Decomposition

> **Re-homed 2026-07-12** (substrate-audit gate G6): authored as a design note but live — ~14 concept docs cite UC anchors here, and `librarian/_index.md` names the registry-update process as the prioritization protocol for future authoring. Now lives in the reference layer it serves, per the DD-112 home rule.

**Status:** Design note. Phase 4 of the session-49 plan. Produces the authoring backlog that drives concept-file and operation-file prioritization. Nick gates any DD filing.

## Purpose

The substrate audit (`2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` §"Librarian Use Case Categories") established that consumer queries decompose into `verb + noun(s)` — operations over concepts. The Librarian reference layer (session 48 exemplars: `harness.md`, `second-brain.md`, `audit.md`) implements that decomposition. This note canonicalizes the session-46 use-case draft under the new decomposition: one row per use case, keyed by a concrete consumer query, mapped to the concept file(s) and operation file that would serve it.

The registry is not a tracking backlog of Librarian calls. It is the **evidence base for which concept and operation files to author next** — each unresolved pointer flags an authoring task.

## Methodology

- **9 categories** retained from the substrate audit (design advice, concrete deliverables, assessment, diagnosis, decision support, explanation, currency, meta/KB, planning).
- **35 use cases** expanded from the audit's example queries. Each query is a realistic consumer utterance; ambiguity is intentional where it tests the Librarian's variant-selection heuristics.
- Each row fixes seven fields (schema below). Where a concept file or operation file does not yet exist, the row flags the gap — the union of those gaps is the authoring backlog.
- Frequency weights (core 80% / long tail) are estimates based on which deliverables Nick named highest-priority (assess-*) and which categories carry the most consumer-value density per query. Calibration is expected — these weights are initial plausible defaults, not measurements.

### Row schema

| Field | Meaning |
|---|---|
| `ID` | Stable identifier `UC-<category>.<n>`. |
| `Query shape` | Verb + noun pattern the query follows. |
| `Example` | A concrete query a consumer might submit. |
| `Concept file(s)` | Which concept file(s) the Librarian loads. `*` = no specific noun; meta/coverage query. |
| `Operation file` | Which operation file drives the procedure. |
| `Tier` | Substrate tier(s) the composition reads. 1 = guides (default); 2 = patterns + findings graph; 3 = watched-library repos. |
| `Deliverable shape` | What the Librarian returns (rubric, prose, table, pointer, scaffold, etc.). |
| `Weight` | `core` (~80% of traffic combined) or `long-tail` (~20%). |

Two gap flags per row:
- **`Needs concept?`** — concept file does not yet exist (or the needed variant isn't authored). Blank = satisfied by existing or planned concept file.
- **`Needs op?`** — operation file does not yet exist. Blank = satisfied by existing or planned operation file.

---

## The 35 Use Cases

### Category 1 — Design advice (5)

Consumer wants step-by-step guidance indexed by what they're building.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-1.1 | design, `<artifact>` + aspect | "How should I design my agent's context files?" | `agent.md` | `design.md` ✓ | 1 | Step-list tied to G2 sections | core | `agent.md` | — |
| UC-1.2 | design, `<artifact>` (no aspect) | "How should I design my agent?" | `agent.md` | `design.md` ✓ | 1 (cross-guide thread) | Full specify→build→secure thread | core | `agent.md` | — |
| UC-1.3 | design, tool-aspect of `<artifact>` | "How should I design the tool registry for my agent?" | `agent.md` (+ aspect pointer) | `design.md` ✓ | 1 | G5 step-list with anchored subsections | core | `agent.md` | — |
| UC-1.4 | design, `<concept>` + variant | "How should I design a hybrid second brain my agent curates?" | `second-brain.md` ✓ (variant C) | `design.md` ✓ | 1+2 | G9+G7 thread + Agentic Systems Tier-2 patterns | long-tail | — | — |
| UC-1.5 | design, `<concept>` (variant-ambiguous) | "What should my agent's memory architecture look like?" | `memory.md` ✓ | `design.md` ✓ | 1+2 | Variant-selection + G7 step-list + Tier-2 debate surface | core | — | — |

### Category 2 — Concrete deliverables (4)

Consumer wants ready-to-copy scaffold or fetch a single artifact by name.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-2.1 | fetch-template, `<name>` | "Give me a template for a context budget worksheet." | `context-rot.md` ✓ (cross-ref to G2) | `fetch.md` ✓ | 1 | Anchor-lifted template body | long-tail | — | — |
| UC-2.2 | catalog, all-of-kind | "Show me all available templates." | `*` (meta) | `fetch.md` ✓ (catalog sub-op) | 1 (manifest) | Flat index of `guide.md#anchor` + kind | long-tail | — | — |
| UC-2.3 | fetch-rule, `<rule-slug>` | "Give me the programmatic-snippet-extraction rule to drop into my repo." | `prompt.md` ✓ (cross-ref) | `fetch.md` ✓ | 1 | Anchor-lifted rule section with deploy manifest pointer | long-tail | — | — |
| UC-2.4 | scaffold, `<artifact>` variant | "Give me an agent.md scaffold for a code-reviewer agent." | `agent.md` | `fetch.md` ✓ (scaffold sub-op) | 1 | Filled G1 template shell with variant-appropriate defaults | long-tail | `agent.md` | — |

### Category 3 — Assessment (6) *— highest priority*

Consumer submits an artifact; wants Contract-derived rubric applied.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-3.1 | audit, `agent.md` | "Audit my agent.md." | `agent.md` | `audit.md` ✓ | 1 | 7-guide rubric applied → Findings + Follow-ups tables | **core** | `agent.md` | — |
| UC-3.2 | audit, prompt | "Audit my system prompt." | `prompt.md` | `audit.md` ✓ | 1 | 4-guide rubric applied | **core** | `prompt.md` | — |
| UC-3.3 | audit, skill | "Audit my SKILL.md." | `skill.md` | `audit.md` ✓ | 1 | 5-guide rubric applied (with G9.I6 gate for safety-critical) | **core** | `skill.md` | — |
| UC-3.4 | audit, harness config | "Audit my harness configuration (`.claude/settings.json`, hooks, permissions)." | `harness.md` ✓ | `audit.md` ✓ | 1 (cross-guide thread) | Cross-guide aspect-sweep report | long-tail | — | — |
| UC-3.5 | audit, second-brain design | "Audit my AI-managed vault design for governance gaps." | `second-brain.md` ✓ (variant C) | `audit.md` ✓ | 1+2 | G9+G7 rubric + Agentic Systems Tier-2 cross-check | long-tail | — | — |
| UC-3.6 | audit, agentic-system | "Check my daily-brief agent system for HITL coverage." | `agentic-systems.md` ✓ | `audit.md` ✓ | 1+2 | G9 rubric + Agentic Systems Tier-2 patterns | long-tail | — | — |

### Category 4 — Diagnosis (5)

Consumer reports a symptom; wants symptom → likely cause → recovery.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-4.1 | diagnose, symptom → cause | "My agent keeps losing track of constraints mid-session." | `context-rot.md` ✓ | `diagnose.md` ✓ | 1+2 | Cause hypothesis + G2 Pitfalls pointers + Tier-2 attention-budget pattern | core | — | — |
| UC-4.2 | diagnose, tool-use symptom | "My agent's tool calls are erratic — wrong args, wrong sequencing." | `agent.md` (tool aspect) | `diagnose.md` ✓ | 1 | G5+G8 Pitfalls cross-read + findings on tool-call reliability | core | `agent.md` | — |
| UC-4.3 | diagnose, memory symptom | "My agent forgets facts across sessions even though I wrote them to memory." | `memory.md` ✓ | `diagnose.md` ✓ | 1+2 | G7 Pitfalls + Tier-2 write-gate + retrieval patterns | core | — | — |
| UC-4.4 | diagnose, degradation pattern | "My agent's output quality drops after ~50 turns." | `context-rot.md` ✓ | `diagnose.md` ✓ | 1+2 | Attention-budget hypothesis + proactive-compaction pattern + G2 Pitfalls | long-tail | — | — |
| UC-4.5 | diagnose, skill-loading symptom | "My skill isn't being triggered when it should be." | `skill.md` ✓ | `diagnose.md` ✓ | 1 | G3b + G8 cross-read on SKILL.md description quality + frontmatter pitfalls | long-tail | — | — |

### Category 5 — Decision support (4)

Consumer weighing two or more options; wants tradeoff table with authoritative citations.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-5.1 | decide, architecture A vs B | "Should I build a single agent or a multi-agent system for this workflow?" | `agent.md` | `decide.md` ✓ | 1 | G3 tradeoff section + `autonomy-gradient-not-binary-delegation` pointer | long-tail | `agent.md` | — |
| UC-5.2 | decide, design-debate | "MongoDB single-store vs. triple-storage memory — which for my agent?" | `memory.md` ✓ | `decide.md` ✓ | 2 | `contradicts`-link surfaced + evidence tables from both patterns | long-tail | — | — |
| UC-5.3 | decide, harness A vs B | "Claude Code or Cursor for an agentic coding workflow with my own skills?" | `harness.md` ✓ | `decide.md` ✓ | 2+3 | Cross-guide thread aspects × harness capabilities; Tier-3 comparison pointers | long-tail | — | — |
| UC-5.4 | decide, model A vs B | "Opus 4.7 or Sonnet 4.6 for a background review agent?" | `agent.md` (model aspect) | `decide.md` ✓ | 1 | G3.I4 / G8.I4 merged invariant + cost/latency/capability table | long-tail | `agent.md` | — |

### Category 6 — Explanation (3)

Consumer wants mechanism + evidence for why something works the way it does.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-6.1 | explain, mechanism | "Why does context rot happen?" | `context-rot.md` ✓ | `explain.md` ✓ | 1 | G2 Key Concepts + attention-budget-depletion pattern mechanism | long-tail | — | — |
| UC-6.2 | explain, design rationale | "Why do agent Contracts need Preconditions?" | `agent.md` | `explain.md` ✓ | 1 | G1 rationale + DD-78 framing note (Contract triple-role) | long-tail | `agent.md` | — |
| UC-6.3 | explain, cost mechanism | "Why does prompt caching reduce cost so dramatically?" | `prompt-caching.md` ✓ | `explain.md` ✓ | 1 | G2 §Caching + pricing math + Anthropic caching docs at Tier 3 if pressed | long-tail | — | — |

### Category 7 — Currency (3)

Consumer wants to know what's new on a topic since their last look.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-7.1 | whats-new, `<concept>` | "What's current on agent memory architectures?" | `memory.md` ✓ | `whats-new.md` ✓ | 1+2 | Recent findings (date-filtered) + re-synthesis staleness note on G7 | long-tail | — | — |
| UC-7.2 | whats-new, `<variant>` | "What's new on hybrid second-brain patterns this quarter?" | `second-brain.md` ✓ (variant C) | `whats-new.md` ✓ | 2 | Date-filtered findings in Agentic Systems cluster | long-tail | — | — |
| UC-7.3 | whats-new, all (scoped) | "What did the KB add about agents over the last N sessions?" | `*` (concept-scoped) | `whats-new.md` ✓ | 2 | Cross-dimension recency listing with pipeline_status filter | long-tail | — | — |

### Category 8 — Meta / KB queries (3)

Consumer wants to know what the KB itself covers, not the subject matter.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-8.1 | coverage, `<dim>` | "What does the KB cover about governance?" | `*` (dim-scoped) | `coverage.md` ✓ | 1 (indices) | Dimension routing + G9 finding count + pattern survey | long-tail | — | — |
| UC-8.2 | coverage, `<concept>` | "Which guides discuss multi-agent orchestration?" | `agentic-systems.md` ✓ (or `*`) | `coverage.md` ✓ | 1 (routing table) | Dim → guide mapping table for the concept | long-tail | — | — |
| UC-8.3 | coverage, `<pattern-class>` | "Are there any `contradicts` pairs in the memory findings?" | `memory.md` ✓ | `coverage.md` ✓ | 2 | Graph-query result over `related_findings` typed links | long-tail | — | — |

### Category 9 — Planning (2)

Consumer wants a sequence for building something across the lifecycle axis.

| ID | Query shape | Example | Concept file(s) | Operation file | Tier | Deliverable shape | Weight | Needs concept? | Needs op? |
|---|---|---|---|---|---|---|---|---|---|
| UC-9.1 | plan, build-order `<artifact>` | "How do I sequence building a new agent from scratch?" | `agent.md` | `plan.md` ✓ | 1 (lifecycle axis) | specify → build → verify → secure → operate; guide-per-step pointer | long-tail | `agent.md` | — |
| UC-9.2 | plan, composing `<concept>` + `<concept>` | "I want an agent + hybrid second brain — in what order?" | `agent.md`, `second-brain.md` ✓ | `plan.md` ✓ | 1+2 | Sequencing prose + cross-concept dependency notes | long-tail | `agent.md` | — |

### Count check

| Category | Rows |
|---|---|
| 1 Design advice | 5 |
| 2 Concrete deliverables | 4 |
| 3 Assessment | 6 |
| 4 Diagnosis | 5 |
| 5 Decision support | 4 |
| 6 Explanation | 3 |
| 7 Currency | 3 |
| 8 Meta / KB | 3 |
| 9 Planning | 2 |
| **Total** | **35** |

---

## Cross-tab — Concept × Operation Coverage

Cell count = number of use cases landing at (concept, operation). Cells with `-` have no current use case but are not ruled out. Existing reference-layer files are marked ✓ in the header.

| Concept ↓ \ Operation → | audit ✓ | diagnose ✓ | design ✓ | decide ✓ | explain ✓ | fetch ✓ | whats-new ✓ | coverage ✓ | plan ✓ | **Row total** |
|---|---|---|---|---|---|---|---|---|---|---|
| **agent.md** (planned) | 1 | 1 | 3 | 2 | 1 | 1 | — | — | 2 | **11** |
| **harness.md** ✓ | 1 | — | — | 1 | — | — | — | — | — | **2** |
| **second-brain.md** ✓ | 1 | — | 1 | — | — | — | 1 | — | 1 | **4** |
| **memory.md** ✓ | — | 1 | 1 | 1 | — | — | 1 | 1 | — | **5** |
| **context-rot.md** ✓ | — | 2 | — | — | 1 | 1 | — | — | — | **4** |
| **skill.md** ✓ | 1 | 1 | — | — | — | — | — | — | — | **2** |
| **prompt.md** ✓ | 1 | — | — | — | — | 1 | — | — | — | **2** |
| **agentic-systems.md** ✓ | 1 | — | — | — | — | — | — | 1 | — | **2** |
| **prompt-caching.md** ✓ | — | — | — | — | 1 | — | — | — | — | **1** |
| **`*`** (meta) | — | — | — | — | — | 1 | 1 | 1 | — | **3** |
| **Col total** | **6** | **5** | **5** | **4** | **3** | **4** | **3** | **3** | **3** | **36*** |

\* Row total sums to 36 because UC-9.2 uses two concept files (`agent.md` + `second-brain.md`); it counts once per concept in the table, once as a use case in the 35 total.

### What the cross-tab reveals

1. **`agent.md` is the gravity well.** 11 of 35 use cases (31%) route through it. Authoring it well — including variants (prompt-based / harness-based / autonomous-vs-supervised) — is the highest-leverage Phase 6 prerequisite after `prompt.md` and `skill.md`.
2. **`audit.md` is already exercised; the other operation files are all greenfield.** Operation-file authoring backlog: `diagnose`, `design`, `decide`, `explain`, `fetch`, `whats-new`, `coverage`, `plan`. Phase 6 only needs `audit.md` + (`agent.md`, `prompt.md`, `skill.md`); the rest are session-50+ backlog.
3. **No single cell owns more than 3 use cases.** The `(agent, design)` cell is the densest at 3. The composition works — variants, aspects, and query shape do the discriminating work without requiring per-use-case concept files.
4. **Tier-2 escalation is the default for 10 use cases (29%).** Mostly memory, second-brain variant C, diagnosis, and design-debate decisions. Tier-2 handling will need first-class treatment in the Phase 5 read-contract — not an afterthought.
5. **Tier-3 appears explicitly in 1 row (UC-5.3)** and implicitly escalatable in several more (UC-3.4, UC-6.3). Tier-3 remains consumer-request-gated, as the substrate audit specified.
6. **`*` (meta) rows do not need a concept file.** They route directly to the operation's own meta behavior (`fetch` → manifest; `whats-new` → date-filter; `coverage` → indices). Phase 5 read-contract must handle the `*` case explicitly.

---

## Authoring Backlog

### Concept files to author

Ordered by use-case load (cross-tab row totals).

| Priority | Concept file | UC count | Variants needed? | Blocks Phase 6? |
|---|---|---|---|---|
| **P1** | `agent.md` ✓ | 11 | Yes — prompt-based / harness-based / autonomous-vs-supervised | **Yes — UC-3.1** |
| **P1** | `prompt.md` ✓ | 2 | No (single referent) | **Yes — UC-3.2** |
| **P1** | `skill.md` ✓ | 2 | No — `skill` has one referent; include G9.I6 gate per session-48 Test 4 | **Yes — UC-3.3** |
| P2 | `memory.md` ✓ | 5 | Yes — working / episodic / semantic / global-learnings | No |
| P2 | `context-rot.md` ✓ | 4 | No | No |
| P3 | `agentic-systems.md` ✓ | 2 | No (rename lands via Dimension 11) | No |
| P3 | `prompt-caching.md` ✓ | 1 | No | No |
| P4 | `mcp.md` ✓ (not in UC list but planned in `_index.md`) | 0 observed | No | No |

**P1 trio is the Phase 6 blocker.** All three must exist (minimally) before `/assess-agent`, `/assess-prompt`, `/assess-skill` can be authored as load-and-apply wrappers.

### Operation files to author

Ordered by cross-tab column totals.

| Priority | Operation file | UC count | Session-49 blocker? |
|---|---|---|---|
| — | `audit.md` ✓ (exists) | 6 | — |
| P2 | `diagnose.md` ✓ | 5 | Session 50 |
| P2 | `design.md` ✓ | 5 | Session 50 |
| P3 | `decide.md` ✓ | 4 | Session 50+ |
| P3 | `fetch.md` ✓ | 4 | Session 50+ |
| P3 | `explain.md` ✓ | 3 | Session 50+ |
| P3 | `whats-new.md` ✓ | 3 | Session 50+ |
| P3 | `coverage.md` ✓ | 3 | Session 50+ |
| P4 | `plan.md` ✓ | 3 | Session 50+ |

**No operation file besides `audit.md` is a Phase 6 blocker.** The three assessment skills (`assess-prompt`, `assess-agent`, `assess-skill`) all compose `audit.md` × concept file.

### Variant-authoring hotspots

- `agent.md` variants (prompt-based / harness-based / autonomous-vs-supervised) are load-bearing for UC-5.4 (model selection overlay varies by variant), UC-9.1 (sequencing differs per variant), and UC-4.2 (tool-use diagnosis differs between prompt-based and harness-based agents). Phase 6 must at least stub the variants, even if the full per-variant composition table is authored iteratively.
- `memory.md` variants do not block Phase 6. Deferred to session 50+.
- `second-brain.md` variants (already authored) correctly surface on UC-3.5, UC-7.2, UC-9.2.

---

## Frequency-Weight Justification

Core (~80% combined) — the three categories Nick named highest-priority or that carry the consumer pain:

| Category | Estimated share | Reasoning |
|---|---|---|
| Assessment (Cat 3) | ~40% | Nick's named top-priority deliverables (assess-*). Three UCs in this category are all `core`. |
| Design advice (Cat 1) | ~25% | "How do I build X" queries dominate practitioner traffic in comparable KBs; 4 of 5 UCs are `core` (variant-ambiguous UC-1.4 demoted to long-tail). |
| Diagnosis (Cat 4) | ~15% | Symptoms are urgent; UCs 4.1–4.3 are `core`. |

Long-tail (~20% combined) — five categories that are valuable but per-query infrequent:

- Decision support, explanation, concrete deliverables, currency, meta/KB, planning.
- Each individually is small; together they carry the breadth that makes the Librarian reference layer worth authoring beyond the three assess-* skills.

**Calibration plan.** These weights are estimates. Once the assess-* skills run for a month, actual query distribution can be logged (via a light Librarian usage log — proposed for session 50+ IB). Weights in this registry are to be revised from measurement, not guessed again.

---

## Open Questions for Nick

1. **Meta/coverage vs. operation files.** UCs 8.1–8.3 and the `*` rows route to `coverage.md` as an operation. Alternative: treat coverage as a *Librarian meta-behavior* (always available without a concept file, handled by the Librarian agent definition itself). Prefer operation-file treatment for symmetry; flagging in case you prefer otherwise.
   - Nick: Lets do operation-file approach. 
2. **`fetch.md` vs. splitting into `fetch-template` / `fetch-rule` / `scaffold`.** The cross-tab collapses UCs 2.1–2.4 into one operation with three sub-ops. Alternative: three separate operation files. Preferred collapse for lightness; flagging for your call.
  - Nick: Agreed to prefer collapse for now. For any of these, we should be mindful of the number of tokens in there. If it will exceed a certain threshold, then we should consider splitting. This would be a meta-concern of the 
3. **`whats-new` staleness dependency.** UC-7.1 depends on guide staleness data (per the lifecycle spec's staleness ledger). If Phase-1 lifecycle DDs aren't filed, `whats-new` degrades to "list recent findings by `created` date" — serviceable but thinner. Confirm that degraded mode is acceptable in the interim.
  - Nick: Lets defer implementation design details for now. Im wondering if this is actually something we should even have in here... perhaps we should force the whats-new to take a date as input, which can be checked against guides and other artifacts that the Librarian consults to answer the query?
4. **Agent-variant authoring discipline.** Phase 6 needs `agent.md` with at least stubbed variants. Full variant composition tables can iterate session-by-session. Confirm this iterative approach is acceptable vs. requiring all three variants fully specified at Phase 6 write.
  - Nick: Oh, lets definitely keep it light yes. The stubs should provide just enough information to help a human understand the distinctions (and possibly return with a query that asks for more about a given variant)
5. **Weight calibration timing.** When is it worth standing up a Librarian usage log? Not a session-49 task, but flagging as an IB item for session 50+ so the weights move from estimates to measurements.
  - Nick: I dont thing a usage log is necessary. We already have a System Log for IL that can assume this responsibility. What do you think?

---

## Cross-References

- Substrate audit (9 categories + rationale): `archive/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md`
- Contract-section spot check (G9.I6 gate for safety-critical skills): `archive/design-notes/2026-04-21-contract-section-spotcheck-agent-audit.md`
- Librarian reference layer exemplars: `operations/references/librarian/_index.md`, `harness.md`, `second-brain.md`, `audit.md`
- Guide routing table: `operations/references/guide-routing-table.md`
- Research dimensions registry: `operations/references/research-dimensions.md`
- Codifier agent definition: `agents/codifier/agent.md`
- Librarian agent definition: `agents/librarian/agent.md`
- Governing DDs: DD-77, DD-78, DD-80, DD-81, DD-82, DD-86
