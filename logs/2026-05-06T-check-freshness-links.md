# Run Log: Freshness And Source Checks

Date: 2026-05-06
Trigger: manual continuation after Miles said "keep working"

## Mode

`eval`

## Candidate Actions Considered

- Improve `scripts/check_long_codex_repo.sh`: highest priority, high risk-reduction, low ambiguity.
- Extend the nested Codex eval with JSON summary output: valuable, but next after the repo check can validate current state more strictly.
- Add a stale-open-loop list: useful structure, but less urgent than executable checks.

Chosen action: improve the repo check.

## What Changed

- Added date freshness validation: `state/status.md` and `state/next_actions.md` must not be older than the most recently modified run log.
- Added research-note validation: every `docs/research/*.md` file must include `## Sources` and at least one URL.
- Added source-ledger validation: every ledger row must include a source URL, local evidence path references, and existing local evidence paths.
- Kept existing structural and eval-harness syntax checks.

## Verification

```sh
./scripts/check_long_codex_repo.sh
```

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Extend `scripts/eval_long_codex_cycle.py` to emit a small JSON summary artifact with duration, event counts, and pass/fail checks.
