You are determining the current official status of two published standards, according to the record
kept by the body that issues each one. This is a verification task with a fixed output shape, not a
literature review.

Do not write an introduction, an executive summary, a synthesis section, or a conclusion. Begin your
answer with the table. A short report with two traceable rows is a complete success. A long report
with a discussion section is a failure, even if everything in it is true.

## The question

For each of the two standards below:

1. What status word does the issuing body itself apply to it, in its own catalogue or its own
   published version of the document? Report that word exactly as the issuing body writes it, rather
   than translating it into a word of your own.
2. What is the date attached to that status? Where a standard has both an original publication date
   and a later revision or version date, report both and say which is which. Do not report one as if
   it were the other.
3. What follows for someone citing this standard today: is there a successor, a replacement, or a
   current equivalent, and is the issuing body itself pointing to one?

This run is about official status. It is not about whether the standard is good, widely adopted, or
worth following.

## Output — exactly two rows, one per standard

| # | Standard | Status word used by the issuing body | Verdict | Dates, each labelled | Verbatim quote | URL hosting that quote | Successor or current equivalent |

- Verdict is exactly one of these three tokens, with nothing appended: `current`, `not-current`,
  `unverified`. The nuance goes in the "status word used by the issuing body" column and in the
  quote, not into the token.
- Verbatim quote is one or two sentences copied from the issuing body's own page or document, in
  quotation marks. Not a paraphrase.
- URL hosting that quote must be the page or document on which those exact words appear. Do not put
  the organization's home page there if the quote came from a catalogue entry, a status page, or the
  document itself.
- If you cannot produce both a verbatim quote from the issuing body and the URL that hosts it, the
  verdict is `unverified`. This is the most important rule in this document. A confident, plausible
  statement of status with no traceable quote from the issuing body is worse than an honest
  `unverified` and will be discarded.

## What counts as a source here

Only the issuing body: its own standards catalogue, its own status page, or the published document
itself on its own site.

Document resellers and standards shops that sell copies of the standard, mirror domains, consultancy
blogs, accessibility-vendor marketing pages, summary articles and aggregators are pointers, not
sources. A reseller's product listing may describe a standard's status in its own commercial
vocabulary, which is not the issuing body's word for it, and a previous run of this task produced a
wrong status by reporting a reseller's word as though it were the issuing body's. Use pointers to
find the issuing body's record, then cite the issuing body's record. If you cannot reach the issuing
body's own record, the verdict is `unverified` and you should say what blocked you.

## Citations must resolve

Put the URL in the row itself. If your output format adds numbered references at the end, the row's
own URL governs, and the two must point to the same document. A previous run's reference number
resolved to a different document than the row it belonged to, which made that row unusable.

## Close with this check, and write nothing after it

- Rows delivered: __ of 2.
- Rows whose reported URL is on the issuing body's own domain: __ of 2.
- Records I could not open, and what blocked each.
- Any row where my verdict token and my prose disagree — name it, or write "none".
- For every row I marked `unverified`, the specific next query or specific source I would
  try, one line each. An `unverified` row is a gap to be filled, not a closed question.

## The two standards

1. **IEEE Std 1028, Standard for Software Reviews and Audits.** Issuing body: IEEE. We currently
   cite this standard for defect severity classes and review process, alongside Fagan's 1976
   inspection paper. Determine its status in IEEE's own record.

2. **W3C WCAG, Web Content Accessibility Guidelines, version 2.2.** Issuing body: W3C. We currently
   cite 2.2 as the version we conform to. Determine, from W3C's own published document and status
   pages, the status and date of version 2.2, and the current status of WCAG 3.0.
