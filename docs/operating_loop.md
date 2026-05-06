# Operating Loop

Use this loop for every long-running Codex cycle in this repo.

## 1. Orient

Read the stable state in this order:

1. `docs/spec.md`
2. `state/status.md`
3. `state/next_actions.md`
4. most recently modified `logs/*.md` (`ls -t logs/*.md | head -1`)
5. relevant files under `docs/research/`

Then run:

```sh
git status --short --branch
./scripts/check_long_codex_repo.sh
```

## 2. Choose One Cycle

Pick exactly one cycle type:

- `research`: find and distill current practices or papers.
- `structure`: improve repo instructions, plans, logs, or state.
- `skill`: improve `.agents/skills/long-codex-cycle`.
- `automation`: improve the heartbeat prompt or cadence.
- `eval`: add or run checks that catch regressions.
- `synthesis`: compress accumulated work into clearer principles.

Choose by expected learning per minute, not by apparent impressiveness.

## 3. Work

Keep the cycle narrow. A good cycle has:

- one question
- one artifact
- one verification
- one handoff

Use web or official docs when the question is current, source-sensitive, or about OpenAI/Codex behavior.

## 4. Verify

Use the cheapest concrete check that fits the artifact:

- shell check for required files and links
- lint/build/test for code
- source links for research
- dry-run prompt review for automation
- JSON/schema/event checks for future `codex exec` evals

If verification fails, either fix it or record the failure with evidence.

## 5. Record

Update all three:

- `state/status.md`
- `state/next_actions.md`
- a new `logs/YYYY-MM-DD-*.md` or the current run log

State updates should answer:

- What changed?
- What evidence supports it?
- What is the next smallest useful step?
- What should the next session avoid repeating?

## 6. Stop Cleanly

Before ending a run:

- make sure no needed shell session is still running
- run `git status --short --branch`
- run `./scripts/check_long_codex_repo.sh`
- report changed files and verification result
