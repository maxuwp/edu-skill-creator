<!-- Detail for L4. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

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

**Corollary added 1.11 (row f24) — never derive identity from position.** The stable-id rule extends:
identity is bound through an explicit key captured at creation and verified against the actual output,
never inferred from array index or file order. A tree builder that enumerated records positionally
renumbered a pilot's decisions and mislabelled a release; the fix was an owner-assigned id. Anything
that reorders or regroups the underlying list silently relabels content otherwise.

*Enforcement status: the positional-identity corollary is guidance only — no rubric flag, test scenario or computed check covers it yet. Recorded rather than implied (L13); a future release adds the mechanism or withdraws the corollary.*
