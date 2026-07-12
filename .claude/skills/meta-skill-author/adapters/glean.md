# Glean Adapter

Glean Agents (Agent Builder) is an **enterprise agent platform**, not a file-based skill
harness. There is no `SKILL.md` loading, no filesystem, and no git — an agent is a hosted
object with a name, description, instructions, attached **Resources**, tool grants, and
triggers. Porting a skill to Glean therefore means **distilling the skill body into the
agent's instructions**, attaching the skill's reference files as Resources, and mapping
every filesystem/git dependency onto Glean-native equivalents (indexed documents, chat
context, search, connector write tools). This is the "false portability" caveat made
concrete: skill *content* ports, but effectiveness depends on replacing harness features
that do not exist on the target. [multi-ide-portability-via-installer-templates]

Format facts below were verified against Glean's official documentation (docs.glean.com —
Agent Builder, How agents work, Triggers, Memory, Execution limits, Agent library, Sharing
and Permissions) via the Glean MCP server on 2026-07-09. **No explicit character caps are
published for name/description/instructions**; operational limits are per-run tool-call
budgets, ~30-minute scheduled-run execution limit, and session token limits — Glean's own
guidance is to shorten instructions if the agent approaches truncation or stalls.
Re-verify tenant-specific tool availability (write tools, MCP tools, memory) before use.

---

## Native Format

