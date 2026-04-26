---
title: "Priority Reassessment Report — 2026-04-26 (spec-as-governance)"
type: "research-report"
category: "priority-reassessment"
created: "2026-04-26"
author: "improvement-loop"
findings_scanned: 1
candidates_flagged: 1
---

# Priority Reassessment Report — 2026-04-26 (spec-as-governance)

## Summary

- **Findings scanned:** 1 (targeted — `specification-as-governance-fourth-enforcement-philosophy`)
- **Reassessment candidates:** 1
- **Proposed priority bumps:** 1 (P2 → P1)
- **Proposed evidence upgrades:** 0 (frontmatter already at Medium; standalone change deferred to a separate evidence-strength pass — see "No Change" notes)
- **Proposed adoption status changes:** 0

**Scope rationale.** Targeted scan triggered by session 72 prioritization queue item 2 (handoff: re-evaluate Candidate 2 at 4th–5th independent-repo surfacing per session-62 §Decision 1). Full-KB scan deferred to next periodic `/reassess-priorities` cycle.

**Skill-contract deviation.** Per the canonical procedure, this skill scans the full KB and produces an N-candidate report. This run is a single-candidate targeted check at handoff direction. Same Criterion-1 + Criterion-2 logic applied; report shape preserved.

---

## Candidates

### Specification-as-Governance — Fourth Enforcement Philosophy

- **Current priority:** P2 (Design Required)
- **Proposed priority:** **P1 (Implement Now)**
- **Criteria triggered:** Criterion 1 (Evidence Accumulation — 5+ independent sources with production evidence)
- **Evidence summary:** 3 prior independent sources at session 62 (LangGraph, n8n, Superpowers) → at minimum 5 total now after net-new evidence: **MemPalace** (RFC 002 with code-level `declared_transformations` conformance machinery; pytest mixin enforcement) and **Amazon Kira** (major production rebuild after Dec 2025 outage; "turns prompts into requirements, tasks, and task lists before code generation begins"). Two further independent surfacings (OpenSpec/YC framework; Roman's spec-as-source-of-truth) are evidence-aligned but framework- or single-practitioner-shaped rather than full-repo enforcement; counted only at the conservative tier.
- **Rationale:** Trigger condition from session-62 §Decision 1 ("revisit at 4th–5th independent-repo surfacing per skill rubric") has fired. The MemPalace evidence is qualitatively the strongest new corroboration — formal spec (`spec_version: 1.0` as loadable-compatibility boundary), reserved transformation vocabulary in §1.4, typed `ClassVar[frozenset[str]]` declaration in §2.1, two conformance tests in §7.2 / §7.3, named failure mode (`TransformationViolationError`), and retroactive contract-audit of existing miner code. This is the same enforcement *shape* as LangGraph's `libs/checkpoint-conformance/` but extends the pattern to a richer transformation vocabulary and applies it to data-handling promises rather than interface contracts. Amazon Kira is the first major production deployment evidence in the cluster (Dec 2025 outage → rebuild around the principle), satisfying the skill rubric's "5+ independent sources **with production evidence** → propose P1" threshold.

#### Independence Audit (counting orgs/authors per Rule 2)

| # | Source | Org / author | Independent? | Class |
|---|--------|--------------|--------------|-------|
| 1 | LangGraph (`libs/checkpoint-conformance/`) | LangChain AI | ✓ | Repo (enforcement code) |
| 2 | n8n (`.claude/specs/`, spec-driven dev skill) | n8n-io | ✓ | Repo (skill) |
| 3 | Superpowers (`superpowers-plugin-spec-driven-sub-agent-orchestra`) | Superpowers / Jeremy Howard-adjacent | ✓ | Repo (plugin) |
| 4 | **MemPalace (RFC 002, declared_transformations)** | MemPalace project | ✓ | Repo (enforcement code + formal spec) — NEW |
| 5 | **Amazon Kira (post-outage rebuild, prompts→requirements→tasks)** | Amazon | ✓ | Production deployment — NEW |
| 6 | OpenSpec (YCombinator, spec deltas) | YC-backed | ✓ (conservative-tier) | Framework / tooling category — NEW, weaker form |
| 7 | spec-as-source-of-truth (Roman's claude -p agent) | Roman (independent practitioner) | ✓ (conservative-tier) | Single-practitioner pattern — NEW, weaker form |

**Conservative reading:** 3 prior + 2 strong new (MemPalace, Kira) = **5 independent sources**, with **production evidence at #5**. Skill Criterion 1 P1 threshold met cleanly.

**Generous reading:** 3 prior + 4 new = 7. Pattern has reached cross-ecosystem convergence (LangChain ⨯ n8n ⨯ Superpowers ⨯ MemPalace ⨯ Amazon ⨯ YC ⨯ independent practitioners).

#### Why session 62 held at P2 and why that hold no longer governs

Session 62 §Decision 1: skill rubric required 5+ for P1; only 3 sources visible. The hold was a conservatism-rule deference, with explicit re-evaluation gate at 4th–5th repo surfacing. Net-new evidence since 2026-04-24 (`declared-transformations-contract-conformance.md` dated 2026-04-23 but processed post-session-62; 2026-04-20 update to `spec-as-source-of-truth-for-agent-construction.md` adding the Kira production-rebuild citation) clears the gate.

#### Downstream implications for Nick to consider

- The finding is `pipeline_status: raw` and `consumed_by: []`. P1 promotion would not auto-propagate downstream — `/identify-artifacts` still owes a classification pass before `/extract-artifacts` could draft anything. The promotion just elevates it into the P1 Implement-Now queue for Codifier.
- `applicability: ["General"]` — the pattern affects MetaSystem governance directly (DD-30 / DD-82 write-boundary contracts are exactly the social-contract class the pattern converts to tested properties). A P1 promotion would surface implementable scope (e.g., conformance tests at Researcher/Codifier/Owner write boundaries).
- `sources: []` is empty in frontmatter despite the body citing `[[langgraph-analysis]]` and `[[n8n-analysis]]`. This is a separate frontmatter-vs-body drift to flag for Researcher cleanup (`/linkage-repair` scope), not blocking on the priority decision.

---

## No Change (Confirmed Held)

- **Evidence-strength upgrade** from "Medium (practitioner-documented)" to "Strong (production-tested)" is *defensible* on the new Amazon-Kira citation but is held this run for two reasons: (a) the Kira evidence is one citation in a related finding's update note rather than a primary source dossier; (b) per skill Rule 5, evidence_strength changes are a separate pass from priority changes. Surfaced for next `/reassess-priorities` full-pass.
- **Adoption status** stays "Not Yet Started" — MetaSystem has not yet adopted any variant of the pattern.
- **`sources: []` frontmatter gap** — out of scope for `/reassess-priorities` (skill modifies frontmatter only for priority/evidence/adoption). Refer to `/linkage-repair` or Researcher cleanup.

---

## Proposed Edit (gated on Nick approval)

**File:** `systems/improvement-loop/research-findings/specification-as-governance-fourth-enforcement-philosophy.md`

**Frontmatter change:**

```diff
- priority: P2
+ priority: P1
- last_updated: '2026-04-19'
+ last_updated: '2026-04-26'
```

No body content changes. No `evidence_strength` or `adoption_status` changes in this run.

---

## Status Field Contract

- `PENDING` — current state, awaiting Nick's gate
- `APPROVED` — Codifier applies the proposed Edit
- `REJECTED` — finding stays at P2; document reason for the audit trail
- `MODIFIED` — Nick proposes a different priority; Codifier honors Nick's value
