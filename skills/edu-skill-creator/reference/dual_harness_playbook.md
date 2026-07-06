# Dual-Harness Playbook — one repo, every harness

The maintenance architecture that ended copy-drift between Claude Code and Codex for
POSED/p2d (L7). `edu-skill-creator-scaffold` generates this layout for every new educational plugin;
this file is the specification.

## Repo layout (per plugin, name `<x>`)

```
<x>-plugin/                      # local working clone; = github.com/<owner>/<x>
├── .claude-plugin/plugin.json   # Claude Code manifest
├── .codex-plugin/plugin.json    # Codex manifest — SAME version, always
├── agents/*.md                  # Claude agent defs (if any)
├── .codex/agents/*.toml         # Codex agent defs (mirror)
├── skills/
│   ├── <x>/                     # umbrella skill (keeps full name)
│   │   └── reference/           # incl. harness_adaptation.md (whitelisted)
│   └── <sub>/                   # sub-skills WITHOUT the <x>- prefix
├── scripts/release_lint.py      # run before every push (rule 0)
├── scripts/link_dev_dirs.py     # symlink personal skill dirs into the repo
├── docs/BUILD_PLAN.md           # resumable build checklist (L8)
├── MAINTAINING.md  AGENTS.md  README.md  CHANGELOG.md
```

## The symlink model

Personal skill dirs are symlinks into the repo — there is never a second copy:

```
~/.claude/skills/<x>-<sub>  →  <repo>/skills/<sub>
~/.codex/skills/<x>-<sub>   →  <repo>/skills/<sub>
```

The umbrella skill keeps its full name (`<x>` → `skills/<x>`). Skills carrying installed
artifacts (e.g. node_modules) stay real directories and are listed as exceptions in
`link_dev_dirs.py`. The link script is idempotent and moves any real directory in the way
to a timestamped backup before linking — always reversible.

## Tool-agnostic SKILL bodies

SKILL.md bodies are shared verbatim across harnesses. Therefore:

- Use neutral placeholders — `<the-plugin's-skill-dir>/scripts/…`, `<skills-dir>/…` — never
  literal `~/.claude/…` or `~/.codex/…` paths. The mapping table lives in exactly one
  whitelisted file: `skills/<x>/reference/harness_adaptation.md`.
- Say "a fresh subagent session," not a harness-specific agent API name.
- Harness-specific escape hatches (sandbox launchers, status-file handoffs) live in scoped
  reference files with one neutral pointer from the SKILL body.

## Release rules

1. **Rule 0:** `python3 scripts/release_lint.py` must exit 0 before any push.
2. `git pull` before editing (the other harness may have pushed).
3. Bump BOTH plugin.json files in lockstep; add a `## <x>_skill.X.Y — <date>` heading to
   CHANGELOG.md (a teaser mention is not an entry — the lint checks for the heading).
4. Commit trailer `Found-on: claude-code | codex-desktop | codex-cli | user-pilot-review`
   so cross-harness discoveries stay visible.
5. Committing IS publishing. Never copy files between trees.

## release_lint.py — the drift classes worth linting

Lint what has actually bitten a release, nothing speculative:

| Check | Class | Why |
|---|---|---|
| Hardcoded `~/.claude/` or `~/.codex/` in skills/**/*.md (whitelist: harness_adaptation.md) | error | Leaked 17 times in one POSED release |
| Both manifests same version | error | Lockstep rule |
| Deprecated repo URLs outside CHANGELOG | error | Post-merge stragglers |
| Scored rubric dimensions sum to 100 (only files marked "100 points" or "/100") | error | Silent rubric drift |
| CHANGELOG has `## <x>_skill.X.Y ` heading for current version | error | Teaser lines once false-passed |
| Reference files cited by SKILLs exist | warn | Dangling pointers |

**Falsifiability rule (L8):** when adding a lint check, first seed the violation and watch
the lint fail, then fix and watch it pass. A lint that can false-pass is worse than none.

## Two-harness co-maintenance

Both agents (Claude Code and Codex) develop the plugin and find different issues — that
is the point. AGENTS.md at the repo root carries the rules above so either harness picks
them up cold. Semantic drift (new rule added at the top, stale text surviving below) is
NOT lintable — the defense is (a) grep the whole skill set for the old rule's phrasing
whenever a rule or schema changes, and (b) the other harness acting as cross-reviewer.
