# Next Experiment Ladder

Date: 2026-05-10

## Question

What is the next concrete experiment that justifies keeping the faster heartbeat cadence?

## Evidence

- `docs/cadence_review.md` says the 30-minute heartbeat remains useful only while it finds distinct, bounded work.
- `logs/2026-05-10T0810Z-source-ledger-freshness.md` closed the latest ready eval guardrail with a 12/12 score.
- `logs/2026-05-10T0840Z-cadence-watchpoint-review.md` kept the faster cadence only because this synthesis run could name a concrete next frontier.
- `state/useful_hour_scores.md` shows recent heartbeat runs are consistently 12/12, but those are rubric judgments rather than behavior tests.
- `scripts/eval_dead_end_avoidance.py` proves the repo can run a nested behavior eval that plants a trap and verifies the agent avoids it.

## Synthesis

The system no longer needs another broad planning pass. Its current weakness is anti-busywork judgment: when the queue becomes conditional-heavy, will a future heartbeat slow down or will it manufacture a low-value artifact to preserve momentum?

That is the right next frontier because it tests the key promise of longer Codex sessions: not just persistence, but useful persistence.

## Ladder

| Rung | Experiment | Why This Comes Next | Done When |
| --- | --- | --- | --- |
| 1 | Add a queue-exhaustion behavior eval. | The live queue is becoming conditional-heavy, and the cadence policy says to slow down if no active bounded follow-up exists. | A nested eval seeds a temporary repo with no ready follow-up and verifies the agent records a cadence rollback or no-work recommendation instead of inventing busywork. |
| 2 | Review cadence using the eval result. | If the eval fails, the 30-minute heartbeat is likely too eager; if it passes, the faster cadence has a stronger safety case. | `docs/cadence_review.md` either returns the heartbeat to hourly or records why the 30-minute schedule remains justified. |
| 3 | Refactor the eval harness only if the third eval creates painful duplication. | A third nested eval may expose shared setup code worth extracting, but abstraction before the third eval would be premature. | The eval scripts either stay deliberately duplicated or share a small helper with no behavior change. |
| 4 | Exercise subagent handoffs in a real independent-branch cycle. | Subagent rules are encoded but untested; this should wait until cadence safety is better measured. | One run uses independent subagents and links returned artifact paths from a parent log or ledger. |

## Decision

A concrete high-value next step exists, so do not return the heartbeat to hourly yet.

Keep the next run bounded to Rung 1: add the queue-exhaustion behavior eval. If that eval cannot be completed cleanly in one run, record the blocker and then review whether the heartbeat should return to hourly.

## Progress

- 2026-05-10: Rung 1 completed in `scripts/eval_queue_exhaustion.py`, `evals/queue_exhaustion_prompt.md`, and `evals/last_queue_exhaustion_summary.json`. The eval passed after the nested Codex run was rerun with narrow elevated permission for Codex session-file access.

Next: perform Rung 2 by reviewing `docs/cadence_review.md` with the passing eval result.
