---
title: "Governance-health audit — DD corpus coherence + DD↔IB↔git mapping"
audit_type: "governance-health"
target_system: "improvement-loop"
date: "2026-06-21"
session: 125
phase: "Phase 1 — read-only diagnostic"
status: "Phase 1 fixes applied (A/B/C/D approved at gate; F held)"
---

# Governance-Health Audit — Session 125, Phase 1

Read-only diagnostic of the IL governance corpus: DD internal coherence, supersession-chain
integrity, and DD↔IB↔git linkage in both directions. All counts are **point-in-time at audit**
(2026-06-21); they are audit observations, not prose to be maintained.

## Method

- Deterministic frontmatter + body-reference extraction across all DDs and IBs (no sampling).
- Supersession-chain resolution for every `status: Superseded` DD.
- Archive cross-check for every body reference that resolves to no live DD file.
- Git presence check for the live-era DD set (DD-100..DD-110).
- `/governance-audit` and `/system-audit` were **considered and deliberately not invoked** — see
  "Engines not run" below.

## Headline verdict

The corpus is **structurally healthy**: no filename↔`decision_id` mismatches, no truly broken
internal references, every Superseded DD resolves (eventually) to a Binding decision, and every
live-era DD is commit-backed. The defects are **traceability hygiene**, not contradictions:
machine-untraceable supersession metadata, documentation that enumerates a stale superseded set,
bare cross-boundary references into the archive, and a few open IBs whose rationale points at
superseded DDs.

At audit: **79 DDs** (70 Binding, 9 Superseded); **70 IBs** (52 Done, 13 Cancelled, 3 Queued,
2 Deferred). Live IL DD range is DD-29..DD-110; DD-01..DD-28 are archived (Household OS) and
DD-33/34/49 are archived (Claude Build) — the federation-collapse boundary.

---

## Findings

### A. Documented superseded set is stale (DOC DRIFT)

`CLAUDE.md` (project root) and the session handoff both enumerate the superseded set as
**"DD-35, DD-43, DD-48."** Reality at audit is **9 Superseded DDs**:
`DD-30, DD-32, DD-35, DD-43, DD-45, DD-46, DD-48, DD-65, DD-72`.

The 6 undocumented ones (DD-30/32/45/46/65/72) are *correctly* marked Superseded — the
documentation simply never kept up. This is a hardcoded list that drifted (the failure mode
Process Rule 3 exists to prevent). **Fix:** replace the enumeration with a frontmatter-filter
instruction ("active set = `status: Binding`; superseded = `status: Superseded`"). Removes a
recurring maintenance tax.
**Class:** hygiene, but edits the constitutional `CLAUDE.md` → **gate the wording**.

### B. `superseded_by` frontmatter is inconsistently populated (TRACEABILITY)

The supersession chain is only partially machine-traceable. Of the 9 Superseded DDs:

| DD | superseded_by (frontmatter) | resolves to | target status |
|----|----|----|----|
| DD-30 | `DD-82` | DD-82 | Binding ✓ |
| DD-35 | `DD-65` | DD-65 | Superseded → (piecewise) |
| DD-72 | `DD-88` | DD-88 | Binding ✓ |
| DD-32 | *(empty)* — body: DD-103 | DD-103 | Binding |
| DD-43 | *(empty)* — body: DD-45 | DD-45 → DD-103 | Binding (2 hops) |
| DD-45 | *(empty)* — body: DD-103 | DD-103 | Binding |
| DD-46 | *(empty)* — body: DD-103 | DD-103 | Binding |
| DD-48 | *(empty)* — body: DD-57 | DD-57 | Binding |
| DD-65 | *(empty)* — **piecewise** | DD-82/80/83/86/89/91 | (no single successor) |

Only DD-30/35/72 carry the field. DD-32/43/45/46/48 record supersession in **body prose only** —
a frontmatter-as-source-of-truth gap. DD-65 is legitimately piecewise (its body documents the
split into DD-82/80/83/86/89/91 thoroughly), so it has no single successor to point to.
**Fix:** backfill `superseded_by` for DD-32/43/45/46/48 from their existing body prose; leave
DD-65 null with a `superseded_by: piecewise` marker (or schema-equivalent).
**Class:** supersession-adjacent metadata on immutable DDs → **gate** (low-risk, mechanics-grade).

### C. Bare cross-boundary references into the archive (LINEAGE CLARITY)

Live Binding DDs cite archived DDs without signalling they're archived:

- **DD-49** (archived → Claude Build; content **re-homed to DD-109**) is cited by 9 live DDs:
  `DD-47, DD-55, DD-56, DD-64, DD-65, DD-82, DD-103, DD-104, DD-109`. DD-109 citing it is correct
  (it *is* the re-home). The others cite DD-49 as if-live — a reader can't find it in the corpus.
- **Household OS DDs** (DD-01/02/12/14/28, archived → Notion) are cited by `DD-37, DD-40, DD-47,
  DD-48, DD-55, DD-58` — genuine historical/cross-boundary lineage.

**Fix (recommended, lightweight):** where DD-49 is cited as live governance, annotate
"(archived; re-homed to DD-109)". Leave clearly-historical Household OS citations as-is.
**Class:** lineage/content decision → **gate**.

### D. Open IBs sourced from Superseded DDs (RATIONALE DRIFT)

| IB | status | source_dd | source status | name |
|----|----|----|----|----|
| IB-102 | Deferred | DD-35 | **Superseded** | Design system-applicator skill spec |
| IB-145 | Queued | DD-45 | **Superseded** | Re-analyze GSD for version drift |

