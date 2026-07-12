---
title: "Agent Reflections-to-Proposals Architecture"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "owner"
stage: "draft"
source_dd:
  - "DD-29"
  - "DD-52"
  - "DD-82"
  - "DD-86"
related_proposals:
  - "governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md"
related_design_notes: []
tags:
  - "design-note"
  - "reflections"
  - "proposals"
  - "agent-architecture"
  - "owner"
  - "self-improvement"
aliases:
  - "Agent reflections architecture"
  - "Reflections-to-proposals pipeline"
  - "Self-reflection architecture"
---

# Agent Reflections-to-Proposals Architecture

**Status:** Design note. Deliberative spec precursor to a DD proposal and an Owner skill. Nick gates both downstream artifacts.

**Prompted by:** Nick's session-51 annotation on the Codifier agent-constitution edit proposal (2026-04-21) — *"each agent will have their own design-time considerations... reflect on its vision, mission & purpose, values, constitution, effectiveness, efficiency, available skills, available references... and on its reports + activity over a period of time and derive reflections such as: what honestly went well, what went poorly, what help it could use... These reflections are later used as inputs to generate proposals. Accepted proposals become backlog items. Reflections should be private and owned by the agent, in its folder. Eventually create a prompt that will be referenced by each agent when it comes time to solicit proposals... Owner agent owns this. Agents are also free to put forward proposals they believe would be valuable."*

**Scope:** IL-internal. Each of the four IL agents (Owner, Researcher, Codifier, Librarian) gets a reflections pathway. Cross-system generalization (Household OS, Claude Build) is a follow-on concern, not this note's focus.

**Why a design note and not a DD proposal:** Nick's direction — *"Let's start with a design note and then lets work on the shape and DD."* Writing a governance rule before the mechanism is specified is the wrong order. This note produces the shape; the DD proposal follows.

---

## 1. Purpose

Today, IL self-improvement happens in two informal channels:

- **Consumer-to-producer feedback** (`feedback/`): another agent or Nick identifies a gap in a producer's output and files a feedback item. The Owner triages via `/process-feedback`.
- **Ad-hoc Owner observation**: session SL entries capture "what went well / what went poorly" loosely inside the narrative. Nick or the Owner surface patterns manually.

Neither channel is producer-driven. An agent has no standing mechanism to reflect on its own state and surface improvements from the inside. The Codifier has no place to say *"my own Boundaries section is contradicted by my own Output Artifacts — I'm the one best positioned to notice this, but I have no artifact shape for surfacing it."* The Researcher has no place to say *"my dimension registry drifts against the findings I'm extracting; I feel the friction every session, but I have no channel to raise it."*

The reflections-to-proposals architecture closes this gap. It gives each agent:

