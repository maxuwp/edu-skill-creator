# Review efficiency — what is measured, and the strategy that follows

**Inputs:** `docs/RESEARCH_review_efficiency_perplexity_2026-08-01.md` (the return, filed verbatim),
`docs/RESEARCH_PLAN_review_efficiency_2026-08-01.md` (controls and pass bar, written first).
**Status:** findings and a proposed strategy. Nothing implemented.

---

## 1. The return missed the bar, and that has to be said first

| bar item | result |
|---|---|
| six strands with content | **met** — 5/5/4/7/2/9 rows, 32 total, none dropped |
| Strands 1 and 2 carry four rows each | **met** |
| three rows anywhere with a number **and** its sample | **met** — twelve by its own count |
| verbatim quote plus hosting URL on every non-negative row | **met** as claimed, 32 of 32 |
| no blog, summary site or aggregator standing as a source | **FAILED** — nineteen of thirty-two rows are `secondary`, and the entire numeric block in Strand 4, the strongest evidence in the return, was read from a paper-summary site rather than the paper |
| roll call reconciles | **met except the last line**, which it left unanswered — the verdict-versus-prose check |
| two of three blind controls fire | **FAILED** — one fired cleanly, one partially, one not at all |

**Controls, in detail, because they say how much weight the rest can carry.** The prediction that
Strand 5 would return a clean negative **fired exactly**: two `not-addressed` rows with databases,
search terms and next queries named. The classic human inspection study was *located* (2500 reviews,
3.2 million lines at Cisco) but its rate-versus-yield number was not extracted, so that control only
half fired. The multi-tool overlap finding was **not** surfaced at all, which is the same weakness the
first Deep Research run showed: it reaches published work and does not reach practitioner
measurement.

**Consequence for use.** The Strand 4 numbers are directionally usable and individually unverified —
they carry the canonical arXiv URL beside the summary site, which is the labelled-secondary contract
working as designed, and any of them that becomes load-bearing must be opened at source first.

**One process finding worth keeping.** The Deep Research run terminated at the compile boundary: it
completed fourteen steps, wrote "Enough material gathered. Now let me compile the full evidence table
report", and produced no table at all. The material was in its context and the delivery failed. The
recovery that worked, at no further Research cost, was a follow-up **in plain Search mode** telling
it to compile from what it had already gathered. That belongs in the research skill's lessons.

## 2. What the return establishes

**The two most decision-relevant results are negatives.**

- **Nobody has measured whether requiring a reviewer to record what it verified changes anything.**
  Strand 5, both rows, with search paths. This is CR 1.20's central claim, and it is untested in the
  published record. Our own measurement would be the first of its kind.
- **Nobody has measured LLM reviewer overlap or inter-rater agreement on the same artifact.** Strand
  1. So running two or three external reviewers has no external evidence base either supporting or
  refuting it — while this project has been generating exactly that data informally for a week.

**The one place with hard numbers points in a single direction: put the cheap deterministic check
first.** In an industrial static-analysis setting, false positives were "76% of the filtered
dataset", each false alarm cost "10-20 minutes of inspection", and hybrid LLM-plus-static-analysis
methods "eliminate 94-98% of false positives while maintaining high recall (0.86-0.88)" at "2.1 to
109.5 seconds" and "$0.0011–$0.12" per alarm. Read through a summary site, so directional; but the
ratio between minutes of human attention and seconds of machine attention is not a subtle effect.

**Selective re-review has a measured human-era analogue.** Safe regression test selection is
"100 percent inclusive", and under stated conditions selection techniques have "fault-detection
abilities equivalent to those of the retest-all approach", though cost-effectiveness "vary[s] widely
based on a number of factors". That is real support for selective invalidation — with the caveat that
*safe* is a technical property of the selection algorithm, not a general licence to narrow.

**Three further negatives, all well formed.** No measured saturation curve for repeated LLM review
rounds. No measurement that disclosure alone, without a question, causes a user to catch a wrong
assumption. No validated rule for which assumptions to surface to a non-expert. The disclosure
question is therefore not merely unanswered by me; it is unanswered by the field.

## 3. The strategy

Five moves, ordered by the strength of the evidence behind them.

**1. Move work down the cost ladder, and treat a review finding that a check could have caught as a
defect in the checking, not a win for the review.** This is the only strand with strong numbers
behind it, and this repository already has the mechanism: the release lint is the cheap deterministic
filter. The rule to adopt is that **every audit finding that a lint could have made becomes a lint
check in the same release**, which is what happened across 1.15 to 1.19 by instinct and should be
policy.

**2. Spend reviewers only on what a deterministic check cannot do.** Scope and foundation
(L20/L22), needs versus means (L23), evidence provenance (L21), and pedagogical judgment. Those are
irreducibly judgmental. A reviewer asked to check formatting, path resolution, or arithmetic is a
reviewer spent at the wrong rate.

**3. Make selective re-review the default, and make the "safe" property explicit.** Re-review the
changed unit plus its dependency cone; record what was deemed unaffected and why. The rebase packet
already carries `confirmed_unaffected` and `re_review` fields; this makes them load-bearing rather
than decorative. The measured caveat travels with it: selection is safe only under stated conditions,
so the conditions must be stated.

**4. Measure our own reviewer overlap, because nobody else has.** The data already exists: three
independent reviewers on CR 1.20, on L20, and on L22. Computing how many findings were raised by
exactly one reviewer is a small, cheap, honest measurement, and per Strand 1 it would be the first
published figure of its kind. It also directly decides whether `c26` (prefer a different model for
independent review) is worth its cost.

**5. Stop adding rounds as the default response to an unsatisfying review.** There is no measured
saturation curve, so nothing in the literature bounds the number of rounds; the bound has to come
from us. The settlement definition already written — converged, rebased, or design verdict — is that
bound, and it should be applied rather than admired.

## 4. What this strategy does not claim

It does not claim to save tokens. The measured cost ratios above are for static-analysis triage, not
for reviewing skills, rubrics and change requests, and this project still records no cost per round.
Every number in §2 was measured on something other than our own artifacts. The honest position is
unchanged from the two previous runs: **the field has not measured the loop, and neither have we**,
and moves 4 and 5 are the two cheapest ways to change the second half of that sentence.
