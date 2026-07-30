# Changelog — Edu Skill Creator

All releases bump both plugin manifests in lockstep. Entry headings follow
`## edu_skill_creator.X.Y — <date>` (the release lint requires the heading, not a mention).

## edu_skill_creator.1.14 — 2026-07-30

Audited this repo against the failure patterns from the sibling POSED project's live test run
(`FINDINGS_posed_multi_model_review_2026-07-29`, `SELFTEST_posed_session_audit_2026-07-29`). Twelve
generalizable patterns were extracted; four were present here.

- **Reference not landing** (their A7). `skills/architecture/SKILL.md` cited
  `reference/validator_template.py`, which does not resolve from that skill — the file is under
  `scaffold/`. A cold agent following that pointer fails. Corrected to the placeholder-qualified path.
  Nine other candidate paths were checked and are outputs a *generated* plugin creates, not defects.
- **Post-approval drift was undetectable** (their A1, the most serious finding in their audit: three
  approved artifacts were edited afterwards and nothing noticed for sixteen days). Our gate decision
  named its artifact by the version *string* `"reflect_ledger.json rev 3.1"` with no hash, so the
  ledger could change under an approval and nothing would ask. Now hash-bound, with **check 14**
  asking on every push rather than waiting to be asked — which is the fix their audit recommends and
  does not yet have.
- **A gate that authenticates a signal, not the record it signs** (their most cross-confirmed
  finding: a review recording `total 81`, `threshold 85`, `passed false` and `recommendation approve`
  simultaneously). Nothing here cross-checked a recommendation against its own evidence. All twelve
  of our reviews are in fact coherent — the hole was latent, not fired. **Check 15** now blocks any
  review recommending approval while carrying critical flags, blocking findings, a sub-threshold
  score, or `passed:false`.
- **Vacuous green** (their pattern: a zero-finding run may mean the check never engaged). Six of
  thirteen lint checks had no failing fixture — 4, 6, 7, 8, 13, 14 — so their clean results carried
  no information. Fixtures added for all; check 6 asserts its warning text since it is warning-only,
  and check 13 runs the suite so it cannot seed itself and is recorded as externally proven in 1.13
  rather than silently skipped. Suite is now 25 checks. The c7 fixture initially passed for the wrong
  reason (the temp copy has no git remote, so the check took its no-origin branch); it now creates a
  real origin and mismatches against it.

Also noted, not yet acted on: 26 ledger fields no script reads (their pattern 9, a self-assessment
with no consumer), and derived counts propagating by citation rather than recomputation (their
pattern 3). Both are recorded for the next harvest rather than half-fixed.

## edu_skill_creator.1.13 — 2026-07-28

Ledger row `f14`: the one-off testers become a suite. The plugin prescribed fixture pairs and TDD for
every plugin it generates and had no tests of its own.

- **`tests/run_deterministic.py`** — 18 checks, seconds, no model calls. Every case corresponds to a
  defect that actually shipped: nine seeded lint violations (including the three fail-open holes fixed
  in 1.12 — dead `DEPRECATED` tuple, silent skip on a deleted index, `findings: []` bypass), five
  validator-template probes covering its three former crash paths, and three reachability checks that
  would have caught 1.10's broken reviewer allowlist. Runs on a throwaway copy; never touches the tree.
- **`tests/evals/E1`, `E2`** — the two behavioural prompts that cannot be scripted: cold-start
  execution, and the semantic enforcement audit that caught a false "implemented as check 11" claim
  two review rounds had passed. Reported separately from deterministic results, never overwriting them.
- **Lint check 13** runs the deterministic suite before every push, so a guard that stops firing is
  caught at release rather than discovered by a tester months later. Proven by disabling the check-3
  guard and watching check 13 fail. `--skip-suite` breaks the recursion when the suite calls the lint.

The suite is not proof of correctness. It is proof that specific known failures stay fixed.

## edu_skill_creator.1.12 — 2026-07-28

**Everything here was found by testing the shipped code, not by review.** Three independent agents
were pointed at 0c09837: one executed the skills cold on a real request, one audited every
enforcement claim against its cited target, one ran the scripts. All three found defects that three
prior review rounds and a passing lint had missed.

### The serious one: 1.10 broke the fresh-context reviewer

`lessons_learned.md` became an 18-line pointer stub in 1.10, but **fifteen citations across nine
files still treated it as the substantive ledger** — including `skill_quality_rubric.md` and
`draft/SKILL.md`, which define the independent reviewer's **input allowlist**. `lesson_index.md` and
`reference/lessons/` were not on that allowlist. A Stage 5 reviewer following the documented inputs
exactly would open an empty file and be unable to interpret the numbered critical flags it exists to
enforce. The plugin's central quality gate, operating rule 3, was wired to nothing for two releases.
All fifteen citations swept; Stage 8's write side now targets a new `lessons/` file plus its index row.

### A false enforcement claim that survived two review rounds

