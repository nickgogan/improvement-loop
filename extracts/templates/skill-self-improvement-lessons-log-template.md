---
title: "Skill Self-Improvement Lessons Log Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "self-improving-skill-lessons-log"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill files that are invoked repeatedly and may accumulate operational failure modes over time"
    - "any agent skill where post-execution self-evaluation is appropriate"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — lessons accumulate in the skill file; removing lessons requires manual pruning but no migration cost"
  auditability: "high when lessons table is in the skill file itself and dated; low when lessons are only in conversation history"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern observed in OB1's Panning for Gold skill (v2.0.0) — 6 documented lessons from 13+ production sessions. MetaSystem skills do not currently include self-improvement phases or lessons logs."
contract:
  preconditions: "The skill is already written and has been invoked at least once. A self-improvement phase can be appended to the skill's execution sequence. The skill file is writable by the agent."
  invariants: "The lessons log table is appended to the skill file (not a separate file). Each lesson includes a date, a plain-English description of what happened, and the rule change it produced. The self-improvement phase runs after the skill's primary output is delivered. Lessons are added only when a genuine failure mode, correction, or inefficiency is observed — not every invocation."
  governance: "Owner: The agent or human who owns the skill file. Lessons that generalize across multiple skills (e.g., compaction-induced data loss) should be promoted to shared guidance rather than remaining skill-local. Periodic pruning is the skill owner's responsibility when the lessons table exceeds ~10 entries."
  recovery: "If a lesson introduces an error in the skill's process steps → revert the change and re-add the lesson as a note only (not a rule change). If the lessons table grows unwieldy → prune entries older than 6 months that have been superseded by later lessons. If a previously-learned lesson is violated in a new invocation → add a new entry; do not modify the original."
tags:
  - "extracted-artifact"
  - "template"
  - "skill-design"
  - "self-improvement"
  - "lessons-log"
---

# Skill Self-Improvement Lessons Log Template

**Source:** [[self-improving-skill-lessons-log]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description |
|----------|-------------|
| `{{SKILL_NAME}}` | Name of the skill being extended |
| `{{SELF_IMPROVEMENT_TRIGGER}}` | What conditions trigger the self-improvement phase (e.g., "after every invocation", "when the user corrects the output", "when token usage exceeds 10k") |
| `{{EVALUATION_CRITERIA}}` | The 2-4 questions the skill asks itself after execution (see defaults below) |

---

## Body

Add the following two sections to the end of any skill file:

```markdown
---

## Phase {{N}} — Self-Improvement

**Trigger:** {{SELF_IMPROVEMENT_TRIGGER}}

**Evaluation criteria:**
{{EVALUATION_CRITERIA}}

Default evaluation criteria (customize per skill):
1. Did any work get lost (to compaction, truncation, or missing writes)?
2. Was token usage reasonable, or were there avoidable re-reads or redundant steps?
3. Did the user correct the output? If so, what triggered the correction?
4. Did any step produce output that was immediately discarded or redone?

**Process:**
1. Run through each evaluation criterion.
2. If a lesson is identified, add one row to the Lessons Log below.
3. If the lesson implies a change to a process step, update that step in the skill file.
4. Do not add a row if no lesson was identified — the log is for genuine improvements only.

---

## Lessons Log

| Date | Session | What happened | Rule change |
|------|---------|---------------|-------------|
| _(first lesson will appear here)_ | | | |
```

---

## Usage

1. Identify the skill to extend. Read the full skill file before editing.
2. Add `Phase {{N}} — Self-Improvement` as the last phase in the skill's execution sequence. Set N to the next phase number.
3. Customize `{{SELF_IMPROVEMENT_TRIGGER}}` — default is "after every invocation," but for expensive skills, "when the user corrects the output" reduces overhead.
4. Customize `{{EVALUATION_CRITERIA}}` — the four defaults apply broadly; add skill-specific criteria (e.g., for a transcript extraction skill: "Were all speaker labels correct after consolidation?").
5. Append the Lessons Log table immediately after the self-improvement phase.
6. On first invocation after the extension, run the self-improvement phase even if nothing went wrong — establish the habit and confirm the evaluation criteria are the right ones.

### Example Lessons Log (from OB1's Panning for Gold skill)

| Date | Session | What happened | Rule change |
|------|---------|---------------|-------------|
| 2026-03-01 | 3 | Background evaluator agents lost to compaction — no output written | Evaluators must write to permanent files before ending |
| 2026-03-15 | 7 | 10 speaker labels generated for 2-person conversation | Added Phase 0.5: Speaker Consolidation — clean speaker data before extraction |
| 2026-04-02 | 11 | Re-read the same source file 3 times due to missing deduplication | Added file-read deduplication check at start of Phase 1 |

---

## Variation Axis

| Variation | When to use |
|-----------|-------------|
| **Lightweight (trigger = user correction only)** | For simple, fast skills where per-invocation evaluation adds more overhead than value |
| **Rich (add session number + token count columns)** | For skills where token efficiency is a key concern; the added columns enable trend analysis |
| **Cross-skill promotion** | When the same lesson appears in 3+ skill logs — promote to shared guidance rather than repeating in each skill |
| **Version-pinned lessons** | When the skill has multiple versions — add a "skill version" column so lessons can be scoped to the version where they apply |

---

## Contract

### Preconditions
The skill is already written and has been invoked at least once. A self-improvement phase can be appended to the skill's execution sequence. The skill file is writable by the agent.

### Invariants
The lessons log table is appended to the skill file (not a separate file). Each lesson includes a date, a plain-English description of what happened, and the rule change it produced. The self-improvement phase runs after the skill's primary output is delivered. Lessons are added only when a genuine failure mode, correction, or inefficiency is observed — not every invocation.

### Governance
Owner: The agent or human who owns the skill file. Lessons that generalize across multiple skills (e.g., compaction-induced data loss) should be promoted to shared guidance rather than remaining skill-local. Periodic pruning is the skill owner's responsibility when the lessons table exceeds ~10 entries.

### Recovery
If a lesson introduces an error in the skill's process steps → revert the change and re-add the lesson as a note only (not a rule change). If the lessons table grows unwieldy → prune entries older than 6 months that have been superseded by later lessons. If a previously-learned lesson is violated in a new invocation → add a new entry; do not modify the original.
