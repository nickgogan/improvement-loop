---
name: link-intake
description: >-
  Triage a LINKS.md batch — Nick's rolling link queue — into one gated verdict
  per link (ADD / ENHANCE / KB-ONLY / REJECT). Use when Nick supplies a new
  LINKS.md batch, asks to "run link intake", "triage the link queue", or
  "process LINKS.md". Orchestrates dedup, transcript prefetch via
  /transcript-fetcher, topical triage-subagent fan-out, and a single gated
  triage report. Changes nothing beyond the report and transcript cache until
  Nick accepts the verdicts.
allowed-tools: Read, Bash, Agent, Write, Edit, Skill
argument-hint: "[--dry-run] [path to links file, default LINKS.md at engine root]"
---

# Link-Intake Triage Orchestrator

Promoted from `operations/references/link-intake-protocol.md` after three stable-shape runs
(pilot + run 2, 2026-07-11; run 3 full sweep, 2026-07-12 — Nick-gated promotion, option 1).
The run reports in `operations/research-reports/*link-intake-triage*.md` are the audit trail
and shape reference.

## When to use

- Nick supplies a new LINKS.md batch and asks to process/triage it.
- Consumer phrasings: "run link intake", "triage LINKS.md", "process the link queue",
  "what should we do with these links".
- Do NOT use for: a single ad-hoc URL mid-conversation (route directly to `/source-triage`
  or `/research-query`); sources already in the KB (that's `/research-loop` Pass 2);
  watched-library upstream checks (`/watch-upstream`).

## Procedure

1. **Parse and dedup the queue** (Read, Bash). Read the links file (default
   `systems/improvement-loop/LINKS.md`). Canonicalize URLs (for YouTube: extract the
   11-char video ID; strip `t=`/`pp=` params). Drop in-batch duplicates. Then dedup
   against the LIVE corpus — never a snapshot index (pilot lesson):
   - `rg` the URL / video ID over `research-sources/` frontmatter `url:` fields;
   - check `watched-libraries/*.md` for already-tracked repos (run-2 lesson);
   - check watched-blogs post logs for posts from tier-1 watched blogs (run-2 lesson).
   Already-ingested links get verdict `REJECT (already in KB)` with the evidence path —
   no subagent cost.
2. **Video links — fetch transcripts FIRST, probe second** (Skill: `/transcript-fetcher`).
   Fetch missing transcripts before running any bulk probe: an 80+ video probe+fetch burst
   in one session trips YouTube's IP rate limit (HTTP 429, run-3 lesson). Fetch in chunks
   of ≤25 videos with a pause between chunks (cost control before, not after, the burst).
   Present the probe cost table (durations, est. tokens, fetched/new) in the report. Links
   whose transcripts exhaust the fetcher's fallback chain get verdict
   `REJECT (defer — transcript blocked)` and stay in the links file as the retry backlog —
   per the transcript-first rule, do not triage a video from its title/metadata alone.
   **`--dry-run` stops here:** dedup + probe cost table only — no fetches, no fan-out, no
   report file; present the preview in conversation.
3. **Classify non-video links** (Read, Bash). Cheap classification per link (URL shape +
   title + README head): SKILL / REPO-SKILLBEARING / REPO-FRAMEWORK / REPO-DEMO /
   PAPER / ARTICLE. Ambiguous cases classify to the cheaper track with a note. All-video
   batches skip this step (single class).
4. **Fan out triage subagents** (Agent, parallel). Group links into topical batches
   (~6–12 links each) so recency-weighting and cluster dedup happen inside one context.
   Same-topic near-duplicates must land in the same batch — if a cluster is split, add an
   orchestrator reconciliation pass before the report. Each subagent prompt must include:
   - a **read-only constraint**: triage subagents read transcripts and grep the KB; they
     must not Write/Edit any file — their verdicts return as final-message text only
     (monotonic narrowing of the run's own envelope);
   - the verdict rubric (below) — exactly one verdict per link;
   - instruction to dedup against the live corpus via `rg` on `research-findings/` and
     `research-sources/` — never a passed-in index;
   - the **recency-weighting rule**: within a same-topic cluster the newest source's
     framing leads; older near-duplicates are `REJECT (covered by <ID>)` unless they
     carry unique patterns;
   - the **measured-experiment heuristic** for news/commentary content: keep only if it
     contains someone's quantified experiment or decision-relevant numbers;
   - the **roster escalation question** per link: does the content define a procedure an
     engine skill could embody, or a tool an engine skill should adopt? Check overlap
     against the engine roster (`systems/improvement-loop/.claude/skills/`), workspace
     roster (root `.claude/skills/`), AND harness built-ins before proposing ADD/ENHANCE;
   - current engine priorities (read `PROGRESS.md` Current Focus + Nick's Prioritizaton
     before composing prompts);
   - output shape: per-link verdict + plain-English rationale (why-it-matters-for-us
     first), novel-pattern estimate for KB-ONLY, dedup hits, roster-escalation answer.
5. **Assemble the report** (Write). As each batch returns, append its verdicts to a
   session-scratch checkpoint file so a crash mid-fan-out loses one batch, not the run.
   If a subagent returns malformed or incomplete verdicts, re-dispatch that batch once;
   on second failure, mark its links `defer — triage failed` and continue. Then write one
   report per run: `operations/research-reports/{date}-link-intake-triage.md`. Sections:
   batch mechanics (dedup/fetch outcomes), verdict summary tables, per-link rationales,
   Blocked/defer section, follow-up queue (each item separately gated), protocol
   observations, probe cost-table appendix. Frontmatter via block scalars (DD-114);
   validate with `operations/kb-maintenance-scripts/validate_frontmatter.py`. Also record
   per-channel calibration observations (authority hit-rates) — they feed the authorities
   registry.
   **Escalation trigger:** pause and ask Nick mid-run if >20% of fetches fail, if dedup
   evidence is contradictory (a link both "already ingested" and "novel"), or if two
   subagents return conflicting verdicts for the same link.
6. **Present the Nick gate.** Closing summary: verdict counts, cost table, Blocked list,
   follow-up queue. **Stop here on `--dry-run` or absent explicit acceptance.**
7. **On Nick's acceptance only** (Edit): remove accepted-verdict links from the links
   file; keep **all `defer — *` links** regardless of reason (they are the retry queue —
   transcript-blocked, paywalled, triage-failed alike). The report
   is the audit trail. Execute nothing else: every ADD/ENHANCE is a separate per-link
   Nick gate (Rule 10 — adopted/modified skills go through `/design-skill` /
   `/assess-skill` in fresh context); KB-ONLY items flow to `/research-loop` Pass 2 with
   its existing gates.

## Verdict rubric — exactly one per link

| Verdict | Criteria | Metadata recorded |
|---|---|---|
| **ADD** | no roster overlap + real capability + relevant | consumption mode, source URL, upstream ref, authoring-model version if discoverable, proposed placement (DD-109) |
| **ENHANCE** | overlaps an existing skill AND carries deltas ours lacks | target skill + the specific deltas |
| **KB-ONLY** | not roster material, but pattern-dense or track-worthy | intake path: research-source / watched-library (+`/repo-analyzer`) |
| **REJECT** | none of the above | one-line reason; `defer — [reason]` if inaccessible so it can re-queue |

## Output shape

- The triage report file in `operations/research-reports/` (protocol format above).
- Fetched transcripts in the transcript cache (via `/transcript-fetcher`).
- A closing summary in conversation presenting the Nick gate.
- After acceptance: the links file updated (triaged links removed, deferred links kept).

## Boundary conditions

- **Termination:** success = report written and Nick gate presented; the post-acceptance
  clearance edit is the only follow-through. Abort = links file missing or empty (report
  "queue empty", change nothing).
- **Out of scope:** Pass 2 extraction (`/research-loop`), source/finding creation,
  executing ADD/ENHANCE verdicts (per-link Nick gates via `/design-skill`), watched-library
  registration, authority-registry writes. This skill's only writes are the report,
  transcripts via the fetcher, and the post-gate links-file clearance.
- **Safety-critical?** Yes (Write/Edit/Bash/Agent). HITL gates: (a) the run itself is
  read-only beyond the report + transcript cache, and triage subagents carry an explicit
  read-only constraint; (b) the links file is edited ONLY after Nick explicitly accepts
  the verdicts in conversation — never in the same breath as the report; (c) no verdict
  is executed by this skill. Enforcement is prompt-layer by design (structural `ask`
  rule declined per Nick's 2026-07-12 no-prompts permissioning ruling); accepted
  residual risk, mitigated by the links file being git-tracked and reversible.

## Cross-references

- Origin protocol (superseded by this skill; retained as history):
  `operations/references/link-intake-protocol.md`
- Run reports (shape reference): `operations/research-reports/2026-07-11-link-intake-triage.md`,
  `operations/research-reports/2026-07-11-link-intake-triage-run2.md`,
  `operations/research-reports/2026-07-12-link-intake-triage.md`
- All paths are engine-relative (`systems/improvement-loop/`); the default links file is
  `LINKS.md` at the engine root
- Composed skills: `/transcript-fetcher` (fetch + probe + Blocked convention),
  `/source-triage` (single-source deep triage), `/research-loop` (Pass 2 extraction)
