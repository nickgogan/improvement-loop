---
type: "link-intake-triage-report"
topic: >-
  Session-150+ triage of the 2026-07-18 LINKS.md batch — 29 YouTube videos + 1
  GitHub repo (langchain-ai/openwiki), incl. Nick's inline notes (Vercel Eve
  watched-repo candidate; mattpocock/skills interest) and the /watch-youtube v0
  eval catch. KB-fit + roster-escalation verdicts per link.
date: "2026-07-18"
protocol_spec: ".claude/skills/link-intake/SKILL.md"
input: >-
  LINKS.md 2026-07-18 batch: 30 links, no in-batch duplicates — 29 unique video
  IDs + langchain-ai/openwiki. Zero pre-fan-out KB dedup hits (all-new material).
verdict_set: ["ADD", "ENHANCE", "KB-ONLY", "REJECT"]
---

# Link-Intake Triage Report — 2026-07-18 (fifth run)

Triage of the full 30-link queue Nick accumulated since wave-3, processed to completion
per the ruled queue (item 1). Four topical triage subagents (Sonnet, Nick-confirmed this
run; read-only), one verdict per link, dedup against the live findings/sources corpus.
**This report changes nothing by itself** — every routing below is separately
Nick-gated.

**Tally: 1 ADD · 4 ENHANCE · 13 KB-ONLY · 12 REJECT · 0 defer.** The KB-ONLY set splits
into 9 research-sources for Pass 2, 1 finding-extension, 2 watched-library
registrations (`vercel/eve`, `langchain-ai/openwiki`), and 1 watched-library update
(pi-agent extension note). Of the 12 REJECTs, 10 are dedup kills against deeper
existing coverage and 2 are relevance/no-measurement kills. ~26–31 novel patterns
estimated across the Pass 2 set; ~54k transcript tokens for the extraction session.
Both Nick inline notes and the /watch-youtube catch resolved (see per-link entries).

## Batch mechanics

- **Queue:** 30 links — 29 YouTube videos + 1 GitHub repo. No in-batch duplicates by
  canonical video ID. Nick inline notes carried into triage: `m8VC2SV2igM` (Vercel
  framework → watched-repo candidate), `M6mYodf0dJM` (mattpocock/skills interest).
  `OV56RddyFuU` entered via the /watch-youtube v0 eval (Nick-accepted catch).
- **KB dedup (pre-fan-out):** 0 hits — all 29 video IDs new to `research-sources/` +
  `research-findings/`; openwiki absent from `watched-libraries/`.
