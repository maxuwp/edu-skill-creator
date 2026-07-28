<!-- Detail for L8. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

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
