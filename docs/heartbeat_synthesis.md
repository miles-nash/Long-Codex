# Heartbeat Synthesis

Last updated: 2026-05-08

## Question

Is `long-codex-hourly-continuation` still steering useful work after the faster cadence, or does the prompt/cadence need tightening?

## Evidence

### Initial Window

- First observed heartbeat: `logs/2026-05-06T0710Z-heartbeat-eval.md`, scored 11/12 in `state/useful_hour_scores.md`.
- Second observed heartbeat: `logs/2026-05-06T0813Z-codex-exec-eval.md`, scored 12/12 in `state/useful_hour_scores.md`.

### Faster-Cadence Window

- Open-loop structure run: `logs/2026-05-08T0715Z-open-loops.md`, scored 12/12 in `state/useful_hour_scores.md`.
- Eval-summary policy run: `logs/2026-05-08T0749Z-eval-summary-policy.md`, scored 12/12 in `state/useful_hour_scores.md`.
- Current steering policy: `docs/automation_steering.md`.
- Current canonical prompt: `docs/automation_prompt.md`.
- Current open-loop state: `state/open_loops.md`.

## Findings

1. The heartbeat is still resuming correctly from durable state.

Both initial runs and the faster-cadence runs read the repo state, selected narrow cycles, produced durable artifacts, verified work, updated state, and pushed coherent changes.

2. The scorecard is doing useful work.

The first run found a real orientation bug: "latest log" was ambiguous when resolved by filename sort. That bug was fixed across the prompt, skill, and operating docs.

3. The open-loop state improved steering.

After `state/open_loops.md` was added, the next run did not prematurely synthesize trends. It resolved a smaller ready ambiguity, `docs/eval_summary_policy.md`, and left the trend synthesis for the next heartbeat.

4. The faster cadence is not yet creating repetitive churn.

The 2026-05-08 runs produced distinct artifacts: one state structure and one policy synthesis. That is not enough evidence to justify a weekly synthesis automation, because the logs are still short and the queue is still steering.

5. No immediate prompt tightening is needed.

The current prompt is explicit enough about read set, cycle choice, artifact, verification, scoring, and blockers. The next risk is drift in the score ledger and open-loop queue, not prompt vagueness.

## Decision

Keep the active heartbeat automation as-is.

Do not add a weekly synthesis automation yet. Do not add a heavier useful-hour behavior eval yet. The better next move is a small consistency check for the useful-hour score ledger, because the score ledger is now part of steering and should not silently lose rubric detail.

## Watchpoints

- If the next two runs choose `eval` again without a specific blocker, tighten the prompt to prefer non-repeated modes more strongly.
- If a run scores below 7, update the automation before doing new research.
- If run logs start getting long or repetitive, add a weekly synthesis automation rather than making the hourly prompt larger.
- If `scripts/eval_long_codex_cycle.py` becomes slow or flaky, add a JSON summary artifact so failures are easier to diagnose.
- If `state/useful_hour_scores.md` grows without consistent rubric fields, add a ledger check before adding model-graded evaluation.
