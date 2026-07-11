---
name: edu-skill-creator-scaffold
description: Edu Skill Creator Stage 4 — Dual-harness repo scaffolding for a new educational plugin. Generates the single-source repo skeleton - both plugin manifests in lockstep, tool-agnostic skills tree, harness_adaptation file, parameterized release lint, symlink dev script, MAINTAINING/AGENTS docs, changelog conventions. Triggers - when the edu-skill-creator umbrella dispatches Stage 4, or the user says "scaffold the plugin repo".
version: "1.7"
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
├── skills/<x>/scripts/validate_<artifact>.py  # ONE per artifact in the architecture's
│                                   #   item-11 computed-validation plan (see below)
├── tests/fixtures/<artifact>_fail/ # expected exit 1 — mirrors a real failure shape
├── tests/fixtures/<artifact>_pass/ # expected exit 0 — minimal compliant session
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

## Validator scaffolding (L11)

For every artifact in the approved architecture's item-11 computed-validation plan,
instantiate `<edu-skill-creator-skill-dir>/../scaffold/reference/validator_template.py`
as `skills/<x>/scripts/validate_<artifact>.py`: replace ARTIFACT, set
`CONTRACT_VERSION`, and turn the plan's structural requirements into the CHECKS list
(the template's sample checks show the shapes: fail-closed required files/records,
per-id upstream coverage — never count matches — forbidden markers, distribution
checks). The runner block is not edited. Then wire both callers in the generated stubs:
the drafter stub says "run `validate_<artifact>.py` pre-gate and fix criticals before
handing off"; the reviewer stub's output schema includes
`computed_checks.<artifact>_validator_pass` + report path, with `approve` illegal
unless true; the umbrella stub refuses to open the human gate on a review log missing
them. Create both fixture dirs per validator (the negative fixture mirrors a real
failure shape and NEVER contains student/faculty course content), and add the
fixture-runner check from the template's docstring to the generated lint. POSED's
`validate_stage5_slides.py` / `validate_outline.py` are the worked examples.

## The lint (rule 0)

Adapt Edu Skill Creator's own `scripts/release_lint.py` — substitute the `<x>_skill.` prefix,
`<x>-skill-dir` placeholder, and the plugin's deprecated-URL list (empty at birth). Then
apply the falsifiability rule (L8): seed one violation per check, watch the lint fail,
fix, watch it pass — and for the fixture-runner check, neutralize the negative fixture
and watch the LINT fail (prove the proof, both directions). Record the seeding runs in
the commit message.

## Templates for the docs

- **MAINTAINING.md / AGENTS.md** — copy the rules VERBATIM from
  `dual_harness_playbook.md` "Release rules" and "Two-harness co-maintenance" (exact
  trailer values, exact heading format `## <x>_skill.X.Y — <date>`); paraphrasing these
  is how a generated repo fails its own lint later.
- **CHANGELOG.md** — starts with `## <x>_skill.0.1 — <date>` "Scaffold".

## Exit check

`git init`, initial commit, `python3 scripts/release_lint.py` exits 0 (including the
validator fixture pairs), each `validate_<artifact>.py` compiles and exits 2 on a bare
directory (fail-closed default proven before any real session exists), and
`link_dev_dirs.py --dry-run` resolves every skill. Mark the BUILD_PLAN items and write
the stage-end summary — per gate_design_patterns.md principle 7: what was generated,
what remains pending/stale — then continue to `edu-skill-creator-draft`.
