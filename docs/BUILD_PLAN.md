# PAGE v1.0 Build Plan — resumable checklist

PAGE = **Plugin Authoring for Grounded Education**. A meta-plugin that provides the
framework, process, and supervision for creating educational plugins — synthesized from
Anthropic's skill-creator, the official plugin-dev plugin, obra's writing-skills (TDD for
skills), and the lessons learned building and improving POSED (14 releases) and p2d (6
releases).

Rule (lesson 8): implement in checklist order, mark each item the moment it lands, commit
in coherent batches. If a session ends mid-build, the next session resumes at the first
unchecked item.

## Checklist

- [x] Repo tree + git init
- [x] docs/BUILD_PLAN.md (this file)
- [x] .claude-plugin/plugin.json + .codex-plugin/plugin.json (1.0.0, lockstep)
- [x] .gitignore
- [x] skills/page/reference/lessons_learned.md — the distilled POSED/p2d ledger (keystone)
- [x] skills/page/reference/edu_grounding_library.md — starter framework library + scope rule
- [x] skills/page/reference/gate_design_patterns.md — HITL gate + dependency-model patterns
- [x] skills/page/reference/dual_harness_playbook.md — repo layout, symlinks, lint, lockstep
- [x] skills/page/reference/harness_adaptation.md — placeholder → path mappings (whitelisted)
- [x] skills/page/reference/skill_quality_rubric.md — /100 reviewer rubric for drafted skills
- [x] skills/page/SKILL.md — umbrella dispatcher (stages, gates, auto-continue)
- [x] skills/intent/SKILL.md (page-intent) — interview + contested-choice inventory
- [x] skills/grounding/SKILL.md (page-grounding) — framework map before design
- [x] skills/architecture/SKILL.md (page-architecture) — pipeline/gates/dependency design + build checklist output
- [x] skills/scaffold/SKILL.md (page-scaffold) — dual-harness repo generation
- [x] skills/draft/SKILL.md (page-draft) — SKILL.md + rubric authoring, fresh-context review
- [x] skills/test/SKILL.md (page-test) — RED/GREEN/REFACTOR + consent-gated evals
- [x] skills/release/SKILL.md (page-release) — lint, changelog, lockstep, packaging
- [x] skills/reflect/SKILL.md (page-reflect) — harvest pilot lessons into lessons_learned.md
- [x] skills/refresh/SKILL.md (page-refresh) — ~90-day authoring-practice/framework refresh
- [x] scripts/release_lint.py — page_skill. prefix, <page-skill-dir> placeholder
- [x] scripts/link_dev_dirs.py — page- prefix, KEEP_NAME {page}
- [x] MAINTAINING.md, AGENTS.md, README.md, CHANGELOG.md (## page_skill.1.0 entry)
- [x] Run link_dev_dirs.py (both trees); verify symlinks resolve
- [x] Run release_lint.py → 0 errors
- [x] git commit (Found-on: claude-code)
- [ ] ASK USER: create github.com/maxuwp/page + push (outward action — needs explicit OK)
- [ ] Codex verification checklist handed to user

## Source anchors (what each stage borrows)

| PAGE stage | Primary sources |
|---|---|
| intent | skill-creator "capture intent + interview"; POSED lesson: author preference ≠ default |
| grounding | POSED grounding release (posed_skill.1.10/1.11); scope-discipline rule |
| architecture | plugin-dev phases 2–3; POSED dependency model + gate design + resumable checklist |
| scaffold | plugin-dev plugin-structure; POSED dual-harness playbook (MAINTAINING/AGENTS/lint/symlinks) |
| draft | skill-creator writing doctrine (progressive disclosure, <500 lines, explain-why); POSED drafter≠reviewer |
| test | obra writing-skills TDD (RED/GREEN/REFACTOR); skill-creator evals; POSED cost-consent ladder |
| release | plugin-dev validation; POSED release hygiene (lint, lockstep, Found-on trailers) |
| reflect | posed-reflect / p2d-reflect pattern |
| refresh | posed-refresh pattern |
