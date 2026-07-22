#!/usr/bin/env python3
"""meta-skill-eval runner — executes structured eval-cases through the real Claude Code CLI.

Subcommands:
  run     Execute a skill's eval-cases (tiers: trigger, execution, retirement).
          Appends fully-attributed rows to the ledger; saves per-run transcripts.
  report  Read-only ledger queries: pass rates, graduation, saturation, retirement.
  sync    Deterministic corpus-sync check: eval-cases cover the real phrasings
          logged in operations/self/eval-candidates.md. Exit 1 on drift.

Design: upstream CareerBuddy system/plans/skill-eval-harness.md (MV46); backend
ported from `codex exec` to the Claude Code CLI in this engine copy — see the
package ADAPTATION.md for every divergence. Schmid-style native harness —
prompt-sets as data, central CHECK_REGISTRY, real-CLI subprocess, trials,
outcome-not-path grading. Every run costs real tokens: default scope is one skill;
a --max-runs cap aborts oversized runs before anything executes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML required: .venv/bin/python -m pip install pyyaml")

HARNESS_VERSION = "2.0.0-claude.1"
REPO_ROOT = Path(__file__).resolve().parents[6]    # MetaSystem workspace root
ENGINE_ROOT = Path(__file__).resolve().parents[4]  # systems/improvement-loop
SKILLS_DIR = ENGINE_ROOT / ".claude" / "skills"            # engine roster (primary)
WORKSPACE_SKILLS_DIR = REPO_ROOT / ".claude" / "skills"    # cross-system roster
MODEL_POLICY = Path(__file__).resolve().parents[1] / "references" / "model-policy.yaml"
ADVERSARIAL_PACK = Path(__file__).resolve().parents[1] / "references" / "adversarial-pack.yaml"
EVALS_HOME = ENGINE_ROOT / "operations" / "evals"
LEDGER = EVALS_HOME / "ledger.jsonl"
TRANSCRIPTS = EVALS_HOME / "transcripts"
CORPUS = ENGINE_ROOT / "operations" / "self" / "eval-candidates.md"
DEFAULT_TIMEOUT_S = 300  # heavyweight near-miss cases legitimately run ~180s (t11, 2026-07-20)
DEFAULT_TRIALS = 3
DEFAULT_MAX_RUNS = 30
FAILURE_CATEGORIES = {
    "incomplete-solution",
    "missing-output",
    "specification-violation",
    "below-threshold-quality",
    "domain-knowledge-gap",
    "safety-or-governance",
    "runtime-error",
    "uncategorized",
}
VALUE_CLASSES = {"capability-uplift", "encoded-preference"}


def resolve_model(explicit, data, skill):
    """Model resolution: --model > eval-set `model:` > optional policy default.

    Policy principle: evals run under the model the skill actually runs with
    in real usage (references/model-policy.yaml) — never a flat cheap default.
    """
    policy = yaml.safe_load(MODEL_POLICY.read_text()) if MODEL_POLICY.exists() else {}
    default_effort = policy.get("default_effort")
    if explicit:
        return explicit, "flag", default_effort
    if data.get("model"):
        return data["model"], "eval-set", default_effort
    if policy.get("default"):
        return policy["default"], "policy-default", default_effort
    sys.exit("No model resolved: pass --model (personal CLI defaults stay user-scoped)")


def resolve_case_model(explicit: str | None, case: dict, resolved: str) -> str:
    """Preserve documented flag > case/set model precedence."""
    return explicit or case.get("model") or resolved

# --------------------------------------------------------------------------- CLI plumbing


def resolve_claude_bin(explicit: str | None) -> str:
    """Find a real Claude Code CLI binary."""
    candidates = []
    if explicit:
        candidates.append(explicit)
    if os.environ.get("CLAUDE_BIN"):
        candidates.append(os.environ["CLAUDE_BIN"])
    which = shutil.which("claude")
    if which:
        candidates.append(which)
    candidates.append(str(Path.home() / ".claude" / "local" / "claude"))
    candidates.append("/opt/homebrew/bin/claude")
    for cand in candidates:
        path = Path(cand).expanduser()
        if path.is_file() and os.access(path, os.X_OK):
            return str(path)
    sys.exit("No Claude Code CLI found: install Claude Code or pass --claude-bin")


# --------------------------------------------------------------------------- case loading


def skill_dir(skill: str) -> Path:
    """Engine roster first, workspace cross-system roster second (DD-109 layout)."""
    for roster in (SKILLS_DIR, WORKSPACE_SKILLS_DIR):
        d = roster / skill
        if d.is_dir():
            return d
    sys.exit(f"Unknown skill: {skill} (no dir under {SKILLS_DIR} or {WORKSPACE_SKILLS_DIR})")


def load_cases(skill: str) -> dict:
    if skill == "_shared":
        # The shared adversarial pack (MV48 G): harness-level probes, not a
        # skill package. Run as a pre-install / pre-export gate, never scheduled.
        if not ADVERSARIAL_PACK.exists():
            sys.exit(f"Adversarial pack not found: {ADVERSARIAL_PACK}")
        return yaml.safe_load(ADVERSARIAL_PACK.read_text())
    path = skill_dir(skill) / "evals" / "eval-cases.yaml"
    if not path.exists():
        sys.exit(f"No eval-cases.yaml for {skill} (expected {path})")
    data = yaml.safe_load(path.read_text())
    for key in ("skill", "version", "updated", "cases"):
        if key not in data:
            sys.exit(f"{path}: missing required key '{key}' (version and updated are paired)")
    if data["skill"] != skill:
        sys.exit(f"{path}: skill field '{data['skill']}' != directory '{skill}'")
    if data.get("value_class") and data["value_class"] not in VALUE_CLASSES:
        sys.exit(f"{path}: invalid value_class '{data['value_class']}'")
    for case in data["cases"]:
        category = case.get("failure_category")
        if category and category not in FAILURE_CATEGORIES:
            sys.exit(f"{path}: case {case.get('id', '?')} has invalid failure_category '{category}'")
    return data


def skill_version(skill: str) -> str:
    """metadata.version from the target skill's SKILL.md frontmatter."""
    text = (skill_dir(skill) / "SKILL.md").read_text()
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if match:
        try:
            front = yaml.safe_load(match.group(1))
            return str((front.get("metadata") or {}).get("version", "unknown"))
        except yaml.YAMLError:
            pass
    return "unknown"


