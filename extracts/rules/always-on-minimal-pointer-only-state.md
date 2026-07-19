---
title: "Always-On Entry File Stays Minimal, Volatile State Pointer-Only"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "always-on-context-minimalism-pointer-only-entry"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "structuring-agent-context.harvest-queue"
identification_report: "structuring-agent-context.harvest-queue.md::always-on-context-minimalism-pointer-only-entry::rule::always-on-minimal-pointer-only-state"
deployed: false
deployed_to: null
context:
  applies_to:
    - "any harness with a single guaranteed-loaded entry file injected into every agent request (a root instruction file, a system-prompt include, or a platform equivalent)"
    - "designers or auditors of an agentic system's always-on context surface"
    - "multi-session agent systems that track active state (current focus, current user, current task, current status) that could go stale if restated in more than one place"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — removing content from the entry file is a deletion with no migration cost; converting a restated fact into a pointer is a small, low-risk refactor"
  auditability: "high — every line of the always-on entry file can be checked against a canon-contents list (mission, load order, standing guards, pointers) and against whether it restates a fact that lives elsewhere; a routine review pass or audit tool can flag violations directly"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented in a single production agent system with a written entry-file spec ('wiring canon'). Not yet formally adopted elsewhere as an explicit, named audit criterion at time of extraction."
contract:
  preconditions: "A harness exists that guarantees loading exactly one instruction file (or a small fixed set) into every agent request — the 'always-on' entry point. The system tracks at least one piece of active or volatile state (current user, current focus, current status) that could otherwise be restated inline in that file."
  invariants: "The always-on entry file carries only the irreducible minimum: a mission/purpose statement, the load order for everything else, standing guards (side-effect boundaries, maintenance discipline), and pointers to skills or detail — never skill bodies, never restated facts. Any volatile state the entry file needs to reference (active user, current target, current status) is represented as a pointer to the surface that actually owns that state, never restated inline as a copied fact. Nothing is added to the entry file without passing the same minimality check as everything already in it."
  governance: "Owner: whoever authors or reviews the harness's always-on entry file. Every proposed addition is checked against the canon-contents list before merge — mission, load order, standing guards, and pointers are in; restated facts, skill bodies, and volatile detail are out. A periodic audit (or equivalent review gate) re-scans the file for accumulated restated facts, since the file drifts toward bloat one small, individually-reasonable addition at a time without an enforcement mechanism."
  recovery: "If a volatile fact is found restated inline in the entry file: extract it to its owning surface (a status file, a memory file, a tracked config) and replace the inline text with a pointer. If the entry file has grown past its irreducible minimum: run an audit pass, classify each line as canon-content or drift, and remove or relocate the drift. If a pointer in the entry file resolves to a missing or broken target: treat this as more serious than a stale inline copy would be, since a broken pointer fails silently — nothing in the entry file itself signals the problem — so pointer targets need their own existence check, not just a one-time link at authoring time."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "context-economy"
  - "pointer-discipline"
---

# Always-On Entry File Stays Minimal, Volatile State Pointer-Only

**Source:** [[always-on-context-minimalism-pointer-only-entry]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An always-on entry file — the one instruction surface a harness guarantees to inject into every agent request — is being authored, extended, or audited.

## Action

**Required:** Keep the file to its irreducible minimum: mission/purpose, load order for everything else, standing guards, and pointers to skills or detail surfaces. Represent any volatile or active state the file needs to reference (current user, current target, current status) as a pointer to its owning surface — never as a restated, inline fact.

**Forbidden:** Pasting skill bodies, restated user/session facts, or any detail that already lives on another surface into the always-on file. Adding "just one more paragraph" to the entry file without checking it against the same minimality standard applied to everything already there.

## Boundary

Enforced at two points: (1) entry-file authoring time, on every proposed addition; (2) periodic audit, re-scanning the whole file for content that accumulated as one-off, individually-reasonable additions but collectively constitutes drift.

## Enforcement

- **Mechanism:** Classify each line or proposed addition against the canon-contents list.
- **Check (deterministic-enough):** `content ∈ {mission, load_order, standing_guard, pointer}` → allowed. `content ∈ {restated_fact, skill_body, volatile_detail}` → violation.
- **Violation response:** Restated facts are extracted to their owning surface and replaced with a pointer; skill bodies are removed and replaced with a skill pointer; accumulated drift found at audit time is relocated or deleted, not left in place "since it's already there."

## Rationale

The always-on entry file is the most expensive real estate in an agentic system — its token cost is paid on every single request, whether or not the content is relevant to that request. Systems drift toward stuffing it with facts that then go stale and leak, because each individual addition looks harmless at the time it's made. Pairing a minimality rule ("always-on = minimal; everything else loads on demand") with a pointer-only rule for volatile state bounds both the recurring token cost and the staleness risk with the same mechanism: a fact lives in exactly one place, and the entry file only ever points to it. This makes the entry file the counterpart, at the harness-injection layer, of a general single-source-of-truth discipline.

## Failure Modes

- **Minimality regrows without enforcement.** The rule requires an active review gate or periodic audit — left unenforced, every incident or edge case tempts one more always-on paragraph, and the file regrows toward the bloat the rule exists to prevent.
- **Broken pointer is worse than a stale copy.** Pointer-only state assumes the pointed-to surface reliably resolves. A broken pointer fails silently — nothing in the entry file itself signals the problem — whereas a stale inline copy is at least visibly present (if wrong). Pointer targets need their own existence check.
- **Ambiguity in any accompanying wake-up/shortcut behavior undermines autonomy boundaries.** Where the entry file's minimalism is paired with a shortcut idiom that resolves a bare mention directly to a recorded next step, that shortcut needs an explicit "ambiguous → ask, don't guess" branch, or it silently becomes a way to bypass standing gates.

## Contract

### Preconditions
A harness exists that guarantees loading exactly one instruction file (or a small fixed set) into every agent request — the "always-on" entry point. The system tracks at least one piece of active or volatile state (current user, current focus, current status) that could otherwise be restated inline in that file.

### Invariants
The always-on entry file carries only the irreducible minimum: a mission/purpose statement, the load order for everything else, standing guards (side-effect boundaries, maintenance discipline), and pointers to skills or detail — never skill bodies, never restated facts. Any volatile state the entry file needs to reference (active user, current target, current status) is represented as a pointer to the surface that actually owns that state, never restated inline as a copied fact. Nothing is added to the entry file without passing the same minimality check as everything already in it.

### Governance
Owner: whoever authors or reviews the harness's always-on entry file. Every proposed addition is checked against the canon-contents list before merge — mission, load order, standing guards, and pointers are in; restated facts, skill bodies, and volatile detail are out. A periodic audit (or equivalent review gate) re-scans the file for accumulated restated facts, since the file drifts toward bloat one small, individually-reasonable addition at a time without an enforcement mechanism.

### Recovery
If a volatile fact is found restated inline in the entry file: extract it to its owning surface (a status file, a memory file, a tracked config) and replace the inline text with a pointer. If the entry file has grown past its irreducible minimum: run an audit pass, classify each line as canon-content or drift, and remove or relocate the drift. If a pointer in the entry file resolves to a missing or broken target: treat this as more serious than a stale inline copy would be, since a broken pointer fails silently — nothing in the entry file itself signals the problem — so pointer targets need their own existence check, not just a one-time link at authoring time.
