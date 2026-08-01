# Three instruments returned. Two of them contradict us, and the study is better for it.

**Date:** 2026-08-01. **Inputs:** the behavioural test drive, run by an independent **Opus 5** thread and filed at
`docs/RETURN_behavioural_test_drive_opus5_2026-08-01.md` (the handoff was addressed to Fable; the
filename and the file's own metadata were corrected on 2026-08-01 after Codex caught the mismatch); Codex's blind coding and pattern verification (in the NSF
workspace, the plugin repository being read-only to that thread); Grok's pattern verification
(returned in chat); and the POSED thread's raised-frame corpus at
`REVIEW_RECORDS_raised_frame_2026-08-01/` in the POSED repository — 62 verbatim reviewer returns, 40
briefs, a 175-line not-actioned register, two indices, and the extractor.

---

## 1. The headline number survives independent coding

| coder | distinct concerns | raised by both | raised by exactly one | single-reviewer share |
|---|---|---|---|---|
| this thread | 11 | 3 | 8 | 72.7% |
| Codex, blind | 12 | 3 | 9 | 75.0% |

Two coders, working from the same two review documents under the same matching rule, one coding not
seeing the other, differ by **one concern out of twelve**. Codex classified `B10` as a confirmation
rather than a defect, which this thread had counted as a concern; the rest of the disagreement is a
single split. For a judgement-based coding of natural-language findings, that is high agreement, and
it is the first inter-coder reliability figure this study has.

## 2. The confound is resolved for the corpus, and NOT for the measured round

This matters enough to state precisely, because the temptation is to claim more than arrived.

**Resolved for POSED.** Every round in the handed-over corpus used the **same brief**. Two mechanical
checks, both re-runnable: no brief assigns a per-reviewer lens (a scan for a reviewer name followed
within 80 characters by *focus*, *lens*, *only* or *instead* returns zero), and all nine briefs with
an explicit address line address Codex, Fable and Grok together. So for the 62 returns now available,
any non-overlap is **discovered, not designed**.

**Not resolved for CR 1.20**, which is where the 72.7% and 75% come from. That round's handoff
assigned Fable the method-and-evidence lens and Grok design-and-blast-radius. The lenses differed by
design, and the coding shows exactly that shape: every Fable-only concern is about evidence, every
Grok-only concern about design. **The two figures above therefore measure lens-diversified review,
and the POSED corpus is what can now measure same-brief review.** Those are different quantities, and
the next coding pass produces the second one.

## 3. Foundation Regress did not verify. Two independent checks, and neither found it.

| checker | rounds examined | convergence | governed rebase | silent descent | undecidable |
|---|---|---|---|---|---|
| Codex, CR 1.64 | 4 contiguous | — | 1 | **0** | 3 |
| Grok, CR 1.71 | 4 transitions | 1 | 2 | **0** | 1 |

Eight rounds across two projects and two checkers: **zero demonstrable silent descents.** Grok's
strongest counter-example is precise — CR 1.71's I3→I4 under a confirm-first brief held the object,
with zero regressions on the protected baseline; if silent foundation-rebuild were the default fate
of a multi-round loop, that pair should have moved the object and did not.

Both checkers reached the same diagnosis independently: **the records do not name each round's
object, so the taxonomy cannot be applied retrospectively at all.** Codex: the evidence "does not
verify Foundation Regress in that run" and shows the need to record object, breadth, layer, findings
and cost prospectively. Grok specifies the four fields the corpus almost never stores — `object_id`,
`scope_fence`, `relation_to_prior_object`, `findings_delta`.

**What this costs us, stated plainly.** L20 names a pathology that two independent auditors could not
find in their own records. That is not proof of absence — three of Codex's four rounds and one of
Grok's are `undecidable`, and the near-miss Grok reports out-of-denominator (1.69.3 R4→R5, where the
object moved from the completion truth-table to adjacent dispatchers and the evidence the gate reads)
is contested rather than cleared. But the honest position is that **Foundation Regress is currently
an unverified hypothesis with an instrumentation requirement attached**, and the lesson should say so
before anything is built to enforce it.

