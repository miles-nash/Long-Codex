# Open Loops

Last updated: 2026-05-08

## Purpose

Separate active blockers, active follow-ups, parked ideas, and retired ideas so future sessions do not confuse "not now" with "blocked" or "never again."

## Active Blockers

- None currently. The repo check passes, the eval summaries are passing, and the active heartbeat automation is still useful.

## Active Follow-Ups

| Item | Why It Matters | Evidence | Next Action |
| --- | --- | --- | --- |
| Heartbeat trend synthesis | The half-hour cadence needs trend evidence before adding a separate weekly synthesis automation. | `docs/heartbeat_synthesis.md`, `state/useful_hour_scores.md` | Update `docs/heartbeat_synthesis.md` after one more heartbeat run. |
| Useful-hour score measurement eval | The eval suite checks completion and dead-end avoidance, but it does not yet measure run quality against the scorecard. | `docs/useful_hour_scorecard.md`, `scripts/eval_long_codex_cycle.py`, `scripts/eval_dead_end_avoidance.py` | Add this only after trend synthesis or when a third eval is clearly warranted. |

## Parked Ideas

- Weekly synthesis automation: wait until hourly or half-hourly logs begin repeating or growing too long.
- Global user skill: wait until the repo-scoped skill proves stable across more cycles.
- Shared eval harness module: wait until a third eval creates real duplication.
- Expanded useful-hour scorecard: keep the current scorecard until runs reveal missing dimensions.
- Eval summary usage policy revisit: the current decision is to keep compact `usage` fields; reopen only if summaries become noisy or expensive.

## Retired Ideas

- Bigger heartbeat prompt as the default solution: retired for now because source ledgers, checks, and skills carry state more cleanly.
- Filename sort for latest log: retired because modification time is the repo rule.
- Summary-only memory: retired because source-backed claims should point to durable local evidence.
- Duplicate automation for faster cadence: retired because updating the existing heartbeat preserves continuity.
- Eval summary usage decision: resolved in `docs/eval_summary_policy.md`.
