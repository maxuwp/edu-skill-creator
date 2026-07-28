<!-- Detail for L3. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

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
