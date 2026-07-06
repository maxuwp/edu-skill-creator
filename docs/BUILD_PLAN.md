# Edu Skill Creator Build Plan — resumable checklist

Edu Skill Creator = **Plugin Authoring for Grounded Education**. A meta-plugin that provides the
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
- [x] skills/edu-skill-creator/reference/lessons_learned.md — the distilled POSED/p2d ledger (keystone)
- [x] skills/edu-skill-creator/reference/edu_grounding_library.md — starter framework library + scope rule
- [x] skills/edu-skill-creator/reference/gate_design_patterns.md — HITL gate + dependency-model patterns
- [x] skills/edu-skill-creator/reference/dual_harness_playbook.md — repo layout, symlinks, lint, lockstep
- [x] skills/edu-skill-creator/reference/harness_adaptation.md — placeholder → path mappings (whitelisted)
- [x] skills/edu-skill-creator/reference/skill_quality_rubric.md — /100 reviewer rubric for drafted skills
- [x] skills/edu-skill-creator/SKILL.md — umbrella dispatcher (stages, gates, auto-continue)
- [x] skills/intent/SKILL.md (edu-skill-creator-intent) — interview + contested-choice inventory
- [x] skills/grounding/SKILL.md (edu-skill-creator-grounding) — framework map before design
- [x] skills/architecture/SKILL.md (edu-skill-creator-architecture) — pipeline/gates/dependency design + build checklist output
- [x] skills/scaffold/SKILL.md (edu-skill-creator-scaffold) — dual-harness repo generation
- [x] skills/draft/SKILL.md (edu-skill-creator-draft) — SKILL.md + rubric authoring, fresh-context review
- [x] skills/test/SKILL.md (edu-skill-creator-test) — RED/GREEN/REFACTOR + consent-gated evals
- [x] skills/release/SKILL.md (edu-skill-creator-release) — lint, changelog, lockstep, packaging
- [x] skills/reflect/SKILL.md (edu-skill-creator-reflect) — harvest pilot lessons into lessons_learned.md
- [x] skills/refresh/SKILL.md (edu-skill-creator-refresh) — ~90-day authoring-practice/framework refresh
- [x] scripts/release_lint.py — edu_skill_creator. prefix, <edu-skill-creator-skill-dir> placeholder
- [x] scripts/link_dev_dirs.py — edu-skill-creator- prefix, KEEP_NAME {edu-skill-creator}
- [x] MAINTAINING.md, AGENTS.md, README.md, CHANGELOG.md (## edu_skill_creator.1.0 entry)
- [x] Run link_dev_dirs.py (both trees); verify symlinks resolve
- [x] Run release_lint.py → 0 errors
- [x] git commit (Found-on: claude-code)
- [x] ASK USER: create github.com/maxuwp/edu-skill-creator + push (outward action — needs explicit OK)
- [x] Codex verification checklist handed to user (Codex review received 2026-07-06)

## edu_skill_creator.1.1 follow-up (Codex review findings, 2026-07-06)

- [x] Stage 1 intent: data/privacy/security question (A.7), accessibility question (A.8),
      three new contested postures (accessibility, student-data, external-service)
- [x] Grounding library: privacy/security/accessibility section (WCAG 2.2, UDL 3.0,
      FERPA/PPRA + PTAC, NIST SSDF consolidated)
- [x] Architecture: mandatory data-flow & security model item + output section
- [x] skill_quality_rubric: critical flags 7–9 (ungoverned student data, undisclosed
      external services, inaccessible HITL pages)
- [x] edu-skill-creator-test: pressure scenarios 7–10 (data leakage, undisclosed external call,
      log/redaction failure, gate accessibility)
- [x] release_lint check 7: manifest homepage/repository vs git origin
      (falsifiability-tested: wrong origin → ERROR, no origin → WARN)
- [x] edu-skill-creator-release: publish-check pointer in step 8
- [x] Independent reviews, round 1: edu-skill-creator (90), edu-skill-creator-intent (87), edu-skill-creator-grounding (63,
      regenerated), edu-skill-creator-scaffold (70, revised) — fixes applied, logs in reviews/
- [x] Independent reviews, round 1: architecture (78), draft (79, 1 crit), test (78),
      release (80), reflect (71, 2 crit), refresh (72, 1 crit) — all findings fixed
- [x] Re-reviews: edu-skill-creator (97), grounding (97), scaffold (98), architecture (95),
      draft (95), test (97), release (90), reflect (88), refresh (91→90 after Part C/B
      reviewer fix) — table green, 0 criticals (reviews/README.md is the record)
- [x] Side catch from review round: posed-refresh symlinks were missing in both harness
      trees (skill added after link script last ran) — relinked via POSED's
      link_dev_dirs.py
- [x] Bump both manifests to 1.1.0 + `## edu_skill_creator.1.1` CHANGELOG heading
- [x] Final lint, commit (Found-on: claude-code), push

## Source anchors (what each stage borrows)

| Edu Skill Creator stage | Primary sources |
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
