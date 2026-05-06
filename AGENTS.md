# Long Codex Instructions

You are building a durable operating system for longer, higher-value Codex sessions.

Before meaningful work in this repo, read:

- `docs/spec.md`
- `docs/operating_loop.md`
- `state/status.md`
- `state/next_actions.md`
- the latest file in `logs/`

When the task involves OpenAI, Codex, ChatGPT Apps, or the OpenAI API, use the OpenAI developer documentation MCP server if it is available; otherwise use official OpenAI docs first.

## Working Loop

Use the loop in `docs/operating_loop.md`:

1. Orient from durable state.
2. Choose one bounded cycle.
3. Research or implement.
4. Verify with a concrete check.
5. Update state, next actions, and a run log.
6. Leave a handoff that lets the next session resume in under five minutes.

## Boundaries

- Prefer repo-scoped durable files over relying on chat memory.
- Keep changes reviewable and focused.
- Do not delete or rewrite user work unless explicitly asked.
- Avoid expanding scope without recording the decision and reason.
- If blocked, leave a precise blocker, the evidence, and the next cheapest test.

## Definition Of Useful Progress

A run was useful if it left at least one of:

- a distilled insight with sources
- an improved instruction, skill, or automation prompt
- a validation script or eval
- an implemented repo/system change
- a clearer next-action queue
- a falsified idea that prevents future waste
