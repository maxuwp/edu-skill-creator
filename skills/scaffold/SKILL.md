---
name: page-scaffold
description: PAGE Stage 4 — Dual-harness repo scaffolding for a new educational plugin. Generates the single-source repo skeleton - both plugin manifests in lockstep, tool-agnostic skills tree, harness_adaptation file, parameterized release lint, symlink dev script, MAINTAINING/AGENTS docs, changelog conventions. Triggers - when the page umbrella dispatches Stage 4, or the user says "scaffold the plugin repo".
version: "1.0"
---

# PAGE Stage 4: Scaffold

Generates the repo skeleton per `<page-skill-dir>/reference/dual_harness_playbook.md`
(the specification — read it before generating anything). Everything here is mechanical;
no author gate except the lint check and the naming confirmations below.

## Confirm with the author first

1. **Plugin name `<x>`** (becomes repo name, skill prefix, changelog prefix
   `<x>_skill.`, placeholder `<x>-skill-dir`).
2. **Repo location** — local path; whether/when to create the remote (creating or
   pushing to a hosting service is the author's action to authorize, never assumed).
3. **Harness set** — both Claude Code and Codex (default) or one.

## Generate (from the approved architecture's component inventory)

```
<x>-plugin/
├── .claude-plugin/plugin.json      # version 0.1.0, lockstep
├── .codex-plugin/plugin.json
├── skills/<x>/SKILL.md             # umbrella stub: pipeline table from architecture.md
├── skills/<x>/reference/
│   ├── grounding_frameworks.md     # copied from Stage 2 output
│   ├── harness_adaptation.md       # <x>-skill-dir mappings; lint-whitelisted
│   ├── manifest_schema.md          # from the architecture's dependency model
│   └── hitl_protocol.md            # gate rules incl. never-accept-on-behalf (L5)
├── skills/<sub>/SKILL.md           # one stub per stage (frontmatter + spec pointer)
├── scripts/release_lint.py         # parameterized for <x>_skill. (see below)
├── scripts/link_dev_dirs.py        # <x>- prefix, umbrella keeps name
├── docs/BUILD_PLAN.md              # Stage 3 output, moved into the repo
├── MAINTAINING.md  AGENTS.md  README.md  CHANGELOG.md  .gitignore
```

If the architecture includes a gate app, copy POSED's guided app
(`skills/posed/scripts/posed_app.py` in github.com/maxuwp/posed) as the starting point
and strip modes the design doesn't use — do not write a gate UI from scratch.

## The lint (rule 0)

Adapt PAGE's own `scripts/release_lint.py` — substitute the `<x>_skill.` prefix,
`<x>-skill-dir` placeholder, and the plugin's deprecated-URL list (empty at birth). Then
apply the falsifiability rule (L8): seed one violation per check, watch the lint fail,
fix, watch it pass. Record the seeding run in the commit message.

## Templates for the docs

- **MAINTAINING.md** — rule 0 (lint before push), pull-before-edit, lockstep version
  bumps, changelog heading format, Found-on trailers, tool-agnostic-body rule.
- **AGENTS.md** — the condensed rules for the other harness's agent, mirroring POSED's.
- **CHANGELOG.md** — starts with `## <x>_skill.0.1 — <date>` "Scaffold".

## Exit check

`git init`, initial commit, `python3 scripts/release_lint.py` exits 0, and
`link_dev_dirs.py --dry-run` resolves every skill. Mark the BUILD_PLAN items, write the
stage-end summary, continue to `page-draft`.
