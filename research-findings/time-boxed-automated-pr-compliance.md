---
name: "Time-Boxed Automated PR Compliance"
summary: |-
  opencode enforces its PR standards with a two-stage bot pipeline instead of maintainer
  attention: a workflow labels non-compliant PRs (skipping team members listed in a checked-in
  file), and a 30-minute cron closes labeled PRs that remain non-compliant after a 2-hour
  grace window. Contributors get a deadline and a fix path, maintainers get zero triage load,
  and the standard is enforced identically at any contribution volume. For us it is the
  reference shape for governance-as-cron: declare the rule, label the violation, time-box the
  remedy, automate the consequence.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings: []
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
---

## What It Is

Repo-level contribution governance implemented as two GitHub Actions workflows. `pr-standards.yml` checks incoming PRs against the repo's standards and labels non-compliant ones `needs:compliance`, exempting maintainers via a checked-in `.github/TEAM_MEMBERS` file. `compliance-close.yml` runs on a 30-minute cron and closes any PR that has carried the label past a 2-hour grace window. The rule, the exemption list, the grace period, and the consequence are all declared in version-controlled workflow files; no maintainer is in the loop for the common case.

## Why It Matters

At community scale (opencode ships 24 localized READMEs), PR triage is where maintainer attention dies — and where standards decay, because inconsistent human enforcement teaches contributors the rules are soft. The pattern's parts each carry weight: **labeling** separates detection from consequence, giving contributors a visible, fixable state rather than an instant rejection; the **time-box** converts "a maintainer will get to it" into a deterministic deadline; the **cron consequence** makes enforcement volume-independent; and the **checked-in exemption file** makes even the exceptions auditable. It is governance shifted from attention to mechanism — the same move agent-facing policy engines make, applied to the human contribution surface.

## Why People Are Using It

Observed in [opencode](https://github.com/anomalyco/opencode) dev branch (`34e5809`, 2026-07-11) — see [[opencode-analysis]] for structural details. It backs an explicit CONTRIBUTING.md scope boundary ("PRs that ignore these guardrails will likely be closed"), so the social contract and the mechanism state the same rule.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Maintainer triage | Humans review and close non-compliant PRs | Low volume; standards requiring judgment, not checks |
| Hard CI gate only | Non-compliant PRs just fail checks, stay open forever | When open-but-red PRs are acceptable clutter |
| PR templates + hope | Declare standards, enforce nothing | Very small communities where norms self-enforce |

## Potential Improvements

- Bot comment on labeling that enumerates the exact failed checks and the deadline, so the grace window is actionable
- Reopen-on-fix automation, making closure genuinely reversible rather than socially final

## Potential Failure Modes

- **False-positive hostility:** a buggy compliance check auto-closing legitimate PRs burns contributor goodwill at machine speed
- **Judgment-shaped rules:** standards that need human interpretation ("design review required") can't be cron-enforced without misfires
- **2-hour window mismatch:** contributors in other timezones may never see the label before closure; the grace period must fit the community's response latency
