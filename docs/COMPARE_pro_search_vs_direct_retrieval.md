# Perplexity Pro Search versus direct retrieval — the same four anchors, run twice

**Question asked:** is Perplexity Pro Search better than this thread's own search?
**Method:** the four anchors from `PILOT_pro_search_4_queries.md`, re-run here with the same
five-line contract, using web search plus direct document retrieval. Same day, 2026-07-31.
**Sample caveat:** n = 4, and these four were chosen because an independent answer key already
exists, not at random. Read the mechanism, not the ratio.

---

## 1. Head to head

| # | Anchor | Pro Search verdict / source | This thread's verdict / source | Who is right |
|---|---|---|---|---|
| 1 | Understanding by Design | `scope-accurate` — `authenticeducation.org` | **`scope-too-narrow`** — ASCD's own white paper, `files.ascd.org` | This thread |
| 2 | Mager / ABCD | `scope-too-broad` — a university course PDF, quote not Mager's | **`unverified` on Mager, ABCD conflation confirmed** — no publisher-hosted Mager text reachable | Same finding, better evidence here; neither produced a Mager quote |
| 3 | Bloom, revised | `scope-too-narrow` — a teaching-centre tip sheet | **`scope-accurate`, with one caveat** — Krathwohl's own article, journal masthead intact | This thread |
| 18 | Mayer, personalization | `scope-too-narrow` — a university-hosted copy of the book, operationalization not reported | **`scope-too-broad`** — ERIC's record of the *Journal of Educational Psychology* study, operationalization reported | This thread |

## 2. The two decisive cases

**Bloom.** Pro Search quoted a university teaching-centre tip sheet: learners "are expected to
progress in a linear manner, beginning at 'remember' and ending at 'create'." The source itself says
the opposite. From Krathwohl's own article, *Theory Into Practice* 41(4), Autumn 2002, College of
Education, The Ohio State University:

> "Like the original Taxonomy, the revision is a hierarchy in the sense that the six major categories
> of the Cognitive Process dimension are believed to differ in their complexity… However, because the
> revision gives much greater weight to teacher usage, **the requirement of a strict hierarchy has
> been relaxed to allow the categories to overlap one another**."

and, of the six categories: "They are arranged in a hierarchical structure, **but not as rigidly as
in the original Taxonomy**."

So our own claim — "levels are not a teaching order" — holds. The caveat is that calling the
revision purely a classification undersells a complexity ordering the authors do assert. Pro Search
did not get a defensible verdict wrong at the margin; it repeated the popular misconception that the
source was written to correct.

**Understanding by Design.** Pro Search returned `scope-accurate` while quoting text about helping
teachers "craft effective and engaging learning activities", which is instruction. ASCD's own white
paper settles it in its first sentence:

> "The Understanding by Design® framework (UbD™ framework) offers a planning process and structure to
> guide **curriculum, assessment, and instruction**."

and names Stage 3 outright: "Stage 3 — Plan Learning Experiences and Instruction… In Stage 3 of
backward design, teachers plan the most appropriate lessons and learning activities", with alignment
described as "the Stage 1 content and understanding must be what is assessed in Stage 2 and **taught
in Stage 3**." Our scope limit excludes something the framework explicitly includes.

**Mayer**, for completeness, since it is the anchor behind the recorded failure. The operationalization
is on the record of the *Journal of Educational Psychology* study (Mayer, Fennell, Farmer & Campbell,
2004): a narrated animation on the human respiratory system, where "the narration for the personalized
version was in conversational style in which **'the' was changed to 'your' in 12 places**", with the
effect appearing on transfer tests but not retention tests. Pro Search was asked for this directly and
returned a general definition instead, from a university-hosted copy of the book.

## 3. Why the difference is structural, not a matter of judgement

Pro Search reports **what pages say about a source**. This thread can **open the source and read it**.
Concretely, on this run: the ASCD and Krathwohl PDFs both came back as binary that the fetch layer
could not render, were saved to disk, and were decompressed and searched locally. That is the step
neither cheap Perplexity mode performs, and it is where every verdict above was actually decided.

Both modes found real, relevant, openly accessible documents in seconds. Only one of them read the
document.

**A consequence for the scorer.** All four Pro Search hosts are `.edu` or an author's organisation —
they pass a domain-based allowlist. The failure is the *genre* of the page, not its host, and
`scripts/score_deepresearch_report.py` cannot see genre. A page that is a summary of the source is
the failure mode this project has to catch, and no host predicate catches it.

## 4. Honest limits of this run

- **#2 is `unverified` here, deliberately.** No publisher-hosted copy of Mager's text was reachable;
  what is reachable is a WordPress-hosted PDF and course pages. Under the rule this project applies
  to others, that is `unverified`, and applying it to myself is the point. The ABCD lineage claim is
  confirmed from secondary sources only: the model is attributed to Heinich, Molenda, Russell and
  Smaldino, *Instructional Technology and Media for Learning*, not to Mager.
- **The Krathwohl PDF is a university-hosted copy** of the *Theory Into Practice* article, not the
  publisher's own site. It is the complete original article with its masthead and copyright line
  intact, which is a materially different object from a summary of it — but the distinction is mine
  to declare, not something a host check establishes.
- **The Mayer quote is from ERIC's record of the study**, not the *Journal of Educational Psychology*
  page, which is paywalled.

## 5. The answer to the question asked

For **locating** candidate sources, Pro Search is fast, broad, and roughly as good. For **verifying a
scope claim**, it is not competitive, and the reason will not be fixed by a better prompt: the job
requires reading the source, and that mode does not read sources.

There is a second result here worth more than the comparison. On the three anchors where verification
succeeded, this thread's independent verdicts match the agentic **browsing** run — `scope-too-narrow`
for UbD, `scope-accurate` for Bloom, `scope-too-broad` for Mayer — reached from different documents,
without consulting it. That is independent corroboration of the browsing run on the sample checked,
and it makes Pro Search the outlier rather than a third opinion.

**What this implies for the method.** The division of labour that works is not "cheap mode replaces
expensive mode". It is: any search mode locates candidate primary sources, and this thread fetches,
reads and quotes them. That is one fetch and one grep per anchor, it spends no Perplexity quota, and
on this sample it produced the same verdicts as the mode that costs the most.
