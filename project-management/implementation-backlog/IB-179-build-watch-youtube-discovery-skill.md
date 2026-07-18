---
name: "Build /watch-youtube — YouTube discovery skill (watch-history discovery)"
id: "IB-179"
source_dd: null
status: "Backlog"
target_system: "improvement-loop"
priority: "P2"
type: "Build"
notes: >-
  Build the Researcher discovery skill designed in the Nick-ruled YT-retrieval
  interlude (design note 2026-07-18-yt-retrieval-design.md; mechanism verified
  in-session on this machine). Nick's watch history is the discovery list — channel-feed
  monitoring was verified but REJECTED (too noisy; Nick curates by watching; do not
  re-propose). Scope: app/yt-watch/ tool (yt-dlp :ythistory via Chrome cookies,
  gitignored high-water mark, per-ID metadata probe), relevance filter (drop clear
  personal-viewing misses only; never persist dropped titles), dedup vs live corpus,
  append survivors to LINKS.md for the /link-intake gate — no triage, no transcripts,
  no verdicts, no authority writes in this skill. Includes the unregistered-channel
  promotion mechanism (2-3+ relevant hits → gated authority-registration proposal).
  Skill authored via /design-skill with /assess-skill audit in fresh context (rule 10),
  engine-scoped placement (DD-109). v0 eval DONE (2026-07-18, Nick-ruled method):
  100% recall, 0 FN, 84% post-ruling precision; filter bar ruled STRICT with the six
  eval verdicts as SKILL.md calibration exemplars; v0 tool at app/yt-watch/discover.py
  is the seed. Pilot: re-run the eval fixture (2026-07-18 batch + eval-report numbers)
  as the regression bar. Positioning vs the PRD bulk-video-intake non-goal is stated
  in the design note (Nick ruling 2026-07-18: note states it, no PRD edit).
milestone: null
---

# IB-179: Build /watch-youtube discovery skill

See `notes:` frontmatter. Canonical design:
`project-management/design-notes/2026-07-18-yt-retrieval-design.md`. Related:
`/link-intake` (consumer gate), `/transcript-fetcher` (app-tool pattern + downstream
transcript flow), `/watch-blogs` (family precedent), IB-177 (separate unit — design-mode
spec formalization of the intake skill).
