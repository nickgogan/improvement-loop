---
type: "link-intake-triage-report"
topic: >-
  Third protocol run (session 135) over the full parked LINKS.md batch —
  86 URLs, all YouTube, 83 unique videos; full-sweep pre-approved by Nick
  2026-07-12. KB-fit + roster-escalation verdicts per link.
date: "2026-07-12"
protocol_spec: "operations/references/link-intake-protocol.md"
input: >-
  systems/improvement-loop/LINKS.md (86 lines, 83 unique video IDs after
  in-batch dedup; hold lifted 2026-07-12)
verdict_set: ["ADD", "ENHANCE", "KB-ONLY", "REJECT"]
---

# Link-Intake Triage Report — 2026-07-12 (third protocol run)

Full sweep of the parked all-video LINKS.md batch, pre-approved by Nick. Eight topical
triage subagents (KB track with per-video roster escalation), one verdict per link, dedup
against the live findings/sources corpus. **This report changes nothing by itself** —
every routing is separately Nick-gated; LINKS.md is cleared only after verdicts are accepted.

**Tally: 0 ADD · 0 ENHANCE · 28 KB-ONLY · 55 REJECT** (of the REJECTs, 20 are
"defer — transcript blocked" and form the retry backlog; 33 are content rejections; 2 are
already-ingested KB sources). ~97 novel patterns estimated across the 28 KB-ONLY sources,
~107k transcript tokens for the Pass 2 extraction session.

## Batch mechanics

- **Probe/dedup:** 86 lines → 83 unique videos (3 in-batch duplicates: `47oi3Q9apK0`,
  `lw6Ld1ZgpV8`, `UztrFXaSWv0`). 63 transcripts already cached from the session-133
  background fetch; 2 videos already fully ingested in the KB (caught by `research-sources/`
  URL grep); 20 needed fetching.
- **Fetch outcome:** 0 of the 20 recovered. YouTube returned a hard IP-level HTTP 429 on the
  subtitle endpoint — the 83-video probe plus fetch burst tripped the throttle. Chain
  exhausted this session: api (IpBlocked) → playwright (no segments) → ytdlp (429) →
  ytdlp + Chrome cookies (429) → browser-assisted HTML (unavailable — Chrome extension not
  connected). The 429 is temporal; a plain re-run next session should succeed. None of the 20
  have research-source entries yet, so per the Blocked convention they are listed in the
  Blocked section below rather than flagged in frontmatter.
- **Cost table** (all 83 unique): 23:30:01 total runtime, ~310k estimated transcript tokens.
  Full per-video table in the appendix. Pass-2-relevant subset (the 28 KB-ONLY): ~107k tokens.

## Verdict summary

### KB-ONLY (28) — route: research-source entry + `/research-loop` Pass 2

| ID | Title | Channel | Est. patterns |
|---|---|---|---|
| VHKXIHP4i10 | Google OKF vs RAG Confusion, Finally Cleared Up | Cloud Codes | 5 |
| _X55fkwdC-Q | Google OKF + RAG: The Ultimate AI Agent Architecture | Cloud Codes | 4 |
| T33iI6izAKw | Open Standard for the Karpathy LLM Wiki | Cole Medin | 5 |
| DTCyvo6cC54 | Every Level of a Claude Second Brain Explained | Nate Herk | 4 |
| -fSjdYzrFvA | Give Your AI Agent a Second Brain (Gbrain + Hermes) | Tonbi's AI Garage | 4 |
| RQckIBzOCsA | The Folder Structure That Makes AI Build Better Software | AI Code That Works | 3 |
| HRw-vP0j8OM | The Agentic OS Setup That Will 10x Claude Code | Chase AI | 2 |
| l5rae4LMKBc | Claude Can Now Build Its Own Harness | Prompt Engineering | 5 |
| MYPLpkENs7A | AI Gateway: The Layer Every AI Stack Eventually Needs | Devsplainers | 5 |
| rh_PcL26zls | You Can't Run AI Agents Without This | Nate B Jones | 4 |
| UNzCG3lw6O0 | Building Great Agent Skills: The Missing Manual | AI Engineer (Matt Pocock) | 5 |
| A8mokin_YOs | New Skills v1.1 (/wayfinder, /research, …) | Matt Pocock | 5 |
| HGCHgD4uGgY | 8 Claude Loops to Build 10x Faster | Austin Marchese | 3 |
| 8wsM0euQOvc | 5 Insane Claude Loops | AI LABS | 4 |
| DQq-z4wROTc | Loop Engineering Explained by Claude Code Creators | Cloud Codes | 2 |
| 2fc0NX9vIJ8 | How to Build A Self-Improving System with Claude | Austin Marchese | 2 |
| rs2fFITXd6g | You're the Problem, Not Claude (6 Fixes) | Austin Marchese | 3 |
| Zp8lr6IzUnQ | GLM 5.2 Is Free And Beats Claude On Most Work | Nate B Jones | 2 |
| 1cSNE-ZkDLQ | You Can't Compete on Cheap Models Anymore | Nate B Jones | 2 |
| nuwlyQXrADg | Do THIS Before You Lose Access to Fable 5 | Mark Kashef | 4 |
| qWhSFjDS3LA | How to Distill Claude Fable 5 | Cloud Codes | 2 |
| p8ypBeNXQ8E | Make Fable 5 80% Cheaper | Chase AI | 2 |
| U4TmrlWEY4M | I Pointed My Agent at the Bills | Nate B Jones | 4 |
| MFzxIT88zfg | I Built a Deck With AI, Then Made a Second AI Attack It | Nate B Jones | 3 |
| UvVVATGIm7k | Claude Code Cuts Token Usage by 94% | Eric Tech | 3 |
| QSK4vf_ZTRA | I Was The Only Thing Connecting Claude, ChatGPT, Codex | Nate B Jones | 3 |
| iQyg-KypKAA | L8 Principal's Agentic Engineering Workflow | Kun Chen | 5 |
| muwRbfuKbR4 | The Best AI Coding Setup Isn't the Most Autonomous One | Cole Medin | 3 |

