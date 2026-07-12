---
date: "2026-04-23"
title: "Librarian Tier-3 Read Log"
type: "operational-reference"
target_system:
  - "improvement-loop"
actor: "Claude (Librarian disposition)"
area: "librarian-usage"
rationale: "Rolling log of Librarian Tier-3 reads (watched-library repo reads) per read-contract §5.3. One bullet per read, grouped under date/session headers. When the file exceeds ~300 lines, rotate to archive/librarian-reads-YYYY-QN.md and start fresh. Q2 of the read-contract was resolved session 55 in favor of this shape (vs. per-read frontmatter files) for Occam reasons. Re-homed from operations/system-log/ 2026-07-12 when the SL folder froze (DD-116; DD-59 scope note) — this is a live rolling log, not a log entry."
source_dd: "DD-82, DD-86"
tags:
  - "librarian"
  - "usage-log"
  - "tier-3"
---

# Librarian Tier-3 Read Log

Rolling log of Librarian Tier-3 reads (watched-library repos via `/watch-upstream` caches). Per the Librarian read-contract §5.3 and Q2 resolution (session 55), Tier-3 reads append one bullet here rather than producing per-read files. (Lived in `operations/system-log/` until 2026-07-12; re-homed when that folder froze as read-only history.)

**Format** — under each `## YYYY-MM-DD (session N)` header:

```
- `<watched-lib/path>:<line-start>-<line-end>` — <consumer-ask summary>
```

**Rotation** — when this file exceeds ~300 lines, move it to `archive/librarian-reads-YYYY-QN.md` and reset this file with the same preamble.

---

## Reads

_No Tier-3 reads recorded yet. First entry will land here._
