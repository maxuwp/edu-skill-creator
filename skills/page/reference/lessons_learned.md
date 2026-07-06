# Lessons Learned — building POSED and p2d

The empirical core of PAGE. Every rule below was paid for by a real failure during the
development and piloting of POSED (posed_skill.1.0 → 1.14) and p2d (p2d_skill.1.0 → 1.6).
When PAGE supervises a new educational plugin, each lesson is a **design requirement**,
not a suggestion — a stage that violates one must justify the deviation at its gate.

Format per lesson: the rule, the failure that taught it, how PAGE enforces it.

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

**PAGE enforcement.** `page-grounding` runs before any architecture work and produces
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

**PAGE enforcement.** `page-intent` includes a mandatory "contested choices inventory";
`page-architecture` requires each inventoried choice to surface as an explicit intake
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

**PAGE enforcement.** `page-architecture` requires a drafter/reviewer pairing per
content stage; `page-draft` authors the rubrics from a standard template (allowlist,
dimensions, threshold, critical flags, output schema, one worked failure example) — and
PAGE itself reviews drafted skills with a fresh-context reviewer.

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

**PAGE enforcement.** `page-architecture` produces an explicit dependency model and gate
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

**PAGE enforcement.** `gate_design_patterns.md` specifies the decision-JSON schema and
gate UI patterns (POSED's guided app is the reference implementation);
`page-architecture` requires every gate to name its decision schema and owning step.

## L6 — Expensive AI runs are consent-gated with a cost ladder

**Rule.** Token-heavy operations (multi-agent simulations, full eval sweeps) are opt-in:
offer full / lite (~1/5 cost, described concretely) / skip, state the cost in plain
language, record the chosen mode in the manifest, re-offer on every re-run. Exception:
when no human will ever rehearse the output (e.g. self-study decks), the simulation is
the only rehearsal — auto-invoke and say why.

**Failure that taught it.** The two-role (professor/student) dry-run simulation was
valuable but "very token consuming" — the author asked that it never run without asking.

**PAGE enforcement.** `page-test`'s eval sweeps and any simulation stage designed into a
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

**PAGE enforcement.** `page-scaffold` generates this layout from day one, including the
parameterized lint; `dual_harness_playbook.md` is the specification.

## L8 — Plan resumably; verify state before committing; make lints falsifiable

**Rule.** Before any large build, write a checklist document and mark items as they land
(sessions die at token limits; the next session resumes at the first unchecked item).
Never chain "edit then commit" blindly — verify the edit actually landed first (a
mid-script abort once produced a bad partial commit). And test every lint in the failing
direction before trusting it: a lint that can false-pass is worse than no lint (POSED's
changelog check once matched a teaser line instead of a real entry).

**PAGE enforcement.** `page-architecture` emits a BUILD_PLAN checklist as a required
artifact; `page-release` requires demonstrating each new lint check fails on a seeded
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

**PAGE enforcement.** `page-architecture` includes refresh + reflect stages in every
educational plugin's design by default (the educator can decline — see L2); PAGE itself
ships `page-refresh` and `page-reflect`.

---

## Quick-reference table

| # | Rule | Enforced at |
|---|---|---|
| L1 | Ground in published frameworks, original scope only | page-grounding gate |
| L2 | Contested choices are explicit options, never defaults | page-intent inventory; rubric critical flag |
| L3 | Independent fresh-context reviewer per content stage | page-architecture; page-draft rubrics |
| L4 | Narrow gates + dependency/stale-state model | page-architecture |
| L5 | Structured decision JSON; never accept on the human's behalf | gate_design_patterns.md |
| L6 | Cost-consent ladder for expensive runs | page-test; simulation stage designs |
| L7 | Single source + symlinks + release lint | page-scaffold |
| L8 | Resumable checklists; verify-then-commit; falsifiable lints | page-architecture; page-release |
| L9 | Refresh + reflect loops | page-architecture defaults |

*Provenance: POSED CHANGELOG entries posed_skill.1.4–1.14 and p2d_skill.1.4–1.6 record
the concrete releases behind each lesson.*
