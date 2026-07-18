---
title: "B — Framework survey: OpenClaw memory architecture"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-16"
---

# OpenClaw — Memory Architecture Dossier

Cross-framework survey input for the engine's E1 memory-architecture spec. Research
conducted 2026-07-16 via Perplexity deep research + WebSearch/WebFetch against
OpenClaw's own docs, a mem0.ai integration writeup, a Chinese technical deep-dive, and
practitioner sources (Hacker News, GitHub issues, blogs). Internal grounding: IL
watched-library entry `watched-libraries/openclaw.md` and structural analysis
`watched-libraries/analysis/openclaw-analysis.md` (both dated ~2026-04-08, version
v2026.4.5 — see currency note below).

---

## 1. Snapshot

**What it is.** OpenClaw is Peter Steinberger's open-source personal AI assistant —
"any OS, any platform," ~346K GitHub stars as of the internal analysis (April 2026),
most-starred project on GitHub at that time. Naming history: **Clawdbot** →
(Anthropic objected to the name's similarity to "Claude") → **Moltbot** → (Steinberger
renamed again, reportedly because he liked "OpenClaw" better) → **OpenClaw**, the
current name. It is a large, plugin-centric TypeScript production codebase (81% TS,
13,216 files per the internal repo analysis), not a markdown-as-code framework — memory
files are a thin but load-bearing layer over a much larger runtime (gateway, ~100
bundled extensions, native iOS/Android/macOS apps).

**Memory scope.** Personal-assistant memory across arbitrary channels (DM, group chat,
voice, etc.) for a single end user per agent instance. Explicitly designed around a
"file-first" philosophy: Markdown files in the agent's workspace are the *canonical*
source of truth; SQLite + embeddings are an acceleration/index layer over them, not the
store of record.

**Major currency event (post-dates internal KB).** On 2026-02-14/15, Steinberger
announced he is joining **OpenAI** to "drive the next generation of personal agents"
(Sam Altman, X, 2026-02-15). OpenClaw itself is being placed into a non-profit
**OpenClaw Foundation** for independent stewardship, with OpenAI continuing to support
it as an open-source project (TechCrunch, Forbes, CNBC, Euronews — all 2026-02-15/16).
This is a governance discontinuity the internal analysis (dated 2026-04-08, i.e.
*after* the OpenAI move but not reflecting it) does not mention — worth flagging back
to the watched-library entry.

**Currency of this dossier.** External sources confirm activity through at least
release **2026.6.11** (release notes) and a **2026.4.9/4.10** cycle that took Dreaming
from beta to GA (2026-04-06, "after six months of testing across thousands of
operators," per a dev.to/Blink summary of the release). The internal
`openclaw-analysis.md` (evaluated 2026-04-08 at v2026.4.5) is now roughly 3 months
stale relative to today (2026-07-16) and predates the OpenAI/Foundation transition,
the Dreaming GA promotion to default-on, and the February security-incident wave
described in §4. Prioritize this dossier's external findings over the internal
analysis where they conflict; the internal analysis's structural inventory (skills
count, plugin count, context-file map) is still reasonably reliable since that layer
changes more slowly than memory internals.

---

## 2. Memory model by type

### Working / short-term memory
- **Storage substrate:** the active conversation/session transcript, plus
  `memory/YYYY-MM-DD.md` daily-note files under the agent's workspace (default
  `~/.openclaw/workspace`).
- **Write path:** the agent (LLM) appends to the current day's file during a session as
  events, decisions, and context arise — described as a running journal, not a curated
  summary. A distinct **automatic memory flush** mechanism fires as a silent internal
  turn when token usage approaches the context-window limit, instructing the agent to
  write important details to the daily note *before* compaction runs
  (`compaction.memoryFlush.enabled`, on by default per docs.openclaw.ai/concepts/memory).
