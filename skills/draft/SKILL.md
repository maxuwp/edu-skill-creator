---
name: page-draft
description: PAGE Stage 5 — Draft the new educational plugin's skills and rubrics, each independently reviewed. Writes SKILL.md bodies per the approved architecture using skill-creator writing doctrine (progressive disclosure, under 500 lines, explain-why), authors the reviewer rubrics, and routes every draft through a fresh-context review against the skill quality rubric. Triggers - when the page umbrella dispatches Stage 5, or the user says "draft the skills" for a plugin under construction.
version: "1.0"
---

# PAGE Stage 5: Draft

Fills the scaffold's stubs with real skills, in the BUILD_PLAN's dependency order:
reference files → rubrics → sub-skill SKILL.md bodies → umbrella body. Every draft gets
an independent review before the author sees it (L3 — applied to ourselves).

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
   draft (+ its references), the plugin's grounding map, the architecture spec for this
   skill, and PAGE's `<page-skill-dir>/reference/skill_quality_rubric.md`. It returns
   the rubric's output JSON; save it to `reviews/<skill>_review.json` BEFORE anything
   is shown to the author.
3. **Iterate** per the rubric's policy (≥85 and no critical flags → done; 80–84 → revise
   with findings, max 3 rounds; <80 → escalate to the author with top findings).
4. Mark the BUILD_PLAN item.

## Author gate (batched)

Don't gate every skill separately — that burns the gate budget (L4). Batch by pipeline
stage: present each batch with a per-skill summary card (purpose, anchor, review score,
open findings) and collect structured decisions (approve / revise + comment, per skill).
The review logs are already on disk; link them.

## Exit

All BUILD_PLAN draft items checked, all reviews ≥85 with no critical flags, author
batches approved. Stage-end summary, then `page-test`.
