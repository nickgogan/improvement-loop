# Worked Example — Design Mode

> End-to-end demonstration of §1 Design Mode: one challenging task →
> tacit-knowledge elicitation → spec gate → SKILL.md draft → capability eval → ship.
> Read `references/decision-sequence.md` alongside this file.

This walkthrough is **illustrative**, not authoritative. The rules it demonstrates
are in `SKILL.md` and the `references/`; if this example ever conflicts with those,
the rules win.

---

## The task

A user wants a skill that turns a messy on-call incident channel into a
structured post-incident review (PIR) draft. We follow Design Mode rather than
writing the spec up front, because authors systematically guess wrong about what
context a model needs `[iterate-on-single-task-then-extract-skill]`.

---

## Step 1 — Iterate on ONE task first (required)

We do **not** start by writing `SKILL.md`. We run one real incident transcript
through the model by hand and observe what bridged the gap between a generic
summary and a usable PIR. The winning approach that emerged:

- The model needed the *timeline* extracted before the *root cause* — when asked
  for root cause first, it anchored on the loudest message, not the earliest signal.
- It needed an explicit instruction that "contributing factors" ≠ "root cause."
- It needed the output sectioned so a human reviewer could veto each claim.

Only after this single task succeeded did we distill the skill. This defeats
premature optimization — writing eval matrices for a skill that does not yet work
on any task `[iterate-on-single-task-then-extract-skill]`.

---

## Step 2 — Elicit tacit knowledge (5 layers, ~45 min)

Senior incident reviewers carry judgment they cannot articulate without prompting
`[tacit-knowledge-as-agent-delegation-barrier]`. The five-layer pass surfaced:

| Layer | What we surfaced |
|-------|------------------|
| 1. Operating rhythms | PIRs are drafted within 48h; the channel is the source of truth |
| 2. Recurring decisions | "Is this a root cause or a contributing factor?" — the hardest recurring call |
| 3. Required inputs | Channel transcript + deploy log + alert timestamps |
| 4. Friction points | Reviewers conflate the first symptom with the first cause |
| 5. Success criteria | Every timeline entry has a timestamp; every claim is human-vetoable |

We used a YAML template with embedded per-section elicitation prompts so the
reviewer produced the knowledge section-by-section instead of one dump
`[yaml-templates-with-embedded-elicitation-instructions]`. See
`templates/skill-md-skeleton.md` for the embedded-elicitation pattern.

---

## Step 3 — Spec-first gate (human approves before any SKILL.md is generated)

We lock the spec before writing the body, because implicit training-data
assumptions cause most cascading failures in long agentic runs
`[spec-first-agent-briefs-prompt-craft-context-inten]`. The eight spec primitives:

- **Objective + why:** Draft a PIR from an incident channel so the human reviewer
  edits rather than authors from scratch.
- **Success metrics:** Reviewer accepts ≥80% of timeline entries unedited.
- **Authoritative inputs:** Channel transcript, deploy log, alert timestamps. Nothing else.
- **Deliverables + format:** Markdown PIR with Timeline / Root Cause / Contributing
  Factors / Action Items sections.
- **Acceptance criteria (verifiable):** Every timeline entry carries a timestamp;
  root cause and contributing factors are in separate sections.
- **Constraints:** MUST NOT invent timestamps; MUST NOT merge root cause with
  contributing factors; escalate if the transcript has no deploy reference.
- **Workflow + checkpoints:** Extract timeline → derive root cause → draft action
  items → present for human veto.
- **Escalation triggers:** Ambiguous root cause → present 2 candidates, do not pick.

We also confirm the seven-part intent structure, paying special attention to
**Stop Rules**, the most commonly omitted component
`[intent-engineering-framework-seven-part-agent-inten]`: *stop and ask if the
transcript lacks timestamps; never fabricate a timeline.*

Execution mode is declared **interactive** (outcome-based), not scheduled
`[hands-off-routine-prompt-precision-pattern]`.

**The human approved this spec.** Only now do we generate `SKILL.md`.

---

## Step 4 — Draft the SKILL.md body

Frontmatter (open-standard fields only — this skill is portable):

```yaml
---
name: incident-pir-drafter
description: >
  Drafts a structured post-incident review (PIR) from an on-call incident
  channel transcript. Use when turning a messy incident thread, Slack channel,
  or alert log into a reviewable PIR with a timestamped timeline, separated root
  cause and contributing factors, and human-vetoable action items. Trigger
  phrases: "draft a PIR", "write up this incident", "post-incident review from
  this channel", "turn this incident thread into a report".
license: MIT
---
```

Body follows the five-layer completeness check
`[five-layer-agent-prompt-architecture]` and is **outcome-based** — we state the
goal and constraints and let the model reason, because prescribed reasoning steps
degrade frontier reasoning models `[reasoning-model-anti-pattern-prescribed-reasoning]`.
No chain-of-thought scaffolding, no few-shot examples in the body. We explain the
WHY behind each constraint rather than stacking ALL-CAPS MUSTs
`[skill-authoring-explain-the-why-not-musts]`, and express behavioral rules as
negative constraints `[negative-constraints-as-probabilistic-output-collapse]`:
*"Do not present a root cause as certain when the transcript supports two readings."*

We mark the human-veto step as a **Proposal-first** HITL tier — the draft is
presented, the human approves before it is treated as final
`[autonomy-gradient-not-binary-delegation]`.

---

## Step 5 — Capability eval (not regression yet)

A brand-new skill starts on a **capability** eval suite with deliberately low
starting pass rates; it only graduates to the regression suite as it approaches
100% `[capability-vs-regression-eval-lifecycle]`. We built 20 description-eval
queries (see `templates/eval-query-set.md`), split 60/40, ran each train query
3 times, and iterated the description ≤5 times, selecting by **TEST** score to
avoid overfitting `[skill-description-optimization-loop-held-out-test]`.

A separate Grader context — never the author's context — scored the drafts
against the acceptance criteria `[generator-assessor-separation-in-skill-iteration]`.

---

## Step 6 — Validate and ship

Run Level 1 deterministic validation first `[bmad-deterministic-skill-validator]`:

```bash
bash scripts/validate.sh ./incident-pir-drafter
```

Only after Level 1 passes does Level 2 (four-discipline rubric, by a separate
Grader) become meaningful. The skill ships once it clears both.

---

## What this example demonstrates

- Single-task-first beats spec-first authoring `[iterate-on-single-task-then-extract-skill]`.
- The spec gate is a real human checkpoint, not a formality.
- Stop Rules and reversibility classification are non-optional.
- The author never grades their own draft `[generator-assessor-separation-in-skill-iteration]`.
