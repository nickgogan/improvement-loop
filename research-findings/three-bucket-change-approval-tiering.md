---
name: Three-Bucket Change Approval (Auto-Approve / Needs-Sign-Off / More-Context)
summary: 'A self-improving system''s proposed changes are tiered into three buckets: auto-approve

  (low-risk fixes — data bloat, missed linkages — applied automatically and logged to a

  changelog.md), need-sign-off (higher-stakes changes — skill edits, new skills,

  structural changes — written to a dated review file as a checkbox list with approve /

  reject / approve-and-don''t-ask-again), and more-context-required (items the system

  cannot decide alone, appended to the same review file). The middle ground between full

  automation (system drift) and review-everything (abandonment); the

  approve-and-don''t-ask-again option is preference memory that teaches the classifier

  over time.'
implementation_notes: 'Governance-gated, KB-first: this touches DD-29 (human gate at every stage boundary) —

  any engine adoption is a separate, explicit Nick gate, not a pipeline outcome. What it

  would offer: DD-29''s gate is binary per stage; this tiers *within* the gate, keeping

  Nick on high-stakes calls while low-risk mechanics self-apply with an audit trail

  (changelog) — directly serving the standing reduce-Nick-bottleneck direction. Concrete

  mechanics to preserve if ever designed: changelog for auto-approved changes, single

  dated review file for buckets 2+3, and don''t-ask-again preference memory.'
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (gate tiering)
- General
adopted_in: []
sources:
- how-to-build-a-self-improving-system-with-claude.md
- 8-claude-loops-to-build-10x-faster.md
related_findings:
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: same-problem
- file: permission-channel-as-escalation-steering-bus.md
  rel: same-problem
- file: automation-verification-gate-skill.md
  rel: same-problem
- file: critical-call-checkpoint-gate-placement-heuristic.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: raw
---

## What It Is

When an improve-system loop analyzes ingested data and proposes changes, every proposal
is classified into one of three buckets before anything is applied:

1. **Auto-approve** — low-risk, not-up-for-debate improvements (data bloat cleanup,
   missed linkages, obvious fixes). Applied automatically; every change logged to a
   `changelog.md` so the human can audit after the fact without gating before it.
2. **Need sign-off** — anything where a wrong choice could degrade output quality: skill
   edits, new skill candidates, structural changes. Written to `output/review-<date>.md`
   as a checkbox list; each item offers **approve / reject / approve-and-don't-ask-again**.
3. **More context required** — items the system cannot classify alone (e.g., a person
   mentioned three times: new client or one-off?). Appended to the same review file so
   the human reviews everything in one sitting.

The design sits deliberately mid-spectrum: full automation is least work but drifts;
review-everything is safe but gets abandoned. The don't-ask-again option is the
compounding piece — each use converts a class of future bucket-2 items into bucket-1,
so the human's review load shrinks over time. "AI makes the easy calls; I prefer making
the hard ones."

## Why It Matters for Us

This is the strongest reduce-Nick-bottleneck mechanism in the July-2026 intake batch. The
engine's DD-29 gate is binary — everything crossing a stage boundary waits for Nick. The
three-bucket pattern shows a governed alternative: tier the changes inside the gate,
auto-apply the mechanical tier with an audit trail, and concentrate human attention on
the tier where taste actually matters ("keeps you as the tastemaker"). Because it
modifies how the human gate operates, it is governance-gated: this finding records the
pattern; adoption is a separate Nick decision.

## Why People Are Using It

Documented and screen-demonstrated twice by the same practitioner (Marchese, 2026-06-28
and 2026-07-03), taught to "hundreds" in his cohort per his claim. The 2026-07-12 intake
triage flagged three-bucket gate-tiering as having **three independent sources** in the
batch — the two Marchese videos plus autonomy-tiering corroboration landing in a parallel
lane — making it a /reassess-priorities evidence-strength candidate once cross-lane
links settle. The KB's existing HOTL autonomy-tiering and permission-channel findings
reach the same tier-the-gate conclusion from the escalation direction.

## Potential Alternatives

- **HOTL autonomy tiering** (existing finding): tiers by *operation class* upfront rather
  than classifying each proposed change at runtime.
- **Review-everything with better UX** (checkbox files, HTML review surfaces): keeps the
  binary gate but lowers its cost — safer, but doesn't compound.

## Potential Improvements

- Preference-memory audit: don't-ask-again decisions accumulate silently; a periodic
  review of the auto-approve ruleset would catch scope creep.
- Risk-classifier evaluation: sample auto-approved changes periodically and check whether
  any were actually bucket-2.

## Potential Failure Modes

- Misclassification: the whole design rests on the system's risk judgment; a
  high-stakes change classified as bucket-1 is applied ungated.
- Bucket-1 scope creep via don't-ask-again — the auto-approve surface only ever grows.
- Changelog theater: an audit trail nobody reads gives the feeling of oversight without
  the fact of it.
