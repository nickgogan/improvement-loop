---
title: "Substrate Audit — Dimensions, Patterns, Guides vs. Librarian Use Cases"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-20"
updated: "2026-04-21"
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
  - "audit"
  - "taxonomy"
  - "librarian"
  - "proposal"
aliases:
  - "Taxonomy audit"
  - "Substrate audit"
  - "Dimension-guide-librarian alignment"
---

# Substrate Audit — Dimensions, Patterns, Guides vs. Librarian Use Cases

**Status:** Diagnostic design note. Not a decision. Nick asked for an ultrathink audit on whether the current taxonomy chain (dimensions → findings → patterns → guides) actually supports the Librarian use cases. This note does that audit honestly — including where I think the current substrate is well-formed, where it has structural gaps, and where gaps are fatal vs. workable.

This note sits **before** the pipeline collapse proposal (`2026-04-20-pipeline-collapse-proposal.md`) in logical order, even though written after. The collapse proposal assumes guides-as-primary-consumer-surface. That assumption is what this audit tests.

**Revision history:**
- **2026-04-20 (v1):** Initial draft. Recommended Option α (view artifacts as a third substrate layer).
- **2026-04-21 (v2 — this revision):** Updated post-interview with Nick. Diagnostic (Framing through Root-Cause Analysis) stands; prescription replaced. Key changes: (a) recommendation moved from Option α to **Option α'** — composition registry + three-tier access, no view artifacts as default; (b) rubric vocabulary disambiguated; (c) dimensions reframe confirmed as **reframe-only** with Agentic OS → Agentic Systems rename, no new Harness dimension; (d) Librarian reference layer (concept files + operation files) introduced as the minimum artifact to support the composition; (e) "consumer artifacts" framing dropped. Nick's inline notes from v1 preserved below in the Current Chain sections with resolutions.

---

## Framing

Nick's question, restated precisely:

> *"We have research dimensions → patterns → guides. Given that the Librarian is the primary consumer surface, is this chain the right substrate? Do the mappings at each step actually support the use cases the Librarian needs to handle?"*

Three sub-questions are packed into that:
1. **Are research dimensions the right organizing principle at the intake layer?**
2. **Does the pattern → guide routing preserve or destroy the information Librarian needs?**
3. **Are the guides themselves structured for the consumer queries they need to answer?**

The Librarian's highest-priority deliverables (per the session-47 handoff) are `assess-prompt`, `assess-agent`, `assess-skill`. These are the stress test. If the substrate works for these, it works for most of the 9 use case categories. If it doesn't, the substrate has a structural gap the collapse proposal cannot patch over.

**What this note is NOT.** It is not a proposal to rewrite the dimension registry. It is not a proposal to re-cluster the guides. It is a diagnostic that surfaces where the current chain does and does not align to consumer use cases, and offers options ordered from lightest (add a view layer) to heaviest (restructure guides).

---

## The Current Chain

### Layer 1 — Intake: Research Dimensions

11 dimensions (10 original + Agentic OS emerging). Each dimension is a **query scope** — what the Researcher scans for during `/research-loop`. See `operations/references/research-dimensions.md`.

| # | Dimension | Breadth | Primary consumer lens |
|---|-----------|---------|----------------------|
| 1 | Context Engineering | Broad | Aspect of building an agent |
| 2 | Model | Medium | Aspect of building an agent |
| 3 | Prompt | Medium | Aspect of building an agent |
| 4 | Tools | Narrow | Aspect of building an agent |
| 5 | Intent (Meta-Dimension) | Medium | Aspect of specifying an agent |
| 6 | Orchestration | Very broad | Aspect of composing agents |
| 7 | Evaluation | Broad | Practitioner phase (verify) |
| 8 | Sandboxing | Narrow | Aspect of securing an agent |
| 9 | Governance | Narrow | Aspect of overseeing agents |
| 10 | Agent Design | Broad | Aspect of specifying an agent |
| 11 | Agentic OS (emerging) | Broad | Consumer artifact class (!) |

**Observation — dimensions as aspects, not artifacts.** Ten of eleven dimensions are **aspects of agent systems** (context, tools, safety, governance, etc.). They partition what research surfaces but not what consumers build. The eleventh, Agentic OS, breaks the pattern — it's indexed by consumer artifact class (personal knowledge management systems). Agentic OS's emergence suggests the dimension registry is already straining the aspect frame.

This is Nick: I agree that the Agentic OS does begin to break the pattern. Let's instead re-frame this research dimensions to something more Researcher-specific. What would you propose?

