# Changelog — PAGE

All releases bump both plugin manifests in lockstep. Entry headings follow
`## page_skill.X.Y — <date>` (the release lint requires the heading, not a mention).

## page_skill.1.1 — 2026-07-06

Codex review round: privacy/security/accessibility hardening + PAGE reviewed by its own
instrument.

- **Stage 1 intent**: new interview questions A.7 (student data/PII, FERPA/PPRA +
  institutional constraints, retention/deletion, de-identification, external
  API/vendor exposure, logging/redaction, permissions) and A.8 (accessibility, incl.
  the plugin's own HITL pages); three new contested postures (accessibility,
  student-data handling, external-service); persisted `intent_gate_decision.json`.
- **Grounding library**: new privacy/security/accessibility section — W3C WCAG 2.2,
  CAST UDL 3.0, FERPA/PPRA + Dept. of Education PTAC, NIST SP 800-218 (consolidated).
- **Architecture**: mandatory data-flow & security model for plugins touching student
  data, external services, or generated UI; exact inputs + refusal conditions;
  independent design review + full gate spec.
- **skill_quality_rubric**: critical flags 7–9 (ungoverned student data, undisclosed
  external services, inaccessible HITL pages).
- **page-test**: pressure scenarios 7–10 (student-data leakage, undisclosed external
  call, log/redaction failure, gate keyboard/screen-reader operability); fresh-context
  GREEN judges; exit gate spec (`test_gate`).
- **release_lint check 7**: manifests' homepage/repository URLs must match the git
  origin (mismatch = error, missing origin = warning). Falsifiability-tested in both
  directions before landing. Lint also hardened against a missing CHANGELOG.
- **PAGE reviewed by PAGE's rubric** (durable evidence in `reviews/`): all 10 skills
  cold-reviewed by fresh-context subagents, findings fixed, revised skills
  re-reviewed to a green board — final scores 88–98, zero critical flags. The round
  caught real defects in its own author: no self stale-state at the umbrella (fixed:
  operating rules 7–8), grounding/reflect/draft/refresh shipping without the
  independent-review or invalidation discipline they preach (all fixed), and — outside
  the repo entirely — POSED's `posed-refresh` symlinks missing from both harness trees
  (relinked).
- Every stage gate now carries the full gate-spec table (gate_id, decision_file,
  owns, invalidates, consent); binary inspections are explicitly distinguished from
  scored rubrics (Fagan/IEEE 1028).

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