# --------------------------------------------------------------------------- check registry

CHECK_REGISTRY = {}


def check(name):
    def deco(fn):
        CHECK_REGISTRY[name] = fn
        return fn

    return deco


@check("skill_loaded")
def _skill_loaded(spec, ctx):
    return spec["skill"] in ctx["skills_loaded"]


@check("skill_not_loaded")
def _skill_not_loaded(spec, ctx):
    return spec["skill"] not in ctx["skills_loaded"]


@check("transcript_contains")
def _transcript_contains(spec, ctx):
    return re.search(spec["pattern"], ctx["transcript"]) is not None


@check("transcript_not_contains")
def _transcript_not_contains(spec, ctx):
    return re.search(spec["pattern"], ctx["transcript"]) is None


@check("response_contains")
def _response_contains(spec, ctx):
    return re.search(spec["pattern"], ctx["response"]) is not None


@check("response_not_contains")
def _response_not_contains(spec, ctx):
    return re.search(spec["pattern"], ctx["response"]) is None


@check("exit_zero")
def _exit_zero(spec, ctx):
    return ctx["exit_code"] == 0


BAN_TERMS_FILE = REPO_ROOT / ".claude" / "export-ban-terms.txt"


@check("no_ban_terms")
def _no_ban_terms(spec, ctx):
    """Leakage probe (MV48 G): no export-ban term appears in response or transcript.

    The ban-terms file is local-only (never exported). On a host without it the
    probe is vacuous — there is no private content to leak — so it passes.
    """
    if not BAN_TERMS_FILE.exists():
        return True
    terms = [
        t.strip() for t in BAN_TERMS_FILE.read_text().splitlines()
        if t.strip() and not t.startswith("#")
    ]
    haystack = (ctx["response"] + "\n" + ctx["transcript"]).lower()
    return not any(t.lower() in haystack for t in terms)


def run_checks(specs, ctx):
    results = []
    for spec in specs:
        fn = CHECK_REGISTRY.get(spec.get("check"))
        if fn is None:
            results.append({"check": spec.get("check"), "pass": False, "error": "unknown check"})
            continue
        try:
            ok = bool(fn(spec, ctx))
        except (re.error, KeyError) as exc:
            results.append({"check": spec["check"], "pass": False, "error": str(exc)})
            continue
        results.append({"check": spec["check"], "pass": ok})
    return results


# --------------------------------------------------------------------------- execution

EXPLICIT_SKILL_EVENT_TYPES = {"skill.loaded", "skill_load", "skill_load.completed"}
EXPLICIT_SKILL_ITEM_TYPES = {"skill", "skill_load", "skill_loaded"}


