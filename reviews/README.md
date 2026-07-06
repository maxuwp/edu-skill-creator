# reviews/ — durable independent-review evidence for Edu Skill Creator's own skills

Edu Skill Creator applies its drafter ≠ reviewer rule (lesson L3) to itself. Each file here is the
output of a **fresh-context subagent review** of one Edu Skill Creator skill against
`skills/edu-skill-creator/reference/skill_quality_rubric.md`, written to disk before any
author-facing approval.

## Scope

- **Reviewed:** every SKILL.md (the umbrella + 9 stage skills) — one
  `<skill>_review.json` each, following the rubric's output schema.
- **Not separately reviewed:** the `reference/*.md` files and scripts. Rationale: the
  reference files are allowlisted INPUTS to every review (the reviewer judges each
  skill against them, so contradictions between a skill and its references surface as
  findings), and the scripts are covered by the falsifiability rule instead (each lint
  check is demonstrated failing before it counts — see CHANGELOG).

## Reviewer protocol

Input allowlist per review: the target SKILL.md, the six `skills/edu-skill-creator/reference/*.md`
files, and `docs/BUILD_PLAN.md` (whose source-anchors table is the skill's design
spec). Never the drafter's session or reasoning. Scores follow the rubric: /100,
threshold 85, critical flags block regardless of score.

## Status (2026-07-06, review pass complete)

Round 1 = first cold review; fixes applied for every finding at or above major; round 2
= independent re-review of the revised text. Where a round-2 verdict was `approve` but
carried residual findings, the cheap ones were fixed post-approval (noted below) and the
verdict retained — the remaining minors are accepted and live in the JSON logs for the
next release to consider.

| Skill | Round 1 | Round 2 | Final | Post-approval fixes |
|---|---|---|---|---|
| edu-skill-creator (umbrella) | 90, 1 critical (no self stale-state) | 97, 0 | approve | Stage-6 gate column clarified |
| edu-skill-creator-intent | 87, 0 | — (approved round 1) | approve | anchors in A.7/A.8, decision file, Part B pacing (its 3 findings) |
| edu-skill-creator-grounding | 63, 2 criticals | 97, 0 | approve | inspection-vs-rubric justification stated |
| edu-skill-creator-architecture | 78, 0 | 95, 0 | approve | inspection-vs-rubric justification stated |
| edu-skill-creator-scaffold | 70, 0 | 98, 0 | approve | — |
| edu-skill-creator-draft | 79, 1 critical (no stage stale-state) | 95, 0 | approve | batch-gate gate_id/owns/invalidates added |
| edu-skill-creator-test | 78, 0 | 97, 0 | approve | — |
| edu-skill-creator-release | 80, 0 | 90, 0 | approve | git-pull step, structural-manifest check, lint-as-reviewer justification |
| edu-skill-creator-reflect | 71, 2 criticals (no reviewer; no redaction) | 88, 0 | approve | cross-pilot ids, inspection note, TPI anchor |
| edu-skill-creator-refresh | 72, 1 critical | 91, 1 critical (blanket L3 waiver) | round 3: 90, 0 — approve | Part B scoped into the independent review alongside Part C (round-3 finding); footer/ladder naming, explicit close-out steps |

The table is the release record; the per-skill JSON files hold every finding verbatim.
The edu_skill_creator.1.1 version bump shipped only with this table green.

**Resolution annotations (edu_skill_creator.1.2).** Every finding in every JSON now carries
machine-readable `status: fixed|accepted` and a one-line `resolution`; each file has a
`resolution_pass` block naming the release it was resolved against. `fixed` = addressed
in the named release; `accepted` = deliberate, documented deviation or deferred minor.
A finding without a status is open — there are currently none.