| Attribute | Detail |
|-----------|--------|
| Primary object | An **Agent** created in Agent Builder |
| Authoring modes | **Auto mode** (default; you state the goal + grant tools, Glean architects the logic — natural-language-first, markdown Instructions editor) or **Workflow mode** (you design the execution flow step by step in the visual builder; best for deterministic processes) |
| Core fields | Icon · Name (required) · Description (optional; shown in Agent Library, can be AI-enhanced) · Agent goal message · Instructions (Auto mode) or Steps/branches (Workflow mode) · Model (agent-level; per-step in Workflow mode) · **Tools** · **Resources** · Triggers · Sharing scope |
| **Resources** | First-class field: attach documents, folders, collections, and other indexed content the agent should rely on — **this is the home for a skill's `references/` and `templates/` content** (no search-and-hope needed) |
| Tools | Glean-native retrieval (Company Search, Read document, people search, web search, code search) · connector tools incl. **write tools** (Jira, Salesforce, M365, Google Docs, Slack…) · custom tools · remote MCP tools. Auto mode supports app-level grants |
| Write capability | **Agents can write/update external systems** (update tickets, edit docs, send messages) when write tools are granted — most write tools require **user confirmation**; scheduled/background runs may only use tools admins allow without confirmation |
| Knowledge access | Permission-enforced retrieval over the org's indexed sources; the agent only sees what the *invoking user* can see |
| Triggering | Chat message trigger (conversational, supports conversation starters) · input form trigger (task-style) · schedule · content trigger (runs on content change) · Slack publishing · API · embed. **No description-matched auto-dispatch across a catalog; no documented @-mention invocation** |
| Sub-agents | **First-class**: an agent step can call another agent; sub-agents have their own memory and only their Respond outputs return to the parent — cross-skill handoff arcs CAN port as agent chains |
| Memory | Run/session memory during execution (chat-triggered agents also see the current chat's prior messages); a **persistent user-memory personalization layer** can apply across chats where enabled (currently GCP deployments only) — do not rely on it for durable state |
| Versioning | Auto-saved drafts; each Save creates a live version with version history, Restore, and restore-to-published; **last 30 versions retained** — the Glean-native equivalent of git checkpoints for the agent definition |
| Distribution | Agent Library (browse/search/filter/favorite); sharing to users/teams/org; certification handled by admins |

**Mapping from the portable skill standard:**

| Open-standard element | Glean mapping |
|-----------------------|---------------|
| `name` | Agent name (human-readable; no charset constraint) |
| `description` | Agent description — discovery is **human browsing + orchestration routing**, not model-side trigger matching; write it for a person scanning the agent library, keep trigger phrasing anyway for @-mention recall |
| SKILL.md body | The **Instructions** field — no lazy body loading; the full instruction set is always paid (same cost profile as Copilot's always-on model) [skill-description-budget-context-overflow] |
| `references/` + `templates/` (L3 depth) | **Attach as Resources** — upload each runtime-essential reference/template to an indexed source (e.g. a Drive folder per agent) and attach it in the Resources field; Instructions then point to each by name. Only inline what is short and load-bearing on every run. Background-research files (design rationale, build plans) stay home — they are authoring-time, not runtime |
| `scripts/` (deterministic validators) | No script execution in the builder. Convert each validator into an **in-prompt deterministic checklist** reported item-by-item, or a **custom tool / remote MCP tool** if the tenant has one configured. Workspace-specific scripts that don't generalize are dropped explicitly, with a note in the port |
| `allowed-tools` | The **Tools** grants (retrieval, web search, connector read/write tools, custom/MCP tools) — set at build time, enforced by the platform; write tools additionally gated by per-use user confirmation |
| Files the skill reads/writes (PROGRESS.md, profiles, guides) | **Designated documents in an indexed connector** (e.g. a "Project PROGRESS" Google Doc), attached as Resources or retrieved by title. Writes: **draft-first by default**; where the tenant grants a write tool (e.g. Google Docs edit), the agent may apply the update **through that tool with user confirmation** — never claim persistence that didn't go through a granted tool |
| git (commit log, diffs, checkpoints) | Does not exist. Drop commit-convention mechanics; keep the *information discipline* (one logical change per update, rationale recorded). Agent-definition changes are covered by Glean's built-in 30-version history |
| `/memories/*` scopes | Run/session memory only, plus the optional user-personalization memory layer (deployment-dependent). Durable *project* state must live in the designated documents themselves — which is exactly the PROGRESS-as-session-bridge pattern |
| Sibling-skill handoffs | Port as **sub-agent calls** (an agent step can run another agent) or merge the arc into one agent — never reference a sibling that doesn't exist on the tenant |

---

## Discovery & Activation

Glean's model is **explicit invocation**: a human finds the agent in the Agent Library
(browse/search/filter/favorite), opens its chat trigger or input form, or a schedule /
content trigger / Slack channel / API call fires it. There is no per-request catalog of
skill descriptions for the model to route against, so:

- The description sells to a **human browser**, not a router. Lead with the outcome
  ("Reconciles your project's PROGRESS doc at session end so anyone can cold-start"), then
  when-to-use, then what it will ask for.
- Undertriggering risk shifts from "model never loads the body" to "colleague never finds
  the agent" — name agents by the job-to-be-done, not the source skill's internal name.
- One skill mode ≠ one agent necessarily. A multi-mode skill (e.g. build/apply/score/refresh)
  ports best as **one Auto-mode agent with an explicit mode-selection preamble** in
  Instructions; split into separate agents (or a parent agent calling sub-agents) only if
  sharing scopes or tool grants differ per mode.
- Chat-trigger agents support **conversation starters** — seed them with the skill's
  trigger phrases so invocation vocabulary survives the port.

## Provides (capability inventory — §4.2 requires × provides)

What this platform supplies against the controlled capability vocabulary
(`../references/capability-vocabulary.md`). Stage-2 ports map every row of the source
skill's `capability-contract.yaml` here: unmet **required** ⇒ the port states "do not
install without it"; unmet **optional** ⇒ the port carries the contract's degradation
note in its "Host capabilities required" block.

| Capability | Provides | How / note |
|---|---|---|
| `internal-document-search` | **native** | Company Search + Read document tools — permission-enforced retrieval over indexed sources |
| `durable-document-store` | partial | Indexed connector docs; writes only via granted write tools with per-use confirmation — draft-first otherwise (the agent pastes, the human saves) |
| `workspace-file-inventory` | partial | Indexed content only — no filesystem; enumeration limited to what connectors index |
| `connector-source-discovery` | **native** | Connector tools across indexed sources, permission-enforced per invoking user |
| `versioned-checkpoints` | partial | Agent-definition version history only (last 30 versions); no content-artifact versioning |
| `change-detection` | absent | No diff/status surface over indexed content |
| `script-execution` | absent | No script runtime in Agent Builder — convert validators to in-prompt checklists or custom/MCP tools (Porting Procedure rule 3) |
| `fresh-context-scoring` | **native** | Sub-agent calls: own memory; only Respond outputs return to the parent |
| `human-approval-channel` | **native** | Per-use write-tool confirmation; conversational approval in chat-trigger agents |
| `reference-bundle-attachment` | **native** | The Resources field (documents, folders, collections) |
| `byproduct-store` | absent | No designated ephemeral store — avoid byproducts or route them to a designated doc |

## Porting Procedure (three-layer pattern applied)

Terminology (house convention, defined in SKILL.md §4.2): **`adapters/<platform>.md`** =
the reusable platform *profile* (this file — one per platform, lives with the porting
method); **`ports/<artifact>.md`** = the generated per-skill *deliverable* for a target
platform (lives inside each ported skill's directory). Adapter = recipe; port = dish.

1. **Canonical source stays in the repo** — the SKILL.md remains authoritative; the Glean
   port is a generated artifact, expected to be re-derived when the source changes. Keep the
   port in `ports/glean-agent.md` inside the skill directory, clearly marked with source
   skill + version.
2. **Distill, don't paste.** Rewrite the body as Goal + Constraints + Context for the
   Instructions field [reasoning-model-anti-pattern-prescribed-reasoning]. Strip: file
   paths, git mechanics, harness-specific tool names, workspace-specific pointers, and all
   `[finding-name]` citations (dead weight in a prompt). Keep: the operating model, stop
   rules, HITL tiers, output formats, and deterministic checklists.
3. **Inventory bundled files — every port names the fate of every bundled file.** Walk the
   skill's `references/`, `templates/`, `scripts/`, and any bundled helper skill; classify
   each as **attach as Resource** (runtime-essential, separable), **inline** (short +
   load-bearing every run), **convert** (script → checklist or custom/MCP tool), or **drop
   with reason** (workspace-specific, authoring-time-only, or not separable). A port that
   silently ignores bundled files is incomplete. Bundled helper skills are usually
   **not ported** — a helper that maintains the local package via sandboxed file edits has
   no Glean equivalent; instead register the new platform in the helper's watch scope so
   refresh runs cover the adapter.
4. **Externalize state.** For every file the skill reads/writes, name a **document
   convention** in Instructions ("a doc titled `<Project> — PROGRESS`"), attach standing
   docs as Resources where possible, and fall back to Company Knowledge retrieval by title.
   First-run behavior: if the doc doesn't exist, the agent outputs a starter template for
   the human to create.
5. **Convert side-effect tiers.** Default posture is **draft-first**: present the updated
   text. Where the tenant grants a write tool, map Proposal-first tiers onto **write-with-
   user-confirmation** through that tool; Human-required tiers stay human-performed. The
   agent never claims to have persisted anything that didn't go through a granted tool.
   Scheduled/unattended runs are restricted to tools allowed without confirmation — assume
   read-only there.
6. **Separability audit before export.** A port leaving the workspace must carry **zero
   user-specific or workspace-specific content** — no personal names, employer targets,
   repo paths, or profile facts. Same bar as the kb-separability guardrail. Note: files
   destined to be *attached as Resources in the target tenant* need only be separable from
   *this* workspace's user content; tenant-internal references are acceptable **inside the
   tenant**, never inside the port file itself.
7. **Verify in-tenant.** Paste into Agent Builder, attach the Resources, run the skill's
   representative task once, and fix against actual behavior (tool-call budgets, truncation)
   before sharing [iterate-on-single-task-then-extract-skill].

## What Does NOT Port

- Description-matched auto-triggering, path-scoped activation, `allowed-tools`
  frontmatter semantics, all Claude Code extension fields.
- Anything requiring a local filesystem, git, or shell. Deterministic validation ports
  only as an in-prompt checklist (weaker: LLM-simulated, not guaranteed) or a custom /
  remote MCP tool.
- Bundled helper skills that maintain the local package (sandbox refresh loops) — no
  Glean equivalent; cover the platform via the helper's source watchlist instead.
- Persistent agent-owned memory as a design dependency — user-personalization memory is
  deployment-dependent; durable state belongs in designated documents.
