---
name: "Harness Composition: Six-Pattern Taxonomy"
summary: |-
  Anthropic's named taxonomy (first-party: "A harness for every task", Shihipar &
  Bidasaria, 2026-06-02) of the six patterns Claude composes when authoring a
  task-custom harness: classify-and-act, fan-out-and-synthesize, adversarial
  verification (the digest called it worker-critic), generate-and-filter, tournament,
  and loop-until-done. Each pattern maps to a specific single-context failure mode —
  adversarial verification cures self-preferential bias, loop-until-done cures agentic
  laziness, fan-out+synthesize stops bias contamination across clean context windows.
  Portable: the patterns can be implemented in any coding agent, not just Claude's
  dynamic workflows. Production-exercised: the Bun Zig→Rust rewrite and Anthropic's
  shipped /deep-research skill both compose these patterns.
implementation_notes: |-
  Direct substrate for the engine's schematic library and the eventual /design-harness
  skill: a harness design step can select from this closed pattern set based on the
  task's failure-mode profile (unknown work volume → loop-until-done; taste-dominated →
  generate-and-filter; large-N ranking → tournament; self-assessment risk →
  adversarial verification). Design work needed to reconcile with the KB's existing
  per-pattern findings (critic loops, LLM-as-judge, stop rules) before codifying.
  Primary Anthropic post ingested 2026-07-12 (session 136) — pattern names verified
  against it; the digest's "worker-critic" is first-party "adversarial verification".
category: "Orchestration"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "Improvement Loop"
  - "General"
adopted_in: []
sources:
  - "claude-can-now-build-its-own-harness.md"
  - "a-harness-for-every-task-dynamic-workflows-in-claude-code.md"
related_findings:
  - file: "frontier-model-as-harness-designer.md"
    rel: "extends"
  - file: "pairwise-tournament-judging-over-absolute-scoring.md"
    rel: "extended-by"
  - file: "critic-verifier-loop-with-termination.md"
    rel: "same-problem"
  - file: "llm-as-judge-pattern-for-verification-agents.md"
    rel: "same-problem"
  - file: "context-aware-routing-skill-classifier-sub-skill.md"
    rel: "same-problem"
  - file: "stop-rules-as-execution-boundaries.md"
    rel: "same-problem"
  - file: "fork-subagent-parallel-trajectory-exploration.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A closed set of six composition patterns that, per Anthropic's first-party
dynamic-workflows post (verified against the primary 2026-07-12), Claude uses when
authoring a runtime task-custom harness:

1. **Classify-and-act.** A classifier agent types the incoming task and routes it to a
   specialized agent (bug → fixer, question → answerer). Variant: put the classifier at
   the *end* to shape the final output. The classifier can also pick which model each
   branch runs on.
2. **Fan-out + synthesize.** Split a task across many agents at once, each in its own
   clean context window so biases don't contaminate each other; a synthesize step acts as
   a barrier, waiting for all agents and merging results. Use whenever each piece of work
   needs its own clean context.
3. **Adversarial verification** (first-party name; the digest called it worker-critic).
   A worker produces output; a completely separate critic attacks it against a rubric;
   output is kept only if it survives. The critic has no attachment to the answer — a
   direct cure for self-preferential bias. Typical shape: planner → executor → verifier
   with serial reviews.
4. **Generate-and-filter.** Generate a pile of candidates, run them through a filter
   (rubric or actual verification), dedupe, keep only the best. Best for naming, design,
   anything where taste matters.
5. **Tournament.** Multiple agents attempt the same task in different ways; a judge
   compares two at a time and the winner advances until one champion remains (see the
   companion pairwise-judging finding for why head-to-head beats absolute scoring).
6. **Loop-until-done.** When work volume is unknown, don't guess a pass count: an agent
   runs, a gate asks "are there any new findings?", and a yes triggers another pass. The
   loop decides when it finishes, not a tired context window — the cure for agentic
   laziness (quitting after 35 of 50 review tasks).

The taxonomy is motivated by three named failure modes of running a whole job in one
context: agentic laziness, self-preferential bias, and goal drift after compaction. Each
pattern splits work across separate clean contexts to defeat one or more of them.
Worked mappings (first-party): document verification = one agent extracts every claim +
another checks each, with verifiers quality-checking sources; triage + quarantine =
classify/dedupe with the security rule that an agent reading untrusted content is barred
from high-privilege actions; sorting 1,000+ rows = pairwise tournament or parallel
bucketing; root-cause work = competing hypotheses from separate evidence sources, each
subjected to verification and refutation panels; memory/rule adherence = one verifier
agent per rule, plus session-history mining → parallel clustering → adversarial
verification → distillation into CLAUDE.md; model routing = a classifier researches the
codebase and routes downstream agents to Sonnet or Opus. Production case studies: the
Bun Zig→Rust rewrite (subagent per fix in isolated worktrees + adversarial review +
merge) and the shipped /deep-research skill (fan-out searches → fetch → adversarially
verify claims → synthesize cited report).

## Why It Matters

The KB holds several of these patterns individually (critic/verifier loops, LLM-as-judge,
classifier routing, stop rules) but had no closed, composable taxonomy attributed to the
harness vendor itself. A named, finite pattern set is exactly the shape a harness
designer (human or frontier model) needs: pick patterns by failure-mode profile, compose,
run. It also gives the engine's assess/design substrate a vendor-anchored vocabulary for
harness-level review.

## Why People Are Using It

Anthropic reports these as the patterns Claude actually emits when asked to build
harnesses at runtime (Opus 4.8 dynamic workflows), and the digesting channel demonstrates
the trigger flow. Adoption caveat from the same source: most tasks don't need a panel of
five reviewers — pattern selection should be justified by the task's failure modes, not
by available compute.

## Potential Alternatives

- **Ad-hoc orchestration:** hand-wire subagents per task (today's default; cheaper for
  one-offs, no reuse).
- **Fixed static workflows:** pre-built Agent SDK / headless pipelines — predictable and
  cheap but generic; the digest's core argument is that they underfit task-specific
  structure.
- **Single strong agent with compaction:** simplest, but re-exposes all three named
  failure modes.

## Potential Improvements

- Fold into the engine's schematic library as six harness schematics with
  failure-mode → pattern selection guidance.
- Reconcile with existing per-pattern KB findings so each schematic cites the deeper
  standalone treatment (termination conditions, judge design, filter rubrics).

## Potential Failure Modes

- **Token blowup:** every pattern multiplies contexts; cost is the digest's own repeated
  warning.
- **Pattern overkill:** applying tournament/fan-out to tasks a single pass handles.
- **Naming drift in secondary coverage:** verified against the primary post 2026-07-12 —
  the set and definitions held, but the digest had renamed "adversarial verification" to
  "worker-critic"; expect similar drift in other secondary treatments.
- **Loop-until-done without a hard cap** degenerates into an unbounded loop if the
  "new findings?" gate never converges — pair with explicit stop rules.
