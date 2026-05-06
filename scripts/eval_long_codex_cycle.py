#!/usr/bin/env python3
"""Smoke-test the Long Codex cycle with `codex exec --json`.

The eval runs in a temporary copy of the repo and verifies that a tiny
long-codex-cycle run updates durable state and leaves a log.
"""

from __future__ import annotations

import argparse
from collections import Counter
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "evals" / "long_codex_cycle_smoke.md"
STATUS_MARKER = "EVAL_SMOKE_MARKER"
LOG_MARKER = "EVAL_SMOKE_LOG"
FINAL_MARKER = "EVAL_SMOKE_DONE"
DEFAULT_SUMMARY = ROOT / "evals" / "last_long_codex_cycle_smoke_summary.json"


def run(cmd: list[str], cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def copy_repo(destination: Path) -> None:
    def ignore(_dir: str, names: list[str]) -> set[str]:
        ignored = {".git", "__pycache__"}
        return {name for name in names if name in ignored}

    shutil.copytree(ROOT, destination, ignore=ignore)


def init_temp_git(repo: Path) -> None:
    commands = [
        ["git", "init", "-q"],
        ["git", "config", "user.name", "Long Codex Eval"],
        ["git", "config", "user.email", "long-codex-eval@example.invalid"],
        ["git", "add", "."],
        ["git", "commit", "-q", "-m", "baseline"],
    ]
    for command in commands:
        result = run(command, cwd=repo)
        require(result.returncode == 0, f"{' '.join(command)} failed:\n{result.stderr}")


def build_command(repo: Path, final_message: Path, model: str | None) -> list[str]:
    command = [
        "codex",
        "exec",
        "--json",
        "--cd",
        str(repo),
        "--sandbox",
        "workspace-write",
        "-c",
        'approval_policy="never"',
        "-c",
        'model_reasoning_effort="low"',
        "-o",
        str(final_message),
    ]
    if model:
        command.extend(["--model", model])
    command.append(PROMPT.read_text())
    return command


def parse_jsonl(raw: str) -> list[dict]:
    events: list[dict] = []
    for line_number, line in enumerate(raw.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"invalid JSONL on line {line_number}: {exc}") from exc
        require(isinstance(event, dict), f"JSONL line {line_number} is not an object")
        events.append(event)
    return events


def path_contains(path: Path, marker: str) -> bool:
    return path.exists() and marker in path.read_text()


def collect_checks(repo: Path, final_message: Path, events: list[dict], returncode: int, parse_error: str | None) -> dict[str, bool]:
    event_types = {event.get("type") for event in events}
    log = repo / "logs" / "eval-smoke-run.md"
    return {
        "codex_returncode_zero": returncode == 0,
        "jsonl_parseable": parse_error is None,
        "thread_started": "thread.started" in event_types,
        "turn_completed": "turn.completed" in event_types,
        "no_turn_failed": "turn.failed" not in event_types,
        "no_error_event": "error" not in event_types,
        "status_marker": path_contains(repo / "state" / "status.md", STATUS_MARKER),
        "smoke_log_created": log.exists(),
        "smoke_log_marker": path_contains(log, LOG_MARKER),
        "final_message_written": final_message.exists(),
        "final_message_marker": path_contains(final_message, FINAL_MARKER),
    }


def usage_from_events(events: list[dict]) -> dict | None:
    for event in reversed(events):
        if event.get("type") == "turn.completed" and isinstance(event.get("usage"), dict):
            return event["usage"]
    return None


def write_summary(path: Path, summary: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")


def require_checks(checks: dict[str, bool]) -> None:
    failed = [name for name, passed in checks.items() if not passed]
    require(not failed, "failed checks: " + ", ".join(failed))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="validate setup and print the command shape without running Codex")
    parser.add_argument("--keep", action="store_true", help="keep the temporary eval repo after running")
    parser.add_argument("--timeout", type=int, default=600, help="seconds to allow the nested Codex run")
    parser.add_argument("--model", default=os.environ.get("CODEX_EVAL_MODEL"), help="optional model override")
    parser.add_argument(
        "--summary-output",
        default=str(DEFAULT_SUMMARY),
        help="path to write a JSON summary artifact; use 'none' to disable",
    )
    args = parser.parse_args()

    require(PROMPT.exists(), f"missing prompt: {PROMPT}")
    require(shutil.which("codex") is not None, "codex CLI not found on PATH")
    require((ROOT / ".agents" / "skills" / "long-codex-cycle" / "SKILL.md").exists(), "long-codex-cycle skill missing")

    if args.dry_run:
        command = build_command(Path("$TMP_REPO"), Path("$TMP_FINAL_MESSAGE"), args.model)
        print("dry run ok")
        print("command:")
        print(" ".join(command[:-1] + ["<prompt>"]))
        print(f"summary-output: {args.summary_output}")
        print("validates: thread.started, turn.completed, status marker, log marker, final marker")
        return 0

    temp_dir = Path(tempfile.mkdtemp(prefix="long-codex-eval-"))
    repo = temp_dir / "repo"
    final_message = temp_dir / "final-message.txt"
    summary_output = None if args.summary_output == "none" else Path(args.summary_output)
    started = time.monotonic()
    try:
        copy_repo(repo)
        init_temp_git(repo)
        command = build_command(repo, final_message, args.model)
        result = run(command, cwd=repo, timeout=args.timeout)
        duration = time.monotonic() - started
        events: list[dict] = []
        parse_error = None
        try:
            events = parse_jsonl(result.stdout)
        except RuntimeError as exc:
            parse_error = str(exc)
        checks = collect_checks(repo, final_message, events, result.returncode, parse_error)
        event_counts = dict(sorted(Counter(str(event.get("type")) for event in events).items()))
        summary = {
            "checks": checks,
            "duration_seconds": round(duration, 3),
            "event_counts": event_counts,
            "event_total": len(events),
            "model": args.model,
            "parse_error": parse_error,
            "passed": all(checks.values()),
            "prompt_path": str(PROMPT.relative_to(ROOT)),
            "returncode": result.returncode,
            "stderr_tail": "" if result.returncode == 0 else result.stderr[-2000:],
            "summary_version": 1,
            "timeout_seconds": args.timeout,
            "usage": usage_from_events(events),
        }
        if summary_output is not None:
            write_summary(summary_output, summary)
        require(result.returncode == 0, f"codex exec failed with {result.returncode}:\n{result.stderr}")
        if parse_error is not None:
            raise RuntimeError(parse_error)
        require_checks(checks)
        print("long-codex-cycle smoke eval passed")
        if summary_output is not None:
            print(f"summary written: {summary_output}")
        return 0
    finally:
        if args.keep:
            print(f"kept temp repo: {repo}", file=sys.stderr)
        else:
            shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"eval failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
