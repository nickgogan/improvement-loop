---
name: "Agent-as-Folder Compiled to a Single Manifest (No Explicit Wiring)"
summary: |-
  Plain English: instead of writing code that imports and wires together an agent's
  system prompt, tools, sub-agents, and integrations, you just drop files into named
  subfolders — the framework discovers everything itself at build/deploy time and
  stitches it into one manifest, with nothing in the agent's entry-point file
  referencing the pieces it's made of. Vercel's Eve frames an AI agent as literally
  "just a folder": instructions (system prompt), agent definition (model/config),
  skills, tools, sandbox (code execution), channels (Slack/Discord), connections (MCP
  servers), sub-agents, and schedules each live in their own named subfolder under one
  parent folder. A compile step traverses the folder at build/deploy time, discovers
  every piece, and produces a single manifest with all connections resolved — "you
  don't have to import or link anything together yourself." The entry-point file
  (agent.ts) never references any of it directly.
implementation_notes: |-
  Directly relevant to the engine's asset-description-language design work: Eve
  resolves "how do the parts of a multi-file agentic artifact stay wired to their
  assembly without hand-maintained imports" via folder-convention + compile-time
  discovery — one clean answer among alternatives already in this KB (explicit wiring
  rows in machine-readable-system-contract-with-wiring-rows.md; named-registry
  references in declarative-agent-spec-with-serialization-registry.md). The engine's
  own agents/{name}/ directory structure (DD-82/DD-86) is a structurally similar
  folder-per-agent pattern already in internal use — it is NOT itself a KB finding,
  but it means the engine has first-hand experience with the folder-as-agent shape to
  compare against Eve's specific choice to make wiring fully implicit (vs. the
  engine's more explicit skill/agent registration). Worth a deliberate compare-and-
  contrast pass before the asset-description-language design settles on an
  explicit-vs-implicit-wiring stance: Eve is evidence for the implicit end of that
  spectrum, the wiring-canon finding is evidence for the explicit end, and the design
  should pick a position with eyes open rather than default to either.
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
  - "IL (asset-description-language design)"
adopted_in: []
sources:
  - "vercel-eve-file-system-agent-framework.md"
related_findings:
  - file: "aios-architecture-folder-per-role-agent.md"
    rel: "same-problem"
  - file: "declarative-agent-spec-with-serialization-registry.md"
    rel: "same-problem"
  - file: "capability-as-agent-composition-primitive.md"
    rel: "same-problem"
  - file: "machine-readable-system-contract-with-wiring-rows.md"
    rel: "contradicts"
  - file: "three-layer-folder-as-workspace-architecture.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-18"
last_updated: "2026-07-18"
pipeline_status: "raw"
consumed_by: []
tags:
  - "agent-design"
  - "agent-composition"
  - "declarative-config"
  - "folder-convention"
  - "vercel"
  - "eve"
---

# Agent-as-Folder Compiled to a Single Manifest (No Explicit Wiring)

## What It Is

Vercel's Eve (open-source, TypeScript, `github.com/vercel/eve`) structures an entire AI
agent as one parent folder containing a fixed set of named subfolders, each holding one
primitive:

- **instructions** — the system prompt / global rules
- **agent definition** — the model choice and top-level config (`agent.ts`)
- **skills** — capabilities, each a markdown file with a trigger description ("load
  this before answering any revenue, sales, or growth questions") — explicitly
  compared by the presenter to Claude Code's `skill.md`-in-a-folder auto-discovery
- **tools** — individual TypeScript files, one per operation, typed with Zod so the
  agent's function-call inputs are validated
- **sandbox** — isolated code execution
- **channels** — integrations like Slack/Discord
- **connections** — MCP servers
- **sub-agents** — dispatched for token-heavy work (e.g., an "investigator" subagent
  handling "why did this metric change" questions)
- **schedules** — recurring/autonomous runs

The minimum viable agent is just `agent.ts` specifying a model plus an
`ANTHROPIC_API_KEY` env var; every other folder is optional and additive. When the
agent is run locally (`eve` command) or deployed, a **compilation step** traverses the
folder, finds everything (skills, MCP servers, tools, etc.), and produces a single
compiled manifest with all connections resolved. The main TypeScript entry file never
imports or calls out any of the other folders — "there's nothing that has to import or
call out the specific things that we have in all of the other folders." Adding a
capability means dropping a file in the matching folder; nothing else in the codebase
changes. A companion coding-agent plugin (Vercel's plugin for Claude Code/Cursor,
installed via one command) bundles a "Vercel Eve" skill plus a Vercel MCP server, so the
*coding agent* — not the human — carries the folder-convention knowledge; a prompt as
short as "Scaffold a new Eve agent called hello agent" is sufficient to bootstrap a
compliant structure, and "Deploy this Eve agent" triggers the MCP server to build,
deploy, and run an automatic smoke test.

The presenter explicitly frames Eve as an attempted **standard** for file-system-based
agents (in the spirit of MCP/A2A), paired conceptually with OKF (Open Knowledge Format)
as a complementary standard for the knowledge-base side — with an explicit scope
boundary: Eve compiles the agent's core primitives (skills, tools, MCP connections,
sub-agents), not markdown knowledge bases, which the presenter has separately argued
don't scale past tens of thousands of documents.

