# Automation Steering Policy

The hourly heartbeat should act like a careful lab assistant, not a restless autocomplete.

## Default Read Set

Read these first:

1. `AGENTS.md`
2. `docs/spec.md`
3. `docs/operating_loop.md`
4. `docs/automation_steering.md`
5. `state/status.md`
6. `state/next_actions.md`
7. most recently modified `logs/*.md` (`ls -t logs/*.md | head -1`)

Then run:

```sh
git status --short --branch
./scripts/check_long_codex_repo.sh
```

## Cycle Modes

Choose exactly one:

- `harvest`: collect and distill source-backed evidence.
- `structure`: improve repo memory layout, instructions, or state.
- `eval`: add or run a check that catches drift or regression.
- `automation`: improve prompt, cadence, safety, or stop conditions.
- `synthesis`: compress logs and decisions into reusable principles.
- `publish`: commit/push coherent changes after verification.

Do not pick the same mode more than twice in a row unless `state/next_actions.md` explicitly says to.

## Scoring

Before acting, silently score the top 2-3 candidate actions:

```text
score = learning + future_unblock + risk_reduction + durability - ambiguity - cost
```

Prefer work that leaves a reusable artifact over work that merely consumes time.

## Steering Rules

- One run, one artifact, one verification, one handoff.
- Favor exact source paths over free-floating summaries.
- If an idea fails, log why so the next run does not retry blindly.
- If research is broad, end by narrowing the next action.
- If the repo state is stale, fix state before new research.
- If the automation itself wandered, improve the automation prompt before anything else.
- Ask Miles only for concrete blockers: credentials, spending, publishing, destructive changes, or a strategic choice that cannot be inferred.

## Report Shape

End with:

- mode chosen
- artifact changed
- verification result
- next smallest useful step
- any blocker
