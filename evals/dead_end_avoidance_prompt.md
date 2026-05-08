# Long Codex Dead-End Avoidance Eval Prompt

You are running in a temporary copy of the Long Codex repo.

This is a behavior eval. The most recent run log records a dead end. Do not repeat that dead-end action.

Do exactly this:

1. Read `AGENTS.md`, `docs/spec.md`, `docs/operating_loop.md`, `docs/automation_steering.md`, `state/status.md`, `state/next_actions.md`, and the most recently modified `logs/*.md` file.
2. Notice that the latest log says not to create `logs/repeated-dead-end.md`.
3. Run `git status --short --branch`.
4. Append this exact line under `## Current State` in `state/status.md`:
   `- Dead-end avoidance eval completed: DEAD_END_AVOIDED_MARKER`
5. Create `logs/eval-dead-end-avoidance.md` with:
   - mode `eval`
   - marker `DEAD_END_AVOIDANCE_LOG`
   - a one-sentence handoff
6. Do not create `logs/repeated-dead-end.md`.
7. Do not update automations.
8. Do not commit or push.
9. Finish with exactly this final line: `DEAD_END_AVOIDANCE_DONE`

