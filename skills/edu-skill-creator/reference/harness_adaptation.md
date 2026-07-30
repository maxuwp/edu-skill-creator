# Harness Adaptation — Edu Skill Creator placeholder mappings

SKILL bodies in this plugin are tool-agnostic. This file (whitelisted in
`scripts/release_lint.py`) defines what the neutral placeholders resolve to per harness.

| Placeholder | Claude Code | Codex | Repo checkout |
|---|---|---|---|
| `<edu-skill-creator-skill-dir>` | `~/.claude/skills/edu-skill-creator` | `~/.codex/skills/edu-skill-creator` | `skills/edu-skill-creator` |
| `<edu-skill-creator-skill-dir:NAME>` | `~/.claude/skills/edu-skill-creator-NAME` | `~/.codex/skills/edu-skill-creator-NAME` | `skills/NAME` |
| `<skills-dir>` | `~/.claude/skills` | `~/.codex/skills` | `skills/` |
| "a fresh subagent session" | a subagent via the Agent/Task tool | a fresh `codex` session or delegated agent | — |
| "ask the user with a structured question" | AskUserQuestion tool | numbered options in chat; wait for the reply | — |

**Cite a sibling skill by name, never by `..`.** The installed layout prefixes every skill
(`edu-skill-creator-scaffold`) while the repo drops the prefix (`skills/scaffold`), so a relative
`<edu-skill-creator-skill-dir>/../scaffold/…` resolves in a git checkout and dangles in the
installed harness — the failure is invisible to whoever wrote it and total for the agent that
follows it. Use `<edu-skill-creator-skill-dir:scaffold>/reference/…`, which the parameterized row
above maps correctly in all three layouts. Release lint check 16 rejects the `..` form and resolves
every remaining citation.

When Edu Skill Creator scaffolds a NEW plugin `<x>`, it generates this same file for that plugin with
`<x>-skill-dir>` entries, and whitelists it in the generated lint.

Codex-specific session mechanics (sandboxed HITL launches, `--status-file` handoff,
cloud-storage-safe staging) are documented in POSED's
`skills/posed/reference/` (`harness_adaptation.md`, `codex_desktop_hitl_launcher.md`,
`cloud_storage_safe_hitl.md`) — treat those as the canonical mechanism descriptions when
scaffolding gate apps for new plugins.
