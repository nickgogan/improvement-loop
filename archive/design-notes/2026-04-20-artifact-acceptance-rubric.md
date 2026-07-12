---
title: "Artifact Acceptance Rubric — What IL Should Produce"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-20"
updated: "2026-04-20"
author: "claude"
stage: "draft"
source_dd:
  - "DD-77"
  - "DD-78"
  - "DD-80"
  - "DD-81"
  - "DD-82"
tags:
  - "design-note"
  - "acceptance-rubric"
  - "librarian"
  - "proposal"
aliases:
  - "What IL accepts"
  - "Artifact acceptance criteria"
---

# Artifact Acceptance Rubric

**Status:** Design proposal. Companion to `2026-04-20-artifact-lifecycle-spec.md`. The lifecycle spec answers *what happens to artifacts that exist*; this rubric answers *which artifacts should exist at all*.

## Framing

The IL's value to humans is mediated by the Librarian. Every artifact the IL produces is judged by one question: **does this make the Librarian more useful on the consumer queries Nick cares about?**

Those queries reduce to four shapes:

| Query shape | Example |
|-------------|---------|
| Advice | "How should I build X?" / "What's the current best practice on Y?" |
| Reference | "What does the research say about context rot?" |
| Concrete scaffold | "Give me a template for an agent.md" |
| Audit | "Is my agent.md / skill / config missing anything?" |

The grounding substrate is the KB (findings, authorities, cross-links) plus cached GitHub repos via watched-libraries. An artifact that doesn't make those four query shapes land better is not worth staging, extracting, or maintaining.

## Consumption Mode per Form

Consumption mode — *how* the consumer uses an artifact — is not uniform across forms. This is the missing lens that explains why "extract everything" is wrong:

| Form | Consumption mode | What Librarian does with it |
|------|------------------|-----------------------------|
| Guide | **Read** (end-directed advice) | Surfaces the relevant guide to answer "how do I do X" |
| Template | **Copy + edit** (direct scaffold) | Returns the template with `{{VAR}}` slots for the consumer to fill |
| Rule | **Grep + enforce** (audit constraint) | Greps the consumer's artifact against the rule set; flags violations |
| Pattern | **Cite** (rationale / reference) | Quoted/linked to explain *why* a guide recommends something |
| Skill | **Adapt** (transferable procedure) | Shown as a concrete example for consumers building similar procedures in their own harness |
| Agent | **Adapt** (transferable persona) | Shown as a concrete example for consumers designing similar agents in their own stack |

Three broad categories emerge:
- **Deploy-ready** (template, rule): consumer lifts and uses directly
- **Read/cite** (guide, pattern): consumer reads through Librarian narrative
- **Reference/adapt** (skill, agent): consumer studies and rebuilds in their own context

Acceptance criteria differ by category. A rule has to be *enforceable*; a pattern has to be *citable*; a skill has to be *transferable*.

---

## Value Hierarchy

In descending order of consumer value:

| Rank | Form | Consumer value | Production priority |
|------|------|----------------|---------------------|
| 1 | Guide | Primary deliverable; where advice lives | High — extract aggressively when clusters form |
| 2 | Template | Direct consumption; concrete hand-off | High — extract when a reusable scaffold is identified |
| 3 | Rule | Audit surface; governance | Medium — extract when finding describes an enforceable binary constraint |
| 4 | Pattern | Rationale layer; Librarian-internal | Low as standalone; High as inline section of a guide |
| 5 | Skill | Reference example for consumer building similar procedures | Low — extract only if pattern is transferable across harnesses |
| 6 | Agent | Reference example for consumer designing similar personas | Very low — extract only on explicit Nick decision |

Note: **skills and agents rank below patterns** for consumer value, even though the pipeline currently extracts them aggressively. Most skills/agents in a finding are reference documentation of what *someone else built* — not deploy-ready infrastructure for our consumers. Rationale patterns are more universally useful to Librarian.

---

## Per-Form Acceptance Criteria

### Guide — Accept if

- Answers a coherent practitioner question (one of the Guide Clusters in the routing table)
- Has 3+ source findings (single-finding guides are patterns in disguise)
- Includes at least one fillable template and one worked example (per `/synthesize-guide` Step 2)
- Carries a ContractSpec (DD-78)

### Guide — Reject if

- Fewer than 3 findings (insufficient substrate)
- Covers >2 distinct practitioner questions (should split)
- Would duplicate content in an existing guide without meaningfully different practitioner framing

### Template — Accept if

- Has ≥1 named `{{VAR}}` slot AND a fillable body
- Generic enough that the consumer fills variables without rewriting the body
- Variation axis is explicit (what changes between renderings: host, system, project, model vendor, etc.)
- Consumer can lift the file, edit variables, and use it without reading the source finding

### Template — Reject if

