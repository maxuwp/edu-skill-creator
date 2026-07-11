# Changelog — Edu Skill Creator

All releases bump both plugin manifests in lockstep. Entry headings follow
`## edu_skill_creator.X.Y — <date>` (the release lint requires the heading, not a mention).

## edu_skill_creator.1.7 — 2026-07-10

L11 becomes generated, not just required: scaffold ships a validator template.

- New `skills/scaffold/reference/validator_template.py` — self-contained,
  import-free skeleton embodying every L11 corollary: fail-closed helpers
  (`require_file`/`require_record` — missing = critical, never a skip; crashing check =
  failing check; exit 2 when the session can't even be read), L12 contract-era +
  `generated_by` helpers, per-id upstream-coverage pattern (never count matches), a
  repetition/distribution helper, report JSON with `passed`/counts/findings, and the
  fixture-runner lint check in its docstring. Behavior-proven before shipping: exit 2 on
  bare/unreadable sessions, exit 1 with a written report on missing records, exit 0 on a
  compliant sample.
- `edu-skill-creator-scaffold`: new "Validator scaffolding (L11)" section — one
  instantiation per architecture item-11 artifact; both callers wired into the generated
  drafter/reviewer/umbrella stubs; `tests/fixtures/<artifact>_{fail,pass}/` in the
  generated tree; the generated lint gains the fixture-runner check with both-direction
  falsifiability ("neutralize the negative fixture and watch the LINT fail"); exit check
  extended (each validator compiles + exits 2 on a bare directory before any session
  exists).
- Cross-refs: architecture item 11 notes the plan only names artifacts + requirements
  (scaffold designs nothing ad hoc); L12's enforcement paragraph records that the
  template is generated. POSED's `validate_stage5_slides.py`/`validate_outline.py`
  cited as worked examples.

## edu_skill_creator.1.6 — 2026-07-10

Reflect harvest from the POSED 1.15–1.30.1 release run (16 releases, 4 days, the
three-model review loop): two new lessons, one corollary, and gate-pattern hardening.

- **L11 — prose contracts rot; computed, fail-closed validators.** The defining pilot
  fact: a deck passed FOUR fresh-context reviews at 94/100 while carrying 13 structural
  criticals, and its approved outline scored 97/100 with 5 more. LLM review establishes
  judgment, not structure. Rule: one validator implementation, two callers (drafter
  pre-gate + reviewer hard gate); `approve` illegal without recorded computed passes.
  Corollaries: fail closed (missing record/artifact/contract = refusal — six fail-open
  holes found by adversarial review in 1.30.1); prove by attack, not only by fixture;
  falsifiability against real failing artifacts + synthetic fixtures (never course
  content); distribution checks (one sentence ×54 passed a 98% word-count band);
  anti-softener rubric language; server-stamped decisions (mechanical L5).
- **L12 — live sessions outlive releases.** `generated_by` + server-owned
  `session_contract_version` on every artifact; contract upgrades distinguished from
  quality gaps; schema changes route to TARGETED amendments of the owning step, never
  full regeneration; unknown contract versions fail closed (a live session carrying
  "1.13" had disarmed every ≥1.29 check).
- **L7 corollary — one canonical implementation inside the plugin**: POSED shipped three
  divergent pacing formulas and two key vocabularies for one concept; prose cites the
  canonical script, never restates values; near-miss keys hard-fail with "did you mean".
- **gate_design_patterns 8–11**: AI pre-fills recommend but hard gates still block
  (`faculty_overrode` audit trail); blank-gate guard + server-stamped decisions; agent
  silence during human review; gate links never navigate away.
- **architecture**: item 5 gains the contract axis (L12); new item 11 computed-validation
  plan (L11). **rubric**: critical flag 11 (prose-only structural enforcement / fail-open
  guards / approve-without-computed-checks); flag 6 extended to contract staleness.
  **test**: scenarios 12 (rationalizing reviewer), 13 (fail-open forgery), 14
  (authoring-context/deixis leakage — students must never see the scaffolding
  conversation). **draft**: no softener language; rubrics cite validators, never restate.

## edu_skill_creator.1.5 — 2026-07-09

Lesson L10 promoted from the POSED pilot (the reflect pattern, run live): educational
content is heterogeneous — templates must be content-type-aware.

- **lessons_learned.md L10** (+ quick-reference row, provenance updated to include
  posed_skill.1.24–1.25): any stage drafting/transforming/rendering teaching artifacts
  works from an explicit content-type registry (definition, equation, derivation,
  procedure, worked example, comparison, code, data figure, …), each type with its own
  body grammar, budgets, and reviewer checks. Corollary: precision blocks are atomic
  end-to-end, and the registry must be wired into EVERY downstream transformer — a rule
  that lives only in the drafter dies in the next stage (POSED 1.24 → 1.25 demonstrated
  both halves).
- **edu-skill-creator-intent**: A.1 now also asks what content TYPES the artifacts carry.
- **edu-skill-creator-architecture**: step 1 requires the content-type registry for
  artifact-producing stages, with the precision-block rule wired into all transformers.
- **skill_quality_rubric**: critical flag 10 — one-size template on heterogeneous
  content, or precision content trimmable/paraphrasable anywhere in the pipeline.
- **edu-skill-creator-test**: pressure scenario 11 — seed a cited definition, equation,
  and code block; verify wording/notation intact through every transform stage.
- **edu_grounding_library**: Alley scope limit sharpened — the visual-evidence body
  applies to data/figure content; precision text is its own evidence.
- Fixed three 1.4 rename casualties where the common noun "page" had become
  "edu-skill-creator" ("HITL page", 2× "gate/human page renders").

## edu_skill_creator.1.4 — 2026-07-06

Rename release: PAGE is now **Edu Skill Creator**.

- Renamed the plugin id, umbrella skill, subskill frontmatter names, placeholders,
  README/maintenance docs, release lint prefix, and dev-link script from generic
  `page` / `PAGE` naming to `edu-skill-creator` / `Edu Skill Creator`.
- Updated both manifests to `edu-skill-creator` 1.4.0 and pointed homepage/repository
  metadata at `https://github.com/maxuwp/edu-skill-creator`.
- Future release headings use `edu_skill_creator.X.Y`; older entries below retain the
  old `page_skill.*` tag prefix for historical accuracy.

## page_skill.1.3 — 2026-07-06

Tiny Codex release-evidence cleanup.

- Corrected the page_skill.1.2 review-evidence tally to match the machine-readable
  review logs: 36 findings total, 16 fixed and 20 accepted.
- Added release_lint check 9: every `reviews/*_review.json` finding must carry
  `status: fixed|accepted` plus a non-empty `resolution`, and every review file with
  findings must carry a `resolution_pass` block. The check was falsifiability-tested
  by deleting a finding status in a temp copy and confirming lint failed.

## page_skill.1.2 — 2026-07-06

Release-evidence hygiene (second Codex review round). No workflow changes.

- **Review logs are now mechanical evidence**: every finding in `reviews/*.json`
  carries `status: fixed|accepted` + a one-line `resolution`, and each file a
  `resolution_pass` block naming the release it was resolved against (36 findings:
  16 fixed, 20 accepted). A status-less finding = open; there are none.
- **Uniform skill versioning**: every SKILL.md frontmatter `version` now tracks the
  plugin major.minor and is bumped together on release. New lint check 8 enforces it
  (falsifiability-tested: failed on all 10 stale files before the bump). Per-skill
  history lives in this changelog.
- **`release_lint.py --publish`**: after the publish gate, the "manifests claim a
  hosted repo but no origin exists" case escalates from warning to error
  (falsifiability-tested with origin removed). `edu-skill-creator-release` step 8 and
  MAINTAINING.md now call for publish mode post-publish.
- edu-skill-creator-refresh: Part B (grounding-library judgment) scoped INTO the independent
  review alongside Part C, per the round-3 reviewer's finding; only Part A's pure
  fact-reporting keeps the L3 waiver.

## page_skill.1.1 — 2026-07-06

Codex review round: privacy/security/accessibility hardening + Edu Skill Creator reviewed by its own
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
- **edu-skill-creator-test**: pressure scenarios 7–10 (student-data leakage, undisclosed external
  call, log/redaction failure, gate keyboard/screen-reader operability); fresh-context
  GREEN judges; exit gate spec (`test_gate`).
- **release_lint check 7**: manifests' homepage/repository URLs must match the git
  origin (mismatch = error, missing origin = warning). Falsifiability-tested in both
  directions before landing. Lint also hardened against a missing CHANGELOG.
- **Edu Skill Creator reviewed by Edu Skill Creator's rubric** (durable evidence in `reviews/`): all 10 skills
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

- **Umbrella + 9 stage skills**: `edu-skill-creator` (dispatcher), `edu-skill-creator-intent` (interview +
  contested-choices inventory), `edu-skill-creator-grounding` (framework map before design),
  `edu-skill-creator-architecture` (stages, gates, dependency model, BUILD_PLAN output),
  `edu-skill-creator-scaffold` (dual-harness repo generation), `edu-skill-creator-draft` (skills + rubrics with
  fresh-context review), `edu-skill-creator-test` (RED/GREEN/REFACTOR + education-specific pressure
  suite, consent-gated), `edu-skill-creator-release` (lint, lockstep, semantic-drift grep,
  author-gated publish), `edu-skill-creator-reflect` (post-pilot harvest, approve-per-item),
  `edu-skill-creator-refresh` (~90-day source refresh).
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