L7's fold stated registry completeness was "implemented as release_lint check 11." Check 11 resolves
numbered enforcement claims; **no registry-completeness check existed anywhere.** The claim originated
in ledger row `f21` and passed both independent reviews, because reviewers verified that cited numbers
resolve rather than that claimed implementations exist. New **check 12** now does what was claimed
(every `lessons/` file is referenced by the index), and the lesson records how the false claim survived.

### Three fail-open holes in the lint that polices fail-open holes

- **Check 3 was dead code.** `DEPRECATED = ()` — an empty tuple no content could ever trigger. The
  repo does have a deprecated URL (the pre-rename `maxuwp/page`); populated, and it now fires.
- **Check 11 silently skipped** when `lesson_index.md` was deleted: `if LL.exists()` bypassed its own
  fail-closed guard, so deleting the entire enforcement ledger produced exit 0. Now an error.
- **Check 9 was bypassable** via `findings: []`, which skipped the `resolution_pass` requirement
  entirely. Now required unconditionally.
Each fixed check was seeded with a violation and observed firing; all four proofs recorded.

### The validator template violated its own doctrine

Three uncaught crashes outside the CHECKS loop, each breaking the documented exit-2 contract: a
manifest that is valid JSON but not an object, an unwritable report directory, and `--report` given
with no path. All now exit 2 with a stated reason. And `stamped()` used truthiness where the template's
own lesson says gate flags are validated by type — fixed, plus the `require_bool` helper that lesson
demanded and the template never had.

### Honest enforcement accounting

Eight of the nine 1.11 folds shipped as prose with no mechanical check — the failure L11 and L13 name,
committed in the release that refined L11 and L13. Rather than imply coverage, each now carries an
explicit *Enforcement status* line stating it is guidance only, so a future release adds the mechanism
or withdraws the corollary. Also fixed: L12's detail file cited `architecture item 11` (now Lifecycle
stages) and `scenarios 12–14` (14 is unrelated); `implementation_patterns.md` declared everything in it
an example while P3's mechanism stayed a live mandate in two files; the umbrella claimed "nine lessons"
in one place and "thirteen" in another against an actual eighteen; rubric flags ran 1–10, 13, 14, 11, 12;
and the umbrella never explained that `edu-skill-creator-<stage>` lives at `skills/<stage>/`.

## edu_skill_creator.1.11 — 2026-07-28

The doctrine release. Gate rows f2–f7, f9(partial), f19–f22, f24–f27, f31 as decided in
`reflect_gate_decision.json`. Ledger goes from thirteen lessons to eighteen.

- **Five new lessons.** **L14** check at the layer the claim is about (five observed instances;
  a correctly grounded oral rubric passed a script that was not speech, because neither anchor
  reached the lexico-grammatical layer). **L15** explicit user decisions are authoritative
  constraints. **L16** evidence burden scales with specificity, consequence and volatility, and no
  precision claim is laundered through a category tag. **L17** when the subject taught is a process,
  its structure is content. **L18** make the compliant path cheaper than the workaround.
- **L18 was the conditional row (f4)** and its grounding investigation resolved positively:
  Beautement, Sasse & Wonham (2008) *The Compliance Budget* (NSPW), with Saltzer & Schroeder's
  psychological acceptability. The scope limit is stated in the lesson per L1's corollary — both are
  validated for human users, and the extension to agent behaviour is analogical, carried by the
  observed incidents rather than by the frameworks.
- **Nine folds** into L1 (corpus provenance), L4 (never derive identity from position), L6 (a silent
  substitution is an unconsented change), L7 (registry completeness), L9 (world-dependent examples
  decay), L10 (anti-tell rules checked against the genre; declared language of instruction) and L11
  (verification reports are self-interested; operational criteria; motivating artifact in the
  acceptance suite; independent threshold re-derivation; measure your own exemplars; detectors need
  a domain model of legitimate variation).
- **`reference/implementation_patterns.md` created (f31)**, in this same release, carrying the four
  mechanisms the lessons no longer mandate — hash-bound decision ledger, locked process graph,
  server-stamped decisions, rendered-surface probes — each with the capability it satisfies, the
  product type it suits, portability, a simpler fallback, and where it was actually run. Shipping it
  later would have made the relocation a deletion.
- **Enforcement added, not merely claimed**: rubric critical flags 13–14, grounding step 2 (the
  layer question), architecture item 6, intent item 8, test scenarios 16–17.
- **Two defects caught in this build.** Inserting numbered items duplicated `3.` in grounding and
  `7.` in architecture, and shifted the computed-validation plan from item 11 to 12, silently
  invalidating L11's enforcement claim. Renumbered, claim corrected. Lint check 11 also silently
  ignored `grounding step`/`intent item`/`draft step` claims because those patterns were not in its
  target table; extended and proven with a seeded `grounding step 99`.
- The L14–L23 proposal document is marked SUPERSEDED with an explicit mapping, since its numbering
  does not match the shipped lessons (L13: mark historical, never leave a superseded instruction live).

## edu_skill_creator.1.10 — 2026-07-28

