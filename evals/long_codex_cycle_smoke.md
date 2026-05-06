# Long Codex Cycle Smoke Eval Prompt

You are running in a temporary copy of the Long Codex repo.

Use the `$long-codex-cycle` method if it is available. This is a smoke eval, so keep the work tiny and local.

Do exactly this:

1. Read `AGENTS.md`, `docs/spec.md`, `docs/operating_loop.md`, `docs/automation_steering.md`, `state/status.md`, `state/next_actions.md`, and the most recently modified `logs/*.md` file.
2. Run `git status --short --branch`.
3. Append this exact line under `## Current State` in `state/status.md`:
   `- Eval harness smoke run completed: EVAL_SMOKE_MARKER`
4. Create `logs/eval-smoke-run.md` with:
   - mode `eval`
   - marker `EVAL_SMOKE_LOG`
   - a one-sentence handoff
5. Do not update automations.
6. Do not commit or push.
7. Finish with exactly this final line: `EVAL_SMOKE_DONE`

