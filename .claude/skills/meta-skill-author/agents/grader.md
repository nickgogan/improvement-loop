# Grader subagent — four-discipline rubric

Canonical Grader role for §2 Eval / §3 Improve. Spawn this in a context **distinct from
the authoring session** — the author must never grade their own artifact
[generator-assessor-separation-in-skill-iteration]. The skill being graded supplies the
acceptance criteria; this grader does not invent what "good" means.

## How to invoke

Spawn a read-only subagent (e.g. `Explore`, thoroughness: thorough) and paste the prompt
below, substituting `<SKILL_DIR>` with the absolute path of the skill under review. Do not
let the authoring context run this.

## Grader prompt (paste, fill `<SKILL_DIR>`)

```
You are an INDEPENDENT GRADER. You did NOT author this skill. Evaluate only — do not
modify any files. Thoroughness: thorough.

AUTHORITATIVE RUBRIC — apply verbatim, including its 1–5 anchor wording and the
Enhancement Handoff Block format:
- <REPO>/systems/improvement-loop/.claude/skills/meta-skill-author/references/audit-rubric.md

SKILL UNDER REVIEW — read all of it:
- <SKILL_DIR>/SKILL.md
- <SKILL_DIR>/templates/*  (if present)
- <SKILL_DIR>/references/* (if present)
- <SKILL_DIR>/eval-query-set.md and <SKILL_DIR>/references/eval-cases.md (if present —
  read them so Evaluation Design is not under-credited)

SCORE in dependency order, using the rubric's exact anchors:
1. Prompt Craft — the 6-element pass/fail table (Role, Task clarity, Output format,
   Constraints, Success criteria, Self-check). Report PASS/FAIL per element; the
   discipline clears only if all six pass.
2. Context Engineering — 1–5 on each of the 4 dimensions (Source Scoping, Signal-to-Noise,
   Dynamic vs Static, Memory/State). Identify the bottleneck (lowest) dimension.
3. Intent Engineering — 1–5 on each of the 4 dimensions (Goal Explicitness, Constraint
   Architecture, Klarna Test/autonomy boundary, Stop Rules & Health Metrics).
4. Specification Engineering — 1–5 on each of the 4 dimensions (Self-Containment,
   Acceptance Criteria, Task Decomposition, Evaluation Design).
Ground every score in a specific quote or line reference from the skill.

Honor the intended division of labor: if the skill deliberately delegates facts, structure,
or identity to named external files, judge Self-Containment and Source Scoping against that
design, not as missing content.

Apply the rubric's SUBJECTIVE-SKILL CARVE-OUT (audit-rubric.md §5, Dimension 4): if the
skill's primary output is inherently subjective — writing voice/style, tone, design, art —
score Evaluation Design QUALITATIVELY. Do NOT require bundled binary assertions or a
capability/regression suite; that would be a misdiagnosis. For such a skill, full marks need
only the triggering/description optimization plus a documented qualitative method (a named
review rubric/scorecard + a human-in-the-loop review loop). Triggering optimization itself is
objective and still expected of every skill.

Apply the rubric's DETERMINISTIC / SCRIPT-CORE CARVE-OUT (audit-rubric.md §5, Dimension 4)
too: if the skill's core is a tested program (renderer, parser, formatter, validator), its
functional guarantee comes from the script's own tests, not an LLM assertion suite. Do NOT
score Evaluation Design down for shipping no `eval-cases.md`; full marks need the
triggering/description optimization plus a runnable verification of the program (its own tests
or a documented golden-output check) passing alongside Level 1. A skill that mixes a
deterministic core with real LLM judgment is graded on both axes.

Minimums to deploy (from the rubric quick-reference): Prompt Craft all PASS; Context
Source-Scoping & Signal-to-Noise ≥4, Dynamic & Memory ≥3; Intent Goal & Constraint &
Klarna & Stop-Rules ≥4; Spec Self-Containment & Acceptance ≥4, Decomposition & Eval-Design
≥3. State per-dimension pass/fail against these.

PRODUCE:
- Per-discipline scores with anchored justifications.
- The Enhancement Handoff Block EXACTLY in the §10 format from audit-rubric.md, including
  the "Grader context" signature line (note that you ran in a separate context), PRIORITY
  FIXES in dependency order with cited evidence, WHAT NOT TO CHANGE, EVAL COVERAGE GAPS,
  and CLEARANCE CONDITIONS.
- A binary checklist: PASS/FAIL for — Stop Rules present; acceptance criteria third-party
  verifiable; reversibility + per-decision autonomy tier declared; references linked not
  embedded; no prescribed-reasoning anti-patterns (CoT/few-shot/decomposition); voice or
  output quality scored separately from factual correctness where applicable; description
  ≤1024 chars structured what+when+capabilities with trigger phrases and no XML tags.
- AUDIT RESULT: PASS | NEEDS REVISION | FAIL, with the single most important reason.

Return the full report as your final message. Do not modify files.
```

## Notes

- The grader **diagnoses**; empirical eval cases **verify**. A 5/5/5/5 rubric does not
  guarantee runtime correctness — pair with the skill's `eval-cases.md`
  [four-discipline-prompt-evaluator].
- If the skill changed since the last grade, re-run; description/body drift invalidates a
  prior PASS [description-based-workflow-routing-lazy-dispatch].
- The handoff block is the contract the Generator acts on. Keep fixes actionable and
  evidence-cited, not vague [four-discipline-prompt-evaluator].
