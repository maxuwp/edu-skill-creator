# Lessons Learned — building POSED and p2d

The empirical core of Edu Skill Creator. Every rule below was paid for by a real failure during the
development and piloting of POSED (posed_skill.1.0 → 1.14) and p2d (p2d_skill.1.0 → 1.6).
When Edu Skill Creator supervises a new educational plugin, each lesson is a **design requirement**,
not a suggestion — a stage that violates one must justify the deviation at its gate.

Format per lesson: the rule, the failure that taught it, how Edu Skill Creator enforces it.

---

## Where the lessons live

This file is no longer the ledger. The always-read card is [`lesson_index.md`](lesson_index.md); each
lesson's full entry and evidence is in [`lessons/`](lessons/), pulled when a stage needs it. Splitting them
was gate row `f1`: a 346-line file ordered read "before doing anything" contradicted this plugin's own rule
that depth belongs in references loaded on demand.
