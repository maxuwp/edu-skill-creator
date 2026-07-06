# Harness Adaptation — PAGE placeholder mappings

SKILL bodies in this plugin are tool-agnostic. This file (whitelisted in
`scripts/release_lint.py`) defines what the neutral placeholders resolve to per harness.

| Placeholder | Claude Code | Codex |
|---|---|---|
| `<page-skill-dir>` | `~/.claude/skills/page` | `~/.codex/skills/page` |
| `<skills-dir>` | `~/.claude/skills` | `~/.codex/skills` |
| "a fresh subagent session" | a subagent via the Agent/Task tool | a fresh `codex` session or delegated agent |
| "ask the user with a structured question" | AskUserQuestion tool | numbered options in chat; wait for the reply |

When PAGE scaffolds a NEW plugin `<x>`, it generates this same file for that plugin with
`<x>-skill-dir>` entries, and whitelists it in the generated lint.

Codex-specific session mechanics (sandboxed HITL launches, `--status-file` handoff,
cloud-storage-safe staging) are documented in POSED's
`skills/posed/reference/` (`harness_adaptation.md`, `codex_desktop_hitl_launcher.md`,
`cloud_storage_safe_hitl.md`) — treat those as the canonical mechanism descriptions when
scaffolding gate apps for new plugins.