- **Injection/recall:** today's and yesterday's daily-note files auto-load at the start
  of a new session (`/new` or `/reset`). Older daily notes are **not** injected
  wholesale — they're indexed into the SQLite hybrid store and pulled on demand via the
  `memory_search` (semantic + BM25 keyword hybrid) and `memory_get` tools.
- **Consolidation/reflection:** daily notes are the *input* to Dreaming (see semantic
  memory below), not consolidated in place.
- **Decay/forgetting:** none described for daily notes themselves — they persist on
  disk indefinitely; only their presence in the *injected* context decays (only
  today/yesterday auto-load).

### Episodic memory (full session transcripts)
- **Storage substrate:** timestamped transcript files, e.g.
  `sessions/YYYY-MM-DD-<slug>.md`, with an LLM-generated descriptive slug.
- **Write path:** automatic at session boundary — OpenClaw saves the outgoing
  conversation to a transcript file when a new session starts.
- **Injection/recall:** not auto-loaded; recalled only via semantic search
  (`memory_search`) or targeted retrieval when the agent or a plugin specifically
  queries past sessions. Functions as a fallback/reconstruction layer after
  compaction or reconnects — release 2026.6.11 notes specifically call out
  "transcript repair" and keeping compaction/memory/QMD-backed memory aligned with the
  intended conversation state through reconnects and upgrades.
- **Consolidation:** transcripts are one of the inputs the Dreaming "light" phase reads
  (alongside daily notes), described as redacted for privacy before being staged as
  dreaming candidates.
- **Decay:** none explicit; same "index-only, not injected" pattern as daily notes.

### Semantic memory (durable facts/preferences — the "long-term memory" layer)
- **Storage substrate:** `MEMORY.md` — a single curated file per agent, explicitly
  *not* a raw transcript or exhaustive archive. Backed by a SQLite database at
  `~/.openclaw/memory/{agentId}.sqlite` holding text chunks, line ranges, and
  serialized embeddings, managed by a `MemoryIndexManager` singleton class (per a
  mem0.ai integration writeup and a Chinese technical deep-dive). Alternative backends
  exist as swappable plugins: a `mem0`-based plugin (`@mem0/openclaw-mem0`, with
  session-scoped vs. user-scoped memory via `run_id`/`userId`) and a "QMD-backed
  memory" plugin referenced in 2026.6.11 release notes.
- **Write path:** three mechanisms layered together — (1) **explicit user command**
  ("remember that I prefer TypeScript"); (2) **agent-initiated distillation**, where a
  generated workspace-instruction/heartbeat flow periodically reviews daily notes and
  promotes recurring, consistently-relevant signals into `MEMORY.md`, pruning stale
  entries; (3) **Dreaming's Deep phase** (see consolidation below), which promotes
  scored candidates automatically.
- **Injection/recall:** `MEMORY.md` loads at the start of every **private** session by
  default (bootstrap injection). Per the deep-dive source and corroborated by the
  internal KB's `six-file-workspace-taxonomy.md` finding, `MEMORY.md` is explicitly
  **not** injected into group-chat/shared sessions — a deliberate privacy boundary
  (daily notes are considered sufficient context there). If the file exceeds a
  configured "bootstrap file budget," the *injected copy* is truncated while the
  on-disk file stays intact — a soft degrade rather than a hard cutoff. Beyond
  bootstrap injection, `MEMORY.md` content is also reachable via `memory_search`.
