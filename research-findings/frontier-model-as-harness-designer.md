---
name: Frontier Model as Harness Designer
summary: 'The strongest available model designs the harness — the goal structure, constraints,

  and scaffolding — that execution then runs inside. Now first-party confirmed: per

  Anthropic''s own dynamic-workflows post (Shihipar & Bidasaria, 2026-06-02), with Opus

  4.8 Claude authors a task-custom harness at runtime — a JavaScript workflow with

  agent/parallel/pipeline primitives, per-agent model choice, optional worktrees, and

  resumability — and the result persists as a reusable saved artifact distributable as a

  skill. Production case study: Bun was rewritten from Zig to Rust using workflows.

  This moves the pattern from design-time advice ("use Fable 5 to design harnesses for

  cheaper executors", Nate B Jones) to a shipped, production-exercised first-party

  capability. Companion prompting guidance stands: short prompts, differentiated

  net-new context, maximum degrees of freedom.'
implementation_notes: 'Priority unchanged pending /reassess-priorities — the 2026-07-12 link-intake triage

  flagged this as an emerging hub finding (3 new extending sources in one batch), and

  the primary Anthropic post was ingested the same session (session 136), lifting the

  earlier evidence cap: first-party authorship + the Bun production case study + the

  shipped /deep-research skill ground the Strong rating. Feeds the eventual

  /design-harness skill and the model-capability registry''s Fable 5 row (harness-design

  as a named strength).'
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (harness design, model routing)
- General
adopted_in: []
sources:
- free-fable-5-tokens-heres-how-to-max-them.md
- claude-can-now-build-its-own-harness.md
- a-harness-for-every-task-dynamic-workflows-in-claude-code.md
- dont-build-more-ai-agents-until-you-watch-this.md
related_findings:
- file: harness-composition-six-pattern-taxonomy.md
  rel: extended-by
- file: frontier-capability-probing-scouting.md
  rel: same-problem
- file: frontier-model-as-unknown-unknown-elicitor.md
  rel: extended-by
- file: harness-non-portability-across-model-families.md
  rel: same-problem
- file: prototype-at-frontier-then-downshift.md
  rel: same-problem
- file: war-game-plan-format-for-executor-handoff.md
  rel: extended-by
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
pipeline_status: raw
---

## What It Is

The conventional split is "strong model plans, cheap model codes." This pushes one level
up: the strong model **designs the harness** — the goal structure, constraints, and
scaffolding — that execution runs inside.

The newest and strongest evidence is a runtime version shipped by Anthropic — now read
first-party ("A harness for every task: dynamic workflows in Claude Code", Thariq
Shihipar & Sid Bidasaria, 2026-06-02; initially ingested via a Prompt Engineering channel
digest): instead of forcing every task through the one coding-shaped harness, Claude
(Opus 4.8) writes a **task-custom harness on the fly** — a JavaScript workflow file with
three primitives (`agent` spawns a subagent in its own clean context window; `parallel`
fans several out and barriers on completion; `pipeline` streams items through chained
stages), plus per-agent model selection, optional per-agent worktrees, and
resume-after-interrupt. The motivating failure modes of single-context execution are
named: agentic laziness (quits after partial work — e.g. 35 of 50 review tasks),
self-preferential bias (grades its own work kindly), and goal drift (the brief leaks out
after compaction). The fix in every case is splitting the job across separate clean
contexts — which is exactly what the authored harness does.

Two properties elevate this beyond one-shot orchestration:

- **Harnesses are reusable saved artifacts.** A generated workflow is not consumed by its
  run; you can try several, keep the best (press "s" in the menu; stored in
  `~/.claude/workflows`), and distribute it via a skill (referenced from SKILL.md,
  optionally as a template). The frontier model's output is a reusable execution
  environment, not a plan for one task. Anthropic's own shipped `/deep-research` skill is
  built this way.
- **It works on ill-defined, non-coding work.** Per the Anthropic post: resume
  ranking, business-plan attack from three angles, mining 6 months of Slack for unfiled
  root causes, and mining one's own session history into CLAUDE.md rules (cluster
  recurring corrections in parallel, adversarially verify candidates, distill survivors).
