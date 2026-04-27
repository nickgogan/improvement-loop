---
title: "Close Irrelevant IDE Files During Agent Sessions"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "ide-context-streaming-silent-token-tax"
identification_report: "managing-agent-context.harvest-queue.md::ide-context-streaming-silent-token-tax::rule::close-irrelevant-ide-files-during-agent-sessions"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "users running coding agents inside IDE-integrated harnesses with automatic editor-state injection"
    - "long-running editor sessions where tabs accumulate beyond the active task's working set"
    - "cost-sensitive or context-budget-sensitive agent workflows where every injected token matters"
  platform_coupling: "specific:IDE-integrated agent harnesses (e.g., editors that automatically stream open-file and selection state to a coding agent)"
  autonomy: "hitl-only"
  stage: "operate"
  reversibility: "trivial — reopen the closed tabs; no state mutation occurs from following the rule"
  auditability: "medium — the user can probe the agent's visible context with a direct question, but the IDE itself typically provides no native injection-scope log"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented mitigation; no formal adoption mechanism beyond user habit at extraction time."
contract:
  preconditions: "An agent runs inside an IDE-integrated harness that silently streams editor state into model context. The user has multiple editor tabs open, only some of which are relevant to the current agent task. The user has the ability to close tabs and to query the agent about its visible context."
  invariants: "At each agent prompt, the set of editor tabs open in the IDE is a near-superset of the task's working set, with non-task tabs closed. The user can, on demand, enumerate which files the agent currently sees and confirm the set matches the task. Unexplained context-window inflation is investigated rather than ignored."
  governance: "Owner: The user/practitioner of the IDE-integrated agent harness. Reinforcement may come from a pre-session checklist, an IDE extension that prompts tab cleanup, or a session-start hook. The rule is user-discipline by default — automated enforcement is a future improvement (visible token-cost indicators, configurable injection scope, automatic budget caps)."
  recovery: "If unexpected context is observed in agent responses, close offending tabs and reissue the prompt. If material token-spend overruns occur, audit IDE-injection scope first using the \"what do you see?\" probe. If the IDE provides no controls or visibility, escalate to a session-level workaround: close the IDE entirely and run the agent from a terminal harness for token-sensitive sessions."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "ide-integration"
  - "silent-context-injection"
  - "token-hygiene"
---

# Close Irrelevant IDE Files During Agent Sessions

**Source:** [[ide-context-streaming-silent-token-tax]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

An agent runs inside an IDE-integrated harness where the IDE silently streams editor state — open files, highlighted selections, visible tabs — into the model's context window without explicit user invocation. The user is engaged in a task whose working set is a known, bounded subset of the open editor files. Tabs unrelated to the current task remain open in the editor (typical editor hygiene: tabs accumulate across days/projects).

## Action

**Required:** Before starting an agent session — and at task-switch boundaries within a session — the user closes editor tabs that are not part of the current task's working set. The user retains only the files genuinely relevant to the prompt being issued. When uncertain what the IDE is injecting, the user asks the agent directly ("what files do you see in your context?") to surface the current injection scope.

**Forbidden:** Treating IDE-open tabs as cost-free. Leaving unrelated files (yesterday's exploratory work, reference tabs, scratch files) open during agent sessions on the assumption they are inert. Issuing a prompt without first verifying — at least mentally — that the open-tab set matches the task's working set. Silently accepting unexplained context-window inflation without diagnosing the IDE-injection contribution.

## Boundary

Enforced at the editor before each agent prompt, with extra attention at task boundaries (starting a new task, switching projects, returning from a long break). The rule lives at the user-discipline level (practitioner habit) and may be reinforced by an IDE extension or session-start checklist that prompts a tab-cleanup before the first agent invocation.

## Enforcement

- **Mechanism:** A short pre-session checklist or IDE-extension prompt: (1) list currently open tabs, (2) flag tabs unrelated to the current task, (3) close them before the first agent prompt.
- **Check (deterministic):** `(open_editor_tabs ⊆ task_working_set) OR (irrelevant_tabs_closed_before_prompt == true)`. Spot-checkable by asking the agent to enumerate its visible context.
- **Violation response:** If unexpected context is observed in agent output (references to files unrelated to the task), close the offending tabs and reissue the prompt. If token consumption is materially higher than expected for the prompt size, audit the IDE-injection scope first before assuming prompt or response bloat. Treat any unexplained context-window growth as an IDE-injection candidate until ruled out.

## Rationale

IDE context streaming is automatic and invisible — every open file and highlighted selection in many IDE integrations gets silently injected as context tokens. Practitioners report this can account for a meaningful share of total context consumption. The user has no visual indicator that injection is occurring, so the cost compounds across sessions without diagnosis. The discovery technique ("what do you see?") reveals the actual injection scope but is rarely invoked. Tab hygiene is the cheapest mitigation: it requires no harness changes, costs nothing, and immediately reduces both token spend and irrelevant-context noise that degrades the agent's task focus.

## Failure Modes

- **Discoverability gap.** The IDE provides no native indicator that injection is happening, so users never think to clean tabs. Mitigation: the "what do you see?" probe; user education at agent onboarding; session-start checklists.
- **Over-pruning degrades ergonomics.** A user closes too aggressively and loses the IDE-aware assistance the streaming was designed to provide. Mitigation: the rule targets *irrelevant* tabs, not the working set; legitimate task files stay open.
- **Configuration complexity.** Where the IDE exposes injection-scope controls, users tune them incorrectly and either save no tokens or starve the model of useful context. Mitigation: prefer the simple discipline (close irrelevant tabs) over the configuration knob; treat any config as additive, not the primary control.
- **Session-end vs. session-start asymmetry.** A user cleans tabs at session end (when it doesn't matter) but starts the next session with whatever was open. Mitigation: the rule fires at session *start* as the primary checkpoint.
- **Probe-blindness.** The user runs "what do you see?" but doesn't recognize injected files in the response, or the model doesn't enumerate completely. Mitigation: re-probe with more specific framing ("list every file path in your current context"); cross-check against the IDE's open tab list.
- **Task scope drift.** What was "irrelevant" at session start becomes relevant mid-session as the task evolves. Mitigation: re-evaluate the working set at the same checkpoint as tab cleanup; opening additional files when the task expands is allowed; the rule is about pollution, not file-count caps.

## Contract

### Preconditions
An agent runs inside an IDE-integrated harness that silently streams editor state into model context. The user has multiple editor tabs open, only some of which are relevant to the current agent task. The user has the ability to close tabs and to query the agent about its visible context.

### Invariants
At each agent prompt, the set of editor tabs open in the IDE is a near-superset of the task's working set, with non-task tabs closed. The user can, on demand, enumerate which files the agent currently sees and confirm the set matches the task. Unexplained context-window inflation is investigated rather than ignored.

### Governance
Owner: The user/practitioner of the IDE-integrated agent harness. Reinforcement may come from a pre-session checklist, an IDE extension that prompts tab cleanup, or a session-start hook. The rule is user-discipline by default — automated enforcement is a future improvement (visible token-cost indicators, configurable injection scope, automatic budget caps).

### Recovery
If unexpected context is observed in agent responses, close offending tabs and reissue the prompt. If material token-spend overruns occur, audit IDE-injection scope first using the "what do you see?" probe. If the IDE provides no controls or visibility, escalate to a session-level workaround: close the IDE entirely and run the agent from a terminal harness for token-sensitive sessions.
