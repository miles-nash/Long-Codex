# Run Log: Source-Ledger Freshness

Date: 2026-05-10
Time: 02:10 America/Denver
Automation: `long-codex-hourly-continuation`

## Mode

`eval`

## Candidate Actions Considered

- Add source-ledger freshness check: score 9. Top queue item, directly closes an active follow-up, cheap to verify, and prevents future stale evidence.
- Review cadence again: score 5. Still important, but the previous cadence review was one heartbeat ago and no watchpoint triggered.
- Add useful-hour behavior eval: score 4. Still premature because deterministic ledger checks are cheaper and enough for the current failure mode.

Chosen action: make source-ledger freshness part of the repo check.

## What Changed

- Updated `scripts/check_long_codex_repo.sh` so every research note must carry a `Date: YYYY-MM-DD` line.
- Updated `scripts/check_long_codex_repo.sh` so `docs/source_ledger.md` must have `Last updated: YYYY-MM-DD` and cannot be older than the latest dated `docs/research/*.md` note.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
./scripts/check_long_codex_repo.sh
python3 scripts/check_useful_hour_scores.py
```

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Review `docs/cadence_review.md` after one more heartbeat run unless a cadence watchpoint triggers first.
