---
title: "Skill Self-Improvement Lessons Log Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "self-improving-skill-lessons-log"
extraction_date: "2026-05-25"
last_change_session: 146
last_change_report: "2026-07-13-source-drift"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "skill files that are invoked repeatedly and may accumulate operational failure modes over time"
    - "any agent skill where post-execution self-evaluation is appropriate"
    - "skill ecosystems where a dedicated improvement process — agent-driven or human-driven — maintains a per-skill learning journal grounded in with/without baseline comparisons"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "low — lessons accumulate in the skill file or its companion journal; removing lessons requires manual pruning but no migration cost"
  auditability: "high when the lessons record is co-located with the skill (in-file table or companion journal file) and dated; low when lessons are only in conversation history"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Two independent implementations observed: OB1's Panning for Gold skill (v2.0.0, in-skill lessons table, 6 documented lessons from 13+ production sessions) and AI LABS' learning loop (companion learning.md journal written by a dedicated skill-improver agent, entries grounded in with/without baseline comparisons). No local adoption yet."
contract:
  preconditions: "The skill is already written and has been invoked at least once. A self-improvement phase can be appended to the skill's execution sequence, or a dedicated improvement process can maintain a companion journal. The skill file (or its companion journal) is writable by the agent."
  invariants: "Each skill has exactly one canonical lessons record — either a table appended to the skill file or a single companion journal file co-located with the skill; never both, never scattered. Each lesson includes a date, a plain-English description of what happened, and the rule change (or baseline result) it produced. Lessons are recorded after the skill's primary output is delivered, never interleaved with it. Lessons are added only when a genuine failure mode, correction, inefficiency, or measured baseline delta is observed — not every invocation."
  governance: "Owner: the agent or human who owns the skill file. When a dedicated improver agent writes the journal, the skill owner still gates rule changes applied back to the skill's process steps. Lessons that generalize across multiple skills (e.g., compaction-induced data loss) should be promoted to shared guidance rather than remaining skill-local. Periodic pruning is the skill owner's responsibility when the lessons record exceeds ~10 entries."
  recovery: "If a lesson introduces an error in the skill's process steps → revert the change and re-add the lesson as a note only (not a rule change). If the lessons record grows unwieldy → prune entries older than 6 months that have been superseded by later lessons. If a previously-learned lesson is violated in a new invocation → add a new entry; do not modify the original. If the in-skill table and a companion journal both exist → consolidate into one canonical record before adding further lessons."
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
| `{{LOG_LOCATION}}` | Where lessons live: `in-skill` (table appended to the skill file) or `companion-journal` (a `learning.md`-style file co-located with the skill) |
| `{{SELF_IMPROVEMENT_TRIGGER}}` | What conditions trigger the self-improvement phase (e.g., "after every invocation", "when the user corrects the output", "when token usage exceeds 10k", "each round of a driven improvement loop") |
| `{{EVALUATION_CRITERIA}}` | The 2-4 questions the skill (or improver agent) asks after execution (see defaults below) |

---

## Body

**Variant A — in-skill lessons log.** Add the following two sections to the end of any skill file:

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

**Variant B — companion learning journal.** Create a `learning.md` file co-located with the skill (e.g., `skills/{{SKILL_NAME}}/learning.md`) — an improvement journal that documents everything learned about the skill in a structured format:

```markdown
# {{SKILL_NAME}} — Learning Journal

## Round {{R}} — {{DATE}}

**What was tried:** <the change or usage under evaluation>
**Result with the skill:** <observed outcome>
**Result without the skill (baseline):** <observed outcome, when a with/without comparison was run>
**Lesson:** <plain-English takeaway>
**Rule change applied:** <the concrete skill edit, or "none — note only">
```

In Variant B the journal is typically written by a dedicated skill-improver process (an improvement-loop agent), not by the skill self-modifying after ordinary use, and entries are grounded in with/without baseline comparisons rather than in-session observations.

---

## Usage

1. Choose `{{LOG_LOCATION}}`. Default to Variant A (in-skill) when the skill improves opportunistically during ordinary use; choose Variant B (companion journal) when a dedicated improvement loop drives rounds of refinement or when baseline with/without comparisons are available.
2. For Variant A: read the full skill file, add `Phase {{N}} — Self-Improvement` as the last phase in the skill's execution sequence, and append the Lessons Log table immediately after it.
3. Customize `{{SELF_IMPROVEMENT_TRIGGER}}` — default is "after every invocation," but for expensive skills, "when the user corrects the output" reduces overhead; in a driven improvement loop, the trigger is each loop round.
4. Customize `{{EVALUATION_CRITERIA}}` — the four defaults apply broadly; add skill-specific criteria (e.g., for a transcript extraction skill: "Were all speaker labels correct after consolidation?").
5. On first invocation after the extension, run the self-improvement phase (or first journal round) even if nothing went wrong — establish the habit and confirm the evaluation criteria are the right ones.
6. Keep exactly one canonical lessons record per skill — do not run both variants in parallel.

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
| **In-skill appended log (Variant A)** | The skill improves opportunistically during ordinary use; zero extra files; lessons live where the process steps live |
| **Companion learning journal (Variant B)** | A dedicated improvement loop drives refinement rounds; journal entries record what was tried and the result both with and without the skill; keeps the skill file lean |
| **Self-modifying vs. improver-written** | Variant A is written by the skill itself post-invocation; Variant B is written by a dedicated skill-improver agent in a driven loop — choose based on who owns the improvement cadence |
| **Lightweight (trigger = user correction only)** | For simple, fast skills where per-invocation evaluation adds more overhead than value |
| **Rich (add session number + token count columns)** | For skills where token efficiency is a key concern; the added columns enable trend analysis |
| **Baseline-grounded entries** | When with/without A-B comparisons are feasible — lessons cite a measured delta rather than an in-session observation |
| **Cross-skill promotion** | When the same lesson appears in 3+ skill logs — promote to shared guidance rather than repeating in each skill |
| **Version-pinned lessons** | When the skill has multiple versions — add a "skill version" column so lessons can be scoped to the version where they apply |

---

## Contract

### Preconditions
The skill is already written and has been invoked at least once. A self-improvement phase can be appended to the skill's execution sequence, or a dedicated improvement process can maintain a companion journal. The skill file (or its companion journal) is writable by the agent.

### Invariants
Each skill has exactly one canonical lessons record — either a table appended to the skill file or a single companion journal file co-located with the skill; never both, never scattered. Each lesson includes a date, a plain-English description of what happened, and the rule change (or baseline result) it produced. Lessons are recorded after the skill's primary output is delivered, never interleaved with it. Lessons are added only when a genuine failure mode, correction, inefficiency, or measured baseline delta is observed — not every invocation.

### Governance
Owner: the agent or human who owns the skill file. When a dedicated improver agent writes the journal, the skill owner still gates rule changes applied back to the skill's process steps. Lessons that generalize across multiple skills (e.g., compaction-induced data loss) should be promoted to shared guidance rather than remaining skill-local. Periodic pruning is the skill owner's responsibility when the lessons record exceeds ~10 entries.

### Recovery
If a lesson introduces an error in the skill's process steps → revert the change and re-add the lesson as a note only (not a rule change). If the lessons record grows unwieldy → prune entries older than 6 months that have been superseded by later lessons. If a previously-learned lesson is violated in a new invocation → add a new entry; do not modify the original. If the in-skill table and a companion journal both exist → consolidate into one canonical record before adding further lessons.
