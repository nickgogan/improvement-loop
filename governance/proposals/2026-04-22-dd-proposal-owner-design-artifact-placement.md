---
title: "DD Proposal — Four-zone architecture for governance, deliberative, operational, and ratified artifacts"
type: "dd-proposal"
stage: "proposed"
target_system:
  - "improvement-loop"
created: "2026-04-22"
updated: "2026-04-22"
author: "owner"
autonomy_tier: "Proposal-First"
source_dd:
  - "DD-44"
  - "DD-52"
  - "DD-55"
  - "DD-56"
  - "DD-59"
  - "DD-86"
tags:
  - "proposal"
  - "dd-proposal"
  - "governance"
  - "fractal-pattern"
  - "owner"
  - "architecture"
aliases:
  - "Four-zone architecture"
  - "Design-notes placement"
  - "Owner design-artifact placement"
---

# DD Proposal — Four-zone architecture for governance, deliberative, operational, and ratified artifacts

**Status:** Owner proposal. Not a DD. Nick files DDs; the Owner proposes and presents rationale.

**Prompted by:** Nick's pushback on a narrower first draft of this proposal (session 50, 2026-04-22) — *"I don't like the concept of having design notes in the `operations/` folder for IL. I think the closest existing thing is actually `project-management/`, which would fall under the governance/provenance of Owner agent actually."* The reframe cut at a cleaner joint than author-role distinctions. This revision replaces the first draft.

**Scope:** The full IL fractal layout for deliberative and governance artifacts. Applies retroactively via migration this session; forward-going for all new writes.

---

## Context

Design output has accumulated in the IL system without a written rule governing placement. Two symptoms surfaced:

1. **Codifier design notes (sessions 46–49)** — substrate audits, read contracts, use-case registries, acceptance rubrics, lifecycle specs, spot-check reports — landed in `operations/design-notes/` by convenience. The `operations/` folder is shaped for runtime event output (SL entries, handoffs, research-reports, loop-reports, identification reports). Deliberative specifications are not runtime events.
2. **Owner design output (session 50)** — a tracking-mechanism proposal and this DD proposal — needed a home at session-49 close. Nick gated them out of `operations/design-notes/` into `governance/proposals/`. That decision was locally correct but exposed a larger drift: the whole `operations/design-notes/` folder is shape-wrong. Deliberative specifications belong under `project-management/` — the fractal's "what we're deciding and why" zone, Owner-governed per DD-55/56/86.

