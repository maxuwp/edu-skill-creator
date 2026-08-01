Build an evidence table, not a report. This task has 6 independent strands. Do not write an introduction, a discussion section, or a conclusion, and do not recommend anything. Begin with Strand 1. A compact set of filled tables is a complete success; a long essay is a failure even if everything in it is true.

THE QUESTION

I need to know what has actually been MEASURED about the cost and the yield of reviewing work produced by AI coding agents, and about the review process itself. I do not need recommendations, best-practice advice, or vendor guidance about how review should be done; I have plenty of that already. I need numbers, the samples they were measured on, and the sentence reporting them.

Where a quantity has only been measured for HUMAN software review, before AI agents existed, include it and mark it clearly as human. Where nothing has been measured, say so and say where you looked: a well-formed negative is a successful answer to any strand in this task, and is worth more to me than a plausible citation.

STRAND 1 - THE MARGINAL VALUE OF ANOTHER REVIEWER

Has anyone measured what a second, third or fourth independent reviewer adds? Look for: overlap or agreement rates between independent reviewers or review tools examining the same artifact; the proportion of defects found by exactly one reviewer; whether different MODELS reviewing the same code find different defects than the same model run again with fresh context; inter-rater agreement among LLM reviewers or LLM judges. Give the overlap or agreement figure, the sample, and the quote.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

Columns: quantity measured | verdict | number | sample | verbatim sentence | human or agent | host class | URL

STRAND 2 - REVIEW EFFORT AGAINST DEFECT YIELD, AND WHERE IT SATURATES

Has anyone measured how defect detection changes with review effort, and whether it saturates? Look for: defects found per unit of review effort; an optimal or recommended review rate with the study behind it; diminishing returns curves; the number of review rounds after which additional rounds find nothing new; escape rates as a function of review depth. Include the classic human software inspection measurements, clearly marked as human, as well as any agent-era equivalent.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

Columns: quantity measured | verdict | number | sample | verbatim sentence | human or agent | host class | URL

STRAND 3 - SELECTIVE RE-REVIEW AGAINST FULL RE-REVIEW

After a change, is it measured whether reviewing only the changed unit plus what depends on it performs as well as reviewing everything again? Look for: regression test selection and its measured safety and cost savings; change-impact analysis effectiveness; partial versus full re-review or re-verification; any measured escape rate attributable to scoping a re-review too narrowly. Both human-era and agent-era results are wanted, each marked.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

Columns: quantity measured | verdict | number | sample | verbatim sentence | human or agent | host class | URL

STRAND 4 - STAGED PIPELINES, DETERMINISTIC CHECKS BEFORE MODEL REVIEW

Is it measured whether running deterministic checks first — compiler, tests, static analysis, linters — before an LLM reviewer changes the total cost or the defect yield of the pipeline? Look for: measured cost or token reduction from filtering with cheap checks first; measured yield differences between a model reviewing raw output versus output that already passed deterministic checks; false-positive rates of LLM reviewers with and without a deterministic pre-screen.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

Columns: quantity measured | verdict | number | sample | verbatim sentence | human or agent | host class | URL

STRAND 5 - DOES REQUIRING A REVIEWER TO RECORD WHAT IT VERIFIED CHANGE ANYTHING

Has anyone measured the effect of requiring a reviewer to report what it checked and found CORRECT, alongside the defects? Related shapes to search for: review briefs or rubrics that require positive findings as well as negative ones; asking a model to state what it verified before listing problems; whether recording confirmed properties reduces the rate at which a later revision breaks something an earlier review had established; regression of previously-passing behaviour across successive AI edits. Search for this specifically and report a clean negative if nothing exists.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

A finding of not-addressed is a successful answer to this strand, not a failure, provided you name the databases, venues and search terms you used.

Columns: what was measured, or searched for | verdict | number | sample | verbatim sentence | host class | URL

STRAND 6 - ASKING, VERSUS DISCLOSING AN ASSUMPTION, VERSUS PROCEEDING

Three distinct behaviours, and I want them kept apart. (a) The agent ASKS a clarifying question and waits. (b) The agent DISCLOSES the assumption it is making without waiting, so the user may correct it or ignore it. (c) The agent proceeds silently. Report what is measured about each, and in particular: is there any measurement that disclosure alone, without a question, causes users to catch a wrong assumption? Is there any validated rule for WHICH assumptions to surface to a NON-EXPERT user, as opposed to surfacing all of them or none? Look for progressive disclosure and selective transparency studies, interruption cost and attention studies, and expected-value-of-information formulations for question selection, and say for each which of (a), (b) or (c) it actually measures.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

Columns: source | which behaviour it measures, a, b or c | verdict | number | sample | verbatim sentence | host class | URL

EVIDENCE RULES

Every claim carries a VERBATIM QUOTE in quotation marks and the FULL URL of the page hosting those exact words, written as plain text beginning with https:// inside the cell. Not a canonical topic page, not an organisation's home page, not a bare hostname.

Every cited row also carries a HOST CLASS, which you assign yourself, from exactly this list:

publisher = the publisher, journal, or issuing body's own domain
author = the author's own site or their institution's page for that work
object-of-study = a page that IS the thing being surveyed
rehost = a genuine, complete copy of the real document on somebody else's domain
secondary = a source quoting or summarising the document rather than being it

If a row's host class is rehost or secondary, GIVE THE CANONICAL PUBLISHER URL IN THE SAME CELL, even if it is paywalled or you could not open it. Say which one you actually read. A labelled rehost is usable; an unlabelled one is not.

If you cannot produce both a verbatim quote and the URL hosting it, the verdict is unverified and you say what blocked you. A confident, plausible answer with no traceable quote is worse than an honest unverified and will be discarded.

Blogs, SEO pages, content farms, aggregators and document resellers are pointers, not sources. Use them to find the document, then cite the document.

A row without a NUMBER and the SAMPLE it was measured on cannot be marked measured-with-number, however confident the source sounds.

For every row marked unverified or not-addressed, name the single specific next query or document you would try.

CLOSE WITH THIS CHECK, AND WRITE NOTHING AFTER IT

- ROWS PER STRAND, one line each, then the total. Count the rows in your own tables; do not report a figure you have not counted.
- Strands completed: __ of 6. Name any strand you did not reach. Do not omit a strand silently.
- Rows carrying both a verbatim quote and its hosting URL: __ of __.
- Rows marked measured-with-number that carry BOTH a number AND the sample: __ of __. Name any that do not.
- Rows by host class: publisher __, author __, object-of-study __, rehost __, secondary __. THESE COUNTS MUST SUM TO THE ROW TOTAL. If a row could take more than one class, list it once under its primary class.
- Rows measured on humans rather than agents: __.
- Sources I could not open, and what blocked each.
- Any row where my verdict token and my prose disagree, name it, or write "none".

HOW TO DELIVER THE RESULT

Put the ENTIRE ANSWER IN ONE MARKDOWN FILE and offer that file for download. It must contain every table and every section asked for above, in order, with nothing left behind in the chat window. Do not split the answer across several files, and do not deliver a table as a CSV: a CSV export carries one table and silently drops everything else.

If you reference any other file in your answer, deliver that file too. A file named but not delivered is a claim with nothing behind it.

If a separate list, CSV or spreadsheet is also useful, produce it IN ADDITION TO the complete Markdown file, never instead of it.
