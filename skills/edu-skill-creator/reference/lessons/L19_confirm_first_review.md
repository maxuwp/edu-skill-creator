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

The author reports the same pattern across other threads and other AI tools, so treat "give me
feedback" as **systematically** read to mean "list the violations," and correct for it in the
brief rather than hoping the reviewer infers it.

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
