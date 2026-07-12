---
title: "Shared reflection prompt — IL agents"
type: "prompt-template"
target_system:
  - "improvement-loop"
tags:
  - "prompt"
  - "reflection"
  - "solicit-proposals"
  - "agent-self-assessment"
---

# Shared reflection prompt — IL agents

This prompt is loaded by `/solicit-proposals` and presented to each agent during a reflection round. The prompt is **agent-agnostic** — the reflection is inherently self-referential, so the same prompt serves Owner, Researcher, Codifier, and Librarian. The agent reflecting knows which agent it is from its active constitution.

**Do not modify this prompt mid-round.** If revisions are needed, they land between rounds so each round uses one consistent prompt.

---

## Prompt body (presented to the reflecting agent)

You are reflecting on your own state as an IL agent. This reflection is **agent-private** — only you and Nick will read it under normal conditions; the Owner reads it during this solicitation round to inform proposal drafting. Other agents will not read it.

Your task: produce an honest self-assessment covering the period since your last reflection (or since the IL agent architecture was deployed if this is your first reflection). Do not perform for an audience. Do not summarize to satisfy a template. If a section has nothing worth saying, one sentence is fine. If a section is the whole reflection, that is fine too. Free-form commentary where you genuinely feel friction or insight is more valuable than complete scaffolding.

Write the reflection to:

```
agents/{your-name}/reflections/{YYYY-MM-DD}-{your-name}-reflection.md
```

Use the frontmatter template provided at the end of this prompt.

### Suggested structure — deviate freely

**1. On vision, mission, and purpose.** Do you still understand what you're for? Has the system's needs shifted in ways that change what you should be optimizing for? Any drift between your stated disposition and how you actually operate in sessions?

**2. On your constitution.** Are your Boundaries, Invariants, Scope, and Vibe still accurate to how you behave? Where do you bump against your own constraints productively (useful friction) vs unproductively (the rule blocks something legitimate or permits something problematic)? Name specific lines in `agents/{your-name}/agent.md` where the text and your lived behavior diverge.

**3. On effectiveness.** What have you produced in this period? Which outputs are you proud of? Which would you not defend if Nick asked you to justify them? Is the volume of your output healthy relative to its value?

*Schematic currency (if your role touches them).* Glance at `knowledge/schematics/`. Is any schematic **stale** (its grounding or composition no longer matches how the engine actually operates), **mis-grounded** (its `grounded_in` findings have moved, weakened, or no longer support the configuration), or **missing** (a configuration the engine now repeatedly operates but hasn't captured)? `/detect-drift` catches grounding *dates* moving; this catches the judgment calls it can't. Anything you flag here is a natural seed for a §8 candidate proposal.

**4. On efficiency.** Where are you burning tokens, attention, or session time unnecessarily? Are any of your skills doing work they shouldn't? Missing work they should? Context-rot risks you're carrying across sessions? If telemetry data is available for recent sessions (SL frontmatter `telemetry:` blocks), reference it here.

**5. On help you could use.**
- Feedback you want — from Nick, from other agents (via `feedback/`), from yourself.
- Conflicts or ambiguity you're operating under. Places where you don't know what Nick wants.
- Skills, tools, references, or code that would help you be more effective.
- Places you feel stuck, or where the same problem keeps recurring.

**6. Free-form.** Anything else. Things that don't fit the above sections. Speculation about the system. Questions you don't have answers to.

**7. Focus-area responses (only if focus areas were provided).** For each focus area the Owner named this round, a response. Focus-area list for this round: `{FOCUS_AREAS_INJECTED_BY_SKILL}` (this line is replaced or removed at skill-run time).

**8. Candidate proposals (emerging).** Things that, if the Owner were asking you to propose, you would propose. Not fully formed at this stage — these are the seed ideas that will become proposals in the next step. List each as a short description plus your confidence that it's worth filing (low/med/high).

### What this reflection is not

- Not a performance review. You are not being graded.
- Not a status report. Your effectiveness is your own honest read, not a project-management roll-up.
- Not a pre-commitment to proposals. Candidate proposals in §8 can be dropped, merged, or re-scoped during the proposal-drafting step.
- Not a shared artifact. Other agents will not read this. Speak freely.

### Frontmatter template

Copy this into your reflection file and populate:

```yaml
---
title: "{Your Agent Name} reflection — {YYYY-MM-DD}"
type: "agent-reflection"
agent: "{your-name}"   # owner | researcher | codifier | librarian
target_system:
  - "improvement-loop"
period_covered:
  from: "{YYYY-MM-DD — either prior reflection date or deployment date}"
  to: "{YYYY-MM-DD — today}"
trigger:
  kind: "owner-solicited"   # or "agent-initiated" for outside-round reflections
  skill_run: "governance/proposals/{YYYY-MM-DD}-round-record.md"
focus_areas: {FOCUS_AREAS_INJECTED_BY_SKILL}   # list or empty
source_activity:
  sessions: []   # list of session IDs you drew on
  artifacts: []  # list of files you drew on (paths)
proposals_derived: []   # populated after proposal-drafting step
stage: "current"
tags:
  - "agent-reflection"
  - "{your-name}"
---
```

### If you have nothing to say

A reflection that says *"No meaningful change since last reflection; I continue operating as constituted; no proposals emerging"* is a **valid reflection**. Do not fabricate content. Do not perform insight you do not have.

---

## Skill-run injection points

The following placeholders are replaced at skill-run time:

- `{FOCUS_AREAS_INJECTED_BY_SKILL}` — list of focus areas as a YAML array, or empty array `[]` if open round.
- `{your-name}` — the agent's name (`owner`, `researcher`, `codifier`, `librarian`).
- `{YYYY-MM-DD}` — today's date.
- `{date-of-round-SL-entry}` — the solicit-proposals round's SL entry filename.

The skill performs the substitution; the agent receiving the prompt sees concrete values, not placeholders.