def parse_skills_loaded(transcript: str) -> tuple[list[str], bool]:
    """Return only explicit structured skill-load evidence from the stream-json transcript.

    Claude Code backend: skill invocations appear as `tool_use` blocks named
    "Skill" inside assistant events. Evidence counts as available once the
    stream's `system`/`init` event has parsed — in that format every tool call
    is present, so the absence of a Skill call is a genuine abstention, not
    missing instrumentation. Agent prose such as "I am using X" is intentionally
    ignored. The upstream Codex envelopes (`skill.loaded` / item-typed) are still
    honored so upstream fixtures and mixed ledgers keep working.
    """
    loaded = set()
    evidence_available = False
    for line in transcript.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        event_type = event.get("type")
        if event_type == "system" and event.get("subtype") == "init":
            evidence_available = True
        if event_type == "assistant":
            message = event.get("message") if isinstance(event.get("message"), dict) else {}
            for block in message.get("content") or []:
                if (
                    isinstance(block, dict)
                    and block.get("type") == "tool_use"
                    and block.get("name") == "Skill"
                ):
                    evidence_available = True
                    inp = block.get("input") if isinstance(block.get("input"), dict) else {}
                    name = inp.get("skill") or inp.get("command")
                    if isinstance(name, str) and name.strip():
                        loaded.add(name.strip().lstrip("/").split()[0])
        item = event.get("item") if isinstance(event.get("item"), dict) else {}
        if event_type in EXPLICIT_SKILL_EVENT_TYPES:
            evidence_available = True
            name = event.get("skill") or event.get("name")
            if isinstance(name, str):
                loaded.add(name)
        if item.get("type") in EXPLICIT_SKILL_ITEM_TYPES:
            evidence_available = True
            name = item.get("skill") or item.get("name")
            if isinstance(name, str):
                loaded.add(name)
    return sorted(loaded), evidence_available


def make_isolated_workspace(mask_skill: str | None, allow_write: bool) -> Path:
    """Build a per-trial workspace with harness hooks/config excluded (engine layout).

    Read-only trials use a symlink mirror. Write-enabled trials receive copies,
    so a mutating run cannot follow a link into the live repo. Both skill rosters
    (workspace `.claude/skills` and `systems/improvement-loop/.claude/skills`,
    DD-109) are rebuilt minus the masked skill; harness settings files (hooks)
    and worktrees are never materialized, so the isolated session runs hook-free.
    Retirement trials omit the target skill from both discovery paths.
    """
    tmp = Path(tempfile.mkdtemp(prefix="claude-eval-workspace-"))
    excluded = {".git", ".venv", "__pycache__", "node_modules"}
    claude_excluded = {"settings.json", "settings.local.json", "worktrees"}

    def place(src: Path, dst: Path):
        if allow_write:
            if src.is_dir():
                shutil.copytree(
                    src, dst, symlinks=False, ignore_dangling_symlinks=True
                )
            else:
                shutil.copy2(src, dst)
        else:
            dst.symlink_to(src, target_is_directory=src.is_dir())

    def build_claude_dir(src: Path, dst: Path):
        dst.mkdir()
        for sub in src.iterdir():
            if sub.name in claude_excluded:
                continue
            if sub.name == "skills":
                roster = dst / "skills"
                roster.mkdir()
                for skill_entry in sub.iterdir():
                    if skill_entry.name != mask_skill:
                        place(skill_entry, roster / skill_entry.name)
            else:
                place(sub, dst / sub.name)

    for entry in REPO_ROOT.iterdir():
        if entry.name in excluded:
            continue
        if entry.name == ".claude":
            build_claude_dir(entry, tmp / ".claude")
        elif entry.name == "systems":
            systems = tmp / "systems"
            systems.mkdir()
            for sys_entry in entry.iterdir():
                if sys_entry.name in excluded:
                    continue
                if (sys_entry / ".claude").is_dir():
                    sys_dst = systems / sys_entry.name
                    sys_dst.mkdir()
                    for sub in sys_entry.iterdir():
                        if sub.name in excluded:
                            continue
                        if sub.name == ".claude":
                            build_claude_dir(sub, sys_dst / ".claude")
                        else:
                            place(sub, sys_dst / sub.name)
                else:
                    place(sys_entry, systems / sys_entry.name)
        else:
            place(entry, tmp / entry.name)
    return tmp


def build_claude_command(bin_, case, model, effort, workspace, final_path):
    """Claude Code headless invocation (backend port; upstream ran `codex exec`).

    Isolation: `--setting-sources project` ignores user-level config, and the
    isolated workspace materializes no settings files, so no hooks fire.
    Sandboxing: non-interactive print mode auto-denies any tool that would
    prompt; read-only cases additionally disallow the mutating file tools
    (stricter than Codex's read-only sandbox, which allowed shell reads — here
    reads go through Read/Grep/Glob), write cases run acceptEdits inside their
    copied workspace. `workspace` is applied as the subprocess cwd; `final_path`
    is written by the runner from the stream's result event (the Claude CLI has
    no --output-schema/--output-last-message analog).
    """
    allow_write = "write" in (case.get("allow_tools") or [])
    del workspace, final_path  # cwd + post-run extraction; kept for signature parity
    cmd = [
        bin_, "-p", "--verbose", "--output-format", "stream-json",
        "--setting-sources", "project",
        "--model", model,
    ]
    if allow_write:
        cmd += ["--permission-mode", "acceptEdits"]
    else:
        cmd += [
            "--permission-mode", "default",
            "--disallowedTools", "Write,Edit,NotebookEdit",
        ]
    if effort:
        cmd += ["--effort", effort]
    cmd.append(case["query"])
    return cmd


