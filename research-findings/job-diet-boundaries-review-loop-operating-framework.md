---
name: "Job–Diet–Boundaries–Review-Loop Agent Operating Framework"
summary: |-
  A four-part care-and-feeding framework for any deployed agent: a job (statable in one
  sentence, or the agent is too vague), a diet (what it reads — stale/bloated/messy
  context makes a stale/bloated/messy agent), boundaries (read/draft/write/send are
  different risk classes; start read-only or draft-only and let the agent earn more
  permission), and a review loop (run → human review → update instructions/sources/
  permissions → run again). Comes with an ownership decision rule: if a system reads
  important context, produces work people act on, or touches a workflow others depend
  on, it needs a named owner now — and a decommission clause: if nobody is willing to
  own it, it shouldn't be doing important work. The 2026 move: from prompts to jobs.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "you-cant-run-ai-agents-without-this.md"
related_findings:
  - file: "agent-owner-card-human-facing-registry.md"
    rel: "extended-by"
  - file: "trust-calibration-progressive-autonomy-ramp.md"
    rel: "same-problem"
  - file: "human-on-the-loop-hotl-autonomy-tiering-framework.md"
    rel: "same-problem"
  - file: "iterative-refinement-loop-with-quality-gate.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A deliberately minimal operating framework for any agent past the build demo — four
things to give it:

1. **A job.** A real, one-sentence-statable job ("prepare first-pass backlog items for
   refinement", "inspect a pull request for risky changes") — not "help with product" or
   "make me more productive." If the job can't be said in a sentence, the agent is too
   vague.
2. **A diet.** What the agent reads — docs, tickets, transcripts, repo instructions,
   examples. The propagation rule: stale diet → stale agent; bloated diet → bloated
   agent; incorrect examples → learned bad habits. Fixing an agent usually means fixing
   its inputs: remove the stale PRD, add a better example, change what it may read.
3. **Boundaries.** Read files / draft / write to a system of record / send or delete are
   escalating risk classes, and the owner's stake should escalate with them. The
   permission-earning ladder: start read-only (draft-only if unsure) and let the agent
   earn more permission over time.
4. **A review loop.** Demystified: the agent runs, a human (occasionally another agent)
   reviews, you note what was good and bad, you update instructions/sources/permissions,
   it runs again. Run, review, improve, run again — not a giant governance process.

Attached decision rule: if a system can read important context, produce work you or your
team act on, or touch a workflow other people depend on, it needs an owner *now* — one
named person, even for team agents. Decommission clause: if nobody is willing to own it,
it probably shouldn't be doing important work, and decommissioning is the correct move.

The framing shift underneath: **prompting is asking; agent work is delegating a job.**
"Write acceptance criteria for this feature" is a prompt. "Read the PRD, the last 20
support tickets, the design brief, and our three best examples; draft the stories;
attach evidence; mark assumptions; don't create Jira tickets; put everything into
review" is a job — sources, boundaries, output shape, and review loop included.

## Why It Matters

The KB's governance findings on this problem are mostly enforcement-grade (HOTL tiers,
identity governance, autonomy matrices). This is the vocabulary-level version a
non-engineer owner can actually run — four words, one decision rule, one decommission
clause — and it packages several engine-adopted practices (context specs as diet,
DD-30-style write boundaries, DD-29 human-gate review loops) into a portable checklist.
Its main engine value is as consumer-facing substrate: when the engine advises others'
agent setups, this is the right altitude for a first ownership conversation. The
decommission clause is the genuinely novel bit — the KB had no explicit
"unowned means turn it off" rule.

## Why People Are Using It

Positioned against the build-obsessed 2026 default ("if every ambitious person creates
three agents, you don't have more productivity unless ownership scales with them"). The
worked example — a PM's story-prep agent whose weekly refinement package quietly becomes
team infrastructure — is the recognizable path by which personal agents become unowned
team dependencies.

## Potential Alternatives

- **HOTL autonomy tiering / autonomy matrix** (existing KB finding): heavier,
  enforcement-oriented; right when compliance demands demonstrable oversight.
- **Progressive autonomy ramp** (existing KB finding): the same earn-permission idea
  formalized per task type with demonstrated-reliability criteria.
- **Owner card + registry** (companion finding): the visibility artifact this framework
  operates behind.

## Potential Improvements

- Bind each element to a verifiable artifact: job → one-sentence statement in the agent
  definition; diet → declared context spec; boundaries → declared permissions; review
  loop → declared cadence + last-review date.
- Team-scale version: the operating team owns the operating agent, with one
  single-threaded owner accountable for whether it works.

## Potential Failure Modes

- **Review-loop decay:** the loop is the first thing skipped once outputs look clean —
  exactly when unnoticed drift accumulates ("because the output looks really clean,
  people stop noticing where it came from").
- **Diet sprawl:** the fix-the-inputs rule fails if nobody prunes; diet is a curation
  duty, not a one-time grant.
- **Ladder without criteria:** "earn more permission" is subjective here; without
  explicit reliability criteria (see the progressive-autonomy-ramp finding) it becomes
  vibes-based escalation.
- **One-sentence-job oversimplification:** some legitimate agents (orchestrators,
  meta-loops) resist a single-sentence job; the test is a smell detector, not a law.
