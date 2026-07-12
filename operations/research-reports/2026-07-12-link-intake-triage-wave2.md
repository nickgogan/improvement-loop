---
type: "link-intake-triage-report"
topic: >-
  Wave-2 retry run (session 136) over the 20-video retry backlog left Blocked
  by the session-135 full sweep. First supervised run of the /link-intake
  skill (promoted from the protocol in session 135).
date: "2026-07-12"
protocol_spec: ".claude/skills/link-intake/SKILL.md"
input: >-
  systems/improvement-loop/LINKS.md (20 lines, 20 unique video IDs — the
  retry backlog kept by the session-135 clearance edit)
verdict_set: ["ADD", "ENHANCE", "KB-ONLY", "REJECT"]
parent_report: "operations/research-reports/2026-07-12-link-intake-triage.md"
---

# Link-Intake Triage — Wave-2 Retry Addendum (session 136)

Retry of the 20 transcript-blocked videos from the 2026-07-12 full sweep, run through the
new `/link-intake` skill (its first skill-shaped run). **Outcome: 0 of 20 recovered — all
20 remain `REJECT (defer — transcript blocked)`.** LINKS.md is unchanged (keep-all-defers
rule); no verdicts changed, so there is nothing to gate beyond acknowledging the miss.

## Batch mechanics

- **Dedup (step 1):** all 20 IDs re-checked against the live corpus (`rg` over
  `research-sources/` URLs + transcript cache) — 0 already-ingested, 0 already-cached.
  Clean retry queue, exactly as left by the session-135 clearance.
- **Fetch-first (step 2):** one chunk of 20 (≤25 rule). Full available chain exhausted:
  - `api` — still **IpBlocked** on all 20;
  - `playwright` — "No transcript segments found" on all 20 (page-level block on the
    same IP, not a parser miss);
  - `ytdlp` (Homebrew 2026.07.04) — **HTTP 429** on the subtitle endpoint;
  - `ytdlp --cookies-from-browser chrome` — same 429 (cookies don't bypass an IP block);
  - browser-assisted HTML — **unavailable** (Chrome extension not connected, same as 135);
  - manual HTML — not attempted (requires Nick at the browser).
- **No triage performed:** transcript-first rule — no video is triaged from title/metadata
  alone. The wave-1 ★ density guesses stand unmodified.

## Root cause note (revises the wave-1 prognosis)

The session-135 report predicted "the 429 is temporal; a plain re-run next session should
succeed." Both sessions ran on the **same calendar day** — the cooldown was hours, not the
implied day+. The block is IP-level (api reports `IpBlocked`, not a per-request 429), and
same-day retry with cookies changes nothing. **Recommendation: retry no earlier than the
next calendar day**, and if it persists, the realistic rungs are (a) the Playwright-CLI
browser rung (pending ENHANCE gate on `/transcript-fetcher`), (b) connecting the Chrome
extension, or (c) manual HTML saves for the 6 ★-marked probable keepers only.

## Verdict summary

Unchanged from wave 1: 20 × `REJECT (defer — transcript blocked)`. See the parent report
for the per-video table (6 marked ★ probable keepers by probe metadata).

## First-skill-run observations (supervised run — audit follow-up d)

1. **No transcription defects found in the exercised path.** Steps 1, 2, and the Blocked
   convention behaved exactly as the protocol did in runs 1–3: dedup → fetch-first →
   chain → defer. Steps 3–4 and 6–7 (classify, fan-out, gate, clearance) were legitimately
   skipped — nothing to triage; `--dry-run` remains unexercised.
2. **Escalation-trigger vs pre-authorized autonomy:** the skill says to pause and ask Nick
   if >20% of fetches fail; this run had 100% failure but the session handoff had
   pre-ruled "chain-exhausted failures stay Blocked/deferred." The handoff overrode the
   skill correctly, but the skill has no language for handoff-level pre-authorization.
   Logged as a watch item, not a change (Rule 11 — first occurrence).
3. **The skill inherits wave-1's optimistic cooldown assumption implicitly** (retry =
   "plain re-run next session"). Candidate one-line Limitations note for
   `/transcript-fetcher` (alongside the existing 80+-batch lesson): IP-level blocks can
   span sessions within the same day; space retries by ≥1 calendar day.
