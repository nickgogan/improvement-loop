---
name: Meta-Skill for Skill Authorship
summary: Skills that teach agents how to author other skills — closing the meta-loop on framework self-extension. Anthropic ships skill-creator as the canonical implementation (anthropics/skills/skills/skill-creator,
  ~485 lines), with operational mechanics including draft → test → grade → improve iteration, eval-viewer with per-test feedback, description-triggering optimization via held-out test set, and blind A/B
  comparison between skill versions. Superpowers' writing-skills/ is a community-built counterpart. Both demonstrate that skill authorship is itself a workflow worth packaging.
implementation_notes: 'Two production implementations corroborate the pattern. (1) Anthropic''s skill-creator (Oct 2025, official, distributed via plugin marketplace at /plugin install example-skills@anthropic-agent-skills)
  — full iteration loop with eval-viewer, benchmark.json schema, description optimizer (`python -m scripts.run_loop`), packaging via `package_skill.py`. Generator-assessor separation enforced: grader.md,
  comparator.md, analyzer.md are separate subagent definitions. (2) Superpowers'' writing-skills (community, v5.0.7) — persuasion principles, structural templates, testing methodology. The Anthropic implementation
  is the production reference; the convergent community implementation is independent corroboration. Anthropic''s engineering post explicitly names this as the forward trajectory: ''we hope to enable agents
  to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities.'''
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-equipping-agents-with-agent-skills.md
- anthropic-skills-repo.md
- building-great-agent-skills-the-missing-manual.md
related_findings:
- file: visual-skills-management-and-meta-skill-creator.md
  rel: same-problem
- file: skill-description-optimization-loop-held-out-test.md
  rel: extends
- file: generator-assessor-separation-in-skill-iteration.md
  rel: extends
- file: iterate-on-single-task-then-extract-skill.md
  rel: extends
- file: skill-authoring-four-guidelines.md
  rel: extends
- file: skill-authoring-explain-the-why-not-musts.md
  rel: extends
- file: self-improving-skill-lessons-log.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-07-12'
pipeline_status: raw
consumed_by: []
---
# Meta-Skill for Skill Authorship

## What It Is

A skill whose purpose is to help agents and authors create and improve other skills. The pattern closes the meta-loop: the system that defines skills also has a skill for defining skills.

Three convergent implementations corroborate the pattern:

**Anthropic skill-creator** (`anthropics/skills/skills/skill-creator/SKILL.md`, ~485 lines). Distributed via `/plugin install example-skills@anthropic-agent-skills`. Operational mechanics:
- **Draft** — interactive interview (capture intent, define success criteria, draft SKILL.md).
- **Test** — spawn with-skill and baseline subagents in parallel; capture timing data on completion.
- **Grade** — separate grader subagent reading `agents/grader.md` evaluates assertions against outputs.
- **Aggregate** — `scripts/aggregate_benchmark.py` produces benchmark.json with pass_rate, time, tokens (mean ± stddev + delta).
- **Review** — `eval-viewer/generate_review.py` opens an HTML reviewer with Outputs and Benchmark tabs.
- **Improve** — author iterates on SKILL.md based on transcripts and user feedback; rerun for next iteration.
- **Description optimization** — `scripts/run_loop.py` runs a 60/40 train/test split with up to 5 iterations, best description by test score.
- **Blind comparison** — separate comparator + analyzer subagents for A/B between skill versions.
- **Package** — `scripts/package_skill.py` produces a `.skill` file for distribution.

**Superpowers writing-skills** (community, github.com/obra/superpowers v5.0.7). Includes persuasion principles, structural templates, testing methodology. Less elaborated mechanics than skill-creator but the same architectural pattern.

**Pocock writing-great-skills** (community, Matt Pocock's skills repo, announced at AI Engineer 2026-06-29). A third convergent implementation, distinct in kind: where skill-creator packages an *empirical iteration loop* (draft → test → grade → improve), writing-great-skills packages an *audit rubric* — a four-part checklist (trigger: user- vs model-invoked decision; structure: steps+reference anatomy, branch analysis; steering: leading words, leg-work; pruning: duplication, sediment, no-op deletion test) encoded as a skill so an agent can run it over its own or community-authored skills. Pocock's framing of the gap is the pattern's rationale stated plainly: "we don't know what makes a skill great... no shared rubric, no framework for looking at a skill and making it better."

## Why It Matters

Most agent frameworks are human-extended only — when you need a new capability, a human writes it. A meta-skill enables agent-assisted framework extension with rigor. Three properties matter:

1. **Distillation over specification.** Skill authorship is a discovery problem (what context does Claude need?). The meta-skill operationalizes the discovery loop.
2. **Generator-assessor separation enforced.** skill-creator NEVER both generates and grades the same artifact in the same context. This is exactly IL governance rule 10 — established independently by Anthropic.
3. **Triggering as a tunable layer.** The description optimization loop makes "does the skill load when it should?" empirically measurable. This is the most consequential layer of skill authoring and historically the hardest to assess.

Anthropic's engineering post explicitly names this trajectory: "we hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities."

For Improvement Loop, the existence of three convergent implementations (Anthropic's iteration loop, Superpowers' authoring guide, Pocock's audit rubric) is well past the evidence threshold: the pattern earns substrate. The pattern's mechanics inform IL Stream B's `/design-skill` and `/design-agent` skill designs.

## Why People Are Using It

Anthropic's skill-creator is the production reference, distributed via the official plugin marketplace and recommended in the Complete Guide PDF as the path to "a functional skill in a single sitting - often in 15-30 minutes." Community adoption visible in awesome-agent-skills lists and the plugin marketplace ecosystem. Superpowers' independent implementation suggests the pattern arises whenever a framework reaches the point where skill quality matters.

## Potential Alternatives

Human-only authorship with documentation guides (no rigor floor, doesn't scale). Template-based scaffolding only (no iteration loop). External code-generation tools (decouple from the framework's conventions). Copy-paste from existing skills (no methodology). All of these work for narrow cases; none operationalize the four authoring guidelines or the generator-assessor separation that skill-creator does.

## Potential Improvements

Cross-skill grader sharing (many skills could share a common grader rather than each shipping its own). Telemetry from production skill usage feeding back into description optimization. Skill version-control with regression suite — when description changes, automatically check that triggering accuracy on the historical test set didn't degrade. Meta-skill for meta-skills: a pattern for evolving the authorship methodology itself as the surface evolves.

## Potential Failure Modes

**Quality degradation through agent-authored examples.** If agent-written skills become the examples that future agents learn from, drift compounds. Anthropic's skill-creator addresses this by including human-curated examples (the document skills, the frontend-design skill); future drift depends on ongoing curation.

**Consistency drift.** Without ongoing validation, each generation of agent-written skills may drift further from the framework's design principles.

**Over-production.** Easy authoring produces many low-value skills. Skill discovery and listing budget pressure (1% of context window) makes this concrete: more skills = less budget per description = degraded triggering for the skills that matter.

**Meta-skill maintenance debt.** The meta-skill itself needs to evolve as the framework evolves. Anthropic's skill-creator has updated through Cowork-specific instructions and Claude.ai-specific adaptations, suggesting ongoing maintenance is needed.

**Generator-assessor erosion.** Under time pressure, authors skip the grader subagent and grade inline (skill-creator explicitly allows this). The separation is the discipline that makes assessment meaningful — collapsing it loses the value.
