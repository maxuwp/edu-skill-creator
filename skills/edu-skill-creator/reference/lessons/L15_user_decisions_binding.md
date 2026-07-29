<!-- Detail for L15. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L15 — Explicit user decisions are authoritative constraints

**Rule.** Preserve the meaning of a user's explicit decision and trace it through every downstream
stage able to alter it. Only a later decision by that same user may waive or supersede it. A
downstream stage's paraphrase, reclassification, or silent omission is not a waiver.

**Failure that taught it.** Faculty instructions vanished across a pipeline: a chosen classroom
anecdote was displaced by reviewer-facing "no universal preference" language, a required line was
dropped at a later stage, and macro-sequence rules were re-broken. A ledger with hash-checked status
fixed the text case; the same failure then recurred one layer down, where a faculty-approved chart
was reclassified as conditional by an agent and omitted — described in the source as a faculty
instruction silently converted into a recommendation. Downstream stages smooth away exactly the
low-frequency, high-value signal a human supplied, because improving prose is what they are for.

**Distinct from L2.** L2 keeps the author's taste out of the user's defaults. This keeps the user's
stated instruction alive through the stages that follow it.

**Enforcement.** `edu-skill-creator-architecture` requires the design to state how user decisions are
traced and which stages can alter them; `skill_quality_rubric` critical flag 14 blocks a design where
a user's explicit decision can be altered or dropped downstream without a later decision from that
user. The mechanism is the architecture's choice: `../implementation_patterns.md` P1 records a
hash-bound ledger and its simpler fallbacks, and the lightest mechanism that provides traceability
for the product type is the right one.
