# Current Practices Harvest: Agent Artifact Handoffs

Date: 2026-05-08

## Question

What current agent-system practice should Long Codex absorb now that the file-based loop is stable?

## Source-Backed Practice

Anthropic's 2025 writeup on its multi-agent research system describes a pattern where subagents can write persistent outputs to an external artifact system and return lightweight references to the lead agent.

The useful principle for Long Codex is simple: when work branches into subagents, the handoff should be an artifact path plus a short summary, not only a conversational recap. This reduces information loss, lowers token copying, and lets later sessions inspect the evidence directly.

## Implication For This Repo

- Keep the default single-agent heartbeat loop for narrow cycles.
- When a future cycle uses subagents, require each subagent to produce or identify a durable artifact path.
- The parent run should link those paths from the run log, `docs/source_ledger.md`, or `state/open_loops.md`.
- Do not add parallel agents just to look busy; reserve them for independent research/eval branches where separate context windows add value.

## Candidate Future Rule

If a run spawns subagents, each assigned subtask should name its ownership boundary and return:

- artifact path
- one-sentence finding
- verification performed or blocker

The parent session then decides whether the result belongs in a ledger, state file, or log.

## Sources

- Anthropic, How we built our multi-agent research system: https://www.anthropic.com/engineering/built-multi-agent-research-system