Both open items justify themselves with a decision that has since been superseded. Either the work
is stale (cancel) or the `source_dd` should re-point to the superseding decision (DD-35's piecewise
heirs; DD-45 → DD-103). IB-145 is already on the deferred-work list in the handoff.
**Class:** content/scope → **gate** (re-point vs cancel is Nick's call).

### E. Open IBs with no `source_dd` (MINOR)

`IB-148` (Build /session-handoff-review) and `IB-170` (Rationalize concept docs / knowledge/) are
Queued with no `source_dd`. Acceptable for exploratory/maintenance backlog, but neither carries a
rationale pointer. **Recommend:** a one-line rationale or a parent DD when they activate. Note only.

### F. `ib_items` reverse-link field is inconsistent and redundant (HYGIENE/POLICY)

DD-side `ib_items` appears in mixed formats — CSV (`IB-139, IB-140`), YAML-list fragments
(`- "IB-147`), and even a Notion URL (DD-43). It duplicates, in reverse, the authoritative
IB→DD `source_dd` link. Per token-economy / no-redundancy, maintaining both invites drift.
**Recommend:** treat IB-side `source_dd` as the single source of truth; stop maintaining `ib_items`
(or, if kept for Dataview, normalize the format). **Class:** policy → **gate**.

### G. Legacy IBs pointing to archived DDs (NO ACTION)

`IB-07/09/49/51/64/96/106/138` carry `source_dd` into archived Household OS / federation DDs. All
are Done or Cancelled — expected for archived-era work. No action; recorded for completeness.

---

## DD↔git reconciliation

- Working tree clean; `main` **in sync with `origin/main`**. The handoff's "10 unpushed commits"
  warning is stale — they were pushed. Nothing pending.
- Every live-era DD (DD-100..DD-110) is commit-backed (DD-103/104/105/106 → `84dccfb`;
  DD-107 → `d8af4dc`; DD-108 → `6392510`; DD-109 → `2ab8f79`; DD-110 → `3cb1c91`).
- `/governance-audit` (proposes unfiled DD/IB/SL from a git diff) would surface nothing this
  session — there is no uncommitted or untracked session work to mine yet.

## Engines not run (and why)

- **`/governance-audit`** — its input is an uncommitted/untracked git delta; the tree is clean, so
  it has nothing to propose right now. Re-run at session close after Phase 2 produces changes.
- **`/system-audit`** — its unique value-add over this report is the *non-DD* surface (fractal
  completeness, skill/agent contract integrity, feedback status), which is outside Phase 1's
  DD/IB/git scope. This audit went DD-by-DD deeper than `/system-audit` does. Offer: run it as a
  separate broad sweep if Nick wants the skill/agent dimension covered too.

---

## Proposed Phase 1 fixes (all GATED — nothing applied yet)

| # | Finding | Fix | Class | Files touched |
|---|---------|-----|-------|---------------|
| A | Stale superseded enumeration | Replace list with frontmatter-filter instruction | hygiene (constitutional doc) | `CLAUDE.md` |
| B | Untraceable supersession | Backfill `superseded_by` for DD-32/43/45/46/48; mark DD-65 piecewise | mechanics on immutable DDs | 6 DD files |
| C | Bare DD-49 refs | Annotate "(archived; re-homed to DD-109)" where cited as live | lineage | up to 8 DD files |
| D | Open IBs on superseded DDs | Re-point or cancel IB-102, IB-145 | scope | 2 IB files |
| F | Redundant `ib_items` | Adopt `source_dd` as single source; stop/ normalize `ib_items` | policy | policy note + DD files |

E and G are note-only.

**Recommendation:** apply **A and B** first (pure traceability hygiene, highest value, lowest risk),
hold **C/D/F** for an explicit decision since they touch lineage/scope/policy. Per the handoff,
nothing here is applied until the gate.

---

---

## Applied at gate (2026-06-21, Nick approved A/B/C/D; F held)

| # | What was applied |
|---|------------------|
| A | `CLAUDE.md:33` — replaced the hardcoded "Superseded: DD-35, DD-43, DD-48" with a `status: Binding`/`Superseded` frontmatter-filter instruction. |
| B | Backfilled the **schema-canonical `supersedes` field** (not the non-schema `superseded_by`) on the two superseding DDs that lacked it: `DD-45` → `supersedes: DD-43`, `DD-57` → `supersedes: DD-48`. All 9 supersessions are now machine-traceable via `supersedes`; DD-65 remains piecewise (documented in its body). Refinement vs the proposed framing: the schema defines `supersedes` (forward, on the new DD), which already covered 7/9 — only 2 pointers were actually missing, so this is 2 schema-correct edits instead of 5 non-schema ones. |
| C | Annotated 8 live-DD citations of archived **DD-49** with "archived → DD-109" (`DD-47, DD-55, DD-56, DD-64 ×2, DD-82, DD-103, DD-104`). DD-65's citation left as-is — it is the superseded historical snapshot and DD-109 is correctly excluded (it *is* the re-home). |
| D | `IB-102` source_dd `DD-35` → `DD-104` (re-pointed to the three-altitude architecture; "system-applicator" = the still-unbuilt whole-system application altitude). `IB-145` source_dd `DD-45` → `null` (kept Queued; reclassified as watched-library maintenance, matching IB-149/153 convention). |
| F | **Held** (not approved this gate) — `ib_items` reverse-link normalization/retirement remains a standing policy recommendation. |

Verification: post-edit re-run confirms all 9 Superseded DDs resolve via the canonical field with
no orphan terminus, and no bare "as-if-live" DD-49 reference remains outside DD-65's frozen snapshot.

---

*Phase 2 (knowledge-coverage + caching policy) is propose-only and begins now.*
