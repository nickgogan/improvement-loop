---
type: "link-intake-triage-report"
topic: >-
  Wave-3 triage (session 144) over the cached 28-video batch — the 20-video
  retry backlog plus 9 Nick-added links (1 in-batch dup), all transcripts
  pre-cached in sessions 142-143 via the kome.ai fallback lane. KB-fit +
  roster-escalation verdicts per link.
date: "2026-07-13"
protocol_spec: ".claude/skills/link-intake/SKILL.md"
input: >-
  Wave-3 queue recovered from git (724bb52^:systems/improvement-loop/LINKS.md):
  29 URLs, 28 unique video IDs after in-batch dedup; LINKS.md itself already
  empty (cleared at session-143 close when the cache completed)
verdict_set: ["ADD", "ENHANCE", "KB-ONLY", "REJECT"]
---

# Link-Intake Triage Report — 2026-07-13 (wave-3, fourth run)

Triage of the wave-3 batch: all 28 transcripts were already on disk (fetched sessions
142–143), so this run had zero fetch cost. Four topical triage subagents (read-only),
one verdict per link, dedup against the live findings/sources corpus. **This report
changes nothing by itself** — every routing is separately Nick-gated.

**Tally: 0 ADD · 0 ENHANCE · 10 KB-ONLY · 18 REJECT · 0 defer.** Of the REJECTs, 2 are
already-ingested KB sources and 16 are content rejections (11 dedup kills, 5
relevance/no-measurement kills). ~34 novel patterns estimated across the 10 KB-ONLY
sources; ~48k transcript tokens for the Pass 2 extraction session.

## Batch mechanics

- **Queue recovery:** LINKS.md was cleared at session-143 close, so the wave-3 list was
  recovered from git (`724bb52^`): 29 URLs → 28 unique IDs (in-batch dup:
  `Q-3fgVdmuVw` ×2).
- **Cache check:** 28/28 transcripts present in `app/transcript-fetcher/transcripts/`;
  no fetches, no probe burst, no rate-limit exposure this run.
- **KB dedup (pre-fan-out):** 2 hits via URL/ID grep over `research-sources/`, both
  `status: Done` → auto-REJECT:
  - `iQyg-KypKAA` → `research-sources/l8-principals-agentic-engineering-workflow.md`
  - `HRw-vP0j8OM` → `research-sources/the-agentic-os-setup-that-will-10x-claude-code.md`
- **Fan-out:** 26 links in 4 topical batches — A: CC setups & agentic-OS tooling (7);
  B: agent architecture, memory & frameworks (7); C: model/tool comparisons & ecosystem
  news (6); D: agent-building strategy & workflow meta (6). All four returned
  well-formed verdicts; no re-dispatch needed. No escalation triggers fired (no fetch
  failures, no contradictory dedup evidence, no conflicting verdicts).

## Verdict summary

### KB-ONLY (10)

| ID | Title (channel) | Intake path | Novel patterns |
|---|---|---|---|
| PRqiGS6fnIM | 1.6M agents registered for OpenClaw and did NOTHING (Nate B Jones) | research-source | 3 |
| xqGCbEDbny8 | Codex: Your First Personal AI Agent Delegation Loop (Nate B Jones) | research-source | 3 |
| BOXK2XFLA-E | Don't build more AI agents until you watch this (Nate B Jones) | research-source | 5 |
| 9CiOwbmOKdU | I Rebuilt Hermes's Best Feature in Claude Code (Simon Scrapes) | research-source | 5 |
| c8QiXuUMZCI | The INSANE Engineering Behind REPLIT Agents (Akhil Sharma) | research-source | 5 |
| PY7xIxybYNc | Pydantic AI 2.0: Composing Capabilities (Cole Medin) | research-source | 4 |
| NE0aBuQF0HA | Introducing /visual-plan (Steve, Builder.io) | research-source | 4 |
| 1njjOIiA8Kc | GPT 5.6 vs Fable 5 Build the Same App (Pat Simmons) | research-source | 3 |
| 7HwhLOPeYh8 | What workflow should you get your AI agent to do? (Vicky Zhao) | research-source (borderline-thin) | 1 |
| Gq0l4IYRIIU | This New n8n Tool (Chase AI) | watched-library changelog note via /watch-upstream | 1 |

