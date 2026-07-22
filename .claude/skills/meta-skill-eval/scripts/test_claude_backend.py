#!/usr/bin/env python3
"""Deterministic contract tests for the Claude Code eval backend (engine port)."""

from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
from pathlib import Path


RUNNER = Path(__file__).with_name("eval_runner.py")
SPEC = importlib.util.spec_from_file_location("eval_runner", RUNNER)
runner = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(runner)


def main() -> None:
    workspace = Path("/tmp/example-eval-workspace")
    final = Path("/tmp/example-final.json")
    cmd = runner.build_claude_command(
        "/usr/local/bin/claude",
        {"query": "evaluate this", "allow_tools": []},
        "claude-test",
        "high",
        workspace,
        final,
    )
    required = {
        "-p", "--verbose", "--output-format", "stream-json",
        "--setting-sources", "project", "--model", "claude-test",
        "--permission-mode", "default", "--disallowedTools",
    }
    assert required.issubset(set(cmd)), cmd
    assert "--effort" in cmd and "high" in cmd
    assert cmd[-1] == "evaluate this"

    write_cmd = runner.build_claude_command(
        "/usr/local/bin/claude",
        {"query": "mutate this", "allow_tools": ["write"]},
        "claude-test",
        None,
        workspace,
        final,
    )
    assert "acceptEdits" in write_cmd and "--disallowedTools" not in write_cmd
    assert "--effort" not in write_cmd

    assert runner.resolve_case_model("flag-model", {"model": "case-model"}, "set-model") == "flag-model"
    assert runner.resolve_case_model(None, {"model": "case-model"}, "set-model") == "case-model"

    # Claude stream-json: prose never counts; init event = evidence available.
    prose_only = json.dumps({
        "type": "assistant",
        "message": {"content": [{"type": "text", "text": "I am using meta-skill-eval."}]},
    })
    assert runner.parse_skills_loaded(prose_only) == ([], False)

    init_only = json.dumps({"type": "system", "subtype": "init", "tools": ["Skill"]})
    assert runner.parse_skills_loaded(init_only) == ([], True)

    skill_call = "\n".join([
        init_only,
        json.dumps({
            "type": "assistant",
            "message": {"content": [
                {"type": "tool_use", "name": "Skill",
                 "input": {"skill": "transcript-fetcher"}},
            ]},
        }),
    ])
    assert runner.parse_skills_loaded(skill_call) == (["transcript-fetcher"], True)

    slash_input = json.dumps({
        "type": "assistant",
        "message": {"content": [
            {"type": "tool_use", "name": "Skill",
             "input": {"command": "/link-intake run the batch"}},
        ]},
    })
    assert runner.parse_skills_loaded(slash_input) == (["link-intake"], True)

    # Legacy upstream Codex envelopes still honored (mixed-ledger compatibility).
    explicit = json.dumps({"type": "skill.loaded", "skill": "meta-skill-eval"})
    assert runner.parse_skills_loaded(explicit) == (["meta-skill-eval"], True)

    ungradeable, checks = runner.verdict_for(
        {"tier": "trigger", "should_trigger": False},
        "trigger",
        {"skills_loaded": [], "skill_evidence_available": False},
        "meta-skill-eval",
    )
    assert not ungradeable
    assert checks[0]["error"] == "structured skill-load evidence unavailable"

    # Final-response extraction from the stream's result event.
    ok_stream = "\n".join([
        init_only,
        json.dumps({"type": "result", "subtype": "success", "result": "bounded answer"}),
    ])
    assert runner.extract_final_response(ok_stream) == ("bounded answer", True)
    assert runner.extract_final_response(init_only) == ("", False)
    err_stream = json.dumps({"type": "result", "subtype": "error_max_turns", "result": "x"})
    assert runner.extract_final_response(err_stream) == ("", False)
    double = "\n".join([
        json.dumps({"type": "result", "subtype": "success", "result": "a"}),
        json.dumps({"type": "result", "subtype": "success", "result": "b"}),
    ])
    assert runner.extract_final_response(double) == ("", False)

    temp = Path(tempfile.mkdtemp(prefix="claude-final-test-"))
    try:
        final_path = temp / "final.json"
        final_path.write_text(json.dumps({"response": "bounded answer"}))
        assert runner.parse_final_response(final_path) == ("bounded answer", True)
        final_path.write_text("not-json")
        assert runner.parse_final_response(final_path) == ("", False)
        final_path.write_text(json.dumps({"response": "x", "extra": True}))
        assert runner.parse_final_response(final_path) == ("", False)
    finally:
        shutil.rmtree(temp, ignore_errors=True)

    # Isolated workspace: both rosters masked, hooks/config never materialized.
    isolated = runner.make_isolated_workspace("meta-skill-eval", allow_write=False)
    try:
        engine_roster = isolated / "systems" / "improvement-loop" / ".claude" / "skills"
        assert not (engine_roster / "meta-skill-eval").exists()
        assert (engine_roster / "meta-skill-author").exists()
        assert (isolated / ".claude" / "skills" / "session-handoff").exists()
        assert not (isolated / ".claude" / "settings.json").exists()
        assert not (isolated / ".claude" / "settings.local.json").exists()
        assert not (isolated / ".claude" / "worktrees").exists()
    finally:
        shutil.rmtree(isolated, ignore_errors=True)

    write_isolated = runner.make_isolated_workspace("meta-skill-eval", allow_write=True)
    try:
        live_target = runner.SKILLS_DIR / "meta-skill-author"
        copied_target = (
            write_isolated / "systems" / "improvement-loop" / ".claude" / "skills" / "meta-skill-author"
        )
        assert copied_target.is_dir() and not copied_target.is_symlink()
        assert copied_target.resolve() != live_target.resolve()
    finally:
        shutil.rmtree(write_isolated, ignore_errors=True)

    print("claude backend tests: PASS")


if __name__ == "__main__":
    main()