**Resolution (2026-04-21):** Reframe-only. Dimensions stay as aspect-topic scan scopes — the registry's purpose is "what the Researcher goes looking for in the world," which is a producer-side question and should be named that way. Two concrete changes: (a) **rename Agentic OS → Agentic Systems** (scope: personal/team/business operational systems where multiple agents serve user workflows — second-brain, daily briefs, scheduled-task setups, vault-as-OS patterns); (b) **rewrite `operations/references/research-dimensions.md` preamble** to make Researcher-specificity explicit (these are scan topics, not consumer categories). **No new Harness dimension** — Harness is a cross-cutting consumer concept that touches Tools + Context + Prompt + Orchestration + Sandboxing. It belongs in the Librarian reference layer (see §"The Librarian Reference Layer" below), not as a scan scope. No two-axis (Topics × Domains) split; the "Application Domains" speculation in v1 was not evidence-grounded beyond Agentic OS and was dropped.

### Layer 2 — Substrate: Findings

545 findings as of session 45. Each finding carries:
- `category` — one of the 11 dimensions (drives guide routing)
- `priority` — P1 / P2 / P3 (drives extraction gating)
- `evidence_strength` — Strong / Medium / Weak (drives confidence)
- `related_findings[]` — typed links (same-problem, contradicts, extends, enables)
- `consumed_by[]` — reverse index to downstream artifacts
- `pipeline_status` — raw / classified / extracted / synthesized / deployed

The finding layer is the rich one. Related-findings links create a graph; typed relationships encode design debates. This is the substrate the Librarian would most directly benefit from querying, but no current consumer path exposes the finding graph — all consumer paths go through guides.

### Layer 3 — Routing: Dimension → Guide Mapping

The guide routing table (`operations/references/guide-routing-table.md`) maps each dimension to a primary guide (with secondary guides for cross-cutting dimensions). This mapping is **not 1:1**:

| Mapping shape | Example | Count |
|---------------|---------|-------|
| Dimension → 1 guide (clean) | Tools → G5 | 4 dimensions |
| Dimension → 1 guide (shared with another dim) | Prompt → G8 (also hosts Model) | 2 dimensions |
| Dimension → 2 guides | Context Engineering → G2, G7 | 2 dimensions |
| Dimension → 3 guides | Orchestration → G3, G3b, G7 | 3 dimensions |
| Dimension → emerging | Agentic OS → (unrouted) | 1 dimension |

Broad dimensions (Context Engineering, Orchestration, Agent Design, Evaluation) fan out to multiple guides. Narrow dimensions (Tools, Intent, Sandboxing, Governance) map 1:1.

**Observation — fan-out is where cross-guide synthesis is hidden.** Every multi-guide dimension is a place where the Librarian must reassemble content. The routing table names this implicitly but does not operationalize it.
- This is Nick: What would you suggest? Im starting to consider the idea that the guides are sort of pre-generated answers to many of the use cases/questions weve outlined. It could suffice for a shallow pass, but the user could ask the Librarian to go deeper and look into the patterns or the findings or even by examining/comparing against any GH repo that would be watched in this system. What do you think?

**Resolution (2026-04-21):** Adopt as the **three-tier Librarian access model**. Guides are shallow-tier pre-generated answers — the default first read. Depth-on-demand escalation follows:
- **Tier 1 (shallow, default):** guides with section-addressable reads (anchors per the collapse proposal). Satisfies most "how do I X" and "explain Y" queries.
- **Tier 2 (medium, on request or when Tier 1 insufficient):** patterns + findings graph. Uses `related_findings` typed links (`contradicts`, `extends`, `same-problem`, `enables`) for design-debate content and cross-finding rationale. Exposes the finding graph that Tier 1 flattens.
- **Tier 3 (deep, on explicit request):** watched-library GitHub repos. Live code comparison against reference implementations. Promotes watched-libraries from Researcher-monitoring-only to first-class consumer-accessible substrate.

This changes what watched-libraries are for: currently they're a Researcher upstream-change surface; post-adoption they're also a Librarian deep-dive destination. Each tier has a precision/cost profile; Librarian defaults to Tier 1 and escalates on consumer ask or when Tier 1 confidence is low.

### Layer 4 — Output: Guides

11 synthesized guides, each indexed by a **practitioner question** (the `Question` column in the routing table). Examples:
- G1: "How do I specify what my agent should do?"
- G2: "My agent is losing context or burning tokens"
- G4: "How do I verify my agent actually works?"

Guides are organized into a lifecycle axis (specify → build → verify → secure → operate) that gives a second navigation path.

**Observation — guides are indexed by practitioner question, which is a different surface than both dimensions and consumer artifacts.** The practitioner question is the consumer's *task* mental model ("I'm managing context today"). It is not their *artifact* mental model ("I'm writing an agent.md today"), nor their *symptom* mental model ("my agent is failing").
- This is Nick: Agreed. Now Im starting to wonder what the point of having the concept of "consumer artifacts" is. What do you think?

**Resolution (2026-04-21):** "Consumer artifacts" framing dropped. It was shorthand for "the consumer brings an artifact to evaluate" — but that's only true for one use-case shape (assessment). Real consumer queries combine a **verb** (operation: audit, diagnose, design, decide) with a **noun** (concept: agent, harness, second-brain, context-rot). The Librarian's job is to decompose the query into substrate reads along both axes, not to pre-index by "artifact." Replaced in v2 by:
- **Operation files** (verb-keyed): `audit.md`, `diagnose.md`, `design.md` — procedural rules for a given operation.
- **Concept files** (noun-keyed): `harness.md`, `second-brain.md`, `agent.md` — definition + composition pointers for a given term.