def extract_final_response(transcript: str) -> tuple[str, bool]:
    """Final response from the stream's single `result` event (backend port).

    Upstream Codex enforced a {"response": str} output schema model-side; the
    Claude CLI has no output-schema flag, so validity here means: exactly one
    result event, subtype `success`, with a string result payload. The runner
    persists the extracted payload to the `.final.json` artifact for parity.
    """
    results = []
    for line in transcript.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and event.get("type") == "result":
            results.append(event)
    if len(results) != 1:
        return "", False
    event = results[0]
    if event.get("subtype") == "success" and isinstance(event.get("result"), str):
        return event["result"], True
    return "", False


def parse_final_response(final_path: Path) -> tuple[str, bool]:
    """Validate the persisted `.final.json` artifact ({"response": str} exactly)."""
    if not final_path.exists():
        return "", False
    text = final_path.read_text(errors="replace")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        return "", False
    valid = (
        isinstance(payload, dict)
        and set(payload) == {"response"}
        and isinstance(payload["response"], str)
    )
    return (payload["response"], True) if valid else ("", False)


def run_case(bin_, case, model, effort, mask_skill, transcript_path, timeout_s):
    allow_write = "write" in (case.get("allow_tools") or [])
    workspace = make_isolated_workspace(mask_skill, allow_write)
    transcript_path = Path(transcript_path)
    final_path = transcript_path.with_suffix(".final.json")
    stderr_path = transcript_path.with_suffix(".stderr.txt")
    cmd = build_claude_command(bin_, case, model, effort, workspace, final_path)
    start = time.monotonic()
    try:
        proc = subprocess.run(
            cmd,
            cwd=workspace,
            capture_output=True,
            text=True,
            timeout=timeout_s,
            stdin=subprocess.DEVNULL,
        )
        exit_code, transcript, stderr = proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        exit_code = -1
        transcript = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(transcript, bytes):
            transcript = transcript.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
    finally:
        duration = round(time.monotonic() - start, 1)
    transcript_path.write_text(transcript)
    if stderr:
        stderr_path.write_text(stderr)
    skills_loaded, skill_evidence_available = parse_skills_loaded(transcript)
    if exit_code == -1:
        response, final_schema_valid = "<timeout>", False
    else:
        response, final_schema_valid = extract_final_response(transcript)
        if final_schema_valid:
            final_path.write_text(json.dumps({"response": response}))
    shutil.rmtree(workspace, ignore_errors=True)
    return {
        "exit_code": exit_code,
        "response": response,
        "transcript": transcript,
        "skills_loaded": skills_loaded,
        "skill_evidence_available": skill_evidence_available,
        "final_schema_valid": final_schema_valid,
        "duration_s": duration,
        "stderr_path": stderr_path if stderr else None,
    }


def verdict_for(case, run_tier, ctx, target_skill):
    # Grade by the CASE's tier (retirement runs override: execution cases,
    # skill masked). Bug fixed in 1.0.1: grading by the CLI filter sent
    # trigger cases through the checks branch with zero checks = vacuous pass.
    tier = "retirement" if run_tier == "retirement" else case.get("tier", "execution")
    if tier == "trigger":
        if not ctx["skill_evidence_available"]:
            return False, [{
                "check": "trigger_match", "pass": False,
                "error": "structured skill-load evidence unavailable",
            }]
        loaded = target_skill in ctx["skills_loaded"]
        expected = case.get("should_trigger", True)
        return loaded == expected, [
            {"check": "trigger_match", "pass": loaded == expected, "loaded": loaded}
        ]
    specs = case.get("checks", [])
    if any(s.get("check") in {"skill_loaded", "skill_not_loaded"} for s in specs) \
            and not ctx["skill_evidence_available"]:
        return False, [{
            "check": "skill-load-evidence", "pass": False,
            "error": "structured skill-load evidence unavailable",
        }]
    checks = run_checks(specs, ctx)
    if not checks:
        return False, [{"check": "none-defined", "pass": False, "error": "execution case without checks"}]
    return all(c["pass"] for c in checks), checks


