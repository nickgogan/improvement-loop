---
term: harness
type: concept
variants: []
target_system:
  - "improvement-loop"
created: "2026-06-15"
updated: "2026-06-15"
author: "claude"
stage: "draft"
tags:
  - "harness"
  - "construction"
  - "metasystem-concept"
  - "rule-11"
  - "rule-12"
aliases:
  - "Harness spec"
  - "Whole-system harness"
---

# Harness (MetaSystem concept)

## Short definition

A **harness** is the whole-system shape MetaSystem authors and audits: a folder (or set of folders) that composes one or more agentic artifacts (skills, agents, prompts) into a coherent runtime that a consumer points at, deploys into, or runs. The harness is the unit `/audit-artifacts` audits and the unit `/design-harness` constructs.

Examples in scope: a system following the fractal-unit pattern (DD-52) with `.claude/skills/`, `agents/`, governance docs; a CLI tool packaging skills + agents; the sizing-engine pilot's three-system comparison + forecasting layer.

The harness is the **whole**; skills/agents/prompts are the **parts**. Per the consumer-abstractions-map split: MetaSystem owns the harness shape; IL owns the skill/agent/prompt shapes. This concept doc is MetaSystem's authored substrate for **constructing** harnesses.

## Not to be confused with

| Not (MetaSystem-)harness | What it is instead |
|---|---|
| **IL runtime-harness concept** (`librarian/harness.md`) | The runtime + tooling surface an *agent* operates inside (Claude Code CLI, Cursor, the API). That is the audit-time lens IL maintains. MetaSystem's harness is the authored whole-system; the two senses are adjacent but distinct. See §Composition for how they connect. |
| **Skill / agent / prompt** | A part of a harness, not a harness. IL owns these. |
| **System (PARA "Areas")** | A persistent organizational space (e.g., `systems/improvement-loop/`). A system may contain one or many harnesses; a harness is the construction unit, not the organizational unit. |
| **Composition layer** | The *pattern* whereby a MetaSystem operation composes IL operations. `/audit-artifacts` instantiates the composition layer; the harness is what the composition operates on. |
| **Codebase** | A harness is the agentic shape; the codebase is what underlies it. `/audit-artifacts` is a harness audit, not a code review (see `/code-review`, `/security-review`). |

## Composition

This concept doc is **primarily §Construction**. §Composition (the audit-time substrate — which IL guides fire on harness aspects) is maintained by IL in `librarian/harness.md` and is read by `/audit-artifacts` indirectly (via the per-artifact dispatches to `/assess-*`).

| Aspect | Owned by | Where to read |
|---|---|---|
| Per-artifact audit substrate (which IL guides apply to each skill/agent/prompt) | IL | `systems/improvement-loop/operations/references/librarian/skill.md`, `agent.md`, `prompt.md` §Composition |
| Runtime-harness audit substrate (tool loading, context, permissions, hooks) | IL | `systems/improvement-loop/operations/references/librarian/harness.md` §Composition |
| **Whole-system harness construction** (this doc) | **MetaSystem** | §Construction below |
| Whole-system harness invariants (what `/audit-artifacts` checks beyond per-artifact dispatch) | MetaSystem | `/audit-artifacts` design contract §"Whole-system invariants" — **empty in v1 per rule 11**; candidates listed there |

When a consumer asks "audit this harness" the dispatch is per-artifact (IL `/assess-*`). When a consumer asks "construct a harness" the dispatch is the §Construction Decision sequence below.

## Construction

Author-time substrate for `/design-harness` (queued — cross-system roadmap step G) and for any operation that constructs a new harness spec. Audit-time operations consume the symmetric gates in inspection mode (see §"Rule-12 audit/design symmetry verification").

### Decision sequence

Ordered steps the author works through before drafting. Each step bounds a downstream authoring choice — skipping a step does not skip the decision, only the deliberation.