See §"The Librarian Reference Layer" below for the full design.

---

## Librarian Use Case Categories — Substrate Needs

From the session-46 draft: 35 use cases across 9 categories. Per category, here's what substrate is needed and what read shape the query implies.

| # | Category | Read shape needed | Aggregation required? |
|---|----------|-------------------|----------------------|
| 1 | Design advice ("how should I build X?") | Step-by-step guidance indexed by what consumer is building | Moderate — spans 2–4 guides for agent-level queries |
| 2 | Concrete deliverables ("give me a template for X") | Ready-to-copy scaffold indexed by artifact type | Low — templates fit naturally inside single guides |
| 3 | **Assessment ("audit my X")** | Rubric indexed by consumer artifact type, with criteria and citations | **High — 5–6 guides per agent audit** |
| 4 | Diagnosis ("my agent is failing with symptom X") | Symptom → likely cause → guide section index | **High — symptoms scatter across Pitfalls sections** |
| 5 | Decision support ("should I use A or B?") | Tradeoff tables, design debates, "it depends" patterns | Medium — tradeoffs embedded but not indexed |
| 6 | Explanation ("why does X happen?") | Mechanism + evidence, rationale patterns | Low — guides carry rationale inline |
| 7 | Currency ("what's current on X?") | Date-indexed finding or guide view | Low — needs a recency filter, not structural change |
| 8 | Meta/KB queries ("what does the KB cover?") | Coverage map (dimensions, guides, finding counts) | Low — `_index.md` and routing table suffice |
| 9 | Planning ("how do I sequence building X?") | Phase-indexed content | Low — lifecycle axis already supports this |

The categories with high aggregation demand are exactly where the Librarian's highest-priority deliverables live.

---

## Mapping Test: Does the Current Substrate Deliver?

For each of the 9 categories, walk the current chain and answer honestly.

### Category 1 — Design advice

**Consumer query example:** *"How should I design my agent's context files?"*

- Maps cleanly to Context Engineering → G2. Librarian reads G2. Satisfied.

**Consumer query example:** *"How should I design my agent?"* (no aspect specified)

- Spans Intent (G1) + Context (G2) + Architecture (G3) + Tools (G5) + Design Patterns (G10). Librarian must aggregate 5 guides or probe the consumer for an aspect.
- **Verdict:** Works for aspect-specified queries. Strains on artifact-level queries. Fixable with a cross-reference layer.

### Category 2 — Concrete deliverables

**Consumer query example:** *"Give me a template for a context budget worksheet."*

- Template exists as `## Templates` section in G2, anchored sub-sections for each template variant.
- Post-collapse (per pipeline collapse proposal), Librarian can read by anchor.
- **Verdict:** Works with anchor-addressable reads. Satisfied.

**Consumer query example:** *"Show me all available templates."*

- No cross-guide template catalog exists. Librarian would grep `## Template:` across all 11 guides.
- **Verdict:** Works but not fast. A `templates-index.md` derived view would help.

### Category 3 — Assessment *(highest priority)*

**Consumer query:** *"Audit my agent.md."*

- **Rubric domains needed:** intent/spec (G1), identity/persona (G10), context management (G2), architecture/decomposition (G3), tool design (G5), safety/permissions (G6), governance/oversight (G9). **7 guides, ~150KB combined.**
- No agent-audit rubric exists as an artifact. Librarian constructs the rubric at query time, from memory of what's in each guide, or by reading all 7 guides and filtering.
- **Failure modes:**
  - Criterion selection is fuzzy — different guides use different vocabularies for the same aspect.
  - Rubric drifts every time guides re-synthesize.
  - Read cost is heavy and cache-hostile.
  - Coverage is inconsistent across runs — Librarian may emphasize different criteria per query.
- **Verdict:** **Does not work natively.** The substrate has the raw material but no aggregated artifact. Runtime aggregation is expensive and fragile.

**Consumer query:** *"Audit my prompt."*

- Rubric domains: prompt craft (G8), intent (G1), context (G2), maybe tool use (G5). 4 guides, ~100KB.
- Same pattern as agent audit. Same failure modes.
- **Verdict:** Same as above. Does not work natively.

**Consumer query:** *"Audit my skill."*

- Rubric domains: spec (G1), prompt (G8), tool use (G5), safety (G6), workflow (G3b). 5 guides.
- Same pattern.
- **Verdict:** Same as above.

**This is the critical gap.** Three of Nick's top-priority Librarian deliverables hit the same missing layer.

### Category 4 — Diagnosis

**Consumer query:** *"My agent keeps losing track of constraints."*

