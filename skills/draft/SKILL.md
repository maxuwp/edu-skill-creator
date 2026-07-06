---
name: page-draft
description: PAGE Stage 5 — Draft the new educational plugin's skills and rubrics, each independently reviewed. Writes SKILL.md bodies per the approved architecture using skill-creator writing doctrine (progressive disclosure, under 500 lines, explain-why), authors the reviewer rubrics, and routes every draft through a fresh-context review against the skill quality rubric. Triggers - when the page umbrella dispatches Stage 5, or the user says "draft the skills" for a plugin under construction.
version: "1.3"
---

# PAGE Stage 5: Draft

Fills the scaffold's stubs with real skills, in the dependency order from the new
plugin's `docs/BUILD_PLAN.md`: reference files → rubrics → sub-skill SKILL.md bodies →
umbrella body. Every draft gets an independent review before the author sees it (L3 —
applied to ourselves).

**Inputs (exact):** the approved `architecture.md` (each skill's spec is its stage-map
row + gate spec), the new plugin's `skills/<x>/reference/grounding_frameworks.md`, and
its `docs/BUILD_PLAN.md`. **Refuses to run** if any is missing, unapproved, or stale.

**Stale-state rule for this stage's own artifacts (L4).** If `architecture.md` or the
grounding map is revised mid-stage, every skill drafted from the old version is marked
stale in BUILD_PLAN and re-drafted or re-reviewed against the new spec. Likewise
*within* the stage: revising a rubric invalidates every review that was performed with
that rubric — the affected skills go back through step 2. Reference files change →
skills citing them get a re-review, not a silent pass.

## Writing doctrine (from Anthropic's skill-creator, verbatim in spirit)

- **Progressive disclosure.** Frontmatter description always loaded; body loaded on
  trigger — keep it under 500 lines; depth goes in `reference/` files loaded on demand.
- **Pushy descriptions.** The frontmatter description states concrete trigger phrasings
  (use the should-trigger list from `intent.md`) and what the skill outputs.
- **Explain why, don't shout.** Imperative instructions with the reasoning attached; a
  constraint whose reason is stated survives paraphrase and edge cases — ALL-CAPS MUSTs
  don't. Trust the executing model to generalize from the why.
- **Generalize (their "principle of generalization").** The motivating course/paper/
  example must not leak into the skill as a hidden assumption; a cold agent in a
  different discipline should be able to execute it.
- **Tool-agnostic bodies.** Neutral placeholders per the new plugin's
  harness_adaptation.md; "a fresh subagent session", not harness API names.

## Rubric authoring (before the skills that use them)

For every reviewer pairing in the architecture, write the rubric from the standard
template: input allowlist · scored dimensions summing to 100 (state "100 points" so the
lint verifies the sum) · threshold 85 · critical flags (include "stance violated" where a
contested choice threads through — L2) · output JSON schema · iteration policy · one
worked failure example. Ground every dimension in the plugin's grounding map.

## Per-skill cycle

1. **Draft** the SKILL.md against its architecture spec.
2. **Independent review**: dispatch a fresh subagent session whose input is ONLY the
   draft (+ its references), the plugin's `grounding_frameworks.md`, this skill's spec
   in `architecture.md`, PAGE's `<page-skill-dir>/reference/skill_quality_rubric.md`,
   and `<page-skill-dir>/reference/lessons_learned.md` (the rubric's critical-flag
   language references the lessons by number — a reviewer without the ledger can't
   apply them). It returns the rubric's output JSON; save it to
   `reviews/<skill>_review.json` BEFORE anything is shown to the author.
3. **Iterate** per the rubric's policy (≥85 and no critical flags → done; 80–84 → revise
   with findings, max 3 rounds; <80 → escalate to the author with top findings).
4. Mark the BUILD_PLAN item.

## Author gate (batched)

Don't gate every skill separately — that burns the gate budget (L4; the umbrella
records this as a justified deviation: quality is judged per-skill by the reviews, the
batch gate is only sign-off). Batch by pipeline stage: present each batch with a
per-skill summary card (purpose, anchor, review score, open findings) and collect
structured decisions, persisted as `draft_gate_decision_<batch>.json` —
`{decision, skills:[{name, disposition: approve|revise, comment}], guidance}`. The
review logs are already on disk; link them. Gate spec: gate_id `draft_gate_<batch>`;
owns — revise dispositions route back to step 1 for that skill; invalidates — a
revised skill re-enters review (step 2), and if its rubric changed, every review made
with the old rubric (per the stale-state rule above).

## Exit

All BUILD_PLAN draft items checked, all reviews ≥85 with no critical flags, author
batches approved. Stage-end summary, then `page-test`.
