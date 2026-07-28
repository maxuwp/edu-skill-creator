<!-- Detail for L11. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L11 — Prose contracts rot; structural requirements need computed, fail-closed validators

**Rule.** Any requirement that code can check, code MUST check. For each artifact,
identify the structural requirements (required rows/fields/tags, coverage against an
upstream contract, count/pacing bands, forbidden markers) and write a computed validator:
**one implementation, two callers** — the drafter runs it pre-gate as a self-check, and
the reviewer re-runs the SAME script as a hard gate. A reviewer's `approve` is illegal
unless the recorded computed checks passed; the orchestrator refuses to open the human
gate on a review log missing them.

**Failure that taught it.** POSED's pilot deck passed FOUR fresh-context review rounds at
94/100 while carrying 13 structural criticals (unmaterialized activities, missing
takeaway, missing subgoal labels); the approved outline scored 97/100 with 5 more. The
reviews weren't lazy — the requirements were prose, and language models score prose
charitably. Computed validators (posed_skill.1.27–1.30) failed both artifacts instantly.
L3's fresh-context reviewer catches *judgment* defects; it does not establish
*structural* facts. Both layers, always.

**Corollaries, each also paid for:**
- **Fail closed.** A missing record, absent artifact, unknown contract version, or
  zero-widget gate page is a refusal, not a skip: POSED's publisher shipped untracked
  files because a missing manifest record was treated as publishable, and its completion
  check trusted a forgeable `exists:true` (posed_skill.1.30.1 — six such holes).
- **Prove by attack, not only by fixture.** Fixture-driven proofs exercise only the paths
  fixtures cover; an adversarial reviewer forging records/bypassing steps found every
  fail-open hole the green fixtures never touched (defense-in-depth; NIST SSDF spirit).
- **Falsifiability against REAL artifacts.** Each validator is proven failing on the
  actual defective pilot artifact AND passing on a synthetic fixture; fixtures ship in
  the repo (release lint runs the pairs) and NEVER contain student/faculty course
  content (the data posture applies to test data too).
- **Aggregates need distribution checks.** Notes passed a 98% word-count band with one
  sentence repeated 54× and an identical cue block on 39/39 slides — repetition defeats
  totals; check uniqueness/variance, not just sums.
- **Anti-softener rubric language.** Rubric phrasing that permits rationalization
  ("present *or clearly represented*") is a named defect — the exact phrase let 2 of 3
  missing activities pass.
- **Mechanical never-accept-on-behalf (upgrades L5).** Gate decisions are stamped
  server-side (`submitted_via`, content-derived `decision_id`); a hand-written decision
  file is the named anti-pattern — the pilot had a gate "accepted by agent action," and
  no prose rule caught it until the stamp check existed.
