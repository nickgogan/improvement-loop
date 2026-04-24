---
title: "Priority-Assignment Ownership Analysis — /promote-findings → /identify-artifacts → /reassess-priorities"
type: "research-report"
category: "structural-analysis"
target_system:
  - "improvement-loop"
created: "2026-04-24"
session: 64
author: "Codifier"
status: "awaiting-nick-gate"
---

# Priority-Assignment Ownership Analysis

## TL;DR

**Gap:** No skill owns initial priority assignment for raw findings. `/promote-findings` writes `priority: null` and defers to `/research-proposer` (**deprecated — DD-80**). `/identify-artifacts` reads priority as an input filter but does not write it. `/reassess-priorities` explicitly disclaims initial-assignment and points at `/identify-artifacts` — which does not actually do it.

**Surface symptom:** Session-58 findings landed at `priority: null`; session 62 worked around the gap by folding priority assignment into an identification-report addendum (flagged as "not durable").

**Proposed fix:** Amend `/identify-artifacts` to assign priority during classification (Option B below). Update `/promote-findings` to stop referencing the deprecated `/research-proposer`. No DD required — skill-contract amendments suffice; DD only if a structural rule surfaces that the amendment cannot encode.

**Gate:** Present to Nick. Do not apply skill edits until ruling.

---

## What Each Skill Says Today

### `/promote-findings` — intake from repo analyses

- **Writes `priority: null` at intake.** Skill file, Step 5 Write Findings, lines 184–185:
  > `priority`: Leave as `null`. The `/research-proposer` assigns priority.
- **Points at a deprecated skill.** `/research-proposer` is marked `DEPRECATED (DD-80) — Superseded by /identify-artifacts + /extract-artifacts. Do not invoke.`
- **Step 5b does *re-evaluation* flagging, not initial assignment.** Lines 188–199: on a *partial-match* update (evidence added to an existing finding), the skill flags a priority re-evaluation candidate if the finding now has 3+ independent-repo corroboration. Only applies to existing findings; does not assign priority to newly-promoted findings.

**Net:** `/promote-findings` explicitly disclaims initial priority-assignment responsibility by pointing it at a deprecated downstream skill.

### `/identify-artifacts` — classification into form

- **Reads priority as an input filter.** Step 0 (Determine Scope), lines 70–78:
  > Priority filter: `P1`, `P2`, or both — use Grep to search `systems/improvement-loop/research-findings/` for matching `priority:` values.
- **Arguments:** `P1 | P2 | P1 P2 | <finding-name> | --category <cat>`. No `null`/`unpriortized` mode. Findings with `priority: null` are invisible to P1/P2 filters unless explicitly named by filename.
- **Back-annotates `pipeline_status` but not `priority`.** Step 7 (Back-Annotate), lines 336–344:
  > Set `pipeline_status: "classified"` on every finding that was classified in this run. Leave `consumed_by: []` — this field is populated later by `/extract-artifacts` or `/synthesize-guide`.
  No mention of `priority`.

**Net:** `/identify-artifacts` treats priority strictly as an input. It does not assign priority, does not propose one, does not back-annotate one.

### `/reassess-priorities` — retroactive re-evaluation

