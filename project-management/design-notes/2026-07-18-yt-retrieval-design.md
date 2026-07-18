---
title: "YT-retrieval design — /watch-youtube discovery skill (watch-history discovery)"
id: "yt-retrieval-design-2026-07-18"
type: "design-note"
category: "research-intake"
target_system:
  - "improvement-loop"
stage: "review"
created: "2026-07-18"
updated: "2026-07-18"
author: "claude"
source_dd: []
tags:
  - "design-note"
  - "researcher"
  - "discovery"
  - "link-intake"
---

# YT-Retrieval Design — `/watch-youtube`

**Status: brainstormed inline with Nick (2026-07-18, the PROGRESS-ruled interlude);
rulings recorded at decision time.** The build is filed as IB-179; drafting the skill
goes through `/design-skill` → `/assess-skill` (rule 10) with this note as intent.

**Plain English.** Today Nick is the engine's YouTube discovery mechanism twice over:
he curates by choosing what to watch, then hand-copies URLs into `LINKS.md` for
`/link-intake` to triage. This design automates the second step and deliberately keeps
the first: **Nick's watch history is the discovery list.** A Researcher skill reads the
history since the last run, enriches each new video with metadata, filters out personal
viewing, dedups against the KB, and appends survivors to `LINKS.md` for the normal
`/link-intake` gate. Discovery is automated; curation stays human; every judgment
stays gated.

## Evidence (verified in-session, 2026-07-18)

- Nick's same-day `LINKS.md` batch: 28 hand-pasted YouTube URLs — the manual labor
  this design removes.
- **Watch-history mechanism proven:** the official Data API dropped watch history in
  2016 and Takeout exports only on a ~2-month cadence. But `yt-dlp :ythistory`
  (InnerTube via Chrome cookies; yt-dlp 2026.07.04 already in the toolchain) returned
  Nick's history as structured JSON on this machine. Its top 5: two videos from the
  current LINKS.md batch (Philipp Schmid evals talk, Anthropic HTML-specs talk), one
  relevant-adjacent, two personal (housing, color dictionary). The history *is* the
  manual-collection behavior, observable programmatically — and the personal entries
  show why a relevance filter is mandatory.

## Design

One Researcher skill, **`/watch-youtube`** (`watch-*` family), plus a small
deterministic tool at `app/yt-watch/` (mirrors the `transcript-fetcher` app-tool
pattern: skill orchestrates, tool executes).

**Discovery pass — watch history** (what Nick actually chose to watch):

1. `yt-dlp :ythistory` with Chrome cookies (read-only), newest-first.
2. **High-water mark** instead of date filter (the feed exposes no watched-at
   timestamps): read until the first video ID seen in the previous run; the watermark
   (top ~10 IDs, includes personal viewing) lives gitignored under `app/yt-watch/`.
   Cold start: take the newest ~50. A re-watched old video resurfacing is treated as
   signal, not noise.
3. **Metadata enrichment** per new ID (probe: title, channel, upload date, duration,
   description head) — triage-relevant decisions ride full metadata, per Nick's ruling.
4. **Relevance filter — strict bar (Nick-ruled on the v0 eval extras):** keep
   core-dimension content, favoring named-practitioner/org talks; drop covered-cluster
   duplicates, companions of already-queued items, clickbait-shaped videos without a
   named authority, off-dimension theory, and loose adjacency. The six eval verdicts
   are the calibration exemplars (eval report §Resolution). Dropped entries are never
   persisted.

**Tail:**

