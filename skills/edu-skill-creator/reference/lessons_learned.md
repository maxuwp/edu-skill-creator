# Lessons Learned — building POSED and p2d

The empirical core of Edu Skill Creator. Every rule below was paid for by a real failure during the
development and piloting of POSED (posed_skill.1.0 → 1.14) and p2d (p2d_skill.1.0 → 1.6).
When Edu Skill Creator supervises a new educational plugin, each lesson is a **design requirement**,
not a suggestion — a stage that violates one must justify the deviation at its gate.

Format per lesson: the rule, the failure that taught it, how Edu Skill Creator enforces it.

---

## L1 — Ground every stage in published frameworks; never invent process

**Rule.** No pipeline stage may invent a process, rubric, or set of criteria where a
citable, established framework exists (instructional design, assessment, presentation
design, software review — whatever the stage's domain is). Each stage carries an explicit
anchor: framework → citation → how it is applied.

**Failure that taught it.** Early POSED stages shipped home-made outline criteria and
review checklists. Pilot review kept re-litigating them ("why these seven dimensions?")
because there was no authority behind them. Once stages were re-anchored (UbD priority
tiers, Mager/ABCD objectives, Mayer multimedia principles, Fagan/IEEE 1028 inspections…),
disagreements became "does this apply the framework correctly?" — answerable.

**Corollary — scope discipline.** Cite a framework only for its original, validated scope.
POSED once over-generalized a protocol validated only for n8n-workflow development into a
universal AI-development framework; the fix was a "Scope and limitations" section. Every
grounding map entry must state what the framework does NOT cover.

**Edu Skill Creator enforcement.** `edu-skill-creator-grounding` runs before any architecture work and produces
`grounding_frameworks.md` for the new plugin; a stage with no anchor is flagged
"invented process — justify or redesign" and blocks the grounding gate.

## L2 — The author's preferences must never become the user's defaults

**Rule.** Any pedagogically contested choice (student AI use, grading philosophy, group
vs. individual work, attendance policy flavor, rigor level…) must be presented to the
educator as an explicit, plainly introduced option set. The plugin author's own stance may
be *offered*, never *assumed*.

**Failure that taught it.** POSED's author is an AI-in-education pioneer, and AI-guided
activities quietly became the default output. His words: "you should not make the ai
assisted design as default… many professors don't like it or even hate students to use AI
assisted work." Fix: a four-option faculty AI stance chosen at intake, with all
AI-flavored design conditional on it, plus a reviewer critical flag "AI stance violated."

**Edu Skill Creator enforcement.** `edu-skill-creator-intent` includes a mandatory "contested choices inventory";
`edu-skill-creator-architecture` requires each inventoried choice to surface as an explicit intake
option with a neutral introduction; reviewer rubrics get a critical flag for violations.

## L3 — Drafter ≠ reviewer, always

**Rule.** Every content-generating step pairs with an independent reviewer that runs in a
fresh context with an **input allowlist** (the artifact + rubric + reference inputs —
never the drafter's reasoning). The review log is written to disk BEFORE the human gate
opens. Scored rubrics: dimensions sum to 100, threshold 85, plus binary critical flags
that block regardless of score.

**Failure that taught it.** Self-review in the same context rationalized the drafter's
errors — cumulative hallucination passed its own checks. In the AI-for-All pilot, a
monolithic self-checked outline sailed through with terminology pile-ups and irrelevant
prerequisites that a cold reader spotted immediately.

**Edu Skill Creator enforcement.** `edu-skill-creator-architecture` requires a drafter/reviewer pairing per
content stage; `edu-skill-creator-draft` authors the rubrics from a standard template (allowlist,
dimensions, threshold, critical flags, output schema, one worked failure example) — and
Edu Skill Creator itself reviews drafted skills with a fresh-context reviewer.

## L4 — Big gates overload the human; split into narrow, dependency-aware steps

**Rule.** A human gate should carry one decision. Decompose large approvals into a wizard
of narrow steps; track dependencies so approving an upstream edit marks downstream
artifacts stale (`valid_from_step`, `stale_due_to`, `needs_regeneration`,
`superseded_by`); block compile/assembly while anything is stale; give every reviewable
item a stable id that is never renumbered.

**Failure that taught it.** POSED's single whole-outline gate produced rubber-stamping
and un-actionable "revise it" feedback. After an upstream edit, downstream artifacts
generated from the superseded version shipped silently. The six-step Stage 3 wizard with
stale-state invalidation fixed both.

**Edu Skill Creator enforcement.** `edu-skill-creator-architecture` produces an explicit dependency model and gate
map for the new plugin; a stage whose gate asks for more than one decision is a review
finding.

## L5 — Structured feedback UI, not free text

**Rule.** Gates collect decisions in structured form: per-item dispositions
(keep/revise/split/remove) with comments keyed to stable ids, section-level feedback
controls, reorder controls — persisted as machine-readable decision JSON that routes each
item back to the step that owns it. And the assistant must never accept/click a gate on
the human's behalf; "prefer defaults" means prefill, never bypass.

**Failure that taught it.** Faculty typed rich feedback into description fields where no
downstream step ever read it. Feedback died in transit.

**Edu Skill Creator enforcement.** `gate_design_patterns.md` specifies the decision-JSON schema and
gate UI patterns (POSED's guided app is the reference implementation);
`edu-skill-creator-architecture` requires every gate to name its decision schema and owning step.

## L6 — Expensive AI runs are consent-gated with a cost ladder

**Rule.** Token-heavy operations (multi-agent simulations, full eval sweeps) are opt-in:
offer full / lite (~1/5 cost, described concretely) / skip, state the cost in plain
language, record the chosen mode in the manifest, re-offer on every re-run. Exception:
when no human will ever rehearse the output (e.g. self-study decks), the simulation is
the only rehearsal — auto-invoke and say why.

**Failure that taught it.** The two-role (professor/student) dry-run simulation was
valuable but "very token consuming" — the author asked that it never run without asking.

**Edu Skill Creator enforcement.** `edu-skill-creator-test`'s eval sweeps and any simulation stage designed into a
new plugin must carry the full/lite/skip consent gate with a recorded mode field.

## L7 — One source of truth; automate drift detection

**Rule.** One repo per plugin serving all harnesses: both plugin manifests version-locked,
shared tool-agnostic SKILL bodies (neutral `<x-skill-dir>/…` placeholders; harness
specifics only in a scoped, whitelisted reference file), personal skill dirs symlinked
into the repo, and a `release_lint.py` run before every push. Lint the drift classes that
actually bit: hardcoded harness paths, manifest version mismatch, deprecated repo URLs,
rubric sums ≠ 100, missing changelog heading, dangling reference citations.

**Failure that taught it.** Four repos (claude/codex × posed/p2d) drifted immediately.
Even after merging, a shared variable containing a literal home-directory harness path
leaked into 17 files — caught by the other harness, then made lintable.

**Corollary — one canonical implementation INSIDE the plugin too.** A formula, constant,
threshold, or key vocabulary that appears in two places will diverge: POSED shipped three
different pacing formulas (drafter script, drafter prose, reviewer inline) and two key
vocabularies for the same corpus-recommendation concept. Rule: one canonical
implementation (a script or a named reference section); every other mention CITES it,
never restates the value; near-miss keys hard-fail with "did you mean" rather than being
silently ignored (posed_skill.1.27/1.30 F7).

**Edu Skill Creator enforcement.** `edu-skill-creator-scaffold` generates this layout from day one, including the
parameterized lint; `dual_harness_playbook.md` is the specification.

## L8 — Plan resumably; verify state before committing; make lints falsifiable

**Rule.** Before any large build, write a checklist document and mark items as they land
(sessions die at token limits; the next session resumes at the first unchecked item).
Never chain "edit then commit" blindly — verify the edit actually landed first (a
mid-script abort once produced a bad partial commit). And test every lint in the failing
direction before trusting it: a lint that can false-pass is worse than no lint (POSED's
changelog check once matched a teaser line instead of a real entry).

**Edu Skill Creator enforcement.** `edu-skill-creator-architecture` emits a BUILD_PLAN checklist as a required
artifact; `edu-skill-creator-release` requires demonstrating each new lint check fails on a seeded
violation before it counts.

## L9 — Knowledge snapshots go stale; build the refresh loop in

**Rule.** A plugin that encodes frameworks, tool capabilities, or model behavior needs a
periodic (~90-day) refresh skill: check for new frameworks and new AI capabilities,
present findings as an approve-per-item ledger, never auto-apply. Likewise, after every
pilot, a reflect skill harvests what the gates revealed into persistent improvements.

**Failure that taught it.** New AI capabilities (e.g. interactive simulation) enabled
lecture designs — personalized FFT/IFFT visualizations — that the frozen skill text could
never propose; and pilot lessons kept accumulating in chat transcripts instead of the
plugin.

**Edu Skill Creator enforcement.** `edu-skill-creator-architecture` includes refresh + reflect stages in every
educational plugin's design by default (the educator can decline — see L2); Edu Skill Creator itself
ships `edu-skill-creator-refresh` and `edu-skill-creator-reflect`.

## L10 — Educational content is heterogeneous; templates must be content-type-aware

**Rule.** Any stage that drafts, transforms, or renders teaching artifacts must work from
an explicit registry of content types (archetypes) — definition, equation, derivation,
procedure, worked example, comparison, code, data figure, … — each with its own body
grammar, budgets, and reviewer checks. One template ("assertion title + short bullets,
prefer a visual") must never be imposed on all content: a definition's exact wording, an
equation, a numbered procedure, or a code block IS the evidence — often more useful than
any figure — and cannot be compressed into fragment bullets.

**Corollary — precision blocks are atomic end-to-end.** Definitions, theorems, equations,
code, verbatim problem statements, and quoted standard text are precision blocks: never
trimmed, paraphrased, "humanized," or reflowed to fit, by ANY stage — overflow ladders
operate on the material around the block, then split or paginate. And the registry must
be wired into EVERY downstream transformer (humanizer, compiler, notes drafter, final
review): a rule that lives only in the drafter dies in the next stage.

**Failure that taught it.** POSED through 1.24 carried a one-grammar-fits-all slide
template. From pilot use: "concepts put in the slide themselves can't be shortened or
simplified… many academic slides contain definitions, processes, equations — necessary
and more useful than a visual, sometimes." Definitions were being trimmed to bullet
budgets and offered figures they didn't need. The first fix (a 12-archetype registry,
posed_skill.1.24) then demonstrated the corollary: it shipped with the humanizer, notes
drafter, and outline planner unaware of it — closed in posed_skill.1.25.

**Edu Skill Creator enforcement.** `edu-skill-creator-intent` asks what content types the
artifacts carry; `edu-skill-creator-architecture` requires a content-type registry for
artifact-producing stages; rubric critical flag 10 blocks one-size templates and
trimmable precision content; `edu-skill-creator-test` pressure scenario 11 seeds
precision blocks and checks their fidelity through the full pipeline.

## L11 — Prose contracts rot; structural requirements need computed, fail-closed validators

**Rule.** Any requirement that code can check, code MUST check. For each artifact,
identify the structural requirements (required rows/fields/tags, coverage against an
upstream contract, count/pacing bands, forbidden markers) and write a computed validator:
**one implementation, two callers** — the drafter runs it pre-gate as a self-check, and
the reviewer re-runs the SAME script as a hard gate. A reviewer's `approve` is illegal
unless the recorded computed checks passed; the orchestrator refuses to open the human
gate on a review log missing them.

**Failure that taught it.** POSED's pilot deck passed FOUR fresh-context review rounds at
94/100 while carrying 13 structural criticals (unmaterialized activities, missing
takeaway, missing subgoal labels); the approved outline scored 97/100 with 5 more. The
reviews weren't lazy — the requirements were prose, and language models score prose
charitably. Computed validators (posed_skill.1.27–1.30) failed both artifacts instantly.
L3's fresh-context reviewer catches *judgment* defects; it does not establish
*structural* facts. Both layers, always.

**Corollaries, each also paid for:**
- **Fail closed.** A missing record, absent artifact, unknown contract version, or
  zero-widget gate page is a refusal, not a skip: POSED's publisher shipped untracked
  files because a missing manifest record was treated as publishable, and its completion
  check trusted a forgeable `exists:true` (posed_skill.1.30.1 — six such holes).
- **Prove by attack, not only by fixture.** Fixture-driven proofs exercise only the paths
  fixtures cover; an adversarial reviewer forging records/bypassing steps found every
  fail-open hole the green fixtures never touched (defense-in-depth; NIST SSDF spirit).
- **Falsifiability against REAL artifacts.** Each validator is proven failing on the
  actual defective pilot artifact AND passing on a synthetic fixture; fixtures ship in
  the repo (release lint runs the pairs) and NEVER contain student/faculty course
  content (the data posture applies to test data too).
- **Aggregates need distribution checks.** Notes passed a 98% word-count band with one
  sentence repeated 54× and an identical cue block on 39/39 slides — repetition defeats
  totals; check uniqueness/variance, not just sums.
- **Anti-softener rubric language.** Rubric phrasing that permits rationalization
  ("present *or clearly represented*") is a named defect — the exact phrase let 2 of 3
  missing activities pass.
- **Mechanical never-accept-on-behalf (upgrades L5).** Gate decisions are stamped
  server-side (`submitted_via`, content-derived `decision_id`); a hand-written decision
  file is the named anti-pattern — the pilot had a gate "accepted by agent action," and
  no prose rule caught it until the stamp check existed.

## L12 — Live sessions outlive releases: version the contract, route upgrades to targeted amendments

**Rule.** A plugin's artifact schemas WILL change while faculty sessions are in flight.
Every artifact carries `generated_by` (drafter + skill version) and the session carries a
server-owned `session_contract_version`; validators distinguish **contract upgrades**
(old artifact, new rules) from **quality gaps** (bad artifact); a schema change marks
in-flight artifacts contract-stale and routes faculty to a TARGETED amendment of the
owning step, seeded with proposed fixes — never a full regeneration, never a downstream
stage patching around a doomed upstream artifact. Unknown or missing contract versions
fail closed (treated as current-era, checks armed).

**Failure that taught it.** A live POSED session carried contract version "1.13", which
disarmed every ≥1.29 enforcement check at once; drafters were re-running against
approved-but-now-invalid outlines; reflect couldn't tell upgrade findings from quality
findings (posed_skill.1.28–1.30, F10). L4's stale-state model covers *content* edits;
this covers *schema* evolution — a different axis that bites exactly when the plugin
improves fastest.

**Edu Skill Creator enforcement (L11 + L12).** `edu-skill-creator-architecture` items 5
and 11 require the contract-version fields and a computed-validation plan;
`skill_quality_rubric` critical flag 11 blocks prose-only structural enforcement and
fail-open guards; `edu-skill-creator-test` scenarios 12–14 attack exactly these surfaces.

---

## Quick-reference table

| # | Rule | Enforced at |
|---|---|---|
| L1 | Ground in published frameworks, original scope only | edu-skill-creator-grounding gate |
| L2 | Contested choices are explicit options, never defaults | edu-skill-creator-intent inventory; rubric critical flag |
| L3 | Independent fresh-context reviewer per content stage | edu-skill-creator-architecture; edu-skill-creator-draft rubrics |
| L4 | Narrow gates + dependency/stale-state model | edu-skill-creator-architecture |
| L5 | Structured decision JSON; never accept on the human's behalf | gate_design_patterns.md |
| L6 | Cost-consent ladder for expensive runs | edu-skill-creator-test; simulation stage designs |
| L7 | Single source + symlinks + release lint | edu-skill-creator-scaffold |
| L8 | Resumable checklists; verify-then-commit; falsifiable lints | edu-skill-creator-architecture; edu-skill-creator-release |
| L9 | Refresh + reflect loops | edu-skill-creator-architecture defaults |
| L10 | Content-type-aware templates; precision blocks atomic end-to-end | edu-skill-creator-architecture registry; rubric critical flag 10; edu-skill-creator-test scenario 11 |
| L11 | Computed fail-closed validators; one implementation, two callers; approve illegal without them | edu-skill-creator-architecture item 11; rubric critical flag 11; edu-skill-creator-test scenarios 12–13 |
| L12 | Contract versioning + targeted amendment re-entry for live sessions | edu-skill-creator-architecture item 5; edu-skill-creator-test scenario 13 |

*Provenance: POSED CHANGELOG entries posed_skill.1.4–1.14 (L1–L9), posed_skill.1.24–1.25
(L10), posed_skill.1.26–1.30.1 (L11–L12 and the L7 corollary), and p2d_skill.1.4–1.6
record the concrete releases behind each lesson.*