def cmd_run(args):
    skill = args.skill
    data = load_cases(skill)
    if data.get("harness") == "excluded":
        sys.exit(
            f"{skill} is harness-excluded (eval-cases.yaml `harness: excluded`) — "
            "pure tool-wrappers earn no paid LLM runs; their script tests own "
            "correctness. Edit the field (human-gated) if this changed."
        )
    tiers = {args.tier} if args.tier != "all" else {"trigger", "execution"}
    cases = [
        c
        for c in data["cases"]
        if (c.get("tier", "execution") in tiers or args.tier == "retirement")
        and (not args.cases or c["id"] in args.cases)
    ]
    if args.tier == "retirement":
        cases = [c for c in cases if c.get("tier") == "execution"]
    if not cases:
        sys.exit("No cases match the tier/id filter.")
    planned = len(cases) * args.trials
    if planned > args.max_runs:
        sys.exit(
            f"Refusing: {planned} runs planned > --max-runs {args.max_runs}. "
            "Every run is real tokens — raise the cap explicitly if intended."
        )

    sk_version = "-" if skill == "_shared" else skill_version(skill)
    model, model_source, policy_effort = resolve_model(args.model, data, skill)
    effort = args.effort or policy_effort  # None -> CLI default, recorded as such

    if args.dry_run:
        for case in cases:
            mode = (
                "acceptEdits" if "write" in (case.get("allow_tools") or [])
                else "default+no-file-writes"
            )
            print(
                f"DRY {case['id']} x{args.trials}: claude -p --output-format stream-json "
                f"--permission-mode {mode} --model {resolve_case_model(args.model, case, model)} "
                f"({case['query'][:70]})"
            )
        return

    bin_ = resolve_claude_bin(args.claude_bin)
    version_proc = subprocess.run(
        [bin_, "--version"], capture_output=True, text=True, timeout=10
    )
    cli_version = version_proc.stdout.strip() or version_proc.stderr.strip() or "unknown"
    run_id = dt.datetime.now(dt.UTC).strftime("%Y%m%d-%H%M%S") + f"-{skill}-{args.tier}"
    tdir = TRANSCRIPTS / run_id
    tdir.mkdir(parents=True, exist_ok=True)
    LEDGER.parent.mkdir(parents=True, exist_ok=True)

    print(
        f"run {run_id}: {len(cases)} cases x {args.trials} trials, "
        f"model={model} ({model_source}), effort={effort or 'cli-default'}, cli={cli_version}"
    )
    passes = 0
    errors = 0
    with LEDGER.open("a") as ledger:
        for case in cases:
            case_model = resolve_case_model(args.model, case, model)
            for trial in range(1, args.trials + 1):
                print(f"  {case['id']} t{trial}: running...", flush=True)
                tpath = tdir / f"{case['id']}-t{trial}.jsonl"
                ctx = run_case(
                    bin_, case, case_model, effort,
                    skill if args.tier == "retirement" else None,
                    str(tpath), args.timeout,
                )
                if ctx["exit_code"] != 0:
                    # CLI/auth/runtime failure: absence of evidence is never graded.
                    ok, checks, verdict = False, [{
                        "check": "cli-exit", "pass": False,
                        "error": "timeout" if ctx["exit_code"] == -1 else f"claude exit {ctx['exit_code']}",
                    }], "error"
                    errors += 1
                elif not ctx["final_schema_valid"]:
                    ok, checks, verdict = False, [{
                        "check": "final-schema", "pass": False,
                        "error": "missing or invalid schema-constrained final output",
                    }], "error"
                    errors += 1
                else:
                    ok, checks = verdict_for(case, args.tier, ctx, skill)
                    ungradeable = any(c.get("error") == "structured skill-load evidence unavailable" for c in checks)
                    verdict = "error" if ungradeable else "pass" if ok else "fail"
                    errors += int(ungradeable)
                passes += ok
                row = {
                        "ts": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
                        "run_id": run_id,
                        "harness": "claude-code",
                        "cli_version": cli_version,
                        "skill": skill,
                        "skill_version": sk_version,
                        "eval_set_version": data["version"],
                        "harness_version": HARNESS_VERSION,
                        "model": case_model,
                        "model_source": model_source if case_model == model else "case",
                        "effort": effort or "cli-default",
                        "case_id": case["id"],
                        "value_class": data.get("value_class", "unspecified"),
                        "tier": args.tier if args.tier == "retirement" else case.get("tier", "execution"),
                        "trial": trial,
                        "verdict": verdict,
                        "failure_category": (
                            "runtime-error" if verdict == "error"
                            else case.get("failure_category", "uncategorized") if verdict == "fail"
                            else None
                        ),
                        "checks": checks,
                        "skills_loaded": ctx["skills_loaded"],
                        "skill_evidence": (
                            "structured" if ctx["skill_evidence_available"] else "unavailable"
                        ),
                        "final_schema_valid": ctx["final_schema_valid"],
                        "duration_s": ctx["duration_s"],
                        "exit_code": ctx["exit_code"],
                        "transcript": str(tpath.relative_to(REPO_ROOT)),
                        "stderr": (
                            str(ctx["stderr_path"].relative_to(REPO_ROOT))
                            if ctx["stderr_path"] else None
                        ),
                }
                ledger.write(json.dumps(row) + "\n")
                ledger.flush()
                print(
                    f"  {case['id']} t{trial}: {verdict.upper()} "
                    f"({ctx['duration_s']}s, skill-evidence={row['skill_evidence']})",
                    flush=True,
                )
    total = len(cases) * args.trials
    note = f", {errors} error" if errors else ""
    print(f"done: {passes}/{total} pass{note} -> {LEDGER.relative_to(REPO_ROOT)}")
    sys.exit(0 if passes == total else 1)


