# AGENTS.md — Edu Skill Creator (Codex + Claude Code)

This repo is the **single source of truth** for Edu Skill Creator on both harnesses. It ships the
Claude Code plugin (`.claude-plugin/`) and the Codex plugin (`.codex-plugin/`) from one
shared `skills/` set.

**The personal skill dirs are symlinks into this repo.** `<skills-dir>/edu-skill-creator-<x>` →
`skills/<x>` (the `edu-skill-creator-` prefix is dropped here; the umbrella
`edu-skill-creator` keeps its name).
Editing a skill through the personal dir edits this repo directly — there is no second
copy.

## Rules for every change

1. `git pull` before editing (the other harness may have pushed).
2. `python3 scripts/release_lint.py` must exit 0 before every push (rule 0).
3. `git commit && git push` from this repo — committing *is* publishing; never copy
   files between trees.
4. Commit trailer `Found-on: codex-desktop` / `codex-cli` / `claude-code` so
   cross-harness work stays visible.
5. **Keep SKILL bodies tool-agnostic.** No literal harness paths — use
   `<edu-skill-creator-skill-dir>/…` / `<skills-dir>/…` per
   `skills/edu-skill-creator/reference/harness_adaptation.md`. Say "a fresh subagent session," not a
   harness-specific API name.
6. Bump BOTH plugin.json files in lockstep on release; add a real
   `## edu_skill_creator.X.Y — <date>` heading to CHANGELOG.md.
7. When changing a rule or schema, grep `skills/` for the old phrasing — stale lower
   sections are the drift class the lint can't catch; you are the cross-reviewer.

Full detail: **MAINTAINING.md** and `skills/edu-skill-creator/reference/dual_harness_playbook.md`.