- **Consolidation/reflection — "Dreaming":** an optional (opt-in in earlier releases,
  **GA and default-on as of v2026.4.5 / 2026.4.9-4.10**, per WebSearch results) background
  process run in three cooperative phases per sweep, **light → REM → deep**:
  - *Light*: scans recent conversations/daily notes/redacted transcripts, dedupes
    signals, stages candidates. No write to `MEMORY.md`.
  - *REM*: builds theme/reflection summaries across recent traces (pattern extraction,
    not fact extraction). No write to `MEMORY.md`.
  - *Deep*: scores every candidate on six weighted signals — Relevance (0.30),
    Frequency (0.24), Query diversity (0.15), Recency (0.15), Consolidation (0.10),
    Conceptual richness (0.06) — and promotes only candidates clearing **all three**
    threshold gates (minScore 0.8, minRecallCount 3, minUniqueQueries 3) into
    `MEMORY.md`. Writes a `## Deep Sleep` entry to `DREAMS.md` and optionally a fuller
    report under `memory/dreaming/deep/YYYY-MM-DD.md`.
  - Human-reviewable surface: **`DREAMS.md`**, a "Dream Diary" of phase summaries and
    narrative reflections, appended to whenever a phase accumulates enough material.
  - Internal machine state lives in `memory/.dreams/` and phase report files, separate
    from the diary.
- **Decay/forgetting/supersession:** the promotion thresholds function as the write
  gate (nothing weak gets in); the *distillation* flow removes stale `MEMORY.md`
  entries during its periodic pass, but no explicit decay/expiry function or
  contradiction-resolution mechanism is documented for entries already promoted —
  matches the internal `dreaming-memory-consolidation.md` finding's flagged failure
  mode ("threshold miscalibration," "cold start problem").

### Procedural memory
- Not a dedicated first-class store. The closest analogues are informal:
  a community-convention `learnings.md` file (not part of the default template, used
  ad hoc per a "My OpenClaw Broke" troubleshooting video to hold "rules learned from
  mistakes"), and the 53 `SKILL.md`-based skills + Plugin SDK, which encode *procedure*
  as static, versioned, code-adjacent artifacts rather than memory that accrues from
  experience. OpenClaw does not appear to have an experience-derived "here's how I
  learned to do X" memory type distinct from semantic `MEMORY.md` facts — a gap also
  flagged as a "Potential Improvement" in the internal KB's dreaming finding (no
  contradiction-detection or procedural column).

### Identity / persona layer (not one of the four canonical types, but load-bearing)
`SOUL.md` (personality/voice/values — "if the agent sounds bland, hedgy, or corporate,
this is the file to adjust," per docs.openclaw.ai) and `USER.md` (user profile: name,
pronouns, timezone, notes) are both injected at every normal session start alongside
`MEMORY.md`. They shape *how* the agent writes and phrases memory rather than storing
memory content themselves — matches the internal KB's six-file-workspace-taxonomy
finding.

---

## 3. Lifecycle trace — one memory item end-to-end

Trace: user tells the agent, mid-conversation, "I prefer TypeScript over JavaScript for
new projects."

1. **Capture (working memory):** the agent appends the statement to today's
   `memory/2026-07-16.md` daily note as part of its normal session-logging behavior
   (or, if the session runs long, this happens specifically during the pre-compaction
   memory-flush turn rather than being lost to summarization).
2. **Indexing:** the daily-note file is chunked, embedded, and written into the
   per-agent SQLite index (`~/.openclaw/memory/{agentId}.sqlite`) by
   `MemoryIndexManager`, making the statement retrievable via `memory_search` even
   before any promotion happens.
3. **Candidate staging (Dreaming — Light phase):** on the next background dreaming
   sweep, the Light phase reads the daily note, dedupes it against other signals, and
   stages it as a promotion candidate — no `MEMORY.md` write yet.
4. **Scoring and gating (Dreaming — Deep phase):** the candidate is scored on the six
   weighted signals. A stated, repeated preference like this scores well on Relevance
   and (once it recurs across sessions) Frequency/Recall count/Unique queries. If it
   clears minScore 0.8, minRecallCount 3, and minUniqueQueries 3, it promotes.
5. **Promotion / write to long-term memory:** the Deep phase appends the distilled fact
   to `MEMORY.md` (e.g., "Prefers TypeScript for new projects") and logs a `## Deep
   Sleep` diary entry to `DREAMS.md` for human review. Alternatively (outside
   Dreaming), the same promotion can happen via the periodic heartbeat-driven
   distillation pass, or immediately if the user explicitly said "remember that."