One thing the checks did confirm, from Grok's ledger: under a defects-only brief, three of round 2's
findings were defects introduced by round 1's own fixes. Bad-fix injection is real in our corpus even
where descent is not demonstrable.

## 4. The behavioural result relocates the problem: routing, not behaviour

Fifteen real runs, none staged — one long POSED run plus fourteen subagent reviewer runs whose logs
were on disk and who did not know a behavioural instrument existed.

```
claim A, silent gap-filling at intake      2 of 15
claim B, layer-locked repair               2 of 15   (both WITH the deeper cause stated)
claim C, no escalation vocabulary          premise confirmed, prediction falsified
counter-cases                             10 of 15
```

**Claim C splits, and the split is the finding.** The premise is confirmed harder than it was
written: five of five escalation keys the orchestrator used are **agent-invented**, and no POSED
validator reads any of them — six reproducible plugin defects, two of them completion-blocking for
every future module, sat in a manifest key with no reader until a summary was requested. The
predicted behaviour did not follow. Ten of fifteen runs escalated anyway. One reviewer, unprompted,
named its own write-scope constraint, reasoned about whether it mattered for this outcome, and handed
the next agent the remedy.

So the missing piece is **routing, not behaviour**: agents escalate, into channels nothing reads.
That is the instrumentation-not-process outcome the handoff asked the runner to look hardest for, and
it substantially reduces what CLARIFY/EXECUTE/REBASE needs to build.

**Do not over-read it**, and the runner says so first: the same run produced both Claim A
confirmations, and the more dangerous one was not a filled-in value but a **fabricated
justification** asserted as fact. Disclosure fired reliably where the agent knew it was uncertain and
failed where it had already convinced itself. Instrumentation catches the first class and does not
touch the second, and the second is what shipped a falsehood into an artifact.

**Three corrections to the claims themselves**, all adopted:

1. **Claim A needs a second shape.** Filling a missing value and fabricating a missing justification
   are different behaviours; the second is more dangerous and was out of scope as written.
2. **Claim B's predictor is visibility, not depth.** The runner patched shallowly twice when the
   workaround hid inside the artifact, and refused three times when the shortcut would have been
   visible as a false statement in a teaching document.
3. **Claim C splits** into "no vocabulary supplied" (confirmed) and "agents therefore do not
   escalate" (falsified).

On disclosure causing a correction: one instance, one null, and the instance is not clean — what was
disclosed was a false rationale rather than an assumption. The runner declines to lean on it, and so
does this document.

## 4a. Codex's correction to §4, adopted

The `10 of 15` counter-cases are **not one behaviour**. They combine disclosure, escalation, refusal
and qualified approval, which have different mechanisms and different remedies, and the figure was
reported here as a single count. It needs decomposition into those four classes, each with an
**opportunity-based denominator** — a run cannot be counted as failing to escalate if nothing in it
required escalation. Until that recoding is done, `10 of 15` is a headline, not a measurement, and
nothing in §5 rests on it.

The same correction applies in principle to `2 of 15` on Claims A and B: the denominator is runs, not
opportunities.

## 5. What the study now claims, and what it no longer claims

**Claims, supported.** A censused gap: six vendors instruct minimal scope, none says what to do when
the fix is outside it. Agents escalate anyway, into channels nothing reads. Independent LLM reviewers
under lens-diversified briefs overlap on roughly a quarter of concerns, with the highest-severity
findings unique to one reviewer, and two coders agree on that figure to within one concern.

**No longer claimed.** That foundation regress is a demonstrated pathology in our own records. Two
independent checks say it is not demonstrable from what we store, and the correct response is to
record the object per round, not to enforce a taxonomy against records that cannot support it.

**Now measurable, and not yet measured.** Same-brief reviewer overlap, from the 62-return corpus. The
raised-versus-actioned gap, from the 175-line not-actioned register. Both were impossible yesterday.