The fractal pattern (DD-52) already distinguishes `operations/` (what happened) from `project-management/` (what we're deciding) from `governance/` (the rules of the house). This proposal makes the distinction operative for design artifacts and collapses a convenience-destination folder that was not fractal-compliant.

---

## Proposal: Four-Zone Architecture

### The zones

| Zone | Purpose | Contains | Governance |
|---|---|---|---|
| **`project-management/design-decisions/`** | Ratified rules (immutable per DD-44) | DDs | Owner triages, Nick files |
| **`project-management/implementation-backlog/`** | Tracked work items | IB items | DD-55/56 |
| **`project-management/design-notes/`** *(new home)* | Deliberative specifications | Substrate audits, read contracts, use-case registries, acceptance rubrics, lifecycle specs, spot-checks, pipeline-mechanics specs | Owner-governed; any agent may write |
| **`governance/`** (root) | Active ratified governance rules | `boundary-rules.md`, `pipeline-rules.md`, `agent-rules.md`, `knowledge-rules.md` | Owner maintains, derived from constitution |
| **`governance/proposals/`** | Owner-authored proposals for governance changes | Tracking-mechanism proposals, DD proposals, amendment proposals, drift reports with remediation plans | Owner, Proposal-First tier |
| **`operations/`** | Runtime event output only | SL entries, handoffs, research-reports, loop-reports, identification reports, extraction reports | Any agent, event-driven |
| ~~`operations/design-notes/`~~ | **Deprecated and removed this session.** Contents migrated to `project-management/design-notes/`. | — | — |

### Placement rule

**Artifact shape governs placement; author role is a heuristic, not authority.**

- **Deliberative specification** (spec, audit, registry, rubric, contract) → `project-management/design-notes/`.
- **Governance-rule proposal** (new rule, new mechanism, DD proposal, amendment) → `governance/proposals/`.
- **Ratified governance rule** (post-gate, active) → `governance/` root.
- **Runtime event output** (log, report, handoff) → `operations/`.

Shape is usually clear from intent: does the artifact specify *how a pipeline mechanic works* (deliberative), or does it propose *a rule for how the system should be governed* (governance-rule), or is it *a record of what happened in a session* (operational)? When a single artifact spans shapes (e.g., a tracking-mechanism proposal that embeds a controlled-vocabulary and routing rules), classify by the primary purpose. The session-50 boundary-case tracking proposal is a governance-rule proposal with an operational substrate embedded — governance-shape wins; `governance/proposals/`.

### Why this split matters

The three zones have genuinely different lifecycles, audiences, and consumption patterns.

| Aspect | `operations/` | `project-management/design-notes/` | `governance/` (proposals + root) |
|---|---|---|---|
| **Purpose** | What happened | What we're deciding and why | The rules of the house |
| **Lifecycle** | Event-driven, append-only | Draft → accepted → superseded; revisited | Proposed → gated → active → amended/superseded |
| **Audience** | Git archaeology; audit trail | Codifier next session; skills that operationalize the spec; Owner cross-session | Nick; future Owner sessions for consistency checks |
| **Persistence** | Indefinite but low-access | Medium — superseded when spec is deployed into skills/artifacts | Long-lived reference (active governance reads forever) |
| **Authority** | Descriptive (states a fact) | Specifying (proposes a plan) | Normative (states a rule) |
| **Folder governance** | Any agent writes; no agent governs | Owner-governed, any agent writes | Owner-governed, Owner writes |

Putting deliberative specs in `operations/` muddled this. Owner queries for "current system-wide rules" had to scan a folder full of sessional descriptive output. Codifier queries for "how does the substrate audit relate to the pipeline collapse proposal?" had to wade through handoffs and SL entries. Both classes of query now get cleanly separated substrates.

---

## Migration (executed this session, not proposed)

**Seven files moved** from `operations/design-notes/` to `project-management/design-notes/` — no content changed, only location:

| File | Size | Source |
|---|---|---|
| `2026-04-20-artifact-acceptance-rubric.md` | 16 KB | Session 46 — Codifier |
| `2026-04-20-artifact-lifecycle-spec.md` | 34 KB | Session 46 — Codifier |
| `2026-04-20-pipeline-collapse-proposal.md` | 32 KB | Session 47 — Codifier |
| `2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md` | 43 KB | Session 47 — Codifier |
| `2026-04-21-contract-section-spotcheck-agent-audit.md` | 30 KB | Session 48 — Codifier |
| `2026-04-21-librarian-read-contract.md` | 31 KB | Session 49 — Codifier |
| `2026-04-21-librarian-use-case-registry.md` | 24 KB | Session 49 — Codifier |

**Cross-references updated** via bulk `sed` across all referring files (SL entries, handoffs, reference-layer files, SKILL.md files, pattern-identification reports, PROGRESS.md at both workspace root and IL root, the moved design notes themselves).

**Empty `operations/design-notes/` directory removed.**

**Unchanged:**
- The two session-50 governance/proposals files (this one + the boundary-case tracking proposal) — they were born under the new rule, no migration needed. Historical context in both files updated to reflect the new canonical location.
- Everything outside IL — per session-50 constraint, no workspace-root deploys. Workspace-root PROGRESS.md is a tracking doc, not a deployed artifact; path update was a broken-link fix.

**Rationale for migrating now rather than deprecating-for-new-writes-only:**

Initial instinct was no-migration (preserve cross-reference stability). Nick's correction: *"I want in this session to also do the full cleanup. If we need to update a lot of files, let's do it, but I think it's better to make things as clean as possible at this stage."* The fractal pattern is load-bearing substrate — leaving a deprecated folder with a frozen snapshot creates permanent cognitive tax ("which of the two design-notes folders is canonical?"). Full cleanup resolves that now; the cost (updating ~27 cross-references) is one-shot; the benefit (one canonical location) compounds across every future session.

---

## Relationship to existing DDs

- **Refines DD-52 (fractal unit pattern).** DD-52 separates `governance/`, `project-management/`, and `operations/` for a reason. This proposal makes the distinction operative for design artifacts and collapses a pre-DD-52 convenience folder that predated the rule's operational clarity.
- **Extends DD-55 / DD-56 / DD-59** (governance-to-operations distinctions for DDs, IB items, System Log). Those DDs established the `project-management/` vs `operations/` split for tracked work and runtime events. This proposal applies the same logic to design artifacts: deliberative specs are tracked-work-shape → `project-management/`; runtime outputs remain in `operations/`.
- **Clarifies DD-86 (Owner responsibility).** DD-86 assigns governance-folder maintenance to the Owner. This proposal extends Owner-governance to `project-management/design-notes/` (as folder maintainer; any agent still authors there) and names `governance/proposals/` as the canonical home for Proposal-First Owner output.
- **Supersedes nothing.** Fills a gap.

---

## Implementation details

Downstream edits (all executed this session alongside the migration):

1. **`project-management/design-notes/_index.md`** — created, catalogs the seven migrated files.
2. **`project-management/_index.md`** — updated to include the new subfolder.
3. **`governance/_index.md`** — updated to include `proposals/` subfolder.
4. **`agents/owner/agent.md`** — Output Artifacts table already names `governance/proposals/` as Proposal-First destination; no edit needed. Input Artifacts Consumed table: no change (Owner already reads governance/).
5. **`agents/codifier/agent.md`** — *deferred proposal*. Codifier's Output Artifacts section currently doesn't name a design-note destination explicitly. Adding a line pointing it to `project-management/design-notes/` is an agent-constitution edit (Proposal-First per Owner autonomy table); deferring to a separate Nick-gated pass after this DD is filed.
6. **`CLAUDE.md`** (IL root) — does not currently reference `design-notes/` anywhere; no edit needed.

Nothing else moves. No other cross-system impact.

---

## Retroactive scope

**Migration executed.** All seven pre-existing design notes moved this session; every cross-reference updated.

**Going forward:**
- From session 50 onward, deliberative specifications land in `project-management/design-notes/`.
- Owner-authored proposals continue to land in `governance/proposals/`.
- `operations/` contains runtime event output only.
- `operations/design-notes/` does not exist.

**Git archaeology:** the move is visible in git history; anyone investigating the old paths can trace them.

---

## Open questions for Nick

1. **DD number.** Needs assignment on filing. Most recent DD is DD-88 (DD-88 supersedes DD-72); DD-89 or next available.
2. **DD title.** Working title above is long. Alternatives: *"Four-zone fractal architecture for design artifacts"*, *"Deliberative design notes live in project-management/design-notes/"*. Your preference.
3. **Codifier agent-constitution edit.** I deferred editing `agents/codifier/agent.md` to a separate Proposal-First pass so this session stays focused. Prefer I include it in the next Owner session after the DD files, or batch it into this session's SL close?
4. **Archive conventions.** When a design note is superseded (e.g., session-49 read-contract would be if the reference layer materializes its protocol elsewhere), does it stay in `project-management/design-notes/` with `stage: "superseded"`, or move to `archive/`? DD-52 names `archive/` as a fractal folder; IL's `archive/` currently only holds retired improvement-proposals. I'd propose supersede-in-place with frontmatter stage change; formal archival only at milestone boundaries. Confirm or redirect.
5. **Cross-system generalization.** Household OS and Claude Build will eventually face the same question. This DD could be IL-scoped or MetaSystem-scoped. I'd propose IL-scoped for now; MetaSystem-level rule can follow if Household OS or Claude Build accumulate design notes and the pattern generalizes.

---

## Summary

- **What this proposes:** a DD codifying the four-zone architecture — `project-management/design-notes/` for deliberative specs, `governance/proposals/` for governance proposals, `governance/` root for ratified rules, `operations/` for runtime events.
- **Migration:** seven design notes moved from `operations/design-notes/` to `project-management/design-notes/` this session; all cross-references updated; deprecated folder removed.
- **Why now:** Nick's reframe made clear that the fractal pattern already had the right split; we just hadn't operationalized it for design artifacts. Full cleanup resolves the drift before more sessions accumulate under the broken convention.
- **Cost:** one-shot — file moves and sed across ~27 files. Already paid.
- **Risk:** low. No content changed. Git history preserves the move. Paths updated atomically.

Nick files the DD if the architecture is acceptable as stated. The Owner does not file DDs (DD-44).

---

## Cross-References

- Companion proposal (Owner output under the new architecture): `governance/proposals/2026-04-22-librarian-boundary-case-tracking.md`
- New home for migrated design notes: `project-management/design-notes/`
- Precipitating decision: Nick's session-50 gate, 2026-04-22, captured in this proposal's Context section
- Governing DDs: DD-44 (DD immutability), DD-52 (fractal pattern), DD-55/56/59 (governance-to-operations distinctions), DD-86 (Owner responsibility)
- Deferred downstream edit: `agents/codifier/agent.md` Output Artifacts section (Proposal-First, separate Nick gate)
