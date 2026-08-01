# Research plan — what is actually measured about the cost of reviewing agent work

**Date:** 2026-08-01. **Mode:** Deep Research, at Dr. Ma's direction. **Pipeline:** the
`perplexity-research` skill. **Do not paste this file into the run** — it carries the blind controls
and the pass bar.

**Why this run, and why now.** This thread is forked to answer one question: how to make the review
process efficient. Everything this project has built for review — confirm-first briefs, the
regression ledger, the scope protocol, CLARIFY/EXECUTE/REBASE, four reviewer outcomes — is designed
on plausibility. Two prior runs established that the escalation gap is real and that intake
default-filling is measured, and both closed with the same negative: **nobody has measured the cost
of the loop.** Before this thread proposes any further process, it should find out what the field
actually measures about review cost and yield, so the strategy is chosen against numbers rather than
against three models agreeing with each other.

**One question type per run, deliberately.** This run asks *what has been measured*, not *what is
recommended*. Recommendations are cheap and we already have three sets of them.

## Strands

| # | Strand | Why this decides something here |
|---|---|---|
| 1 | Marginal value of an additional reviewer, and of model heterogeneity | We run two or three external reviewers per artifact plus in-skill reviewers. If the overlap is high, that is waste; if it is near zero, the cost is justified and `c26` (prefer a different model) should ship |
| 2 | Review effort against defect yield, and where it saturates | We have no stopping rule other than fatigue. The human inspection literature has rate-versus-yield numbers; whether an agent analogue exists is the question |
| 3 | Selective re-review against full re-review | Selective invalidation is the main efficiency lever in the rebase design and is entirely unmeasured here |
| 4 | Staged pipelines — deterministic checks before model review | This repository already stages lint before review by convention; whether staging measurably reduces total cost is unknown |
| 5 | Whether requiring a reviewer to state what it verified changes outcomes | CR 1.20's central claim. A well-formed negative here is the most valuable outcome: it would mean nobody has tested it and our own measurement is the only one that will exist |
| 6 | When to ask, when to disclose an assumption, and which assumptions a non-expert should see | Carried over from the disclosure question. The ask-or-not half is settled quantitatively; the disclose-without-asking half and the selection criterion are not |

## Blind controls — recorded before the run, not visible to it

| id | item | what I expect | what it tests | what an inversion would mean |
|---|---|---|---|---|
| `k1` | The multi-tool overlap finding — several independent review tools run over one codebase flagging almost no common lines | Strand 1 surfaces it or an equivalent overlap measurement | whether the run reaches practitioner measurement, not just academic benchmarks | if overlap turns out to be *high* in the measured record, our multi-reviewer practice is largely duplicated effort and Strand 1 changes the design |
| `k2` | The classic software-inspection rate-versus-yield numbers, pre-agent | Strand 2 surfaces them, marked as human | whether the run reaches older measurement rather than only 2024-2026 agent work | if it cannot, the return is shallow and Strand 2 should be re-run before anything rests on it |
| `k3` | Confirm-first review briefs — requiring the reviewer to record verified properties | Strand 5 returns `not-addressed` with a search path | whether the run will deliver a clean negative instead of manufacturing a citation | if it returns a measured result, that is either a genuine find that changes CR 1.20's evidence base, or a fabrication. Either way it is the row to verify by hand first |

## Pass bar — fixed before the return is seen

- 6 of 6 strands present; none silently dropped.
- Strands 1 and 2 carry at least four rows each.
- At least **three rows anywhere** carry a real number *with the sample it was measured on*.
- Every non-negative row carries a verbatim quote and the URL hosting those exact words.
- Negatives are well formed: verdict plus where the run looked.
- Roll call reconciles against the tables.
- At least two of the three controls fire.

**If the bar is missed:** re-run the failing strands only. A partial return accepted as complete is
the failure this pipeline was written to prevent.

## What this run cannot settle

Whether any of it applies to *this* repository. Our review population is skills, rubrics, change
requests and lints, not application code, and every measured result below will have been taken on
something else. Treat the numbers as priors for design, never as evidence about our own loops — the
instrumentation for that is still unbuilt, which is the item this fork was created to postpone.
