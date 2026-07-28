<!-- Detail for L5. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

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
