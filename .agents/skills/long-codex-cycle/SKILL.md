---
name: long-codex-cycle
description: Run a bounded long-horizon Codex persistence cycle in this repo; use for hourly heartbeat continuations, durable state updates, automation refinement, and agent memory/eval improvements.
---

# Long Codex Cycle

Use this skill when continuing the Long Codex persistence project.

## Orient

Read these files first:

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

## Choose One Cycle

Pick exactly one:

- `research`: source-backed investigation and distillation.
- `harvest`: source-backed investigation and distillation.
- `structure`: improve docs, state, handoff, or plan.
- `skill`: improve this skill.
- `automation`: improve heartbeat prompt, cadence, or safety.
- `eval`: add or run a verification check.
- `synthesis`: compress logs and decisions into reusable principles.
- `publish`: commit and push a coherent verified update.

Choose the smallest cycle that creates durable learning.

## Execute

During the cycle:

- Keep the artifact narrow.
- Use official OpenAI docs for OpenAI/Codex facts.
- Use current web research for time-sensitive claims.
- Prefer files over chat memory.
- Record failed ideas if they prevent future waste.

## Finish

Before ending:

1. Run `./scripts/check_long_codex_repo.sh`.
2. Update `state/status.md`.
3. Update `state/next_actions.md`.
4. Add or update a run log under `logs/`.
5. Report changed files, verification result, blocker if any, and next smallest useful step.

## Quality Bar

A passable cycle leaves one durable artifact, one verification result, and one clear handoff.
