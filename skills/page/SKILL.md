---
name: page
description: PAGE — Plugin Authoring for Grounded Education. Umbrella workflow for creating a NEW educational plugin or skill set (or overhauling an existing one) with an established, framework-grounded process instead of ad-hoc drafting. Guides the author through intent interview, framework grounding, pipeline architecture, dual-harness scaffolding, skill drafting with independent review, TDD-style testing, release, and post-pilot reflection. Triggers - when the user wants to "make a plugin/skill for <educational task>", "turn this teaching workflow into a plugin", "build a skill set like POSED", or asks how to structure an educational agent pipeline.
version: "1.0"
---

# PAGE — Plugin Authoring for Grounded Education

You are supervising the creation of an **educational plugin**: a HITL-gated agent
pipeline that produces teaching artifacts (lessons, decks, labs, assessments, feedback,
advising flows…). PAGE exists because building POSED and p2d taught nine expensive
lessons — read `<page-skill-dir>/reference/lessons_learned.md` before doing anything.
Every lesson there is a design requirement for the plugin you are about to build.

## Operating rules (apply to every stage)

1. **Grounding (L1).** No stage of the new plugin may invent process or criteria where a
   citable framework exists. The grounding map is written BEFORE architecture.
2. **No author defaults (L2).** Pedagogically contested choices become explicit intake
   options in the new plugin — including choices YOU, the builder, feel strongly about.
3. **Drafter ≠ reviewer (L3).** Applies to the new plugin's stages AND to PAGE itself:
   drafted skills are reviewed by a fresh subagent session against
   `<page-skill-dir>/reference/skill_quality_rubric.md`.
4. **Human gates (L5).** Present each PAGE gate to the author and wait. Never approve on
   their behalf; "prefer defaults" means prefill, never bypass.
5. **Resumable (L8).** Stage 3 emits a BUILD_PLAN checklist; every later stage marks its
   items as they land, so any session can resume at the first unchecked item.
6. **Cost consent (L6).** Test sweeps and simulations are offered full / lite / skip with
   the cost stated plainly; record the chosen mode.

## Pipeline

| Stage | Skill | Output artifact | Gate |
|---|---|---|---|
| 1 Intent | `page-intent` | `intent.md` + contested-choices inventory | author approves intent |
| 2 Grounding | `page-grounding` | `grounding_frameworks.md` (new plugin's map) | author approves map; unanchored stages resolved |
| 3 Architecture | `page-architecture` | `architecture.md` + `BUILD_PLAN.md` + manifest/dependency schema | author approves design |
| 4 Scaffold | `page-scaffold` | dual-harness repo skeleton + lint + link script | lint exits 0 |
| 5 Draft | `page-draft` | SKILL.md files + rubrics, each independently reviewed | per-skill review ≥85, no critical flags → author gate (batched) |
| 6 Test | `page-test` | RED/GREEN/REFACTOR log + eval results | consent-gated; author reviews findings |
| 7 Release | `page-release` | lint-clean tagged release, CHANGELOG entry | rule-0 lint + author approves publish |
| 8 Reflect | `page-reflect` | pilot-lesson harvest → updates to the plugin AND to PAGE's lessons_learned.md | author approves each harvested item |
| — Refresh | `page-refresh` | ~90-day authoring-practice/framework refresh ledger | approve-per-item |

Stages run in order; each dispatches its skill. **Auto-continue:** after a gate is
approved, proceed to the next stage without re-asking, but announce the transition with a
one-paragraph stage-end summary (what was decided, what it constrains downstream).

## Session state

Keep a working directory for the build (default: alongside the new plugin's repo,
`docs/` once the repo exists; before that, a `<plugin-name>-design/` folder the author
chooses). Artifacts: `intent.md`, `grounding_frameworks.md`, `architecture.md`,
`BUILD_PLAN.md`, review logs `reviews/<skill>_review.json`, test logs `tests/`.

Track progress in `BUILD_PLAN.md` checkboxes — that file is the single source of truth
for "where are we." On session start, read it first and resume.

## Reference files

- `reference/lessons_learned.md` — the nine lessons; read first, always.
- `reference/edu_grounding_library.md` — starter framework menu + scope rules.
- `reference/gate_design_patterns.md` — gate spec, decision JSON, stale-state model.
- `reference/dual_harness_playbook.md` — repo layout, symlinks, lint, release rules.
- `reference/skill_quality_rubric.md` — the /100 instrument for reviewing drafted skills.
- `reference/harness_adaptation.md` — placeholder → path mappings (harness-specific).

## What PAGE is not

PAGE builds *educational* plugins. For a generic (non-educational) plugin, point the
author at Anthropic's skill-creator and the official plugin-dev plugin instead — PAGE's
extra machinery (grounding maps, stance inventories, gate patterns) earns its cost only
where pedagogy and human sign-off are central.
