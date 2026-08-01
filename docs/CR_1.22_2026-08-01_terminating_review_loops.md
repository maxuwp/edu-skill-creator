# CR 1.22 — Give every review loop a declared stopping condition

**Prepared by:** Claude (Opus 5), 2026-08-01, at Dr. Ma's direction.
**Revision 0.** Not yet reviewed.
**Status:** PROPOSED. Nothing here is implemented. Per-row gate required.
**Depends on:** CR 1.20 gating first, because it allocates the next two release lint check ids and
the next rubric critical flag id. This CR takes the free ids after those, and if CR 1.20 gates
differently the ids here move with it. No id is written down here, because a numbered enforcement
claim in this repository must resolve to an implemented item (L13, release lint check 11) and none of
these exist yet.
**Sibling:** the same wiring is proposed for the POSED skill drafter as a separate CR in that
repository. This one covers Edu Skill Creator only.

**Already landed, and therefore NOT gated here:** lesson `L24_review_termination.md`, its
`lesson_index.md` row, revision 2 of `docs/CONTRACT_reviewer_behaviour_2026-08-01.md`, revision 3 of
`docs/CONTRACT_designing_reviewers_in_skills_2026-08-01.md`, revision 1 of
`docs/CONTRACT_fixer_behaviour_2026-08-01.md`, and `docs/BACKLOG_contract_wiring_2026-08-01.md`. All
of it is prose. **L24 is currently doctrine with no enforcement**, which is the same state L19 was in
when CR 1.20 opened, and this CR is the same kind of remedy.

---

## 1. The defect

A review loop in this project has a declared scope (L22) and a declared shape (L19), and **no
declared end**. Every round is dispatched with the same brief, so every round is an open invitation
to find something, and the only stopping mechanism in the system is the faculty member losing
patience and saying stop.

Observed 2026-08-01. The fixer contract, revision 0: 98 lines, status `PROPOSED`, loaded by nothing,
sent out with five specific questions. The return was six major findings, three minor findings, a
larger replacement envelope and eleven acceptance tests — a full revision cycle against a draft that
governed nothing. Challenged, the reviewer withdrew the disposition in full and settled on two local
corrections, naming its own error: it had treated a short proposed behavioural contract as if it were
a production protocol.

*Evidence status.* One case, and the withdrawal was the reviewer's own re-disposition under
challenge rather than an independent adjudication that the six findings were invalid. What it does
establish is structural and does not depend on who was right: the round had no declared type and no
termination condition, so producing more findings was the only behaviour the brief rewarded. Dr. Ma's
judgement of the pattern — that without an interruption the exchange continues indefinitely — is the
load-bearing evidence, and it is a statement about the process, not about either party's competence.

**Why this is not covered by L19, L20 or L22.** L19 says what a round must return. L20 says when
repeated rounds indicate descent rather than convergence. L22 says where a round may look. A loop
that satisfies all three still has no exit. L24 supplies the missing condition, and this CR makes it
a mechanism.

## 2. What "done" would look like

A review stage that can be dispatched and cannot fail to terminate: the round type is declared on
dispatch, the follow-up round is structurally forbidden from opening unbounded findings, settlement
happens on a passing targeted check without anyone asking for it, and the round budget overrun
routes to the faculty member as a decision rather than as another round.

## 3. Rows

| Row | Change | Why |
|---|---|---|
| `t1` | `skills/architecture/SKILL.md`: every reviewer pairing declares `round_type` and `round_budget` at design time. A pairing that specifies a reviewer with no round type and no budget is an incomplete design and the stage says so. | L24, and L4: the gate budget is a design-time property, not a runtime improvisation. |
| `t2` | `skills/draft/SKILL.md`: the review brief template carries the round type and, for `disposition_check` and `targeted_check`, the four-member reopen class verbatim. **After a full review, the next dispatch is never another full review.** | The defect is created by the brief, so the brief is where it is fixed. A brief that asks for open review gets open review, every time. |
| `t3` | Reviewer output schema gains `round_type: full_review \| disposition_check \| targeted_check` and, on any finding opened by a non-full round, `reopen_class: contradiction \| false_approval \| irreversibility \| protected_property_broken`. | Designer contract revision 3, invariant 7. A rule with no field to check is prose. |
| `t4` | **New release lint check (next free id after CR 1.20)**: a finding recorded under a non-full `round_type` with no `reopen_class`, or with a `reopen_class` outside the four, fails. Fail-closed, one negative fixture per branch. | L11: the requirement is checkable, so code checks it. Without it, `t3` is a field nobody reads — the exact failure recorded when five invented escalation keys sat in manifests no validator opened. |
| `t5` | Era-gate `t4` on the same `review_contract_version` field CR 1.20's `c5` introduces. Logs that predate the era, or read `pre-1.20`, are exempt; a post-era log with no round type fails. | Without the era gate the check fails on every existing review log. With a missing-means-exempt default it fails open forever. Same argument as `c5`, and it is why `t4` can ship at all. |
| `t6` | `skills/test/SKILL.md` round records log the declared round type, the round index against its budget, and whether the round stayed inside its type. | L20's convergence-versus-descent metric cannot distinguish descent from over-review unless the round type is recorded. This row is what makes the L24 hypothesis falsifiable rather than doctrinal. |
| `t7` | Settlement is a stage transition, not a message: when the targeted checks on the named corrections pass, the stage marks the artifact settled and stops dispatching. Reopening a settled artifact requires a named reopen-class member, recorded. | "Settlement is a favour someone must ask for" is the current state, and the asker is always the human. |
| `t8` | Budget overrun routes to the faculty gate as a decision — continue with a raised budget, accept as-is, or re-scope — never to another automatic round. | L5: the human decides cost and risk. An agent that grants itself one more round has set its own budget. |
| `t9` | `skill_quality_rubric.md` gains a **critical flag, at the first free id after the one CR 1.20 claims**: "a review stage dispatches a reviewer with no declared round type, or has no state in which review ends". | Critical flags are how this repository makes a rule block rather than advise. |
| `t10` | The backlog register becomes part of the stage design: a named file per artifact where out-of-class observations go, recorded once. A stage that forbids raising an item without providing somewhere to put it will get it raised as a finding anyway. | L18: make the compliant path cheaper than the workaround. This is the compliant path for a reviewer who genuinely sees something worth keeping. |

## 4. Risks, stated rather than mitigated away

**The reopen class can be gamed.** Any finding can be framed as a contradiction if the reviewer wants
it raised. `t4` checks that the label is present and legal, not that it is honest. What the label buys
is that a gamed reopen is visible in the record and countable afterwards, which an unlabelled finding
is not.

**Suppressing real defects.** A disposition check that finds a genuine problem outside the four
classes writes it to backlog, and if the artifact then ships with that problem, this CR caused it. The
judgement being made is that a review process nobody can stop costs more than the backlog items it
would have caught. That judgement is contestable and should be revisited once `t6` produces data —
specifically, how many backlog items later become real defects.

**One case.** The evidence in §1 is a single exchange. The structural claim does not depend on
adjudicating it, but the magnitude does, and this CR does not claim a measured saving of tokens or
rounds. `t6` exists so that the next version of this argument is made from counts.

## 5. What this CR does not do

It does not wire the three contracts into any skill. Nothing loads them today and nothing loads them
after this CR gates; the rows here wire **L24** specifically, through the brief, the schema, the lint
and the rubric, which are the four surfaces this repository has already established as the ones that
make a rule bind. Contract wiring remains the open decision recorded in
`docs/BACKLOG_contract_wiring_2026-08-01.md`.
