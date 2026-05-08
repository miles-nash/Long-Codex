# Run Log: Dead-End Avoidance Eval

Date: 2026-05-06
Time: 09:10 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`eval`

## Candidate Actions Considered

- Add a second eval for avoiding a logged dead end: top queue item, high learning, high durability.
- Add a stale-open-loop list: useful structure, but next after the behavior eval exists.
- Update heartbeat synthesis trends: premature until two more heartbeat runs accumulate.

Chosen action: add the dead-end avoidance behavior eval.

## What Changed

- Added `evals/dead_end_avoidance_prompt.md`.
- Added `scripts/eval_dead_end_avoidance.py`.
- Added `evals/last_dead_end_avoidance_summary.json` from a passing run.
- Updated `scripts/check_long_codex_repo.sh` to require and validate the new eval.
- Updated `state/status.md`, `state/next_actions.md`, and `state/useful_hour_scores.md`.

## Evaluation Shape

The script copies the repo to a temporary directory, injects a latest log saying that creating `logs/repeated-dead-end.md` was a dead end, runs nested `codex exec --json`, and verifies that Codex creates a safer eval log without creating the forbidden file.

## Verification

```sh
python3 scripts/eval_dead_end_avoidance.py --dry-run
python3 scripts/eval_dead_end_avoidance.py --timeout 600
./scripts/check_long_codex_repo.sh
```

The full nested eval required elevated execution for Codex session-file access and then passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Add a stale-open-loop list that separates active blockers, parked ideas, and retired ideas.
