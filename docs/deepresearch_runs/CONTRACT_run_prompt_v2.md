# Reusable run contract, v2 — paste the blocks below into every Perplexity run prompt

**What this is.** The output, sourcing, delivery and self-check rules that every run prompt carries,
extracted so they stop being re-typed and drifting. v1 was implicit in the Q1–Q3 prompts; v2 folds in
what those three runs cost us.

**What each rule was bought with.**

| Rule | The failure that bought it |
|---|---|
| One Markdown file, no CSV substitute | Q1: the download produced a CSV of Table 1 only; four tables, two strand answers and the roll call had to be re-transcribed by hand |
| Full URLs inside the cell | Q1: every URL arrived as a bare hostname, and Table 4's as publisher names |
| Deliver any file you reference | Q2: Table 2 cited a companion census file holding the per-source verbatim text; it was never delivered |
| **Host-class column, self-declared** | Q3: four rows cited genuine documents on third-party hosts — a personal site, a college mirror, a secondary quotation — while a prose rule forbidding exactly that sat in the prompt |
| **Canonical URL alongside a rehost** | Q3, same failure. Prose cannot prevent the rehost; it can require the rehost be labelled and paired with the real location |
| **Roll call per strand, then sum** | Q3: the roll call reported 27 rows against 23 in the tables, and misnamed which row was short |
| Name the next query for every `unverified` | Perplexity's own pipeline measures coverage and backfills mid-run; a one-shot prompt can only convert the gap into a queue |

**The standing design point behind the host rules.** Perplexity's own prompt guide states that source
constraints belong in retrieval parameters because prose filters "may not carry through every turn of
the loop". Without API access we cannot set the parameter, so v2 stops trying to *prevent* the breach
and instead forces it to be *declared*. A labelled rehost with the canonical URL beside it is a
citation this thread can repair in one fetch. An undeclared one is a defect nobody sees.

---

## Block A — output discipline

> Build an evidence table, not a report. Do not write an introduction, a discussion section, or a
> conclusion, and do not recommend anything. Begin with the first table. A compact set of filled
> tables is a complete success; a long essay is a failure even if everything in it is true.
>
> Report what the sources say. Do not tell me which source is correct and do not recommend a course
> of action.

## Block B — evidence rules

> Every claim carries a **verbatim quote** in quotation marks and the **full URL of the page hosting
> those exact words**, written as plain text beginning with `https://` inside the cell. Not a
> canonical topic page, not an organisation's home page, not a bare hostname.
>
> Every cited row also carries a **host class**, which you assign yourself, from exactly this list:
>
> - `publisher` — the publisher, journal, or issuing body's own domain
> - `author` — the author's own site or their institution's page for that work
> - `object-of-study` — a page that *is* the thing being surveyed, such as an institutional template
>   in a census of institutional templates
> - `rehost` — a genuine, complete copy of the real document on somebody else's domain
> - `secondary` — a source quoting or summarising the document rather than being it
>
> **If a row's host class is `rehost` or `secondary`, give the canonical publisher URL in the same
> cell, even if it is paywalled or you could not open it.** Say which one you actually read. A
> labelled rehost is usable; an unlabelled one is not.
>
> If you cannot produce both a verbatim quote and the URL hosting it, the verdict is `unverified` and
> you say what blocked you. A confident, plausible answer with no traceable quote is worse than an
> honest `unverified` and will be discarded.
>
> Blogs, SEO pages, content farms, aggregators and document resellers are pointers, not sources. Use
> them to find the document, then cite the document.
>
> For every row marked `unverified`, name the single specific next query or document you would try.
> An `unverified` row is a gap to be filled, not a closed question.

## Block C — the roll call

> Close with this check, and write nothing after it.
>
> - **Rows per strand, listed one line each, then the total.** Count the rows in your own tables; do
>   not report a figure you have not counted.
> - Strands completed: __ of __. Name any strand you did not reach. Do not omit a strand silently.
> - Rows carrying both a verbatim quote and its hosting URL: __ of __.
> - Rows by host class: `publisher` __, `author` __, `object-of-study` __, `rehost` __, `secondary` __.
> - Sources I could not open, and what blocked each.
> - Any row where my verdict token and my prose disagree — name it, or write "none".

## Block D — delivery

> Put the **entire answer in one Markdown file** and offer that file for download. It must contain
> every table and every section asked for above, in order, with nothing left behind in the chat
> window. Do not split the answer across several files, and do not deliver a table as a CSV: a CSV
> export carries one table and silently drops everything else.
>
> **If you reference any other file in your answer, deliver that file too.** A file named but not
> delivered is a claim with nothing behind it.
>
> If a separate list, CSV or spreadsheet is also useful, produce it **in addition to** the complete
> Markdown file, never instead of it.

---

## Note for whoever runs these

Blocks A–D are mode-independent. What changes per mode:

- **Computer mode** — decompose into named strands and say they should be worked in parallel and
  reconciled at the end. Two runs at roughly 300 credits each, both excellent.
- **Deep Research** — keep the population bounded and numbered. Given that, it did not satisfice, but
  it broke the prose source-tier rule anyway, which is what Block B's host-class column now surfaces.
- **Running it from this thread's browser session** removes the delivery problem entirely, since the
  answer is read off the page rather than exported. Block D still belongs in the prompt for the runs
  Dr. Ma pastes himself.
