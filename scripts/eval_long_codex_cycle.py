#!/usr/bin/env python3
"""Smoke-test the Long Codex cycle with `codex exec --json`.

The eval runs in a temporary copy of the repo and verifies that a tiny
long-codex-cycle run updates durable state and leaves a log.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "evals" / "long_codex_cycle_smoke.md"
STATUS_MARKER = "EVAL_SMOKE_MARKER"
LOG_MARKER = "EVAL_SMOKE_LOG"
FINAL_MARKER = "EVAL_SMOKE_DONE"


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


def validate(repo: Path, final_message: Path, stdout: str) -> None:
    events = parse_jsonl(stdout)
    event_types = {event.get("type") for event in events}
    require("thread.started" in event_types, "missing thread.started event")
    require("turn.completed" in event_types, "missing turn.completed event")
    require("turn.failed" not in event_types, "turn.failed event emitted")
    require("error" not in event_types, "error event emitted")

    status = (repo / "state" / "status.md").read_text()
    require(STATUS_MARKER in status, "status.md missing smoke marker")

    log = repo / "logs" / "eval-smoke-run.md"
    require(log.exists(), "smoke log was not created")
    require(LOG_MARKER in log.read_text(), "smoke log missing marker")

    require(final_message.exists(), "final message file was not written")
    require(FINAL_MARKER in final_message.read_text(), "final message missing completion marker")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="validate setup and print the command shape without running Codex")
    parser.add_argument("--keep", action="store_true", help="keep the temporary eval repo after running")
    parser.add_argument("--timeout", type=int, default=600, help="seconds to allow the nested Codex run")
    parser.add_argument("--model", default=os.environ.get("CODEX_EVAL_MODEL"), help="optional model override")
    args = parser.parse_args()

    require(PROMPT.exists(), f"missing prompt: {PROMPT}")
    require(shutil.which("codex") is not None, "codex CLI not found on PATH")
    require((ROOT / ".agents" / "skills" / "long-codex-cycle" / "SKILL.md").exists(), "long-codex-cycle skill missing")

    if args.dry_run:
        command = build_command(Path("$TMP_REPO"), Path("$TMP_FINAL_MESSAGE"), args.model)
        print("dry run ok")
        print("command:")
        print(" ".join(command[:-1] + ["<prompt>"]))
        print("validates: thread.started, turn.completed, status marker, log marker, final marker")
        return 0

    temp_dir = Path(tempfile.mkdtemp(prefix="long-codex-eval-"))
    repo = temp_dir / "repo"
    final_message = temp_dir / "final-message.txt"
    try:
        copy_repo(repo)
        init_temp_git(repo)
        command = build_command(repo, final_message, args.model)
        result = run(command, cwd=repo, timeout=args.timeout)
        require(result.returncode == 0, f"codex exec failed with {result.returncode}:\n{result.stderr}")
        validate(repo, final_message, result.stdout)
        print("long-codex-cycle smoke eval passed")
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
