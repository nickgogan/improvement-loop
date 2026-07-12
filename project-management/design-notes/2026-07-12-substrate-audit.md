---
title: "Substrate audit — per-class kernel-vs-state verdicts (restructure program Phase 2)"
id: "substrate-audit-2026-07-12"
type: "design-note"
category: "substrate-audit"
target_system:
  - "improvement-loop"
stage: "review"
created: "2026-07-12"
updated: "2026-07-12"
author: "claude"
tags:
  - "design-note"
  - "substrate-audit"
  - "restructure-program"
  - "kernel-vs-state"
---

# Substrate Audit — Per-Class Kernel-vs-State Verdicts

**Program:** `operations/plans/2026-07-12-engine-restructure-program.md` §Phase 2.
**Litmus applied:** *if a downstream consumer would pull it, it's kernel; if only this
instance needs it, it's state.* Verdict vocabulary: keep / distill / archive / re-home.
**Standing rule:** every verdict below is a proposal. Nothing has been moved, superseded,
or edited. Nick gates each numbered item in §Gates before any execution.

## Executive summary

Six classes audited by parallel Owner-disposition auditors (session 139). The substrate
is healthier than the clutter hypothesis suggested in two places (IB items and concept
docs need essentially nothing) and worse in two others (the April design-note monsters
are ~230KB of fully-ratified state, and the System Log retirement left one **functionally
broken skill** and several second-order writers behind). The DD corpus splits 26 kernel /
59 state, directly seeding the Phase 5 kernel manifest; seven Binding DDs are
functionally dead and close with one consolidating supersession. `knowledge/guides/` is
confirmed too shallow to carry the system and dissolves. The audit also produced the
DD-59 scope note (drafted, §System Log) and a distill-candidate list that sizes the
second-brain question: the dominant loss pattern is *learning entries that routed their
fix but stranded their calibration data*.

## Urgent (broken today, independent of any gate)

1. **`/extract-artifacts` is functionally broken.** Its DD-95 `--sl STEM` provenance
   validation requires a System Log entry that can no longer exist after the SL producer
   retirement (session 138). Every future non-guide artifact write aborts. The provenance
   anchor needs re-pointing (candidates: the source finding itself, or the identification
   report). Fix shape is a Nick gate (item G5) because it touches DD-95.
2. **Second-order SL writers survived the retirement:** seven dormant Librarian
   encounter-log surfaces, `/solicit-proposals` round records, freshness-assuming reads
   in `/system-audit` + `/system-health`, and the live `librarian-reads.md` rolling log
   inside the frozen folder. Cleanup is mechanical once G4/G5 are ruled.

## Gates (Nick rules each; numbered for reference)

- **G1 — DD consolidating supersession.** One new DD closes the seven functionally-dead
  Binding DDs: DD-38, DD-40, DD-42, DD-50, DD-58 (Notion/Household-era, obsoleted by
  DD-103/DD-106), DD-31 (stranded by DD-80), DD-90 (stranded by DD-116).
- **G2 — DD distills.** DD-39, DD-47, DD-61 (kernel content, stale text/overlap) and the
  half-stranded halves of DD-59/DD-95 get distilled per the DD-section table.
- **G3 — DD re-homes.** DD-60 and DD-62 re-home to `knowledge/` as methodology patterns.
- **G4 — DD-59 scope note.** Drafted verbatim in §System Log; records producer
  retirement without supersession.