Gate row `f1` only: the lessons ledger becomes an always-read card plus detail files. No doctrine
changes; the approved lessons and folds land in 1.11.

- **The defect.** `skills/draft/SKILL.md` tells authors that depth belongs in references "loaded on
  demand", while the umbrella ordered `lessons_learned.md` read "before doing anything". That file
  was 346 lines and 3,297 words with its index at line 325, so an agent reading top-down consumed
  the whole evidence corpus before reaching the summary.
- **The split.** `reference/lesson_index.md` is now the always-read card: 25 lines, one row per
  lesson, carrying the single authoritative applicability map. Each lesson's full entry moved to
  `reference/lessons/L01…L13_*.md`, pulled when a stage appears in its Applies-to column.
  `lessons_learned.md` remains as a pointer only. Stage skills cite lesson ids; they do not restate
  the rules, because a second map would drift from the first (L7).
- **Lint check 11 hardened.** It previously parsed the quick-reference table inside
  `lessons_learned.md`. After the split it found no table and passed vacuously — a check that
  silently checks nothing. It now reads the card, **fails closed when it parses zero rows**, and
  additionally verifies that every lesson id resolves to an existing detail file (the dangling-id
  requirement in `f1`). Proven both directions: a seeded `L01_MISSING.md` path fails, restore passes.
- Decided at the gate recorded in `reflect_gate_decision.json` (28 rows, 8 grouped calls).

## edu_skill_creator.1.9 — 2026-07-28

L13 applied to L13: the lesson that forbids promising enforcement the code refuses had
shipped promising two enforcement points that did not exist.

- **The defect.** L13's "Enforced at" column claimed `edu-skill-creator-release sweep`
  and `edu-skill-creator-test scenario 15`. The release skill carried only the older,
  narrower "semantic-drift grep" (scoped to rules changed *this* release, no count
  requirement), and the test suite ended at scenario 14. Only `rubric critical flag 12`
  was real. L13 was also the sole lesson with no enforcement paragraph (L11's is
  deliberately shared with L12).
- **Swept the class, reporting the count** (L13's own rule): all 13 rows audited, 29
  resolvable claims checked, **1 unresolved** — plus one claim ("release sweep") that
  proved *unverifiable as written*, because a bare skill name plus a noun cannot be
  checked. Claims now cite numbered units for exactly that reason.
- **`release_lint` check 11** resolves every numbered enforcement claim in the ledger's
  quick-reference table against the numbered items actually present in the rubric, test,
  architecture and release skills. Falsifiability came free and in the honest direction:
  the check FAILED on the real shipped defect before any fix, and a seeded `architecture
  item 99` fails on restore. This makes the ledger's enforcement column computed rather
  than asserted, which is L11 applied to L13.
- **The enforcement now exists.** `edu-skill-creator-release` step 2 is rewritten as the
  **class sweep**: two triggers (rules changed this release; any review finding citing a
  file:line), one pass, report the count rather than "fixed as suggested", delete or
  move superseded instructions rather than annotate them, table cells whose value is the
  instruction named explicitly, and the wrong-layer signal when a second round finds
  another instance. `edu-skill-creator-test` scenario 15 plants one instruction in four
  surfaces and cites one, with the table-cell variant. `edu-skill-creator-draft` step 3
  carries the same rule at the layer where review findings are actually handled.
- L13 gains its enforcement paragraph.

No stage, gate, schema or product-behaviour changes.

## edu_skill_creator.1.8 — 2026-07-27

L13 — the authoring half of L11: once a skill ships both prose and enforcement, the prose
can teach what the code refuses.

- New `lessons_learned.md` L13, harvested from posed_skill.1.64–1.66. The evidence is
  POSED's six-round 1.66 review: `hitl_protocol.md` listed `approved: true` as the manifest
  effect of a terminal approval that `approval_provenance.py` refuses in every contract era,
  and the same instruction had four more homes (orchestrator step 4, the README, the
  harness-adaptation note, and the outline skill's "Upload an override" path, which saved
  pasted content *as the approved outline*). Each round fixed the cited line and found the
  next home. The rule: sweep the class in one pass and report the count.
- **Annotation is not repair.** The four-option table survived a round with an explicit
  non-approval warning above it. A Manifest-effect column reading `approved: true` is an
  instruction; prose above it is commentary. Superseded procedure is deleted or moved to a
  marked historical section — Anthropic's "old patterns" rule applied to procedure, not
  only to time-sensitive facts.
- Corollaries also recorded: when each round finds a new instance the fix is at the wrong
  layer (the 1.64 CSP precedent); a contradiction inside one instruction set is one defect
  with two locations, so deferring half is a scheduled regression; measure the region, not
  the file; a dispute between two competent reviewers usually indicts your own rule rather
  than either reviewer.
- `skill_quality_rubric.md` gains **critical flag 12** so L13 blocks rather than advises.
- Quick-reference table and the umbrella's stale "nine lessons" pointer updated (thirteen).

No stage, gate, schema or validator behaviour changes: this release adds a lesson, a
critical flag, and their citations.

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
