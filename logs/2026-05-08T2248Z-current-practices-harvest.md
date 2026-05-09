# Run Log: Current Practices Harvest

Date: 2026-05-08
Time: 15:48 America/Los_Angeles
Automation: `long-codex-hourly-continuation`

## Mode

`harvest`

## Candidate Actions Considered

- Harvest one current source-backed practice: score 9. Top queue item, current-source sensitive, and directly improves the source ledger.
- Add a subagent rule immediately without new source work: score 5. Useful, but less grounded before the harvest.
- Add a useful-hour behavior eval: score 4. Still premature while current-practices memory has an open gap.

Chosen action: harvest Anthropic's artifact-handoff practice for subagent work.

## What Changed

- Added `docs/research/2026-05-08-agent-artifact-handoffs.md`.
- Updated `docs/source_ledger.md` with a new Anthropic source row.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Source

- Anthropic, How we built our multi-agent research system: https://www.anthropic.com/engineering/built-multi-agent-research-system

## Verification

```sh
./scripts/check_long_codex_repo.sh
```

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Add a short subagent artifact-handoff rule to `docs/operating_loop.md` and `.agents/skills/long-codex-cycle/SKILL.md`.
