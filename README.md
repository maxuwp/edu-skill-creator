# Edu Skill Creator

A meta-plugin: the framework, process, and supervision for creating **educational
plugins** (HITL-gated agent pipelines that produce teaching artifacts). Edu Skill Creator exists so
that every new educational plugin starts from an established, framework-grounded process
instead of ad-hoc drafting — and starts from the lessons already paid for while building
[POSED](https://github.com/maxuwp/posed) (lecture/curriculum authoring, 14 releases) and
[p2d](https://github.com/maxuwp/p2d) (paper-to-deck, 6 releases).

## What it synthesizes

- **Anthropic's skill-creator** ([anthropics/skills](https://github.com/anthropics/skills)) —
  the skill lifecycle: intent → interview → draft → evals → iterate → package; progressive
  disclosure; the principle of generalization.
- **The official plugin-dev plugin** ([anthropics/claude-code](https://github.com/anthropics/claude-code/tree/main/plugins/plugin-dev)) —
  plugin component structure, the 8-phase creation workflow, validation tooling.
- **obra's writing-skills** ([obra/superpowers](https://github.com/obra/superpowers)) —
  TDD for skills: RED baseline pressure scenarios → GREEN minimal skill → REFACTOR
  loopholes closed.
- **The POSED/p2d lessons ledger** (`skills/edu-skill-creator/reference/lessons_learned.md`) — nine
  design requirements paid for by real pilot failures: framework grounding with scope
  discipline; contested pedagogical choices as explicit options, never author defaults;
  drafter ≠ reviewer; narrow dependency-aware gates; structured decision JSON; consent
  ladders for expensive runs; single-source dual-harness repos with drift lint;
  resumable build plans and falsifiable lints; refresh + reflect loops.

## Pipeline

`edu-skill-creator` (umbrella) dispatches: `edu-skill-creator-intent` → `edu-skill-creator-grounding` → `edu-skill-creator-architecture` →
`edu-skill-creator-scaffold` → `edu-skill-creator-draft` → `edu-skill-creator-test` → `edu-skill-creator-release` → `edu-skill-creator-reflect`, with
`edu-skill-creator-refresh` as the ~90-day maintenance loop. Each stage ends at a human gate; Edu Skill Creator
never approves on the author's behalf.

## Install

Both harnesses are served from this one repo (`.claude-plugin/` and `.codex-plugin/`
manifests in lockstep). For development, `scripts/link_dev_dirs.py` symlinks the
personal skill directories into `skills/`.

## Maintenance

See `MAINTAINING.md` (rule 0: `scripts/release_lint.py` before every push) and
`AGENTS.md` for the cross-harness rules. Build history: `docs/BUILD_PLAN.md` and
`CHANGELOG.md`.

## License

MIT — © Xiaoguang Ma (maxuwplatt@gmail.com), UW-Platteville.