6. **Recall/injection in a future session:** on the next **private** session, `MEMORY.md`
   loads automatically at bootstrap — the preference is present in context without any
   retrieval call. In a group-chat session, `MEMORY.md` does not load; the preference
   is only reachable if a `memory_search` call happens to surface it.
7. **Long-run fate:** the entry persists indefinitely unless a later distillation pass
   judges it stale (no explicit decay timer) or a contradictory statement triggers a
   human/agent edit — no automated contradiction-detection is documented, so
   conflicting entries can coexist until manually or heuristically cleaned up.

---

## 4. Practitioner sentiment

**Works, per practitioners/docs:**
- File-first, git-diffable memory is repeatedly cited as the core value proposition —
  users can open, edit, and audit exactly what the agent "knows" (docs.openclaw.ai,
  undated but current as of 2026-07; mem0.ai integration blog, 2026).
- Dreaming's graduation from beta to GA in **v2026.4.5 (2026-04-06)** is described as
  having been tested "across thousands of operators" over six months before going
  default-on (dev.to/Blink summaries, 2026-04).
- Release **2026.6.11** claims specific reliability fixes aligning "sessions,
  compaction, memory, and QMD-backed memory" through reconnects/upgrades/transcript
  repair — i.e., OpenClaw's own team was still actively patching memory-continuity bugs
  as of June 2026.

