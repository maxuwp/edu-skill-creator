# POSED grounding questions, deduplicated and ranked for a 2,200-credit budget

**Inputs:** three independent question lists returned to Dr. Ma by the POSED threads (Opus 5,
Fable 5, Grok), 2026-07-31.
**Constraint:** roughly one comprehensive Computer run, then Deep Research until the monthly
allowance is gone, then nothing.
**Ranking rule:** a question earns Computer mode only if it needs *many parallel retrievals
reconciled into one answer*. A question with one authoritative source does not, however important it
is — that is a Deep Research job or a free one.

---

## Tier 0 — already answered. Do not spend anything on these.

Six items appear in the three lists that existing evidence settles. Five come from the grounding
audit already paid for in edu-skill-creator; two were settled in this thread today from primary
sources.

| Asked by | Question | What we already have |
|---|---|---|
| Fable 1.2, Grok 3 | Is ABCD Mager's? | **No.** ABCD is Heinich, Molenda, Russell & Smaldino, *Instructional Technology and Media for Learning*. Confirmed twice independently: the browsing audit, and this thread's own retrieval today. `plan/SKILL.md:18` conflates two lineages and can be corrected now. |
| Fable 1.3, Grok 4 | Does A&K 2001 publish canonical per-level verb lists? | Partially. The browsing audit found **401 unique verbs across 47 published verb lists, with only 4 verbs appearing in all six tiers** (Frontiers, 2020). The canonical lists in circulation are not the book's. Whether the book publishes sparse sample verbs still needs the primary check — folded into Q1 as a control rather than paid for separately. |
| Fable 2.1/2.2, Grok 5 | Is there empirical support for treating band mismatch as a warning, not an error? | **Yes, already in hand.** A 2022 *CBE—Life Sciences Education* study of 940 items found the two dimensions are not independent and that **"prompt words do not reliably predict cognitive processes"**. That is the citable support Fable wants for B5 and for closing D1. |
| Grok 20 | Is 7±2 in the primary cognitive-load literature? | **No.** The browsing audit found Sweller 1988 states no working-memory numeric threshold; the only number is a simulation property. Also: germane load was formally dropped by Kalyuga & Plass (2025). Cowan's 4±1 still needs its own primary citation — Tier 3 below, free. |
| Fable 1.5, Grok 18 | Are Gagné's nine events a closed checklist? | **No.** Gagné, Briggs & Wager, ch. 10: the chapter is scoped to events for a single performance objective within a lesson, and **"by no means are all of these events provided for every lesson."** That answers the essential-subset question directly. |
| Fable 1.4, Grok 13 | Wiggins & McTighe on "understand" and on evidence | Partially. This thread confirmed today from ASCD's own white paper that UbD guides **"curriculum, assessment, and instruction"** and that Stage 3 plans instruction. The specific treatment of "understand" as a goal verb is not yet covered — kept in Q3. |

**Consequence:** the Mager/ABCD run all three threads proposed is cancelled, and Fable's blind
control 1.2 has already fired. Two of Fable's four numeric constants and one of Grok's Fleet A items
are closed without spending.

## Tier 1 — the one Computer run

**Q1. Do published Bloom verb lists agree with each other, and does the primary source authorise any
of them?**

This is the only question on any of the three lists that genuinely needs parallel paths reconciled.
It requires collecting six or more independently published verb lists, extracting the placement of
the same verb set from each, building a comparison matrix, checking the 2001 book itself, and then
reconciling disagreement into one verdict. A single-pass mode will sample two lists and generalise;
that is precisely the satisficing failure recorded in `METHOD_deep_research_orchestration_v1.md` §2.

It is also the most load-bearing question POSED has. It decides whether band mismatch stays a
warning or becomes critical (D1), whether `outcome_verb_bands.md` can cite anything at all for its
placements, and whether the discipline verbs POSED actually uses — `allocate`, `route` — have any
published home.

Prompt: `docs/deepresearch_runs/POSED_Q1_verb_band_reconciliation.md`.

**Blind controls, recorded here and absent from the prompt.** Expected: (a) the lists disagree on
`identify` and `define`, placing them in different levels; (b) A&K 2001 gives sparse illustrative
verbs, not the exhaustive tables in circulation; (c) `allocate` and `route` appear on few or no
published lists, which would mean POSED's engineering verbs are unanchored rather than misplaced.

## Tier 2 — Deep Research, in this order, one run each

**Q2. The avoid-list census.** *Promoted to Computer mode after Q1 cost only ~300 credits.* Prompt:
`docs/deepresearch_runs/POSED_Q2_avoid_list_census.md`. Which assessment offices publish lists of
verbs to avoid, which terms appear on them, whether ABET follows the same convention, and whether the
convention is contested in the literature at all. *Decides:* whether B3 states a fact or a documented
position, whether `comprehend` and `grasp` stay on POSED's avoid list, and whether engineering mode
needs an exemption. Fable 3.1, Grok 6/7/8/9.

**Blind controls for Q2, recorded here and absent from the prompt.** Expected: (a) `understand` and
`know` appear on nearly every list, making them settled; (b) `comprehend` and `grasp` appear on few,
which would mean POSED's avoid list over-extends beyond the published convention; (c) **ABET's own
Criterion 3 outcomes use phrasing the avoid lists would reject**, which if true means engineering
mode cannot apply the convention to accreditation-derived outcomes; (d) Strand 6 finds real published
critique of avoid lists, which would turn B3 from a fact into a documented position.

