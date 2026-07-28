<!-- Detail for L10. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

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
