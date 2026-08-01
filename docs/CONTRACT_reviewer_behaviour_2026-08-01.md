# Reviewer contract — for Codex, Grok, Fable, and any model asked to review

**Status: PROPOSED reviewer contract, not yet wired.** No skill entry, lesson index row, reviewer
dispatch, schema or lint currently loads it, so it is prose outside the loading path — which is the
defect its own companion warns about. It becomes durable behaviour when the briefs inject its fields,
a schema validates the envelope, non-pass outcomes have named consumers, and process data is
recorded. Until then, adopt it by choice.

Derived from evidence in this project's own records; each rule carries its evidence status so the
weak ones can be argued with rather than obeyed equally.

**Revision 2, 2026-08-01** adds §8, the termination rule: every round declares its type, a
disposition check may not open new findings outside a short reopen class, settlement is automatic,
and review depth is proportional to the artifact's status. It changes nothing else.

**Revision 1, 2026-08-01**, after an independent review by Codex. What that review confirmed and
neither revision touches: the confirm-first structure with `confirmed_correct` before findings and a
do-not-break baseline; one consolidated report rather than serial single-finding returns; the
separation of local findings, scope pressure and requirements questions; the three-way closure
language; the requirement for artifact version, scope, oracle and prior confirmed properties; honest
`not recorded` for missing cost data; and the refusal to claim token savings or universal foundation
regress. Eleven findings changed the rest, each noted in place.

---

## 1. Declare before you read

Before substantive review, run a **bounded orientation pass**: derive these fields and disclose them.
Stop only when a load-bearing field cannot be derived safely. An assumption about the oracle or the
scope is marked provisional and cannot support `PASS` until it is confirmed.

```
artifact_and_version:      what you are reviewing, at what hash or revision
population_type:           finite | bounded_model | open_ended
review_population:         the set you will inspect, enumerated where the type allows
coverage_limitations:      what you could not reach, and why
in_scope / out_of_scope:   surfaces you may and may not raise findings about
acceptance_oracle:         what would establish that this artifact is correct
prior_confirmed:           properties an earlier round verified, which you must not break
```

**`population_type` is not a formality.** Security, usability and semantic surfaces frequently have no
finite population, and a contract that demands one invites an unsupported universal claim. Enumerate
where enumeration is possible; otherwise state the threat or behaviour model you worked within, and
report residual uncertainty rather than coverage.

A review that cannot say what it covered cannot support a claim of closure, whichever type it is.

## 2. Test the foundation before the details

Are the requirements, the architecture, the evidence source and the acceptance oracle valid? If any
of them fails, **stop the detailed review** and return one consolidated packet. Reviewing the
descendants of an invalid foundation produces findings that will be discarded.

*Evidence: observed case, general rule not yet measured. One recorded security review found four
bypass mechanisms across four rounds before replacing URL enumeration as the primary control with
deny-by-default CSP. The parser remained useful as defence in depth, so the earlier findings were
incomplete rather than useless. This supports testing the control model before exhaustive mechanism
enumeration; it is one case, not general proof.*

## 3. Report once, and report both halves

Complete the declared population, then return **one** consolidated report containing:

- `confirmed_correct` — what you checked and found right, with **how you verified it**. A mechanism,
  not an impression. This is the do-not-break baseline for the next round.
- `findings` — each as the smallest acceptable change, naming what it must not disturb.
- `scope_pressure` — anything whose fix lies outside the declared scope. Not a finding. Not fixed by
  you.
- `requirements_questions` — load-bearing ambiguities only, each written with the decision its answer
  settles. If neither answer changes a decision, do not ask it.

A partial report presented as complete causes unreviewed breadth to reappear as new findings in later
rounds, which is what makes a loop look endless from the outside. The records show that pattern; they
do not establish that reviewers generally return one issue at a time, and this contract no longer
claims they do.

*Evidence: mixed. Defect-only reviews demonstrably let fixes create later defects — three findings in
one round were introduced by the previous round's own fixes. That confirm-first then prevents this is
observed in one change request and is not generally proven.*

## 4. Do not IMPLEMENT the repair in the review pass

Repair guidance is required, not forbidden — an implementer that has to infer the intended fix will
often infer a different one. Specify the acceptance constraints, the smallest repair shape, the
affected dependencies, and the alternatives where an architectural choice is genuinely open.

What is forbidden is modifying the artifact during the review pass. Implementation is a separate
pass, and for consequential changes a separate agent, working against the protected baseline. A
trivial local correction may be implemented by the same author in a later, explicitly delimited pass
and then independently reviewed.

*Why: the finder and the fixer being the same party in the same pass is how a round's fix becomes the
next round's defect — three findings in one recorded round were introduced by the previous round's
own fixes.*

## 5. Say precisely what "done" means

Never write closed, verified, or implemented without distinguishing:

```
local repair       — this instance is fixed
class closure      — this defect class cannot recur WITHIN a finite population or an explicitly
                     stated threat or behaviour model, and here is the model
full acceptance    — the complete regression passed at settlement
```

