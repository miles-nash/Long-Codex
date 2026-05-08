#!/usr/bin/env python3
"""Validate the useful-hour score ledger has consistent rubric entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "state" / "useful_hour_scores.md"
REQUIRED_RUBRIC = ["Artifact", "Verification", "Learning", "Steering", "Handoff", "Restraint"]


def section_blocks(text: str) -> list[tuple[str, list[str]]]:
    blocks: list[tuple[str, list[str]]] = []
    current_title: str | None = None
    current_lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            if current_title is not None:
                blocks.append((current_title, current_lines))
            current_title = line[3:].strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)
    if current_title is not None:
        blocks.append((current_title, current_lines))
    return blocks


def line_matching(lines: list[str], pattern: str) -> str | None:
    regex = re.compile(pattern)
    for line in lines:
        if regex.match(line):
            return line
    return None


def validate_section(title: str, lines: list[str]) -> list[str]:
    errors: list[str] = []
    text = "\n".join(lines)

    if line_matching(lines, r"^Automation:\s+.+$") is None:
        errors.append(f"{title}: missing Automation line")
    if line_matching(lines, r"^Mode chosen:\s+`[^`]+`\s*$") is None:
        errors.append(f"{title}: missing Mode chosen line")

    score_line = line_matching(lines, r"^Score:\s+\d+/12\s*$")
    if score_line is None:
        errors.append(f"{title}: missing Score line")
        declared_score = None
    else:
        declared_score = int(re.search(r"\d+", score_line).group(0))
        if not 0 <= declared_score <= 12:
            errors.append(f"{title}: score {declared_score} is outside 0-12")
        if declared_score < 7 and "blocked" not in text.lower():
            errors.append(f"{title}: score below 7 without a blocker note")

    rubric_scores: dict[str, int] = {}
    rubric_pattern = re.compile(r"^-\s+([A-Za-z-]+):\s+([0-2])\s+-\s+.+$")
    for line in lines:
        match = rubric_pattern.match(line)
        if match:
            name = match.group(1)
            if name in rubric_scores:
                errors.append(f"{title}: duplicate rubric item {name}")
            rubric_scores[name] = int(match.group(2))

    for rubric in REQUIRED_RUBRIC:
        if rubric not in rubric_scores:
            errors.append(f"{title}: missing rubric item {rubric}")

    unexpected = sorted(set(rubric_scores) - set(REQUIRED_RUBRIC))
    for name in unexpected:
        errors.append(f"{title}: unexpected rubric item {name}")

    if declared_score is not None and set(rubric_scores) == set(REQUIRED_RUBRIC):
        computed = sum(rubric_scores.values())
        if computed != declared_score:
            errors.append(f"{title}: score {declared_score} does not match rubric sum {computed}")

    if line_matching(lines, r"^Result:\s+.+$") is None:
        errors.append(f"{title}: missing Result line")

    return errors


def main() -> int:
    if not LEDGER.exists():
        print(f"missing ledger: {LEDGER}", file=sys.stderr)
        return 1

    blocks = section_blocks(LEDGER.read_text())
    if not blocks:
        print("useful-hour ledger has no scored sections", file=sys.stderr)
        return 1

    errors: list[str] = []
    for title, lines in blocks:
        errors.extend(validate_section(title, lines))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"useful-hour score ledger ok ({len(blocks)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
