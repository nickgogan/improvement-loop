# /watch-youtube v0 Eval — Discovery Pass vs Hand-Curated LINKS.md (2026-07-18)

**Method (Nick-ruled):** build the initial discovery pass, run it, and score it against
the 2026-07-18 LINKS.md batch as ground truth — the closer the discovery output matches
what Nick hand-collected, the more correct the skill. Tool: `app/yt-watch/discover.py`
(v0), one `yt-dlp :ythistory` call via Chrome cookies + corpus dedup. Relevance
judgment simulated model-side from title+duration (as the skill will do), keep-if-
borderline per the design note. Raw history stayed in gitignored `state/` and the
session scratchpad; this report names only on-topic or borderline-professional titles —
clearly-personal entries appear as counts.

## Headline numbers

| Metric | Result |
|---|---|
| History window reachable | 194 rows → 132 unique videos (62 re-watch rows) |
| Ground truth (LINKS.md batch) | 28 video IDs |
| **Recall — batch videos present in history** | **28/28 = 100%** |
| Batch span in history | positions 1–131 (the "collection era") |
| False negatives (batch videos the filter would drop) | **0** |
| Already-ingested watched videos correctly dedup-excluded | 27 unique (56 rows) |
| Dedup catches Nick's manual process missed | 2 (see below) |
| Filter false positives vs Nick's curation (batch era) | 6 (2 of them borderline-keeps) |
| **Precision vs Nick's curation** | 26 kept-and-pasted / 32 proposed = **81%** |

Every video Nick hand-collected was sitting in the reachable history, none would have
been relevance-dropped, and the pass would have proposed them all — plus six extras.

## Dedup wins over the manual process

Two batch links are videos **already ingested** (transcripts exist from earlier runs):
`Q-3fgVdmuVw` (Ultimate Guide to Building 10x Faster) and `r5iBG1s_MDk` (4 Loops).
Nick re-pasted them by hand; the skill would have silently excluded both. The 27
already-ingested watched videos (re-watches of transcribed sources) were all correctly
excluded by the corpus dedup.

## The six extras (Nick gates: noise or missed value?)

On-topic titles the filter would have proposed that Nick chose not to queue:

| Pos | Video | Title | Judge note |
|---|---|---|---|
| 35 | `hzQie4EucY0` | This "Karpathy file" will 10x your claude output | on-topic; triage would likely REJECT (Karpathy-wiki cluster already ingested) |
| 36 | `sBg90v2qfas` | OpenWiki Brains, general-purpose memory for agents | companion video of the `langchain-ai/openwiki` repo Nick DID queue |
| 46 | `neK8ydl0Vlk` | This Repo Just Solved The #1 Claude + Codex Headache | on-topic, clickbait-shaped; measured-experiment heuristic would judge at triage |
| 51 | `OV56RddyFuU` | Self-Training Agents: Hermes Agent, HF Traces, Skills, MCP — Merve Noyan, HF | strongly on-topic; plausibly a genuine miss |
| 3 | `GlYgs6v2YfU` | But what is cross-entropy? (watched 3×) | borderline-keep: model-layer theory, off the agentic-coding dimensions |
| 61 | `VbqaL_eHhKY` | YC's Head of Design Shows You How To Design With AI (watched 2×) | borderline-keep: design-with-AI adjacency |

Borderline drops (professional-shaped, judged off-dimension): "Dot Plots" (product
analytics), "Why every tech company is hiring for this job" (career commentary).
All other drops — 40+ unique videos — were clearly personal viewing (counts only).

**Resolution (Nick ruling, same day):** keep `OV56RddyFuU` (the Hugging Face
self-training-agents talk — "that's a good one"; appended to LINKS.md under the
skill's dated marker), skip the other five. Post-ruling score: 27 of 32 proposals
Nick-valid (26 batch + 1 genuine catch the curator missed) = **84%**, recall 100%,
and the extras channel proved nonzero yield (1 in 6). **Filter bar codified as
strict**: keep core-dimension content, favoring named-practitioner/org talks; drop
covered-cluster duplicates, companions of already-queued items, clickbait-shaped
videos without a named authority, off-dimension theory, and loose adjacency. These
six verdicts are the SKILL.md's calibration exemplars.

## Cold-start observation (pre-batch era, positions 132–194)

The window extends past the current batch into already-processed history. A cold-start
run would additionally propose the on-topic, never-queued: `xUnRQ9vLXxo` (Theo Browne
— Everything we knew about software has changed), `d9XCX0PcOq0` (Stop Using Fable 5 in
Claude Code), `zWQe2Fn--Eg` (The AI Future No One Wants to Talk About, borderline),
and `zhCIF4S1Pyw` (Post Launch FAQ — ambiguous title, the case where the metadata
probe earns its place). Everything else pre-batch was personal (drop) or already
ingested (dedup).

## Build implications for IB-179

1. **Uniq by video ID** keeping newest position — 32% of raw rows are re-watch
   duplicates; v0 prints raw rows.
2. **No duration floor** — a 4:47 batch video (`VONzHfDp4-U`) rules out short-video
   heuristics.
3. **History depth**: the reachable window (~132 unique) comfortably covers a
   collection era; the high-water mark makes routine runs read far less.
4. **Probe selectively** — title+duration sufficed for ~95% of judgments; the metadata
   probe is needed only for ambiguous titles ("Post Launch FAQ"), keeping per-run
   YouTube requests minimal.
5. **Acceptance fixture**: this batch + this report's numbers (100% recall, 0 FN,
   ≥81% precision, both double-pastes dedup-excluded) are the regression bar for the
   built skill's pilot run.
