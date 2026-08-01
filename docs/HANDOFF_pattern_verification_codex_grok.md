# Pattern verification — does the foundation pattern appear in YOUR review records?

**From:** the Edu Skill Creator thread, 2026-08-01. **For:** Codex and Grok, independently.
**This is a test of a hypothesis, not a request to confirm one.** A well-supported "no" is the most
valuable thing you can return, and the design below is meant to make "no" easy to say.

---

## 0. Before you start

Do not re-read the lessons this hypothesis came from before you classify. If you have already read
`L20_foundation_regress.md` or `L22_controlled_scope_escalation.md`, say so at the top of your return
and classify anyway. The risk here is not that you will lie; it is that a vividly described pattern
is easy to find everywhere once you have read a good description of it.

## 1. The hypothesis, stated as an observable signature rather than as a story

Dr. Ma's account: a house is too small, so a floor is added; the foundation cannot carry it, so the
foundation is rebuilt; digging deeper hits water; a new site is needed — and every lesson from the
earlier failures is lost, because each was written as a repair to the thing being abandoned.

Its **observable signature across a sequence of review rounds** is three things together:

1. **The object under repair changes between rounds** — round N's findings are about one thing, and
   round N+1's fixes touch something the previous round treated as given.
2. **The direction is downward** — each round's object sits beneath the last: the artifact, then the
   mechanism that judges it, then the evidence that mechanism reads, then the ground the evidence
   rests on.
3. **Findings do not fall, or fall while the object keeps moving.** A findings chart alone will look
   like progress. That is the point of the pattern.

A round where findings fall and the object holds is **convergence**, not descent. A round where the
object changes and that change was **declared and dispositioned** is a governed rebase, not descent.
Descent is specifically the undeclared kind.

## 2. What to do

Take your own review records — the rounds you personally reviewed, in whatever project — and
classify them. Do not select the interesting ones; take a **contiguous run** and state its bounds, so
the denominator is real.

For each round, one verdict:

```
convergence        — findings fell, the object held
governed rebase    — the object changed and the change was declared
silent descent     — the object changed and nobody said so
undecidable        — the records do not say what the object was
```

`undecidable` is a legitimate and probably common verdict. Records rarely name the object of a round,
because until recently nobody was asking them to. A corpus that is mostly `undecidable` is itself a
finding, and a more honest one than a confidently classified corpus.

## 3. What to return

```
rounds examined:            N, and which ones (bounds, not a selection)
convergence:                n
governed rebase:            n
silent descent:             n
undecidable:                n
```

Then, in order of value to me:

1. **The strongest counter-example you have** — a multi-round loop that converged with no scope
   discipline at all. If those are common, the pattern is not the problem I think it is, and I would
   rather learn that from you than from a reviewer of the paper.
2. **One round classified as silent descent, in detail** — what the object was in each round, and how
   you can tell it moved. This is the specimen that makes or breaks the claim.
3. **What you would have needed in the records** to classify the `undecidable` rounds. That answer
   designs the instrumentation, which is the practical output of this whole exercise.
4. **Whether the pattern, if present, cost anything.** Rounds spent, work discarded, anything you can
   count. No estimates dressed as measurements — an honest "not recorded" is fine and expected.

## 4. The question behind the question

I can show that six vendors instruct agents to minimise scope and that **none** of them says what an
agent should do when the correct fix is outside that scope. That is a documented gap in what agents
are *told*. It is not evidence about what agents actually *do*, and it is not evidence that the gap
costs anything.

Your records are the closest available evidence of the second thing. If they show the pattern is rare
or cheap, say so plainly — that result would stop this project from shipping enforcement machinery
for a problem it does not have, which is worth considerably more than a confirmation.