- This is context rot. Covered in G2 Pitfalls + G7 Key Concepts + `context-rot-detection-and-mitigation` pattern + `context-rot-attention-budget-depletion` pattern.
- No symptom → cause → guide-section index exists. Librarian must know the mapping or search Pitfalls.
- **Verdict:** Works if Librarian remembers; brittle otherwise. A symptom map would help.

**Consumer query:** *"My agent's tool calls are erratic."*

- Covered partially by G5, partially by G8 (prompt craft for tool use), partially by G2 (tool definitions consume context).
- No cross-guide diagnosis view.
- **Verdict:** Works with heavy search. Symptom-indexed view would resolve.

### Category 5 — Decision support

**Consumer query:** *"Should I use a single agent or multi-agent architecture?"*

- Covered in G3 with a Key Concepts section. Pattern `autonomy-gradient-not-binary-delegation` is relevant.
- **Verdict:** Works — G3 is the right landing spot. Clean.

**Consumer query:** *"MongoDB single-store vs. triple-storage memory?"*

- Covered in G7 via `mongodb-single-store-polymorphic-evidence-memory` vs. `triple-storage-memory-architecture` (`contradicts` link between them).
- **Verdict:** Works if Librarian exposes the finding-graph `contradicts` relationship. Today, Librarian reads guides not findings — the graph relationship is invisible unless guides explicitly reproduce it.

### Category 6 — Explanation

**Consumer query:** *"Why does context rot happen?"*

- G2 Key Concepts explains the n²-attention mechanism. Pattern `context-rot-attention-budget-depletion` has the mechanism in more detail.
- **Verdict:** Works well. Explanation is one of the things guides do best.

### Category 7 — Currency

**Consumer query:** *"What's current on agent memory architectures?"*

- G7 covers memory. New findings (session 45 Memongo cluster) are classified but not yet re-synthesized into G7.
- **Verdict:** Works but laggy. "Current" requires either recent re-synthesis OR a "recent findings" view on top of findings. Current state: stale until re-synthesis runs.

### Category 8 — Meta/KB queries

**Consumer query:** *"What does the KB cover about governance?"*

- Dimensions registry + guide routing table + G9 finding count (10) answer this.
- **Verdict:** Works. Existing `_index.md` files suffice.

### Category 9 — Planning

**Consumer query:** *"How do I sequence building a new agent?"*

- Lifecycle axis (specify → build → verify → secure → operate) maps directly. Routing table surfaces it.
- **Verdict:** Works well.

---

## Gap Inventory

Gaps ordered by severity — how much consumer value is lost if the gap remains.

| # | Gap | Severity | Affected use cases | Current workaround |
|---|-----|----------|-------------------|--------------------|
| 1 | **No consumer-artifact-indexed rubrics.** No artifact exists that says "for an agent, these are the N criteria, here's where each criterion is authoritative in the KB." | **High** | Assessment (3), partially Design advice (1) | Runtime aggregation at Librarian query time |
| 2 | **No symptom → cause → guide-section index.** Pitfalls are scattered across guides; no lateral view. | **Medium-high** | Diagnosis (4) | Librarian memory + grep across Pitfalls sections |
| 3 | **Finding-level graph relationships are invisible to consumer path.** `contradicts`, `extends`, `same-problem` links carry design-debate content that guides sometimes flatten or omit. | **Medium** | Decision support (5), Explanation (6) | None — Librarian reads guides, not findings |
| 4 | **No template / rule / skill catalog spanning guides.** Post-collapse, the anchor manifest (collapse proposal DD-NEW-1) will partially address this per guide, but no cross-guide index. | **Low-medium** | Concrete deliverables (2) | Grep `## Template:` across guides |
| 5 | **No recency filter.** "What's current on X" requires either recent re-synthesis or date-filtered reads. | **Low-medium** | Currency (7) | Staleness ledger on guides |
| 6 | **Aspect-centric guide structure strains on artifact-level queries.** Queries that start with a consumer artifact (agent, prompt, skill) must cross-aggregate aspects (context, tools, safety, governance). | **Medium** | Design advice (1), Assessment (3) | Multi-guide reads |

Gaps 1 and 2 are load-bearing. Gaps 3–6 are workable. Gap 6 is a structural observation that could motivate bigger changes but isn't strictly necessary to fix.

---

## Root-Cause Analysis — Why Do the Gaps Exist?

### The two-layer design that produced them

The substrate has two implicit layers:

1. **Producer layer** — dimensions + findings. Researcher-facing. Optimized for "what do we scan for?" The dimensions are aspects because that's how agent-systems research is organized in the external world.

2. **Product layer** — guides. Consumer-facing for "how do I X" queries. Indexed by practitioner question. Aspect-centric because they inherit from dimensions.

Both layers are reasonable for their designed purpose. The gap is that **there's no third layer** — no consumer-view layer that re-indexes product content around consumer artifact types, symptoms, or decisions. The Librarian has been expected to *be* the third layer — computing the view at query time.

### Why expecting Librarian to aggregate at runtime is insufficient

