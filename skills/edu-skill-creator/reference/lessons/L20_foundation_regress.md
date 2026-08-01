<!-- Detail for L20. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L20 — Foundation Regress: when each fix exposes a constraint one layer deeper, the loop is descending, not converging

**The failure, named.** A review round finds a defect. The fix requires changing something one
layer below the artifact under review. That change exposes a constraint one layer below *it*. The
loop keeps running and keeps producing findings, so it looks like progress, but each round is
working on a different and deeper object than the last. The author's account of it, which is the
canonical statement of this lesson:

> The house is too small, so we add a second floor. The reviewer finds the foundation cannot carry
> it, so we rebuild the foundation. Digging deeper, we hit water. Now we must find a new location
> suited to the deeper foundation, so we restart from location selection — and every lesson from
> the previous failures is lost, because none of them was written down as something the *next*
> location would have to satisfy.

Two distinct failures are joined there, and both must be answered:

1. **Foundation regress** — remediation descends through layers while presenting itself as
   iteration. Cost grows per round while the object under repair keeps changing.
2. **Relocation amnesia** — the lessons are written as repairs to the thing being abandoned, so a
   rebuild inherits none of them and re-earns them at full price.

**Rule.**

1. **A fix that changes a layer below the artifact under review is a re-scope, not a fix.** Stop
   the round. Record the constraint the deeper layer imposes, then re-open deliberately at that
   layer with the protected baseline (L19) carried forward. Rounds that silently change object are
   the mechanism of the regress.
2. **Write every lesson as a constraint on *any* implementation, never as a repair to this one.**
   The test is mechanical: *could this entry be checked against a replacement written from
   scratch?* If it cannot, it will not survive a relocation, and it is a changelog entry
   masquerading as a lesson.
3. **Declare the loop's budget before the first round** — maximum rounds, and the cost of a round.
   Exhausting the budget is a design verdict ("this foundation is not deep enough"), not a failure
   to try harder, and it is reported as such.
4. **Halt on no progress.** If round *N* returns no fewer findings than round *N−1*, and any of
   them is a regression of a property an earlier round verified, do not run round *N+1*. Re-derive
   the constraints instead. More rounds against a descending loop buy depth, not convergence.
5. **The party that finds a defect does not author its fix in the same pass.** Bad-fix injection
   rises with the fixer's familiarity with a dense module, which is precisely the person a review
   loop hands the repair to by default.

**How to detect it early.** Three signatures, none of which requires waiting for the loop to fail:

- The layer touched by each round's fix is monotonically lower (content → mechanism → the evidence
  the mechanism reads → the ground that evidence rests on). Record the layer per round; L14 already
  supplies the vocabulary for naming it.
- Findings per round are flat or rising rather than falling.
- Round *N* fixes a defect that round *N−1*'s fix introduced.

**Failure that taught it.** A validator audit ran three rounds and returned roughly forty findings.
Reviewed as one population rather than as three rounds, nearly all of them reduced to a single
defect shape — a value asserted by an agent being checked against another value the same agent
asserted — and the rounds had been descending through it: the artifact, then the mechanism that
judged the artifact, then the evidence that mechanism read. The loop was not finding forty defects.
It was finding one defect forty times, at successively deeper layers, and paying full price each
time. The regression ledger in that project recorded properties of the build and cases against the
build; neither would have survived replacing it, which is relocation amnesia stated exactly.

In this repository the same loop was run five times under a brief that carried the previous round's
verified properties forward (L19). Findings stopped reopening prior fixes after the brief changed,
and the suite grew from 25 cases to 104 — each fixed defect converted into a permanent falsifiable
case, which is what "a constraint that survives the rebuild" looks like mechanically. That is the
positive control for rule 2.

**How we will know it is solved.** The claim behind this lesson is economic, so it needs a metric
rather than an impression. Per review loop, record: rounds run against the declared budget; findings
per round; the share of findings that are regressions of previously verified properties; the layer
each round's fix touched; and the cost of a round. Convergence is *findings falling while the layer
stays fixed*. Descent is *findings flat or falling while the layer drops* — which reads as progress
on a findings chart alone, and is the reason the metric needs the layer column.

Stated honestly: this repository records rounds, findings and reopened-fix counts, and it does not
yet record cost per round or layer per round. Until it does, the token-cost claim is a well-founded
expectation rather than a measured result, and it should not be reported as measured.

**Applies to.** `edu-skill-creator-architecture` (declare the loop budget and the finder/fixer split
alongside each reviewer pairing), `edu-skill-creator-test` (RED/GREEN rounds record layer and
findings, and halt on no progress), `edu-skill-creator-reflect` (the harvest states constraints on
any future implementation, not repairs to this one), `edu-skill-creator-release` (a loop that
exhausted its budget is a release-blocking design verdict, not a warning).

**Related.** L19 supplies the protected baseline that stops one round from undoing another — the
necessary partner, since a loop cannot converge on ground it keeps re-breaking. L14 supplies the
layer vocabulary this lesson counts in. L16 governs how much evidence a claim at a given depth
requires. The circular-evidence lesson scoped as L21 explains why the descent so often terminates in
the evidence layer rather than in code.

**Status of enforcement.** Prose and metric definition only, as of 2026-07-31. The stage-body wiring
and the ledger columns above are specified here and not yet mechanized; treat an unwired rule as
unenforced (L13) and do not cite this lesson as a gate.