**Q3. Evidence of learning, and the restatement defect.** Prompt:
`docs/deepresearch_runs/POSED_Q3_evidence_of_learning.md`. What do Wiggins & McTighe require of
acceptable evidence relative to a goal, what do university templates demand of a
"how will this be assessed" field, and is "evidence that only rephrases the objective" a named
failure mode anywhere in the literature? Include what UbD says about `understand` as a goal verb.
*Decides:* whether B4's Jaccard restatement check is grounded pedagogy or only a regex. Fable
1.4/1.6, Grok 13/14/15.

**Run this one in Deep Research, not Computer — it is a mode test as well as a question.** Q1 and Q2
cost ~300 credits each, so the constraint that shaped this plan turned out to be looser than assumed.
The open question is now whether the cheaper mode, given the same contract that made the Computer runs
work, satisfices the way it did on 2026-07-31. Q3 is a fair test because it is bounded: four strands,
one census with a countable target, and no strand requiring more than a handful of documents.

**What counts as satisfactory, fixed in advance so the judgement is not made after seeing the
result.** All four strands reached and none dropped silently; Strand 2 returns six or more distinct
publishers; every non-`unverified` row carries a verbatim quote and the URL hosting it; no blog,
content farm or aggregator cited as a source; delivered as one Markdown file; roll call present and
matching the tables. Dropping a strand while reporting completion, or returning three sources against
a six-source target, is the satisficing failure and settles the mode question against Deep Research
for this class of work.

**Blind controls for Q3, recorded here and absent from the prompt.** Expected: (a) UbD *does*
explicitly separate Stage 2 evidence from the Stage 1 goal, so Strand 1.1 should come back
`required-explicitly`; (b) the restatement defect is **not** a named failure mode in the literature,
which would mean B4's check is a house invention POSED must own rather than cite; (c) Mislevy's
evidence model is a full argument structure, not a sentence, so citing ECD for a one-line planning
field would be a scope overreach of the same species as the Mayer failure in lesson L14.

**Q4. What real learning outcomes actually look like.** Prompt:
`docs/deepresearch_runs/POSED_Q4_outcome_audits_and_rubrics.md`, built on
`CONTRACT_run_prompt_v2.md`. Published audits of university SLOs: how often do outcomes carry a
condition and a criterion; what instruments exist for scoring an outcome *statement* rather than
student work; whether any of those instruments reports reliability; and whether outcome-statement
quality predicts anything downstream. *Decides:* B6 severity, and whether B2's term-list signature can
cite an instrument. Fable 2.3/3.4, Grok 14.

**Blind controls for Q4, recorded here and absent from the prompt.** Expected: (a) condition and
criterion are rare in real published outcomes, most being bare verb-plus-object; (b) outcome-quality
rubrics exist in quantity but **none reports inter-rater reliability**; (c) no published evidence links
outcome-statement wording to any downstream result, only outcome-assessment *alignment*, which is a
different claim.

**Why (b) and (c) matter beyond this question.** If they hold, they complete a pattern already visible
in Q2 and Q3: the avoid list is a convention with no evidence base, the restatement defect has no name
in the literature, and the instruments for judging outcome statements would then be unvalidated too.
That would mean POSED's outcome-quality apparatus is convention rather than evidence — which does not
make it wrong, but does determine how every one of those checks must be worded to a faculty user. That
conclusion should be drawn once, deliberately, rather than three times by accident.

**Q5. The numeric constants.** Four numbers currently resting on arithmetic rather than published
norms: lecturer speech rate in natural lectures, out-of-class workload rates behind the Rice
estimator, discourse-marker rates in academic lecture corpora such as MICASE, and published time
norms for think-pair-share and similar activities. *Decides:* the pacing constant, the assessment
budget default, the oral-register bands, and the delivery-time model. Fable 4.1/4.2/4.4/4.5.

## Tier 3 — free. I retrieve these directly, no Perplexity spend.

Today's comparison established that direct retrieval beats Pro Search on exactly this shape of
question: one claim, one authoritative source, quote required.

- **ABET's student-outcome phrasing** and any guidance on converting it to course-level outcomes.
  One issuing body. Fable 3.3, Grok 8.
- **Cowan's 4±1**, from the primary paper, to replace the 7±2 the rubric currently implies.
  Grok 20.
- **The Rice workload estimator's own published rates and cited sources**, if the estimator
  documents them. One institutional source. Overlaps Q5 and may remove that sub-item entirely.
- **Mager's own definitions of condition and criterion**, if any publisher-hosted text is reachable.
  This thread returned `unverified` on it today and should say so rather than let it into a paid run.
  Fable 1.1, Grok 2.

## Tier 4 — drop, or defer past the budget

- **Practice-time allocation across cognitive levels** (Fable 2.4). A large, unsettled literature
  answering a question POSED can decide by faculty judgement. Highest cost, lowest decision value.
- **AI-era assessment integrity, 2023–2026** (Grok 21). A real topic and a good Deep Research
  subject, but it grounds no current CR row. Defer until something depends on it.
- **Automated Bloom-classifier accuracy** (Fable 2.2). Folded into Q1 as one sub-question rather than
  a run of its own, since the CBE—LSE finding in Tier 0 already carries the argument it was meant to
  support.

## Spending plan

| | Mode | Cost |
|---|---|---|
| Q1 | Computer | the credit budget |
| Q2, Q3, Q4, Q5 | Deep Research | monthly allowance, one run each |
| Tier 3 | direct retrieval here | none |
| Tier 0 | already answered | none |
| Tier 4 | not run | none |

If credits survive Q1, the second-best Computer candidate is Q2, for the same reason: it is a census
across many institutions rather than a lookup in one.