- Is a worked example dressed as a template (all slots are pre-filled)
- Is so abstract the variables have no defaults or examples
- Is really a pattern ("here's how to *think* about the structure")
- Tightly coupled to source author's specific tooling without a portable backbone

### Rule — Accept if

- Expressible as a deterministic check (regex, enum, cardinality, format, presence/absence)
- Has a named enforcement boundary (tool call, commit, session start, pre-deploy, output format, etc.)
- Binary pass/fail — no graded or advisory language
- Captures an anti-pattern cleanly ("never do X; reason Y") where X is observable

### Rule — Reject if

- Requires judgment to evaluate (then it's a pattern, not a rule)
- Has no enforcement boundary (a "rule" nobody can check is a norm, not a rule)
- Duplicates an existing rule's constraint (should extend, not create new — see lifecycle spec DD-X7)
- Describes scaling/tuning guidance (heuristics are patterns)

### Pattern — Accept if

- **Inline in a guide** (default): every pattern-classified finding feeds into its target guide's body with a named anchor. The pattern is citable via `guide-name.md#pattern-anchor`.
- **Standalone as `extracts/patterns/` file** (exception): only when the pattern is cited by ≥2 guides or is referenced by a Librarian-facing rationale outside any single guide's scope. Examples: `programmatic-tool-calling` (cross-cuts tool design, skill architecture, walkthrough generation) deserves standalone status.

### Pattern — Reject as standalone if

- Only cited by one guide (belongs inline in that guide)
- Duplicates content already present in the guide that routes it
- Is actually a rule/template/skill/agent misclassified as pattern

### Skill — Accept if

- The procedure is **transferable** — consumer can implement an analogous skill in their harness by adapting the structure
- Inputs/outputs are specified generically (not hard-coded to source author's file paths, tool names, or vendor APIs)
- Includes at least one failure mode section (signals the author thought about the skill as an operation, not just a one-off)
- Represents a recurring skill shape, not a one-off implementation

### Skill — Reject if

- Tightly coupled to source-author's custom infrastructure (consumer can't adapt without also adopting the infra)
- Really a pattern or template in skill-shaped clothing (center of gravity is the framework, not the procedure)
- Consumer would realistically rebuild from scratch rather than adapt — reference value is low
- Is IL-internal infrastructure (belongs in `agents/codifier/` or `.claude/skills/`, not in `extracts/`)

### Agent — Accept if

- The disposition is **transferable** — consumer can instantiate a similar role with their own stack
- "How it thinks" is the most important part of the entry, not what it runs on
- Explicit scope, handoff contract, and recovery model (reads like a job description, not a deployment)

### Agent — Reject if

- Auto-created without Nick's explicit approval (agent extraction is system-level per DD-82)
- Persona is tied to specific tools/vendors (consumer can't adapt)
- Is really multiple roles (then it's a pattern per DD-76)
- Would introduce an agent class that conflicts with existing MetaSystem agent definitions (Owner / Researcher / Codifier / Librarian)

---

## Audit of Current `extracts/` Against This Rubric

Present state, judged against the rubric. This is a **diagnostic**, not a mandate — decisions on what to retire, rewrite, or keep belong to Nick.

| Form | Count | Accept under rubric | Likely reject | Notes |
|------|-------|---------------------|---------------|-------|
| Guide | 11 | ~11 | 0 | All cover coherent practitioner questions with 5+ findings each. No known rejections. |
| Template | 4 | ~4 | 0 | All have `{{VAR}}` slots and fillable bodies. Small, clean set. |
| Rule | 9 | ~8 | ~1 | Mostly clean; one candidate for re-review is `balanced-positive-negative-eval-sets.md` (check if heuristic vs. enforceable). Spot check needed. |
| Pattern | 72 | Uncertain — most should fold inline | Many standalone | Under the rubric's default ("inline in target guide"), most would retire once guides reach stable state. Keeping standalone status should require justification per pattern. |
| Skill | 11 | ~4–6 | ~5–7 | Need per-file review for transferability. Some (e.g., `deep-plan-four-agent-pipeline`, `thinking-models-mental-framework-commands`) look transferable. Others (`stupid-button-token-audit-diagnostic`, `multi-agent-proportional-content-summarization`) may be specific enough that consumer value is low. |
| Agent | 2 | 2 | 0 | `qa-agent-independent-compliance-review` (Quinn) and `initializer-agent-scaffolding` — both have transferable dispositions. Clean keep. |

### Headline observations

1. **The 72 pattern extracts are the elephant.** Under the rubric, most should fold into their target guide inline and retire as standalone files. Exception: cross-cutting patterns cited by ≥2 guides (≈10–15 of the 72, pending audit). Retiring the rest would make `extracts/patterns/` lighter by ~80% without losing content (it's all captured in guides).

2. **The 11 skill extracts are mixed.** Half look transferable; half look tightly coupled to source-author specifics. A per-file review under the skill acceptance criteria would likely retire ~5.

3. **Rules, templates, agents, guides are already well-disciplined.** The existing DD-80/DD-81 pipeline has been doing this correctly — the audit's action items are mostly historical cleanup, not pipeline changes.

4. **The `extracts/` directory, post-audit, would likely shrink from ~109 artifacts to ~30–40.** Most of the loss is pattern-inline-with-guide absorption, not content loss.

---

## Implications for the Pipeline

### `/identify-artifacts` — No Change

Classification is unchanged. Findings still route to their primary form. The rubric applies downstream.

### `/synthesize-guide` — Absorb Patterns Inline

Under this rubric, the default behavior when synthesizing is to embed pattern content inline with anchor IDs. Standalone pattern extraction only happens when an external trigger fires (pattern cited by ≥2 guides; Librarian-side citation beyond any guide). This aligns with DD-81 ("patterns route to guide synthesis, not individual extraction") and tightens it: patterns should not be standalone-extracted *at all* unless the cross-guide criterion fires.

### `/extract-artifacts` — Apply Per-Form Acceptance Gate

Add a gate step after the current pattern filter: for each approved non-pattern finding, run the form-specific acceptance criteria. If the finding fails the criteria, surface as "rejected under acceptance rubric" with the failed criterion named. Nick overrides by re-marking APPROVED with a `--force` flag or equivalent. This makes the rubric operational at extraction time.

### `/extract-artifacts` — Harvest Queue (from revised DD-X9)

The co-occurrence harvest queue — the revised DD-X9 mechanism we discussed — feeds the same acceptance gate. Embedded templates in pattern bodies pass the rubric if they have named variables and a fillable body. Embedded skills fail the rubric if they're not transferable. Embedded rules pass if they have an enforceable boundary.

### Librarian — Primary Consumer

The Librarian queries `extracts/` (and eventually the deployed `meta-system/knowledge/` locations). The rubric is what ensures everything Librarian finds is worth returning to the consumer. The rubric is implicitly the Librarian's quality contract.

---

## Proposed DDs (Additions to Lifecycle Spec's DD Bundle)

These complement DD-X1 through DD-X9 in the lifecycle spec. Titles only; not filing this session.

- **DD-X10: Artifact acceptance rubric — per-form criteria.** Codifies the criteria above as the Codifier's gate at extraction time.
- **DD-X11: Patterns default to inline, not standalone.** Standalone pattern extraction requires ≥2 guide citations or explicit Nick approval. Default `/synthesize-guide` behavior embeds patterns in the guide body with anchor IDs.
- **DD-X12: Retroactive audit and retirement.** `/extract-artifacts --audit` mode runs the acceptance rubric against existing `extracts/` and produces a retirement proposal. Nick gates per-artifact.

---

## Open Questions for Nick

1. **On the 72 pattern extracts:** do you want a retroactive audit now, or defer until guides are more stable?
2. **On skill acceptance:** is "transferable" the right criterion, or are you okay keeping all source-specific skills as "here's how X built it" references for comparison value?
3. **On Librarian coupling:** should the acceptance rubric be owned by the Librarian agent (as a read-side quality contract) or by the Codifier (as a write-side production gate)? DD-86 suggests Codifier owns production, but rubric shape is inseparable from Librarian's needs.
4. **On pattern inlining:** if patterns become inline sections, how does Librarian cite them? Anchor IDs require guide stability. Proposal: `guide-name.md#pattern-slug` as the citation shape, stable across re-syntheses via preserved anchors.
5. **On "IL-internal skills" mis-filed:** should we sweep `extracts/skills/` for anything that's really IL infrastructure and move it to `agents/codifier/`? Or is everything there genuinely consumer-reference?

---

## Relationship to the Lifecycle Spec

The lifecycle spec says: *here's what happens to artifacts at every stage — merge, create, change-log.*

This rubric says: *here's which artifacts should exist in the first place, judged against Librarian consumption modes.*

They're designed to work together:
- Acceptance rubric = write-time gate (what enters staging)
- Lifecycle spec = post-write mechanics (what happens to things that entered)

Together they bound the IL's production surface.

---

## Cross-References

- Lifecycle spec: `project-management/design-notes/2026-04-20-artifact-lifecycle-spec.md`
- Identification report (session 45): `operations/pattern-identification-reports/2026-04-20-session-45-identification-report.md`
- Form classification rubric: `operations/references/form-classification-rubric.md`
- Librarian agent: `agents/librarian/agent.md`
- Codifier agent: `agents/codifier/agent.md`
- Guide routing table: `operations/references/guide-routing-table.md`
- Governing DDs: DD-77, DD-78, DD-80, DD-81, DD-82
