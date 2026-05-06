# Deep Research: Agent Memory And Long-Run Steering

Date: 2026-05-06

## Thesis

Long-running Codex should not try to become one huge uninterrupted mind. It should become a disciplined sequence of bounded runs with durable memory, explicit steering, and lightweight evaluation.

The practical design target is:

- preserve exact evidence when it matters
- summarize only the parts that should guide future decisions
- organize state by use, not by chronology alone
- test whether memory improves the next action
- schedule reflection as work, not decoration

## What The Current Research Says

### 1. Memory Needs Layers

Multi-layer memory work decomposes long histories into working, episodic, and semantic layers, with retrieval gates to reduce drift and context growth. For Codex, that maps cleanly:

- working: `state/status.md`, `state/next_actions.md`, latest log
- episodic: `logs/*.md`, run transcripts, evidence ledgers
- semantic: `docs/research/*.md`, `docs/operating_loop.md`, decisions and principles

The important move is not "store everything." It is "store at the right level and retrieve only what the next subgoal needs."

### 2. Indexes Beat Summaries Alone

Memex(RL) argues that running summaries are lossy because they compress or discard past evidence. Its alternative is a compact working context with stable indices pointing to full-fidelity interactions. The Codex-friendly version is simple:

- keep concise status and research synthesis in the prompt path
- keep source URLs, logs, and exact command outputs discoverable by path
- when a future run needs detail, dereference the path instead of trusting a memory blur

This repo should therefore prefer "claim + evidence path" over "claim floating in a summary."

### 3. Structure Is Itself A Capability

StructMemEval distinguishes factual recall from the ability to organize memory into useful structures such as ledgers, trees, and to-do lists. That matters here because a pile of markdown logs will eventually become its own confusion.

The repo should grow explicit structures:

- decision log
- experiment ledger
- source ledger
- useful-hour scorecard
- stale-open-loop list

### 4. Memory Has To Affect Action

MemoryArena is especially relevant: it tests multi-session tasks where agents acquire memory through action and must use that memory to solve later subtasks. This is the right evaluation target for Long Codex.

Do not ask "can the agent recall what happened?" Ask:

- Did the next run avoid repeating dead work?
- Did it pick a better next action because of prior logs?
- Did it cite the evidence it used?
- Did it retire stale assumptions?

### 5. Agent Memory Evals Are Fragile

Recent surveys warn that agentic memory benchmarks can saturate, rely on shaky judge metrics, vary by backbone model, and hide latency/throughput costs. Translation for this repo:

- start with deterministic checks
- use small behavior evals before model-graded rubrics
- record token/time cost when possible
- evaluate the memory system in the actual workflow, not only on trivia recall

## Codex-Specific Lessons

OpenAI Codex best practices now describe the exact ladder this repo is building:

1. task context
2. durable guidance in `AGENTS.md`
3. configuration
4. MCP for changing outside context
5. skills for repeated workflows
6. automations for stable recurring work

OpenAI's automation docs say thread automations are right when continuity matters, but the prompt must say what to do on each wake, how to decide whether to report, and when to stop or ask for input.

OpenAI's reasoning guide says `high` is a good fit for long-horizon research and agentic tasks, while `xhigh` should be reserved for very long rollouts when evals justify the cost. So the default hourly continuation should prefer `high`; reserve `xhigh` for explicit deep research or hard architectural synthesis.

## Steering Policy For Future Runs

Each hourly run should choose one mode:

- `harvest`: gather and distill new evidence
- `structure`: improve memory organization
- `eval`: test whether the loop works
- `automation`: improve the scheduler/prompt
- `synthesis`: compress lessons into principles
- `publish`: commit/push a coherent update

Score candidate actions with:

```text
value = learning + future_unblock + risk_reduction + durability - ambiguity - cost
```

Then pick the highest-scoring action that can finish in one run.

## Anti-Patterns

- Re-reading every source every hour.
- Adding more memory stores before testing the current one.
- Treating "more detailed prompt" as a substitute for better state files.
- Summarizing away source paths.
- Creating automations that do not know when to stop.
- Letting a run end without updating `state/next_actions.md`.

## Sources

- OpenAI Codex best practices: https://developers.openai.com/codex/learn/best-practices
- OpenAI Codex thread automations: https://developers.openai.com/codex/app/automations#thread-automations
- OpenAI reasoning effort guide: https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort
- Multi-Layered Memory Architectures for LLM Agents: https://arxiv.org/abs/2603.29194
- Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory: https://arxiv.org/abs/2603.04257
- Evaluating Memory Structure in LLM Agents: https://arxiv.org/abs/2602.11243
- MemoryArena: https://digitaleconomy.stanford.edu/publication/memoryarena-benchmarking-agent-memory-in-interdependent-multi-session-agentic-tasks/
- Anatomy of Agentic Memory: https://arxiv.org/abs/2602.19320
- Memory for Autonomous LLM Agents: https://arxiv.org/abs/2603.07670