- **Cost.** Each assess-agent query reads ~150KB of guide content. Even with aggressive caching, cross-session warmup is expensive.
- **Consistency.** Runtime aggregation depends on Librarian's reasoning. Two sessions can produce different rubrics from the same substrate.
- **Auditability.** If the rubric drifts between sessions, Nick can't tell whether Librarian has a bug or the substrate has a bug.
- **Non-scaling.** As the KB grows (545 → 1000 → 2000 findings), guides grow, and runtime aggregation cost scales linearly.

### Why this wasn't visible earlier

- The guides were synthesized before Librarian use cases were canonicalized. Sequence mattered: substrate-first, consumer-second.
- The Librarian agent exists on paper (DD-82) but hasn't been put into production. The highest-priority deliverables (assess-*) haven't been built yet.
- Within the current KB shape, the gap is papered over — the Librarian *can* aggregate at runtime for ad hoc queries. It's only when you commit to assess-* as stable, repeatable skills that the gap becomes load-bearing.

Nick's ultrathink prompt catches this at the right moment: before assess-* skills are built, not after.

---

## Disambiguation — "Rubric" in Our System

Before the options: the word "rubric" appears in three distinct senses that got conflated in v1. Naming them explicitly so the prescription reads cleanly.

| Rubric | Where | Role | Consumer |
|---|---|---|---|
| **Form classification rubric** | `operations/references/form-classification-rubric.md` | Decision spec for classifying findings into pattern / skill / rule / template / agent. Producer-side. | `/identify-artifacts` — deterministic input. |
| **Artifact acceptance rubric** | `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md` (proposed, session 46) | Write-time gate — which artifacts are worth staging. Per-form accept/reject criteria. | `/extract-artifacts` + `/synthesize-guide` — gates what enters `extracts/`. |
| **Hypothetical assessment rubrics** | Nonexistent as artifacts. Either emergent (from guide Contract sections, composed at read time) or materialized (view artifacts). | Read-time audit criteria for consumer-submitted artifacts. | `/assess-prompt`, `/assess-agent`, `/assess-skill`. |

And a fourth thing that looks rubric-shaped but is actually governance — **Contract sections (DD-78 ContractSpec)** on every artifact:
- Four fields: **preconditions** (when the artifact applies), **invariants** (what must hold), **governance** (who gates changes), **recovery** (what to do when things break).
- Authored per DD-78 as the artifact's own operational contract, not as consumer-audit criteria. However, invariants *read as* declarative testable statements by construction — they can function as audit criteria with minor framing.
- Untested claim (v1 asserted it, v2 flags it for validation): Contract invariants across `{G1, G2, G3, G5, G6, G9, G10}` compose into a coherent agent-audit rubric. Spot-check required; deferred to session 48.

Throughout the rest of this note, "assessment rubric" means the third kind unless qualified.

---

## Options — From Lightest to Heaviest

Four options evaluated. v1 recommended α. v2 recommends **α' (alpha-prime)** — a lighter variant of α that emerged from interview.

### Option α' — Composition Registry + Three-Tier Access (v2 recommendation)

**Shape:** No new substrate form. Instead, introduce a **Librarian reference layer** of small pointer artifacts (concept files + operation files) that encode how to decompose consumer queries into reads against existing guides / patterns / findings / watched-library repos. Depth-tiered access model from Tier 1 (guides) through Tier 2 (patterns + findings graph) to Tier 3 (watched-library repos).

```
[Dimensions] --> [Findings] --> [Guides]
                     |              |
                     v              v
               [Librarian reference layer]  <-- concept files + operation files
                     |
                     v
              [Librarian Skills]
```

**Concrete mechanisms:**
- **Concept files** (noun-keyed): one file per consumer term (harness, second-brain, agent, memory, context-rot, mcp, …). Contains: definition, "not to be confused with," composition pointers (where to look in the KB by aspect), optional variants (Agent / Memory / Second Brain have multiple referents), Librarian read rule.
- **Operation files** (verb-keyed): one file per Librarian operation (audit, diagnose, design, …). Contains: default composition rule (which guide sections to read), procedure, consumer-input handling, output shape.
- **Three-tier access:** Librarian defaults to Tier 1 (guides). Escalates to Tier 2 (patterns + findings graph using `related_findings` typed links) on consumer ask or when Tier 1 confidence is low. Escalates to Tier 3 (watched-library repo reads) on explicit consumer ask for deep comparison against reference implementations.

**Pros:**
- No new *artifact form* — just small pointer files. Much lighter than view-artifact authoring.
- The reference layer is a routing table, not a knowledge base. It can be hand-authored and iterated.
- Dimensions + guides unchanged. Collapse proposal unchanged.
- Bounded per-query read cost via the composition pointers.
- Promotes watched-libraries from Researcher-only monitoring to Librarian-accessible depth substrate.
- Incremental: start with ~5 concept files + ~3 operation files; grow as Librarian encounters terms.