1. **Name the harness's bounded operation.** A harness packages one whole-system operation. State it as a noun-phrase ("MongoDB sizing comparison engine across SAGE + Excel calculator + consulting tool") or a verb-phrase ("audit an agentic system at a local path"). If you cannot state the operation without naming two end-shapes (e.g., "audits *and* designs"), the scope is two harnesses with rule-10 binding, not one harness — see step 6.

2. **Identify the consumer demand and audience archetypes.** Write the concrete consumer phrasings that should invoke this harness. Name which of the audience archetypes 1–5 are served and how. A harness with single-archetype demand and no recurrence is rule-11 weak — defer or scope smaller.

3. **Enumerate the owned abstractions.** List which IL-maintained artifacts (skill, agent, prompt) this harness will ship or compose. Each shape adds an audit/design dispatch. Use the consumer-abstractions-map's split as the inventory:

   | Artifact | If shipped by this harness | Dispatch (audit) | Dispatch (design) |
   |---|---|---|---|
   | SKILL.md | counts in `/audit-artifacts` discovery | `/assess-skill` | `/design-skill` |
   | agent.md / CLAUDE.md (agent-disposition) | counts | `/assess-agent` (variant inferred or passed) | `/design-agent` |
   | Standalone prompt | counts | `/assess-prompt` | (no IL `/design-prompt` yet — see IL map weak-demand row) |
   | CLAUDE.md (MOC / orientation) | discovered, filtered out by MOC pre-filter | n/a | n/a |

   Record the artifact count and shape mix. This is the input to the bin-packing step `/audit-artifacts` will run (see SKILL.md §"Sizing" / §"Bin packing").

4. **Run the Safety-critical classification.** Apply this gate — analogous to the per-skill G9.I6 gate but at the harness level.

   A harness is **safety-critical** if **any** of:
   - It ships one or more safety-critical skills (any skill with destructive `allowed-tools` or destructive procedure steps — see IL `librarian/skill.md` §"Decision sequence" step 4).
   - Its whole-system operation performs cross-system writes, deployments, or credential manipulation.
   - It composes outputs that feed automated downstream actions without human review.
   - Its `/design-*` peer will instantiate destructive artifacts on consumer systems.

   Per rule-10/G9.I6 at the harness level: a safety-critical harness must encode HITL gating in its composition (confirm-before-act, dry-run mode, conversation-only default with explicit `--write` opt-in). `/audit-artifacts` ships this discipline: `--write` is off by default; safety-critical action requires consumer opt-in. Authoring a safety-critical harness without HITL gating produces a harness that will fail audit on first whole-system inspection.

5. **Specify the assessor binding (rule 10 — generator-assessor separation).** Every harness must have a paired assessor. Two cases:
   - **This harness is an assessor.** (Example: `/audit-artifacts`.) Then it cannot also be the constructor for the same shape. Its constructive peer is a separate `/design-*` harness (rule 10).
   - **This harness is a constructor.** (Example: `/design-harness` when shipped.) Then it must delegate quality assessment to a separate assessor in fresh context (rule 10). For `/design-harness` the delegate is `/audit-artifacts`.
   - **This harness is neither assessor nor constructor** (e.g., a pilot domain harness like the sizing engine). Then rule 10 applies inwardly: any safety-critical skill it ships must have HITL gating; any constructive operation it internally performs must delegate quality assessment per IL rule 10 at the per-artifact level.

6. **Specify the constructive-peer binding (rule 12 — audit/design symmetry).** Per rule 12, an abstraction that supports audit but not construction (or vice versa) is in symmetric debt — auditable-but-not-constructible (or the inverse). At the harness level this means:
   - If this harness is an assessor (`/audit-artifacts`), its rule-12 peer is `/design-harness`. The peer must exist or be on the committed roadmap.
   - If this harness is a constructor (`/design-harness`), its rule-12 peer is `/audit-artifacts`. Same.
   - If this harness is neither, the binding does not apply at the harness level — only at the per-artifact level (skills inside the harness still owe their own audit/design symmetry to IL).

   This step is a **hard gate** for assessor/constructor harnesses. Shipping an assessor without a queued constructor (or vice versa) leaves coverage asymmetric.

