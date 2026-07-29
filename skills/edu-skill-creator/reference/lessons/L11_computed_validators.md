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
- **Mechanical never-accept-on-behalf (upgrades L5).** Where the environment offers a surface
  the agent cannot write to, gate decisions are stamped there (`submitted_via`, content-derived `decision_id`); a hand-written decision
  file is the named anti-pattern — the pilot had a gate "accepted by agent action," and
  no prose rule caught it until the stamp check existed.

**Corollaries added 1.11 (rows f3, f19, f20, f26, and f6's threshold clause).**

*A verification report is self-interested evidence.* It counts only when its provenance, target
binding, freshness and reproducibility are established — a citation to a passing report is not
evidence unless it re-runs to the same verdict, and stale versus forged is indistinguishable, so both
block. A status that reduces scrutiny is assigned by the verifier, never asserted by the producer.
Observed: a completion claim resting on fifteen hand-written gate decisions, fourteen sharing a
microsecond-identical timestamp; a 128-byte forged report cited by an AI reviewer's approval while the
real validator failed seven criticals; a delta re-gate invoked with an empty changed-list approving an
artifact nobody viewed; an independence flag emitted as the string "false", truthy in every naive
check, so gate flags are validated by type.

*Criteria carry operational definitions.* Every criterion ships a stated observable that would fail it
and at least one worked failing example. A criterion naming a principle with no behavioural anchor
cannot reject anything, whatever severity it is assigned.

*The motivating artifact enters the acceptance suite.* A rubric or validator change that cannot fail
the artifact that motivated it has not been implemented.

*Thresholds are independently re-derived.* Any numeric threshold is reimplemented by a second
implementer from the written definition, never from the code. Of eight markers so tested, three died;
one had been inflated roughly threefold and already quoted in three documents. Where the literature
supplies no threshold, prefer a presence check or a reported value shown to a human over an invented
number — three invented targets have been withdrawn at cost.

*Measure the exemplars you ship.* Run the skill's own instrument over the skill's own examples before
release; it is cheap and it tests whether authored guidance produces the behaviour it describes.

*Detectors need a domain model of legitimate variation.* Pure similarity either blocks deliberate
variation or misses disguised reuse. A shared problem stem with a new target was legal pedagogy a naive
exact-match gate would have blocked; ambiguous matches route to a human rather than failing closed.

*Enforcement status: the self-interested-report corollary is covered by test scenario 13. Threshold re-derivation, exemplar self-measurement and domain-model-aware detectors are guidance only — no dedicated check yet, recorded rather than implied (L13).*