**Cons:**
- Composition rules live as prose + pointer tables. Less machine-enforced than a view with structured fields.
- Upfront judgment call per concept/operation: what's worth authoring vs. what stays runtime-aggregated.
- Depends on Contract sections of guides being usable as audit criteria (untested — spot-check deferred).

**Implementation cost:** Low. ~1 new directory (`operations/references/librarian/`). Initial authoring: ~5 concept files, ~3 operation files, one template each. No new skill required; existing Librarian agent reads the reference files directly.

### Option α — Pre-Built View Artifacts (v1's original recommendation; now superseded by α')

**Shape:** Same architectural impulse as α' but heavier — introduce standalone **view artifacts** (`views/rubrics/agent-audit-rubric.md`, `views/diagnostics/symptom-map.md`, etc.) that *are* the rubrics, with structured fields. Requires a synthesis skill to maintain them from guides.

**Why α' replaces α:** Nick's interview feedback surfaced that much of what v1 proposed as "view artifact content" is already in guide Contract sections (rubric-shaped invariants) — we don't need to duplicate that content into view files; we need pointers to it. The reference layer is the pointer artifact; guides remain the content authority. Views as standalone artifacts become an *optional* escalation when raw composition needs curation (high-stakes assessment) — not the default.

**When would α win over α'?** If the spot-check of Contract sections (deferred to session 48) shows invariants don't compose into usable audit rubrics without curation, views become necessary as curated rubric artifacts over the raw guide content. Retained as a fallback plan, not a primary recommendation.

### Option β — Re-Normalize Dimensions to Consumer Artifacts

**Shape:** Rewrite the dimension registry around consumer artifact types. Researcher intake becomes consumer-aligned.

**Verdict:** Over-engineered and disruptive. Major impact on Researcher workflow (545 findings need re-categorization); loses the aspect-centric framing that matches how research is organized externally; doesn't eliminate cross-aspect synthesis anyway. **Not recommended. Rejected in v2.**

### Option γ — Restructure Guides Around Consumer Artifacts

**Shape:** Keep dimensions as intake; re-cluster the 11 guides into consumer-artifact-indexed mega-guides.

**Verdict:** Addresses the right problem but over-commits. Loses aspect-indexed queries that work well today; creates 150KB mega-guides; breaks the lifecycle axis. **Not recommended. Rejected in v2.**

### Comparison Table (v2)

| Criterion | **α' (Reference layer + tiers)** | α (View artifacts) | β (Re-dimension) | γ (Re-guide) |
|-----------|--------------------------------|---------------------|------------------|--------------|
| Addresses assessment gap | ✓ (pending Contract-section validation) | ✓ | ✓ | ✓ |
| Addresses diagnosis gap | ✓ | ✓ | Partial | Partial |
| Addresses decision-support gap | ✓ (Tier 2 finding graph) | Partial | ✗ | ✗ |
| Preserves Researcher workflow | ✓ | ✓ | ✗ | ✓ |
| Preserves aspect-indexed queries | ✓ | ✓ | ✓ | ✗ |
| Preserves lifecycle axis | ✓ | ✓ | ✓ | ✗ |
| Compatible with collapse proposal | ✓ | ✓ | ✓ | Needs refactor |
| Adds new substrate form | No (pointer files only) | Yes (views) | No | No |
| Single source of truth | Guides | Guides | Guides | Mega-guides |
| Migration cost | Lowest | Low-medium | High | Medium-high |

---

## Recommendation

**Option α' — Librarian reference layer (concept + operation files) + three-tier access.**

### Reasoning

1. **Lighter than α.** Pointer-based rather than content-based. No new synthesis skill, no new artifact form, no duplication of guide content.
2. **Addresses the load-bearing gaps without touching the producer side.** Dimensions stay. Findings stay. Guides stay. Pipeline collapse stays valid.
3. **Gives the finding graph a consumer path.** v1's Gap #3 (finding-graph invisible to consumer) was unsolved by α; α' solves it explicitly via Tier 2 — patterns + findings with `related_findings` edges are a deliberate second-tier substrate.
4. **Promotes watched-libraries.** They become first-class consumer substrate (Tier 3) rather than Researcher-monitoring-only — picks up the Tier-3 depth Nick explicitly asked for.
5. **Incremental adoption.** Start with 3 operations + 5 concepts; grow. No big up-front authoring obligation.
6. **Degrades gracefully.** If a concept/operation isn't authored, Librarian falls back to runtime aggregation as today. The reference layer is an optimization, not a dependency.

### The Librarian Reference Layer

Directory: `operations/references/librarian/`. Flat layout, two file types distinguished by `type:` frontmatter.

**Concept file template** (noun-keyed):
```yaml
---
term: harness
type: concept
variants: []   # optional; populated for Agent, Memory, Second Brain
target_system: improvement-loop
---
```
Body sections:
- **Short definition** — one sentence.
- **Not to be confused with** — adjacent-but-distinct terms with pointers.
- **Variants** (optional, one subsection per variant) — used when the term has multiple distinct referents a consumer might mean. Applies to: **Agent** (prompt-based / harness-based / autonomous-vs-supervised), **Memory** (working / episodic / semantic / global-learnings), **Second Brain** (human / AI / hybrid). Does *not* apply to: Harness, MCP, Context Rot, Agentic Systems — single referent each.
- **Composition** — table of (aspect → guide / dim → specific anchors / findings). Where to look in the KB.
- **Librarian read rule** — default query handling. Variant-selection notes if variants present. Depth escalation signals.

