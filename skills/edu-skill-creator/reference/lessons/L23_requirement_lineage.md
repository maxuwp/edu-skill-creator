<!-- Detail for L23. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L23 — Preserve the need, reconsider the means: a requirement can be a workaround for a limitation that no longer exists

**Rule.** Preserve confirmed needs and preferences. Reconsider solutions and compromises. **Hold
ambiguous requirements without either deleting or enforcing them** until the person who asked has
answered. Two axes are recorded per requirement and never conflated — what it *is*
(`need | outcome | preference | constraint | solution | workaround | assumption`) and what happens to
it in a migration (`preserve | adapt | retire_workaround | invalidate | hold_pending_clarification`).
The full record, with its provenance fields and the question format, is defined once in
`docs/DESIGN_clarify_execute_rebase_2026-08-01.md`.

**The failure this prevents, in the author's own example.** A house has small windows, so the design
carries "many lighting fixtures." The site changes to one with good daylight. Every migration rule
written before this lesson says a recorded requirement is protected by default — so the fixtures ride
across, and the new house has a large window *and* twelve lamps. The requirement was never a
requirement. It was a **compensating workaround** for a limitation that the new foundation removed,
and carrying it forward imports the old foundation's defect into the new one.

Now the same sentence with a different reason behind it: the fixtures are wanted for their decorative
character, daylight or no daylight. Here the correct migration is the opposite — preserve the
fixtures and *adapt the structure* to support and power them.

**The two cases are indistinguishable in the artifact.** Identical text, identical requirement
record, opposite correct actions. No amount of reading the design, the code, or the prior review logs
separates them. Only the person who asked knows, which is why this cannot be solved by better
analysis and must be solved by asking.

**Where the asking belongs.** Two places, for different reasons. At intake, because the cheapest time
to catch an ambiguity is before anything is built on it. And in **every substantive review round**,
because by then the artifact is concrete enough to expose needs that neither the author nor the
faculty member could articulate at the start — which is the genuinely useful thing a review round
does besides finding defects.

**How to ask.** Counterfactual, and one question at a time: *if the limitation that produced this
were gone, would you still want it?* Write each question with the decision each answer settles; if
neither answer changes a decision, the question is not load-bearing and is not asked. One to three
per interaction as a default, and if more load-bearing ambiguities remain, schedule another
clarification gate rather than guessing the rest.

**Unknown does not mean active.** The first version of this rule said to carry an ambiguous
requirement forward and flag it. That is not sufficient: a requirement carried forward *as active*
still gets built, so the twelve-lamp house survives the flag. `hold_pending_clarification` keeps the
item in the lineage while committing the design to nothing. Where work must continue before the
answer arrives, take the most reversible option — provide for the possibility structurally, defer the
commitment — and record that the reversibility was chosen deliberately.

**An inference must never become a confirmation.** Every lineage entry carries a status of
`inferred`, `observed`, `user_confirmed` or `derived`, and a `user_confirmed` status points at the
interaction or stamped decision that established it. Without that field, an agent's own guess about
what the faculty member wanted is read three rounds later as the faculty member's stated requirement.
That is the circular-evidence failure reserved as L21, appearing in the requirements layer rather than
the evidence layer.

**Two kinds of progress, and the second is not a failure.** A round can close no defects, open a
question, and be the most valuable round in the loop, because uncertainty about what is actually
wanted went down. Record it as such: artifact convergence and requirements resolution are separate
axes, and L20's definition of convergence is deliberately **not** widened to absorb the second — that
would let a descending loop relabel itself as discovery.

**Applies to.** `edu-skill-creator-intent` (the intake assumption audit produces the first lineage
records), `edu-skill-creator-grounding` and `edu-skill-creator-architecture` (a stage requirement
that is really a workaround for a tooling limitation should be recorded as one),
`edu-skill-creator-draft` (review briefs carry the question format and the `CLARIFICATION_REQUIRED`
outcome), `edu-skill-creator-reflect` (harvest confirms needs, and retires workarounds whose
limitation has gone).

**Related.** L22 governs when the foundation may change; this lesson governs what crosses with it.
L20 names the pathology and supplies the metric this lesson adds an axis beside. L19's protected
baseline is what makes "preserve" meaningful. L2's contested-choices inventory is the same instinct
applied at intake: never let a default stand in for a decision the faculty member should make.

**Status of enforcement.** Prose only, as of 2026-08-01. No schema carries `semantic_role`, no
reviewer output is checked for `CLARIFICATION_REQUIRED`, and the acceptance test — same artifact
text, different human answer, different migration decision, and only after asking — has no runner.
Treat an unwired rule as unenforced (L13).
