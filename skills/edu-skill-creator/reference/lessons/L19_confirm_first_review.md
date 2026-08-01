<!-- Detail for L19. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L19 — Feedback is two halves; a revision is a modification, never a new draft

**Rule.** Every review brief this system writes — L3's independent reviewers, the Stage 5 skill
reviews, the Stage 6 test findings, the Stage 8 reflect ledger — must require **both** halves,
and the first one is what makes an iterative loop terminate:

1. **Verified properties.** What the reviewer checked and found **correct**. This is not praise.
   It is a **protected baseline**: a do-not-break list that every later round is obliged to keep.
2. **Defects.** Each reported as the **smallest modification that respects that baseline**.

And the corollary, which is the half that actually gets violated: **a fix is an informed
modification of something known good, never a rewrite.** A rewrite discards the properties the
previous version established, which is exactly the mechanism by which one round's fix becomes the
next round's defect.

Where a criterion or artifact will be reviewed more than once, keep a **cumulative regression
ledger**: every case any round established, with its verdict, the round that established it, and
why it is on the list. Enforce it mechanically — a lint check or a test that fails the release —
so a later round cannot fix one case by breaking an earlier one. The ledger's verdict set must
include **ambiguous** and **present-but-not-a-defect**, not only pass/fail. Those two missing
verdicts are where oscillation lives: a case with nowhere to go gets re-decided every round.

**Failure that taught it.** Five adversarial review rounds on `talk-like-a-professor` returned 5,
7, 8, 11 and 10 criticals — increasing, not converging. Every brief defined `critical` as "a
claim is false" or "a defect can slip through"; none asked what had been confirmed right. With no
protected baseline, the same lexical criterion was rewritten wholesale four times, and each
rewrite fixed that round's examples while minting the next round's. The round-5 reviewer
diagnosed the criterion's architecture as the cause. The author's diagnosis was better and was
about method: *"did you just list the violations? did you confirm what is right? a revision can't
be a new draft, it should be a well informed modification."*

The moment a baseline artifact existed in that repo — a heading-case file carrying 25 cases
accumulated across five rounds, enforced by its own release lint — it immediately caught two
regressions that had already shipped unnoticed, each one a property an earlier round had
verified and a later rewrite had silently dropped. (Paths are named without backticks here on
purpose: they belong to the talk-like-a-professor repository, not this one, and a bare
`tests/…` citation would resolve against the wrong tree.)

**Second instance, and what it does and does not show.** This repository ran the same loop five
times, with the brief changed after round 3 and extended once more after round 4. Measured per
fix-set, which is how the early rounds were counted: rounds 1 to 3 reopened a prior property three
times out of three, wholesale; round 4 produced one narrow regression, caught by the baseline
re-verification; round 5's fix-set has had no subsequent round, so its reopening count is
**unobserved**. The qualitative shift is the sturdier claim — rounds 1 to 3 each replaced a mechanism
wholesale and each replacement carried the next defect, while round 5's fixes are narrow in-place
modifications.

Three things changed alongside the brief and are named rather than absorbed: the deterministic suite
grew from 25 to 78 falsifiable cases *before* round 4, so prior fixes were mechanically pinned by
then; round 3 had no external auditors; and three rounds had already swept the older surfaces.
Attribution therefore belongs to the combination, and **the component the record most directly
supports is the mechanised baseline, not the brief's wording.** The same is true of the first
instance: the convergence event there was a baseline artifact coming into existence, not a rewording.
POSED's `strengths`/`preserve_units` enforcement is the worked precedent for feasibility — shipped
and enforced in code — but no measurement of its effect on reopening rates exists, and its contract
is weaker than this one, so "shipped and enforced" is the honest description, not "solved".

The author reports the same pattern across other threads and other AI tools. That is author-reported
and not independently examinable here; the systematic-misreading claim is scoped to the two instances
above plus that testimony, named as testimony. Treat "give me feedback" as read to mean "list the
violations," and correct for it in the brief rather than hoping the reviewer infers it.

**What this method does not fix, and the part that is now bound.** A property confirmed *in error*
becomes protected error, and the ledger will defend it. That risk is no longer only described:
`how_verified` must name a classified mechanism and at least one entry per log must be of a strong
kind (mutation, command, diff, schema), enforced by release lint check 17, and a wrong row leaves the
baseline only through a supersession that demonstrates the original verification was vacuous **as a
mechanism** — re-run the recorded `how_verified` against the case it should have caught and show it
passing — enacted by the human gate, never by an agent. Protected error's likeliest home is the
`present-but-not-a-defect` verdict, which certifies an absence and is the hardest verdict to falsify
by mutation.

**Applies to.** `edu-skill-creator-architecture` (specify the ledger alongside each reviewer
pairing), `edu-skill-creator-draft` (the review brief template and every rubric it authors),
`edu-skill-creator-test` (RED/GREEN findings carry the confirmed set forward),
`edu-skill-creator-reflect` (the harvest ledger records what held, not only what broke).

**Brief language that works.** Put the confirm pass first and make it a deliverable, not a
courtesy:

> Before reporting any defect, record what you checked and found correct, with how you verified
> it. That list is the do-not-break baseline. Then report defects, each as the smallest
> modification that keeps every item on that list true. If a fix would break one, say so and
> propose the trade explicitly rather than taking it silently.