**Operation file template** (verb-keyed):
```yaml
---
operation: audit
type: operation
target_system: improvement-loop
---
```
Body sections:
- **Short definition** — what this operation does.
- **Default composition rule** — which substrate to read (guide sections, typically Contract + Pitfalls for audit; Step sections for design; etc.).
- **Procedure** — how Librarian applies the rule to consumer input.
- **Consumer input handling** — what the consumer submits, format expectations.
- **Output shape** — structured response format.
- **Noun-specific overrides** (optional) — when the operation applies differently to specific concepts, pointer to the concept file's override section.

**Early entries (sized for session 48):**
- Concepts: `harness.md`, `agentic-systems.md`, `second-brain.md` (with 3 variants), `context-rot.md`, `mcp.md`. Likely next wave: `agent.md` (with variants), `memory.md` (with variants), `prompt-caching.md`, `skills.md`.
- Operations: `audit.md`, `diagnose.md`, `design.md`.

### Three-Tier Access Model (formal)

| Tier | Substrate | When used | Cost | Precision |
|---|---|---|---|---|
| **Tier 1 (shallow, default)** | Guides, section-addressable per the collapse proposal anchor manifest | First pass for every query; satisfies most consumer questions | Low (~5–25 KB per query) | Curated, synthesized |
| **Tier 2 (medium, on escalation)** | Patterns + findings, using `related_findings` typed links (`contradicts`, `extends`, `same-problem`, `enables`) | Consumer asks for depth; Tier 1 confidence low; design-debate queries; cross-finding rationale | Medium (~10–50 KB per query) | Raw, authoritative on specific mechanisms |
| **Tier 3 (deep, on explicit request)** | Watched-library repos (live GitHub content via existing `/watch-upstream` caches) | Consumer asks to compare their approach against reference implementations; "how does Anthropic actually do this?" queries | High (~100 KB+ per query, external fetch) | Ground truth, latest |

Concept and operation files should name which tiers they escalate to by default.

### What Option α' implies for existing work

**Pipeline collapse proposal (Stream A, already drafted):** Still valid. Trim the "Librarian Read Contract" section — replace its three-option view/manifest sketch with a pointer to this audit's reference layer + three-tier access. The guide anchor manifest (DD-NEW-1 in the collapse proposal) remains load-bearing: it's what concept files point into and what Librarian's section-addressable Tier-1 reads depend on.

