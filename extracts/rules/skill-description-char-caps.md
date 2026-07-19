---
title: "Skill-Description Character Caps — Soft 1,000 / Hard 1,536"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "skill-description-budget-context-overflow"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "structuring-agent-context.harvest-queue"
identification_report: "structuring-agent-context.harvest-queue.md::skill-description-budget-context-overflow::rule::skill-description-char-caps"
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill or command libraries whose descriptions are read into an always-on system-prompt listing on every turn"
    - "authoring or lint/audit tooling for agent-harness skill or command catalogs"
    - "harness configurations that truncate or drop catalog entries once a total description-character budget is exceeded"
  platform_coupling: "agnostic — the numeric caps (1,000 soft / 1,536 hard) are calibrated to one coding harness's default description-budget config and independently corroborated by a second, unrelated production skill library's own audit tooling; recalibrate the numbers for harnesses with a materially different budget default, but the two-tier discipline itself is portable"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — shortening a description is a text edit with no migration cost or rollback complexity"
  auditability: "high — description length is a mechanical character count, checkable at authoring time or via an automated audit; both known implementations already enforce it with tooling (a built-in diagnostic on one side, a whole-tree audit on the other)"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Independently corroborated by two production skill-library systems converging on the same numeric caps — a widely used coding harness's documented budget/truncation behavior, and a private enterprise skill library's whole-tree audit tooling. No direct MetaSystem adoption recorded at extraction time."
contract:
  preconditions: "A skill or command library exists whose descriptions are read into an always-on system-prompt listing on every turn, and the harness enforces (or can be given) a total character budget for that listing."
  invariants: "Every skill/command description, combined with any adjoining 'when to use' text, stays at or under 1,536 characters — the hard cap. Descriptions between 1,000 and 1,536 characters are flagged at Medium severity even though they remain under the hard cap, since the shared budget is finite and every long description crowds out others. New descriptions are authored to fit within 1,000 characters at creation time rather than trimmed reactively after tripping a cap."
  governance: "Owner: whoever authors or reviews skill/command descriptions, plus any lint/audit tooling that runs over the library. The two-tier check (soft 1,000 / hard 1,536) applies at description-authoring time and is re-checked by periodic library audits as descriptions are edited or added."
  recovery: "If a description exceeds 1,536 characters: treat as a High-severity finding and trim immediately — when trimming, prioritize keeping the primary trigger/use-case text early in the description and any collision-avoidance or hand-off clause intact, since harness truncation cuts the tail first. If a description is between 1,000 and 1,536 characters: treat as Medium — trim opportunistically at the next edit, not urgent. If a skill or command is suspected of silently under-triggering: check its description length against these caps before assuming the trigger wording itself is at fault."
tags:
  - "extracted-artifact"
  - "rule"
  - "skill-authoring"
  - "context-engineering"
  - "context-budget"
---

# Skill-Description Character Caps — Soft 1,000 / Hard 1,536

**Source:** [[skill-description-budget-context-overflow]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

Authoring or auditing a skill/command description (plus any adjoining "when to use" text) inside an agent harness that reads every catalog entry's description into an always-on listing, consumed on every turn regardless of whether the entry is used.

## Action

**Required:** Keep every description at or under 1,536 characters (the hard cap). Treat the 1,000–1,536 range as a soft-warn zone. Author new descriptions to fit within 1,000 characters at creation time, rather than writing long and trimming later.

**Forbidden:** Leaving a description above 1,536 characters once discovered — this is a High-severity finding, not a style nit, because harness truncation can silently strip exactly the keywords or hand-off clauses needed for correct routing. Relying on eyeballed length instead of a mechanical character count.

## Boundary

Enforced at two points: (1) skill/command authoring time, before the entry is committed to the catalog; (2) periodic library audits, which mechanically scan every entry's current length as the catalog grows and descriptions get edited.

## Enforcement

- **Mechanism:** Mechanical character count of `description + when_to_use` (or the harness's equivalent combined field).
- **Check (deterministic):**
  - `length <= 1000` → pass.
  - `1000 < length <= 1536` → Medium finding (soft cap).
  - `length > 1536` → High finding (hard cap; truncation risk).
- **Violation response:** High findings are trimmed immediately, tail-first content (trigger keywords, collision-avoidance clauses) preserved as the priority. Medium findings are trimmed at the next convenient edit.

## Rationale

The harness reads every catalog entry's description on every turn as part of deciding what to load — the description budget is a shared, finite resource, not a per-entry allowance. Past the budget, entries get truncated (least-recently-used first in one implementation) or dropped to name-only, and the truncation is graceful in the sense that it doesn't error, but it can silently strip the exact keywords a routing decision needed — so a skill appears to "undertrigger" for no visible reason, when the real cause is invisible character-budget pressure. Two independent production systems converge on the same 1,536-character ceiling from different angles (one as a documented harness truncation point, the other as a self-imposed audit-tooling hard cap), and both additionally flag descriptions well before that ceiling (around 1,000 characters) as already expensive — which is strong corroboration that the two-tier discipline, not just the single hard number, is the right shape for the rule. One of the two systems sharpens the failure mode further: descriptions there end with a peer-hand-off clause, and truncation cuts the tail — so collision protection is exactly what dies first, which is why that system treats the hard cap as High severity and requires new descriptions to fit the soft cap at creation time rather than after the fact.

## Failure Modes

- **Silent under-triggering from truncation.** A skill present in the listing but with its critical "use when X" phrase truncated will appear to undertrigger with no obvious diagnostic signal pointing at length.
- **Cascading description bankruptcy.** Adding one new skill can trigger truncation of older descriptions elsewhere in the same budget, silently degrading unrelated skills' triggering accuracy.
- **Reactive-only discipline.** Diagnosing overflow only after noticing degraded behavior (rather than checking length at authoring time or via a standing audit) means the cost is paid — sometimes for a while — before it's caught.

## Contract

### Preconditions
A skill or command library exists whose descriptions are read into an always-on system-prompt listing on every turn, and the harness enforces (or can be given) a total character budget for that listing.

### Invariants
Every skill/command description, combined with any adjoining "when to use" text, stays at or under 1,536 characters — the hard cap. Descriptions between 1,000 and 1,536 characters are flagged at Medium severity even though they remain under the hard cap, since the shared budget is finite and every long description crowds out others. New descriptions are authored to fit within 1,000 characters at creation time rather than trimmed reactively after tripping a cap.

### Governance
Owner: whoever authors or reviews skill/command descriptions, plus any lint/audit tooling that runs over the library. The two-tier check (soft 1,000 / hard 1,536) applies at description-authoring time and is re-checked by periodic library audits as descriptions are edited or added.

### Recovery
If a description exceeds 1,536 characters: treat as a High-severity finding and trim immediately — when trimming, prioritize keeping the primary trigger/use-case text early in the description and any collision-avoidance or hand-off clause intact, since harness truncation cuts the tail first. If a description is between 1,000 and 1,536 characters: treat as Medium — trim opportunistically at the next edit, not urgent. If a skill or command is suspected of silently under-triggering: check its description length against these caps before assuming the trigger wording itself is at fault.
