<!-- Detail for L8. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L8 — Plan resumably; verify state before committing; make lints falsifiable

**Rule.** Before any large build, write a checklist document and mark items as they land
(sessions die at token limits; the next session resumes at the first unchecked item).
Never chain "edit then commit" blindly — verify the edit actually landed first (a
mid-script abort once produced a bad partial commit). And test every lint in the failing
direction before trusting it: a lint that can false-pass is worse than no lint (POSED's
changelog check once matched a teaser line instead of a real entry).

**Fold — a fixture must name the guard it proves, and every branch needs one.** "Seed a
violation, watch it fail" is necessary and not sufficient. Two failure shapes both shipped
here and both read as coverage:

- *Passing for the wrong reason.* Two cases seeded a violation of lint check 11 by deleting
  `lesson_index.md` and by dangling a lesson path. Each mutation also orphaned lesson files,
  so check 12 failed the lint and the fixtures went green — with check 11's guard deleted,
  both still passed. A case that asserts only "the lint exited nonzero" proves the lint can
  fail, never that THIS guard fired. Assert the specific error text.
- *Whole-check granularity hides dead branches.* Deleting an entire check was caught; deleting
  one branch inside it was not. Nine fail-closed branches (missing input, empty glob, vacuous
  parse) had no fixture at all. Seed per branch, not per check.
- *No positive control.* Five probes asserted the validator template's refusal paths and none
  asserted it could still pass. A template hardwired to `exit 1` would have satisfied all five.

The same rule governs fixture *sets*: one negative fixture per validator trips whichever check
runs first and leaves the rest unproven forever, so the contract is one negative per CHECK,
each asserting the report names its own check.

**Edu Skill Creator enforcement.** `edu-skill-creator-architecture` emits a BUILD_PLAN checklist as a required
artifact; `edu-skill-creator-release` requires demonstrating each new lint check fails on a seeded
violation before it counts; `tests/run_deterministic.py` makes `expect_tag` a required argument,
so a case that cannot name its guard cannot be written; release lint check 13 enforces a floor on
the case count, so cases cannot be removed rather than fixed.