**Lifecycle spec (session 46):** Reference files need lifecycle mechanics — lighter than guides (they're pointer files; regeneration is cheaper than synthesis). Reuses existing mechanisms: frontmatter `last_change_*` fields, SL entries for narrative. No new companion-changelog files.

**Acceptance rubric (session 46):** Reference files are a new artifact kind. Acceptance criteria:
- **Accept if:** composition pointers resolve; definition is terse (≤ 1 paragraph); variants are used only when a term has genuinely distinct referents; Librarian read rule is stated.
- **Reject if:** file duplicates guide content (should be pointers); file is a synthesis product (use a guide or view instead); concept has no observed consumer query pattern (don't speculate).

**Librarian use-case registry (Stream B.1):** Reshaped. Each of the 35 use cases maps to a (concept, operation) pair — e.g., "audit my agent.md" → (concept: agent, operation: audit). Registry becomes the primary evidence base for which concept/operation files to author first.

**Librarian read-contract design (Stream B.2):** Absorbs α' directly. Librarian's read shape becomes:
1. Parse consumer query into verb + noun(s).
2. Load operation file for the verb (if exists; else runtime aggregation per operation defaults).
3. Load concept file(s) for the noun(s) (if exists; else runtime aggregation per concept defaults).
4. Compose: operation's procedure × concept's composition pointers → targeted Tier-1 reads.
5. On depth signal, escalate to Tier 2 or Tier 3 per the concept/operation file's escalation rules.

**Assessment skill designs (Stream B.3):** Become thin wrappers. Each skill does:
1. Receive consumer input (the artifact being assessed).
2. Load `audit.md` + concept file (e.g., `agent.md`).
3. Apply operation's procedure with concept's composition pointers.
4. Produce output per operation's output shape.

Intelligence lives in the operation + concept files, not in the skill prose. Skills are load-and-apply.

---

## Proposed New DDs (if Option α' is accepted)

Titles only. Nick gates filing. These slot into the lifecycle-spec + acceptance-rubric + collapse-proposal bundle.

1. **DD-NEW-REF-1: Librarian reference layer.** Define `operations/references/librarian/` directory, concept and operation file types, frontmatter schema (`type: concept | operation`, `term | operation`, `variants: []`). Establishes the pointer-file substrate as a first-class artifact form.
2. **DD-NEW-REF-2: Three-tier access model.** Codify Tier 1 (guides) / Tier 2 (patterns + findings graph) / Tier 3 (watched-library repos) as Librarian's read-contract substrate. Each tier has read-escalation signals and cost/precision profiles.
3. **DD-NEW-REF-3: Reference file acceptance criteria.** Per file type (concept vs operation). Composition pointers must resolve; duplication of guide content rejected; variants only when load-bearing.
4. **DD-NEW-REF-4: Dimension registry reframe.** Rename Agentic OS → Agentic Systems. Rewrite `research-dimensions.md` preamble to make Researcher-specificity explicit. Harness is not a dimension (it's a Librarian concept file).
5. **Retained for possible future activation (from v1's α):** view-artifact DDs. Not filed yet. Triggered only if Contract sections prove insufficient for composition and curated rubrics become necessary.

---

## What This Audit Does NOT Resolve

- **Validation of Option α'.** Whether Contract invariants across the relevant guides actually compose into coherent audit rubrics is an empirical claim. Spot-check deferred to session 48 — read `{G1, G2, G10}` Contract sections and test composition against a sample agent.md. If insufficient, escalate to Option α (view artifacts) for curated rubrics.
- **Full use-case registry mapping.** Stream B.1 work — map the 35 session-46 use cases onto (concept, operation) pairs.
- **Read-contract details per tier.** Stream B.2 — formal read-escalation rules, confidence-disclosure protocol, provenance surfacing.
- **Per-assessment-skill specifications.** Stream B.3 — assess-prompt, assess-agent, assess-skill.
- **References-by-agent reorg.** Current `operations/references/` contains files owned by different agents (dimensions → Researcher; form-classification-rubric → Codifier; guide-routing-table → shared). The `librarian/` subfolder introduced here is the first agent-scoped subdirectory. Mirror moves for Researcher + Codifier plus skill path updates are a genuine IB item. Flagged for session 48+ scope.
- **Finding-graph tooling at Tier 2.** Traversing `related_findings` edges is currently manual (grep). A small tool or skill for "expand this finding's neighbors" might be useful — deferred.
- **Historical pattern inventory.** 72 pattern extracts are orthogonal. Acceptance rubric DD-X11 + collapse proposal handle them.

---

## Open Questions for Nick (revised in v2)

Most of v1's open questions were resolved during the 2026-04-21 interview. Remaining:

1. **Spot-check outcome (session 48).** If Contract sections compose cleanly into an agent-audit rubric: proceed with pure α'. If not: escalate to α (view artifacts) for the assessment use case specifically. Any red lines on either outcome?
2. **References-by-agent reorg timing.** Do you want this as a standalone IB for session 48, or folded into the post-α'-adoption work in session 49+?
3. **Terminology — "Codifier" vs. "Curator."** You referenced the "curator" agent; current 4-agent architecture (DD-82) names it "Codifier." Confirming it's a speech-ism, not a rename proposal.

Resolved during interview (for the record):
- ~~Accept α or redirect?~~ → α' (lighter variant)
- ~~Dimensions reframe — two-axis or reframe-only?~~ → Reframe-only; Agentic OS → Agentic Systems; no Harness dimension
- ~~View residence?~~ → N/A under α'
- ~~View synthesis skill?~~ → N/A under α'
- ~~Consumer artifacts framing?~~ → Dropped; replaced by (concept, operation) decomposition
- ~~Variants as concept-file field?~~ → Confirmed for Agent, Memory, Second Brain
- ~~Reference file directory?~~ → `operations/references/librarian/`

---

## Cross-References

- Pipeline collapse proposal (write-side; Librarian Read Contract section to be trimmed in this session's minimum-coherent close): `project-management/design-notes/2026-04-20-pipeline-collapse-proposal.md`
- Lifecycle spec (artifact-state mechanics): `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- Acceptance rubric (write-time gate): `project-management/design-notes/2026-04-20-artifact-acceptance-rubric.md`
- Guide routing table (dimension → guide mapping): `operations/references/guide-routing-table.md`
- Research dimensions registry (intake taxonomy; rewrite deferred to session 48): `operations/references/research-dimensions.md`
- Form classification rubric (producer-side, unchanged): `operations/references/form-classification-rubric.md`
- Librarian agent definition (role description may update post-α'): `agents/librarian/agent.md`
- Governing DDs:
  - DD-77 (single-form classification) — unchanged
  - DD-78 (ContractSpec) — **Contract invariants now load-bearing as emergent audit criteria under α'**; DD-78 framing may need amendment to reflect dual role
  - DD-80 (pipeline simplification) — unchanged by this audit
  - DD-81 (pattern filter) — unchanged by this audit
  - DD-82 (IL 4-agent architecture) — **Librarian role expands** to include reference-layer maintenance and three-tier access; may warrant DD amendment
  - DD-86 (Owner responsibility) — unchanged
