# Designing an AI reviewer inside a skill — for the Edu Skill Creator and POSED drafters

**When you write a stage that dispatches a reviewer, this is what the reviewer's contract and its
consumer must look like.** Derived from evidence in this project's own records, with each rule's
evidence status attached so the weak ones can be argued with.

**Revision 2, 2026-08-01**, after Codex's disposition check on revision 1. Revision 1 (same day,
after Codex's first review) stopped forcing a mechanical check into reviews where none is valid, and
added runnability, population type and stable finding ids. Revision 2 closes the four findings that
check left partially open: the envelope's fields existed but the **relationships between them did
not**, which is a schema that looks strict and enforces nothing. It now carries `coverage_model`,
`confirmed_id`, the repair-guidance fields the prose already required, structured `scope_pressure`,
and six conditional invariants.

Unchanged and protected across both revisions: the named-consumer rule for escalation outcomes,
review at the representation the faculty member actually judges, delta review followed by one
settlement regression, and the deferral of an automated rebase engine. Codex verified all ten
protected properties intact at revision 1 and did not reopen them.

---

## 1. The reviewer's output schema, not its prose

A review brief that asks for good behaviour in prose gets it inconsistently. Specify the **output
shape** and let the lint check it:

```
artifact_and_version:
population_type:            finite | bounded_model | open_ended
review_population:          enumerated where the type allows
coverage_limitations:
coverage_model:             required for bounded_model, and for any class-level claim on an
                            open-ended surface
in_scope / out_of_scope:
acceptance_oracle:
confirmed_correct:          [{confirmed_id, property, how_verified, how_verified_kind,
                              claim_layer, location}]
do_not_break:               [confirmed_id]
findings:                   [{finding_id, claim_or_surface, evidence,
                              acceptance_constraints, smallest_change,
                              affected_dependencies, alternatives,
                              preserve:[confirmed_id], severity}]
scope_pressure:             [{issue, load_bearing, required_boundary,
                              authorized_route, consumer, persistence, closing_state}]
requirements_questions:     [{question, decision_if_yes, decision_if_no}]
review_status:              completed | unrunnable
unrunnable_reason:
outcome:                    PASS | REVISE_LOCAL | CLARIFICATION_REQUIRED | REBASE_REQUIRED | null
rebase_subtype:             boundary_rescope | foundation_rebase | null
cost:                       calls, tokens, elapsed — or "not recorded"
```

**Six conditional invariants, which are what make the envelope checkable rather than decorative.**
Revision 1 carried the fields and left the relationships between them unstated, which is a schema
that looks strict and enforces nothing.

1. `review_status: completed` requires a non-null `outcome` and an empty `unrunnable_reason`.
2. `review_status: unrunnable` requires `outcome: null` and a non-blank `unrunnable_reason`.
3. `rebase_subtype` is required only when `outcome: REBASE_REQUIRED`, and is null otherwise.
4. `PASS` is prohibited while any `scope_pressure` item with `load_bearing: true` lacks an
   `authorized_route`.
5. Every `do_not_break` entry and every finding's `preserve` value must resolve to a declared
   `confirmed_id`.
6. A class-closure claim on `bounded_model` or `open_ended` requires an explicit `coverage_model`
   and a statement of residual uncertainty.

**Evidence must fit the claim, and no single kind is universally required.**

```
how_verified_kind: mutation | command | diff | schema | independent_semantic_review |
                   human_gate | primary_source | other
claim_layer:       structural | behavioral | semantic | preference
```

Mechanical evidence is mandatory for structural and executable claims **where it is available**.
Semantic and preference claims require an appropriate independent or human source instead. Forcing a
mechanical item into a pedagogical review manufactures a proxy check, which is the error already
recorded in this project when one authored tag agreeing with another authored tag was read as
pedagogical truth. What remains forbidden everywhere is "read it and it looked right" with no source
at all.

`review_status` is orthogonal to `outcome`: a reviewer that cannot reach the artifact or run a
required check is `unrunnable` with a null outcome, and never authorizes progress. `finding_id` is
stable so a separate coder can compute overlap after the fact — reviewers do not self-assess
uniqueness.

## 2. Every escalation outcome needs a named consumer, and the lint must prove it exists

**This is the most strongly evidenced rule here and the one most likely to be skipped.** Spontaneous
escalation is observed — agents reached for it through five invented manifest keys that no validator
read, and six reproducible defects, two of them completion-blocking for every future module, sat in
one of those keys until someone happened to ask for a summary. How *often* agents escalate is not
measured, because opportunities and behaviours were never separately coded; the missing consumer is
what was directly observed.

So: for `CLARIFICATION_REQUIRED` and `REBASE_REQUIRED`, the stage design must name **who consumes
it, where it persists, and what state closes it**. A skill that emits an escalation with no consumer
has built a channel into a wall. If you can write the emitter and not the consumer, do not ship the
emitter.

## 3. Review at the layer the faculty member actually judges