### REJECT — content (33)

| ID | Title | One-line reason |
|---|---|---|
| 2kKkb01GxYQ | OKF: Folder Replacing Vector DBs | Covered by VHKXIHP4i10 (oldest of 4 same-channel OKF re-shoots) |
| l46NJXUL4PM | OKF + Claude: Why We Stopped Using RAG | Covered by VHKXIHP4i10 + T33iI6izAKw + existing KB |
| R-5_2nsF_ZM | Karpathy Wiki Doesn't Scale | Sponsored Redis Iris demo; multi-user production lane, not ours |
| 47oi3Q9apK0 | Definitive Guide AI Second Brain | All engine-relevant rules already in KB; rest is human Zettelkasten |
| Aded2v7_vag | Obsidian: Thinking Person's Setup | Author-declared "not for AI to read"; human PKM tutorial |
| HgAQOkG_v8c | I Built My Own AI Memory | Strategy essay; Open Brain already in KB |
| A0pdL3MS_7E | My Entire File System in 9 Minutes | PARA tour + newsletter funnel; PARA already the KB's anti-pattern baseline |
| HhWwllcbc2g | Fable Built the Ultimate Agent Harness | Build-along vlog; ADE/Hermes/OpenRouter covered; normalizes --dangerously-skip-permissions |
| HIJVMVBM4KM | When to Use Claude Agent SDK | Fully redundant with the KB's SDK-decision cluster |
| 141biWM1mlE | This Meta-Harness Changes Everything | Omnigent launch video; KB's watched-library analysis (newer HEAD) supersedes it |
| 9PUaEj0pMYE | The Skill vs Prompt Problem | "Open Skills" launch promo; concepts all in KB and engine substrate |
| d2XiTDzoizc | This Skill Instantly 10x'es Output | His "refresh skill" is functionally our /session-handoff |
| pw79ro49CzU | Anthropic Guide for Better Output | Secondhand walkthrough — ingest the primary Anthropic field guide instead (queued in follow-ups) |
| UztrFXaSWv0 | CC Creators Don't Prompt Anymore | Loop-engineering mechanics all covered; superseded by newer framing |
| ju7R6jer6_M | Stop Building AI Agents the Old Way | 7-component taxonomy is a packaging of findings the KB already holds |
| lw6Ld1ZgpV8 | I Tried /teach | Third-party demo; state-workspace covered; pedagogy off-dimension |
| Vwn19n8W-qE | Agent Loop Explained in 10 Minutes | Fundamentals explainer; every element covered |
| A4zMyjkL0Dc | Stopped Prompting One Task at a Time | Conceptual teaser; cross-loop propagation handled better by HGCHgD4uGgY |
| mn4XBSBIuag | Your $20 AI Plan Costs Them Thousands | Bubble/market analysis; zero builder procedures |
| LpXhy2iiaQE | DeepSeek's New AI Is a Game Changer | Vision-paper news; weak registry flag recorded |
| mG4SmhWyeFA | DeepSeek Solved AI's Billion Dollar Problem | Provider serving-infra optimization; not applicable to builders |
| H9oNA5IyrXA | Apple, Anthropic, OpenAI Same Move | Context-wars strategy essay; extractable residue lives in the 2 KB-ONLY econ videos |
| t7L6-fMpxFc | Apple WWDC 2026 | Consumer-platform strategy |
| 0GQ2RP-25gM | Clever Hans Horse — Computerphile | ML-explainability; the moral is already `benchmark-signal-mismatch` |
| huAwz_BR8WM | Demis Hassabis On What AI Will Do Next | Interview/forecast; verification-enables-autonomy already threaded in KB |
| J2ZE6XGCYb0 | Here we go again... | Loop-engineering rebrand commentary; all covered |
| o6O4xu1LhDU | Fable 5 Just Got Extended | Promo-cycle news; benchmark claims rumor-tier (explicitly NOT for registry) |
| lplVBFr0Ndc | Fable 5 Use Cases You Must Do NOW | Use-case listicle; frontier/cheap division already canon |
| pbrln2TVeh4 | Claude Creating Millionaires | Monetization narrative; roast-council covered by generator-assessor findings |
| Mqr2WYQEhBw | Hermes vs Claude vs OpenClaw | Consumer tour; memory-notes pattern covered |
| dk1Y3VtC3F8 | 12 Open Source AI Tools | RAG-stack listicle; no procedures, no watched-library candidates |
| luBkbzjo-TA | Principled Agentic Engineer (67 min) | PIV system already in KB via newer Archon-lineage sources by same author |
| zbmuiaPuiNM | Google Masterclass on Agentic Engineering | Same Google whitepaper as the already-processed osmani-new-sdlc source |

### REJECT — already ingested (2)

| ID | Title | Evidence |
|---|---|---|
| RtxUdvSTQGc | Free Fable 5 tokens | `research-sources/free-fable-5-tokens-heres-how-to-max-them.md` status: Done; finding extracted |
| dUmT0OIGoqE | Better Language For AI Agents | `research-sources/scientists-found-a-better-language-for-ai-agents.md` status: Done; finding extracted |

### REJECT — defer, transcript blocked (20) — the retry backlog

