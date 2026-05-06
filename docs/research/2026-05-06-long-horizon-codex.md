# Research Notes: Long-Horizon Codex

Date: 2026-05-06

## Short Answer

The winning pattern is not a bigger prompt. It is a disciplined agent loop with external state:

- stable spec
- milestone plan
- runbook
- verification at each checkpoint
- live documentation/status log
- automations or background runs that resume from those files

## Source Distillation

OpenAI's long-horizon Codex writeup describes a 25-hour Codex experiment and names the key mechanism: durable project memory in markdown files. The file stack was spec, plan, implementation runbook, and documentation/status. It also highlights the core loop: plan, edit, run tools, observe, repair, update docs, repeat.

OpenAI's Codex automation docs separate standalone automations from thread automations. Thread automations are heartbeat wakeups for the same conversation and are a good fit when continuity matters. Durable prompts should say what to do each wakeup, when to report, and when to stop.

OpenAI's memory docs say Codex memories are useful for stable preferences and recurring workflows, but required team guidance should stay in `AGENTS.md` or checked-in docs. Translation: use memories as a helpful recall layer, not the source of truth.

OpenAI's AGENTS.md docs say Codex reads global and project instructions before work, with project files closer to the current directory overriding earlier guidance. This repo should keep required behavior in root `AGENTS.md`.

OpenAI's skills docs say skills are a reusable workflow format with progressive disclosure. A repo-scoped skill is a good way to make hourly automations trigger a consistent cycle without bloating every prompt.

OpenAI's eval-skills guide recommends measuring agent-skill behavior with small eval sets, deterministic checks, JSONL traces from `codex exec --json`, and schema-based rubric checks where rules are not enough.

OpenAI's compaction docs frame long interactions as a context-management problem: carry compacted state forward and drop stale detail once a compact state exists. For this repo, the practical equivalent is to maintain concise durable state files and avoid making the next run reread every raw artifact.

METR's time-horizon work argues that agent capability is well described by the length of tasks agents can complete, and estimates a roughly seven-month doubling time for frontier agent task length. The implication is to design work as bounded, checkable chunks that can grow over time.

Recent memory-agent research points in the same direction:

- MUSE converts trajectories into structured experience after each subtask, then uses a hierarchical memory module for future planning.
- H2R separates high-level planning memory from low-level execution memory.
- MemoryAgentBench evaluates accurate retrieval, test-time learning, long-range understanding, and selective forgetting.

## Design Principles For This Repo

1. Make state inspectable. Markdown beats hidden context.
2. Split memory by level. Keep mission and constraints separate from logs and next actions.
3. Update after each cycle. Reflection delayed until the end is often reflection lost.
4. Keep prompts durable. A heartbeat prompt should be enough even after chat context is weak.
5. Measure the process. Add checks for structure, stale state, and automation prompt quality.
6. Prefer narrow cycles. Long runs are many small loops, not one grand gesture.

## Sources

- OpenAI Developers, "Run long horizon tasks with Codex" (2026-02-23): https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- OpenAI Developers, "Automations" Codex app docs: https://developers.openai.com/codex/app/automations
- OpenAI Developers, "Memories" Codex docs: https://developers.openai.com/codex/memories
- OpenAI Developers, "Custom instructions with AGENTS.md": https://developers.openai.com/codex/guides/agents-md
- OpenAI Developers, "Agent Skills": https://developers.openai.com/codex/skills
- OpenAI Developers, "Testing Agent Skills Systematically with Evals" (2026-01-22): https://developers.openai.com/blog/eval-skills
- OpenAI Developers, "Compaction": https://developers.openai.com/api/docs/guides/compaction
- METR, "Measuring AI Ability to Complete Long Tasks" (2025-03-19): https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
- Yang et al., "Learning on the Job: An Experience-Driven Self-Evolving Agent for Long-Horizon Tasks" (2025): https://arxiv.org/abs/2510.08002
- Ye et al., "H2R: Hierarchical Hindsight Reflection for Multi-Task LLM Agents" (2025): https://arxiv.org/abs/2509.12810
- Hu, Wang, McAuley, "Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions" (revised 2026): https://arxiv.org/abs/2507.05257