- **G5 — DD-95 / `/extract-artifacts` repair.** Choose the new provenance anchor (see
  Urgent #1); DD-95 amendment or scope note accordingly.
- **G6 — Design-note archive sweep.** Archive 10 fully-ratified notes to
  `archive/design-notes/` (convention proposed in §Design Notes), distill-then-archive 2,
  re-home the Librarian read-contract + use-case registry to
  `operations/references/librarian/` per DD-112.
- **G7 — IB hygiene.** Close IB-148 (mooted by Phase 0) and IB-102 (superseded by the
  harness-materialization model); merge IB-103 into IB-173; assign IB numbers to the two
  work-shaped PROGRESS backlog lines (meta-skill-author follow-ups A/D/E, governance
  visualization).
- **G8 — Guides dissolution.** Fold `research-to-codification-pipeline.md` into the
  future kernel "how it works" doc (Phase 4/5; until then mark it DD-cache), keep
  `skill-authoring-guide.md` as cheat-sheet pending the Phase 4 harness-description doc,
  trim or delete the stale `_index.md`; archive the 10 harvest-queue files, deprecated
  G2, and `system-log-template.md` from the extracts/knowledge trees.
- **G9 — Boundary-case routing dangler.** Boundary-case encounters still route to the
  retired System Log (design-note finding); pick the new destination (likely IB or
  knowledge/, consistent with the DD-116 routing rule).
- **No-gate follow-ups** (mechanics, route to `/maintain-docs`): stale
  `knowledge/reference/_index.md` (Household-OS framing), stale
  `extracts/guides/CLAUDE.md` deployment-target line, DD-66 missing `title` frontmatter.

## What this feeds

- **Second-brain sizing (next unit of work):** the honest drop-inventory is §System
  Log's distill-candidate list (10 entries, dominant pattern: stranded calibration data)
  plus §IB's observation that pre-DD-116 closure notes absorbed session reports. Rule 11
  asks whether that loss rate justifies a store mechanism beyond DD-116 routing.
- **Phase 5 kernel construction:** the 26 kernel-tagged DDs, the two kernel-shaped
  design-wisdom docs (`fractal-pattern.md`, `vocabulary.md`, flagged for a DD-112
  amendment), and the guides/templates flagged kernel-shaped in §Guides.

---
# Substrate Audit — Design Decisions class

## Design Decisions (85 audited)

**Plain-English summary.** Of 85 DDs (76 Binding, 9 Superseded), the large majority need no action: 26 form the portable kernel (identity, values, architecture invariants, asset-form definitions, lifecycle rules) and 39 are healthy engine-instance state (pipeline mechanics, KB structure, tuning). The real finding is a cleanup opportunity: 7 Binding DDs are functionally dead — five Notion/Household-era structure DDs (DD-38/40/42/50/58) that DD-103/DD-106 obsoleted without formally superseding, plus DD-31 (stranded by DD-80) and DD-90 (stranded by DD-116's SL retirement) — one consolidating supersession DD could close all seven, Nick-gated per DD-44. Five more are distill candidates (stale text or half-stranded by later rulings), two agent-team-methodology DDs would serve better re-homed as knowledge patterns, and the 9 already-Superseded DDs are candidates for archival placement (moved, never deleted; chains stay traceable). Every non-keep verdict here is a proposal for Nick — no DD is touched by this audit.

Litmus applied: *if a downstream consumer pulling the engine's governance would need it, it's kernel; if only this instance needs it, it's state.* Binding-spine vs procedural is the discriminator — a Binding DD can still be state.

### Keep — kernel (26)

| DD | Title | Status | Class | Verdict | Rationale |
|----|-------|--------|-------|---------|-----------|
| DD-29 | Human gate at every stage boundary | Binding | kernel | keep | Values-derived rule binding every session; any consumer pulls it |
| DD-36 | Periodic research drives system evolution | Binding | kernel | keep | Core operating model; body's S2/S3 refs stale but decision holds |
| DD-37 | Five design philosophy principles | Binding | kernel | keep | The values layer itself — constitution material |
| DD-41 | Research KB is IL-owned operational data | Binding | kernel | keep | Ownership boundary that declares the KB state, not kernel |
| DD-44 | DD lifecycle: Binding/Proposed/Superseded | Binding | kernel | keep | The lifecycle rule every governance consumer needs |
| DD-52 | Seven-folder fractal unit structure | Binding | kernel | keep | Exported architecture invariant; downstream systems are built on it |
| DD-53 | Agents as primary work interface | Binding | kernel | keep | Interaction model; flag Phase-4 tension with single-implicit-agent |
| DD-55 | DDs distributed to system-scoped folders | Binding | kernel | keep | Governance-placement invariant consumers inherit |
| DD-56 | IB items distributed to system-scoped folders | Binding | kernel | keep | Same placement invariant, IB half |
| DD-63 | Structured artifact communication between agents | Binding | kernel | keep | File-mediated handoff invariant, reaffirmed by DD-82 |
| DD-74 | Token budget constraints on context files | Binding | kernel | keep | Portable token-economy rule (no counts, no duplication) |
| DD-78 | ContractSpec on every codified artifact | Binding | kernel | keep | Asset-form definition — universal artifact layer |
| DD-80 | Direct extraction replaces proposer stage | Binding | kernel | keep | Defines the engine's core value flow (identify → extract) |
| DD-82 | Four-agent system, file-mediated handoffs | Binding | kernel | keep | Primary-actors model; flag Phase-4 single-agent tension |
| DD-86 | Owner agent as system steward default | Binding | kernel | keep | Actor + authority-tier model every graduated system inherits |
| DD-92 | ContextSpec consumer-facing fit metadata | Binding | kernel | keep | Asset-form definition, companion to DD-78 |
| DD-103 | Collapse federation into one engine | Binding | kernel | keep | Identity — what the system now is |
| DD-104 | Single-engine, three-altitude architecture | Binding | kernel | keep | Top-level architecture shape |
| DD-105 | Charter as root vision doc with trajectory signals | Binding | kernel | keep | Constitution pointer; defines vision-vs-rulebook split |
| DD-107 | Schematic artifact form | Binding | kernel | keep | Asset-form definition for top-altitude output |
| DD-108 | Owner files DDs as mechanics; Nick gates content | Binding | kernel | keep | Autonomy/gating rule — governance kernel by definition |
| DD-109 | System-scoped skills + skills-as-atomic-unit | Binding | kernel | keep | Atomic-capability-unit half is portable; placement half is instance detail |
| DD-116 | Session-ops spine: PROGRESS + HISTORY + commits | Binding | kernel | keep | Ops model already proven portable (pulled from CareerBuddy); artifacts are state, the convention is kernel |
| DD-39 | Stage before deploying to live systems | Binding | kernel | distill | Invariant is kernel; mechanism text is Notion-era and reframed by DD-111 — distill the invariant into kernel docs |
| DD-47 | Three-peer workspace directory organization | Binding | kernel | distill | Workspace shape is kernel but text still names dissolved meta-system/ + s1-schema; propose post-collapse supersession |
| DD-61 | Milestone-gated agent development loop | Binding | kernel | distill | Genuine gate invariant but overlaps DD-29; fold into one human-gate kernel rule |

### Keep — state (39)

| DD | Title | Status | Class | Verdict | Rationale |
|----|-------|--------|-------|---------|-----------|
| DD-51 | Single git repository for MetaSystem | Binding | state | keep | Instance repo topology; still governs |
| DD-54 | Single Obsidian vault with YAML frontmatter | Binding | state | keep | Load-bearing substrate, but no consumer pulls "Obsidian vault" |
| DD-57 | Descriptive system names without S-numbers | Binding | state | keep | Instance naming convention |
| DD-64 | Bootstrap skill instantiates agent teams | Binding | state | keep | Live skill mechanics; meta-system-template refs mildly stale |
| DD-66 | Dependency spectrum for external packages | Binding | state | keep | Research-ops posture; fix missing `title` field (data defect) |
| DD-67 | Two-pass research extraction model | Binding | state | keep | Pipeline mechanics |
| DD-68 | Externalized research dimensions registry | Binding | state | keep | KB structure |
| DD-69 | Bidirectional source–finding links | Binding | state | keep | KB data-integrity rule |
| DD-70 | Four-type finding cross-references | Binding | state | keep | KB data-integrity rule |
| DD-71 | Four-verdict source triage tree | Binding | state | keep | Intake procedure |
| DD-73 | Ten canonical dimensions with rebalance | Binding | state | keep | KB structure (DD-87 lawfully added the 11th) |
| DD-75 | Override forces guided tier | Binding | state | keep | Form Router mechanics |
| DD-76 | Multi-role findings bias to pattern | Binding | state | keep | Form Router mechanics |
| DD-77 | Single form per finding, no hints | Binding | state | keep | Router output contract |
| DD-79 | Four anti-tacit-knowledge fields | Binding | state | keep | Finding-schema rule (hit when writing data) |
| DD-81 | Pattern findings route to guide synthesis | Binding | state | keep | Pipeline routing detail |
| DD-83 | On-demand research intake pathway | Binding | state | keep | Second intake pathway, instance component |
| DD-84 | Private monorepo with subtree publishing | Binding | state | keep | Instance publishing infrastructure (foundational yet state) |
| DD-85 | Single vault without nested vaults | Binding | state | keep | Instance substrate; near-duplicate of DD-54 — merge candidate if either is ever reopened |
| DD-87 | Agentic OS as dimension eleven | Binding | state | keep | Narrow dimension addition |
| DD-88 | Priority-governed finding lifecycle v2 | Binding | state | keep | Pipeline process (active successor of DD-72) |
| DD-89 | Four-zone design-artifact placement | Binding | state | keep | Instance folder semantics |
| DD-91 | Reflections-to-proposals pipeline | Binding | state | keep | Live but lightly used; revisit only on recurrence |
| DD-93 | Guide regen preserves designated sections | Binding | state | keep | Synthesis mechanics |
| DD-94 | Paired changelog files for guides | Binding | state | keep | Mechanics; "narrative lives in SL" clause stale post-DD-116 |
| DD-96 | Source-drift detection for extracts | Binding | state | keep | Codifier procedure |
| DD-97 | Extension-first before new artifacts | Binding | state | keep | Codifier discipline |
| DD-98 | Guide split at threshold conditions | Binding | state | keep | Procedure, as amended by DD-102 |
| DD-99 | Theme graduation from unrouted bucket | Binding | state | keep | Procedure |
| DD-100 | Versioned side-file for regeneration | Binding | state | keep | Mechanics |
| DD-101 | Co-occurrence harvest queue | Binding | state | keep | Mechanics |
| DD-102 | Raised guide-split thresholds | Binding | state | keep | Tuning amendment to DD-98 |
| DD-106 | Claude Build retired; Household OS to Notion | Binding | state | keep | One-time transition record explaining the workspace's shape |
| DD-110 | Two audit lenses, two homes | Binding | state | keep | Instance naming/placement disambiguation |
| DD-111 | extracts/ is substrate, not staging | Binding | state | keep | Engine KB placement semantics |
| DD-112 | Concept-doc home rule | Binding | state | keep | Instance placement rule; Phase 2 must reconcile it with the kernel model (plan names this explicitly) |
| DD-113 | Forward-only source_dd linkage | Binding | state | keep | Governance data-format rule |
| DD-114 | YAML block-scalar convention + linter | Binding | state | keep | Data-integrity mechanics |
| DD-115 | FOUNDATIONS.md generated spine | Binding | state | keep | Derived-view mechanism over this instance's DD corpus |

### Distill / re-home candidates (proposals — Nick gates each)

| DD | Title | Status | Class | Verdict | Rationale |
|----|-------|--------|-------|---------|-----------|
| DD-59 | System log distributed to system-scoped folders | Binding | state | distill | SL retired as producer (DD-116); supersede into a read-only-history placement note and drop from FOUNDATIONS |
| DD-95 | Session tracking fields on non-guide extracts | Binding | state | distill | `last_change_sl` stem can no longer be produced post-DD-116; propose amending supersession |
| DD-60 | Composable agent teams per project | Binding | state | re-home | Product methodology referencing dissolved meta-system templates; belongs in knowledge/patterns, not governance |
| DD-62 | Two-phase development: Explore then Harden | Binding | state | re-home | Development methodology the engine teaches, not a rule the engine obeys — knowledge pattern |
| (also DD-39, DD-47, DD-61 — kernel-content distills, listed in the kernel table) | | | | | |

### Archive candidates

**Binding but functionally dead — propose one consolidating supersession DD (Nick-gated per DD-44), then archival placement:**

| DD | Title | Status | Class | Verdict | Rationale |
|----|-------|--------|-------|---------|-----------|
| DD-31 | Scoped assessment by finding applicability | Binding | state | archive | Governs the Proposer stage that DD-80 eliminated |
| DD-38 | Four-section architecture documentation hub | Binding | state | archive | Notion-era doc hub; structure no longer exists post-DD-103 |
| DD-40 | System docs in Household Teamspace | Binding | state | archive | Household Teamspace framing dead post-DD-106 |
| DD-42 | Cross-system databases as top-level peers | Binding | state | archive | Superseded in practice by DD-55/56/59 distribution |
| DD-50 | S1-schema as read-only Notion mirror | Binding | state | archive | s1-schema and its Notion mirror left with Household OS |
| DD-58 | S1 and S2 consolidated as Household OS | Binding | state | archive | Household OS archived to Notion (DD-106); no local referent |
| DD-90 | Session telemetry on system log entries | Binding | state | archive | SL retired as producer (DD-116); telemetry block has no carrier |

**Already Superseded — archival placement only (moved with chains intact, never deleted; precedent: DD-33/34/49 archived with Claude Build):**

| DD | Title | Status | Class | Verdict | Rationale |
|----|-------|--------|-------|---------|-----------|
| DD-30 | Two-agent model with read/write boundaries | Superseded | state | archive | Superseded by DD-82 |
| DD-32 | Four-system decomposition of Household OS | Superseded | state | archive | Superseded by DD-103 |
| DD-35 | IL skill composition with scope boundaries | Superseded | state | archive | Superseded by DD-65 (itself superseded) |
| DD-43 | Rename to MetaSystem, consolidate DD specs | Superseded | state | archive | Superseded by DD-45 chain |
| DD-45 | MetaSystem as active knowledge layer | Superseded | state | archive | Superseded by DD-103 |
| DD-46 | Research-to-MetaSystem knowledge flow | Superseded | state | archive | Superseded by DD-103 |
| DD-48 | Incubator bootstrapping and S-number promotion | Superseded | state | archive | Superseded by DD-57 |
| DD-65 | Six local-first IL skills with Perplexity | Superseded | state | archive | Long outgrown; skill set now far larger |
| DD-72 | Priority-governed finding lifecycle v1 | Superseded | state | archive | Superseded by DD-88 |

### Patterns observed

Three supersession events left strandees: DD-103/DD-106 obsoleted five Notion/Household-era DDs (38/40/42/50/58) without formal supersession; DD-80 stranded DD-31; DD-116 stranded DD-90 and half of DD-94/95 — one consolidating cleanup DD closes all of it. The April pipeline-mechanics block (DD-67 through DD-102, ~30 DDs) is procedure-shaped, not decision-shaped — under the kernel model these read as pages of an ops manual with DDs as its change log; no move proposed now (they work as state), but any kernel authoring should generalize the *process*, not cite 30 DDs. FOUNDATIONS ≠ kernel: DD-54/84 are foundational-yet-state (instance substrate), while DD-63/74/78/92/107 are kernel-yet-unflagged — the two litmuses measure different things and should stay separate. Tuning-by-amendment chains (DD-72→88, DD-98→102) work fine; no mechanism change needed. One data defect: DD-66 lacks a `title` field. Phase-4 flag only (no action): DD-53/DD-82's multi-agent model sits in tension with the single-implicit-agent vision.
# Substrate Audit — Implementation Backlog

## Implementation Backlog (73 audited)

**Plain-English summary.** The IB folder holds 73 items: 7 live (3 Backlog, 2 Queued, 2 Deferred), 53 Done, 13 Cancelled. Against the kernel litmus every one of them is **state** — instance-specific work tracking that no downstream consumer would pull; no exceptions found. The Done and Cancelled classes should **stay exactly where they are**: they cost nothing at read time (`/ib list` greps frontmatter only, nothing globs full bodies, there is no `_index.md` to maintain), and moving them to `archive/` would corrupt the semantics of `archive/` (which holds retired *systems*, not retired *rows*) and break `/ib`'s hos/cb scope filters. Among the live items, three (IB-171/172/173) are Nick-approved and healthy; IB-145 is a cheap legitimate maintenance item; but **IB-148 is mooted by Phase 0** (its audit target, the dated-handoff corpus, no longer accumulates) and the two Notion-era Deferred relics **IB-102 and IB-103 are invisible to PROGRESS** — one superseded by the restructure program itself, the other a duplicate of IB-173.

**Kernel-vs-state verdict for the class: state, in full.** IB items are the engine-instance's memory of its own work. The kernel is the export unit by construction; a downstream system pulling the engine's governance kernel has no use for the record that the engine once set up Notion teamspaces. Exception sweep: the closest thing to kernel content is architectural rulings embedded in Done closure notes (e.g., IB-164's session-85 partition-by-queue-file concurrency ruling) — but in each sampled case the ruling was also applied to its canonical home (SKILL.md / DD), so the IB copy is a record, not the source. Flagged as a pattern, not an exception.

---

### 1. Live items (7)

| ID | Title | Status | Verdict | Rationale |
|----|-------|--------|---------|-----------|
| IB-172 | Layered memory architecture eval — OKF + storage/retrieval tiers | Backlog | **keep** | Nick-approved ("100%"), P2, PROGRESS-tracked; direct input to this program's Phase 2 second-brain design. |
| IB-173 | Three-bucket gate tiering — DD-29 refinement | Backlog | **keep** | Nick-approved ("totally agreed"), P2, KB-grounded, PROGRESS-tracked; governance-gated design item. |
| IB-171 | Corpus-wide KB linkage-hygiene sweep | Backlog | **keep** | Nick ruled "save for later"; well-scoped (measured inventory + pointers to detection scripts); sweep-session shaped per standing preference. |
| IB-145 | Re-analyze GSD for version drift (v1.33.0 → v1.34.2+) | Queued | **keep** | Legitimate cheap maintenance (`/repo-analyzer gsd --force`); drift has only grown since filing, so value is intact. |
| IB-148 | Build /session-handoff-review skill (audit handoff corpus) | Queued | **close (mooted)** | Its entire input surface — an accumulating `handoff-prompts/` corpus — was retired by Phase 0; dated handoffs are frozen in `archive/handoffs/`, and its functions (repeat-item, drift, cruft detection) are now structurally owned by `/session-handoff`'s reconcile-in-place + route-then-compact + line-budget hook. Any one-time retrospective of the frozen corpus is IB-172/second-brain *input*, not a standing P2 build. PROGRESS already suspects this ("likely mooted — resolve or close"); confirmed. |
| IB-102 | Design system-applicator skill spec | Deferred | **close (superseded)** | Notion-era relic (blank body, M4, `notion_id`). The "applicator that executes system-specific changes" concept is superseded by the restructure program's harness-materialization model (kernel → compiled targets, plan §2) while the deploy stage stays Nick-gated (DD-29). Not tracked in PROGRESS. |
| IB-103 | Implement gate relaxation mechanism | Deferred | **merge → IB-173** | Same problem as IB-173 (relaxing DD-29's binary gate for low-risk/two-way-door changes); IB-173 is the approved, KB-grounded successor design. Close IB-103 with a pointer; carry its prerequisites idea (track record before relaxing) into the IB-173 spec if useful. Not tracked in PROGRESS. |

**Cross-check vs PROGRESS.md §Backlog/Icebox:**

- *Live IB items PROGRESS doesn't know:* **IB-102 and IB-103** (both Deferred). PROGRESS names IB-171/172/173/145/148 only. Since both get close/merge verdicts above, resolving them also resolves the visibility gap — no PROGRESS edit needed beyond the close.
- *PROGRESS backlog lines with no IB number* (header says "Work items carry IB numbers"): meta-skill-author assess follow-ups A/D/E; `/link-intake` escalation-language watch item; governance visualization; G3/G9 guide bifurcation; MongoDB sizing-engine pilot; Memongo improvement surfaces; GitHub collaborators for `il-published`; Obsidian Workspaces config; temp-directory cleanup. Honest read: the trigger-gated reminders (G3/G9, MongoDB pilot, GitHub collaborators, Obsidian, temp cleanup, Memongo) are event-gated *watch* lines and arguably fine as PROGRESS-only. Two are genuinely work-shaped and unnumbered: **meta-skill-author follow-ups A/D/E** and **governance visualization** — candidates for IB numbers at the next maintenance pass, or accept them as PROGRESS-only and soften the header claim.

### 2. Done items (53) — class verdict: **keep in place, immutable record**

Sampled 10 for homogeneity (IB-07, IB-64, IB-104, IB-120, IB-139, IB-146, IB-155, IB-160, IB-164, IB-170): all are completed-work records with status/priority/source-DD frontmatter plus a closure body of varying depth. Homogeneous as a class; no item carries kernel content whose canonical home is the IB file.

Argument for keep-in-place (vs re-home to `archive/`):

- **Read-time cost is effectively zero.** `/ib list` explicitly "uses grep on frontmatter — never reads full files" (`/Users/nickgogan/MetaSystem/.claude/skills/ib/SKILL.md` line 82). No skill, hook, or `_index.md` globs the folder's bodies; there is no catalog to maintain (workspace Process Rule 1). Done items cost disk, not context — the token economy has nothing to collect here.
- **Fractal-pattern semantics.** `archive/` archives retired *units* (Household OS, Claude Build, meta-system shell). `/ib` already resolves `archive/*/project-management/implementation-backlog/` as *historical systems* (hos/cb scope filters, SKILL.md line 27, 82). Moving Done engine rows there would conflate "work finished" with "system retired" and break those filter semantics.
- **Reference stability.** Done IB IDs are cited from DDs, HISTORY.md, and closure notes of other IBs; in-place status partitioning keeps every reference valid with zero churn. Next-number allocation already scans engine + archive folders, so no numbering concern either way — but there is simply no benefit to pay any move cost for.

Exceptions/notes within the class (not verdict-changing):

- **Bloated closure notes:** IB-155 (~3.1k), IB-159–IB-166 (~4.7–13k) carry session-work-report dumps in a single-line YAML `notes:` field — the IB-form analog of the April design-note monsters. Cost is per-item-read only, so no action required; relevant as second-brain evidence (see Patterns).
- **Blank-body Notion imports** (e.g., IB-104, IB-120): frontmatter-only records, harmless.
- **IB-164 session-85 amendment** embeds an architectural ruling (Option A end-to-end subagent mode + partition-by-queue-file) — ruling was applied to the SKILL.md, so the IB copy is record-not-source; noted as the pattern of decision-shaped content landing in IB closures pre-DD-116 routing.

### 3. Cancelled items (13) — class verdict: **keep in place, immutable record**

Sampled 8 (IB-28, IB-96, IB-106, IB-136, IB-142, IB-147, IB-167, IB-168): homogeneous — nearly all are casualties of the federation collapse (DD-103): Household OS/Notion-era items (IB-28, IB-96, IB-106), meta-system-shell build items (IB-136, IB-142, IB-167, IB-168), and one pipeline supersession (IB-147, replaced by the DD-80-shaped `/extract-artifacts` that was built by a different path). Same keep-in-place logic as Done — plus these records are the *only* place documenting why that work deliberately didn't happen, which is audit value the kernel doesn't need but the instance does. Pure state. No exceptions.

---

### Patterns observed

1. **The IB database is already kernel-clean by construction** — 73/73 state; the litmus needs no per-item enforcement here, only the (already-true) rule that nothing globs IB bodies into context.
2. **Status frontmatter is the archive.** Done/Cancelled partitioning via `status:` + grep-listing makes physical re-homing strictly cost-with-no-benefit; this generalizes to any row-per-file governance database.
3. **Pre-DD-116, IB closure notes absorbed session reports and even architectural rulings** (IB-155/159–166 monsters; IB-164 amendment) — direct evidence for the Phase 2 second-brain design: work-records were the overflow home for learnings that now route to DD/knowledge/IB per the session-138 ruling.
4. **Deferred is a visibility dead zone:** both Deferred items (IB-102/103) fell out of PROGRESS and rotted for months; whatever survives this audit should either carry a PROGRESS line or a trigger, never bare "Deferred".
5. **PROGRESS's "work items carry IB numbers" claim is ~70% true** — 9 unnumbered lines, of which 2 are genuinely work-shaped; decide number-them vs soften-the-claim at the next maintenance pass.
6. Notion-era imports (blank bodies, `notion_id`, URL-shaped `design_decision` fields) are inert but schema-noisy; harmless, not worth a cleanup pass on its own.
# Substrate Audit — Design Notes Class

## Design Notes (17 audited)

*(Folder holds 17 files — 16 dated notes + `_index.md` — not 18 as scoped; ls verified 2026-07-12.)*

**Plain-English summary.** The folder is two populations wearing one label. Ten notes are finished deliberation — the April monsters plus the June gate-inputs — whose every surviving decision was ratified into DDs (DD-91, DD-93–101, DD-103, DD-111, DD-112) or shipped as the concept-doc layer; they are pure state and can be archived wholesale (~230KB of the ~380KB). But four notes quietly became load-bearing runtime substrate: the Librarian read-contract and use-case registry are delegated to by path from 9–14 live concept docs, the boundary-case tracking note is the schema source for the `/assess-*` skills, and the audit-system design contract is the living contract for `/audit-artifacts`. Under the kernel litmus those are kernel (a downstream consumer of the Librarian layer would pull them) and belong in `operations/references/`, not in a deliberation folder — which is exactly the DD-112 home rule this folder violates. Two notes additionally dangle against DD-116's System-Log retirement (boundary-case encounters write to `operations/system-log/`; DD-90 telemetry lives on SL entries) and need a reconciliation ruling, not just a move.

### Per-note verdicts

| filename | date | size | kernel/state | verdict | what survives distillation |
|---|---|---|---|---|---|
| 2026-04-20-artifact-acceptance-rubric.md | 2026-04-20 | 16K | state | **archive** | Nothing new — per-form acceptance thinking lives on in `operations/references/form-classification-rubric.md` and the DD-93–101 bundle (DD-97 extension-first); zero live refs, no DD cites it |
| 2026-04-20-artifact-lifecycle-spec.md | 2026-04-20 | 34K | state | **archive** | Nothing — fully ratified into DD-93–DD-101 (all Binding, each cites this note as provenance) |
| 2026-04-20-pipeline-collapse-proposal.md | 2026-04-20 | 32K | state | **archive** | Nothing — partially adopted via the DD-81/DD-93–102 bundle; the guides+patterns-only collapse was never executed and DD-111's two-bodies reframe superseded it; zero live refs |
| 2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md | 2026-04-20 | 43K | state | **archive** | Nothing — Option α' was validated (spot-check note), built as the `operations/references/librarian/` concept-doc layer, and is live; 2 provenance pointers (`librarian/_index.md`, `runtime-environment.md`) to leave or mechanically repoint |
| 2026-04-21-agent-reflections-to-proposals-architecture.md | 2026-04-21 | 32K | state | **archive** | Nothing — ratified as DD-91; `/solicit-proposals` + `reflection-prompt.md` ship the template and round mechanics |
| 2026-04-21-contract-section-spotcheck-agent-audit.md | 2026-04-21 | 30K | state | **archive** | Nothing — empirical PASS evidence for Option α'; cited as provenance by `skill.md`/`audit.md`/`librarian/_index.md` (historical citations, fine pointing at archive path) |
| 2026-04-21-librarian-read-contract.md | 2026-04-21 | 31K | **kernel** | **re-home** → `operations/references/librarian/read-contract.md` | The whole document — 9+ concept docs and `agents/librarian/workflows/cross-concept-subagent.md` delegate governing sections (§Step-1 verb extraction, §8.x input handling) to it by path; it is the Librarian's live query-execution protocol, misfiled as deliberation (DD-112 home rule) |
| 2026-04-21-librarian-use-case-registry.md | 2026-04-21 | 24K | **kernel** | **re-home** → `operations/references/librarian/use-case-registry.md` | The 35-UC registry + registry-update process — ~14 live concept docs cite UC anchors; `librarian/_index.md` names its update process as the prioritization protocol for future authoring |
| 2026-04-21-session-telemetry-harness-requirements.md | 2026-04-21 | 16K | state | **archive** | §6 harness requirements as optional Phase-4 feedstock (note in restructure plan, don't copy); flag **DD-90 as mooted by DD-116** (telemetry schema lives on retired SL entries) — supersession/scope note alongside the planned DD-59 note |
| 2026-04-22-librarian-boundary-case-tracking.md | 2026-04-22 | 22K | mixed | **distill** → encounter taxonomy (13 types) + entry schema into `operations/references/librarian/boundary-cases.md`; then archive | The taxonomy/schema/routing that `/assess-skill` (and siblings) delegate to by path; the write destination `operations/system-log/` **conflicts with DD-116 SL-producer retirement** — needs a Nick ruling on where encounters land now (candidate: IB-172 layered-memory feedstock) |
| 2026-06-12-audit-system-design-contract.md | 2026-06-12 | 22K | **kernel** | **keep** (re-home candidate, later pass) | Entire note — living design contract for `/audit-artifacts` (SKILL.md delegates its invariant-candidate list and drift-update rule to it; DD-110 cites it); `stage: stable`, not deliberation-in-progress |
| 2026-06-18-engine-collapse-restructure-plan.md | 2026-06-18 | 17K | state | **archive** | Nothing — plan executed, ratified as DD-103; also shape-misfiled (it is a plan; `operations/plans/` → archive is its natural lineage) |
| 2026-06-20-extracts-knowledge-reconciliation.md | 2026-06-20 | 8.7K | state | **archive** | Nothing — two-bodies frame ratified as DD-111 (rename-in-place); `extracts/CLAUDE.md` + IB-170 hold provenance pointers |
| 2026-06-21-dd-wisdom-caching-policy.md | 2026-06-21 | 9.0K | mixed | **distill** → the 4-criteria cache policy + exclusions + anti-redundancy invariant into a DD (decision-shaped, per DD-116 routing); then archive | The policy is live law with no DD: `governance/agent-rules.md` justifies its DD-37 cache "per the DD-wisdom caching policy" — a Binding rule should not anchor to a draft note |
| 2026-06-21-ib170-concept-doc-placement.md | 2026-06-21 | 6.8K | state | **archive** | Nothing — ratified as DD-112 (home rule + harness/runtime-environment split, executed) |
| 2026-06-22-agentic-os-direction.md | 2026-06-22 | 9.6K | kernel (direction) | **keep** | All of it — live North Star: referenced by PROGRESS.md, the restructure program plan (§2 builds directly on it), research-dimensions, link-intake-protocol, watched-libraries; revisit only after Phase 4 pins scope |
| _index.md | 2026-04-22 | 3.0K | state | **keep + update** | MOC survives; rewrite "What belongs here" to exclude living reference material (registries, read contracts, spot-check reports — the very classes that made this folder load-bearing) per the kernel litmus |

**Tallies:** archive 10 · re-home 2 · distill-then-archive 2 · keep 3.

### Patterns observed

1. **Two populations, one folder:** finished deliberation (state) and living operational reference (kernel) — the folder's `_index.md` explicitly invited both ("use-case registries", "read contracts", "spot-check reports"), which is how it became load-bearing.
2. **The note→DD-bundle→ship pattern is healthy:** every April monster's surviving content is in Binding DDs; once ratified, the note is pure provenance and the DD corpus carries the ruling — archiving loses nothing.
3. **Live surfaces delegate to design notes by path** (concept docs → read-contract §8.x; skills → boundary-case schema) — a DD-112 home-rule violation predating DD-112; the kernel litmus and the live-reference test give the same answer on every file.
4. **DD-116 left two danglers here:** boundary-case encounters route to the retired SL, and DD-90's telemetry schema lives on SL entries — both need explicit reconciliation, not silent archival.
5. **Zero live refs reliably predicts archive:** the three notes nothing cites (acceptance-rubric, pipeline-collapse, and effectively session-telemetry) are all superseded state.

### Proposed archive destination convention

`systems/improvement-loop/archive/design-notes/` — filenames preserved, no stubs. Consistent with the fractal pattern's system-scoped `archive/` and with existing precedent (`archive/handoffs/` from Phase 0, `archive/improvement-proposals/`). Pointer policy: (a) live load-bearing pointers (skills, concept docs, workflows) are rewritten **before** any move — that is what forces the two re-homes; (b) provenance citations in immutable records (DDs, HISTORY.md) are left untouched — the file still exists at the archive path, and mechanical path-rewrites inside DDs are avoidable churn. All moves Nick-gated per the Phase-2 contract.
# Substrate audit — System Log class

## System Log (153 entries)

The System Log corpus is 153 entries in `systems/improvement-loop/operations/system-log/` spanning 2026-03-01 to 2026-06-22, and it is unambiguously **state, not kernel** — no downstream consumer would pull another instance's change ledger. The session-138 ruling (retired as producer, corpus kept read-only as IB-172 feedstock) is confirmed; nothing in the corpus argues otherwise. The corpus itself costs nothing at cold start, but the retirement was only executed on the *named* producers — ten live skills still carry write paths or freshness-assuming read paths into the folder, and one (`/extract-artifacts`) will **hard-fail on its next non-guide write** because it validates a `--sl` stem against an SL entry that can no longer exist. From a ~13-body sample, most learning-shaped entries routed their *action* at the time but left their *calibration data and generalizable patterns* entry-local — that residue is exactly the IB-172 distill feedstock.

*(Note: DD-59's path map also covers 22 Household OS + 4 Claude Build entries now under `archive/` — read-only history per the DD-103 amendment; not audited here.)*

---

### 1. Class-level disposition

**Verdict: KEEP IN PLACE — state (not kernel), read-only feedstock for IB-172. Confirms the session-138 ruling and DD-116.**

Kernel litmus: no downstream consumer of the engine's governance kernel would pull this instance's operational change ledger; only this instance (specifically the IB-172 layered-memory design) needs it. The plan's own examples name "ops byproducts" as state. Archive-move is *not* recommended: DD-116 explicitly keeps the corpus in place, `/sl read`/`/track sl` path maps point at the current location, and IB-172 will read it soon — moving it now buys nothing and breaks two skills' path maps.

**Does the corpus cost anything at read time?** The files themselves: no — nothing reads them at cold start (PROGRESS.md is the sole cold-start artifact per DD-116). The residual *wiring*, however, is not retirement-clean. Full census of `system-log` references across `.claude/skills`, IL `.claude/skills`, and `agents/` trees:

**Retirement-aware (correct, no action):**

| Surface | State |
|---|---|
| `/sl` (`/Users/nickgogan/MetaSystem/.claude/skills/sl/SKILL.md`) | RETIRED AS PRODUCER banner; read/list only |
| `/track` (`.claude/skills/track/SKILL.md`) | `sl create` marked RETIRED (line 83); read paths live |
| `/governance-audit` (`.claude/skills/governance-audit/SKILL.md`) | SL proposals retired (line 19) |
| `/session-handoff` | Aligned with DD-116 (commit 5cba938) |

**NOT retirement-aware — still producer-shaped or freshness-assuming (Phase-2 follow-ups):**

| Surface | Problem | Severity |
|---|---|---|
| `/extract-artifacts` (`systems/improvement-loop/.claude/skills/extract-artifacts/SKILL.md` lines 50, 474–487) | Requires `--sl STEM` on every non-guide artifact write (DD-95 provenance), validated against `operations/system-log/<stem>.md` existing — **functionally broken**: with no new SL entries, every future non-guide write aborts. Provenance anchor needs re-pointing (commit hash / HISTORY entry). | **High — breaks a pipeline stage** |
| 7 Librarian surfaces: `/assess-skill`, `/assess-agent`, `/assess-prompt`, `/ask-kb`, `/compare-repos`, `/design-skill`, `/design-agent` | Encounter-log write contract appends to `operations/system-log/session-<N>-librarian-encounters.md`, and `<N>` is *inferred from the most recent session SL entry* — both the write target and the numbering source are retired. (Mitigating: zero encounter logs were ever written in 27+ sessions — see `dropped-summarize-encounters` entry.) | Medium — dormant but contract-invalid |
| `/solicit-proposals` (SKILL.md line 123 + reflection-prompt.md line 82) | Writes a round record to `operations/system-log/{date}-solicit-proposals-round.md` | Medium — will produce a new SL entry on next round |
| `/system-audit` (line 144), `/system-health` (line 117) | Read the 10 / 5 "most recent" SL entries assuming a live log — will now read a frozen June corpus as if current, or misread silence as drift | Low — staleness hazard |
| `librarian-reads.md` (inside the corpus folder) | Not a log entry — a live rolling Tier-3 read log (read-contract §5.3), currently empty, designated to *append* inside the now read-only folder | Low — needs a re-home ruling or an explicit carve-out |
| `agents/owner/agent.md` (lines 148, 161), `.claude/agents/owner.md` (line 65) | Read-only path-map rows; harmless but should note "historical/read-only" | Cosmetic |

Minor corpus hygiene (fold into any IB-172 pre-pass, not worth standalone action): 2 entries lack a `date:` field (`session-128-*` pair; one uses `timestamp:` instead), ~8 entries have empty `change_type`, and the folder mixes three file types (log entries, the rolling read log, the encounter-log convention).

---

### 2. Unrouted-learning scan (distill candidates for the IB-172 pass — NOT for immediate action)

Method and honesty caveat: 153 titles + frontmatter scanned, 13 bodies read. **Title-scanning cannot establish routing status** — whether a learning later landed in a DD/knowledge/IB is only verifiable by reading the entry body *and* grepping the destination. Roughly 110 of 153 entries are `Implementation`/`Update` session records whose content is duplicated by git + (backfilled) HISTORY.md — no learning payload, pure feedstock. The candidates below come from the ~15 learning-shaped entries (`Operational Learning`, `Operational`, `Data Integrity`, decision-bearing `Update`); sampled ones are verified, title-only ones are marked.

1. `enables-migration-85-percent-error-rate.md` (verified) — the "definitional, not functional, dependency" test for correct *enables* links and "default to same-problem during migrations" heuristic; the anti-patterns were routed into `/finding-crosslink`, but this sharper test appears entry-local.
2. `summary-only-crosslink-evaluation-false-positive-discovery.md` (verified) — type-specific error-rate calibration baseline (contradicts ~0%, enables ~40%, same-problem ~60%); mitigations routed, the calibration table itself lives only here.
3. `transcript-extraction-8x-pattern-density.md` (verified) — the content-type miss hierarchy (implementation details 31% > named patterns 23% > …); the transcript-first principle was codified, the measurement data was not.
4. `source-finding-misattribution-discovery.md` (verified) — "title-based matching is a known failure mode; transcript verification belongs in the extraction quality gate" — partially absorbed by two-pass extraction, never stated as a pattern in `knowledge/`.
5. `session-85-codifier-subagent-queue-mutation-discipline.md` (verified) — partition-by-queue-file writer serialization is a *generalizable* subagent-concurrency pattern, routed only into one skill's Step 4.8; its logged-for-future list (codifier calibration reflection, DD-98 split-trigger watch, harvest-queue replenishment) may still be open work → IB check.
6. `dropped-summarize-encounters-from-il-priority-queue.md` (verified) — the producer-side diagnostic ("assess-* skills never invoked on real consumer artifacts") was explicitly deferred as "a separate diagnostic, not a skill build" and never became an IB.
7. `session-127-frontmatter-yaml-hygiene-sweep.md` (verified) — the A/B/C YAML defect-class taxonomy; the prevention mechanism shipped (DD-114), the taxonomy is entry-local.
8. `token-economy-overhaul-context-files-slimmed.md` (title-only) — token-economy rationale is a standing Nick principle; whether the concrete overhaul heuristics landed in `knowledge/` is unverified.
9. `enables`-adjacent: `first-full-kb-crosslink-pass-completed.md` + `summary-only…` together imply a "bulk-classification degrades threshold discipline" meta-pattern (verified across two bodies) — pattern-shaped, unrouted.
10. `session-127-harness-whole-system-invariants-confirmed-deferred.md` (title-only, `Decision` type) — a deferred decision that may need an IB/DD trace check.

---

### 3. Draft DD-59 scope note (for Nick's approval — appended to DD-59 as a note, not a supersession)

> **Scope note (2026-07-12, session 138; codified in DD-116; filed via the restructure program's Phase-2 substrate audit).**
> The System Log is **retired as a producer**: no agent or skill creates new SL entries, in any system.
> Session tracking is carried by git (Conventional Commits) + `HISTORY.md`; learnings route by shape —
> decision-shaped → a DD, pattern-shaped → `knowledge/`, work-shaped → an IB item.
> The historical corpus in `operations/system-log/` stays in place, **read-only**, as feedstock for the
> IB-172 layered-memory design; archived systems' folders remain read-only history per the DD-103 amendment.
> DD-59 remains **Binding** for what it actually decided — the system-scoped *placement* of System Log data —
> and the path map above still governs where the historical corpus lives and how to find entries.
> This note narrows only the producer side; it is not a DD-44 supersession.

---

### Patterns observed

- The corpus splits into three eras: Notion-import records (Mar), dense operational learnings (Apr), and session records duplicating git/HISTORY (Apr–Jun) — the third class is what validated the retirement.
- Learning entries consistently routed their *fix* but stranded their *calibration data* — the data, not the prose, is the IB-172 payload.
- `operations/system-log/` had quietly become a mixed namespace (log entries + rolling read log + planned encounter logs); read-only status now surfaces those placement conflicts.
- Retirement was executed on named producers only; second-order writers (provenance validators, encounter-log contracts, round records) were missed — a sweep pattern worth repeating for any future surface retirement.
- Every "helper writes into an ops folder" contract embeds a freshness assumption somewhere (`infer <N> from most recent entry`); freezing a folder invalidates inferences, not just writes.
## Guides

**Summary (plain English).** Nick's suspicion is confirmed: `knowledge/guides/` does not carry the system. It holds exactly two guides, and both are secondary surfaces — the pipeline guide restates what the engine CLAUDE.md, the DDs (DD-80/DD-29/DD-111), and the skill files already carry, and the skill-authoring guide was deliberately slimmed (session 124) to a syntax cheat-sheet after its design substance moved to the Librarian concept docs. The real depth lives in `operations/references/librarian/*.md`, the G-guides in `extracts/guides/`, and the DDs. The right move is not to rebuild these guides but to fold their unique content into the kernel docs the restructure program defines ("how it works" + "harness description") and let the class dissolve. The synthesized guides in `extracts/guides/` should stay exactly where they are (DD-111 rename-in-place) — they are research-KB state consumed in place by heavily path-coupled assessors; if the kernel later needs generalized asset-form definitions, distill *from* them rather than relocating them.

---

### 1. Authored guides — `knowledge/guides/` (content audit)

#### 1a. `research-to-codification-pipeline.md` (~11KB)

- **Verdict: fold-into-kernel-doc** (then archive the original).
- **Tag: kernel-shaped content in a state-shaped wrapper.** "How the engine's pipeline works" is precisely the kernel's *how it works* component (plan §2: "the point of the system · how it works"). A downstream consumer adopting the DBDO pipeline would pull this — litmus says kernel. But the file as written is not the kernel form of it.
- **Evidence:**
  - **Duplication:** the 4-stage pipeline table appears in engine `CLAUDE.md` (§The Pipeline) with the same stages/skills/gates; the decisions it narrates live in DD-80, DD-29, DD-39, DD-111; the procedures live in the four SKILL.md files. The design-note `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md` already classifies this guide as a **DD cache** (caches the DD-80 cluster, 7 DDs).
  - **Drift magnet:** it embeds a "Current State" status table (lines 165–177) — per-session-maintenance content the token-economy rule forbids. `HISTORY.md:115` records drift already being fixed in it once.
  - **Thin inbound coupling:** only two live by-name consumers outside its own folder — the engine `CLAUDE.md` reference-table pointer (line 226) and `operations/references/form-classification-rubric.md:412` (a "Related" link). Cheap to fold; two pointers to update.
- **Fold destination:** the kernel's *how-it-works* doc gets the stage/gate model and the DD-111 two-bodies framing (its genuinely good synthesis); the "Current State" table and status commentary are instance state and go to PROGRESS/HISTORY semantics, i.e. dropped.

#### 1b. `skill-authoring-guide.md` (~3.7KB, retitled "SKILL.md Mechanics Reference")

- **Verdict: keep** as-is now; **re-home into the kernel's harness-description doc** when Phase 4 builds it.
- **Tag: kernel** (harness reference). A downstream consumer instantiating on a Claude Code harness would pull exactly this — frontmatter fields, invocation control, variables, scope table. Under the target model, harness mechanics belong in the kernel's *harness description* / materialization layer, not in engine knowledge.
- **Evidence:** it already did its distillation — the header explicitly delegates design guidance to `operations/references/librarian/skill.md` §Construction and `/design-skill` (verified: that concept doc carries the Decision sequence; this file carries only syntax). Content is factual, low-maintenance, non-duplicative. Inbound references are weak (dd-wisdom-caching-policy table, `_index.md`, one old system-audit line). One watch-item: the newly imported `/meta-skill-author` toolchain ships a platform-matrix reference with overlapping harness-mechanics scope — check overlap when assigning its owner in this Phase-2 audit.

#### 1c. `_index.md` (~1.2KB)

- **Verdict: rebuild (trim) or delete.**
- **Tag: state** (catalog).
- **Evidence:** stale pre-collapse language ("across the Household OS"), a hardcoded 2-row catalog table sitting directly above a Dataview query that renders the same thing, last updated 2026-04-07. Workspace Process Rule 1 limits kept `_index.md` files to Dataview-driven live views — the hardcoded table violates that. If the two guides fold/re-home as above, the folder empties and the index deletes with it.

**Class verdict:** `knowledge/guides/` as a class is dissolvable. It was designed (DD-45-era) as the deployment target for synthesized guides, but that flow never ran into it — DD-111 recognized `extracts/guides/` as the live substrate instead, and `extracts/guides/CLAUDE.md` still names `knowledge/guides/` as its "deployment target," a pointer that is now fiction and should be corrected in the same pass.

---

### 2. Synthesized guides — `extracts/guides/` (placement only)

**Class verdict: keep in place — state (research-KB substrate), consumed in place; graduate by distillation, not relocation.**

Rationale (8 lines):
1. The plan rules the research KB is state by fiat; these are synthesized *from* findings and remain source-coupled (`/detect-drift` exists precisely because they drift with sources) — that is state behavior, not kernel behavior.
2. What a downstream consumer actually pulls is the **assessment capability** (the `/assess-*` skills + Librarian concept docs), not the G-guides themselves; the guides are that capability's internal substrate.
3. Coupling is heavy and directory-literal: 58 non-archive files reference `extracts/guides` by path; `operations/references/guide-routing-table.md` hard-codes every `G# → extracts/guides/<file>.md` mapping; `/assess-skill`, `/assess-agent`, `/assess-prompt` each name the directory in their substrate tables (SKILL.md lines 62/54/64) and resolve G-numbers through the routing table. So yes — path-coupled, via one indirection layer (the routing table) that would localize a future move to one file plus the three skill tables.
4. DD-111 (Binding, 2026-06-21) already adjudicated exactly this question and chose rename-in-place over relocation on Rule-11 grounds; nothing in the kernel model invalidates that — it strengthens it, since the kernel is "export unit by construction, not by sweep."
5. If Phase 4's kernel needs *generalized asset-form definitions* (skills/agents/rules as markdown with adaptation commentary), the right move is to **distill** those from the G-guides' Contract subsections into new kernel docs — the G-guides stay behind as their evidence base.

**Exceptions (behave differently from the class):**
- `*.harvest-queue.md` (10 files, ~170KB total) — synthesis working byproducts, pure ops state, not substrate; archive candidates in this audit's sweep.
- `managing-agent-context.md` (G2, 102KB) — marked **deprecated** in the routing table (split into G2a/G2b) but still on disk; archive candidate.
- `changelog/` and `CLAUDE.md` — meta, fine; but `CLAUDE.md` line 5 still calls `knowledge/guides/` the deployment target (stale post-DD-111; fix wording).

---

### 3. Placement check — `knowledge/patterns/` and `knowledge/templates/`

Both exist and both are **kernel-shaped**, which makes their current placement acceptable now but destined for the kernel's *generalized forms* section rather than for state. `knowledge/patterns/` holds exactly two deployed patterns (`capability-type-selection.md`, `upstream-dependency-spectrum.md`) — both are generalized decision rubrics a downstream consumer would pull (litmus: kernel), and the session-128 SL entry already flagged them as "policy-in-disguise" awaiting reconciliation; that reconciliation should land as fold-into-kernel, not as a rewrite in place. `knowledge/templates/` (agent-templates, skill-templates, prompt-templates, project-scaffold, schematic-template, environment-manifest.json) is the closest thing the engine already has to the kernel's "generalized forms of every asset" — it is kernel by construction and should be the seed of that section when Phase 4 defines the descriptor. One dead item: `system-log-template.md` (updated 2026-06-22) templates a producer retired by DD-116 — archive it. No moves proposed now; tag both folders kernel-destined in the audit ledger.

---

### Patterns observed

- Confirmed: the authored guides are restatement layers; the load-bearing depth consistently lives one level down (concept docs, G-guides, DDs, SKILL.md files).
- Recurring drift magnets: "Current State" tables and hardcoded catalog tables inside knowledge docs — every one found had already drifted.
- Path coupling to `extracts/guides/` is wide (58 files) but funneled through one routing table — indirection layers are what make future kernel moves cheap.
- The kernel model resolves `knowledge/`'s identity crisis cleanly: guides → kernel *how-it-works*/harness docs; patterns + templates → kernel *generalized forms*.
- Pre-collapse language (Household OS) survives in low-traffic `_index.md` files — index files rot fastest.
- DD-111's "distill, don't relocate" instinct generalizes: every graduation proposed here is a fold or distill, never a folder move.
# Substrate Audit — Concept-Doc Homes (DD-112 rule vs the kernel model)

**Class:** concept-doc homes · **Phase:** 2 (engine restructure program) · **Date:** 2026-07-12
**Rule under re-examination:** DD-112 (`project-management/design-decisions/DD-112.md`, Binding)
**Litmus applied:** *if a downstream consumer would pull it, it's kernel; if only this instance needs it, it's state.*

## Concept-Doc Homes

**Plain-English summary.** The apparent conflict — "concept docs describe generalized abstractions, so they look like kernel material" — dissolves on inspection. The kernel's "generalized forms of every asset" means generalized forms of *this system's own* assets (its skills, agents, rules, hooks), not reference docs about abstractions in general; the Librarian concept/operation docs are pointer files whose composition pointers resolve into the research KB, which the program plan explicitly classifies as **state** — a doc made of pointers-into-state cannot travel in a kernel without arriving broken. So DD-112's placement of all concept docs under `operations/references/librarian/` is *confirmed*, not contradicted, by the kernel model. The one genuine kernel-shaped pocket is on the other side of DD-112's table: `knowledge/reference/` design-wisdom (`fractal-pattern.md`, `vocabulary.md`, and to a lesser degree `dbdo-pipeline.md`) already has downstream pull — workspace cross-system rules direct every system to `vocabulary.md`, and `fractal-pattern.md` defines the structure of every system the engine produces. No re-home is recommended now because the kernel target (`governance/` as portable kernel) does not exist until Phase 5; every verdict below is therefore "keep" today, with the design-wisdom rows flagged for Phase 5. Any change touching DD-112 is a **Nick-gated supersession/amendment (DD-44)**.

### Population (discovered)

Four homes hold concept-doc-class material:

1. `operations/references/librarian/` — the Librarian reference layer: 11 `type: concept` + 9 `type: operation` pointer files + `_index.md` (load-bearing substrate map). This is what `/assess-*` and `/design-*` compose (audit.md × skill.md, design.md × agent.md, etc.).
2. `operations/references/` (top level) — operational reference the engine consults at runtime: rubrics, routing tables, dimensions, registries.
3. `knowledge/reference/` — engine self-knowledge / design-wisdom: 3 docs + `_index.md`.
4. `agents/{name}/` — agent-scoped helper files (DD-112 explicitly left these agent-private; sampled: `agents/librarian/agent.md`, `agents/librarian/workflows/`).

### Per-file verdicts

All paths relative to `/Users/nickgogan/MetaSystem/systems/improvement-loop/`.

| file | current home | kernel/state | keep / re-home | proposed home under kernel model | rationale (≤1 line) |
|---|---|---|---|---|---|
| `agent.md` (concept) | `operations/references/librarian/` | state | keep | same | Pointer file into research-KB guides/findings — pointers-into-state; only the engine's assess/design skills consume it. |
| `agentic-systems.md` | `operations/references/librarian/` | state | keep | same | Same: KB-pointer substrate for engine query decomposition. |
| `context-rot.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `harness.md` | `operations/references/librarian/` | state | keep | same | Same; DD-112's own relocation target — placement confirmed under litmus. |
| `mcp.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `memory.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `prompt.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `prompt-caching.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `runtime-environment.md` | `operations/references/librarian/` | state | keep | same | Same; DD-112's disambiguation rename — no kernel bearing. |
| `second-brain.md` | `operations/references/librarian/` | state | keep | same | Same (content feeds Phase 2 second-brain design, but the doc is engine substrate). |
| `skill.md` (concept) | `operations/references/librarian/` | state | keep | same | Same. |
| `audit.md` (operation) | `operations/references/librarian/` | state | keep | same | Verb-keyed procedure the engine's own skills compose; instance machinery. |
| `coverage.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `decide.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `design.md` (operation) | `operations/references/librarian/` | state | keep | same | Same. |
| `diagnose.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `explain.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `fetch.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `plan.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `whats-new.md` | `operations/references/librarian/` | state | keep | same | Same. |
| `_index.md` | `operations/references/librarian/` | state | keep | same | Load-bearing substrate map (Process Rule 1 exemption); state by definition. |
| `consumer-abstractions-map.md` | `operations/references/` | state | keep | same | Promotion-gating table for the engine's own substrate investment; instance-only. |
| `form-classification-rubric.md` | `operations/references/` | state | keep | same | Form Router decision spec — engine pipeline machinery. |
| `guide-routing-table.md` | `operations/references/` | state | keep | same | Routing into KB guides (state); pointers-into-state. |
| `research-dimensions.md` | `operations/references/` | state | keep | same | Scopes the engine's own research scanning; instance-only. |
| `model-capability-registry.md` | `operations/references/` | state (today) | keep | same | Downstream value is plausible but no concrete pull demand (Rule 11); revisit only on demand. |
| `link-intake-protocol.md` | `operations/references/` | state | keep (superseded/history) | same | Already superseded by `/link-intake` skill; historical record, not a placement question. |
| `fractal-pattern.md` | `knowledge/reference/` | **kernel-shaped** | keep, revisit at Phase 5 | Phase 5 candidate: `governance/` kernel ("how any produced system is structured") | Downstream consumers demonstrably pull it (DD-52 structure of every produced system) — but the kernel target doesn't exist yet; no concrete conflict today. |
| `vocabulary.md` | `knowledge/reference/` | **kernel-shaped** | keep, revisit at Phase 5 | Phase 5 candidate: `governance/` kernel (shared terminology) | Workspace Cross-System Rule 3 directs all systems to it — an existing downstream pull; same no-target-yet reasoning. |
| `dbdo-pipeline.md` | `knowledge/reference/` | mixed | keep, revisit at Phase 5 | likely stays; content may be *distilled into* the kernel's "how it works" doc | "How this engine works" is kernel *content*, but the doc itself may be self-knowledge that gets summarized, not moved. |
| `_index.md` | `knowledge/reference/` | state | keep | same | Dataview catalog; also stale (Household-OS framing, missing rows) — flag for `/maintain-docs`, not a placement issue. |
| `agents/librarian/agent.md` (+ peers under `agents/{name}/`, incl. `workflows/`) | `agents/{name}/` | state (today) | keep, revisit at Phase 5 | Phase 5: kernel gains a *generalized form* of each agent; `agents/` remains the materialization | Agent definitions are exactly what the kernel generalizes — but generalized forms are *derived* kernel docs, not re-homed originals (DD-112's Rule-11 stance holds). |

### Does the DD-112 rule still hold per home?

- **`operations/references/librarian/` — holds.** DD-112 placed concept docs as "operational reference the engine consults at runtime." The litmus reaches the same answer independently: these are pointer files into state (the research KB), consumed only by this instance's skills. The "generalized abstractions = kernel material" reading conflates *docs about generalized abstractions* with *generalized forms of the system's own assets*; the kernel model means the latter. No conflict; a downstream consumer pulling the kernel would expect the *system's* generalized skills/agents/rules — not the engine's private audit substrate.
- **`operations/references/` (top level) — holds.** Same reasoning; rubrics/routing/dimensions are engine machinery.
- **`knowledge/reference/` — holds today, pressured at Phase 5.** DD-112 calls this "engine self-knowledge," but two of its three docs already have cross-boundary downstream pull, which the litmus classifies as kernel. This is the only concrete tension found — deferred because the kernel home doesn't exist until Phase 5 kernel construction (re-homing now would just create a different anomaly).
- **`agents/{name}/` — holds.** DD-112's agent-scoped carve-out survives; the kernel will hold *derived generalized forms* of agents, not the working helper files.

**Nick gate:** every verdict above is a proposal only. Any re-home or rule change touching DD-112 requires a Nick-gated supersession or amendment per DD-44 and workspace Hard Constraint 3.

### Patterns observed

1. DD-112 **survives the kernel model as-is** — no supersession needed now; the litmus independently reproduces its concept-doc placement.
2. At Phase 5, DD-112 likely needs a **Nick-gated amendment, not a supersession**: add a third home row (`governance/` = kernel: constitution docs + generalized forms of the system's own assets) to its two-home table — the placement logic ("home by what it is") extends cleanly.
3. The pressure point is `knowledge/reference/`, not the Librarian layer: `fractal-pattern.md` and `vocabulary.md` already behave like kernel docs (downstream pull exists today).
4. Recurring discriminator worth carrying into Phase 5: **pointers-into-state can never be kernel** — it cheaply classifies every Librarian-layer file and will classify future reference docs.
5. Minor hygiene (out of scope, no gate needed): `knowledge/reference/_index.md` is stale (Household-OS framing, catalog missing `household-os/` removal context) — route to `/maintain-docs`.
