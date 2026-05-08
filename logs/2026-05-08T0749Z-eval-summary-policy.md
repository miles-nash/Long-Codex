# Run Log: Eval Summary Policy

Date: 2026-05-08
Time: 00:49 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`synthesis`

## Candidate Actions Considered

- Update heartbeat trend synthesis: score 5. Valuable, but still one run early because the queue asks for two more heartbeat runs after the open-loop artifact.
- Add a weekly synthesis automation: score 3. Premature until logs repeat or grow too long.
- Decide eval summary usage fields: score 8. Ready now because two eval summaries already include `usage`, and the scorecard names token efficiency as a future quality dimension.

Chosen action: document the eval summary policy and resolve the usage-token open loop.

## What Changed

- Added `docs/eval_summary_policy.md`.
- Updated `scripts/check_long_codex_repo.sh` to require the policy and validate the key `usage` and `summary_version` guidance.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
./scripts/check_long_codex_repo.sh
```

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

After one more heartbeat run, update `docs/heartbeat_synthesis.md` with trend notes and reconcile it with `state/open_loops.md`.
