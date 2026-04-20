---
name: Signal Capture as Byproduct of Work
summary: Organizational knowledge systems only compound if signal capture is a byproduct of doing the work — not a separate documentation act. When feeding the system requires extra effort, the people with
  the most valuable context will strategically withhold it, and the system stagnates.
implementation_notes: null
category: Memory Architecture
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- world-models-orgs-three-architectures.md
related_findings:
- file: compounding-knowledge-loop-internal-data.md
  rel: same-problem
- file: org-world-model-three-architecture-patterns.md
  rel: part-of
- file: tacit-knowledge-as-agent-delegation-barrier.md
  rel: same-problem
- file: claude-code-hooks-for-automatic-session-memory.md
  rel: same-problem
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: same-problem
- file: composable-templates-for-lazy-capture.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: classified
consumed_by: []
---

## What It Is

A design principle for organizational knowledge systems: the system must capture signal as a natural byproduct of doing work, not as a separate documentation effort. If contributing to the knowledge system requires a distinct, extra step, the system will fail to accumulate the most valuable knowledge — specifically:

- People with the most valuable context are the most strategic about withholding it (information advantages are real)
- Even non-malicious team members will skip documentation under time pressure
- Back-channel conversations route around the system, keeping critical context in heads rather than the model
- The result is a knowledge system populated with low-stakes, easy-to-document information and missing the judgment-rich, high-stakes context that would make it useful

**Two failure modes:**
1. *Malicious withholding:* Team members who benefit from information asymmetry will not voluntarily feed a system that erodes that advantage
2. *Benign forgetfulness:* Even well-intentioned contributors forget to document when documentation is a separate step

**Design implication:**
Tool selection and workflow design must prioritize passive capture — where using the tool to do the work also produces the signal. Examples: commit messages over documentation files, ticket updates over status emails, structured decisions made in the system rather than in a separate document that gets pasted in.

The incentive structure also matters: team members need to believe there is an advantage to them personally for feeding the model, not just an advantage to the organization.

## Why It Matters

An org world-model that requires active documentation will drift toward the interests of whoever has time and motivation to document. The resulting knowledge asymmetry will shape system outputs in ways that aren't visible — because the absence of signal looks like "no signal" rather than "missing signal."

This is the human-side analogue of the technical signal fidelity problem: even with perfect technical architecture, the system is only as good as the organizational behaviors that feed it.

## Why People Are Using It

Raised as one of five principles for building world models that compound into real advantage. The author frames it as an underappreciated organizational change requirement: most teams are not ready to feed a system honestly, and most implementations don't design for resistance.

## Potential Improvements

- Hook-based passive capture: system integrations that record decisions and actions as side effects of normal work (e.g., auto-logging Slack threads where decisions were made)
- Friction reduction: making the "feed the model" action take fewer steps than the back-channel alternative
- Incentive design: making the model visibly useful to the people feeding it, not just to management

## Potential Failure Modes

- Passive capture can produce low-signal noise at high volume if not filtered — quantity of capture does not equal quality of signal
- Tool lock-in: optimizing for passive capture in one tool stack makes migration painful
- Privacy concerns: automatic capture of work conversations may create compliance issues in regulated industries
- The model may accumulate a skewed picture of reality if only certain types of work are naturally logged (e.g., code commits but not architecture discussions)