## Why It Matters

This removes wiring code as a category: capability inclusion becomes structural
(a file exists in the right folder) rather than declared (an import statement or
registry entry that can drift out of sync with what it references). It also collapses a
trade-off the presenter names directly — file-system-based agents have historically been
the easy-to-build, personal/second-brain kind, not the production-grade,
thousands-of-users kind — by adding durable sessions, sandboxing, human-in-the-loop
approval, an evals gate, and Vercel-scale hosting on top of the same folder convention
(see the companion findings on durable sessions and evals-as-gate extracted from this
same source). For the engine, this is a concrete, verified (3,853-star, active) industry
data point on one specific answer to "how should the parts of a multi-file agentic
artifact stay assembled without hand-maintained wiring" — directly grounding the
asset-description-language design question the engine is working through.

## Why People Are Using It

The presenter (Cole Medin) notes he is "seeing a lot of organizations build this kind of
thing for themselves internally" already — ad hoc folder conventions for agent + model +
skills + system prompt — and frames Eve as offering a shared standard instead of every
org reinventing one. Backed by Vercel's hosting/scaling infrastructure and a coding-agent
plugin that lowers the barrier to *correct* usage. The upstream repo is independently
verifiable (github.com/vercel/eve, "The Framework for Building Agents," 3,853 stars,
active) — a real adoption signal beyond the sponsored review itself, though no
third-party production deployment is demonstrated in this source; the demo shown is the
presenter's own single "Eve analyst" agent talking to a data warehouse and to Slack.

## Potential Alternatives

- **Declarative AgentSpec with a serialization-name registry** (`declarative-agent-spec-
  with-serialization-registry.md`) — an explicit YAML/JSON spec references capabilities
  by a stable registered name; still zero hand-written import code, but every part must
  be named in the spec, unlike Eve's fully implicit folder-presence-is-inclusion model.
- **Machine-readable system contract with wiring rows**
  (`machine-readable-system-contract-with-wiring-rows.md`) — the opposite design stance:
  wiring is explicitly declared, versioned, and hash-checked for drift, trading
  convention-magic for auditability and per-row invariants. Directly contradicts Eve's
  implicit-discovery approach on the same underlying question.
- **Folder-per-role multi-agent org structure** (`aios-architecture-folder-per-role-
  agent.md`) — folders organize *many* agents (one per department/role) rather than the
  *parts of one* agent; same folder-as-structure instinct, different granularity.
- **Hand-wired code** (traditional agent frameworks) — full control and explicit
  traceability, at the cost of a code change at the wiring site for every new
  capability.

## Potential Improvements

- No visibility into the compiled manifest itself is shown in the source — a
  manifest-inspect/diff tool for debugging "why wasn't my skill picked up" would be a
  natural next step.
- No drift detection between folder source and compiled manifest is mentioned (contrast
  with this KB's own `manifest-hash-drift-detection-for-derived-docs.md` pattern) —
  worth watching for as the framework matures.
- Cross-framework portability: the folder convention is currently Eve/Vercel-specific; a
  shared spec (the presenter's own Eve+OKF pairing speculation) could let the same
  folder compile to multiple target runtimes.

## Potential Failure Modes

- **Convention debt at scale** — once dozens of skills/tools/subagents accumulate
  across folders, "just drop a file in" loses the legibility it started with (no
  central manifest to read without running the compiler); the same failure mode is
  already flagged in this KB for folder-as-structure patterns generally
  (`three-layer-folder-as-workspace-architecture.md`: "CLAUDE.md proliferation...
  navigation overhead"; `aios-architecture-folder-per-role-agent.md`: "navigation and
  maintenance become non-trivial").
- **Silent misplacement** — implicit wiring means a naming collision or a file dropped
  in the wrong folder has no described compiler-error surface in this source; contrast
  with the explicit wiring-row model, which trades convenience for exactly this
  guarantee.
- **Framework/platform lock-in** — the compile step and hosting model are
  Vercel-specific; the "standard" is presently a single vendor's implementation.
- **Sponsorship-calibrated evidence** — this is a launch demo by a paid partner (Vercel
  disclosed); no independent third-party production deployment is shown, only the
  presenter's own demo agent and Vercel's own infrastructure claims.
