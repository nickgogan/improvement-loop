---
notion_id: 3351e08b-9b34-81b0-b6cd-c920d55689b1
name: Human-on-the-Loop (HOTL) Autonomy Tiering Framework
summary: 'Explicit governance model that distinguishes HITL (approve before action) from HOTL (monitor + override after action). Autonomy Matrix assigns Control Tier to every AI-driven process. Three governance
  pillars: (1) Veto Protocol; (2) Algorithmic Guardrails (define boundaries with dollar/scope thresholds, not procedures); (3) Audit Trail. Single Command Center for all pending approvals.'
implementation_notes: 'KB existing patterns don''t address when agents should ask vs. act. HOTL + Autonomy Matrix provides the framework. Also tied to EU AI Act Article 14 compliance. Claude Code Auto Mode
  is an implementation of HOTL principles at the tool level. Sources: https://www.torryharris.com/insights/articles/human-on-the-loop-ai / https://www.strata.io/blog/agentic-identity/practicing-the-human-in-the-loop/'
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- human-on-the-loop-ai-hotl-torry-harris.md
- hitl-agentic-ai-strataio-2026-guide.md
- anthropic-trustworthy-agents-in-practice.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-19'
related_findings:
- file: autonomy-gradient-not-binary-delegation.md
  rel: same-problem
- file: mcp-elicitation-for-user-input.md
  rel: enabled-by
- file: agent-state-machine-with-witness-monitoring.md
  rel: same-problem
- file: claude-code-auto-mode-ai-driven-permission-classif.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
---
# Human-on-the-Loop (HOTL) Autonomy Tiering Framework

## What It Is
A governance tier system for production agents that provides explicit policy for when agents should act autonomously vs. pause for human review.

**HITL vs. HOTL distinction:**
- **HITL** -- Human approves before every action. AI cannot proceed without command at each stage. This is the bottleneck.
- **HOTL** -- Agent operates autonomously within guardrails; human monitors and can intervene. Intelligence shifts from interface prompting to infrastructure-embedded decision-making.

**Autonomy Matrix:** Categorizes every AI-driven process by two dimensions (complexity x stakes) to assign a Control Tier. Recommended to start at Tier 3 (Operational) to build trust.

**Three Governance Pillars:**
1. **Veto Protocol** -- Standardized Pause Points with Decision Summary answering three questions: "What action am I taking?", "Why is this the optimal path? (The Logic Chain)", "What is the projected impact?"
2. **Algorithmic Guardrails** -- Define boundaries with explicit thresholds, not procedures. Example: "The agent may reallocate budget between marketing channels autonomously, provided the shift does not exceed $5,000 per day."
3. **Audit Trail** -- Timestamped log of which data points influenced each decision, enabling Post-Action Review (PAR) for quarterly tuning.

**Implementation Roadmap:** Inventory silos → Assign tiering → Define approval portals → Monitor drift (quarterly reviews).

## Why It Matters
Provides the missing governance framework for the KB's existing agent patterns. EU AI Act Article 14 requires demonstrable human oversight.

## Why People Are Using It
Convergence across multiple 2026 sources. Regulatory pressure is making governance documentation non-optional. Evidence from agent management tools shows per-task permission selection — users grant different autonomy levels to different agent tasks within the same session, rather than a blanket autonomy setting.

## Potential Failure Modes
HOTL relies on guardrails being correctly set. Post-Action Review requires humans to actually review the audit trail.