All failed the full available fallback chain this session (429 rate limit; browser rung
unavailable). Re-queue: re-run `fetch.py --input LINKS.md` next session after cooldown, then
triage in one wave-2 pass. Titles suggest several probable keepers (marked ★ = probe metadata
suggests on-mission density; judgment deferred until transcripts exist per the
transcript-first rule).

| ID | Title | Channel-unknown/duration | Note |
|---|---|---|---|
| PxuMqeIqCEo | AI Agent Memory Masterclass | 27:18 | ★ memory architecture |
| c8QiXuUMZCI | The INSANE Engineering Behind REPLIT Agents | 23:49 | ★ production harness engineering |
| Q-3fgVdmuVw | Ultimate Guide to Building 10x Faster with Claude Code | 23:27 | ★ |
| PRqiGS6fnIM | 1.6M agents registered for OpenClaw and did NOTHING | 28:04 | ★ agent-adoption postmortem |
| PW0sgog3kXY | STOP Using Claude Code Without This Fable 5 Agentic OS | 20:40 | ★ agentic-OS |
| BOXK2XFLA-E | Don't build more AI agents until you watch this | 18:25 | ★ |
| xqGCbEDbny8 | Codex: Your First Personal AI Agent Delegation Loop | 19:36 | |
| glAoiBWVkmU | Claude Code + Obsidian Setup That Runs My Life | 16:12 | |
| R2-Y1Hjwx2U | Stop Picking Between Claude Code and Codex | 16:13 | |
| Rl7rvHbDqGk | I Stopped Building AI Agents and Did This Instead | 16:13 | |
| PY7xIxybYNc | Pydantic AI 2.0: Composing Capabilities | 15:00 | possible watched-library signal |
| 9CiOwbmOKdU | I Rebuilt Hermes's Best Feature in Claude Code | 14:42 | |
| IShdbDP4Jgg | Top 10 Claude Code Plugins (June '26) | 12:27 | |
| jOK10k70XWE | OpenClaw vs Hermes Agent | 9:29 | |
| Gq0l4IYRIIU | New n8n Tool for Claude Code Automations | 10:15 | |
| Pi-m8R068r4 | The AI Offer You Can Sell Tomorrow Morning | 27:03 | likely monetization REJECT |
| eozCDUxwU8k | Best Local AI Hardware (Apple vs Nvidia) | 9:11 | likely hardware REJECT |
| 7HwhLOPeYh8 | What workflow should your AI agent do? (3 Questions) | 8:06 | |
| OSJJYWaxkKQ | Stop Using AI For This | 6:01 | likely REJECT |
| NE0aBuQF0HA | Introducing /visual-plan | 4:26 | |

## Per-link rationales (KB-ONLY, plain English first)

### Knowledge substrate — OKF / wiki standards

**VHKXIHP4i10 — OKF vs RAG, Cleared Up (Cloud Codes, 07-08).** Our workspace IS a curated
markdown KB, and OKF is the first vendor-published open standard for exactly that shape —
the KB has zero OKF coverage. Leads the four-video OKF cluster (newest, cleanest). Patterns:
"RAG is a process, OKF is a format" category distinction; read-write knowledge substrate
(agents edit concepts in place — the KB can self-improve); OKF spec conventions (bundle,
path-as-identity, index.md, append-only log.md); OKF bundle as pre-labeled RAG input;
files-authored-for-models drift trend (llms.txt → agents.md → claude.md → OKF).

**_X55fkwdC-Q — OKF + RAG hybrid (Cloud Codes, 06-28).** Survives recency because it alone
carries the hybrid architecture: what to do when a query exceeds curation — a live design
question for our knowledge architecture. Patterns: query router (canonical → curated KB,
exploratory → retrieval); 80/20 curated-spine split; curated-concepts-outrank-retrieved-chunks
precedence rule; curated index as pre-search map behind one retrieval facade.

**T33iI6izAKw — Open standard for the Karpathy wiki (Cole Medin, 07-02).** Densest in the
cluster and most on-mission: our KB is a bespoke wiki with its own `_schema.yaml` — exactly
the non-interoperable artifact this argues against. Raises a real, gateable architecture
question: should the engine's KB be OKF-conformant or OKF-exportable? Patterns: substrate
standardization for cross-agent interop ("what MCP did for tools, OKF does for knowledge");
spec-as-skill (paste spec.md to one-shot conformant KBs); subagent-parallelized KB refactor;
multi-bundle two-tier indexing + thin CLI; shareable knowledge bundles as distribution format.

### Second brain / memory / folder structure

**DTCyvo6cC54 — Second-brain levels (Nate Herk, 06-17).** Crisp selection heuristics for the
decision the engine keeps advising on — when markdown routing is enough vs when vector/graph
layers pay their way. Patterns: reverse-engineer storage format from anticipated query shape;
evergreen-vs-volatile ingestion rule (give access to volatile systems, don't copy them in);
escalating search-order routing (curated file → wiki → live system-of-record); per-folder
heterogeneous retrieval levels, upgraded only on felt pain.

**-fSjdYzrFvA — Gbrain + Hermes second brain (Tonbi's AI Garage, 07-07).** The cleanest
boundary taxonomy yet for where agent memory ends and a knowledge base begins, on an
architecture matching our local-first commitments. Patterns: memory/wiki/world-KB trichotomy;
markdown-in-git system of record + derived disposable DB; MCP-subprocess vs CLI shell-out
tradeoff; write-back discipline ("memory is not the brain"). Roster note: **Gbrain (25k
stars, MIT) is a watched-libraries candidate** — zero KB coverage today.

**RQckIBzOCsA — Folder structure for AI software (AI Code That Works, 06-21).** Lands on a
live engine concern — our vault has archives, generated docs, and a growing CLAUDE.md surface,
and the KB has nothing on docs-lifecycle partitioning. Patterns: split docs by lifespan, not
topic (active/decisions/reference/archive; stale plans confidently steer agents at
already-hit targets); root-file edit guard (agent asks before editing CLAUDE.md itself);
over-fragmentation as the drowning problem's dual. Future (post-extraction, separately gated):
deltas to /maintain-docs and engine CLAUDE.md conventions.

**HRw-vP0j8OM — Agentic OS setup (Chase AI, 06-25).** Mostly re-cuts already-ingested Chase
AI material; two procedures survive. Patterns: session-history mining for skill discovery
(read the last 10-20 sessions, extract repeated manual tasks, propose skill candidates —
grounded in usage data); distribution-as-floor-raising (wrap validated skills as one-click
headless `claude -p` buttons). Lean 2-finding extraction.

### Harness / infrastructure

**l5rae4LMKBc — Claude builds its own harness (Prompt Engineering, 06-03).** Digest of an
Anthropic first-party blog on runtime-authored task-custom harnesses — the strongest evidence
yet for the frontier-model-as-harness-designer idea the KB holds only as P3 practitioner
opinion. Patterns: runtime-authored harness primitives; six-pattern harness-composition
taxonomy (classify-and-act, fan-out+synthesize, worker-critic, generate-and-filter,
tournament, loop-until-done); pairwise-tournament-beats-absolute-scoring judging;
loop-until-done as the cure for agentic laziness; harnesses as reusable saved artifacts.
**Follow-up: fetch the underlying Anthropic dynamic-workflows blog as a primary source.**

**MYPLpkENs7A — AI gateway layer (Devsplainers, 07-08).** The gateway is the one
infrastructure layer the KB names nowhere (`six-layer-agent-infrastructure-stack` has no
model-traffic layer) — decision-relevant for a multi-model agentic OS. Patterns: gateway's
five jobs + "adopt when your situation turns plural" heuristic; smart-routing catch-22
(RouteLLM: 95% frontier quality at 25% traffic); cache-aware routing threshold (mid-stream
model switches destroy warm caches); semantic-caching failure modes; gateway as
SPOF/key-vault attack surface (mandate a bypass path).

**rh_PcL26zls — Agent ownership (Nate B Jones, 06-21).** Ownership-as-operational-requirement
in the engine's governance-first lane; the KB has the problem side, not these remedy
artifacts. Patterns: agent owner card / human-facing registry ("A2A protocol for humans");
job–diet–boundaries–review-loop operating framework; permission-earning ladder;
ownership decision rule + decommission clause. Flag for the restructure Phase 2 audit: the
owner-card field set is a candidate criteria-delta for /assess-agent.

### Skills / prompting

**UNzCG3lw6O0 — Building great agent skills (Matt Pocock @ AI Engineer, 06-29).** A tier-1
authority handing over a skill-audit rubric that maps nearly 1:1 onto what /assess-skill and
/design-skill check — extraction upgrades their substrate. Patterns: leading-words lexical
steering (verified by watching the phrase echo in reasoning traces); invocation-mode decision
triad (incl. disable-model-invocation as a predictability lever); branch analysis as the
externalization rule; leg-work amplification by hiding future steps; pruning failure modes
(no-op deletion test, sediment detection, single source of truth).

**A8mokin_YOs — Skills v1.1 changelog (Matt Pocock, 07-08).** Applied evidence for the
missing-manual techniques plus one new planning topology. Patterns: wayfinder (issue-tracker
map of typed, session-sized, blocking-ordered decision tickets — the map, not the chat,
carries state); facts-vs-decisions leading-word split (stops interview skills grilling
themselves); Fowler code-smell names as ~10-line prior invocation; two-axis parallel review
(standards vs spec fidelity); reference-only skill shape for AFK agents. Roster checked and
declined: /wayfinder et al. overlap the GSD suite and /session-handoff.

### Loops / self-improvement

**HGCHgD4uGgY — 8 Claude loops (Austin Marchese, 07-03).** The engine runs a growing loop
portfolio (research-loop, watch-blogs, audits) and has nothing that monitors that portfolio's
run health — this is a concrete recipe for that gap. Patterns: ecosystem monitoring meta-loop
(convention-based `*-loop` discovery = zero-maintenance registry, compatible with our
no-hardcoded-counts rule; shared run-log skill; composability scan); North Star drift loop
(session-history trajectory extrapolation vs locked goals — /detect-drift is source-drift, a
different thing); critical-call-checkpoint heuristic for gate placement.

**8wsM0euQOvc — 5 loop archetypes (AI LABS, 07-09).** Newest and most operationally concrete
loop taxonomy; two recipes land on engine surfaces. Patterns: with/without-skill A/B baseline
runs to measure a skill's marginal impact; learning.md improvement journal inside the skill;
process-optimizer agent (improves the loop itself, not the artifact); multi-perspective
review council (4 specialized critics + orchestrator). Future home for the first two:
/meta-skill-author Eval/Improve modes, once its ownership lands.

**DQq-z4wROTc — Loop engineering (Cloud Codes, 06-26).** Two design rules survive dedup:
closed-loop floor + one open exploration instruction (the concrete rescue of
non-deterministic loops); legible/executable/verifiable agent-readiness triad. Provenance
note: attributes "my job is to write loops" to Anthropic's Claude Code lead via a June-2026
field guide — record as secondhand/unverified.

**2fc0NX9vIJ8 — Self-improving system (Austin Marchese, 06-28).** Its three-bucket change
approval (auto-approve / needs-sign-off / more-context, with checkbox review file and
"approve-and-don't-ask-again" preference memory) is the strongest reduce-Nick-bottleneck
mechanism in the batch — and touches DD-29, so it is governance-gated, KB-first. Also:
session-history mining as the self-improvement signal. Pass 2: process as a pair with
HGCHgD4uGgY; extract the three-bucket pattern once, citing both.

**rs2fFITXd6g — 6 fixes (Austin Marchese, 07-07).** Three mechanisms survive; one fills a
real gap — our verifier findings are code-centric. Patterns: persona-clone review board as
verifier for outputs with no tests; automation-verification gate skill (our rule 11 turned
into an executable mechanism — corroboration); proof-based concept grounding via session
history.

### Models / economics

**Zp8lr6IzUnQ — GLM 5.2 (Nate B Jones, 06-28).** Crosses the bar on decision-relevant
model-selection material. Patterns: center/edge-of-distribution task classification as the
model-routing input; harness non-portability across model families (Lindy: full harness
rewrite to move off Claude — strongest practitioner corroboration yet for our
skill↔model-coupling findings). Registry: first dedicated GLM 5.2 evidence (wanted-list item).

**1cSNE-ZkDLQ — Can't compete on cheap models (Nate B Jones, 07-05).** Under the essay: a
quantified three-tier experiment (Hashimoto). Patterns: frontier capability-probing ("$40
question" scouting — deliberate frontier spend on tasks not on any backlog); prototype-at-
frontier-then-downshift (generates the routing-table entries our tier-routing findings
consume). Registry: Fable-5 parity/uniqueness datapoints corroborating the existing entry.

### Fable usage / cost engineering

**nuwlyQXrADg — War-gamed plans (Mark Kashef, 07-05).** Upgrades the plan artifact itself —
the thing frontier-designs/cheap-executes says the frontier model should produce. Patterns:
war-game plan format (move / expected observation / failure signal / countermove); fork
triggers + abort conditions + blocked-variables ledger; executor-model-tailored plans;
frontier as unknown-unknown elicitor. Candidate enrichment for how the engine writes
handoff/plan documents (via pipeline, separately gated).

**qWhSFjDS3LA — Distilling Fable (Cloud Codes, 07-05).** Value is the quantified
counter-evidence: naive trace distillation made the student worse than its own base
("style transfers, genius does not") vs on-policy distillation working at 1/10 cost.
Evidence-only for the Model dimension — the engine has no fine-tuning surface. Primary-paper
verification flagged.

**p8ypBeNXQ8E — Fable 80% cheaper (Chase AI, 07-03).** Two quantified cost levers absent
from the KB. Patterns: effort-level tuning as first-order cost lever (low-effort frontier ≥
max-effort previous tier at ~1/6 cost, with benchmark numbers); frontier-as-advisor via CLI
`/advisor`. Registry note: effort-level economics for the next intentional refresh.

**U4TmrlWEY4M — Agent at the bills (Nate B Jones, 07-03).** A complete, reusable recipe for
high-trust document work, demonstrated three times. Patterns: nine-primitive agent skeleton
with a designed-in prepare-don't-submit gate; receipt artifact as the trust mechanism;
structure-addressed retrieval beats vector search for cited-document domains; data
normalization as cheap-model enabler.

**MFzxIT88zfg — Deck attack (Nate B Jones, 05-27).** Third independent corroboration of the
engine's rule-10 generator-assessor stance, with three genuine deltas. Patterns:
enumerate-don't-fix hostile-reviewer prompt (task flip as reliability mechanism);
cross-vendor adversarial build/attack loop + terminal language-polish pass; task risk
gradient for calibrating verification depth (a future /assess-* calibration idea).

**UvVVATGIm7k — 94% token cut (Eric Tech, 06-23).** The technique behind the plugin, not the
plugin: a token-economy mechanism distinct from our brevity findings — code reuse and YAGNI,
not terse output. Patterns: seven-rung minimal-code decision ladder (reuse-before-write);
on-demand vs always-on skill activation discipline; measure-the-delta + staging-clone
verification for AI refactors. Roster note: **Ponytail is a watched-libraries candidate**
(vendor-claimed benchmarks; one independent-ish corroboration in p8ypBeNXQ8E).

### Multi-agent / agentic engineering

**QSK4vf_ZTRA — Built my replacement (Nate B Jones, 06-26).** Names the exact problem the
agentic-OS trajectory targets — the human as the "hallway" between harnesses — with a
vendor-neutral ticket queue as coordination substrate. Queue mechanics are already in the KB;
the contract layer survives. Patterns: work-ticket contract (prompt-mode vs work-mode
boundary object with outcome/owner/scope/definition-of-done/receipt); claim receipt as
auditable proof-of-done distinct from agent self-report; needs-input escalation state
carrying the exact blocking question. Future harness-layer schematic candidate.

**iQyg-KypKAA — L8 principal's workflow (Kun Chen, 06-20).** Densest item in the batch — a
practitioner demonstrating the "harness layer above coding agents" the engine is moving
toward, with concrete pipeline stages. Patterns: dev-cost-estimation bias correction (models
overweight development cost, pick cheap designs — standing rule corrects it); memory-file→
skill migration to cut always-loaded token tax; post-implementation validation pipeline
(worktree isolation → intent extraction → rebase-first → adversarial fresh-context review →
evidence artifacts attached to PR → risk-gated human review); popularity ≠ efficacy for
skills (a 177k-star skill measured at +5% tokens and worse results); worktree lifecycle
pooling.

**muwRbfuKbR4 — Best setup isn't most autonomous (Cole Medin, 07-03).** Argues the engine's
own DD-108 position from independent evidence. Patterns: level-3 sandwich principle (full
coding delegation is justified by human planning + validation on both sides);
autonomy-progression-gated-by-maturity ("trust muscle" — remove the human from an
already-trusted workflow, never add autonomy first); dark-factory failure-mode taxonomy
(cascading failures, stalled handoffs, evaluation gaming).

## Follow-up queue (each item separately gated)

1. **Pass 2 extraction session** over the 28 KB-ONLY sources (~107k transcript tokens,
   ~97 estimated patterns). Pairing instructions: Austin Marchese pair (HGCHgD4uGgY +
   2fc0NX9vIJ8 — extract three-bucket once); Pocock pair (UNzCG3lw6O0 + A8mokin_YOs — one
   source cluster); Nate Jones econ pair (Zp8lr6IzUnQ + 1cSNE-ZkDLQ — two halves of one
   model-strategy framework); OKF keepers (write the spec-conventions finding once, sourced
   to both).
2. **Primary sources to fetch** (both absent from KB): the Anthropic dynamic-workflows blog
   (behind l5rae4LMKBc) and the Anthropic "field guide to Claude Fable" (behind the
   pw79ro49CzU REJECT).
3. **Watched-libraries candidates:** Gbrain, mattpocock/skills, Ponytail.
4. **Authority-registry candidates** (pending extraction hit-rate): Nate Herk, Tonbi's AI
   Garage, Austin Marchese.
5. **Model-capability-registry refresh bundle** (next intentional D2/2.A refresh, not
   piecemeal): GLM 5.2 first evidence; Hashimoto Fable-5 datapoints; GPT-5.6
   restricted-availability note; effort-level economics; weak DeepSeek vision flag.
   Explicitly excluded: the o6O4xu1LhDU rumor-tier benchmark claims.
6. **Evidence-strength / crosslink candidates for /reassess-priorities:** thin-router +
   scale-threshold findings (now corroborated across 4+ independent channels); three-bucket
   gate-tiering (3 independent sources); generator-assessor rule 10 (3rd external
   corroboration); DD-108 supervised autonomy (3 distinct sources);
   frontier-model-as-harness-designer as emerging hub finding (3 new extending sources).
7. **Blocked retry backlog:** re-run the fetch for the 20 deferred videos after 429 cooldown
   (plain `fetch.py --input LINKS.md` re-run; dedup will skip everything else), then wave-2
   triage.
8. **LINKS.md clearance** once verdicts are accepted — remove the 63 triaged; keep the 20
   deferred (they are the retry queue).

## Protocol observations (third run — promotion-trigger input)

- **Shape held for the third consecutive run**, but degenerately: an all-video batch
  collapses the classify step (single class) and the three parallel tracks to one KB track.
  The protocol's novel part — the roster rubric — fired weakly again: 0 ADD / 0 ENHANCE
  across 83 links (pilot: 0/1; run 2 similar). Every roster escalation that fired resolved to
  "KB-first, revisit on recurrence" per Rule 11.
- **What did the work this run:** topical batching of subagents (dedup-within-cluster), the
  recency-weighting rule (killed 5+ near-duplicate re-shoots cleanly), live-corpus grep dedup
  (2 already-ingested videos caught; no snapshot-index failures), and the session-134 probe
  tooling (dedup + cost table for free).
- **New heuristic worth codifying:** "does the video contain someone's *measured experiment*?"
  separated KB-ONLY from REJECT perfectly in the industry-news cluster.
- **Operational lesson:** an 83-video probe + fetch burst trips YouTube's IP rate limit
  (HTTP 429 on the subtitle endpoint) and poisons the rest of the session's fetches. For
  future 80+ batches: fetch first (before probing), or space the two by hours, or split
  across sessions. Candidate note for transcript-fetcher SKILL.md Limitations.
- **Authority-intelligence accumulating:** per-channel calibration (Medin's marginal-novelty
  rate dropping; Nate Jones reliable at ~50% KB-ONLY; monetization channels at 0%) is
  becoming triage-relevant state the protocol has nowhere to record. If promoted, a thin
  per-channel prior could live in the authorities registry.

## Appendix — probe cost table (83 unique videos)

Probe run 2026-07-12 (`fetch.py --probe --input LINKS.md`; in-batch duplicates skipped:
47oi3Q9apK0, lw6Ld1ZgpV8, UztrFXaSWv0). `[fetched]` = transcript cached; `[new]` = fetch
required (all 20 subsequently blocked by the 429 rate limit).

```
luBkbzjo-TA   1:07:01  ~14,743 tok  2026-04-30  [fetched]  FULL Guide to Becoming a Principled Agentic Engineer
9PUaEj0pMYE     17:45  ~ 3,905 tok  2026-06-19  [fetched]  The Skill vs Prompt Problem Everyone Gets Wrong
t7L6-fMpxFc     18:34  ~ 4,084 tok  2026-06-11  [fetched]  Apple WWDC 2026: The AI Story Everyone is Missing
mn4XBSBIuag     19:24  ~ 4,268 tok  2026-06-15  [fetched]  Your $20 AI Plan Costs Them Thousands
lw6Ld1ZgpV8     15:10  ~ 3,336 tok  2026-06-15  [fetched]  I Tried /teach and 10x'd My Ability To Learn
dUmT0OIGoqE      6:57  ~ 1,529 tok  2026-06-19  [fetched]  Scientists Found A Better Language For AI Agents
LpXhy2iiaQE      7:43  ~ 1,697 tok  2026-05-22  [fetched]  DeepSeek's New AI Is A Game Changer
huAwz_BR8WM     21:28  ~ 4,722 tok  2026-05-25  [fetched]  Demis Hassabis On What AI Will Do Next
rh_PcL26zls     14:20  ~ 3,153 tok  2026-06-21  [fetched]  You Can't Run AI Agents Without This
MFzxIT88zfg     19:29  ~ 4,286 tok  2026-05-27  [fetched]  I Built a Deck With AI, Then Made a Second AI Attack It
iQyg-KypKAA     45:46  ~10,068 tok  2026-06-20  [fetched]  L8 Principal's Agentic Engineering Workflow
mG4SmhWyeFA      5:50  ~ 1,283 tok  2026-06-22  [fetched]  DeepSeek Just Solved AI's Billion Dollar Problem
47oi3Q9apK0     54:42  ~12,034 tok  2026-06-22  [fetched]  The Definitive Guide to Setting Up Your AI Second Brain
RQckIBzOCsA     14:24  ~ 3,168 tok  2026-06-21  [fetched]  The Folder Structure That Makes AI Build Better Software
A0pdL3MS_7E      8:55  ~ 1,961 tok  2026-06-23  [fetched]  My Entire File System in 9 Minutes
zbmuiaPuiNM     21:55  ~ 4,821 tok  2026-06-25  [fetched]  Google Just Dropped a Masterclass on Agentic Engineering
A4zMyjkL0Dc     15:38  ~ 3,439 tok  2026-06-24  [fetched]  I Stopped Prompting AI One Task At A Time
2kKkb01GxYQ      5:59  ~ 1,316 tok  2026-06-24  [fetched]  Google's OKF: The Simple Folder Replacing Vector Databases
0GQ2RP-25gM     18:42  ~ 4,114 tok  2026-06-25  [fetched]  Why AI is like a (Clever Hans) Horse - Computerphile
QSK4vf_ZTRA     22:04  ~ 4,854 tok  2026-06-26  [fetched]  I Was The Only Thing Connecting Claude, ChatGPT, and Codex
_X55fkwdC-Q      9:49  ~ 2,159 tok  2026-06-28  [fetched]  Google OKF + RAG: The Ultimate AI Agent Architecture
H9oNA5IyrXA     17:13  ~ 3,787 tok  2026-06-29  [fetched]  Apple, Anthropic, And OpenAI Just Made The Same Move
HgAQOkG_v8c     16:16  ~ 3,578 tok  2026-07-01  [fetched]  I Built My Own AI Memory by Talking to Claude
T33iI6izAKw     19:37  ~ 4,315 tok  2026-07-02  [fetched]  Finally, an Open Standard for the Karpathy LLM Wiki is HERE
UztrFXaSWv0     24:39  ~ 5,423 tok  2026-06-18  [fetched]  The Creators of Claude Code and OpenClaw don't Prompt Anymore
lplVBFr0Ndc     11:59  ~ 2,636 tok  2026-07-02  [fetched]  Claude Fable 5 Use Cases You Must Do NOW
muwRbfuKbR4     21:14  ~ 4,671 tok  2026-07-03  [fetched]  The Best AI Coding Setup Isn't the Most Autonomous One
RtxUdvSTQGc      3:50  ~   843 tok  2026-07-04  [fetched]  Free Fable 5 tokens this weekend? Here's how to max them
1cSNE-ZkDLQ     15:39  ~ 3,443 tok  2026-07-05  [fetched]  You Can't Compete on Cheap Models Anymore
Mqr2WYQEhBw     10:37  ~ 2,335 tok  2026-06-27  [fetched]  Hermes vs Claude vs OpenClaw: You HAVE to try it
U4TmrlWEY4M     15:44  ~ 3,461 tok  2026-07-03  [fetched]  Every AI Agent Demo Stops at Email
pbrln2TVeh4      9:36  ~ 2,112 tok  2026-07-03  [fetched]  How Claude is Creating a New Generation of Millionaires
d2XiTDzoizc     14:19  ~ 3,149 tok  2026-07-02  [fetched]  This Skill Instantly 10x'es Every Claude Output
p8ypBeNXQ8E     12:01  ~ 2,643 tok  2026-07-03  [fetched]  Make Fable 5 80% Cheaper (& Other Usage Cheat Codes)
nuwlyQXrADg     13:58  ~ 3,072 tok  2026-07-05  [fetched]  Do THIS Before You Lose Access to Fable 5
Zp8lr6IzUnQ     17:35  ~ 3,868 tok  2026-06-28  [fetched]  GLM 5.2 Is Free And Beats Claude On Most Work
Aded2v7_vag     40:22  ~ 8,880 tok  2026-07-02  [fetched]  Obsidian: The Thinking Person's Set Up (FULL SET UP)
DTCyvo6cC54     30:59  ~ 6,816 tok  2026-06-17  [fetched]  Every Level of a Claude Second Brain Explained
HRw-vP0j8OM     31:20  ~ 6,893 tok  2026-06-25  [fetched]  The Agentic OS Setup That Will 10x Claude Code
ju7R6jer6_M     14:50  ~ 3,263 tok  2026-07-03  [fetched]  Stop Building AI Agents the Old Way
UNzCG3lw6O0     20:43  ~ 4,557 tok  2026-06-29  [fetched]  Building Great Agent Skills: The Missing Manual
141biWM1mlE     14:09  ~ 3,113 tok  2026-06-15  [fetched]  This Meta-Harness Changes How You Run AI Agents
qWhSFjDS3LA     11:10  ~ 2,456 tok  2026-07-05  [fetched]  How to Distill Claude Fable 5 Before It Goes Offline Again
l46NJXUL4PM      9:45  ~ 2,145 tok  2026-07-04  [fetched]  Google OKF + Claude : Why We Stopped Using RAG
UvVVATGIm7k     17:14  ~ 3,791 tok  2026-06-23  [fetched]  Claude Code Cuts Token Usage by 94% | Here's Why
Vwn19n8W-qE      9:51  ~ 2,167 tok  2026-07-06  [fetched]  Agent Loop Explained in 10 Minutes...
DQq-z4wROTc      8:31  ~ 1,873 tok  2026-06-26  [fetched]  Loop Engineering Explained by Claude Code Creators
l5rae4LMKBc     13:24  ~ 2,948 tok  2026-06-03  [fetched]  Claude Can Now Build Its Own Harness... For Every Task
J2ZE6XGCYb0      8:11  ~ 1,800 tok  2026-06-09  [fetched]  Here we go again...
o6O4xu1LhDU      6:01  ~ 1,323 tok  2026-07-07  [fetched]  Fable 5 Just Got Extended (Here's Why)
HGCHgD4uGgY     17:11  ~ 3,780 tok  2026-07-03  [fetched]  8 Claude Loops to Build 10x Faster
2fc0NX9vIJ8     16:46  ~ 3,688 tok  2026-06-28  [fetched]  How to Build A Self-Improving System with Claude
rs2fFITXd6g     14:05  ~ 3,098 tok  2026-07-07  [fetched]  You're the Problem, Not Claude (6 Fixes to 10x Output)
pw79ro49CzU     11:25  ~ 2,511 tok  2026-07-07  [fetched]  Anthropic Just Dropped a Guide for WAY Better Claude Output
VHKXIHP4i10      9:00  ~ 1,980 tok  2026-07-08  [fetched]  Google OKF vs RAG Confusion, Finally Cleared Up
HIJVMVBM4KM     14:30  ~ 3,190 tok  2026-06-19  [fetched]  When to Use Claude Agent SDK
-fSjdYzrFvA     15:20  ~ 3,373 tok  2026-07-07  [fetched]  Give Your AI Agent a Second Brain (Gbrain + Hermes Agent)
dk1Y3VtC3F8     14:30  ~ 3,190 tok  2026-07-08  [fetched]  12 Open Source AI Tools That Feel ILLEGAL To Know About
HhWwllcbc2g     19:21  ~ 4,257 tok  2026-07-07  [fetched]  Claude Fable 5 Just Built the Ultimate Agent Harness
A8mokin_YOs     15:11  ~ 3,340 tok  2026-07-08  [fetched]  New Skills! v1.1 brings /wayfinder, /research, /implement…
MYPLpkENs7A     11:21  ~ 2,497 tok  2026-07-08  [fetched]  AI Gateway: The Layer Every AI Stack Eventually Needs
8wsM0euQOvc     13:25  ~ 2,951 tok  2026-07-09  [fetched]  5 Insane Claude Loops You Need To Use Right Now
R-5_2nsF_ZM     18:57  ~ 4,169 tok  2026-07-09  [fetched]  I Love the Karpathy LLM Wiki but it Doesn't Scale
jOK10k70XWE      9:29  ~ 2,086 tok  2026-06-15      [new]  OpenClaw vs Hermes Agent (Don't choose WRONG!)
PY7xIxybYNc     15:00  ~ 3,300 tok  2026-07-10      [new]  Pydantic AI 2.0: Composing Capabilities
9CiOwbmOKdU     14:42  ~ 3,234 tok  2026-07-10      [new]  I Rebuilt Hermes's Best Feature in Claude Code
eozCDUxwU8k      9:11  ~ 2,020 tok  2026-07-11      [new]  The Best Local AI Hardware (APPLE vs NVIDIA)
Pi-m8R068r4     27:03  ~ 5,951 tok  2026-05-22      [new]  The AI Offer You Can Sell Tomorrow Morning
Q-3fgVdmuVw     23:27  ~ 5,159 tok  2026-07-11      [new]  The Ultimate Guide to Building 10x Faster with Claude Code
7HwhLOPeYh8      8:06  ~ 1,782 tok  2026-07-10      [new]  What workflow should you get your AI agent to do?
PxuMqeIqCEo     27:18  ~ 6,006 tok  2026-06-07      [new]  AI Agent Memory Masterclass
PRqiGS6fnIM     28:04  ~ 6,174 tok  2026-07-10      [new]  1.6M agents registered for OpenClaw and did NOTHING
NE0aBuQF0HA      4:26  ~   975 tok  2026-06-16      [new]  Introducing /visual-plan
BOXK2XFLA-E     18:25  ~ 4,051 tok  2026-06-17      [new]  Don't build more AI agents until you watch this
OSJJYWaxkKQ      6:01  ~ 1,323 tok  2026-06-12      [new]  Stop Using AI For This
c8QiXuUMZCI     23:49  ~ 5,239 tok  2026-06-13      [new]  The INSANE Engineering Behind REPLIT Agents
PW0sgog3kXY     20:40  ~ 4,546 tok  2026-06-14      [new]  STOP Using Claude Code Without This Fable 5 Agentic OS
xqGCbEDbny8     19:36  ~ 4,312 tok  2026-06-12      [new]  Codex: Your First Personal AI Agent Delegation Loop
IShdbDP4Jgg     12:27  ~ 2,739 tok  2026-06-06      [new]  The Top 10 Claude Code Plugins (June '26)
glAoiBWVkmU     16:12  ~ 3,564 tok  2026-05-16      [new]  The Claude Code + Obsidian Setup That Now Runs My Life
Gq0l4IYRIIU     10:15  ~ 2,255 tok  2026-05-01      [new]  This New n8n Tool Just Changed Claude Code Automations
R2-Y1Hjwx2U     16:13  ~ 3,567 tok  2026-06-10      [new]  Stop Picking Between Claude Code and Codex
Rl7rvHbDqGk     16:13  ~ 3,567 tok  2026-05-28      [new]  I Stopped Building AI Agents and Did This Instead

Total: 83 videos, 23:30:01 runtime, ~310,175 estimated transcript tokens
```
