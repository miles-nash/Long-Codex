# Open Loops

Last updated: 2026-05-08

## Purpose

Separate active blockers, active follow-ups, parked ideas, and retired ideas so future sessions do not confuse "not now" with "blocked" or "never again."

## Active Blockers

- None currently. The repo check passes, the eval summaries are passing, and the active heartbeat automation is still useful.

## Active Follow-Ups

| Item | Why It Matters | Evidence | Next Action |
| --- | --- | --- | --- |
| Useful-hour score ledger consistency | The score ledger now steers automation decisions, but its rubric shape is not checked. | `docs/useful_hour_scorecard.md`, `state/useful_hour_scores.md` | Add a lightweight check before adding a model-graded useful-hour eval. |
| Faster-cadence review | The cadence is temporarily faster after Miles said to work more than hourly for now. | `docs/heartbeat_synthesis.md`, `state/useful_hour_scores.md`, `logs/2026-05-08T0715Z-open-loops.md`, `logs/2026-05-08T0749Z-eval-summary-policy.md`, `logs/2026-05-08T0827Z-heartbeat-trend-synthesis.md` | After two more heartbeat runs, decide whether to keep 30-minute-ish cadence or return to hourly. |

## Parked Ideas

- Weekly synthesis automation: wait until hourly or half-hourly logs begin repeating or growing too long.
- Global user skill: wait until the repo-scoped skill proves stable across more cycles.
- Shared eval harness module: wait until a third eval creates real duplication.
- Expanded useful-hour scorecard: keep the current scorecard until runs reveal missing dimensions.
- Eval summary usage policy revisit: the current decision is to keep compact `usage` fields; reopen only if summaries become noisy or expensive.
- Useful-hour behavior eval: wait until the score ledger shape is checked or manual scoring proves insufficient.

## Retired Ideas

- Bigger heartbeat prompt as the default solution: retired for now because source ledgers, checks, and skills carry state more cleanly.
- Filename sort for latest log: retired because modification time is the repo rule.
- Summary-only memory: retired because source-backed claims should point to durable local evidence.
- Duplicate automation for faster cadence: retired because updating the existing heartbeat preserves continuity.
- Eval summary usage decision: resolved in `docs/eval_summary_policy.md`.
- Post-open-loop heartbeat trend synthesis: resolved in `docs/heartbeat_synthesis.md`; keep the heartbeat as-is and defer weekly synthesis automation.