Over an open-ended surface, report the controls established and the residual uncertainty. Never write
"cannot recur" about a population you could not enumerate.

*Evidence: strong. A run reported `release_lint: 0 error(s)` while the behaviour the lint existed to
prevent remained possible. Green is a statement about what was checked, never about what is true.*

## 6. Four outcomes, plus an orthogonal runnability flag

```
review_status:    completed | unrunnable
outcome:          PASS | REVISE_LOCAL | CLARIFICATION_REQUIRED | REBASE_REQUIRED | null
unrunnable_reason:
rebase_subtype:   boundary_rescope | foundation_rebase        # when outcome is REBASE_REQUIRED
```

`review_status` is **orthogonal** to the outcome. A reviewer that cannot read the artifact, run a
required check, or reach the declared population is `unrunnable`, and `outcome` is null. Reporting
operational failure as a semantic verdict is the pass/fail/unrunnable conflation this project has
already had to correct once in validator dispatch. An unrunnable review never authorizes progress.

`CLARIFICATION_REQUIRED` means a load-bearing need is ambiguous — an expressed requirement that could
be a preference or a workaround, which the artifact cannot settle. `REBASE_REQUIRED` means a new
execution foundation **or an approved scope contract** is needed; `boundary_rescope` covers the case
where the fix exceeds the current scope without invalidating the foundation, such as an adjacent
shared component. **Do not return `PASS` while load-bearing scope pressure has no authorized route.**
Neither escalation is advice to the implementer: the requester must route them.

*Evidence: spontaneous escalation is observed, so a complete absence of escalation ability is
falsified. Its frequency and reliability are not measured, because opportunities and behaviours were
not separately coded. The directly observed systems defect is that recorded escalations had no
required consumer — five invented keys, no validator reading any of them. **If you escalate into a
channel nobody reads, you have not escalated.** Say so in your return if you suspect that is
happening.*

## 7. Record what your review cost and what it added

At the end of every review, in one line each: findings opened, previously confirmed properties you
broke or found broken, whether the object under review changed from the previous round, and any
count you honestly have of calls, tokens or elapsed time. Write **not recorded** rather than an
estimate.

Give every finding a **stable id** with its claim or surface, its evidence, and its severity, so that
a separate coder can compute overlap, unique valid findings, false positives and cost **after** all
reviewers have finished independently.

Do not predict which of your findings another reviewer would have missed. You cannot know another
reviewer's counterfactual output, and your prediction would be one more same-agent assertion offered
as evidence — the exact failure this project has a lesson about. You may label a finding
`lens_specific_hypothesis`; that label is a hint for the coder, never a measurement of uniqueness.

## 8. Every round declares its type, and the loop terminates

**This is the section that ends the reviewer duel, and it is the one to read first if you read only
one.** Before you review, you are told which of three rounds this is, and the type fixes what you may
return:

```
full review        — you may open new findings across the declared population
disposition check  — you report only whether the named prior findings closed and whether the
                     protected baseline held. You may not open new findings.
targeted check     — you report only pass or fail on the named corrections.
```

**The reopen class.** A disposition check or targeted check may open a new finding only for: a
critical contradiction between two rules in the artifact, a false approval (a property recorded as
confirmed that is not true), an irreversibility or data-loss risk, or a broken protected property.
Name which one applies. Everything else you notice — a field you would have added, a schema you would
have designed, a binding you think wiring will need — goes to **backlog**, recorded once, raised
never again.

**Settlement is a state, not a favour.** When the targeted checks on the named corrections pass, the
artifact is settled and no further general round is scheduled. You do not need to be told to stop.

**Review depth is proportional to the artifact's status.** A document marked `PROPOSED` and loaded by
nothing gets adoption review — is it coherent and safe enough to try? A document that governs
execution gets protocol review — is every field defined and every transition legal? Reviewing a
proposal as a protocol manufactures findings against a standard the artifact never claimed, and it is
the specific failure that produced this section: a 98-line proposed contract, unwired, drew six major
findings and a larger replacement envelope, all of which were withdrawn on challenge and settled with
two local corrections.

*Evidence: one case, and the withdrawal was the reviewer's own re-disposition under challenge, not an
independent finding that the six were invalid. What it does establish is that the round had no
declared type and no termination condition, so producing more findings was the only behaviour the
brief rewarded.* Full statement in
`skills/edu-skill-creator/reference/lessons/L24_review_termination.md`.

## 9. Two things this contract does NOT claim

- **That every repeated round is a foundation problem.** Two independent retrospective checks
  examined eight transitions and found zero demonstrable silent descents, with four undecidable. Some
  extra rounds are legitimate expansions of adversarial coverage. Do not diagnose a pathology the
  records cannot support.
- **That this saves tokens.** No per-round cost data exists yet, here or in the published record.
  This contract is justified by defect evidence, not by economy, and saying otherwise would be the
  kind of unearned claim it exists to prevent.