*Evidence: strong, and it is the most expensive failure recorded.* Stage 5's markdown gate concealed
timing conflicts, missing response mechanisms, unexplained terminology, misplaced activities, missing
prerequisites and unresolved visuals. All of them became obvious in the Stage 6 render — after
substantial downstream work already existed on top of them.

When you place a review gate, ask what representation the human will actually judge, and put the gate
there. A cheaper gate on the wrong representation is not cheaper.

## 4. Foundation first, then breadth, then one report

The reviewer tests the requirements, architecture, evidence source and acceptance oracle **before**
inspecting details, and stops if any fails. Then it inspects the declared population — completely
where `population_type` is finite, and within the stated model otherwise — and reports once. Build the brief so that stopping early on a bad foundation is the *compliant* path,
not an exception — otherwise a reviewer that finds a broken oracle still has to produce a full
finding list to look diligent.

## 5. Separate the finder from the fixer, and review only the delta

The reviewer names the smallest acceptable change; a different agent implements it against the
protected baseline. Then re-review **the changed units and their dependency-affected units only**,
and run the complete deterministic regression once at settlement.

Do not re-dispatch unchanged artifacts through full model review because something nearby moved. The
nearest measured analogue is regression test selection, where safe selection has fault-detection
ability equivalent to retest-all under stated conditions — so state the conditions, and record what
you deemed unaffected.

## 6. Make closure language part of the schema

`closed`, `verified` and `implemented` must resolve to one of: local repair, defect-class closure, or
full acceptance. A validator can check that the word appears with its qualifier. A report saying
`release_lint: 0 error(s)` while the prevented behaviour remained possible is a real event in this
corpus, not a hypothetical.

## 7. Record the process, or none of this can be evaluated

Have the stage write, per round: findings opened, closed and reopened; previously confirmed
properties broken; whether the object under review changed and whether that change was declared; and
calls, tokens, elapsed time and artifacts regenerated. Plus, per reviewer, the count of unique valid
findings — computed **post hoc by a separate coder** from stable finding ids, never self-reported. A
reviewer cannot know another reviewer's counterfactual output, and a self-prediction of uniqueness is
one more same-agent assertion offered as evidence.

**This is what turns the rest of this contract from doctrine into something testable.** Without it,
the next revision of these rules will be argued the way this one was — from plausibility and three
models agreeing with each other.

## 8. What NOT to build yet

Two independent retrospective checks over eight review transitions found **zero demonstrable silent
descents** and four undecidable. Foundation Regress, minimal-scope instructions as a cause, and token
causation are **hypotheses awaiting prospective instrumentation**, not established pathologies.

So: build the envelope (§1), the routing (§2) and the recording (§7). Do **not** build an automated
rebase system, a layer taxonomy enforcement, or a scope-descent detector yet. When this project last
shipped enforcement ahead of evidence, it invented a one-descent-per-round cap that had no support,
and the withdrawn rule then survived three commits in the always-read index while the corrected
lesson sat unread underneath it.

Lens diversity for high-risk work — one reviewer on semantic validity, one on implementation
integrity, one on usability — is supported by the evidence available. Whether **same-brief** reviewers
add as much is not yet measured, and the corpus that would settle it exists but is uncoded.

## 9. Acceptance tests for the wiring, so §1 to §7 can fail

From Codex's review of this contract. A stage that claims to implement the envelope should be able to
produce each of these.

1. Missing artifact access produces `review_status: unrunnable`, never a semantic outcome.
2. A finite schema review may claim class closure after exhaustive controls.
3. An open security review reports its threat model and residual uncertainty, not universal closure.
4. A semantic teaching review passes without manufacturing a mechanical `confirmed_correct` item.
5. `CLARIFICATION_REQUIRED` names a consumer, a persistence path, and a closing state.
6. Load-bearing boundary scope pressure with no authorized route cannot return `PASS`; it routes
   through `REBASE_REQUIRED` with `rebase_subtype: boundary_rescope`. Boundary pressure that is not
   load-bearing, or that already has an authorized route, does not block `PASS`.
7. Two independent reviewer reports are coded post hoc for overlap, without reviewer self-prediction.
8. A reviewer may propose repair constraints but cannot modify the artifact during the review pass.
9. The security example is described as incomplete control coverage, with the parser's
   defence-in-depth value preserved.

**When these get wired, do not inject both documents into every reviewer prompt.** Keep the designer
contract as an authoring reference. Maintain one compact operative core for reviewers — the envelope,
the six invariants, the review order, and the outcome definitions — and link the evidence discussion
rather than repeating it. Test retention and output conformance through the actual harness before
calling the behaviour durable, and do not invent a word limit before that test. As measured on
revision 1: the reviewer contract is about 1,450 words and this one about 1,380, and neither is
loaded by anything yet, so no retention failure has been observed either way.

**Open questions neither contract settles**, carried from the same review: whether separate finder
and fixer agents improve quality enough to justify their cost; whether delta-only model review
preserves semantic defect yield; the frequency of spontaneous escalation under verified
opportunities; whether same-brief reviewers add enough unique valid findings to justify routine
parallel review; and whether `REBASE_REQUIRED` should be renamed `RESCOPE_REQUIRED` with foundation
rebase as its subtype.
