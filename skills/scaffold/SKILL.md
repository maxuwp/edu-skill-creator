---
name: edu-skill-creator-scaffold
description: Edu Skill Creator Stage 4 — Dual-harness repo scaffolding for a new educational plugin. Generates the single-source repo skeleton - both plugin manifests in lockstep, tool-agnostic skills tree, harness_adaptation file, parameterized release lint, symlink dev script, MAINTAINING/AGENTS docs, changelog conventions. Triggers - when the edu-skill-creator umbrella dispatches Stage 4, or the user says "scaffold the plugin repo".
version: "1.4"
---

# Edu Skill Creator Stage 4: Scaffold

Generates the repo skeleton per `<edu-skill-creator-skill-dir>/reference/dual_harness_playbook.md`
(the specification — read it before generating anything). The Claude Code manifest and
component layout follow the official plugin-dev plugin's plugin-structure conventions
(the grounding library's anchor for plugin mechanics); scope note per L1's corollary:
plugin-dev anchors the **Claude Code** manifest only — the Codex manifest is maintained
by mirroring convention (the playbook's lockstep rule), not an external spec.
Everything here is mechanical; no author gate except the lint check and the
confirmations below.

**Refuses to run** unless `architecture.md` and the new plugin's BUILD_PLAN exist and
are gate-approved. If architecture changes after a scaffold run, list which generated
files are now stale (`needs_regeneration`) and regenerate them rather than patching by
memory.

## Confirm with the author first

1. **Plugin name `<x>`** (becomes repo name, skill prefix, changelog prefix
   `<x>_skill.`, placeholder `<x>-skill-dir`).
2. **Repo location** — local path; whether/when to create the remote (creating or
   pushing to a hosting service is the author's action to authorize, never assumed).
3. **Harness set** — both Claude Code and Codex (default) or one.

Record the three answers in `scaffold_decisions.json` in the build session — a resumed
session reads it instead of re-asking (L8).

## Generate (from the approved architecture's component inventory)

```
<x>-plugin/
├── .claude-plugin/plugin.json      # version 0.1.0, lockstep
├── .codex-plugin/plugin.json
├── skills/<x>/SKILL.md             # umbrella stub: pipeline table from architecture.md
├── skills/<x>/reference/
│   ├── grounding_frameworks.md     # copied from Stage 2 output
│   ├── harness_adaptation.md       # authored fresh HERE from the confirmed plugin name; lint-whitelisted
│   ├── manifest_schema.md          # from the architecture's dependency model
│   └── hitl_protocol.md            # gate rules incl. never-accept-on-behalf (L5)
├── skills/<sub>/SKILL.md           # one stub per stage (frontmatter + spec pointer)
├── scripts/release_lint.py         # parameterized for <x>_skill. (see below)
├── scripts/link_dev_dirs.py        # <x>- prefix, umbrella keeps name
├── docs/BUILD_PLAN.md              # Stage 3 output, moved into the repo
├── MAINTAINING.md  AGENTS.md  README.md  CHANGELOG.md  .gitignore
```

If the architecture includes a gate app, copy POSED's guided app
(`skills/posed/scripts/posed_app.py` in github.com/maxuwp/posed; if a local POSED
checkout exists, prefer it — the app's modes are described in
`gate_design_patterns.md` "Session mechanics") as the starting point rather than
writing a gate UI from scratch. Stripping criteria: remove a mode when the
architecture's gate specs name no gate that uses it, and remove artifact-specific pages
whose artifact types the new plugin doesn't produce; keep the session/cloud-safe and
status-file machinery intact regardless.

## The lint (rule 0)

Adapt Edu Skill Creator's own `scripts/release_lint.py` — substitute the `<x>_skill.` prefix,
`<x>-skill-dir` placeholder, and the plugin's deprecated-URL list (empty at birth). Then
apply the falsifiability rule (L8): seed one violation per check, watch the lint fail,
fix, watch it pass. Record the seeding run in the commit message.

## Templates for the docs

- **MAINTAINING.md / AGENTS.md** — copy the rules VERBATIM from
  `dual_harness_playbook.md` "Release rules" and "Two-harness co-maintenance" (exact
  trailer values, exact heading format `## <x>_skill.X.Y — <date>`); paraphrasing these
  is how a generated repo fails its own lint later.
- **CHANGELOG.md** — starts with `## <x>_skill.0.1 — <date>` "Scaffold".

## Exit check

`git init`, initial commit, `python3 scripts/release_lint.py` exits 0, and
`link_dev_dirs.py --dry-run` resolves every skill. Mark the BUILD_PLAN items and write
the stage-end summary — per gate_design_patterns.md principle 7: what was generated,
what remains pending/stale — then continue to `edu-skill-creator-draft`.
