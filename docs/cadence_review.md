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
