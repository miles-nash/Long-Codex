# Run Log: Subagent Handoff Rule

Date: 2026-05-10
Time: 00:38 America/Denver
Automation: `long-codex-hourly-continuation`

## Mode

`structure`

## Candidate Actions Considered

- Add subagent artifact-handoff rule to the operating loop and skill: score 9. Top queue item, high durability, low cost, and directly follows the harvested source.
- Review cadence watchpoints: score 4. No watchpoint has triggered; recent scores remain high.
- Add useful-hour behavior eval: score 4. Still premature while a source-backed rule is ready to encode.

Chosen action: encode the subagent artifact-handoff rule in the operating loop and repo skill.

## What Changed

- Updated `docs/operating_loop.md` with a `Subagent Handoffs` section.
- Updated `.agents/skills/long-codex-cycle/SKILL.md` with the same subagent handoff requirement.
- Updated `scripts/check_long_codex_repo.sh` to verify the rule remains present.
- Updated `state/status.md`, `state/next_actions.md`, `state/open_loops.md`, and `state/useful_hour_scores.md`.

## Verification

```sh
./scripts/check_long_codex_repo.sh
```

Result: passed.

## Useful-Hour Score

12/12. Details are in `state/useful_hour_scores.md`.

## Next

Review `docs/cadence_review.md` now that two post-review heartbeat runs exist.