# --------------------------------------------------------------------------- report


def cmd_report(args):
    if not LEDGER.exists():
        sys.exit("No ledger yet — nothing has run.")
    rows = [json.loads(line) for line in LEDGER.read_text().splitlines() if line.strip()]
    if args.skill:
        rows = [r for r in rows if r["skill"] == args.skill]
    if not rows:
        sys.exit("No matching rows.")
    if getattr(args, "paired", False):
        return report_paired(rows)
    if getattr(args, "efficiency", False):
        return report_efficiency(rows, args)
    by_key = {}
    for r in rows:
        key = (r["skill"], r["tier"], r["model"], r.get("effort", "cli-default"))
        by_key.setdefault(key, []).append(r)
    print(f"{'skill':<24} {'tier':<11} {'model':<20} {'effort':<12} {'latest':>7} {'runs':>5}  label")
    for (skill, tier, model, effort), grp in sorted(by_key.items()):
        run_ids = sorted({g["run_id"] for g in grp})
        rates = []
        for rid in run_ids:
            sub = [g for g in grp if g["run_id"] == rid]
            rates.append(sum(g["verdict"] == "pass" for g in sub) / len(sub))
        latest = rates[-1]
        if tier == "retirement":
            label = "RETIRE-SIGNAL" if latest >= 0.8 else "still-needed"
        elif len(rates) >= 2 and rates[-1] == rates[-2] == 1.0:
            label = "regression" + (" (saturated)" if len(rates) >= 3 and rates[-3] == 1.0 else "")
        else:
            label = "capability"
        print(f"{skill:<24} {tier:<11} {model:<20} {effort:<12} {latest:>6.0%} {len(run_ids):>5}  {label}")


def _row_passed(row: dict) -> bool:
    if row.get("verdict") == "pass":
        return True
    if row.get("verdict") == "human-scored":
        return bool((row.get("judge_verdict") or {}).get("overall_pass"))
    return False


def _dedupe_grades(rows: list[dict]) -> list[dict]:
    """One grade per case/trial; a human score supersedes its advisory run row."""
    grades: dict[tuple[str, int], dict] = {}
    for row in rows:
        key = (row["case_id"], row.get("trial", 1))
        current = grades.get(key)
        if current is None or row.get("verdict") == "human-scored":
            grades[key] = row
    return list(grades.values())


def report_paired(rows: list[dict]) -> None:
    """Report latest matched execution vs skill-masked output uplift.

    Only case ids present in both latest runs are compared. This prevents an
    unmatched case roster from manufacturing uplift. Trigger rows are irrelevant.
    """
    groups: dict[tuple[str, str], dict[str, list[dict]]] = {}
    for row in rows:
        if row.get("tier") not in {"execution", "retirement"}:
            continue
        key = (row["skill"], row["model"])
        groups.setdefault(key, {}).setdefault(row["tier"], []).append(row)

    reported = False
    print(f"{'skill':<24} {'model':<20} {'cases':>5} {'with':>7} {'masked':>7} {'uplift':>8}  value-class")
    for (skill, model), tiers in sorted(groups.items()):
        if "execution" not in tiers or "retirement" not in tiers:
            continue
        latest = {}
        for tier in ("execution", "retirement"):
            run_id = max(row["run_id"] for row in tiers[tier])
            latest[tier] = _dedupe_grades(
                [row for row in tiers[tier] if row["run_id"] == run_id]
            )
        execution_cases = {row["case_id"] for row in latest["execution"]}
        retirement_cases = {row["case_id"] for row in latest["retirement"]}
        matched = execution_cases & retirement_cases
        if not matched:
            continue
        execution = [row for row in latest["execution"] if row["case_id"] in matched]
        retirement = [row for row in latest["retirement"] if row["case_id"] in matched]
        with_rate = sum(_row_passed(row) for row in execution) / len(execution)
        masked_rate = sum(_row_passed(row) for row in retirement) / len(retirement)
        value_class = next(
            (row.get("value_class") for row in execution if row.get("value_class")),
            "unspecified",
        )
        print(
            f"{skill:<24} {model:<20} {len(matched):>5} {with_rate:>6.0%} "
            f"{masked_rate:>6.0%} {with_rate - masked_rate:>+7.0%}  {value_class}"
        )
        reported = True
    if not reported:
        print("(no matched execution/retirement rows — run the same execution cases in both tiers)")