### REJECT (18)

| ID | Title (channel) | Reason |
|---|---|---|
| iQyg-KypKAA | L8 Principal's Agentic Engineering Workflow (Kun Chen) | already in KB (Done) |
| HRw-vP0j8OM | The Agentic OS Setup That Will 10x Claude Code (Chase AI) | already in KB (Done) |
| Q-3fgVdmuVw | Ultimate Guide to Building 10x Faster (Austin Marchese) | covered by his 2 processed deep-dives |
| PW0sgog3kXY | Fable 5 Agentic OS "Jarvis" (Chase AI) | covered by processed agentic-OS synthesis |
| glAoiBWVkmU | CC + Obsidian Setup (Chase AI) | older iteration of processed synthesis; recency rule |
| IShdbDP4Jgg | Top 10 CC Plugins (Chase AI) | listicle, no measurement; items all covered |
| r5iBG1s_MDk | 4 Loops (Dream Labs AI) | secondhand re-explanation of processed loop-engineering material |
| PxuMqeIqCEo | AI Agent Memory Masterclass (The Carbon Layer) | covered by memory-cluster findings + IB-176 design §1 |
| n32qq7Kwzh0 | Hermes Architecture EXPLAINED (Hugging Face) | covered by hermes-agent watched-library analysis (deeper) |
| 4JBp4Wp36Lw | Ontologies, World Models, Company Brains (Devin Kearns) | commentary, no experiment; world-model cluster covers it |
| deeOA6YVfqw | CC Video Generation with Archon (Cole Medin) | covered by archon registry + Ralph-loop findings; drift flag below |
| jOK10k70XWE | OpenClaw vs Hermes (Metics Media) | consumer buying guide; covered by Hermes/OpenClaw findings |
| R2-Y1Hjwx2U | Stop Picking Between CC and Codex (Nate B Jones) | ergonomics opinion, zero measurement; covered by his processed corpus |
| eozCDUxwU8k | Best Local AI Hardware (Cloud Codes) | vendor-quoted numbers secondhand; no engine decision turns on it |
| OSJJYWaxkKQ | Stop Using AI For This (Kyle Cook) | opinion without measurement; KB holds position in stronger form |
| Rl7rvHbDqGk | I Stopped Building AI Agents (Dan Harrison) | derivative of tracked authority (Jake Van Clief); no numbers |
| EuzYhzB0vbI | Agent Loops Clearly Explained (Nate Herk) | covered by newer loop-engineering synthesis |
| Pi-m8R068r4 | The AI Offer You Can Sell Tomorrow (Nate Herk) | sell-AI-services GTM content; no transferable pattern |

## Per-link rationales — KB-ONLY

### PRqiGS6fnIM — 1.6M agents registered for OpenClaw and did NOTHING (Nate B Jones, 28:04)

