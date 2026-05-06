# Run Log: Eval Summary Artifact

Date: 2026-05-06
Time: 08:05 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`eval`

## Candidate Actions Considered

- Extend `scripts/eval_long_codex_cycle.py` with JSON summary output: top queue item, high observability value.
- Add a second dead-end-avoidance eval: valuable, but easier after eval summaries exist.
- Add a stale-open-loop list: useful structure, but less urgent than making eval results inspectable.

Chosen action: add summary output to the smoke eval.

## What Changed

- `scripts/eval_long_codex_cycle.py` now writes a JSON summary artifact.
- Added `evals/last_long_codex_cycle_smoke_summary.json` from a passing run.
- `scripts/check_long_codex_repo.sh` now validates that the summary exists, passed, has event counts, and has all checks passing.
- Updated `state/status.md`, `state/next_actions.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
./scripts/check_long_codex_repo.sh
python3 scripts/eval_long_codex_cycle.py --dry-run
python3 scripts/eval_long_codex_cycle.py --timeout 600
```

The first full eval attempt failed inside the workspace sandbox because nested Codex needed access to Codex session files. Re-running with the approved elevated command succeeded.

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Add a second eval that checks whether the cycle avoids repeating a dead end noted in a prior log.