# --------------------------------------------------------------------------- efficiency (MV48 F)

SESSION_STORE = ENGINE_ROOT / "operations" / "self" / "session-store"
ARCHIVE_TOKENS_RE = re.compile(
    r'"(?:promptTokens|outputTokens|completionTokens)"\s*:\s*(\d+)'
)
ARCHIVE_CREDITS_RE = re.compile(r'"copilotCredits"\s*:\s*([\d.]+)')


def report_efficiency(rows, args):
    """Efficiency reads (MV48 F) — zero new instrumentation.

    Eval-run side: duration + transcript size from ledger rows and their saved
    transcripts. Real-usage side (--sessions): tokens/credits regex-mined from the
    transcript archive where recorded; hosts without the archive skip that table.
    """
    by_key = {}
    for r in rows:
        key = (r["skill"], r["tier"], r["model"])
        by_key.setdefault(key, []).append(r)
    print(f"{'skill':<24} {'tier':<11} {'model':<20} {'runs':>5} {'avg s':>7} {'avg transcript KB':>18}")
    for (skill, tier, model), grp in sorted(by_key.items()):
        durs = [g["duration_s"] for g in grp if isinstance(g.get("duration_s"), (int, float))]
        sizes = []
        for g in grp:
            tp = REPO_ROOT / g.get("transcript", "")
            if g.get("transcript") and tp.exists():
                sizes.append(tp.stat().st_size / 1024)
        avg_d = sum(durs) / len(durs) if durs else 0.0
        avg_kb = sum(sizes) / len(sizes) if sizes else 0.0
        print(f"{skill:<24} {tier:<11} {model:<20} {len(grp):>5} {avg_d:>7.1f} {avg_kb:>18.1f}")
    if getattr(args, "sessions", False):
        if not SESSION_STORE.exists():
            print("\n(no transcript archive on this host — real-usage table skipped)")
            return
        print(f"\n{'session':<40} {'tokens':>12} {'credits':>9}")
        for f in sorted(SESSION_STORE.glob("*.jsonl")):
            text = f.read_text(errors="replace")
            tokens = sum(int(m) for m in ARCHIVE_TOKENS_RE.findall(text))
            credits = sum(float(m) for m in ARCHIVE_CREDITS_RE.findall(text))
            if tokens or credits:
                print(f"{f.stem:<40} {tokens:>12,} {credits:>9.2f}")


# --------------------------------------------------------------------------- score (MV48 D)


def cmd_score(args):
    """Append a human scorecard verdict for a hitl case as an attributed ledger row.

    Judge-verdict schema v1 (references/judge-verdict-schema.md): subjective-class
    output quality is human-scored; this records the score so subjective skills
    trend in the ledger like everyone else. The row references the scored run.
    """
    if not LEDGER.exists():
        sys.exit("No ledger yet — nothing to score.")
    rows = [json.loads(l) for l in LEDGER.read_text().splitlines() if l.strip()]
    ref = [
        r for r in rows
        if r["run_id"] == args.run_id and r["case_id"] == args.case and r.get("verdict") != "human-scored"
    ]
    if not ref:
        sys.exit(f"No ledger row for run {args.run_id} case {args.case} — score must reference a real run.")
    base = ref[-1]
    if not (0 <= args.score <= 100):
        sys.exit("--score must be 0–100")
    overall_pass = args.score >= args.pass_threshold
    failure_category = None if overall_pass else (
        args.failure_category or "below-threshold-quality"
    )
    row = {
        "ts": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "run_id": base["run_id"],
        "skill": base["skill"],
        "skill_version": base["skill_version"],
        "eval_set_version": base["eval_set_version"],
        "harness_version": HARNESS_VERSION,
        "model": base["model"],
        "case_id": base["case_id"],
        "tier": base["tier"],
        "trial": base["trial"],
        "verdict": "human-scored",
        "failure_category": failure_category,
        "judge_verdict": {
            "version": 1,
            "overall_pass": overall_pass,
            "score": args.score,
            "failure_category": failure_category,
            "scorer": "human",
            "scorecard": args.scorecard or "",
            "checks": [{"id": "human-scorecard", "pass": args.score >= args.pass_threshold,
                        "note": args.note or ""}],
        },
        "transcript": base.get("transcript", ""),
    }
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a") as ledger:
        ledger.write(json.dumps(row) + "\n")
    print(
        f"scored: {base['skill']} {base['case_id']} (run {base['run_id']}) → "
        f"{args.score}/100 {'PASS' if row['judge_verdict']['overall_pass'] else 'FAIL'}"
    )


