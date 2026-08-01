# Pilot — Pro Search as the verification instrument, four queries

**Run:** 2026-07-31, in Dr. Ma's signed-in Perplexity Pro session, driven from this thread.
**Design:** one anchor per query, the compressed five-line contract, mode "Search".
**Answer key:** `AUDIT_grounding_perplexity_browsing_2026-07-31.md`, produced independently in the
agentic browsing mode before this method existed.
**Stopped after four.** The reason is in §3.

---

## 1. What held, every time

The format contract survived compression to a single paragraph. All four returns came back as the
five labelled lines, with a verdict token from the closed set, a quoted sentence, a URL and a
currency line. No essay, no preamble, no discussion section. Whatever else is wrong below, the
output-shape problem that dominated the Deep Research returns is solved: a short contract in a fast
mode is obeyed.

One blind control also hit. Query 2 was asked about Mager without being told what to look for, and
returned unprompted that "ABCD is a later mnemonic lineage that maps audience, behavior, condition,
and degree onto the same basic objective-writing idea, rather than Mager's original three-part
framing." That is the conflation the browsing run found, reproduced independently.

## 2. What failed

| # | Anchor | Returned verdict | URL it cited | Failure |
|---|---|---|---|---|
| 1 | Understanding by Design | `scope-accurate` | `authenticeducation.org` | Verdict contradicts its own quote. The quote says UbD helps teachers "craft effective and engaging learning activities", which is instruction — the browsing run read the same fact as `scope-too-narrow`. |
| 2 | Mager / ABCD | `scope-too-broad` | `agsci.psu.edu/.../abcd-model.pdf` | Right finding, wrong evidence. A university course PDF, and the quote is generic goals-versus-objectives text that is not Mager's. |
| 3 | Bloom, revised | `scope-too-narrow` | `uwaterloo.ca/centre-for-teaching-excellence/...` | **Contradicted by the primary source.** It quoted a teaching-centre tip sheet saying learners "are expected to progress in a linear manner, beginning at 'remember' and ending at 'create'". Anderson & Krathwohl's own text says the process categories do **not** form a cumulative hierarchy, and Krathwohl 2002 says "the requirement of a strict hierarchy has been relaxed". |
| 18 | Mayer, personalization | `scope-too-narrow` | `jsu.edu/online/faculty/MULTIMEDIA LEARNING by Richard E. Mayer.pdf` | **The flagship control, failed in the direction that matters.** A university-hosted copy of the book, not the study or its publisher. It did not report the operationalization even though the query asked for it directly, and `scope-too-narrow` points toward *widening* an anchor whose recorded failure was that it had already been widened too far. |

**Source tier: 0 of 4 cited the original publication or its publisher.** The four hosts are an
author's organisation page, a university course PDF, a university teaching-centre tip sheet, and a
university-hosted copy of a commercial book. The prompt excluded review, blog, teaching-centre,
course, aggregator, mirror and reseller pages by name, in every query.

**Mode instability.** By query 4 the session had drifted into "Learn step by step" — the answer ended
by asking the user a question and offering learning-mode follow-ups. The mode selector does not hold
across queries in a session, so mode is a per-query precondition to be re-checked, not set once.

## 3. Diagnosis, and why this is worse than the Deep Research failure

Pro Search answers in seconds from readily indexed pages. For exactly these frameworks, the readily
indexed pages **are** teaching-centre summaries, course handouts and lecture PDFs — and that
population is the one most likely to carry the popular simplification rather than the source's own
qualification. Bloom is the clean demonstration: the misconception that the levels are a teaching
ladder is precisely what a teaching-centre tip sheet repeats, and it is precisely what the revised
taxonomy's own text denies.

So the two cheap modes fail differently, and the difference is not in our favour:

- **Deep Research** was incomplete and honest. It reached 15 of 29 anchors, declared the other 14
  unreached, and its errors were traceable to the sources it named.
- **Pro Search** is complete and confidently wrong. It answers every query, in the right shape, with
  a real quote from a real page — and the page is a summary of the source rather than the source.

A rejected-host check would have caught none of these four automatically, because a university
domain reads as academic. The failure is not the top-level domain, it is the *genre* of the page.
That is a limitation of the scorer's host predicate worth recording:
`scripts/score_deepresearch_report.py` tests where a page lives, not what kind of page it is.

## 4. What Pro Search is good for

Locating. In all four cases it found real, relevant, openly accessible documents in seconds. What it
does not do is read the source and quote what the source itself says. That split suggests a hybrid
worth testing separately: Pro Search as a locator that returns candidate primary-source URLs, and
this thread as the reader that fetches each one and quotes it, which is a step the browsing mode was
performing internally and neither cheap mode performs at all.

## 5. Cost of the pilot

Four Pro Searches out of a weekly allowance Perplexity does not publish for Pro. No Research queries
were spent. The account page exposes no live usage counter, so the remaining allowance is unknown.
