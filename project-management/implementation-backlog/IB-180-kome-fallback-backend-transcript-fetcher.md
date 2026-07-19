---
name: "kome.ai fallback backend inside the transcript-fetcher chain"
id: "IB-180"
source_dd: null
status: "Backlog"
target_system: "improvement-loop"
priority: "P2"
type: "Build"
notes: >-
  Promote the kome.ai fallback lane from ad-hoc session scripting into a first-class
  fetch.py backend (--backend kome, slotted into the auto chain after playwright/ytdlp
  fail with IpBlocked/429). Trigger fired for the second time: session 143 recovered
  24/24 blocked videos via manual POST kome.ai/api/transcript; session 151 (wave-4
  link-intake) recovered 7/7 mid-run after YouTube IP-blocked chunk B despite the
  ≤25-chunk rule — chunking mitigates but does not prevent. Implementation shape is
  proven: POST {video_id, format: true}, ~3s pause between calls, segment count from
  newline count, metadata header from the probe (watch-page metadata is not blocked).
  Session-151 recovery script is the seed (scratchpad kome_recover.py pattern —
  reimplement inside fetch.py; scratchpad is ephemeral). Keep the ≥1-calendar-day
  retry spacing rule for the YouTube-direct backends; kome is exempt (different
  infrastructure). Update the transcript-fetcher SKILL.md fallback chain (step between
  browser and manual-HTML) when built.
milestone: null
---

# IB-180: kome.ai fallback backend for the transcript fetcher

See `notes:` frontmatter. Evidence: HISTORY.md sessions 143 and 151;
`operations/research-reports/2026-07-18-link-intake-triage.md` §Batch mechanics +
§Protocol observations. Related: `/transcript-fetcher` (owning skill),
`/link-intake` (primary consumer).
