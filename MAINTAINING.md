# MAINTAINING — PAGE

This repo is the **single source of truth** for PAGE on both harnesses (Claude Code and
Codex). It follows the dual-harness playbook it teaches:
`skills/page/reference/dual_harness_playbook.md` is the full specification — this file
is the operational summary.

## Rule 0

`python3 scripts/release_lint.py` must exit 0 before every push. When you ADD a lint
check, first seed a violation and watch it fail (a lint that can false-pass is worse
than no lint).

## Every change

1. `git pull` before editing — the other harness may have pushed.
2. Edit through the symlinked working dirs (`<skills-dir>/page-<x>`) or here directly;
   they are the same files. Never copy files between trees.
3. Keep SKILL bodies tool-agnostic: `<page-skill-dir>/…` placeholders, "a fresh subagent
   session". Harness specifics live only in
   `skills/page/reference/harness_adaptation.md` (lint-whitelisted, with
   `dual_harness_playbook.md`).
4. When a rule or schema changes, grep the whole `skills/` tree for the OLD phrasing —
   semantic drift (new rule on top, stale text below) is the one class the lint cannot
   catch.
5. Verify edits landed before committing a batch (a mid-script abort once produced a
   bad partial commit in POSED).

## Releases

- Bump `.claude-plugin/plugin.json` AND `.codex-plugin/plugin.json` in lockstep.
- **Uniform skill versioning:** every `skills/*/SKILL.md` frontmatter `version` equals
  the plugin's major.minor and is bumped together on release (lint check 8 enforces
  it). Per-skill change history lives in CHANGELOG, not in the frontmatter.
- Review evidence is mechanical: every `reviews/*_review.json` finding needs
  `status: fixed|accepted`, a non-empty `resolution`, and a file-level
  `resolution_pass` block (lint check 9 enforces it).
- After the publish gate, run `python3 scripts/release_lint.py --publish` — in this
  mode a manifest that claims a hosted repo with no configured origin is an error,
  not a warning.
- Add a real `## page_skill.X.Y — <date>` heading to CHANGELOG.md (teaser mentions
  don't count and don't pass the lint).
- Commit trailer: `Found-on: claude-code | codex-desktop | codex-cli | user-pilot-review`.
- Update `docs/BUILD_PLAN.md` checkboxes if the release completes plan items.

## Dev setup on a fresh machine

`python3 scripts/link_dev_dirs.py` — symlinks `~/.claude/skills/page-<x>` and
`~/.codex/skills/page-<x>` into `skills/<x>` (idempotent; backs up anything in the way).
See the script docstring.

## Sibling repos

POSED (github.com/maxuwp/posed) and p2d (github.com/maxuwp/p2d) are the plugins whose
development produced PAGE's `lessons_learned.md`; their pilots feed `page-reflect`.