7. **Cross-check against §Composition.** Confirm the IL substrate the harness will be audited against matches the surface authored. If the harness ships no skills, `/assess-skill` will never fire — the harness should not advertise skill-aware operation. If the harness ships agents with no embedded tool directives, G5 substrate won't fire (Variant A path). Mismatches mean the Decision record over- or under-specifies the surface.

### Template skeleton

The minimum valid harness spec shape. Fill in placeholders; do not delete required sections. A harness spec lives as a **design contract** in `systems/improvement-loop/project-management/design-notes/<date>-<name>-design-contract.md` (current placement; see priority-queue item 6 for the placement-debate gate). The corresponding SKILL.md (if the harness is implemented as a slash command) lives in `.claude/skills/<name>/SKILL.md`.

```markdown
---
title: "<harness-name> Design Contract"
id: "<harness-name>-design-contract"
type: "design-note"
category: "capability-design"
target_system:
  - "meta-system"
stage: "draft"   # draft → stable-after-pilot → stable
created: "<YYYY-MM-DD>"
updated: "<YYYY-MM-DD>"
author: "<owner | claude>"
tags: ["design-note", "<harness-name>", "harness"]
---

# `<harness-name>` Design Contract

## Plain-English purpose
<One-paragraph "point this at X, get Y" statement. State the bounded operation from Decision sequence step 1.>

## Why MetaSystem owns this (vs. IL)
<State which whole-system shape this harness composes. Reference the consumer-abstractions-map split.>

## Input contract
<Table of inputs: required path/args + optional flags + defaults. Mirror /audit-artifacts's shape.>

## Discovery / composition contract
<For audit harnesses: discovery rules + shape table. For design harnesses: substrate-load order + interview surface. For domain harnesses (e.g., sizing engine): the adapter / data-source contract.>

## Owned abstractions
<List per Decision-sequence step 3: which artifacts ship, what shapes they take, which IL dispatches apply.>

## Safety-critical classification
<Yes/No per Decision-sequence step 4. If Yes: name the HITL gate.>

## Assessor binding (rule 10)
<Name the paired assessor (or "this harness IS the assessor; constructive peer is <name>"). Per Decision-sequence step 5.>

## Constructive-peer binding (rule 12)
<Name the paired constructor (or "this harness IS the constructor; assessor peer is <name>"). Per Decision-sequence step 6. State whether the peer ships, is queued, or is N/A for non-assessor/non-constructor harnesses.>

## Output contract
<For audit harnesses: three artifacts (manifest, per-artifact findings, summary). For design harnesses: drafted artifact + delegated audit report. For domain harnesses: the consumer-visible deliverables.>

## Boundaries
<What this harness does NOT do. List adjacent operations explicitly and point to the harness that does them.>

## Whole-system invariants
<v1 default: empty per rule 11; candidates listed for future commit.>

## Audience archetypes (1–5)
<Which archetypes consume which outputs, at what depth.>

## Cross-references
<Pointers to IL substrate composed, related harnesses, and the consumer-abstractions-map row.>
```

A harness spec missing any of `Plain-English purpose`, `Input contract`, `Owned abstractions`, `Safety-critical classification`, `Assessor binding`, `Constructive-peer binding`, `Output contract`, or `Boundaries` is not a complete harness — `/design-harness` (when shipped) will refuse to consider the spec stable, and `/audit-artifacts` of a folder built from such a spec will surface the gaps as structural-incompleteness findings.

### Scoping heuristics

When in doubt, prefer the smaller harness plus explicit composition over the larger one with internal branching.

- **Split when:** the harness has two distinct whole-system end-shapes (e.g., a single harness that both audits *and* designs the same shape — split per rule-10 precedent). A second sign: the Plain-English purpose statement needs "and" connecting two operations with different output shapes.
- **Collapse when:** the proposed "harness" is a single skill with no whole-system composition — it should be a SKILL.md inside an existing harness, not a new harness.
- **Stay one harness when:** the operation has multiple input modes but the same whole-system end-shape (e.g., `/audit-artifacts <path>` vs. `/audit-artifacts <path> --diff <prior>` — same operation, same output shape, one mode-flag).
- **Layer when:** two operations build on each other and share substrate (sizing-engine evidence: forecasting layered on top of comparison). The layered operation may be a separate harness that takes the underlying harness's output as input — this is the **multi-surface composition** pattern. Author the underlying harness first; layer the second after the first is stable.

