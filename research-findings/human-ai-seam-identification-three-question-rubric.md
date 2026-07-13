---
name: "Human/AI Seam Identification via Three-Question Delegation Rubric"
summary: |-
  A procedure for locating the seam between what belongs to the human and what belongs
  to the AI in a candidate workflow, via three questions: (1) What are you avoiding?
  (procrastinated-but-important work is the high-leverage delegation target — the
  counter to the low-value "morning brief" default); (2) What would you hire for?
  (if you could onboard an intern with a playbook, you can onboard an agent); (3) What
  moves the North Star? The deeper value (Nick's ruled framing) is seam identification:
  problem-identification, standards, and direction stay human; playbook-executable
  parts go to the AI — "what can I do, or AI can do, or a combination of us" is the
  explicit partition question.
implementation_notes: |-
  Ruled framing from the wave-3 gate: extract as a Librarian advisory capability — the
  Librarian helps an operator see which parts of a potential workflow should belong to
  the human rather than the AI or the AI system — and as input to the Phase 4
  agent-vs-skill interview, not merely a workflow-selection checklist. Design: fold the
  three questions into the Librarian's design-mode intake and the Phase 4 interview
  script.
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (Librarian advisory)"
  - "General"
adopted_in: []
sources:
  - "what-workflow-should-you-get-your-ai-agent-to-do.md"
related_findings:
  - file: "five-persistent-human-skills-agent-era-framework.md"
    rel: "extends"
  - file: "tacit-knowledge-as-agent-delegation-barrier.md"
    rel: "same-problem"
  - file: "four-estimate-agent-routing-test.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "writing-agent-specifications.md"
---

# Human/AI Seam Identification via Three-Question Delegation Rubric

## What It Is

Vicky Zhao's rubric for choosing what to get an agent to do, taught to her cohort
students. Surface form: three selection questions —

1. **What are you avoiding?** Procrastinated-but-important work signals a complicated,
   energy-expensive first hurdle — exactly where an agent unlocking the start changes
   quality of life. Explicitly counters the default of automating nice-to-haves ("I
   never looked at that morning brief again").
2. **What would you hire for?** If you already know how the work goes well enough to
   onboard an intern/assistant with a playbook, that playbook onboards an agent.
3. **What moves the North Star?** Tie workflow selection to the goal already declared
   in CLAUDE.md, not to what's easy to spin up.

The deeper pattern — and the framing Nick ruled leads this finding — is **seam
identification**. The rubric's real output is a partition of a candidate workflow:
"what are some of the workflows that *I* can do, or *AI* can do, or a *combination of
us* can do." Problem identification, standards, and direction ("it's always you, the
person who's thinking, that is in the driver's seat") stay on the human side;
playbook-executable execution crosses to the AI. Working the rubric also forces the
operator to articulate where they're blocked and why — surfacing tacit structure that
then makes the agent spec specific ("everything... is being specific").

## Why It Matters

Most delegation guidance answers "what CAN the agent do"; this answers "which parts
SHOULD leave the human." That is precisely the advisory question the engine's Librarian
should be able to help an operator with when they bring a potential workflow: walk the
three questions, and return a seam map — human-owned parts, AI-owned parts, joint
parts — rather than a yes/no on automation. It also gives the Phase 4 agent-vs-skill
interview a ready-made intake: avoided work + hireable work + North-Star relevance is
a compact way to elicit which workflows deserve agents at all.

## Why People Are Using It

Instructional procedure from a creator teaching a cohort, grounded in her own
newsletter case (avoided work → high-friction human delegation failed → agent-assisted
setup was expensive but "improved my quality of life"). No quantified experiment —
one practitioner's procedure plus a taught cohort, hence Medium and not stronger.

## Potential Improvements

- Formalize the output as an explicit seam map artifact (human / AI / joint columns)
  rather than an implicit answer.
- Add a fourth check from the tacit-knowledge finding: can you actually write the
  playbook, or does the "hire for" answer overestimate your ability to articulate it?

## Potential Failure Modes

- **Avoidance ≠ delegable.** Some avoided work is avoided because it requires human
  judgment or authority (the very parts that must not cross the seam).
- **Rubric applied once, not re-applied.** Seams move as agent capability grows; a
  static partition goes stale.
- **North-Star question degenerates** into justifying whatever the operator already
  wanted to automate.
