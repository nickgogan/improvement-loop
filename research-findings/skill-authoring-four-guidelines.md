---
name: Skill Authoring Four Guidelines (Anthropic Engineering Canon)
summary: |-
  Anthropic's engineering post on Agent Skills lists four canonical authoring guidelines: (1) Start with evaluation — identify capability gaps on representative tasks before building. (2) Structure for scale — split SKILL.md when unwieldy; code can serve as both tool and reference. (3) Think from Claude's perspective — monitor real use; tune name and description for triggering accuracy. (4) Iterate with Claude — capture successful approaches and common mistakes into the skill during real work; ask Claude to self-reflect on what went wrong. These are first-principles, not rules; the skill-creator skill operationalizes them.
implementation_notes: "Guideline 4 — 'Iterate with Claude' — is the most novel. It frames skill authoring as a process of capturing in-context patterns: 'As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong.' This positions skill development as continuous distillation from real usage, rather than upfront design. Pair with the 'iterate on a single task before expanding' pro tip from the Complete Guide PDF for a tight loop."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-equipping-agents-with-agent-skills.md"
  - "anthropic-complete-guide-building-skills-pdf.md"
related_findings:
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
  - file: "iterate-on-single-task-then-extract-skill.md"
    rel: "extends"
  - file: "skill-authoring-explain-the-why-not-musts.md"
    rel: "same-problem"
  - file: "meta-skill-for-skill-authorship.md"
    rel: "extended-by"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Authoring Four Guidelines (Anthropic Engineering Canon)

## What It Is

The four "Getting started" guidelines from Anthropic's engineering post on Agent Skills (Oct 2025):

1. **"Start with evaluation."** Identify specific gaps in your agents' capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.

2. **"Structure for scale."** When the SKILL.md file becomes unwieldy, split its content into separate files and reference them. If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce token usage. Code can serve as both executable tools and as documentation — it should be clear whether Claude should run scripts directly or read them into context as reference.

3. **"Think from Claude's perspective."** Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts. Pay special attention to the `name` and `description` of your skill — Claude will use these when deciding whether to trigger the skill in response to its current task.

4. **"Iterate with Claude."** As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong. This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront.

## Why It Matters

These are the four orientations that distinguish effective skill authoring from naive authoring. Each maps to a failure mode that authors hit without it:

1. **Without evaluation-first**: authors build skills for problems Claude already handles fine, or miss real gaps. Skill authorship becomes a vanity project.
2. **Without scaling structure**: SKILL.md balloons past the 5K Level 2 budget; references mix exclusive paths; scripts get loaded as content when they should execute. Token cost grows, skill effectiveness drops.
3. **Without Claude's perspective**: authors write descriptions that read clearly to humans but don't match user phrasing; instructions optimize for author understanding, not model comprehension.
4. **Without iteration with Claude**: authors try to anticipate context Claude needs. They are systematically wrong. The model knows what it needs better than the author can guess — but only by demonstration, not introspection.

Guideline 4 is the most novel of the four. It reframes skill authorship from "design upfront" to "distill from observed use," and it positions Claude itself as a participant in skill development. The skill-creator skill operationalizes exactly this loop with explicit eval/feedback/iterate stages.

## Why People Are Using It

Cited canon in Anthropic's engineering post and re-stated across all derivative guides. Anthropic's own skill-creator skill implements the loop these guidelines describe. Practitioner adoption visible in awesome-agent-skills and ComposioHQ/awesome-claude-skills curated lists, where descriptions follow the structure these guidelines imply.

## Potential Alternatives

Upfront-design-only skill authoring (works for narrow use cases, fails at scale). Specification-driven authoring (write the skill against a contract — heavier and slower; loses the in-context learning benefit). Template-based authoring (skill-creator template-skill is the minimal start; the guidelines are about how to go beyond template).

## Potential Improvements

A canonical fifth guideline: "Optimize the description with a held-out test set" — the skill-creator's description-optimization loop is so distinctive it arguably deserves named status. A guideline about skill composition: how to design skills that work well alongside other skills (composability is mentioned in the PDF but doesn't have a guideline of its own). A guideline about scope ("when should this be a skill vs. a CLAUDE.md fragment vs. a subagent?") — currently scattered across docs.

## Potential Failure Modes

**Evaluation theater.** Authors claim "evaluation-first" but run trivial test cases that don't probe real gaps. Eval rigor varies wildly. The skill-creator skill addresses this with worked examples; thin treatments don't.

**Scaling structure without authoring discipline.** Splitting SKILL.md into files works only if the file references are well-positioned. Splitting for the sake of splitting creates a navigation problem.

**"Iterate with Claude" as license to ship skills without thinking.** Some authors interpret guideline 4 as "just have Claude generate the skill." The guideline is about distilling observed use patterns, not delegating authorship. The PDF explicitly calls out a related yellow flag: heavy-handed ALL CAPS MUSTs as a sign of authors not iterating thoughtfully.

**Real-scenario monitoring requires infrastructure.** Guideline 3 ("think from Claude's perspective") needs telemetry: who triggered the skill, who didn't, where it went off-rails. Without it, "monitor how Claude uses your skill" is aspirational.