### Authoring-time anti-patterns

Mistakes made while writing the harness spec. Distinct from `/audit-artifacts`'s structural findings, which surface at audit time after the harness has artifacts authored.

- **Assessor/constructor conflation.** Authoring a single harness that both produces and assesses the same artifact shape. Rule-10 violation by construction. Split.
- **Composition without composition cross-check.** Authoring "this harness ships skills" without listing which `/assess-skill` invariants will fire on those skills. Audit-time surprises = construction-time omissions.
- **Premature whole-system invariants.** Adding harness-level invariants beyond IL `/assess-*` composition before 2–3+ concrete instances surface. Rule-11 violation. v1 default is empty.
- **Safety-critical classification skipped.** Writing the input/output contract first and leaving safety-critical "for review". Inverts the safety envelope. Run the classification before procedure detail.
- **Constructive-peer omission.** Shipping an assessor harness without a queued or shipped constructive peer. Leaves rule-12 coverage asymmetric. Either queue the peer or downgrade scope.
- **Multi-surface composition collapsed.** Authoring a single harness that layers forecasting on comparison rather than separating them. Hides the substrate-sharing contract; obscures the comparison's reusability. Layer instead.
- **Deviation-semantics omitted (comparison harnesses).** For multi-system comparison harnesses (sizing-engine class), failing to specify the deviation semantics (empirical vs theoretical, surface both with labels, whose value is "ground truth") before procedure detail. The deviation contract is load-bearing for downstream forecasting layers. Specify it in §"Discovery / composition contract."

### Composition cross-check (rule 12 binding)

At Decision-sequence step 7, walk these checks before declaring the spec stable:

1. **For every shape the harness ships, the matching IL substrate exists.** Skills → IL `librarian/skill.md` §Construction + §Composition. Agents → IL `librarian/agent.md`. Prompts → IL `librarian/prompt.md` §Composition (note: §Construction not committed in IL — see IL map "moderate demand" row). If a shape is shipped without IL substrate, file an IB item to IL or scope the harness without that shape.
2. **Assessor and constructor halves are both committed.** Per rule 12, the abstraction (here: harness) cannot be audit-only or design-only without filing the gap as debt. `/audit-artifacts` shipped (audit half); `/design-harness` queued (design half) — symmetric.
3. **Whole-system invariants the harness adds are evidence-backed.** Empty v1 is the rule-11 default. Any added invariant must cite ≥2–3 concrete instances of the invariant being needed across audited harnesses.

## Rule-12 audit/design symmetry verification

Walk every `/audit-artifacts` invariant and confirm §Construction tells the builder how to satisfy it. This is the rule-12 self-check; failures surface §Construction gaps to backfill.