- **Transcript acquisition:** 2/29 pre-cached (2026-07-13). Probe 29/29 OK. Chunked
  fetch (16+11, ≤25 rule): 20 new via api backend, then a YouTube IP block
  (IpBlocked/429) took out the last 7 — playwright fallback empty, ytdlp 429. The
  **kome.ai fallback lane** (session-143 proven; the PROGRESS backlog trigger "next
  YouTube IP block" fired today) recovered **7/7**. Net: **29/29 transcripts cached,
  zero transcript-blocked defers** — the retry backlog stays empty.
- **Non-video classification:** openwiki = REPO-FRAMEWORK (LangChain CLI, TypeScript,
  12.3k stars, active) from README + repo metadata.
- **Fan-out:** 4 topical batches — A skills/evals/expertise (6) · B
  harness/architecture/infra (8) · C loops/CC-practice/setup (7) · D
  context/memory/specs/org (8 + openwiki). All four returned complete, well-formed
  verdicts on first dispatch; no re-dispatches, no escalation triggers fired.
- **Orchestrator reconciliation:** two verdict-vocabulary normalizations for tally
  consistency, action unchanged in both — openwiki `ADD (tool/watched-library)` →
  KB-ONLY (watched-library registration), matching how batch B labeled the
  same-shaped Eve outcome; `r5iBG1s_MDk` `ENHANCE` targeting a *finding* → KB-ONLY
  (finding-extension at Pass 2), since ENHANCE is reserved for roster skills. Two
  subagent-flagged metadata gaps resolved live by the orchestrator: Vercel Eve
  upstream ref = `github.com/vercel/eve` (3,853★, pushed 2026-07-18;
  vercel-labs/eve and vercel/eve-framework do not exist); ExplainDiff upstream ref =
  `gist.github.com/geoffreylitt/a29df1b5f9865506e8952488eac3d524` + companion essay
  `geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck.html`.

## Verdict summary

### ADD (1)

| Link | What | Placement |
|---|---|---|
| `WkBPX-oDMnA` — "Understanding is the new bottleneck" (Geoffrey Litt, Notion) | Comprehension-gate explainer skill modeled on Litt's ExplainDiff: change/document → teaching doc (background → plain-language intuition → interactive mockup → narrated walkthrough → 5-question quiz the human must pass before approving) | Engine-scoped `systems/improvement-loop/.claude/skills/` (DD-109); upstream ref: the gist above (HTML + Notion variants); authoring model unstated |

### ENHANCE (4)

| Link | Target skill | Deltas ours lacks |
|---|---|---|
| `0vphxNt4wyk` — "Don't Ship Skills Without Evals" (Schmid, DeepMind) — **Nick's ruled anchor for queue item 4** | `/meta-skill-author` | SkillBench 1.1 numbers (~15% avg lift; AI-generated skills can measurably hurt; <500-line guidance); capability-vs-preference skill taxonomy (retireable vs durable); executable regex+LLM-judge eval harness (JSON cases + runner) vs our static trigger-eval; retirement/ablation protocol; multi-trial cross-harness discipline |
| `vy7o1g2iHY8` — "Deleted 95% of my agent skills" (Nick Nisi, WorkOS) | `/self-improve` + `/meta-skill-author` | Transcript-mining of run logs as an automatic scan-mode input (doom-loop signatures); domain-sharded memory-file routing (E1-relevant); cryptographic proof-of-execution vs trusted self-reports (E4-relevant); the 77%→97% skill-regression case (10,000 lines → 553 "gotchas", eval 68min→6min); hash-gated skill regeneration |
| `504PvfXou5Y` — "BDD, ADR, PRD, WTF" (Cichra, Safe Intelligence) | `/dd` (workspace root) | File/module-scoped decisions with lint enforcement (DD declares governed paths, linter blocks violating commits — ours are convention-only); BDD-style executable behavior specs bridging decision→verification (our pre-commit checks schema, not behavioral conformance) |
| `PDJfciNhyHU` — "They Need A Clean Setup" (Nate B Jones) | `/simplify-context` (workspace root) | Map-first per-control record (where-lives/when-loads/what-job/who-owns/evidence/misuse-risk) — candidate seed for the queue-item-3 asset-description schema; empirical compact-vs-thick A/B testing (his test: compact 3/3, thick failed twice) vs our static-only audit; per-surface harness differentiation; capability-drift decay detection |

### KB-ONLY (13)

| Link | Intake path | Novel est. | One-line why |
|---|---|---|---|
| `am_oeAoUhew` — Harness Engineering (Lopopolo, OpenAI) | research-source | 5–6 | Primary source for harness engineering (ours was secondhand): garbage-collection day, QA-plan-as-merge-gate, persona-keyed per-push reviewers, lint-failure-as-remediation-prompt |
| `ow1we5PzK-o` — Multi-Agent Architecture That Ships (Factory) | research-source | 6–8 | Production missions architecture: five-pattern taxonomy, pre-code validation contracts, dual adversarial validators — primary material for future `/design-harness` + E2 task contract |
| `kfSDc2eVLo4` — Domain Expertise (Lovejoy) | research-source | 2–3 | Oracle→Evaluator→Architect progression — maps directly onto Nick's own bottleneck-reduction trajectory |
| `M6mYodf0dJM` — mattpocock/skills walkthrough — **Nick's note** | research-source | 1–2 | Everyday-flow fork rule + ~140k-token "smart zone" ticket sizing; repo already watched at the version shown — no re-analysis needed |
| `OqM67QG_Ikk` — fork() to Fleet (OpenAI) | research-source | ~3 | Novel only in persistence: CoW snapshotting, always-on tiered cache, snapshot-lineage scheduling (isolation third already covered) |
| `VktrqzQgytY` — CI/CD Is Dead | research-source | ~2 | Pre-merge reconciliation queue + review-outcome-not-diff; weight Medium (vision register) |
| `-we7iVySwkM` — Agents Talk Across Terminals | research-source | ~2 | Flat no-parent agent comms with observed failure modes — cross-link counterpoint to Factory's caution |
| `JQ_We_ztxrI` — "building loops wrong" (AI Jason) | research-source | ~3 | Loop-contract-as-one-file; poll-then-wake "combo" trigger (E4 wake/dispatch); CC/Codex event-trigger gap |
| `HjWESsnoU6g` — PARA experiment (Forte) | research-source | 1 | Measured 78% agent taxonomy-classification accuracy + named failure mode — calibration for E1 reflection-routing |
| `r5iBG1s_MDk` — "4 Loops" (Dream Labs) | finding-extension → `persona-clone-review-board.md` | (ext.) | Weighted multi-persona numeric score as an autonomous-loop stop condition for non-code outputs |
| `m8VC2SV2igM` — Vercel Eve (Cole Medin) — **Nick's note** | watched-library registration + `/repo-analyzer` | ~3 | `github.com/vercel/eve`: agent = folder of markdown+TS compiled to one manifest — working prior art for the queue-item-3 asset-description language |
| openwiki (langchain-ai) | watched-library registration + `/repo-analyzer` | — | CI-driven self-updating codebase wiki + personal-brain mode; emits Google's Open Knowledge Format — prior art for the E1 reflection mechanism; absent from the memory-spec 12-framework survey (gap flagged) |
| `t70YWb03vm0` — Pi subagents | watched-library update (`pi-agent.md` note) | 1 | `pi-agent-sub-agents` package exercising the extension API we already watch; cross-harness confirmation of our agent-split pattern |

### REJECT (12)

| Link | Reason |
|---|---|
| `3_gYbhABcAE` — Why Senior Engineers Struggle (Schmid) | Principles-only, no numbers; all five points covered deeper by existing findings |
| `OV56RddyFuU` — Self-Training Agents (HF) — /watch-youtube catch | Covered by `watched-libraries/hermes-agent.md` (deeper, newer); rest is HF product tour, no measured experiment |
| `Dtzy3UOJX9M` — Agent Harness Architecture | Content-mill explainer, unsourced stats; inferior in-batch to `am_oeAoUhew`; covered by harness mental-model findings |
| `956DPSPX4wg` — Automating The Wrong Layer | Covered by the 5-finding folder-workspace set from the same practitioner's earlier video; new segment is a self-described untested one-off |
| `JoXbk2fm7jM` — Agent loops in CC/Codex | Covered by loop-engineering source + heartbeat/cron findings; superseded in-cluster by `JQ_We_ztxrI`/`r5iBG1s_MDk` (recency rule) |
| `Q-3fgVdmuVw` — Ultimate Guide 10x (Marchese) | Self-recap of his own two already-extracted videos; wrapper is generic content-business advice |
| `MhHEGMFCEB0` — OpenAI Codex Masterclass | Every mechanism has an equal-or-deeper Claude-Code-native KB equivalent; competitive-intel confirmation only |
| `so9l_MwS2yg` — Attention Is the Bottleneck (Proser) | Covered by `session-history-mining-for-skill-discovery.md` (3× corroborated); rest is personal productivity habits |
| `esY99nYXxR4` — Context Management (Delucia) | Covered by five-context-techniques + two-threshold-compaction + context-rot findings; memory-spec corpus covers the territory |
| `Qrpm7E80wQ0` — HTML files as AI specs (Shihipar) | Covered by the 6-file Derrick-HTML set; superseded by the 2026-07-13 MDX synthesis that critiques ungoverned HTML |
| `hYcOFTMesGc` — Roadmap / AI-Native Teams | 15 rhetorical commandments, no measured experiment |
| `VONzHfDp4-U` — Claude's Deference Explained | Real Anthropic persona-variance study, but no intersection with engine priorities |

## Blocked / defer

None. 29/29 transcripts obtained (kome.ai lane recovered all 7 IP-blocked videos);
openwiki classified from live README. The LINKS.md retry backlog will be empty after
clearance.

## Follow-up queue (each item separately Nick-gated)

1. **ADD → `/design-skill` run in fresh context (rule 10):** the comprehension-gate
   explainer skill from `WkBPX-oDMnA` + the ExplainDiff gist. Clearest first use:
   gating prose-heavy DDs/plans with a verify-understanding artifact.
2. **ENHANCE anchor → queue item 4 (already ruled):** `0vphxNt4wyk` deltas feed the
   `/meta-skill-author` eval-sophistication upgrade; Pass 2 extraction of this source
   should run before or with that work.
3. **ENHANCE set → per-skill gates:** `vy7o1g2iHY8` (→ `/self-improve` +
   `/meta-skill-author`), `504PvfXou5Y` (→ `/dd`), `PDJfciNhyHU` (→
   `/simplify-context`). Each via `/assess-skill`-mediated change in fresh context.
4. **Watched-library registrations:** `vercel/eve` (Nick's note; queue-item-3 prior
   art) and `langchain-ai/openwiki` (E1 prior art) → registry entries + `/repo-analyzer`
   passes. Plus the `pi-agent.md` extension note (no analyzer pass needed).
5. **KB-ONLY set → `/research-loop` Pass 2:** 9 research-sources + 1 finding-extension
   + the `WkBPX-oDMnA` secondary patterns (microworlds, shared spaces) — ~54k
   transcript tokens, ~26–31 novel patterns estimated.
6. **Memory-spec corpus gap:** openwiki absent from the 12-framework survey
   (`operations/plans/memory-spec-inputs/`) — record as a corpus-gap note (candidate
   line item alongside IB-178's corrections ledger, Nick routes).
7. **kome.ai fallback promotion:** the backlog line's trigger ("next YouTube IP block")
   fired and the lane went 7/7 — second proven occurrence (after session 143).
   Candidate IB item: build kome.ai in as a fetch.py backend.
8. **Authority-registry updates from calibration** (below) — notably AI Engineer
   (conference) has no `research-authorities/` entry despite repeated strong-signal
   appearances.

## Per-channel calibration

- **AI Engineer** (9 talks this batch — the dominant source): strong signal on
  named-practitioner, quantified talks (OpenAI ×3, Factory, Notion, Safe Intelligence,
  WorkOS ×2); the rejects reflect KB maturity or Codex-centricity, not weak content.
  Screen per-talk for measured claims; worth a dedicated authority entry.
- **Nate B Jones** (2): split verdict confirms the authority file's existing note — his
  harness-maintenance lane is strong (`PDJfciNhyHU` → ENHANCE), his org-commentary lane
  is not (`hYcOFTMesGc` → REJECT). Prioritize the former.
- **AI Jason** (1): production-tested, concrete, low fluff — prioritize for
  loop/orchestration content.
- **Cole Medin** (1): signal; disclosed Vercel sponsorship, minor discount.
- **Matt Pocock** (1): diminishing marginal value on already-tracked stable releases;
  full value on version bumps / new repos.
- **Jake Van Clief** (1): second consecutive mostly-re-coverage video — spot-check
  future submissions rather than blanket-include.
- **Austin Marchese** (1): skip recap/roll-up episodes; keep watching new material.
- **Dream Labs AI** (1): real technique inside a community-upsell wrapper — moderate,
  filter the pitch.
- **Tiago Forte** (1): honest quantified reporting, edge-of-relevance subject matter —
  occasional checks.
- **How I AI** (2): good general signal; both episodes redundant for us this batch.
- **Skill Advancement** (1): content mill, unsourced stats — noise, deprioritize.
- **Eric Michaud** (2): hands-on but unvetted solo creator — light monitoring only.
- **DIY Smart Code** (1): competent reporting, off-axis topics — no tracking.

## Protocol observations

- **kome.ai lane is now load-bearing:** 7/7 recovery today after 24/24 in session 143.
  The IP block hit mid-run even under the ≤25-chunk rule (block landed 5 videos into
  chunk B, ~21 fetches into the session) — chunking mitigates but does not prevent;
  the in-tool backend (follow-up 7) is the durable fix.
- **Verdict-vocabulary drift across subagents** (first occurrence): one subagent used
  ADD for a watched-library registration, another used ENHANCE for a finding-extension.
  Both normalized transparently above. Per the tolerate-one-off rule, no skill-text
  change proposed; revisit if it recurs.
- **Fan-out hygiene:** 4/4 batches complete and well-formed on first dispatch;
  read-only constraint held (no writes by subagents); model class asked-and-confirmed
  (Sonnet) per the session-146 ruling.

## Appendix — probe cost table

| ID | Duration | ~Tokens | Uploaded | Fetch route | Title |
|---|---|---|---|---|---|
| `so9l_MwS2yg` | 25:17 | 5,562 | 2026-06-11 | api | Your Attention Is the Bottleneck (Proser, WorkOS) |
| `t70YWb03vm0` | 12:36 | 2,772 | 2026-05-18 | api | Setting Up Pi Subagents |
| `-we7iVySwkM` | 11:30 | 2,530 | 2026-05-21 | api | These AI Agents Talk to EACH OTHER Across Terminals! |
| `HjWESsnoU6g` | 12:23 | 2,724 | 2026-04-07 | api | AI Organized My Files (Claude Code + PARA) |
| `JQ_We_ztxrI` | 14:06 | 3,102 | 2026-07-13 | api | I was building loops wrong... |
| `vy7o1g2iHY8` | 17:42 | 3,894 | 2026-05-30 | api | How I deleted 95% of my agent skills (Nisi, WorkOS) |
| `r5iBG1s_MDk` | 18:34 | 4,084 | 2026-07-12 | cached | Claude Code's Creator Revealed the 4 Loops |
| `OqM67QG_Ikk` | 44:33 | 9,801 | 2026-07-13 | api | From fork() to Fleet (Bhardwaj, OpenAI) |
| `Q-3fgVdmuVw` | 23:27 | 5,159 | 2026-07-11 | cached | The Ultimate Guide to Building 10x Faster with Claude |
| `ow1we5PzK-o` | 18:30 | 4,070 | 2026-05-06 | api | The Multi-Agent Architecture That Actually Ships (Factory) |
| `956DPSPX4wg` | 26:37 | 5,855 | 2026-05-20 | api | You're Automating The Wrong Layer |
| `WkBPX-oDMnA` | 19:33 | 4,301 | 2026-07-10 | api | Understanding is the new bottleneck (Litt, Notion) |
| `3_gYbhABcAE` | 10:39 | 2,343 | 2026-05-30 | api | Why (Senior) Engineers Struggle (Schmid, DeepMind) |
| `VONzHfDp4-U` | 4:46 | 1,048 | 2026-07-14 | api | Claude's Deference, Warmth, Depth, Candor Explained |
| `hYcOFTMesGc` | 17:52 | 3,930 | 2026-07-12 | api | Your Roadmap Is Why You're Losing to AI-Native Teams |
| `kfSDc2eVLo4` | 24:45 | 5,445 | 2026-05-16 | api | How to Leverage Domain Expertise (Lovejoy) |
| `esY99nYXxR4` | 16:16 | 3,578 | 2026-05-10 | api | How we solved Context Management in Agents (Delucia) |
| `0vphxNt4wyk` | 21:45 | 4,785 | 2026-07-14 | api | Don't Ship Skills Without Evals (Schmid, DeepMind) |
| `504PvfXou5Y` | 12:49 | 2,819 | 2026-06-03 | api | BDD, ADR, PRD, WTF (Cichra) |
| `Dtzy3UOJX9M` | 8:52 | 1,950 | 2026-07-13 | kome | Agent Harness Architecture |
| `m8VC2SV2igM` | 16:23 | 3,604 | 2026-07-16 | api | Production AI Agents (Vercel Eve) (Medin) |
| `M6mYodf0dJM` | 17:17 | 3,802 | 2026-07-16 | api | mattpocock/skills: complete workflow |
| `VktrqzQgytY` | 18:37 | 4,095 | 2026-05-13 | api | CI/CD Is Dead (Santos/Faulkner) |
| `PDJfciNhyHU` | 15:50 | 3,483 | 2026-07-15 | kome | Fable 5 And GPT-5.6... Clean Setup (Jones) |
| `Qrpm7E80wQ0` | 35:58 | 7,912 | 2026-05-18 | kome | HTML files as AI specs (Shihipar, Anthropic) |
| `am_oeAoUhew` | 46:20 | 10,193 | 2026-04-17 | kome | Harness Engineering (Lopopolo, OpenAI) |
| `JoXbk2fm7jM` | 29:07 | 6,405 | 2026-06-17 | kome | How to write AI agent loops in CC and Codex |
| `MhHEGMFCEB0` | 1:01:58 | 13,632 | 2026-04-29 | kome | OpenAI Codex Masterclass |
| `OV56RddyFuU` | 19:10 | 4,216 | 2026-05-13 | kome | Self-Training Agents (Noyan, HF) |

Batch total: 29 videos, 10:23:12 runtime, ~137,094 estimated transcript tokens.
Fetch outcome: 2 cached · 20 api · 7 kome.ai · 0 blocked.

## Pass 2 extraction outcome (appended post-gate, 2026-07-18/19)

Nick accepted all verdicts and approved the Pass 2 extraction batch (G9.I6 gate, one
approval covering the batch). Applied to the KB:

- **28 new findings** (2 at P1: `lint-test-failures-as-remediation-prompts`,
  `structured-handoff-schema-self-healing-multi-agent-missions` — both with named live
  engine hooks) + **8 finding updates**, including the `harness-engineering-third-evolution`
  primary-source upgrade (Medium→Strong; Lopopolo is the term's originator) and the
  `persona-clone-review-board` cartridge delta with its explicitly flagged
  autonomy-vs-rehearsal tension.
- **12 new sources**, **11 new authorities** + 2 authority updates (incl. the new
  `ai-engineer.md` conference entry consolidating 6 sources, and a
  sponsorship-calibration note added to `cole-medin.md`).
- **2 watched-library registrations** — `vercel/eve` (Nick's inline note; Apache-2.0,
  3,853★) and `langchain-ai/openwiki` (MIT, 12,280★; also logged as a memory-spec
  survey gap in the IB-178 ledger) — plus a `pi-agent.md` Notable Extensions note.
- **Registry maintenance:** both new loop findings added to the 11.A Loop Engineering
  cluster in `research-dimensions.md`; two entries appended to the IB-178 corrections
  ledger (openwiki survey gap; pre-collapse `S3` applicability values on two live
  findings).
- Extraction ran as 6 read-only Sonnet subagents staging to scratchpad; all 53 staged
  files passed `validate_frontmatter.py` pre-apply; zero slug collisions cross-batch or
  vs the live KB.

Remaining follow-ups from this run (unchanged, separately gated): the `WkBPX-oDMnA`
ADD via `/design-skill`; the four ENHANCE skill upgrades; `/repo-analyzer` passes on
eve + openwiki; the kome.ai fetch.py backend IB; reciprocal back-links via the next
`/finding-crosslink` pass.
