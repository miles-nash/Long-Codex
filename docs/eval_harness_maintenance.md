# Eval Harness Maintenance

Date: 2026-05-10

## Question

Should the three nested Codex eval scripts be refactored into a shared helper now?

## Evidence

- `scripts/eval_long_codex_cycle.py`: 225 lines.
- `scripts/eval_dead_end_avoidance.py`: 254 lines.
- `scripts/eval_queue_exhaustion.py`: 300 lines.
- Shared plumbing appears in all three scripts: subprocess wrapper, repo copy, temporary git init, `codex exec --json` command construction, JSONL parsing, marker checks, usage extraction, summary writing, and check failure reporting.
- Behavior-specific code is still meaningful in each script: prompt constants, trap setup, safe/forbidden log names, expected markers, and summary-specific checks.

## Candidate Scores

- Record the decision and defer extraction: score 8. Low risk, preserves a clear handoff, and avoids changing three passing evals just after adding the third.
- Extract `scripts/codex_eval_utils.py` now: score 6. Would reduce duplication, but it would touch all eval scripts and require heavier reruns to gain confidence.
- Ignore the duplication: score 3. The duplication is real enough that future sessions need an explicit rule.

## Decision

Do not refactor the eval harness in this run.

Keep the current duplication until one of these triggers occurs:

- a fourth nested Codex eval is added
- a shared behavior changes, such as `codex exec` flags, JSONL parsing, summary schema, temp repo setup, or session permission handling
- one eval bug must be fixed in two or more scripts

When a trigger occurs, extract only the boring shared mechanics into `scripts/codex_eval_utils.py`. Keep behavior-specific trap setup and check dictionaries local to each eval script.

## Proposed Helper Boundary

A future helper should own:

- `run`
- `require`
- `copy_repo`
- `init_temp_git`
- `build_codex_exec_command`
- `parse_jsonl`
- `path_contains`
- `usage_from_events`
- `write_summary`
- `require_checks`

Each eval script should keep:

- prompt path and marker constants
- trap or temp-state injection
- behavior-specific `collect_checks`
- summary-specific extra fields
- dry-run validation text

## Next Use

Use this note before adding another eval or changing shared eval runtime behavior. If none of the triggers has occurred, leave the scripts duplicated and spend the cycle on a higher-value system behavior.