**Doesn't work / breaks, dated practitioner claims:**
- **"OpenClaw's memory is unreliable, and you don't know when it will break"** — HN
  submission (nishantsoni.com), ~168 points, posted roughly **mid-April 2026** ("3
  months ago" relative to 2026-07-16). Commenter `Gareth321`: RAG-style retrieval "is
  like putting a 1990s Honda Civic engine into a Ferrari" — argues weight-based
  learning, not retrieval, is what's actually needed. Commenter `operatingthetan`:
  reports the agent "randomly edit[s] its own config, uses incorrect json keys and then
  the whole thing is dead," or "blows through its context and doesn't know to compact."
  Commenter `loehnsberg` frames the fleet of agents as suffering "anterograde amnesia,"
  requiring constant human oversight. Commenter `ambewas`: true single-exposure
  learning would need an architecture current LLMs don't have — memory can't
  consolidate the way human sleep does (ironic given OpenClaw's own "Dreaming"
  branding).
- **"OpenClaw's Memory Is Broken. Here's how to fix it"** — Daily Dose of Data Science
  blog, published **2026-02-17**. Core claim: "It remembers everything you tell it but
  understands none of it" — the semantic-embedding retrieval layer can't reason about
  *relationships* between stored facts (e.g., knowing "Alice" and "auth team" exist
  doesn't let it infer Alice manages the auth team). Proposes bolting on **Cognee**
  (open-source knowledge-graph engine) as an augmentation layer rather than a
  replacement.
- **GitHub issue #43747, "[Bug]: Memory management is in chaos"** — opened
  **2026-03-12**, still **open** as of the fetch. Reporter and two colleagues on the
  same OpenClaw version (2026.3.8) each get different memory behavior: one on SQLite
  (`~/.openclaw/memory/main.sqlite`), one on daily markdown files, one with **no memory
  retention at all**. Reporter: "I never see any of our memory is managed in same way,"
  requesting "a rewrite on memory management session, make strict definition on this
  thing." Labels applied by maintainers indicate this was tagged as a regression with
  "session-state corruption risk" and flagged as needing a product decision, not just a
  patch — i.e., the maintainers themselves treated this as an architectural gap, not a
  simple bug.
- **"OpenClaw had a rough week"** — HN thread, ~**2026-05-08** ("69 days ago" relative
  to 2026-07-16). Practitioner-reported churn: one user switched to "Hermes Agent" and
  called it "night and day how much more stable" than OpenClaw; another switched to
  "picoclaw" because OpenClaw "was too slow," praising the alternative as "reliable,
  tiny, fast." General thread sentiment criticized the codebase as effectively
  "vibe coded," citing hundreds of thousands of lines of code and a backlog of stale
  PRs as evidence of thin review bandwidth — relevant context for trusting any single
  memory-subsystem claim in the docs, since the surrounding engineering process was
  publicly questioned around the same time.
- **Plugin ecosystem fragmentation:** a GitHub issue against a third-party memory
  plugin (`MemTensor/MemOS-Cloud-OpenClaw-Plugin#109`, 2026, version 2026.4.x) reports
  the plugin isn't recognized under `plugins.slots.memory` — evidence that the
  "pluggable memory backend" design (mem0, QMD, MemOS, etc.) creates real integration
  breakage in practice, not just theoretical flexibility.

**Security/quality critiques, dated:**
- **February 2026 wave of security research** (multiple outlets: Imperva, Snyk,
  HiddenLayer, Giskard, an arXiv paper "Taming OpenClaw," and independent researcher
  writeups) documented prompt-injection paths that specifically target the memory
  system: (a) an attacker instructing the agent (directly, or indirectly via a
  poisoned web page) to "save the API key in memory," landing secrets in plaintext in
  `MEMORY.md` where malicious skills are specifically designed to look for them
  (API Stronghold, "OpenClaw 2026 Security Crisis," 2026-02); (b) **memory-based
  persistence** — an attacker who gets the agent to write a malicious instruction into
  `SOUL.md` makes that instruction "part of the agent's permanent operating system,
  surviving restarts and chat resets" (multiple outlets, Feb 2026); (c) a documented
  case of indirect injection writing an attacker-controlled instruction into
  `HEARTBEAT.md`, causing the agent to silently await commands from an attacker C2
  server (same wave); (d) Snyk's "280+ Leaky Skills" research (2026) found that a large
  fraction of the ClawHub skill ecosystem exposed API keys/PII, which is adjacent to
  but compounds the memory-exfiltration risk since skills can read workspace memory
  files. This is the same February window as the RCE bug covered by The Hacker News
  ("OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link,"
  2026-02) and overlaps with the timing of Steinberger's OpenAI move — a rough month
  for the project on both the governance and security fronts simultaneously.
- The internal KB's own `openclaw-analysis.md` (2026-04-08) independently corroborates
  the group-chat isolation as a deliberate mitigation ("MEMORY.md security: only loaded
  in DM sessions, never in group chats") — but external research shows that mitigation
  doesn't cover the indirect-injection paths above, which operate through *any*
  channel that can get content in front of the agent (a poisoned webpage, a malicious
  skill, a crafted message), not just group chats.

---

## 5. Verdict

**Strengths (transferable):**
- **File-first canonicity with an index-as-accelerator, not index-as-store.** SQLite +
  embeddings are explicitly downstream of the Markdown files, never authoritative. This
  is the same posture DD-territory in this engine already favors (markdown+git as
  system of record) — OpenClaw is independent validation that a production, VC-funded-
  adjacent, hundred-thousand-star project converged on the same principle at much
  larger scale.
- **Explicit visibility-scoping of durable memory** (`MEMORY.md` in DMs only, not group
  chats) is a concrete, low-cost pattern this engine's single-operator context doesn't
  strictly need (there's no multi-channel exposure) but which generalizes well as a
  template for *any* future multi-consumer surface: gate what loads by audience, not
  just by content sensitivity classification.
- **Named, human-reviewable consolidation output (`DREAMS.md`)** is a genuinely good
  idea independent of the Dreaming mechanism's own reliability problems: a diary of
  *why* something got promoted to long-term memory is cheap to produce and gives a
  human a lightweight audit trail without requiring them to approve every write.
- **Pre-compaction flush-to-disk** (write-before-you-forget, triggered near the context
  limit rather than after the fact) is a directly reusable pattern for any harness that
  does its own compaction — capture the "about to lose this" moment explicitly rather
  than hoping the summarizer preserves what matters.

**Failure modes (grounded in dated practitioner evidence, §4):**
- **Retrieval without relational reasoning.** The single most consistent complaint
  (dailydoseofds 2026-02-17, HN 2026-04 thread) is that semantic-embedding search finds
  *similar text*, not *related facts* — the system can hold "Alice" and "auth team" as
  separate memories without ever inferring the relationship. This is a real ceiling on
  the value of a pure markdown+vector-index approach and a concrete argument for
  keeping recall paths simple (grep/frontmatter-filter, as this engine already does)
  rather than reaching for embeddings to solve a problem embeddings don't solve.
- **Unstated/undocumented gating produces divergent behavior across identical
  installs** (GitHub #43747, 2026-03-12, still open) — three users on the same version
  got three different memory architectures (SQLite / markdown-daily-files /
  no-retention). For a spec-writing exercise, the lesson is sharp: the write and
  promotion paths must be **one deterministic path**, documented precisely enough that
  "what gets written when" isn't emergent from feature-flag combinations.
- **Consolidation gates can silently starve memory.** Dreaming's three threshold gates
  (score/recall-count/unique-queries) mean a true-but-rarely-repeated fact never
  promotes — matches the internal KB finding's flagged "cold start problem" and
  "threshold miscalibration" risks. Any promotion-gate design this engine adopts should
  have a manual override (explicit "remember this" bypasses gates) — OpenClaw does
  appear to have this via explicit user commands, which is worth preserving as a
  minimum bar.
- **Memory is an attack surface, not just a storage question.** The February 2026
  security wave shows durable memory files becoming (a) a secrets-exfiltration target
  and (b) a **persistence mechanism for injected instructions** (`SOUL.md`,
  `HEARTBEAT.md` overwrite attacks survive restarts). For a human-gated, single-operator
  engine this is lower-stakes (no adversarial multi-tenant exposure, no autonomous
  execution of untrusted content by default) — but the general principle transfers:
  any file that is both (1) auto-loaded into every session's context and (2)
  writable by the agent itself is a durable-persistence channel, and any pipeline that
  lets *external, untrusted content* (a fetched webpage, a skill's output) flow into
  agent reasoning should be treated as a potential writer to that channel, gated the
  same way code changes are gated.
- **Codebase/process trust matters as much as the memory design on paper.** The "rough
  week" thread (~2026-05-08) reflects a broader skepticism about review depth on a
  fast-moving, large, plugin-heavy codebase — a reminder that a memory *architecture*
  described in docs is only as trustworthy as the engineering discipline behind its
  implementation. Not directly transferable as a design lesson, but relevant caveat
  weight: treat OpenClaw's documented behavior as aspirational/intended rather than
  verified-in-practice without independent confirmation (which is exactly what this
  dossier tried to do by weighting practitioner reports alongside the docs).

**Net transferability for this engine (markdown+git, single-operator, human-gated):**
High on the *file-first-canonical, index-as-accelerator* principle and the
*human-reviewable consolidation diary* pattern (both cheap, both compatible with
existing DD-grounded practice). Low-to-moderate on the *Dreaming three-phase
autonomous promotion* mechanism itself — its own practitioner record shows real
reliability and calibration problems, and this engine's human-gate discipline (DD-2 /
Hard Constraint 2, no autonomous modification of live systems without review) is
already stricter than what Dreaming assumes; an engine-native consolidation step should
stay human-approved-per-batch rather than adopting OpenClaw's autonomous threshold-gate
promotion outright. The security lesson (auto-loaded + agent-writable = persistence
channel) is worth carrying into E1 as a design constraint even though this engine's
threat model is currently much narrower.
