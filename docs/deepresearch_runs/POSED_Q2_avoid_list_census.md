Build an evidence table, not a report. This task has six independent strands that should be worked in
parallel and reconciled at the end. Do not write an introduction, a discussion section, or a
conclusion, and do not recommend anything. Begin with Table 1. A compact set of filled tables is a
complete success; a long essay is a failure even if everything in it is true.

## The question

University assessment offices commonly publish lists of verbs and phrases that should be **avoided**
in student learning outcomes, on the grounds that they describe something unobservable. I need to
know how widely those lists agree, whether accreditation bodies follow the same convention, and
whether the convention itself is settled or contested in the literature.

## Strand 1 — the census of avoid lists

Find **at least eight independently published lists** of verbs or phrases to avoid in learning
outcomes. Each must come from a different publisher: no two from the same university or university
system. Prefer university assessment offices, teaching and learning centres, accreditation bodies,
and academic publishers. A page that reproduces such a list without naming its source does not count.
Record publisher, document title, year if stated, and the full URL of the page or PDF carrying the
list.

## Strand 2 — the matrix

For each term below, record whether each list in Strand 1 names it as a term to avoid: `avoid` if the
list names it, `absent` if the list exists but does not name it, `unverified` if you cannot read that
list's entry.

    understand · know · learn · appreciate · comprehend · grasp · be familiar with · be aware of ·
    be exposed to · value · realize · become acquainted with

## Strand 3 — nominalized phrases

Separately from single verbs, do these lists flag phrases that wrap an unobservable state inside an
observable-looking verb — for example "demonstrate knowledge of", "develop an understanding of",
"gain awareness of", "show appreciation for"? Report which lists flag which phrases, with a verbatim
quote from each list that does.

## Strand 4 — accreditation and engineering

Does ABET, or engineering-education outcome guidance, follow the same convention? Two specific
things:

1. Quote **ABET's Criterion 3 student outcomes verbatim**, in the exact wording ABET publishes, from
   ABET's own site.
2. Report whether ABET or engineering-program guidance anywhere instructs against, or permits, the
   terms in Strand 2 — and if any accredited-program document uses one of those terms in a published
   outcome, quote it.

Report what you find, including a finding that accreditation language does not follow the convention.
That is a real result, not a failure.

## Strand 5 — contested stems

Some stems look weak but are treated as observable in assessment practice, and some are argued about.
For `identify`, `describe`, `explain`, `discuss` and `demonstrate`, report whether published guidance
treats each as acceptable, as acceptable only with qualification, or as one to avoid. Separate the
ones that are near-universally rejected from the ones on which published guidance splits.

## Strand 6 — is the convention itself contested?

Find published critique of avoid lists as an instrument: scholarship in assessment, higher-education
or educational-measurement literature arguing that banning verbs like "understand" is unjustified,
that observability is the wrong criterion, or that the practice has no empirical support. Also report
any published defence that cites evidence rather than convention. If no critical literature exists,
say so explicitly — that is itself the answer.

## Strand 7 — reconciliation

Only after the strands above. For each term in Strand 2, state how many of the lists you found name
it, and classify it: `near-universal` if named by all or nearly all, `common` if named by a majority,
`occasional` if named by a minority, `absent` if named by none.

## Output

**Table 1 — sources.** `id | publisher | document title | year | full URL`

**Table 2 — the matrix.** Rows are the twelve terms, columns are the source ids, cells are `avoid`,
`absent` or `unverified`.

**Table 3 — reconciliation.** `term | lists naming it | out of | classification`

**Table 4 — nominalized phrases.** `phrase | lists flagging it | verbatim quote from one of them | full URL`

**Table 5 — contested stems.** `stem | acceptable / acceptable-with-qualification / avoid | how the guidance splits | verbatim quote | full URL`

**Strand 4 answer**, as a labelled block: ABET Criterion 3 outcomes quoted verbatim with the URL,
then one line on whether accreditation language follows or departs from the avoid convention.

**Strand 6 answer**, as a labelled block: verdict (`contested-in-literature` /
`no-critique-found` / `defended-with-evidence`), with each source quoted and linked.

## Rules that decide whether this is usable

- Every claim carries a **verbatim quote** in quotation marks and the **full URL of the page hosting
  those exact words**. Not a canonical topic page, not an organisation's home page.
- If you cannot produce both, mark that cell or row `unverified` and say what blocked you. A
  confident, plausible answer with no traceable quote is worse than an honest `unverified` and will be
  discarded.
- Blogs, SEO pages, content farms, aggregators, mirror domains and document resellers are pointers,
  not sources. A list you cannot trace to a named publisher does not enter Table 1.
- An assessment-office or teaching-centre page **is** a valid source here, because the institutional
  list is itself the object being studied. For Strand 4 only the accreditation body's own site counts,
  and for Strand 6 only peer-reviewed or published scholarship counts.
- Report what the sources say. Do not tell me which list is correct and do not recommend a course of
  action.

## Close with this roll call, and write nothing after it

- Sources in Table 1: __ (target: 8 or more, all different publishers)
- Matrix cells filled: __ of 12 terms × __ sources; cells left unverified: __
- Strands completed: __ of 7. Name any strand you did not reach.
- Sources I could not open, and what blocked each.
- For anything marked `unverified`, the single specific next query or document I would try.

## How to deliver the result

Put the **entire answer in one Markdown file** and offer that file for download. It must contain every
table and every section asked for above, in order, with nothing left behind in the chat window. Do not
split the answer across several files, and do not deliver a table as a CSV: a CSV export carries one
table and silently drops everything else, which happened on a previous run and cost a manual
re-transcription of the whole result.

If a separate list, CSV or spreadsheet is also useful, produce it **in addition to** the complete
Markdown file, never instead of it.

Write **every URL in full inside the table cell**, as plain text beginning with `https://`. A bare
hostname such as `example.edu` is not a citation and will be rejected. Do not rely on a hyperlink, a
footnote marker or a citation chip to carry the address, because those do not survive export.
