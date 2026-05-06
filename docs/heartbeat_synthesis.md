# Heartbeat Synthesis

Last updated: 2026-05-06

## Question

After two observed heartbeat runs, is `long-codex-hourly-continuation` steering useful work, or does the prompt need tightening?

## Evidence

- First observed heartbeat: `logs/2026-05-06T0710Z-heartbeat-eval.md`, scored 11/12 in `state/useful_hour_scores.md`.
- Second observed heartbeat: `logs/2026-05-06T0813Z-codex-exec-eval.md`, scored 12/12 in `state/useful_hour_scores.md`.
- Current steering policy: `docs/automation_steering.md`.
- Current canonical prompt: `docs/automation_prompt.md`.

## Findings

1. The heartbeat is resuming correctly from durable state.

Both runs read the repo state, selected a narrow cycle, produced a durable artifact, verified it, updated state, and pushed coherent changes.

2. The scorecard is doing useful work.

The first run found a real orientation bug: "latest log" was ambiguous when resolved by filename sort. That bug was fixed across the prompt, skill, and operating docs.

3. The steering policy is controlling scope.

The second run did not wander into broad research. It chose the highest-priority eval task, ran the nested `codex exec --json` smoke test in a temporary copy, and left the next action smaller than it found it.

4. No immediate prompt tightening is needed.

The current prompt is explicit enough about read set, cycle choice, artifact, verification, scoring, and blockers. The next risk is not prompt vagueness. It is that future runs may over-index on eval work unless the queue keeps pulling them into structure and synthesis.

## Decision

Keep the active heartbeat automation as-is.

Do not update the prompt this cycle. The better next move is to improve durable memory structure, starting with a source ledger that maps claims to evidence and implications.

## Watchpoints

- If the next two runs choose `eval` again without a specific blocker, tighten the prompt to prefer non-repeated modes more strongly.
- If a run scores below 7, update the automation before doing new research.
- If run logs start getting long or repetitive, add a weekly synthesis automation rather than making the hourly prompt larger.
- If `scripts/eval_long_codex_cycle.py` becomes slow or flaky, add a JSON summary artifact so failures are easier to diagnose.