- **Explicitly disclaims initial-assignment responsibility.** Lines 25–29:
  > Do NOT use this skill for:
  > - Initial priority assignment on new findings (that's `/identify-artifacts`)
  > - Classifying findings into forms (that's `/identify-artifacts`)
- **Points at `/identify-artifacts`.** Which, per above, does not actually do it.
- **Carries the full priority rubric.** Criteria 1–5 (evidence accumulation, strength upgrade, adoption signal, convergent implementation, related-findings cluster) are the best-developed priority rubric in the system. Threshold logic: 3+ independent sources → P2; 5+ with production evidence → P1.

**Net:** `/reassess-priorities` has the rubric but refuses to apply it at intake; it hands the rubric to a skill that doesn't use it.

---

## Where the Buck Gets Passed

```
/promote-findings ──(priority: null; see /research-proposer)──▶ DEPRECATED
                                                                    │
/reassess-priorities ──(initial assignment is /identify-artifacts's job)──▶ /identify-artifacts
                                                                              │
                                                                    ┌─────────┘
                                                                    ▼
                                                        /identify-artifacts:
                                                        reads priority, does not write it
                                                                    │
                                                                    ▼
                                                        ORPHANED — no owner
```

**Operational consequence:** Codifier improvises a workaround per session. Session 62 precedent: priority addendum appended to the identification report after classification. Explicitly flagged in session-62 SL as "not durable" and as an Owner-level governance gap.

---

## Candidate Owners

### Option A — `/promote-findings` assigns priority at intake

Assignment happens at the earliest point, closest to the source evidence (analysis doc, candidate description, repo adoption signals).

**For:**
- Single-pass: finding is written complete, no downstream null-priority state.
- Closest to source evidence.

**Against:**
- `/promote-findings` is a bridge-from-repo-analyses skill only. `/research-loop` is the other intake path (web sources, URLs, papers). Priority assignment at intake would need to be duplicated in `/research-loop` — or the problem just moves.
- Pre-classification priority ignores the form-rubric context. A finding's form (pattern vs rule vs agent) materially affects whether P1/P2/P3 fits — rules at P3 rarely make sense; patterns at P1 are rare.
- Expands `/promote-findings` scope beyond its current disposition (librarian — deduplication + schema compliance).

### Option B — `/identify-artifacts` writes priority at classification *(recommended)*

The classification pass already reads each finding's frontmatter, runs a rubric, and has a subagent drafting rationale per finding. Add priority assignment as a parallel output.

**For:**
- Single pass co-locates form and priority — both are rubric applications on the same evidence.
- The session-62 addendum workaround was already this pattern. Formalizing is the smallest delta from current practice.
- `/reassess-priorities` already names this skill as the initial-assignment owner — the contract is already pointing here; only the implementation is missing.
- Covers both intake paths (`/promote-findings` and `/research-loop`) because both feed findings into the KB where `/identify-artifacts` picks them up.

**Against:**
- `/identify-artifacts` currently uses priority as an **input filter**. Mode conflict must be resolved: if a finding enters with `priority: null`, the skill assigns it; if it enters with `P1`/`P2`, the skill uses it as filter. Achievable via argument semantics — e.g., `--assign-missing` or a dedicated `unassigned` scope.
- Skill scope expands from "form classification only" to "classification + priority." Justifiable — form and priority are both rubric-driven fit calls, not orthogonal concerns.

### Option C — New dedicated priority-assignment step

A `/assign-priority` skill or a formal Stage-1.5 step between `/promote-findings` and `/identify-artifacts`.

**For:**
- Clean separation of concerns. Each skill stays narrow.

**Against:**
- Adds a pipeline stage for what is fundamentally a one-pass rubric application.
- No evidence of independent priority-assignment work that would justify its own skill. Per standing feedback: "tolerate one-off patterns over adding mechanisms."
- Orchestration cost — another command to invoke, another human gate to honor.

### Option D — Status quo (flag per-session addendum as documented pattern)

Codifier continues to improvise; document it in `/identify-artifacts` as an optional "priority addendum when priority is null" sub-procedure.

**For:**
- Zero-delta. Known workaround.

**Against:**
- Flagged as not durable in session-62 SL.
- Non-Codifier callers of `/identify-artifacts` would still face the gap.

---

## Tradeoff Table

| Criterion | A: promote | B: identify | C: new step | D: status quo |
|---|---|---|---|---|
| Single-pass (no stage added) | ✓ | ✓ | ✗ | ✓ |
| Uses form-classification signal | ✗ (too early) | ✓ | depends | ✓ (inline) |
| Covers both intake paths | ✗ (repo only) | ✓ | ✓ | ✓ |
| Smallest contract change | Moderate | Small | Large (new skill) | Zero |
| Matches session-62 precedent | ✗ | ✓ | ✗ | ✓ (informal) |
| Rubric reuse (from `/reassess`) | ✓ | ✓ | ✓ | ✓ |
| Durable (not a per-session call) | ✓ | ✓ | ✓ | ✗ |

**Option B dominates on durability, scope fit, and contract delta.**

---

## Proposed Fix — Literal Edits (for Nick's Approval)

### Edit 1 — `/identify-artifacts` SKILL.md

**Add to Arguments table (after `--category`):**

```markdown
| `--assign-priority` | In addition to form classification, assign an initial priority to findings with `priority: null`. Uses the rubric embedded in /reassess-priorities (Criteria 1–5). Required when scope includes any unassigned finding. |
```

**Modify Step 0 (Determine Scope) to handle null-priority findings:**

```markdown
**Handling null-priority findings:**
- If any finding in scope has `priority: null`, either set `--assign-priority` or the skill will warn and skip.
- The priority filter (`P1` / `P2` / `P1 P2`) excludes null-priority findings by default — explicit `--assign-priority` opt-in is required to include them.
```

**Add Step 3.5 (after subagent classification, before Step 4 Write Report):**

```markdown
### Step 3.5: Priority Assignment (when --assign-priority is set)

For each finding in scope whose `priority` is `null`:

1. Apply the priority rubric from /reassess-priorities (Criteria 1–5, summarized below):
   - **P1 (Implement Now):** 5+ independent sources AND production evidence (documented usage at scale).
   - **P2 (Design Required):** 3+ independent sources; convergent implementation across unrelated orgs.
   - **P3 (Monitor):** 1–2 sources; single-author or single-org adoption; weak-to-medium evidence.
   - **Not Flagged:** weak-only evidence; theoretical; not yet actionable.
2. Record proposed priority alongside form classification in the identification report's Details block.
3. Priority is a PROPOSED value — Nick gates at report review. The skill writes the frontmatter `priority` field only on APPROVED findings at Step 7 back-annotation.

Independence rule: same author/org across multiple repos counts as one source. Count orgs, not documents.
```

**Modify Step 7 (Back-Annotate):**

```markdown
### Step 7: Back-Annotate Finding Files

After the identification report is written:

1. Set `pipeline_status: "classified"` on every classified finding.
2. If `--assign-priority` was set AND Nick approved priority proposals, set `priority` to the approved value.
3. Leave `consumed_by: []` — populated later by `/extract-artifacts` or `/synthesize-guide`.
```

**Add to Rules:**

```markdown
8. **Priority assignment (when enabled).** Under `--assign-priority`, the skill proposes priority using the /reassess-priorities rubric and writes it only on Nick-approved findings. Initial-priority ownership is this skill's responsibility; /reassess-priorities handles retroactive re-evaluation only.
```

### Edit 2 — `/promote-findings` SKILL.md

**Step 5 (Write Findings), lines 184–185, replace:**

```markdown
- `priority`: Leave as `null`. The `/research-proposer` assigns priority.
```

**With:**

```markdown
- `priority`: Leave as `null`. `/identify-artifacts --assign-priority` assigns priority at the classification step.
```

### Edit 3 — `/reassess-priorities` SKILL.md

**Lines 27–28 ("Do NOT use this skill for"), no edit required** — the existing text already correctly names `/identify-artifacts` as the initial-assignment owner. Once Edit 1 lands, the pointer resolves.

**Optional clarification (lines 32–40 "Cognitive Disposition") — add:**

```markdown
- **Initial vs retroactive is the boundary.** This skill does retroactive only. Initial priority assignment on new findings belongs to /identify-artifacts (with --assign-priority). A finding with `priority: null` is in-flight through classification, not this skill's scope.
```

---

## DD Question

**Does this need a DD?**

Arguments for: clarifies pipeline responsibility across three skills; fills a gap explicitly flagged in two session SLs; could be referenced in future skill additions.

Arguments against (my lean): skill-contract amendments already encode the rule. DDs reserved for architectural / constitutional decisions; this is operational pipeline mechanics. Per standing feedback — "tolerate one-off patterns over adding mechanisms" and "minimum viable abstraction" — amendments alone may suffice. If ambiguity recurs after amendments land, file a DD then.

**Recommendation: skill-contract edits only. No DD this pass.**

---

## Gate & Next Step

Nick, three calls to make:

1. **Option A / B / C / D?** My recommendation: Option B.
2. **Literal edits above — apply as drafted?** Or amend further?
3. **DD or no DD?** My recommendation: no DD this pass.

Once ruled, I will apply the approved edits and log the structural change in the session-64 SL.
