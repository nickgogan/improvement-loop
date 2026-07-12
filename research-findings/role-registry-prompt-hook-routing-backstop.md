---
name: 'Role Registry + Prompt-Submit Hook — Deterministic Routing Backstop When No Front-Door Agent Owns Intake'
summary: 'A UserPromptSubmit hook scores every incoming prompt against a role registry (personas, each with aliases, keywords, and an auto-load skill set) using deterministic whole-word token matching with stopword filtering, field-weighted scoring, and a verbatim-phrase bonus. It is a yes/no GATE with a threshold, not a ranked list: on a confident match it injects a short note naming the role and its auto-skills; on a weak match or any error it does nothing. Guarantees: reads the registry straight from disk (no server, no MCP handshake, no dependencies), always exits 0 (fail-open, never blocks a prompt). It is the runtime safety net for skill drift — even a brand-new skill that is not hub-aware still gets role-appropriate context surfaced at prompt time.'
implementation_notes: 'Nick''s explicit interest: worth considering for multi-agent systems where there is NO front-door agent — when no single agent owns intake, a deterministic prompt-time hook is the one place routing can still happen reliably, because it runs before any model reasoning and cannot itself drift (it is ~100 lines of dependency-free scoring). For the engine''s harnessed-agentic-OS direction this is a harness-layer primitive: the engine''s four IL agents are skill-selected today (implicit front door = the skill table), but the restructure program''s single-implicit-agent vision plus portable governance kernel needs exactly this shape — a disk-read registry mapping intent surfaces to auto-load asset sets, enforced by hook rather than by prompt discipline. Design details worth keeping verbatim: whole-word matching over substring (substring fires on incidental hits and injects noise), gate-not-ranking semantics (inject only above threshold, never a best-effort guess), and always-exit-0 fail-open (a routing aid must never become an availability risk). Nick confirmed (2026-07-12) the hook is worth keeping; the anonymized verbatim script is preserved at research-sources/raw/context-hub/hub-context-hook.mjs.'
category: Intent Engineering
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup + hook source))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: hook-based-transparent-memory-injection.md
  rel: same-problem
- file: hub-and-spoke-two-tier-skill-taxonomy.md
  rel: same-problem
- file: mcp-hub-skill-pack-serving-telemetry-middleware.md
  rel: extends
pipeline_status: raw
consumed_by: []
tags:
- userpromptsubmit-hook
- role-registry
- deterministic-routing
- fail-open
- multi-agent-intake
---

# Role Registry + Prompt-Submit Hook — Deterministic Routing Backstop

## What It Is

A ~100-line dependency-free Node script wired to the harness's `UserPromptSubmit` hook.
On every prompt it:

1. Reads the incoming prompt from stdin (JSON).
2. Loads `roles/registry.json` straight from disk — an array of personas, each with
   `id`, `title`, `personaPrompt`, `description`, `aliases`, `keywords`, and
   `autoSkills` (the skill set that should auto-load for that persona).
3. Scores the prompt against every role deterministically.
4. If the best score clears a threshold, injects a short `additionalContext` note naming
   the matched role, its auto-skills, and a pointer to the hub tool
   (`hub_role_resolve_skills`) for the full merged set. Otherwise: silent no-op.

It is explicitly a **backstop**, not the router: normal skill routing happens through
descriptions; this net catches prompts that routing misses — including prompts hitting
brand-new or non-hub-aware skills.

## Why It Matters

Plain English: in a system with many agents and skills, *someone* has to notice what kind
of work an incoming request is and pull in the right context. Usually that is a
front-door agent. When there is no front door — multiple entry points, background agents,
a growing skill roster where any given skill may be drift-stale — this pattern puts a
deterministic, zero-dependency routing check at the one chokepoint every prompt passes:
prompt submission. Because it is plain token scoring on a disk file, it cannot
hallucinate, cannot drift with model changes, costs no tokens when it doesn't fire, and
cannot take the system down (fail-open by construction).

## How It Works (scoring mechanics)

- **Tokenization:** lowercase, split on non-alphanumerics, keep tokens ≥3 chars; filter a
  ~40-word stopword list (the, and, for, use, make, fix, help, need, want, …).
- **Whole-word matching only** — substring matching would fire on incidental hits (e.g.
  "in" inside "testing") and inject noise. This is the stated design rationale.
- **Field-weighted, highest-field-wins:** each significant term scores once, at the
  highest-weight field it appears in — role `id` = 5, `title` = 4, `personaPrompt` = 3,
  tags (aliases + keywords + autoSkills) = 3, `description` = 2.
- **Phrase bonus:** any curated multi-word alias/keyword appearing verbatim in the prompt
  adds +5.
- **Gate, not ranking:** the single best role must clear a threshold (default 10,
  env-tunable via `HUB_HOOK_THRESHOLD`; registry path via `HUB_CONTEXT_DIR`) or nothing
  is injected. There is no "closest match" fallback.
- **Fail-open guarantees:** registry missing/corrupt, non-JSON stdin, prompts under 4
  chars, any thrown error → silent no-op; the script always exits 0 and never blocks a
  prompt (never exit 2). No server dependency, no MCP handshake, no npm packages — fast
  cold start on every prompt.

## How It Could Fail

- **Registry staleness.** The net is only as good as `roles/registry.json`; roles that
  lag the actual skill roster inject outdated auto-skill lists (mitigated upstream: the
  registry is generated by the hub's sync pipeline).
- **Threshold tuning.** Too low → noisy injections on unrelated prompts; too high → the
  backstop never fires. A fixed default (10) assumes curated aliases/keywords.
- **Single-best-role assumption.** Prompts spanning two roles inject only one; the
  gate-not-ranking choice trades recall for precision deliberately.
- **English-token bias.** Tokenization (≥3-char Latin alphanumerics, English stopwords)
  degrades on other languages and heavy code-content prompts.
