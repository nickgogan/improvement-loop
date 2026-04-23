---
name: "Agent-Generated Codebase Walkthrough for Onboarding"
summary: "A coding agent produces a structured Markdown walkthrough of a codebase explaining how the system works, file by file. Simon Willison's concrete example: used Claude Code + Opus 4.6 + Showboat on his vibe-coded SwiftUI slide app 'Present' to generate walkthrough.md covering all Swift files. Use cases: onboarding to unfamiliar ecosystems, recovering knowledge from one's own stale or vibe-coded code, countering skill degradation from LLM-assisted development."
implementation_notes: "A natural fit for MetaSystem: we have many vibe-coded skills and incubator projects. A periodic agent-generated walkthrough per incubator project could serve as both onboarding doc and drift detector (if the walkthrough has to materially change between runs, the code has drifted). Pairs with the self-describing-codebase finding — walkthrough is the human-readable output; module manifests are the machine-readable input."
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "simon-willison-linear-walkthroughs-agentic-patterns.md"
related_findings:
  - file: self-describing-codebase-structural-semantic-context.md
    rel: extends
  - file: deep-plan-multi-agent-exploration-pattern.md
    rel: same-problem
  - file: programmatic-snippet-extraction-via-shell-anti-hallucination.md
    rel: enabled-by
  - file: agent-onboarding-via-interview-style-context.md
    rel: same-problem
  - file: interactive-explanations-extend-linear-walkthroughs.md
    rel: extended-by
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is

A pattern where a coding agent reads an entire codebase and produces a structured Markdown document that walks through the system, typically file by file, explaining architecture, mechanics, and key interactions. Simon Willison names this "linear walkthrough" in his "Agentic Engineering Patterns" guide.

Simon's concrete workflow:
- Target: his own vibe-coded SwiftUI slide-presentation app ("Present", ~40 minute project).
- Agent: Claude Code with Opus 4.6.
- Harness: Showboat — a purpose-built tool that lets the agent embed Markdown notes (`showboat note`) and shell command outputs (`showboat exec`) directly into the walkthrough document.
- Output: a 6-file walkthrough.md explaining every Swift file in the repo.

The agent is explicitly instructed to use `sed`, `grep`, or `cat` to extract code snippets rather than copying them by hand — see companion finding on programmatic snippet extraction.

## Why It Matters

Three distinct use cases, each valuable:

1. **Onboarding to an unfamiliar ecosystem.** Simon reports: "I learned a great deal about how SwiftUI apps are structured and absorbed some solid details about the Swift language itself just from reading this document." The walkthrough doubles as a tutorial for the user.

2. **Recovering knowledge from stale code.** Projects written months ago, or vibe-coded in a single sitting, lose their mental model quickly. A walkthrough rebuilds it without requiring a full re-read.

3. **Countering skill degradation.** A stated concern in the guide: heavy LLM-assisted development erodes direct-reading skill. Walkthroughs, produced by an agent but read by a human, restore the reading practice.

For MetaSystem specifically, this is directly usable. Many skills, hooks, and incubator projects are vibe-coded first-drafts that could benefit from a periodic walkthrough regeneration — both as onboarding artifact and as implicit drift detection (a walkthrough that has to materially change between regenerations tells you the code is evolving in ways that deserve attention).

## Why People Are Using It

Source: Simon Willison's "Agentic Engineering Patterns" guide (simonwillison.net). Published Feb 25 2026, last modified March 4 2026. Part of the "Understanding code" chapter group, counterpart to "Interactive explanations."

Simon is a Tier 1 independent practitioner — co-creator of Django, author of Datasette, one of the most consistent public documenters of frontier AI patterns since 2022. His first-party testimony plus the public example repo (github.com/simonw/present) constitutes practitioner evidence.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Interactive explanations | Agent answers ad-hoc questions about the code | When the user's questions are narrow, not comprehensive |
| Hand-written README / ARCHITECTURE.md | Human-authored documentation | When the code is small or the human has a strong mental model already |
| Self-describing codebase manifests | Structured machine-readable module manifests | When the audience is another agent, not a human |
| Auto-generated API docs | Tool-extracted docs (JSDoc, rustdoc, etc.) | For library-shaped code where API surface is the key concern |

## Potential Improvements

- **Regeneration cadence** — decide per-project how often walkthroughs refresh. Too often wastes tokens; too rarely lets drift accumulate.
- **Diff-over-walkthrough** — after the first walkthrough, subsequent runs could produce diffs-since-last-walkthrough rather than full regeneration.
- **Integration into `/onboard` skills** — the walkthrough could be the primary artifact a new agent reads at session start.
- **Walkthrough as eval** — if the walkthrough correctly explains the code, it's implicit evidence the agent read and understood. Walkthrough accuracy becomes a comprehension eval.

## Potential Failure Modes

- **Agent hallucinates the architecture** — the walkthrough reads plausibly but mischaracterizes how modules interact. Mitigated by programmatic snippet extraction (forcing the agent to show actual code, not describe it).
- **Walkthrough rot** — the code changes, the walkthrough doesn't, and readers are actively misled.
- **Over-broad walkthroughs for large codebases** — the pattern scales poorly beyond 10-20 files; for large codebases, targeted walkthroughs per module beat one monolithic doc.
- **Dependence on a harness** — Simon uses Showboat; agents without a comparable tool may fall back to manual snippet copying (the failure mode Simon explicitly warns against).