Strongest item in batch C; directly feeds the pending named-deps gap-check (the "Nate B
Jones" ask). Gives a *measured* basis for the engine's routine chat-vs-subagent-vs-fan-out
routing decision: Stanford repeated-sampling numbers (15.9% → 56% solve rate at 250
attempts; ~95% coverage at 10k but selection without a mechanical verifier stalls at
~100 attempts) plus Anthropic production data (token spend explains 80% of run-quality
variance). Ran his own three tasks on camera incl. ~10x Fable-5 cost reduction via
plan/judge-expensive + work-cheap split. Novel: (1) repeated-sampling scaling law +
verifier ceiling — evals are the binding constraint on multi-agent scale; (2)
four-estimate agent test (size / independence / separation-of-concerns / checkability) →
routing verdict chat / single agent / team / human; (3) two-constraint decomposition
theory (split for memory vs split for eval; "fresh eyes on demand"). Partial dedup:
`anthropic-multi-agent-research-system` (90.2% figure), receipt-artifact finding. Roster:
no — the four-question test is rule/pattern-shaped; flag for the Phase 4 interview and
IB-176, don't mint a mechanism from one source.

### xqGCbEDbny8 — Codex: Your First Personal AI Agent Delegation Loop (Nate B Jones, 19:36)

Second half of the Jones gap-check; lands on IB-176 and the queued Phase 4 agent-vs-skill
interview. Measured: his own year-long token-burn curve (510M tokens peak day,
300–500M/day sustained; inflection attributed to computer-use + model 5.5) as a
quantified receipt that the unit of delegated work changed. Novel: (1) chief-of-staff
home-base thread — one persistent thread owns goal/folders/standard and routes sub-jobs,
eliminating human-as-router; (2) planning-thread vs execution-thread separation, each
with its own subagents; (3) token-burn telemetry as delegation-adoption metric. The
five-element assignment contract is corroboration — his newer work-ticket video (already
in KB) leads per recency. His corrections→skill compounding test ("same correction twice
→ promote") routes as IB-176 design input, not a roster item.

### BOXK2XFLA-E — Don't build more AI agents until you watch this (Nate B Jones, 18:25)

Anchors the Jones gap-check on the harness-maintenance side: agents break when the world
drifts AND when the model inside improves, so harnesses need scheduled fitness reviews —
exactly the trigger the engine's model-capability-registry refresh half-embodies. Passes
the measured bar on the Vercel case (deleted 80% of the agent's tools, agent improved).
Novel: (1) bidirectional agent breakage (over-restriction traps better models); (2) tool
pruning as maintenance discipline; (3) five-point agent health checklist (inputs current
/ reach fits model / job drifted / proof linkable / value real); (4) harness-depth =
maintenance-ownership tradeoff; (5) build from the observed workflow, not the paper
workflow. Extends `frontier-model-as-harness-designer`. Roster: no ADD on one source;
the checklist is a natural future ENHANCE delta for `/system-health` or the registry
refresh procedure if the pattern recurs.

### 9CiOwbmOKdU — I Rebuilt Hermes's Best Feature in Claude Code (Simon Scrapes, 14:42)

Highest-value link in batch B and the newest memory-cluster source (its framing leads).
A practitioner rebuilds Hermes-grade memory inside Claude Code as portable local
markdown — the engine's exact stack — and corroborates the ruled IB-176 design
point-for-point: post-turn hook capture, size-capped curated snapshot (2,500-char
memory.md) separate from append-only transcripts, files-over-runtime portability, and
Hermes' self-rewrite failure mode as evidence for gated promotion + generator-assessor
separation. Its session-history import as day-one memory bootstrap independently
validates the SL distill-then-close plan. Decision-relevant number: 1,300 Reddit
comments analyzed, ~30% of Hermes switchers citing memory defaults. Novel: (1)
storage/injection/recall triad as memory-system evaluation rubric; (2) session-history
import as memory bootstrap; (3) recall ladder (hybrid semantic+keyword, rerank, expand
to neighboring context, cite source transcript, say-don't-know); (4) post-turn promotion
hook into a hard-capped snapshot with user-editable promotion rules; (5) asker-scoped
team memory — a multi-tenant-gap datapoint. Also strengthens the Simon Scrapes Tier-2
authority entry.

### c8QiXuUMZCI — The INSANE Engineering Behind REPLIT Agents (Akhil Sharma, 23:49)

The reversibility stack is not in the corpus: existing sandbox findings compare isolation
runtimes, nothing covers Replit's three-layer reversible-state design.
Reversibility-as-enabler-of-autonomy is the infrastructure generalization of Claude Code
checkpoints and speaks to the harness-layer North Star; the memory-design's
shadow-sandbox step is a miniature of the same principle. Secondhand teardown — mark
evidence medium, verify against Replit primaries before citing as strong. Novel: (1)
three-layer reversible state, one undo surface (copy-on-write FS snapshots / automatic
background git + immutable backup remote / forkable Postgres branches); (2) reversibility
enables parallel sampling (cheap forks, discard losers); (3) borrow-the-strongest-
isolation-boundary tenancy (one GCP project per customer); (4) give the agent the human
tool surface — custom agent-only primitives fight the training distribution; (5)
capability-tax framing (every powerful capability is an operational cost paid forever).

### PY7xIxybYNc — Pydantic AI 2.0: Composing Capabilities (Cole Medin, 15:00)

The industry converging on the engine's own harness-layer vocabulary: Pydantic AI 2.0
ships a "capability" primitive (instructions + tools + lifecycle hooks + guardrails +
model settings in one shareable unit — "the layer above MCP") and splits the framework
into a lean core vs a named "harness" lane. A datapoint for the portable-kernel /
single-implicit-agent design. Pydantic AI is not currently a watched library. Novel: (1)
capability as the single agent-composition primitive; (2) lean-core vs harness two-lane
framework layering; (3) progressive disclosure at capability level (catalog of brief
descriptions, full instructions on demand); (4) Monty — Pydantic's lightweight
open-source sandbox (watched-library candidate in its own right). Optional follow-up
(Nick's call): add `pydantic/pydantic-ai` to watched-libraries + `/repo-analyzer`.

### NE0aBuQF0HA — Introducing /visual-plan (Steve, Builder.io, 4:26)

Directly on the North Star's plan-artifact axis and names a problem Nick has personally
flagged: prose-heavy plans/DDs make human gating expensive. Answer: render plans as MDX
with reusable interactive components (wireframes, diagrams, commentable API specs) so
review happens at the plan level — plans as the abstraction layer engineers reason at;
plus a post-execution "visual recap" mirror artifact that catches "that's not what I
meant" cheaply. Open source (skills + CLI + GitHub action), from an existing KB
authority (builder-io). Best pattern-density-per-minute in the run. Novel: (1)
plan-as-reasoning-abstraction-level; (2) MDX-with-reusable-components over freeform
"HTML slop"; (3) visual recap; (4) plan/recap as CI artifact on every PR. Roster: no ADD
now — adopting an MDX toolchain on first occurrence fails abstractions-earn-their-keep —
but this is the strongest input yet for the parked governance-visualization session
(IB-175); the source should be in the KB before that session runs.

### 1njjOIiA8Kc — GPT 5.6 vs Fable 5 Build the Same App (Pat Simmons, 26:26)

Fills an explicit hole: the model-capability registry's GPT-5.6 line has no KB grounding,
and registry claims must be KB-grounded, never invented. Real quantified head-to-head:
same one-shot prompt, three builds, deployed live, wall-clock + cost per run (e.g.
Shots.so clone: Fable 30 min/$12 vs 5.6 Soul 2h51m/~$100; NYC platform: Fable ~20
min/$95 vs 5.6 ~$11). Qualitative winner 5.6 Soul on thoroughness/design
fidelity/instruction-following. Caveats: n=1 per task, buggy subscription cost readouts
(he flags his own numbers) — file as Anecdotal/Medium, "one practitioner head-to-head,"
not a benchmark. Novel: (1) 5.6 Soul capability profile (thoroughness at 3–6× wall-clock;
follows staged gates literally); (2) Fable one-shot pixel-fidelity weakness despite speed;
(3) harness cost-observability bug pattern — use independent log-based accounting
(`ccusage`) for any cost claim.

### 7HwhLOPeYh8 — What workflow should you get your AI agent to do? (Vicky Zhao, 8:06)

**Borderline — flagged honestly as thin; Nick may reasonably kill it.** One clean
procedure: pick delegation targets by (1) what you're avoiding (procrastination as
high-leverage signal, counter to the "morning brief" default), (2) what you'd hire for
(playbook-onboardable = agent-onboardable), (3) what moves the North Star. A ready-made
selection rubric for the Phase 4 agent-vs-skill interview. No quantified experiment, but
it's instructional procedure-defining content, not news commentary. 1 novel pattern.

### Gq0l4IYRIIU — This New n8n Tool (Chase AI, 10:15)

n8n is a formally watched library (last evaluated v2.16.0, April) and this documents a
real upstream change: an official instance-level MCP server built for coding agents.
Consumption mode is a watched-library changelog note routed through `/watch-upstream`,
not a full source extraction. 1 transferable pattern: typed-IR compile gate — the model
authors workflow config as TypeScript that must type-check and compile before conversion
and deploy, filtering structural errors pre-instantiation (generalizes our pre-commit
frontmatter validation).

## Per-link rationales — REJECT

Condensed; dedup evidence paths were verified live by the triage subagents.

- **iQyg-KypKAA / HRw-vP0j8OM** — already fully processed KB sources (`status: Done`);
  caught pre-fan-out by URL grep.
- **Q-3fgVdmuVw** (Austin Marchese) — self-repackage of his two processed deep-dives;
  all load-bearing mechanisms (session-history mining, three-bucket tiering,
  distribution-as-floor-raising, improve-system loop) already extracted.
- **PW0sgog3kXY** (Chase AI) — the "Jarvis" instance of the processed four-level
  agentic-OS construct; voice stack irrelevant to a markdown engine; 3-tier intent
  routing corroborates `smart-model-routing-catch-22`.
- **glAoiBWVkmU** (Chase AI) — older iteration of the processed June-25 synthesis;
  recency rule; only plugin trivia remains.
- **IShdbDP4Jgg** (Chase AI) — listicle without measurement; each non-trivial item
  already covered (cross-model verification, NotebookLM cluster, claudemd-as-traversal-
  guide, progress-md-session-bridge).
- **r5iBG1s_MDk** (Dream Labs AI) — secondhand re-explanation of the Anthropic
  loop-engineering material the KB already synthesized more rigorously; if primary
  grounding is wanted, ingest the Anthropic article itself.
- **PxuMqeIqCEo** (The Carbon Layer) — well-taught recap of ground the engine already
  ruled on in the IB-176 design; corroborates, contradicts nothing, no experiment;
  9CiOwbmOKdU is the newer cluster leader.
- **n32qq7Kwzh0** (Hugging Face) — re-walkthrough of an already-tracked repo whose KB
  analysis goes deeper; marginal deltas trivia-grade.
- **4JBp4Wp36Lw** (Devin Kearns) — ontology/world-model trend monologue, no experiment;
  world-model cluster + Karpathy sources cover it; abstention-layer delta too thin.
- **deeOA6YVfqw** (Cole Medin) — sponsored demo applying tracked Archon primitives;
  every structural pattern in corpus. **Carries the Archon drift flag (follow-up 2).**
- **jOK10k70XWE** (Metics Media) — consumer buying guide with secondhand aggregates and
  affiliate links; curator-vs-approval-gated framing already in KB.
- **R2-Y1Hjwx2U** (Nate B Jones) — interface-ergonomics commentary, zero measurement;
  receipts point already extracted from his Open Engine video; superseded within-cluster
  by PRqiGS6fnIM.
- **eozCDUxwU8k** (Cloud Codes) — vendor-quoted hardware numbers relayed secondhand (the
  channel's recorded failure mode); no engine decision turns on local-inference hardware.
- **OSJJYWaxkKQ** (Kyle Cook) — opinion without measurement; the KB holds his core
  argument in three stronger findings (code-as-deterministic-tool, CLI-first,
  planner-executor guardrails).
- **Rl7rvHbDqGk** (Dan Harrison) — 3-folder scheme adapted (by his own statement) from
  tracked authority Jake Van Clief; motivational content; "way less token spend" with
  zero numbers.
- **EuzYhzB0vbI** (Nate Herk) — the KB's loop-engineering synthesis (published a week
  later) carries everything load-bearing; caps/stop-rules already findings.
- **Pi-m8R068r4** (Nate Herk) — GTM ladder for AI consultants + sponsor read; priorities
  rank sell-AI-services content LOW absent transferable patterns; none present.

## Blocked / defer

None — all 28 transcripts were cached before this run; no fetches attempted.

## Follow-up queue (each item separately Nick-gated)

1. **Pass 2 extraction** of the 10 KB-ONLY sources via `/research-loop` (~48k transcript
   tokens; 9 full source entries + 1 watched-library changelog note).
2. **Archon watched-library refresh** — deeOA6YVfqw evidences upstream drift (workflow
   UI/log viewer, first-class Ralph loops, ~23k stars) vs registry
   `last_evaluated_version: v0.3.2 (2026-04-09)`. Run `/watch-upstream` or
   `/repo-analyzer` on Archon **before** the named-deps gap-check that names it.
3. **Pydantic AI watched-library candidate** — add `pydantic/pydantic-ai` (+ note Monty
   sandbox) if Nick wants dependency-grade tracking of the capability primitive.
4. **n8n registry changelog note** — instance-level MCP + typed-IR compile gate, via
   `/watch-upstream`.
5. **Authority-registry updates at Pass 2 filing time:** Pat Simmons — new Tier-3
   candidate (practitioner-experimenter); Nate B Jones — add "harness maintenance +
   delegation loops" specialty note (4/6 keep rate this run, trending above tier on that
   lane); Nate Herk — scope note "strong on first-hand system walkthroughs, weak on
   explainers/sales" (0/2 this run); Chase AI — add triage-priority note "dedup against
   his own corpus before fetching; only newest synthesis per construct" (1 thin keep /
   5 incl. the already-ingested reject); Austin Marchese — "process topic-specific
   deep-dives, skip guide/roadmap formats"; Simon Scrapes — bump source count, add
   memory specialty. No new entries for Dream Labs AI, Metics Media, Dan Harrison, Kyle
   Cook, The Carbon Layer, Devin Kearns; Vicky Zhao held until recurrence
   (tolerate-one-off rule).
6. **Phase 4 interview inputs** (no action now, note for the interview file): Jones
   four-estimate agent test + two-constraint decomposition; Zhao three-question
   workflow-selection rubric; Jones corrections→skill compounding test → IB-176.
7. **Governance-visualization session (IB-175) input:** the /visual-plan source is the
   strongest input yet — extract before that session runs.

## Gate outcome

Nick accepted all verdicts 2026-07-13 (same session). Notes from the gate:

- **Vicky Zhao keep affirmed, with an upgraded rationale:** the value is not the rubric
  itself but **seam identification** — the Librarian should be able to help an operator
  see which parts of a potential workflow belong to the *human* and not to the AI or the
  AI system. Extract the finding with that framing (a Librarian advisory capability +
  Phase 4 interview input), not merely as a workflow-selection checklist.
- **Archon `/watch-upstream` refresh greenlit** (before the named-deps gap-check).
- LINKS.md clearance: no-op — file already empty since session-143 close.

## Protocol observations

- **Cache-first wave shape worked.** Splitting fetch (sessions 142–143) from triage
  (this run) meant zero rate-limit exposure and a pure-read triage session. Worth keeping
  when a batch needs the fallback fetch lane anyway.
- **Queue recovery from git.** Clearing LINKS.md at cache-completion (session 143) left
  this run without an on-disk queue; recovering from `724bb52^` worked but was an extra
  step. Minor: when transcripts are prefetched ahead of triage, keep the link list in
  LINKS.md until triage acceptance (the skill's own clearance rule) — deviation noted,
  no harm done since the report now carries the full list.
- **Channel-corpus dedup is doing real work.** 11 of 16 content rejections were dedup
  kills against the KB — heavily concentrated in channels that iterate one construct
  across many videos (Chase AI ×3, plus Marchese and Herk self-overlaps). The per-channel
  triage notes in follow-up 5 should cut future fetch cost.
- **Zero ADD/ENHANCE for the second consecutive run** — consistent with the roster
  having stabilized; roster escalation now mostly routes content into existing owners
  (`/watch-upstream`, IB-176, Phase 4 interview) rather than proposing new skills.

## Appendix — cost table

No fetches this run (28/28 cached). Transcript sizes (full-text, timestamps stripped):

| Batch | Videos | Transcript bytes | Est. tokens |
|---|---|---|---|
| A — CC setups & agentic-OS tooling | 7 | ~148k | ~37k |
| B — architecture, memory & frameworks | 7 | ~185k | ~46k |
| C — comparisons & ecosystem news | 6 | ~130k | ~33k |
| D — strategy & workflow meta | 6 | ~137k | ~34k |
| Pre-fan-out rejects (2, not re-read) | 2 | — | — |
| **Total** | **28** | **~600k** | **~150k** |

KB-ONLY subset headed to Pass 2: ~191k bytes ≈ ~48k transcript tokens.
Subagent cost this run: 4 triage agents, ~443k tokens total.
