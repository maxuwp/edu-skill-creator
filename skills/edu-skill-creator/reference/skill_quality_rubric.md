# Skill Quality Rubric — reviewer instrument for drafted skills (/100, threshold 85)

Used by `edu-skill-creator-draft`'s independent reviewer. The reviewer runs in a **fresh context**
with this input allowlist ONLY: the drafted SKILL.md (+ its reference files), the new
plugin's grounding map, the architecture doc's spec for this skill, and
`lessons_learned.md`. Never the drafter's reasoning or chat context (L3).

## Scored dimensions (sum = 100 points)

| # | Dimension | Pts | What passes |
|---|-----------|-----|-------------|
| 1 | Grounding fidelity | 25 | Every process/criterion traces to the grounding map; frameworks applied within their stated scope; no invented process without a recorded justification |
| 2 | Gate & reviewer correctness | 25 | Gates follow `gate_design_patterns.md` (one decision, stable ids, decision JSON, reviewer-before-gate, never-accept-on-behalf); content stages have an independent reviewer with an input allowlist |
| 3 | Authoring craft | 20 | Progressive disclosure (body < 500 lines, references for depth); imperative instructions that explain why; generalizes beyond the motivating examples; a cold agent could execute it |
| 4 | Pipeline integrity | 15 | Inputs/outputs named exactly (files, manifest fields); refuses to run on missing/stale inputs; dependency and stale-state behavior specified |
| 5 | Harness neutrality & hygiene | 15 | No hardcoded harness paths (placeholders per harness_adaptation.md); versioned; changelog-ready; expensive operations consent-gated (L6) |

Scoring: start at each dimension's maximum; deduct per finding (blocking −8, major −4,
minor −1; floored at 0 within the dimension).

## Critical flags (block regardless of score)

1. A pedagogically contested choice is baked in as a default (L2).
2. A content-generating step reviews its own output (L3).
3. A gate can be skipped, or the skill instructs accepting on the human's behalf (L5).
4. A framework is cited outside its validated scope (L1 corollary).
5. A token-expensive operation runs without a consent gate (L6).
6. Downstream artifacts are not invalidated after upstream changes (L4).
7. Student data or PII is handled without governance — no retention/deletion,
   de-identification, redaction, or permissions rules where the data-flow model
   requires them (FERPA/PTAC anchor).
8. An external service or API is used without disclosure and consent in the plugin's
   intake or gate flow.
9. The skill generates HITL web pages without keyboard and screen-reader operability
   (WCAG 2.2 anchor) — the gate human may be the person who needs it.
10. A single body grammar/template is imposed on heterogeneous educational content, or
    precision content (definitions, equations, code, verbatim problem statements) is
    subject to trimming or paraphrase-to-fit at ANY pipeline stage (L10) — a humanized
    or shortened definition is a wrong definition.

## Output schema

```json
{
  "skill": "<name>", "score": 0, "threshold": 85,
  "dimension_scores": { "grounding": 0, "gates": 0, "craft": 0,
                        "integrity": 0, "hygiene": 0 },
  "critical_flags": [],
  "findings": [ { "severity": "blocking|major|minor", "location": "…",
                  "issue": "…", "fix": "…" } ],
  "recommendation": "approve | revise | regenerate"
}
```

Iteration policy: score ≥ 85 and no critical flags → human gate opens. 80 ≤ score < 85 →
drafter revises with the findings (max 3 rounds). Score < 80 → escalate to the author
with the top findings.

## Worked failure example

A drafted `quiz-builder` skill says: *"Generate 10 MC items per objective; distractors
should be plausible."* Findings: no anchor to Haladyna's item-writing rules (dim 1,
major); no independent item reviewer (critical flag 2); item count invented rather than
derived from the assessment blueprint (dim 1, major); gate collects feedback as free text
(dim 2, major). Recommendation: regenerate against the grounding map.
