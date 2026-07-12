---
name: 'Two-Path Skill Authoring Decision Sequence with Hard Promotion Gates'
summary: 'Codify skill authoring as exactly two canonical paths — Path A (iterate on one real task, then distill into SKILL.md; the Anthropic-endorsed default) and Path B (spec-first with eval queries written before the body) — each ending in a HARD gate that blocks promotion: Path A gates on description trigger accuracy (90% trigger / 0% near-miss fire), Path B on a four-discipline rubric pass in every dimension. The sequence includes explicit path-switch conditions and a catalog of eight named authoring detours (skipping eval design, description drift, self-grading, context bloat, prescribed reasoning, over-production, specialization theater, convenience erosion).'
implementation_notes: 'The engine''s /design-skill already walks a construction decision sequence and delegates its audit to /assess-skill in fresh context (rule 10) — that maps to Path B plus generator-assessor separation. What it lacks is (a) the Path A default (distill from a task that already worked, rather than spec upfront), (b) any HARD gate semantics — nothing currently blocks deployment on trigger-accuracy failure, and (c) explicit path-switch conditions. The overlap with the imported /meta-skill-author toolchain (which carries this sequence as a reference doc) is a flagged open question for the restructure program''s Phase 2 audit; this finding is the comparative input for deciding which sequence survives.'
category: Agent Design
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-meta-skill-author-references.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- skill-authoring
- decision-sequence
- hard-gates
- evaluation
---

# Two-Path Skill Authoring Decision Sequence with Hard Promotion Gates

## Why It Matters

Most skill-authoring guidance is a pile of individually true rules with no ordering. This pattern turns them into a procedure: two named paths, a rule for choosing between them, explicit switch conditions when the chosen path stalls, and a gate that unconditionally stops promotion. The gate concept is the important part — a skill whose description doesn't trigger reliably is dead capability regardless of body quality, so triggering is verified *before* the skill is allowed to consume catalog budget, not after users notice it never fires.

## What It Is

- **Path A (default, Anthropic-endorsed):** pick one challenging task already completed successfully with AI → elicit the tacit knowledge behind it (5-layer, ~45-min elicitation: operating rhythms, recurring decisions, required inputs, friction points, success criteria) → draft SKILL.md from that one task → test on 3–5 variants (one paraphrase, one near-miss, one edge case) → HARD GATE on description trigger accuracy → adversarial near-miss testing → promote and graduate the passing evals into a regression suite. Path A inverts spec-driven development deliberately: "authors systematically guess wrong upfront"; distilling from a task that already worked beats specifying in advance.
- **Path B (spec-first):** for well-defined scope or compliance contexts — write 8 spec primitives and the 7-part intent structure, define the 20 eval queries *before* drafting the body, draft the body around the locked spec, then HARD GATE on the four-discipline rubric (Prompt Craft → Context → Intent → Specification, scored in dependency order; any single failing dimension blocks promotion, no trade-offs).

## How It Works

- **Hard gate semantics:** work stops until the gate passes; there is no conditional promotion. Path A fails if the skill misses ≥ 10% of clear positive queries OR fires on any should-not-trigger near-miss. Gate action is constrained: revise the *description*, not the body; after 5 failed iterations, re-run tacit-knowledge elicitation because the description likely reflects the wrong framing of the skill's purpose.
- **Path-switch table:** spec-first fails after 2+ attempts to articulate tacit knowledge → switch to A; single-task skill too narrow → expand with B's 20-query structure; body grows past 500 lines → split into separate skills.
- **Eight named detours** function as a pre-mortem checklist, each grounded in prior evidence — e.g. Detour 2 (editing the body without re-running description optimization silently breaks triggering), Detour 3 (self-grading; generator-assessor separation is "the load-bearing governance rule"), Detour 8 (convenience erosion: under deadline pressure the whole eval pipeline collapses to inline self-assessment, so separation must be the path of least resistance, not an optional step).

## How It Could Fail

The sequence is heavyweight for trivial skills — 20 eval queries and a 5-role subagent cast (Generator/Executor/Grader/Comparator/Analyzer) per skill is real cost, and the source itself warns that easy meta-authoring over-produces low-value skills that pressure the ~1% skill-listing context budget. The gates only bind if tooling enforces them; as prose, they erode exactly the way Detour 8 predicts.
