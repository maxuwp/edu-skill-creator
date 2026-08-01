<!-- Detail for L24. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L24 — Review terminates: a round declares what it may open, and settlement is a state, not a favour

**Rule.** Every review round declares its **type** before it runs, and the type fixes what the round
is allowed to return.

```
full review        — may open new findings across the declared population
disposition check  — may only report whether named prior findings closed and whether the
                     protected baseline held. It may NOT open new findings, except the
                     reopen class below.
targeted check     — may only report pass or fail on the named corrections. Nothing else.
```

**The reopen class, and it is short.** A disposition check may open a new finding only when it is a
critical contradiction between two rules in the artifact, a false approval (a property recorded as
confirmed that is not true), an irreversibility or data-loss risk, or a broken protected property.
Everything else the reviewer notices — missing bindings, richer schemas it would have designed,
fields it would have added — is **backlog**, recorded once and not raised again.

**Settlement is automatic.** When the targeted checks on the named corrections pass, the artifact is
settled. No further general review round is scheduled, and no party has to ask for the loop to stop.
A reviewer that wants a settled artifact reopened must name which member of the reopen class applies.

**Review depth is proportional to the artifact's status, not to the reviewer's appetite.** A
document marked `PROPOSED` and loaded by nothing gets adoption review — is it safe and coherent
enough to try? A document that governs execution gets protocol review — is every field defined, every
transition legal? Applying protocol review to a proposal manufactures findings against a standard the
artifact never claimed.

**Round budget.** An artifact enters review with a declared maximum number of rounds. Exceeding it is
not a reason for another round; it is a signal that the artifact, the brief, or the acceptance oracle
is wrong, and that is a decision for the human who owns the work.

**Failure that taught it, 2026-08-01.** The fixer contract, revision 0: 98 lines, status `PROPOSED`,
loaded by nothing, sent out with five specific questions. The return was six major and three minor
findings plus a larger proposed envelope and eleven acceptance tests — a further revision cycle on a
draft that governed nothing. When challenged, the reviewer withdrew the disposition in full and
settled on **two** local corrections, describing its own error precisely: it had treated a short
proposed behavioural contract as if it were a production protocol.

*What this evidence does and does not support.* It is a single case, and the withdrawal is the
reviewer's own re-disposition under challenge rather than an independent adjudication that the six
findings were invalid. What it does establish is that the round had no declared type and no
termination condition, so producing more findings was the only behaviour the brief rewarded. The
faculty member's judgement of the pattern is the load-bearing evidence here: *"every single time, you
review, find something to pick on, and back and forth. if I don't say stop you two can battle for a
whole year."* The stopping condition was never the reviewer's to invent; it was missing from the
design.

**Why this is not L22 or L19.** L22 governs where a round may look (scope). L19 governs what a round
must return (both halves). Neither says when the loop **ends**, and an unterminated loop with correct
scope and correct structure still runs forever. L24 supplies the terminating condition: a declared
round type, a short reopen class, automatic settlement, and a round budget owned by the human.

**Applies to.** `edu-skill-creator-architecture` (every reviewer pairing declares round type and
round budget), `edu-skill-creator-draft` (review briefs state the type and carry the reopen class),
`edu-skill-creator-test` (round records log the declared type and whether the round stayed inside
it), `edu-skill-creator-release` (a settled artifact is not re-opened for a release without a named
reopen-class member). External reviewers work under
`docs/CONTRACT_reviewer_behaviour_2026-08-01.md` §8, which states this rule in their terms.

**Related.** L19 (the protected baseline a disposition check verifies), L20 (descent is one cause of
extra rounds; over-review is another and they are distinguishable only if the round type is
recorded), L22 (scope pressure is the other thing a round may not absorb), L16 (a finding raised
against a standard the artifact never claimed is an evidence-burden error), L13 (an unwired document
is unenforced, and reviewing it as if it were enforced is the mirror of that mistake).

**Status of enforcement.** Prose only, as of 2026-08-01. No brief declares a round type, no validator
rejects a disposition check that opens findings, and no harness counts rounds against a budget. Treat
an unwired rule as unenforced (L13), and do not cite this lesson as a gate.
