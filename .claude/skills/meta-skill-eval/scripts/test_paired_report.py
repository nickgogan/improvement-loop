#!/usr/bin/env python3
"""Hermetic tests for paired output uplift and typed failure categories."""

import contextlib
import importlib.util
import io
import tempfile
from pathlib import Path

RUNNER = Path(__file__).resolve().parent / "eval_runner.py"
spec = importlib.util.spec_from_file_location("eval_runner", RUNNER)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def test_paired_report() -> None:
    rows = [
        {"skill": "fixture", "model": "model-a", "tier": "execution", "run_id": "run-2", "case_id": "x1", "trial": 1, "verdict": "fail", "value_class": "capability-uplift"},
        {"skill": "fixture", "model": "model-a", "tier": "execution", "run_id": "run-2", "case_id": "x1", "trial": 1, "verdict": "human-scored", "judge_verdict": {"overall_pass": True}, "value_class": "capability-uplift"},
        {"skill": "fixture", "model": "model-a", "tier": "execution", "run_id": "run-2", "case_id": "x2", "verdict": "pass", "value_class": "capability-uplift"},
        {"skill": "fixture", "model": "model-a", "tier": "retirement", "run_id": "run-1", "case_id": "x1", "verdict": "fail"},
        {"skill": "fixture", "model": "model-a", "tier": "retirement", "run_id": "run-1", "case_id": "x2", "verdict": "pass"},
    ]
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        runner.report_paired(rows)
    text = output.getvalue()
    assert "100%" in text and "50%" in text and "+50%" in text
    assert "capability-uplift" in text


def test_invalid_failure_category() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        skills = Path(temp_dir)
        evals = skills / "fixture" / "evals"
        evals.mkdir(parents=True)
        (evals / "eval-cases.yaml").write_text(
            """skill: fixture
version: 1
updated: 2026-07-20
class: objective
cases:
  - id: x1
    tier: execution
    query: fixture
    failure_category: made-up
    checks: [{check: exit_zero}]
"""
        )
        previous = runner.SKILLS_DIR
        runner.SKILLS_DIR = skills
        try:
            try:
                runner.load_cases("fixture")
            except SystemExit as error:
                assert "invalid failure_category" in str(error)
            else:
                raise AssertionError("invalid failure category was accepted")
        finally:
            runner.SKILLS_DIR = previous


if __name__ == "__main__":
    test_paired_report()
    test_invalid_failure_category()
    print("test_paired_report: PASS")
