# Open Loops

Last updated: 2026-05-10

## Purpose

Separate active blockers, active follow-ups, parked ideas, and retired ideas so future sessions do not confuse "not now" with "blocked" or "never again."

## Active Blockers

- None currently. The repo check passes, the eval summaries are passing, and the heartbeat is paused because no ready scheduled work exists.

## Active Follow-Ups

| Item | Why It Matters | Evidence | Next Action |
| --- | --- | --- | --- |
| Heartbeat restart gate | The heartbeat is paused because repeated no-trigger wakes would create churn; restarting should require a concrete experiment ladder or direct user request. | `docs/cadence_review.md`, `logs/2026-05-10T1525Z-daily-cadence-slowdown.md`, `/Users/milesnash/.codex/automations/long-codex-hourly-continuation/automation.toml` | Restart only when a bounded next experiment benefits from scheduled continuation. |

## Parked Ideas

- Global user skill: wait until the repo-scoped skill proves stable across more cycles.
- Shared eval harness module: wait until a third eval creates real duplication.
- Expanded useful-hour scorecard: keep the current scorecard until runs reveal missing dimensions.
- Eval summary usage policy revisit: the current decision is to keep compact `usage` fields; reopen only if summaries become noisy or expensive.
- Useful-hour behavior eval: wait until the score ledger shape is checked or manual scoring proves insufficient.
- Useful-hour score ledger check exceptions: revisit only if a real blocked run scores below 7 and needs explicit syntax.
- Weekly synthesis automation: wait until logs become repetitive or hard to scan.
- Parallel subagent cycles: wait until a cycle has genuinely independent branches and can use artifact handoffs.
- Subagent handoff drift check: add only if the operating loop and repo skill diverge later.
- Source-ledger row coverage: add only if date freshness is not enough to catch material research notes missing from the ledger.
- Eval harness refactor: extract `scripts/codex_eval_utils.py` only if a fourth eval is added, shared runtime behavior changes, or one bug must be fixed in multiple eval scripts.

## Retired Ideas

- Bigger heartbeat prompt as the default solution: retired for now because source ledgers, checks, and skills carry state more cleanly.
- Filename sort for latest log: retired because modification time is the repo rule.
- Summary-only memory: retired because source-backed claims should point to durable local evidence.
- Duplicate automation for faster cadence: retired because updating the existing heartbeat preserves continuity.
- Eval summary usage decision: resolved in `docs/eval_summary_policy.md`.
- Post-open-loop heartbeat trend synthesis: resolved in `docs/heartbeat_synthesis.md`; keep the heartbeat as-is and defer weekly synthesis automation.
- Useful-hour score ledger consistency: resolved in `scripts/check_useful_hour_scores.py`.
- Faster-cadence review: resolved in `docs/cadence_review.md`; keep 30-minute heartbeat active while watchpoints stay clear.
- Current-practices harvest: resolved in `docs/research/2026-05-08-agent-artifact-handoffs.md` and `docs/source_ledger.md`.
- Subagent artifact handoff rule: resolved in `docs/operating_loop.md` and `.agents/skills/long-codex-cycle/SKILL.md`.
- Post-review cadence check: resolved in `docs/cadence_review.md`; keep 30-minute heartbeat active while watchpoints stay clear.
- Source-ledger freshness: resolved in `scripts/check_long_codex_repo.sh`; source ledger date must now be at least as new as the latest dated research note.
- Next-experiment synthesis: resolved in `docs/next_experiment_ladder.md`; a queue-exhaustion behavior eval is the next concrete frontier.
- Queue-exhaustion behavior eval: resolved in `scripts/eval_queue_exhaustion.py`, `evals/queue_exhaustion_prompt.md`, and `evals/last_queue_exhaustion_summary.json`.
- Cadence review after queue-exhaustion eval: resolved in `docs/cadence_review.md`; active heartbeat returned to hourly at `FREQ=HOURLY;INTERVAL=1`.
- Eval harness maintenance assessment: resolved in `docs/eval_harness_maintenance.md`; duplication is acceptable until a concrete helper trigger occurs.
- No-ready-work branch observation: resolved in `logs/2026-05-10T1425Z-no-ready-work-observation.md`; the first live hourly run followed the branch cleanly.
- Repeated no-ready-work watch: resolved in `docs/cadence_review.md`; active heartbeat slowed to daily at `FREQ=DAILY;INTERVAL=1`.
- Daily no-ready-work watch: resolved in `docs/cadence_review.md`; heartbeat paused at `status = "PAUSED"` after another no-trigger wake.
