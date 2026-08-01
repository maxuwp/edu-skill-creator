# Canonical design record — CLARIFY / EXECUTE / REBASE

**Status:** design record, 2026-08-01. Not implemented. This file is the **single source** for the
loop contract: the three states, the reviewer outcomes, the packet shapes, and the settlement test.
Lessons state why; the reviewer procedure states how; neither restates what is defined here (L7).

**How it was produced.** Four independent contributions, reconciled here rather than merged silently:

| Source | What it contributed | What survived unchanged |
|---|---|---|
| This thread's research run | The empirical base: six vendors instruct minimal scope and **none** tells the agent what to do when the fix is outside it; intake default-filling is measured; two load-bearing negatives | All of it; see `docs/FINDINGS_ai_scope_control_2026-08-01.md` |
| Grok, dual-mode loop proposal (in the POSED repository, docs/PROPOSAL_dual_mode_review_loop_2026-08-01.md, cited without backticks because it is another repository's path) | The **harness stop** — do not tell the implementer to ignore minimal scope, stop calling the implementer; settlement is converged or escalated, never fatigue; mode tokens in the task header; constraints that survive a rebuild | Harness stop, settlement definition, header block |
| Codex | Intake assumption audit; **foundation-first review order**; dependency graph in place of a single layer ladder; three reviewer outcomes; **selective invalidation**; removal of the one-descent reserve | All adopted |
| Dr. Ma | **Rebase, not restart.** A new foundation must be chosen using every requirement already gathered, including the ones discovered while building on the wrong one, and prior work is carried across rather than re-earned | The governing principle of the REBASE state |

**What this replaces.** L20 stands as the pathology lesson. L22 is amended, not rewritten — its
declared-scope requirement and its graded response survive; its scan-order rule, its one-descent
reserve, and the breadth of its authority table do not. The reviewer procedure in
`skills/edu-skill-creator/reference/review_scope_protocol.md` becomes the operational half of this
record.

---

## 1. Why the human answer was the wrong shape

The first design was change control: declare a boundary, grade an expansion by impact, route it to
an authority. That governs expansion **after** a defect is found. For an agent the causal chain
starts earlier and is closed differently:

1. The request is underspecified. The agent fills the gaps with defaults **silently**, and the
   foundation defect is created there. Measured: agents guess unspecified requirements about 41% of
   the time, and underspecified prompts are twice as likely to regress across model or prompt
   changes.
2. Standing instructions then say make the smallest change and do not disturb working code. Four of
   six major vendors state this explicitly in their own documentation.
3. **No vendor documents what the agent should do when the correct fix is below that scope.** The
   sharpest illustration is Amazon's: when the diff grows past five files, the instruction is that
   *the human* should reduce the feature description. The agent is given no move.
4. So the loop stays at the surface, and each round repairs a different, deeper object while looking
   like iteration.

An agent cannot decide on its own that a standing constraint should not apply this time, and asking
it to weigh a scope rule against a task goal produces either paralysis or incoherence. The fix is
therefore **architectural, not rhetorical**: change which state the system is in, rather than asking
one agent to reinterpret its own constraints.

## 2. The three states

```text
OUTER   CLARIFY  -> establish and approve the foundation before drafting
        REBASE   -> choose a new foundation from everything already learned, and migrate
INNER   EXECUTE  -> minimal, ledger-safe work inside the approved foundation
```

**EXECUTE is not loosened.** Minimal change, protected baseline, confirm-first review, mutation
re-proof. Everything L19 requires still holds. The contract does not ask an implementer to violate
its own discipline; it stops calling the implementer.

### 2.1 CLARIFY — the state that did not exist

Before the first draft, an assumption audit is produced and approved:

```text
explicit_requirements:
inferred_assumptions:
foundation_choices:
unresolved_decisions:
acceptance_evidence:
protected_existing_work:
non_goals:
```

Each inferred assumption is triaged, because clarification is not free:

```text
assumption:
impact_if_wrong:  low | high
reversibility:    easy | difficult
evidence:
action:           accept_default | clarify | explore_read_only
```

A low-impact, easily reversible default may be **adopted and disclosed**. A high-impact or
hard-to-reverse assumption must be clarified, or explored read-only, before it is adopted. The
triage is the point: blanket "always ask" is expensive, and the published scaffold that works is
selective — it "conserv[es] queries on simple tasks while proactively seeking information on more
complex issues", reaching a 69.40% resolve rate on an underspecified benchmark.

### 2.2 REBASE — rebase, do not restart

This is the state the first two proposals got wrong, in the same direction: both described the
outer loop as *replan*, which reads as beginning again. A new foundation is not a blank sheet.
**Every prior decision is protected by default and must be given a recorded disposition.**

Dispositions are recorded on **two axes**, because what a requirement *means* and what *happens to
it* during migration are different questions and conflating them was a defect in the first version of
this record:

```text
semantic_role:          need | outcome | preference | constraint | solution | workaround | assumption
migration_disposition:  preserve | adapt | retire_workaround | invalidate | hold_pending_clarification
```

The category the first version was missing entirely is **`workaround`**: a solution adopted only
because of a limitation in the *old* foundation. Carrying one forward is not preservation, it is
importing the old foundation's defect into the new one.

```text
# the same expressed request, two different underlying needs
expressed: "many lighting fixtures"   need: brightness, windows are small
  semantic_role: workaround           migration_disposition: retire_workaround
expressed: "many lighting fixtures"   need: decorative character
  semantic_role: preference           migration_disposition: preserve
```

Nothing in the artifact distinguishes those two rows. Only the person who asked can.

**Unknown does not mean active.** When a requirement's role is genuinely undetermined, the
disposition is `hold_pending_clarification`: the item stays in the lineage and is neither deleted nor
built. "Carry it forward and flag it" is not good enough, because carrying an unresolved requirement
forward *as active* still builds the twelve-lamp house on the bright lot. If work must continue
before the answer arrives, take the **most reversible** option — provide for the possibility
structurally, defer the commitment — and record that the reversibility was chosen deliberately.

Two consequences that are the whole point of doing this with an agent rather than a project manager:

- **The new foundation is chosen using the requirements discovered while building on the wrong one.**
  Needs surfaced during structural, functional and detail work are inputs to the new choice, not
  casualties of it. An agent holds the entire history and can consume all of it at once; a human
  team re-derives it. Not using that is the waste.
- **A rejected alternative is still knowledge.** Invalidated work survives as a candidate, a
  constraint, a preference signal, or a negative example, and is recorded as such rather than
  deleted.

**No artifact is regenerated merely because its upstream foundation changed.** Regeneration requires
a demonstrated incompatibility, not a changed ancestor.

## 3. Reviewer outcomes, and the harness stop

Every reviewer in this system and every external reviewer returns exactly one of:

```text
PASS | REVISE_LOCAL | CLARIFICATION_REQUIRED | REBASE_REQUIRED
```

`CLARIFICATION_REQUIRED` means the foundation may well be sound, but a **load-bearing need is
ambiguous** — typically because an expressed requirement could be a preference or a workaround and
the artifact cannot tell you which. It is a distinct state from `REBASE_REQUIRED`, which means the
clarified need has shown the current foundation to embody a workaround, a wrong assumption, or an
unnecessary compromise.

`REBASE_REQUIRED` is **not advice to the current implementer**. The harness ends the execution task
and opens a separate, read-only rebase task. That is what makes this an architecture rather than an
etiquette: the implementer is never asked to hold two contradictory laws at once.

Prompt precedence alone does not achieve this. A task instruction can outrank a repository
instruction file, but it cannot override a system or developer instruction, so a rule that tries to
license an agent out of its own scope constraint is unreliable. A separate state is reliable.

## 4. Review order — foundation first, breadth second

The earlier procedure required a complete horizontal scan before any finding was written. That is
wrong in the case that matters most: once a foundation assumption is demonstrably invalid, reviewing
its descendants produces findings that will be discarded.

1. Test the **foundation assumptions and the acceptance oracle** first.
2. If either fails, **stop the detailed review** and emit one consolidated rebase packet.
3. If the foundation holds, complete the horizontal scan across the declared breadth.
4. Report confirmed-correct properties first (L19).
5. Report all local findings together, each as the smallest modification naming what it must not
   disturb.
6. Re-review only changed and dependency-affected units.
7. Run the full regression suite once, at settlement.

## 5. When to emit REBASE_REQUIRED

- An accepted foundation assumption is contradicted.
- The acceptance evidence cannot establish the intended outcome at this layer.
- The correct fix changes architecture or intended behaviour.
- The impact cone crosses the approved object boundary.
- A previously confirmed property would have to be sacrificed.
- The same defect shape reappears after one local repair.
- Execute rounds are exhausted with findings not falling while the object holds.

**Escalation is decided on the dependency and impact graph, not on a layer ladder.** Layer labels
(content, mechanism, evidence-operand, ground, harness) remain useful for *reporting* what moved, but
they are a diagnostic vocabulary, not the decision rule: a control plane such as the release lint is
not simply "deeper", and real defects travel laterally through shared dependencies as often as they
travel down.

## 6. The rebase packet

One shape, defined here only.

```text
invalidated_foundation:
evidence:
new_requirements_discovered:
complete_prior_decision_inventory:
carry_forward_unchanged:
carry_forward_as_constraints:
adapt_to_new_foundation:
invalidate_with_evidence:
rejected_alternatives_and_reasons:
affected_dependency_cone:
confirmed_unaffected:
new_foundation_candidates:
migration_plan:
re_review:
reuse_without_review:
do_not_break:
faculty_decision_needed:
```

**Test every constraint before it enters the packet:** could this be checked against a replacement
written from scratch? If not, it is a changelog entry, not a constraint (L20 rule 2).

**The rebasing agent receives the accumulated history** — the conversation, prior artifacts,
decisions, evidence and review findings — not merely the latest defect report. Compression into a
structured decision graph is allowed; compression that loses the user's reasoning or requirements is
the amnesia this contract exists to prevent.

## 6a. Requirement lineage, and the provenance that keeps it honest

A requirement is not a string. It is a chain, and only the chain lets a later agent tell an end from a
means:

```text
underlying need  ->  desired outcome  ->  constraint or preference  ->  chosen solution
                 ->  compromise or workaround  ->  current artifact
```

Each significant requirement carries a record:

```text
expressed_request:
semantic_role:          need | outcome | preference | constraint | solution | workaround | assumption
underlying_need:
rationale:
status:                 inferred | observed | user_confirmed | derived
source_reference:
confirmed_by:
confirmed_at:
decision_id:
confidence:
migration_disposition:
```

**An inference must never silently become `user_confirmed`.** A `user_confirmed` status points at the
actual interaction or the stamped decision that established it. Without that rule, an agent's own
guess about what the faculty member wanted is read three rounds later as the faculty member's stated
requirement — which is the circular-evidence failure reserved as L21, arriving in a new place. The
`status` field is what makes the laundering visible.

## 6b. Asking well: the question is part of the design

Review rounds are the natural place to discover a need, because the artifact is finally concrete
enough to argue with. The reviewer must not silently reinterpret a request; it asks, and the answer
becomes a durable lineage update every later agent receives.

Each question is written with its consequences attached, which is also the test of whether it is worth
asking:

```text
question:                 If daylight were sufficient, would you still want these fixtures?
decision_if_yes:          preserve as an aesthetic preference
decision_if_no:           classify as a workaround, reconsider during rebase
affected_design_elements: window design, electrical layout, fixture procurement
```

If neither answer changes a decision, the question is not load-bearing and is not asked.
Counterfactual form works best, because it separates the end from the means in one sentence: *would
you still want X if the limitation that produced it were gone?*

**One to three questions per interaction is the default, not a cap.** If more than three load-bearing
ambiguities remain, the reviewer pauses and schedules another clarification gate rather than guessing
the rest. The bound exists because clarification is not free; the escape hatch exists because
guessing is how the foundation defect is created in the first place.

## 7. Settlement

A loop is settled only as one of:

- **Converged** — findings falling or zero, the object holding across the last two execute rounds,
  the protected baseline re-proved, acceptance green.
- **Rebased** — a rebase packet accepted and a new loop opened on the new foundation.
- **Design verdict** — the foundation cannot satisfy the invariant, recorded as a conclusion rather
  than as a failure to try harder.

"Many rounds were run and everyone is tired" is not settlement.

**A rebase is complete only when** every prior decision has a recorded disposition on both axes;
unchanged work is demonstrably preserved; adapted work is faithful to its original purpose;
invalidated work carries the evidence for why it could not survive; every `retire_workaround` names
the limitation that no longer holds; every `hold_pending_clarification` item is either resolved or
explicitly deferred with the reversible option that was taken in the meantime; the new foundation
accommodates both the original and the later-discovered requirements; and nothing was regenerated
merely because its upstream changed.

**The acceptance test for the whole requirements-discovery half**, stated so it can fail: take one
expressed request whose underlying need is ambiguous, hold the artifact text constant, and vary only
the human's answer. The migration decisions must differ — `retire_workaround` under one answer,
`preserve` under the other — and must differ **only after** the clarification, never before. The
lighting pair is the standing fixture for this. A system that produces the same migration decision
under both answers has not implemented this section; a system that produces different decisions
without having asked has implemented something worse. **Not mechanised as of 2026-08-01:** this is a
process test with no runner, and saying so is the L13 discipline.

## 8. Authority

| Decision | Who |
|---|---|
| Adopt and disclose a low-impact reversible default | the agent |
| Clarify a high-impact or hard-to-reverse assumption | the faculty member, in CLARIFY |
| Local revision inside the approved foundation | the agent |
| Technical boundary adjustment with no change to intent, approved decisions, risk or cost | the agent, recorded |
| Accept a rebase packet | the faculty member |
| Change pedagogical intent, an approved decision, the risk posture, or the cost envelope | the faculty member |

The earlier authority table was too human-heavy. Faculty authority attaches to intent, approved
decisions, risk and cost, not to every technical boundary adjustment.

## 9. Instrumentation — what makes any of this measurable

Three **orthogonal** axes per round. They are kept separate on purpose: a round can fail on the first
and succeed on the second, and collapsing them would let a descending loop relabel itself as
discovery.

```text
artifact_convergence:      findings_opened, findings_closed, regressions
requirements_resolution:   load_bearing_unknowns_opened, load_bearing_unknowns_resolved,
                           needs_confirmed, workarounds_identified
foundation_transition:     stable | governed_rebase | silent_descent
```

Also record per round: round id, state, object, declared breadth, dependency-cone size, artifacts
carried forward versus adapted versus regenerated, clarification count, and token or dollar cost
where available.

**`silent_descent` is the pathology; `governed_rebase` is not.** The difference is entirely whether
the foundation change was declared and dispositioned, which is what makes the distinction observable
rather than a matter of intent.

Without these columns, L20's convergence-versus-descent test cannot be run and the cost claim cannot
be checked. This is the single largest gap between what this design asserts and what this repository
can currently observe.

## 10. What is not established

- **That any of this saves tokens.** No published source measures the cost of iterative repair
  loops, and none measures whether constraining an agent to a minimal change raises or lowers its
  resolution rate. The minimal-scope convention is, on the published record, untested.
- **That minimal-diff discipline caused our own loops.** Every finding above is about what others
  publish. Our claim rests on transcripts and on instrumentation that does not exist yet.
- **The two figures Codex cited for the clarification scaffold** (a 61.2% baseline and a doubling of
  inference cost) are not in that paper's abstract; the selective-clarification conclusion is
  supported by a different sentence in the same abstract. Do not carry those numbers into a lesson
  until the full text is checked.
- **Budget defaults.** The retry and replan caps in the dual-mode proposal come from one system's
  configuration, not from a measurement of ours. Adopt them as starting conventions, labelled.

## 11. Consequences for existing artifacts

| Artifact | Change |
|---|---|
| L20 Foundation Regress | **definition of convergence unchanged, on purpose.** The three-axis metric is added *beside* it, not folded into it: an earlier proposal of mine would have admitted "discovery" as a third convergence category, which would have let a descending loop relabel itself. Its enforcement path is this record |
| L23 Requirement lineage | new lesson: preserve confirmed needs and preferences, reconsider solutions and compromises, hold ambiguous requirements without deleting or enforcing them |
| L22 Controlled scope escalation | **amended**: scan order corrected to foundation-first; one-descent reserve removed as unevidenced; escalation decided on the dependency graph with layer labels demoted to reporting; authority narrowed; CLARIFY and REBASE added. Its declared-scope requirement and graded response survive |
| `skills/edu-skill-creator/reference/review_scope_protocol.md` | becomes the operational procedure implementing this record, and stops defining packet shapes |
| The dual-mode proposal in the POSED repository | keeps its analysis; its contract section defers to this record, so one contract exists rather than two |
