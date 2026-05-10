# Cadence Review

Date: 2026-05-08

## Question

Should `long-codex-hourly-continuation` keep the temporary faster cadence or return to hourly?

## Evidence

- Live automation config: `/Users/milesnash/.codex/automations/long-codex-hourly-continuation/automation.toml`
- Current live schedule observed in config: `FREQ=MINUTELY;INTERVAL=30`
- Miles explicitly allowed working more than hourly for now.
- Faster-cadence run: `logs/2026-05-08T0715Z-open-loops.md`, score 12/12.
- Faster-cadence run: `logs/2026-05-08T0749Z-eval-summary-policy.md`, score 12/12.
- Faster-cadence run: `logs/2026-05-08T0827Z-heartbeat-trend-synthesis.md`, score 12/12.
- Faster-cadence run: `logs/2026-05-08T0912Z-score-ledger-check.md`, score 12/12.

## Candidate Scores

- Keep the 30-minute heartbeat active and add clearer watchpoints: score 9. High momentum, good evidence, low implementation risk, and aligned with Miles's instruction.
- Return to hourly now: score 5. Lower noise risk, but premature while runs are still useful and distinct.
- Add weekly synthesis automation now: score 3. Still premature because logs are compact and non-repetitive.

## Decision

Keep the active heartbeat automation unchanged at `FREQ=MINUTELY;INTERVAL=30`.

The faster cadence has not yet created repetitive churn. The better control is not a schedule rollback; it is watchpoints that force a cadence change when value drops.

## Watchpoints

Return to hourly or pause faster cadence if any of these happen:

- two consecutive heartbeat runs score below 10
- any heartbeat scores below 7 without a concrete external blocker
- two consecutive runs create repetitive logs without new artifacts
- the next-action queue has no active follow-up that can finish in one bounded run
- Miles asks to slow down

## Next Use

Use this review when deciding whether to update the automation schedule or add weekly synthesis.

## Follow-Up Review: 2026-05-10

### Evidence

- Live automation config still shows `FREQ=MINUTELY;INTERVAL=30`.
- Post-review run: `logs/2026-05-08T2248Z-current-practices-harvest.md`, score 12/12.
- Post-review run: `logs/2026-05-10T0638Z-subagent-handoff-rule.md`, score 12/12.
- The two post-review runs produced distinct artifacts: one current-practices harvest and one operating-rule update.
- No cadence watchpoint has triggered.

### Candidate Scores

- Keep the 30-minute heartbeat active: score 9. Evidence remains strong, and the faster cadence is still producing distinct useful artifacts.
- Return to hourly now: score 4. Would reduce activity, but there is no evidence of churn or low-value runs.
- Add weekly synthesis automation now: score 3. Still premature because the logs are compact and the queue remains readable.

### Decision

Keep the active heartbeat automation unchanged at `FREQ=MINUTELY;INTERVAL=30`.

Review cadence again if a watchpoint triggers or after two more heartbeat runs. The next non-cadence bottleneck is making sure source-ledger metadata stays fresh as new research notes land.

## Follow-Up Review: 2026-05-10 02:40 America/Denver

### Evidence

- Live automation config still shows `FREQ=MINUTELY;INTERVAL=30`.
- Post-follow-up run: `logs/2026-05-10T0810Z-source-ledger-freshness.md`, score 12/12.
- The latest run closed a real eval guardrail and did not create repetitive churn.
- The active queue is now becoming conditional-heavy; without a concrete next synthesis target, the "no active follow-up" watchpoint could trigger soon.

### Candidate Scores

- Keep the 30-minute heartbeat active and aim the next run at synthesis: score 8. Recent value is still high, but the queue needs a compact next-experiment ladder.
- Return to hourly now: score 6. Reasonable if the queue stays conditional-only, but premature while one synthesis pass can decide the next useful frontier.
- Add weekly synthesis automation now: score 3. Still too heavy; one manual synthesis cycle is the cheaper test.

### Decision

Keep the active heartbeat automation unchanged at `FREQ=MINUTELY;INTERVAL=30`.

The next run should perform one bounded synthesis over recent logs and decisions, then either name a concrete next experiment or recommend returning the heartbeat to hourly. If that synthesis cannot identify a high-value bounded step, the "no active follow-up" watchpoint should be treated as triggered.

## Follow-Up Review: 2026-05-10 05:14 America/Denver

### Evidence

- Live automation config was updated from `FREQ=MINUTELY;INTERVAL=30` to `FREQ=HOURLY;INTERVAL=1`.
- Queue-exhaustion eval passed in `evals/last_queue_exhaustion_summary.json`.
- The eval verified the no-ready-work branch: no busywork log, rollback recommendation present, and `turn.completed` without errors.
- Recent fast-cadence runs were useful, but the active queue is now mostly conditional maintenance rather than urgent high-learning work.

### Candidate Scores

- Return the heartbeat to hourly: score 9. The queue-exhaustion eval gives confidence that the system can recognize low-value continuation, and hourly cadence reduces churn now that the urgent experiment ladder is complete.
- Keep the 30-minute heartbeat active: score 6. The fast cadence has been productive, but no longer has a concrete high-value next rung that needs immediate pressure.
- Add weekly synthesis automation now: score 3. Still premature because logs are readable and hourly cadence reduces synthesis pressure.

### Decision

Return the active heartbeat automation to hourly at `FREQ=HOURLY;INTERVAL=1`.

This is not a rollback due to failure. It is the intended watchpoint behavior: fast cadence was useful while closing a concrete ladder of eval and cadence questions; hourly is now the better default until Miles asks for another burst or the queue names a new high-value experiment.

## Follow-Up Review: 2026-05-10 09:25 America/Denver

### Evidence

- Live automation config was updated from `FREQ=HOURLY;INTERVAL=1` to `FREQ=DAILY;INTERVAL=1`.
- First live no-ready-work branch succeeded in `logs/2026-05-10T1425Z-no-ready-work-observation.md`.
- This wake again found no concrete trigger: repo check passed, no new user direction arrived, no new experiment ladder exists, and the queue remains conditional.
- Repeating no-ready-work logs hourly would create the churn the queue-exhaustion eval was meant to prevent.

### Candidate Scores

- Slow the heartbeat to daily: score 9. Preserves continuity and gives the system a chance to notice new triggers without producing empty hourly churn.
- Pause the heartbeat: score 7. Also valid, but slightly too aggressive while the user still wants long-horizon persistence.
- Keep hourly and log another no-ready-work result: score 2. This would prove the branch twice but would add little new learning.

### Decision

Slow the active heartbeat automation to daily at `FREQ=DAILY;INTERVAL=1`.

Use daily as the quiet default. Return to hourly or faster only when Miles asks for another burst or `state/next_actions.md` names a concrete experiment ladder that benefits from tighter cadence.