- **It carries production weight.** The post's headline case study: **Bun was rewritten
  from Zig to Rust using workflows** — a subagent per fix in an isolated worktree,
  adversarial review by a separate agent, then merge, with the guidance to avoid
  resource-intensive commands so parallelism stays maximal.

The independent practitioner framing (Nate B Jones, 2026-07-04 — published after the
digest but carrying weaker, opinion-tier evidence) remains as the design-time half of the
pattern: use the frontier model (Fable 5) to design detailed
goals and custom harnesses that a cheaper executor (e.g. Codex) works within; invoke
frontier models with short prompts, differentiated net-new context, and deliberately
preserved degrees of freedom — over-constraining to a linear procedure wastes exactly the
capability being paid for.

Operational specifics: the first-party trigger word is "ultracode" (guaranteeing
workflow creation; natural prompting also works), while the digest reported the bare
keyword "workflow" — which misfires when the word appears in ordinary prose, a
trigger-design flaw worth noting; token cost can be capped in the prompt ("use only
10,000 tokens"); and it composes with `/loop` (recurring runs) and `/goal` (hard
completion requirements). Anthropic's own adoption bar: "parallelism and specialization
have to earn their coordination cost" — most traditional coding tasks do not need a
panel of five reviewers.

## Why It Matters for Us

This is now vendor-shipped convergence on the engine's own thesis: the valuable
design-time artifact is the harness/governance layer, with execution delegated downward
(agentic-OS direction; DD-108 supervised autonomy). It feeds two concrete surfaces: the
model-capability registry's Fable 5 row (harness-design as a named strength) and the
eventual `/design-harness` skill — whose product is precisely what this pattern says the
strongest model should produce. The six composition patterns Anthropic says the model
uses when authoring harnesses are extracted separately
(`harness-composition-six-pattern-taxonomy.md`) — that taxonomy is direct substrate for a
schematic library.

Corroboration signal: the 2026-07-12 link-intake triage identified this as an emerging
hub finding — three new sources in a single batch extend it (this runtime-authoring
digest, plus war-gamed executor-tailored plans and frontier-designs/cheap-executes
material in adjacent lanes). Flagged as a /reassess-priorities candidate; priority is
deliberately left at P3 here.

## Strategy tier — the harness flywheel (Nate B Jones, 2026-06-17)

A second Jones source adds the vendor-strategy reading of the same pattern: the
frontier labs' implicit bet is not only that models improve, but that **better models
let them ship and evolve the harness faster** — "if the model can help you ship the
harness and test the harness and refactor the harness and observe the harness...
capability gain is going to start to compound": better agents build better harnesses,
better harnesses make agents touch more real work, more real work pressures the
harness to improve again. He names exactly two teams executing this well (Anthropic
with Claude Code, OpenAI with Codex) and reads Codex's surface (terminal, desktop,
IDE, browser, computer use, plugins, memory, automations, approvals, sandboxing,
logs) as a continuously maintained workbench, not a chatbox. Consequence for
harness-owners: the self-designing loop this finding describes is also the reason
custom harness depth is a maintenance-ownership decision (see
`harness-depth-as-maintenance-ownership.md`).

## Caveats

The primary Anthropic post was ingested 2026-07-12 (session 136), confirming the
digest's claims and adding the Bun case study — the earlier secondhand-evidence cap no
longer applies. Remaining caveats: the vendor is describing its own capability, so
external replication of the non-coding examples is still thin; cost is the recurring
warning — runtime-authored multi-agent harnesses use significantly more tokens, and
pattern selection should be justified by the task's failure modes, not available
compute. The digest-reported keyword-trigger misfire suggests the invocation surface is
still maturing.
