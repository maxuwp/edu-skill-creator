# Independent coding task — for Codex and for Grok, separately

**From:** the Edu Skill Creator thread, 2026-08-01. **This is not a review.** You are not being asked
to judge a document, find defects, or improve anything. You are being asked to **code data**, and the
value of your output depends entirely on it being produced without seeing anyone else's coding.

---

## 0. Read this first: what would spoil the result

A coding of this kind is worthless if the coders converge because they saw each other's work. So:

- **Do not open `docs/DATA_reviewer_overlap_2026-08-01.md`.** It contains a completed coding of the
  same material. If you have already read it, say so at the top of your return and code anyway; a
  contaminated coding that declares itself is usable, a hidden one is not.
- **Do not read the other coder's return** if it reaches you.
- If you recognise your own findings in the material, that is expected — say so, and code anyway.
  Perfect blindness is not available in this corpus, because every candidate coder was also a
  reviewer in it. Declared self-involvement is the best available substitute, and it is the honest
  one.

## 1. The task

Two documents record two independent reviews of the same change request:

- `docs/REVIEW_CR_1.20_fable.md` — findings numbered F1 to F8
- `docs/REVIEW_CR_1.20_grok.md` — findings numbered B1 to B10

Eighteen numbered findings. Some of them are the same concern described by two reviewers; some are
raised by one reviewer only. **Your job is to decide which is which.**

## 2. The matching rule, and it is the only rule

> Two findings are **the same concern** when they would be closed by the same modification.

Not "when they are about the same section". Not "when they sound similar". If fixing one would leave
the other still standing, they are two concerns.

Reviewers number differently: one may spend three numbered findings on a single problem while the
other spends one. Count **concerns**, not findings, or the more granular reviewer will look more
productive and the disagreement will look larger than it is.

## 3. What to return

A table, and nothing else that matters:

| # | concern, one sentence in your own words | Fable finding ids | Grok finding ids | raised by |
|---|---|---|---|---|

Then four lines:

```
total distinct concerns:
raised by both reviewers:
raised by exactly one:
percentage raised by exactly one:
```

Then, and this part is as valuable as the table:

- **Any merge you were unsure about**, with the alternative reading. If a different coder could
  defensibly split one of your rows into two, name it. Disagreement about the merges IS the
  measurement of coder reliability, so surfacing your own borderline calls is the useful move, not a
  weakness.
- **Any finding you could not place** — one that is not a defect claim at all, or that is a
  confirmation rather than a finding.
- **Severity, as each reviewer labelled it**, where they labelled it. Note in particular whether any
  finding either reviewer marked critical or blocking was raised by that reviewer alone.

## 4. Why this is worth your time

The research pass that prompted it searched for any published measurement of overlap between
independent LLM reviewers examining the same artifact and found none. Whatever number falls out of
this coding, its credibility rests on more than one party having derived it from the raw documents.
One coder produced a figure already; if yours differs, the difference is the finding, and I would
rather have an honest disagreement between coders than an agreed number nobody checked.

## 5. Optional second item, only if you have appetite

`docs/RESEARCH_review_efficiency_perplexity_2026-08-01.md` is a research return that **failed** the
bar it was measured against: nineteen of thirty-two rows are secondary sources, and its strongest
numeric block was read from a paper-summary site rather than the paper. Two of its rows are the
load-bearing ones for this study — Strand 1's `not-addressed` on reviewer agreement, and Strand 5's
`not-addressed` on confirm-first review. **Try to falsify those two negatives.** If a published
measurement of either exists and the run missed it, that is worth more to me than the coding task
above, because it would mean the study's central claim to novelty is wrong.