# --------------------------------------------------------------------------- sync

SESSION_RE = re.compile(r"session\s+([0-9a-f]{8})")


def corpus_rows(corpus: Path = CORPUS):
    """{skill: [hex8, ...]} from the eval-candidates store (quoted rows only).

    A missing corpus is not an error (MV48 portability): a fresh host — new user,
    new machine — legitimately starts with no real-phrasing corpus; sync passes
    cleanly and coverage begins accruing with the first capture.
    """
    if not corpus.exists():
        return None
    rows, current = {}, None
    for line in corpus.read_text().splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
        elif current and line.lstrip().startswith('- "'):
            m = SESSION_RE.search(line)
            if m:
                rows.setdefault(current, []).append(m.group(1))
    return rows


def cmd_sync(args):
    corpus = Path(args.corpus) if args.corpus else CORPUS
    skills_dir = Path(args.skills_dir) if args.skills_dir else SKILLS_DIR
    rows = corpus_rows(corpus)
    if rows is None:
        print(f"no corpus at {corpus} — fresh host, nothing to sync (clean pass)")
        sys.exit(0)
    if args.skill:
        rows = {k: v for k, v in rows.items() if k == args.skill}
    drift = False
    for skill, keys in sorted(rows.items()):
        path = skills_dir / skill / "evals" / "eval-cases.yaml"
        if not path.exists():
            print(f"{skill}: no eval-cases.yaml yet ({len(keys)} corpus rows waiting)")
            continue
        data = yaml.safe_load(path.read_text())
        sources = " ".join(
            str(c.get("source", "")) for c in data.get("cases", [])
        ) + " " + " ".join(data.get("corpus_waivers", []))
        missing = [k for k in set(keys) if k not in sources]
        if missing:
            drift = True
            print(f"{skill}: DRIFT — corpus rows not covered: {', '.join(sorted(missing))}")
        else:
            print(f"{skill}: in sync ({len(set(keys))} corpus rows covered)")
    sys.exit(1 if drift else 0)


# --------------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="execute eval-cases for one skill")
    p_run.add_argument("--skill", required=True)
    p_run.add_argument("--tier", choices=["trigger", "execution", "retirement", "all"], default="all")
    p_run.add_argument("--cases", type=lambda s: s.split(","), default=None)
    p_run.add_argument("--trials", type=int, default=DEFAULT_TRIALS)
    p_run.add_argument("--model", default=None, help="required unless the eval set explicitly pins one")
    p_run.add_argument("--effort", default=None, choices=["low", "medium", "high"], help="explicit reasoning effort passed to the CLI (--effort)")
    p_run.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    p_run.add_argument("--max-runs", type=int, default=DEFAULT_MAX_RUNS)
    p_run.add_argument("--claude-bin", default=None)
    p_run.add_argument("--dry-run", action="store_true")
    p_run.set_defaults(fn=cmd_run)

    p_rep = sub.add_parser("report", help="ledger pass rates + lifecycle labels")
    p_rep.add_argument("--skill", default=None)
    p_rep.add_argument("--paired", action="store_true",
                       help="latest matched with-skill vs skill-masked output uplift")
    p_rep.add_argument("--efficiency", action="store_true",
                       help="efficiency reads: avg duration + transcript size per skill×tier×model (MV48 F)")
    p_rep.add_argument("--sessions", action="store_true",
                       help="with --efficiency: add real-usage tokens/credits mined from the transcript archive")
    p_rep.set_defaults(fn=cmd_report)

    p_score = sub.add_parser("score", help="append a human scorecard verdict for a hitl case (judge-verdict schema v1)")
    p_score.add_argument("--run-id", required=True, help="the run being scored (must exist in the ledger)")
    p_score.add_argument("--case", required=True, help="case id within that run")
    p_score.add_argument("--score", type=int, required=True, help="0–100 per the skill's scorecard")
    p_score.add_argument("--pass-threshold", type=int, default=70, help="overall_pass boundary (default 70)")
    p_score.add_argument("--scorecard", default=None, help="pointer to the rubric used")
    p_score.add_argument("--failure-category", choices=sorted(FAILURE_CATEGORIES - {"runtime-error", "uncategorized"}),
                         help="typed reason for a failing subjective verdict")
    p_score.add_argument("--note", default=None)
    p_score.set_defaults(fn=cmd_score)

    p_sync = sub.add_parser("sync", help="corpus-sync drift check (exit 1 on drift)")
    p_sync.add_argument("--skill", default=None)
    p_sync.add_argument("--corpus", default=None,
                        help="override corpus path (fixture testing; default: the live store)")
    p_sync.add_argument("--skills-dir", default=None,
                        help="override skills dir (fixture testing; default: the engine roster)")
    p_sync.set_defaults(fn=cmd_sync)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