- Dedup against the live corpus — video-ID `rg` over `research-sources/` URLs, the
  transcript cache, and the current `LINKS.md` (link-intake's live-corpus rule).
- Append survivors to `LINKS.md` under a dated marker (`# --- /watch-youtube
  YYYY-MM-DD ---`), bare URLs; per-video provenance (channel, upload date) lives in
  the report.
- Discovery report to `operations/research-reports/{date}-watch-youtube.md`:
  new-video table with metadata, dedup hits, dropped-count (titles not persisted),
  unregistered-channel observations.
- Update the history watermark.
- **Zero transcript spend here** — transcripts remain in `/link-intake`'s chunked,
  gated flow. Discovery costs one history call + one metadata probe per new video.
- The skill's only writes: the LINKS.md append, the report, the gitignored watermark.
  It never touches authorities, findings, or sources.

**New-channel promotion (Nick's mechanism, ruled 2026-07-18):** when history keeps
surfacing relevant videos from a channel that is not yet an authority (recurrence
threshold 2–3+, per the tolerate-one-off rule), the report proposes registering it as
an authority — Nick gates; registration is a normal authority-entry creation.
`/link-intake`'s existing per-channel calibration observations remain the complementary
prune/tier signal on the authority side.

## Rulings and their provenance

- **History is the discovery list; channel-feed monitoring removed** — Nick, follow-up
  ruling 2026-07-18: watching channel uploads "would be too noisy. I like to use myself
  as a curator for these, so they are more high-signal. I use the YT History as the
  list." See rejected alternative below.
- **History via API + metadata in scope** — Nick pushed for API-based history with full
  metadata ("that way we can decide based on that"); mechanism verified same session.
- **Promotion of unregistered channels to authorities** — Nick's idea, verbatim intent.
- **PRD posture: design note states the distinction, no PRD edit** — Nick picked
  explicitly (see next section).
- **LINKS.md handoff** — design recommendation consistent with Nick's answers (one
  queue, existing gates); he gates it with this note.

## Rejected alternative — channel-feed monitoring (do not re-propose)

Verified working in the same session: YouTube serves native RSS per channel
(`youtube.com/feeds/videos.xml?channel_id=UC…`, no API key; Cole Medin's feed surfaced
the Vercel Eve video two days before Nick hand-pasted it), and a design pass existed
that watched the ~30 YouTube-typed authorities' feeds with watch-state fields on
authority entries. **Nick rejected it (2026-07-18): channel uploads are unfiltered
publish streams — too noisy; his own watching is the curation layer.** Consequence:
no watch fields on authorities, no channel-ID backfill, no `_schema.yaml` change, no
feed fetching. If a future need arises for publish-stream coverage, it re-enters
through a fresh Nick gate, not by default.

## Relationship to the PRD non-goal

The PRD closes **"bulk video intake as research strategy"** (two consecutive
zero-ADD/ENHANCE runs; `/link-intake` owns routine batches). This design does not
reopen it — if anything, history-only scoping narrows it further: discovery volume is
bounded by what Nick personally chose to watch, not by what channels publish. The
skill adds no extraction spend, fetches no transcripts, and issues no verdicts; triage
stays Nick-invoked with every downstream gate unchanged — aligned with "research spend
goes to targeted queries and primary sources."

## Privacy and failure modes

- History is personal data: processed locally, in-session; only relevant survivors are
  written anywhere; the gitignored watermark holds raw IDs only; dropped titles are
  never persisted; cookies are read from Chrome's store, never copied into the repo.
- Cookie expiry / InnerTube drift → the run reports "history unavailable" and exits
  without writes (manual LINKS.md pasting remains the natural fallback). The history
  call is one request per run — no IP-block exposure of the transcript kind.

## Out of scope

Channel-feed/publish-stream monitoring (rejected above), triage verdicts, transcript
fetching, authority tier changes, bulk-intake reopening, subscriptions-feed ingestion
(`:ytsubs` — same noise objection). Future seams, not v1: a discovery-sweep umbrella
over the `watch-*` family; scheduling the run as a Researcher wake-queue item under E4
wake/dispatch.

## v0 eval (Nick-ruled method, run 2026-07-18)

Nick's ruling: the true evaluation is to build the initial version, run it, and score
its output against the hand-curated LINKS.md batch — the closer the match, the more
correct the skill. Run same-day with `app/yt-watch/discover.py` (v0):
**28/28 batch videos recovered from history (100% recall), 0 false negatives, 81%
precision vs Nick's curation (6 on-topic extras, 2 borderline), and the dedup caught 2
already-ingested videos Nick had re-pasted by hand.** Nick ruled on the extras same
day: keep the Hugging Face self-training-agents talk (a genuine catch — appended to
LINKS.md), skip five → post-ruling precision 84%, extras yield 1-in-6, filter bar
codified strict (Design step 4). Full numbers and build implications:
`operations/research-reports/2026-07-18-watch-youtube-eval.md`. The six verdicts are
the SKILL.md's calibration exemplars; the eval numbers are the pilot regression bar.

## Build path (IB-179)

1. `app/yt-watch/` tool: extend v0 `discover.py` with watermark + uniq-by-ID +
   selective probe enrichment (eval implications 1–4).
2. Skill authored via `/design-skill` with this note as intent; `/assess-skill` audits
   in fresh context (rule 10). Placement: engine-scoped `.claude/skills/watch-youtube/`
   (DD-109).
3. Pilot = re-run against the eval fixture (2026-07-18 batch): 100% recall, 0 FN,
   ≥81% precision, both double-pastes dedup-excluded.