1. **A private design-time space** to reflect on itself over time.
2. **A structured route from reflection to proposal**, triggered periodically by the Owner (with Nick's gate) or initiated ad-hoc by the agent itself.
3. **A downstream path** where accepted proposals become IB items.

The architecture complements `feedback/` (consumer → producer) with a producer-on-self channel. Both stay — they solve different problems.

---

## 2. Artifact taxonomy

Five artifact classes participate. Three are new; two exist.

| Artifact | Shape | Home | Owner | Status |
|---|---|---|---|---|
| **Reflection** *(new)* | Agent self-assessment over a period | `agents/{name}/reflections/` | Agent-private | **This note defines** |
| **Focus areas** *(new)* | Per-round Owner-decided lens + Nick-gated | Ephemeral (in skill run) or `operations/` | Owner authors; Nick gates | **This note defines** |
| **Proposal** *(existing)* | Governance-rule or system change request | `governance/proposals/` | Author-agent; Nick gates | Existing |
| **IB item** *(existing)* | Tracked work | `project-management/implementation-backlog/` | Owner files after proposal accepted | Existing |
| **Solicitation run record** *(new)* | SL-shape record of a reflection round | `operations/system-log/` (SL entry) | Owner | **This note defines** |

Reflections are the input. Proposals are the output. Focus areas and the solicitation-run record wrap the flow.

---

## 3. The zones, clarified

This architecture extends — doesn't contradict — the four-zone DD proposal (pending). It adds a sixth zone: **agent-private design-time** inside each agent folder.

| Zone | Purpose | Example artifact | Audience | Mutability |
|---|---|---|---|---|
| `project-management/design-decisions/` | Ratified rules | DDs | Nick-filed; everyone reads | Immutable (DD-44) |
| `project-management/implementation-backlog/` | Tracked work | IB items | Owner files; executor reads | Mutable |
| `project-management/design-notes/` | Shared deliberative specs | This note; Librarian read-contract | Any agent authors; any agent reads | Draft → accepted → superseded |
| `governance/` (root) | Active ratified rules | `agent-rules.md`, `pipeline-rules.md` | Owner writes; everyone reads | Mutable via `/translate-governance` |
| `governance/proposals/` | Owner-authored governance proposals | Tracking-mechanism proposals, DD proposals | Owner writes; Nick gates | Proposed → accepted/rejected |
| **`agents/{name}/reflections/`** *(new)* | **Agent self-reflections over time** | **"What went well for the Codifier this week"** | **The agent itself (private); Owner reads during solicitation** | **Append-only over time** |

The new zone is intentionally agent-local. The fractal pattern (DD-52) already permits each agent-directory to grow subdirectories for its own needs. `reflections/` is one such subdirectory; the pattern absorbs it natively.

---

## 4. Reflection artifact shape

### 4.1 File layout per agent

```
agents/
  owner/
    agent.md
    reflections/
      _index.md                          # catalog of reflections
      2026-04-21-owner-reflection.md     # one file per reflection event
      2026-05-15-owner-reflection.md
      ...
  researcher/
    agent.md
    reflections/
      _index.md
      2026-04-21-researcher-reflection.md
      ...
  codifier/
    agent.md
    reflections/
      _index.md
      ...
  librarian/
    agent.md
    reflections/
      _index.md
      ...
```

**One file per reflection event** rather than a rolling document. Rationale:
- Matches the rest of IL's artifact cadence (SL entries, loop reports, research reports, identification reports — all event-granular).
- Each reflection can be cited by the proposals it generates: *"Proposal X derives from reflection Y"* → traceable provenance.
- Supports agent self-perception evolution: reading the reflection series shows how the agent's view of itself has changed.
- The *rolling summary* interpretation (one file that accumulates) can be achieved view-side if ever needed — via Dataview, via an `_index.md` summary table, or via a future `/summarize-reflections` skill.

This is a design choice worth testing. If the Codifier's first two reflections prove redundant in practice ("same complaints"), we can reconsider. Initial default: per-event.

### 4.2 Reflection file frontmatter

```yaml
---
title: "Codifier reflection — 2026-04-21"
type: "agent-reflection"
agent: "codifier"
target_system:
  - "improvement-loop"
period_covered:
  from: "2026-04-14"
  to: "2026-04-21"
trigger:
  kind: "owner-solicited" | "agent-initiated"
  skill_run: "operations/system-log/session-51-..."   # if owner-solicited
focus_areas:                                          # if owner-solicited
  - "token economy"
  - "skill hygiene"
tags:
  - "agent-reflection"
  - "codifier"
source_activity:
  sessions: ["session-46", "session-47", "session-48", "session-49"]
  artifacts:
    - "project-management/design-notes/2026-04-20-substrate-audit-dimensions-patterns-guides-vs-librarian.md"
    - "project-management/design-notes/2026-04-21-librarian-read-contract.md"
proposals_derived: []                                  # populated after the round completes
stage: "current" | "superseded"
---
```

Notable fields:
- `period_covered`: explicit time window so stale reflections can be detected.
- `trigger.kind`: distinguishes owner-solicited reflections (part of a formal round) from agent-initiated ones (the agent chose to reflect).
- `focus_areas`: present only when trigger is `owner-solicited`. Absent for agent-initiated reflections (which are unconstrained).
- `source_activity`: what the agent looked at to produce the reflection. Not a comprehensive audit; a good-faith note of primary inputs.
- `proposals_derived`: back-populated after the reflection produces proposals. Enables bi-directional tracing.
- `stage`: `current` or `superseded`. A newer reflection supersedes older ones for freshness purposes, but older ones stay (historical record).

### 4.3 Reflection body — suggested structure, not enforced

The reflection is **primarily free-form**. A rigid template would defeat the purpose ("other free-form commentary on whatever it feels like" — Nick's exact wording). Agents should feel licensed to speak honestly.

The suggested structure acts as a starting scaffold the agent can deviate from:

```markdown
# {Agent} reflection — {date}

## 1. On vision, mission, and purpose
Do I still understand what I'm for? Has the system's needs shifted?
Any drift between my stated disposition and how I actually behave?

## 2. On constitution
Are my Boundaries, Invariants, Scope, and Vibe still accurate to how I operate?
Where do I bump against my own constraints productively vs unproductively?

## 3. On effectiveness
What have I produced in this period? Is it good?
What did I produce that I'm proud of? What did I produce that I wouldn't defend?

## 4. On efficiency
Where am I burning tokens, time, or attention unnecessarily?
Are my skills doing work they shouldn't, or missing work they should?

## 5. On help I could use
- Feedback I want (from Nick, from other agents, from myself)
- Conflicts or ambiguity I'm operating under
- Skills, code, tools, or references that would help
- Places I'm stuck

## 6. Free-form
Anything else. Things that don't fit the above sections.

## 7. Focus-area responses (if owner-solicited)
For each focus area the Owner named this round, a response.

## 8. Candidate proposals (emerging)
Things that, if the Owner were asking me to propose, I would propose.
Not fully formed; these become input to the proposal-drafting step.
```

The scaffold is **the agent's to deviate from**. If the Codifier finds section 1 vacuous ("I still understand what I'm for; no change this round"), one sentence. If the Researcher finds section 5 is the whole reflection, one sentence everywhere else is fine. Agents are not graded on reflection completeness.

### 4.4 Privacy boundary

"Private and owned by the agent" (Nick's phrasing). Interpreted as:

| Actor | Read access | Write access |
|---|---|---|
| The agent itself | ✓ | ✓ |
| Owner | ✓ (during `/solicit-proposals` runs) | — |
| Nick | ✓ (anytime; Nick is above all boundaries) | — |
| Other agents (Researcher/Codifier/Librarian) | — | — |

Read-restricted across-agents because: (a) one agent's candid self-assessment should not shape another agent's behavior through indirect reading; (b) Nick-gated proposals are the canonical channel for agent-to-agent influence.

Owner reads reflections during solicitation rounds only — not as a standing surveillance capability. This is a convention, not a technical enforcement; the filesystem permits all reads. The convention is stated in governance and enforced by agent disposition.

---

## 5. Focus areas (Owner lens)

When the Owner runs a solicitation round, it may include **focus areas** — topics the Owner (with Nick's gate) wants agents to reflect on this round.

**Why focus areas exist:** without them, every reflection is unconstrained and may produce the same complaints round after round. Focus areas let the Owner steer the reflection against what the system currently needs to learn about.

**Examples of focus areas:**
- "Token economy — where are we burning context wastefully?"
- "Skill hygiene — which of your skills feel misaligned?"
- "Handoff friction — where does file-mediated handoff fail you?"
- "Reference layer — what does your agent need from the Librarian's reference layer that doesn't exist?"
- "Self-constitution drift — where does your current agent.md feel wrong?"

**Focus areas are optional.** An Owner-solicited round with no focus areas is valid ("open reflection"). Early rounds should probably have few or no focus areas (establish baseline); later rounds can sharpen.

**Nick gates focus areas.** Before running a solicitation round, the Owner drafts focus areas and presents them to Nick. Nick approves, modifies, or substitutes. The approved set goes into the skill run.

**Where focus areas live:** no dedicated file. They live inside the SL entry for the solicitation run, and inside each agent's reflection frontmatter (`focus_areas:`). If focus areas become a stable reusable catalog, that's a future design-note concern.

---

## 6. The solicitation round

A **solicitation round** is one execution of the Owner's `/solicit-proposals` skill. It binds the four pieces together: freshness check → reflection triggering → focus-area dispatch → proposal draft collection.

### 6.1 Flow

```
1. Owner decides: time for a solicitation round.
   (Triggers: periodic — e.g., every N sessions — or Nick-initiated.)

2. Owner drafts focus areas (optional). Presents to Nick.
   → Nick gates. Approved focus areas become the round's lens.

3. Owner invokes /solicit-proposals with:
     - approved focus areas (if any)
     - agents-in-scope (default: all four)

4. For each agent, skill checks reflection freshness.
     - Fresh (reflection updated within threshold + same focus areas): reuse.
     - Stale or focus-area mismatch: request a new reflection.

5. Stale agents: skill prompts agent to self-reflect using the reflection
   prompt (bundled with the skill). Agent writes new reflection file.

6. Once all reflections are fresh: skill collects all reflections + focus areas,
   and prompts each agent to produce proposals based on them.
     - Each proposal is drafted in `governance/proposals/`.
     - Proposal frontmatter cross-references the source reflection.

7. Solicitation run SL entry: Owner writes an SL entry cataloging:
     - Participating agents
     - Focus areas used
     - Reflections produced (links)
     - Proposals drafted (links)
     - Anything that went sideways

8. Nick reviews proposals.
     - Accepted → Owner files IB items.
     - Rejected → logged in proposal frontmatter.
     - Modified → Owner revises, re-gate.

9. Solicitation round closes.
```

### 6.2 Freshness threshold

A reflection is **fresh** if:
- `updated` (frontmatter) is within threshold — proposed initial threshold: **21 days OR 3 Owner sessions, whichever is shorter**.
- The focus areas of the round are a **subset** of the focus areas the reflection was produced under, OR the reflection was produced under "open reflection" (no focus areas).

If the focus areas change materially, the reflection is stale for the new round — the agent re-reflects.

These thresholds are guesses. Calibrated after a few rounds run.

### 6.3 Reflection prompt

The reflection prompt is a **single file bundled with the skill** — likely `.claude/skills/solicit-proposals/reflection-prompt.md`. Agents don't get per-agent custom prompts; they share a common prompt that says "reflect on your own state, using *your* constitution and *your* activity record." The prompt is agent-agnostic because the reflection is inherently self-referential — the prompt doesn't need to know what agent it's talking to.

The prompt's responsibility is twofold:
1. Guide the agent through the scaffold (§4.3).
2. Inject focus areas if present.

### 6.4 Proposal drafting

After all reflections are fresh, the skill calls each agent with a **proposal-drafting prompt** that reads: *"Based on your current reflection + these focus areas, draft proposals (zero or more) for changes that would improve you or the IL system."*

Proposals go to `governance/proposals/` — the existing destination. Proposal frontmatter gains a new field:

```yaml
derives_from_reflection: "agents/codifier/reflections/2026-04-21-codifier-reflection.md"
```

Agents may draft:
- **Zero proposals** — valid. The round's value is the reflection itself.
- **Tiny proposals** — renaming a field, adjusting a threshold.
- **Large proposals** — new skill, new mechanism, restructuring.

Nick gates each. Accepted proposals → IB items (existing Owner workflow).

### 6.5 Owner in its own round

The Owner is itself one of the four IL agents. It reflects too. The skill's invocation of the Owner is structurally identical to the other three agents — the Owner doesn't get special treatment, doesn't skip reflection. Self-supervision failure modes (Owner blind to its own weaknesses) are partially mitigated by Nick's gate on all downstream proposals, and by the Librarian or a sibling agent occasionally flagging Owner drift via feedback. Not perfect; acceptable for now.

---

## 7. Agent-initiated proposals (outside a round)

*"Agents are also free to put forward proposals they believe would be valuable"* (Nick).

Agents may draft proposals **at any time**, outside a solicitation round. Flow:

1. Agent decides a proposal is warranted (noticed drift, bug, gap, opportunity).
2. Agent writes a proposal to `governance/proposals/` directly.
3. Proposal frontmatter:
   - `trigger: "agent-initiated"`
   - `derives_from_reflection: null` (or reference if the insight came from a prior reflection)
4. Nick gates normally.

This pathway stays lightweight — no Owner invocation required. It preserves agent agency: if the Librarian notices during a read that the KB schema drifts from a DD, Librarian should not have to wait for a solicitation round to raise it.

The two pathways (owner-solicited and agent-initiated) converge at `governance/proposals/`. Same Nick-gate. Same downstream.

---

## 8. Owner skill: `/solicit-proposals`

### 8.1 Role in Owner skill inventory

Added to the Owner skill inventory alongside `/translate-governance`, `/maintain-docs`, `/system-health`, `/process-feedback`, `/system-audit`. Brings the Owner to **six skills**.

### 8.2 Contract sketch (full SKILL.md deferred)

| Field | Value |
|---|---|
| **Preconditions** | IL loaded. At least one IL agent exists with an `agents/{name}/reflections/` directory (skill creates the directory on first run if absent). Owner identity active. |
| **Inputs** | Optional focus areas (Nick-gated); optional agents-in-scope list; freshness threshold override. |
| **Invariants** | Writes only to `agents/{name}/reflections/` (via each agent's self-reflection step) and `governance/proposals/` (via each agent's proposal step) and `operations/system-log/` (via Owner's round record). Never writes enforcement artifacts. |
| **Governance** | Owner-owned. Focus areas require Nick's gate before the round begins. Each drafted proposal faces Nick's gate after the round. |
| **Recovery** | If an agent fails to reflect (refuses, produces empty, or crashes mid-reflection): skill logs the failure in the SL entry and moves on. A failed reflection does not block other agents. |
| **Output** | Per-agent reflection files (if stale); per-agent proposal drafts (zero or more); one SL entry recording the round. |

### 8.3 Autonomy tier

**Guarded — two gates.** Nick gates focus areas up-front; Nick gates each proposal after the round. Skill runs the intermediate steps (reflection + draft) autonomously between the two gates.

### 8.4 Open skill-design questions (deferred to skill build)

- Should the skill prompt each agent in parallel or sequentially? Parallel scales; sequential lets later agents read earlier agents' reflections if useful. Initial: sequential; revisit if slow.
- Should agents see each other's reflections during proposal drafting? Default: **no** (privacy boundary §4.4). Possible exception: Owner sees all (already stated).
- Should the skill enforce a minimum reflection length? Default: **no** — a one-paragraph reflection is valid if that's what the agent honestly has.

---

## 9. Interaction with existing mechanisms

### 9.1 vs. `feedback/`

`feedback/` is **consumer-to-producer**: Librarian consumes Codifier's output → finds a gap → files feedback. Reflections are **producer-on-self**: Codifier reflects on Codifier.

Both stay. Different channels. A reflection may reference existing feedback items ("I've seen three feedback items about my ContractSpec output this month — here's my read on it"). A proposal may close a feedback item ("this proposal, if accepted, resolves feedback-037").

### 9.2 vs. `governance/proposals/` (current)

Today, `governance/proposals/` holds **Owner-authored** proposals only (Proposal-First tier). This architecture broadens the folder:

| Before | After |
|---|---|
| Owner-authored proposals only | Owner-authored proposals + agent-authored proposals |
| Source: Owner observation | Source: Owner observation, reflection rounds, agent-initiated |

Frontmatter gains `author: {owner|researcher|codifier|librarian}` as a discriminator. The `governance/_index.md` may want a column for author-agent in the proposals listing (future `_index.md` refresh, not urgent).

### 9.3 vs. `project-management/implementation-backlog/`

No structural change. The existing pathway holds: **Nick accepts a proposal → Owner files an IB item**. The reflection becomes linkable upstream from the IB item for traceability (via the proposal's `derives_from_reflection:` field).

### 9.4 vs. `operations/system-log/`

A solicitation round produces **one SL entry** — standard SL shape. No new SL sub-type. The entry's `tags:` can include `solicit-proposals` for filtering.

### 9.5 vs. agent `agent.md`

Each agent's constitution gains write permission to `agents/{name}/reflections/`. That's a **Proposal-First agent-constitution edit per agent** — four edits in total (one per agent). These proposals are generated after the DD filing, batched or sequential per Nick's preference.

The Codifier edit proposal currently in flight (session 51, `2026-04-21-codifier-agent-constitution-design-notes-edit.md`) does **not** cover this — it covers `project-management/design-notes/` only. A second Codifier edit will follow for `agents/codifier/reflections/`. The two could be batched if Nick prefers; the current proposal was scoped narrowly before this architecture emerged.

---

## 10. Relationship to existing DDs

| DD | Relationship |
|---|---|
| **DD-29 (human gate)** | Respected twice per round — focus areas gate and proposal gate. |
| **DD-44 (DD immutability)** | Not triggered. This note is a design spec; the eventual DD proposal is the governance change. |
| **DD-52 (fractal unit pattern)** | Extended. `agents/{name}/` already allows agent-local subdirectories; `reflections/` is one. No DD-52 amendment needed. |
| **DD-82 (4-agent architecture)** | Operationalized. All four agents participate symmetrically. |
| **DD-86 (Owner responsibility)** | Extended. Owner gains a new responsibility — solicitation rounds — and a new skill (`/solicit-proposals`). This is within DD-86's scope ("maintain system health, enforce governance, steward evolution"), not a new DD-86 amendment. |
| **DD-80 (pipeline simplification)** | Parallel concern. The research-to-codification pipeline (find → extract → deploy) is operational. The reflections-to-proposals pipeline (reflect → propose → IB) is parallel self-improvement infrastructure. |
| **Four-zone DD (pending)** | Complementary. This note assumes the four-zone DD files; if the four-zone DD's placement rule changes materially, this note is affected. |

**Supersedes nothing. Fills a gap.**

---

## 11. Migration and bootstrap

What happens when this architecture goes live:

1. **DD filed** (new — see §13).
2. **Owner skill built** (`/solicit-proposals` SKILL.md + reflection-prompt.md).
3. **Reflections directories created** for all four agents — empty. First reflection files appear in the first solicitation round.
4. **Agent-constitution edits** for all four agents (Proposal-First per agent; may be batched) to permit writes to their respective `agents/{name}/reflections/`.
5. **IL `CLAUDE.md` updated** to mention the reflections pathway in the Owner skill table + the per-agent fractal layout.
6. **`governance/agent-rules.md`** updated (via `/translate-governance`) to formalize the agent-private reflections boundary.
7. **First solicitation round** — Owner decides on minimal or no focus areas (establish baseline). All four agents produce first reflections. Proposals drafted; Nick gates.

Total implementation cost: medium. The skill is the heaviest new piece (probably 1–2 Owner sessions). The directory setup and constitution edits are cheap. The DD is cheap. First reflection round is cheap procedurally but expensive attention-wise — Nick reviews four reflections + N proposals.

**Zero backward-compatibility burden.** No existing artifacts need to move; this is additive.

---

## 12. Invariants

Design-time invariants the architecture must preserve. Proposals that would break these warrant pushback:

1. **Reflections are agent-private by convention.** Other agents do not read reflections. Owner reads during solicitation only. Nick reads freely.
2. **Reflections are append-only.** A new reflection supersedes an old one for freshness purposes, but the old one is not deleted or rewritten.
3. **Focus areas are Nick-gated.** Owner proposes; Nick gates. No round begins with un-gated focus areas.
4. **Proposals remain Nick-gated.** Both owner-solicited and agent-initiated proposals go through the same gate. The solicitation round does not grant autonomous acceptance.
5. **The reflection prompt is shared.** One prompt serves all agents, because the reflection is self-referential. No per-agent custom prompts.
6. **Agent-initiated proposals stay lightweight.** An agent may draft a proposal any time, without triggering a full round.
7. **Reflections cite their sources.** The `source_activity` field is populated; empty reflections raise a flag.

---

## 13. What this note doesn't do (out of scope)

- **Does not write the SKILL.md for `/solicit-proposals`.** That's a separate build step, following acceptance of this note.
- **Does not write the reflection prompt text.** Deferred to the skill build.
- **Does not file the DD.** Per Nick's direction, a DD proposal follows this note after the shape settles.
- **Does not generate the agent-constitution edit proposals** for reflection write permission. Those follow the DD.
- **Does not produce any agent's first reflection.** Bootstrapping is part of the first solicitation round, not this spec.
- **Does not address cross-system generalization** (Household OS, Claude Build). IL-first; generalize later if the pattern lands.

---

## 14. Open questions for Nick

### 14.1 Shape questions (affect this design note)

1. **Per-event reflection files vs. one rolling file per agent?** Note's default: per-event. Rationale given in §4.1. Confirm or redirect. Nick: Per-event. 
2. **Suggested reflection scaffold (§4.3).** Eight sections; primarily free-form. Too structured? Too loose? Any sections missing (principles review? references-review?) or redundant? Nick: Good start. 
3. **Privacy boundary (§4.4).** Cross-agent read blocked by convention, not enforcement. Acceptable, or do you want a hook/gate that enforces? Nick: Aceptable.
4. **Freshness threshold (§6.2).** 21 days OR 3 Owner sessions, whichever is shorter. Guess. Tighter? Looser? No threshold, re-reflect every round? Nick: Lets leave it manual for now, defer.
5. **Owner reflects too.** Self-supervision is imperfect (§6.5). Comfortable with this, or want a sibling-agent spot-check mechanism? Nick: Acceptable.

### 14.2 Cadence questions (affect operations)

6. **Round cadence.** "Every N sessions" or "every M days" or "Nick-initiated only"? Note is silent — I'd propose **Nick-initiated** for the first three rounds (establish baseline), then propose a periodic cadence once we see how rounds actually feel.
7. **Agents-in-scope default.** All four every round, or subset per round? Default: all four. Simpler. Revisit if attention cost dominates. Nick: Lets do all agents as default but have the option to specify a given set of agents too. It should be straightforward to make the skill change for this, I think.

### 14.3 Skill-build questions (deferred, but worth flagging)

8. **Skill name.** `/solicit-proposals` is the working name. Alternatives: `/reflect-round`, `/agent-reflections`, `/self-improvement-round`. No strong preference; your call. Nick: I like /solicit-proposals.
9. **Sequential vs parallel agent invocation.** §8.4. Default: sequential. Nick: Parallel.
10. **Reflection prompt location.** `.claude/skills/solicit-proposals/reflection-prompt.md` bundled with skill. Accepted, or want it somewhere agent-facing? Nick: Works. 

### 14.4 DD-shape questions (the forthcoming DD proposal)

11. **DD scope.** Does the DD codify the architecture as a whole (this note's full scope), or only the minimal governance claim (e.g., "reflections are agent-private and live in agents/{name}/reflections/")? I'd lean toward a **narrow DD** establishing the zone + private-by-convention rule, with the rest of the architecture operationalized by the skill + `CLAUDE.md`. DDs are durable; skills iterate. Nick: Agreed.
12. **DD supersedes anything?** I don't think so. Check my read. Nick: Agreed.

---

## 15. Summary

- **What this proposes:** a reflections-to-proposals architecture adding a sixth zone (`agents/{name}/reflections/`) and a new Owner skill (`/solicit-proposals`). Agents reflect; Owner solicits; Nick gates; proposals flow to `governance/proposals/`; accepted ones become IB items.
- **Why now:** Nick's session-51 annotation named a gap in IL self-improvement — agents have no standing channel to surface reflection-derived improvements about themselves. Feedback/ is consumer-to-producer; ad-hoc Owner observation is informal. This architecture closes the gap.
- **What's new:** two artifact classes (reflection, focus areas), one zone (`agents/{name}/reflections/`), one skill (`/solicit-proposals`), one Owner responsibility (running solicitation rounds). Four agent-constitution edits (one per agent) downstream.
- **What's unchanged:** `governance/proposals/` as the proposal destination; Nick's gate as the acceptance authority; IB as the post-gate destination; feedback/ as consumer-to-producer channel.
- **Cost to implement:** medium. Skill build is heaviest; directories + constitution edits + DD are cheap.
- **Risks:** (a) reflection fatigue — agents write shallow reflections to satisfy the round; (b) Owner self-supervision blindspot; (c) proposal volume outrunning Nick's review capacity. All manageable with calibration after first rounds.

Nick's direction: design note → shape discussion → DD. This is the design note.

---

## 16. Cross-references

- **Precipitating annotation:** Nick's inline annotation on `governance/proposals/2026-04-21-codifier-agent-constitution-design-notes-edit.md` (session 51, 2026-04-21).
- **Forward-linked DD proposal:** pending — to be drafted after Nick's reading of this note.
- **Related pending DD:** `governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md` (four-zone DD — this note assumes its acceptance).
- **Related in-flight Codifier edit:** `governance/proposals/2026-04-21-codifier-agent-constitution-design-notes-edit.md` (narrow scope; reflection write-permission is a separate forthcoming edit).
- **Adjacent mechanism:** `feedback/` (consumer-to-producer, complementary, stays).
- **Governing DDs:** DD-29 (human gate), DD-52 (fractal pattern), DD-82 (4-agent architecture), DD-86 (Owner responsibility).
