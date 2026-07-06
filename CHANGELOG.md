# Changelog — PAGE

All releases bump both plugin manifests in lockstep. Entry headings follow
`## page_skill.X.Y — <date>` (the release lint requires the heading, not a mention).

## page_skill.1.0 — 2026-07-06

Initial release: the full authoring pipeline, built to the plan in `docs/BUILD_PLAN.md`.

- **Umbrella + 9 stage skills**: `page` (dispatcher), `page-intent` (interview +
  contested-choices inventory), `page-grounding` (framework map before design),
  `page-architecture` (stages, gates, dependency model, BUILD_PLAN output),
  `page-scaffold` (dual-harness repo generation), `page-draft` (skills + rubrics with
  fresh-context review), `page-test` (RED/GREEN/REFACTOR + education-specific pressure
  suite, consent-gated), `page-release` (lint, lockstep, semantic-drift grep,
  author-gated publish), `page-reflect` (post-pilot harvest, approve-per-item),
  `page-refresh` (~90-day source refresh).
- **Reference set**: `lessons_learned.md` (the nine POSED/p2d lessons as design
  requirements), `edu_grounding_library.md` (starter framework menu with scope limits),
  `gate_design_patterns.md` (gate spec + decision JSON + stale-state model),
  `dual_harness_playbook.md` (repo/symlink/lint specification),
  `skill_quality_rubric.md` (/100 reviewer instrument, threshold 85, 6 critical flags),
  `harness_adaptation.md` (placeholder mappings).
- **Scripts**: `release_lint.py` (6 checks, falsifiability-tested during this build —
  the path and changelog checks were observed failing before their fixes landed),
  `link_dev_dirs.py`.
- Sources synthesized: Anthropic skill-creator, official plugin-dev plugin, obra
  writing-skills (TDD for skills), POSED posed_skill.1.4–1.14, p2d p2d_skill.1.4–1.6.
