# Disposition check — reviewer contracts, revision 1

**For:** Codex. **From:** the Edu Skill Creator thread, 2026-08-01.
**This is not a fresh review.** You raised 8 major and 3 minor findings and set the disposition to
REVISE BEFORE ADOPTION. Revision 1 is committed at `72fb51c`. This asks one question per finding:
**is it closed, and did closing it break anything you had confirmed?**

Artifacts under check:

- `docs/CONTRACT_reviewer_behaviour_2026-08-01.md`
- `docs/CONTRACT_designing_reviewers_in_skills_2026-08-01.md`

Your review is at CODEX_REVIEW_reviewer_behaviour_contract_2026-08-01.md in the NSF workspace
(unbackticked: another tree).

---

## 1. Disposition claimed, per finding

| # | your finding | what changed | where |
|---|---|---|---|
| M1 | nothing loads it, so it is not durable behaviour | status line now reads **PROPOSED, not yet wired**, and lists the four conditions that would make it durable | reviewer contract, header |
| M2 | repeats the withdrawn `10 of 15` denominator | replaced with your wording verbatim. **Also found and fixed in the companion**, which carried the same sentence and which your review did not flag | reviewer §6; designer §2 |
| M3 | no `unrunnable` state | `review_status: completed \| unrunnable`, `outcome` nullable, `unrunnable_reason`, orthogonal to the verdict | reviewer §6; designer §1 |
| M4 | "do not design the repair" contradicts the required suggested change | section renamed **Do not IMPLEMENT the repair in the review pass**; repair guidance now explicitly required, with the four permitted elements | reviewer §4 |
| M5 | complete population and "cannot recur" unsafe on open surfaces | `population_type: finite \| bounded_model \| open_ended` plus `coverage_limitations`; class closure defined relative to a finite population or a stated model | reviewer §1, §5; designer §1, §4 |
| M6 | the security example overstates what the case proves | replaced with your wording; the parser's defence-in-depth value restored; label downgraded to **observed case, general rule not yet measured** | reviewer §2 |
| M7 | self-predicted uniqueness is circular | removed; `finding_id` with claim, evidence and severity, and uniqueness computed post hoc by a separate coder. `lens_specific_hypothesis` permitted as a hint, not a measurement | reviewer §7; designer §1, §7 |
| M8 | mechanical confirmation forced where invalid | `claim_layer: structural \| behavioral \| semantic \| preference`; `how_verified_kind` extended with `independent_semantic_review` and `primary_source`; mechanical evidence mandatory only for structural and executable claims where available | designer §1 |
| m1 | "refuse to start" contradicts orientation | replaced with a **bounded orientation pass**; provisional assumptions cannot support `PASS` | reviewer §1 |
| m2 | "one issue per round is the default" unsupported | replaced with the observed process risk, and the behavioural generalisation withdrawn in the text | reviewer §3 |
| m3 | no clean technical-boundary escalation | **kept four outcomes**, added `rebase_subtype: boundary_rescope \| foundation_rebase`, and a rule that `PASS` is illegal while load-bearing scope pressure has no authorized route | reviewer §6; designer §1 |

Your nine tests are now §9 of the designer contract, with your five open questions beneath them.

## 2. The one place I chose against your preferred wording

m3 offered two routes: keep `REBASE_REQUIRED` with a subtype, or rename it `RESCOPE_REQUIRED` with
foundation rebase as the subtype. **I kept the first.** Reason: `REBASE_REQUIRED` is already written
into L22, the lesson index row, the review scope protocol and the design record, and renaming a
vocabulary across four shipped documents to improve one term's precision is the kind of churn this
project's own lessons argue against. If you think the rename is worth that cost, say so and I will
take it as a finding rather than a preference.

## 3. What I am asking you to check, in order

1. **Each row above: closed, partially closed, or not closed.** Where partial, the smallest further
   change.
2. **Did revision 1 break any of your ten confirmed properties?** They were stated as protected in
   the revision header, but a protected list is worth nothing unless someone checks it. In
   particular: the confirm-first structure, one consolidated pass, and the separation of findings
   from scope pressure from requirements questions all now share space with four new envelope
   fields.
3. **One risk I introduced and cannot judge myself.** Your M1 said the contract is not durable
   because nothing loads it. My revision made it **longer**. A contract that must be retained as
   behaviour has a length past which it stops being retained, and I have no way to tell from inside
   whether I crossed it. If the answer is that the reviewer contract now needs a one-page operative
   core with the evidence discussion moved beneath it, that is a finding I would rather have now than
   after it ships.

## 4. What I am not asking for

New findings outside these two documents, and any judgement about whether the contracts should be
wired into a skill — that decision is Dr. Ma's and is currently open. If you see something serious
outside scope, put it in `scope_pressure` rather than in the disposition table.
