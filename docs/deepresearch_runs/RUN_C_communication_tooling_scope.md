You are verifying factual scope claims about four specific published sources. This is a verification
task with a fixed output shape, not a literature review.

Do not write an introduction, an executive summary, a synthesis section, or a conclusion. Begin your
answer with the table. A short report with four traceable rows is a complete success. A long report
with a discussion section is a failure, even if everything in it is true.

## The question

For each of the four items below I state what I take the source to be and a claim about what it
covers, marked "our scope limit". Both were written by me, are the thing under test, and may be
wrong. Do not treat them as context to reason from.

Item 1 is a research publication. For it, determine from the source itself: what population, task
type and observable layer it actually studied; whether my scope limit is accurate, too broad or too
narrow; and any number it states exactly, reporting untraceable numbers as untraceable.

Items 2 to 4 are software repositories or vendor documentation. For each, determine from the
repository or documentation itself: what the source actually is and what it actually covers; whether
my one-line description of it is accurate, too broad or too narrow; whether it still exists at the
path cited, or has moved, been renamed, or been archived; and its current version or most recent
activity.

This run is about what these sources are and cover. It is not about whether they are good or whether
we should be using them.

## Output — exactly four rows, one per item

| # | Anchor | Verdict | What the source actually is or validated | Verbatim quote | URL hosting that quote | Currency |

- Verdict is exactly one of these six tokens, with nothing appended: `scope-accurate`,
  `scope-too-broad`, `scope-too-narrow`, `superseded`, `contested`, `unverified`. Do not write
  "scope-accurate (with a correction)" or any other qualified form. Qualifications belong in the
  "what the source actually is or validated" column.
- `contested` means correctly cited and within scope, but under active published empirical
  challenge. Use it when that is the real situation.
- Verbatim quote is one or two sentences copied from the source, in quotation marks. Not a
  paraphrase. For a repository, quote its own README or documentation.
- URL hosting that quote must be the page, file or PDF on which those exact words appear. Do not put
  an organization's home page or a canonical topic page there if the quote came from somewhere else.
- If you cannot produce both a verbatim quote and the URL that hosts it, the verdict is `unverified`.
  This is the most important rule in this document. A confident, plausible summary with no traceable
  quote is worse than an honest `unverified` and will be discarded.
- Paywalled or unreachable: `unverified`, and say which source was unreachable and what blocked it.
  That is a useful result, not a failure.
- Currency must state the current edition, version or latest activity date, and name any successor.

## What counts as a source

Cite the original publication, its publisher, or the project itself: the paper (including
author-hosted or institution-hosted PDFs and ERIC full text), the publisher's page, the repository's
own files on its own host, the vendor's own documentation site.

Reviews, summaries, blog posts, course pages, tutorial sites, aggregator sites, package mirrors and
document resellers are pointers, not sources. Use them to find the original, but the URL you report
must be the original. A previous run of this task failed by citing a personal blog review for a
book's contents, an unrelated commercial PDF for a software methodology, and a mirror domain rather
than the issuing agency. If the only thing you can reach is a pointer, the verdict is `unverified`.

## Citations must resolve

Put the URL in the row itself. If your output format adds numbered references at the end, the row's
own URL governs, and the two must point to the same document. A previous run's reference number
resolved to a different paper than the row it belonged to, which made that row unusable.

## Close with this check, and write nothing after it

- Rows delivered: __ of 4.
- Rows whose reported URL is the original publication, the project's own repository, or the vendor's
  own documentation: __ of 4.
- Sources I could not open, and what blocked each.
- Any row where my verdict token and my prose disagree — name it, or write "none".
- For every row I marked `unverified`, the specific next query or specific source I would
  try, one line each. An `unverified` row is a gap to be filled, not a closed question.

## The four items

1. **Assertion–evidence slide structure (Michael Alley).** We use it to ground slides built as a
   full-sentence assertion headline supported by visual evidence. Our scope limit: "Technical
   presentation slides."

2. **The Anthropic `skill-creator` skill.** We take it to be first-party vendor documentation for a
   methodology for authoring agent skills. Cited at the `anthropics/skills` repository on GitHub.

3. **`plugin-dev`, in the `anthropics/claude-code` repository on GitHub.** We take it to be
   first-party vendor documentation for developing Claude Code plugins.

4. **`writing-skills`, in the `obra/superpowers` repository on GitHub.** We take it to be community
   documentation for authoring agent skills.
