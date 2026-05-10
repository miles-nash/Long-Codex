# Run Log: Hourly Cadence Return

Date: 2026-05-10
Time: 05:14 America/Denver
Automation: `long-codex-hourly-continuation`

## Mode

`automation`

## Candidate Actions Considered

- Return the heartbeat to hourly: score 9. The queue-exhaustion eval passed, the fast-cadence experiment ladder is complete, and the active queue is now maintenance-oriented.
- Keep the 30-minute heartbeat active: score 6. The faster cadence was productive, but it no longer has a concrete urgent experiment rung.
- Add weekly synthesis automation now: score 3. Still premature because logs are readable and hourly cadence lowers synthesis pressure.

Chosen action: update the live heartbeat back to hourly and record the cadence decision.

## What Changed

- Updated `long-codex-hourly-continuation` from `FREQ=MINUTELY;INTERVAL=30` to `FREQ=HOURLY;INTERVAL=1`.
- Updated `docs/cadence_review.md` with the post-queue-exhaustion cadence decision.
- Updated `scripts/check_long_codex_repo.sh` to require the active hourly cadence decision.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
sed -n '1,220p' /Users/milesnash/.codex/automations/long-codex-hourly-continuation/automation.toml
./scripts/check_long_codex_repo.sh
python3 scripts/check_useful_hour_scores.py
git diff --check
```

Result: passed. The live automation config shows `FREQ=HOURLY;INTERVAL=1`.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Do a bounded eval-harness maintenance assessment: compare the three nested Codex eval scripts and either extract a small shared helper or record why duplication is still acceptable.