| `/audit-artifacts` check (audit-time) | §Construction satisfier (design-time) | Symmetric? |
|---|---|---|
| Discovery by shape-based glob (skills, agents, prompts, CLAUDE.md) | Decision-sequence step 3 enumerates the owned abstractions and shape mix; Template skeleton §"Owned abstractions" captures it | ✅ |
| MOC pre-filter on CLAUDE.md (frontmatter `type: index` OR word count <100) | Implicit: a constructor authoring a CLAUDE.md classifies it at author time as MOC vs agent-disposition. Authoring-time anti-pattern: "MOC drift" (writing an agent-disposition CLAUDE.md that decays to MOC shape) — **gap surfaced; add to Authoring-time anti-patterns in a future commit if recurrence appears** | ⚠ partial |
| Bin packing under 250k token ceiling | Decision-sequence step 3 records artifact count and shape mix; sizing constants (`{skill: 18k, agent-A: 22k, agent-B: 32k, agent-C: 28k, prompt: 20k}`) are audit-time mechanics, not author-time gates. Author concern: don't ship a single artifact so large it forces an oversized bin. **Soft signal only; no Decision-sequence gate** | ✅ (no design-time obligation; audit-time mechanic) |
| `/assess-skill` dispatch per discovered skill | Decision-sequence step 3 lists `/assess-skill` as the audit dispatch for ship-shape SKILL.md | ✅ |
| `/assess-agent` dispatch per discovered agent (variant-aware) | Same — Decision-sequence step 3 names the dispatch and variant inference | ✅ |
| `/assess-prompt` dispatch per discovered prompt | Same | ✅ |
| Per-artifact safety-critical classification (G9.I6 firing on destructive skills) | Decision-sequence step 4 runs Safety-critical classification at the harness level; each shipped safety-critical skill inherits the gate via IL substrate | ✅ |
| Whole-system summary synthesis (at-a-glance + critical findings + common findings + invariants) | Template skeleton §"Output contract" requires the harness to specify output shape; audit harnesses' shape mirrors `/audit-artifacts`'s three artifacts | ✅ |
| `--write` default-off (G9.I6 mitigation: conversation-only safe default) | Decision-sequence step 4 Safety-critical classification mandates HITL gating; Template skeleton §"Safety-critical classification" names the gate | ✅ |
| Audit-trail one-line append to `operations/artifact-audits/runs.md` on `--write` | No symmetric design-time gate (mechanic of audit-time writes); construction-time concern is "the harness writes are reversible and audit-trail-emitting" — captured under safety-critical HITL gating | ✅ |
| Discovery records structural gaps (e.g., `agents/` present but empty) | Decision-sequence step 7 cross-check against §Composition surfaces shape/surface mismatches at design time | ✅ (mostly; the empty-folder case is audit-only signal) |
| Manifest's `## Ambiguous classifications` block | Author-time concern: CLAUDE.md placement should disambiguate intent (agent-disposition vs MOC). Captured implicitly under Template skeleton §"Owned abstractions"; could be sharpened in a future commit | ⚠ partial |
| Whole-system invariants (v1: empty; candidates pending recurrence) | §Construction §"Composition cross-check" check 3 enforces rule-11 evidence gating on added invariants | ✅ |
| Engine subagent discoverability (planned candidate) | No symmetric design-time gate yet — would be added when whole-system invariant is committed | N/A (deferred symmetrically) |

**Verdict:** Rule-12 symmetry is **substantially satisfied** by this §Construction draft. Two partial gaps surfaced (MOC drift anti-pattern; ambiguous-CLAUDE.md author-time disambiguation) — both are speculative recurrence triggers, not committed scope. Per rule 11, defer adding the explicit anti-patterns until 2–3 concrete authoring instances surface MOC drift or CLAUDE.md ambiguity at *design* time. The current substrate is sufficient to seed `/design-harness`.

## Provenance surfacing

`/design-harness` (when shipped) will cite this concept doc by section anchor and IL substrate by file path. The audit-time substrate composed via `/audit-artifacts` cites IL `librarian/*.md` per IL convention.

## Cross-references

- MetaSystem consumer-abstractions-map: `systems/improvement-loop/knowledge/reference/consumer-abstractions-map.md`
- `/audit-artifacts` SKILL.md (the audit half of the harness-level pair): `systems/improvement-loop/.claude/skills/audit-artifacts/SKILL.md`
- `/audit-artifacts` design contract: `systems/improvement-loop/project-management/design-notes/2026-06-12-audit-system-design-contract.md`
- IL runtime-harness concept (§Composition substrate): `systems/improvement-loop/operations/references/librarian/harness.md`
- IL skill concept (§Construction reference shape this doc parallels): `systems/improvement-loop/operations/references/librarian/skill.md`
- IL design operation spec (Phase model for §Construction consumers): `systems/improvement-loop/operations/references/librarian/design.md`
- IL rules 10/11/12: `systems/improvement-loop/governance/agent-rules.md`
- Cross-system roadmap step G + sizing-engine pilot (priority-queue items 1, 5): workspace `PROGRESS.md`
