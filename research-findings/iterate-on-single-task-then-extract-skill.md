---
name: Iterate on a Single Task Until Claude Succeeds, Then Extract the Skill
summary: The most effective skill-authoring pattern from Anthropic is to iterate on ONE challenging task until Claude succeeds, then extract the winning approach into a skill. This leverages Claude's in-context learning during the iteration loop and provides faster signal than broad testing. Only after a working foundation exists do you expand to multiple test cases for coverage. The Anthropic Complete Guide names this as a 'Pro Tip' and the skill-creator skill operationalizes the loop with iteration-N workspace directories.
implementation_notes: "Counter-intuitive ordering: skill-authoring inverts traditional 'write spec, then test' methodology. The methodology is 'work through the task in conversation, watch what Claude does well and badly, distill the winning approach into SKILL.md, THEN test against held-out variants for coverage.' Anthropic's authoring guidance: 'As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong.' This is the in-context distillation pattern. The skill-creator workspace structure (iteration-1/, iteration-2/, ... with eval-0/, eval-1/) supports this loop mechanically."
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
  - "anthropic-skills-repo.md"
  - "anthropic-complete-guide-building-skills-pdf.md"
related_findings:
  - file: "skill-authoring-four-guidelines.md"
    rel: "extends"
  - file: "meta-skill-for-skill-authorship.md"
    rel: "extended-by"
  - file: "skill-authoring-explain-the-why-not-musts.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Iterate on a Single Task Until Claude Succeeds, Then Extract the Skill

## What It Is

The recommended skill-authoring sequence from Anthropic:

1. **Pick one challenging task** — not a representative test set yet, just one task the skill should enable.
2. **Work through it with Claude** — collaborate inline, observe what Claude does well and badly, course-correct in conversation.
3. **Distill the winning approach** — capture the successful pattern (and the named mistakes to avoid) into SKILL.md.
4. **Test against held-out variants** — only after the skill works on the original task, expand to coverage across paraphrased and adjacent tasks.

The Complete Guide PDF names this a "Pro Tip" and credits it to early skill creators. The skill-creator skill operationalizes the loop with workspace directories named `iteration-1/`, `iteration-2/`, etc., each containing per-eval subdirectories.

The cognitive frame: skill authorship is distillation, not specification. You don't know what context Claude needs until you watch what it does. Iterating on one task first reveals the gap; the skill captures the bridge.

## Why It Matters

This inverts traditional spec-driven development. The traditional sequence is: write spec, design implementation, test. Skill authoring's sequence is: work through one task, distill the working approach, test variants.

The reasoning is empirical: Anthropic's authoring observation is that authors *systematically guess wrong* about what context Claude needs. Working through a single task with Claude reveals the true gap; specifying it upfront does not.

This pairs with the engineering post's fourth guideline ("iterate with Claude"). Together they form a methodology: discover-by-doing on one task, distill, then expand.

The "single task first" rule also defeats premature optimization. Without it, authors spend time writing eval matrices for skills that don't yet work on any task.

## Why People Are Using It

Cited as the "most effective" pattern by Anthropic's own observation across early adopters and internal teams. Embedded in skill-creator's workspace structure. The Complete Guide PDF's claimed "15-30 minutes to first working skill" target depends on this pattern — the iteration loop assumes single-task focus.

## Potential Alternatives

Spec-first authoring (write SKILL.md upfront from imagined requirements — generally weaker because authors guess context wrong). Test-matrix-first (build a test suite, then iterate against it — slower; you can fail many tests without learning what to fix). Copy-template (start from template-skill, fill in — works for simple skills but doesn't develop authoring judgment).

## Potential Improvements

A canonical "minimum task description" structure that produces good iteration starting points. Per-iteration retrospective prompts — "what did Claude get wrong this time, and what context would have helped?" — that translate iteration observations directly into SKILL.md edits. Cross-skill iteration patterns: lessons from authoring skill A that help start skill B.

## Potential Failure Modes

**One-task overfitting.** If the chosen task happens to have idiosyncrasies, the distilled skill encodes them. The held-out test step (expansion to variants) is the defense; skipping it means the skill works only on its training task.

**Iterating on an under-specified task.** If the original task isn't a clear win/lose, "Claude succeeds" is fuzzy. The skill never reaches a stable distillation point.

**Confusing context for instruction.** Authors distill the user's specific context (project paths, dataset names, etc.) into SKILL.md, making the skill non-portable. The distillation should capture the workflow shape, not the particulars.

**Iteration without distillation.** Working through 5 tasks in conversation without capturing the working approach into SKILL.md produces no skill — just a long session.

**Stopping at the first success.** Skills that work on one task often don't generalize. The methodology requires the expansion step; the named "Pro Tip" frames single-task as the *starting* point, not the endpoint.
