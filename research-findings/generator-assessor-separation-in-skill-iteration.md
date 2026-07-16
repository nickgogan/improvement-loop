---
name: Generator-Assessor Separation in Skill Iteration (Anthropic Skill-Creator)
summary: Anthropic's skill-creator skill operationalizes a strict separation between generation and assessment in the skill-development loop. The skill-creator drafts/iterates skills; a separate grader
  subagent (instructed via agents/grader.md) evaluates assertions against outputs; a separate comparator (agents/comparator.md) does blind A/B between skill versions; a separate analyzer (agents/analyzer.md)
  explains why one version won. This is direct external corroboration of IL governance rule 10 (generator-assessor separation), arrived at independently by Anthropic in production skill authoring.
implementation_notes: 'Verbatim from skill-creator: ''Grade each run — spawn a grader subagent (or grade inline) that reads agents/grader.md and evaluates each assertion against the outputs.'' For blind
  comparison: ''give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won.'' The pattern is consistent across the loop: draft
  (skill-creator) → run tests (with-skill + baseline subagents) → grade (grader subagent) → if comparing versions (comparator + analyzer subagents). The skill-creator never both generates AND evaluates
  the same artifact. This is exactly rule 10 in MetaSystem''s IL governance — established independently.'
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Already Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in:
- Improvement Loop
- General / Cross-System
sources:
- anthropic-skills-repo.md
- i-built-a-deck-with-ai-then-made-a-second-ai-attack-it.md
related_findings:
- file: skill-description-optimization-loop-held-out-test.md
  rel: enables
- file: machine-framework-for-agentic-coding-skill-asses.md
  rel: same-problem
- file: meta-skill-for-skill-authorship.md
  rel: same-problem
- file: enumerate-dont-fix-hostile-reviewer-prompt.md
  rel: extended-by
- file: cross-vendor-adversarial-build-attack-loop.md
  rel: extended-by
- file: task-risk-gradient-for-verification-depth.md
  rel: extended-by
- file: closed-loop-floor-open-exploration.md
  rel: same-problem
- file: multi-perspective-review-council.md
  rel: extended-by
- file: no-mistakes-post-implementation-validation-pipeline.md
  rel: same-problem
- file: persona-clone-review-board.md
  rel: extended-by
- file: two-axis-parallel-code-review-standards-vs-spec.md
  rel: same-problem
- file: with-without-skill-ab-baseline-measurement.md
  rel: same-problem
- file: controller-deauthorization-reviewer-independence.md
  rel: same-problem
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---

# Generator-Assessor Separation in Skill Iteration (Anthropic Skill-Creator)

## What It Is

Anthropic's official skill-creator skill structures the skill-development loop as a strict separation of roles, each handled by a distinct subagent context:

| Role | Agent Definition | Job |
|---|---|---|
| **Generator (skill author)** | skill-creator/SKILL.md | Drafts and iterates SKILL.md |
| **Executor (with-skill / baseline)** | Spawned subagents per eval | Runs the skill (or baseline) on each test case |
| **Grader** | skill-creator/agents/grader.md | Evaluates assertions against outputs |
| **Comparator** | skill-creator/agents/comparator.md | Blind A/B between two skill versions |
| **Analyzer** | skill-creator/agents/analyzer.md | Explains why one version beat the other |

Each is a separate agent definition, intended to be spawned as an independent subagent context. The skill-creator NEVER both generates and assesses the same artifact in the same context.

The directness from skill-creator: "Grade each run — spawn a grader subagent (or grade inline) that reads `agents/grader.md` and evaluates each assertion against the outputs." For blind comparison: "give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won."

## Why It Matters

This is direct external corroboration of IL governance rule 10 ("Generator-assessor separation") arrived at independently in Anthropic's production skill-authoring tooling. Two independent teams faced the same problem — skill quality assessment is unreliable when the same context generated the skill — and reached the same architectural answer: separate the contexts.

The corroboration matters for IL Stream 0 / B-lite because it confirms that the rule isn't a MetaSystem-specific convention but a recurring solution to a recurring problem. When Stream B-lite proposes `/design-skill` and `/design-agent`, the same separation pattern should apply: the design skill must delegate quality assessment to a separate assessor invocation, not self-grade.

The skill-creator's approach also enriches the rule with concrete operational mechanics:
- **Grader receives assertions, not just outputs** — the assessor doesn't decide what good looks like; the spec does.
- **Blind comparison hides which output is which** — defeats positional bias.
- **Analyzer post-hoc explains the win** — separates "which won" from "why it won," each in fresh context.

## Why People Are Using It

Built into Anthropic's officially distributed skill-creator skill. The separation is explicit and instrumented (assertions saved to JSON, grading.json schema versioned for an HTML reviewer, benchmark.json aggregation). This is production-grade rigor, not aspirational design.

## Potential Alternatives

Self-grading (the skill-creator could grade its own outputs — explicitly rejected by the design). Single-grader-multiple-roles (one subagent both grades and compares — collapses the distinct epistemic positions). Human-only grading (skips the assistant entirely — slower, harder to scale, but ground-truth). LLM-as-judge with the same context (cheaper but reproduces the self-grading anti-pattern).

## Potential Improvements

Cross-skill grader sharing — many skills could share `agents/grader.md` rather than each ship its own. Grader templates for common assertion shapes (file-output assertions, regex assertions, semantic-equivalence assertions). Calibration of grader reliability (run the grader on known-good and known-bad outputs to measure base rates). Analyzer-augmented improvement loop — feed "why the winner won" back into the generator's next iteration.

## Potential Failure Modes

**Grader-context leak.** If the grader subagent receives the SKILL.md itself (not just the assertions and outputs), it knows what the skill was trying to do and may bias toward judging on intent rather than result.

**Assertion drift.** Authors who write the assertions are the same authors who write the skill. The assertion set encodes their assumptions about what success looks like. Mitigation: pair assertion authoring with user review.

**Blind comparison preferences.** Even blind comparators have biases (verbose-over-terse, format preferences). Multiple comparator runs with shuffled order help; not eliminated.

**Analyzer post-hoc rationalization.** Asking the analyzer "why did X win" can produce coherent narratives that don't reflect the real causal driver. The pattern is useful for human consumption but should be discounted as direct evidence.

**Convenience erosion.** Under deadline pressure, authors skip the grader subagent and "grade inline" (skill-creator explicitly allows this). This collapses the separation under exactly the conditions where the discipline matters most.

## Corroboration Log

**2026-07-12 (session 136) — third independent corroboration.** Nate B Jones's production
office-document workflow (`i-built-a-deck-with-ai-then-made-a-second-ai-attack-it.md`)
arrives at the same architecture independently of both Anthropic's skill-creator and the
engine's rule 10: one model builds (Codex), a separate model attacks (Opus 4.7
hostile review), looped to convergence. This makes three independent origins for the
separation pattern — a /reassess-priorities evidence-strength candidate. Three genuine
deltas from this source are extracted as their own findings (linked `extended-by` above):

1. **Enumerate-don't-fix task flip** — the mechanism underneath the separation, and its
   cheapest form (works even same-model): `enumerate-dont-fix-hostile-reviewer-prompt.md`.
2. **Cross-vendor pairing + terminal language-polish pass** — decorrelating blind spots by
   training lineage, and sequencing polish after substance:
   `cross-vendor-adversarial-build-attack-loop.md`.
3. **Task risk gradient** — calibrating how much assessor/human depth each artifact class
   gets: `task-risk-gradient-for-verification-depth.md`.

Annotation only — priority unchanged pending the gated /reassess-priorities pass.
