Build an evidence table, not a report. This task has 6 independent strands. Do not write an introduction, a discussion section, or a conclusion, and do not recommend anything. Begin with Strand 1. A compact set of filled tables is a complete success; a long essay is a failure even if everything in it is true.

THE QUESTION

I need to know what is actually published and measured about how AI coding agents handle the SCOPE of a change, in two specific situations: when the correct fix lies outside the change they were asked to make, and when the original request was underspecified so the agent filled the gaps itself. The usual answer, that agents should make minimal focused changes, is the thing under test rather than the answer.

The following chain is a HYPOTHESIS I want evidence for or against. It is not context to reason from, and you should not treat any part of it as established: (a) at intake a human under-describes the need, and the agent silently fills the gaps with defaults, creating a defect in the foundation of the work; (b) instructions to make the smallest change and to avoid disturbing already-working code then prevent the agent from ever reaching that foundation; (c) so repair rounds repeat at a shallow level, the defect survives, and cost accumulates; (d) adding a scope-escalation procedure on top could conflict with the standing instruction to minimise scope. Report what sources say about each part, including sources that contradict it.

STRAND 1 - IS THE PHENOMENON NAMED

Is there a recognised, named term in published work for an AI agent repeatedly producing shallow or symptom-level repairs that fail to reach a root cause, or for a repair loop that does not converge? Test at least six candidate names and report each separately: "symptom fix", "band-aid fix", "shallow patch", "surface fix", "root-cause analysis failure in agents", "non-convergent repair loop", "agent thrashing", plus any term you find in use that I have not listed. For each, give the definition as published and who published it.

Verdict token per row, one of exactly these, with nothing appended: named-and-defined | attested-informally | not-attested | unverified

A finding of not-attested is a successful answer to this strand, not a failure, provided you say where you looked.

Columns: candidate term | verdict | published definition, verbatim | who published it | host class | URL

STRAND 2 - WHAT PUBLISHED AGENT INSTRUCTIONS ACTUALLY SAY ABOUT SCOPE

Find at least SIX separately published instruction sets for AI coding agents, from SIX DIFFERENT organisations, no two from the same organisation. Acceptable objects: a vendor's official documentation for its coding agent, a published system prompt or agent-instruction file, an official best-practices page for configuring such an agent. For each, quote what it says about the scope of a change: whether it instructs the agent to make the smallest or most focused change, to avoid modifying unrelated or already-working code, to stay within the requested task, or says nothing on the subject.

For this strand the organisation's own documentation IS the object of study, so its own domain is the correct source. A third party summarising a vendor's guidance does not count as an instance.

Verdict token per row, one of exactly these, with nothing appended: explicit-minimal-scope | implicit-minimal-scope | no-such-instruction | unverified

Columns: organisation | document | verdict | the scope instruction, verbatim | host class | URL

STRAND 3 - DOES THE SAME DOCUMENT DEFINE AN ESCALATION PATH

For every instruction set you found in Strand 2, and using the same rows, report whether that same document also tells the agent what to do when the correct fix lies OUTSIDE the minimal scope: stop and ask, propose a plan before acting, escalate to the human, open a separate task, perform root-cause analysis, revise the specification, or nothing at all. Quote the escalation language if it exists. If a document instructs minimal scope and says nothing about the case where minimal scope is insufficient, that silence is the finding and should be reported as such.

Verdict token per row, one of exactly these, with nothing appended: escalation-defined | escalation-mentioned-no-mechanism | no-escalation | unverified

Columns: organisation | verdict | escalation language, verbatim, or "silent" | host class | URL

STRAND 4 - UNDERSPECIFIED REQUESTS AND DEFAULT-FILLING

Find at least SIX separately published sources, of which AT LEAST TWO must be peer-reviewed papers or preprints reporting a study rather than practitioner or vendor writing, on what happens when a request to an AI coding agent is underspecified: whether the agent fills the gaps with assumptions or defaults, whether that has been observed or measured, and what documented countermeasures exist. Countermeasures to look for by name: requiring clarifying questions before work begins, recording assumptions explicitly, specification-driven or spec-first agent workflows, a separate planning phase before editing, requirements elicitation techniques adapted for language-model agents.

Verdict token per row, one of exactly these, with nothing appended: mechanism-documented | advice-only | not-addressed | unverified

Columns: source | verdict | what it documents, verbatim | is it an empirical study, yes or no | host class | URL

STRAND 5 - HAS ANY OF THIS BEEN MEASURED

Separate from what people recommend: has anyone MEASURED any of the following, and reported a number? The number of attempts or rounds an agent needs before a defect is actually resolved; the proportion of agent fixes that address a symptom rather than a cause; the rate at which an agent's fix introduces a new defect; the token or dollar cost of iterative repair loops; whether constraining an agent to a minimal change raises or lowers its resolution rate. For every row give the NUMBER, the SAMPLE it was measured on, and the verbatim sentence reporting it. Include measurements from human software engineering where the same quantity was measured before agents existed, marking them clearly as such.

Verdict token per row, one of exactly these, with nothing appended: measured-with-number | asserted-without-measurement | not-addressed | unverified

A finding of not-addressed is a successful answer to this strand, not a failure, provided you say which databases and venues you searched.

Columns: quantity measured | verdict | number | sample | verbatim sentence | human or agent | host class | URL

STRAND 6 - CONFLICT BETWEEN A STANDING CONSTRAINT AND THE TASK

Is there published work on what an AI agent does when a standing instruction in its system prompt conflicts with what the immediate task requires, and on how such conflicts are meant to be resolved? Look for treatments of instruction precedence or hierarchy between system and user instructions, detection of conflicting instructions, published evidence on which instruction wins when they disagree, and any guidance on writing a task instruction that is permitted to override a standing constraint. For each source, state precisely what KIND of conflict it addresses, since a source about resisting malicious injected instructions is not evidence about a benign conflict between a scope constraint and a task goal. Say which kind each source covers.

Verdict token per row, one of exactly these, with nothing appended: documented-with-resolution | documented-no-resolution | not-addressed | unverified

Columns: source | verdict | kind of conflict addressed | verbatim quote | host class | URL

EVIDENCE RULES

Every claim carries a VERBATIM QUOTE in quotation marks and the FULL URL of the page hosting those exact words, written as plain text beginning with https:// inside the cell. Not a canonical topic page, not an organisation's home page, not a bare hostname.

Every cited row also carries a HOST CLASS, which you assign yourself, from exactly this list:

publisher = the publisher, journal, or issuing body's own domain
author = the author's own site or their institution's page for that work
object-of-study = a page that IS the thing being surveyed, such as a vendor's own agent documentation in a census of agent documentation
rehost = a genuine, complete copy of the real document on somebody else's domain
secondary = a source quoting or summarising the document rather than being it

If a row's host class is rehost or secondary, GIVE THE CANONICAL PUBLISHER URL IN THE SAME CELL, even if it is paywalled or you could not open it. Say which one you actually read. A labelled rehost is usable; an unlabelled one is not.

If you cannot produce both a verbatim quote and the URL hosting it, the verdict is unverified and you say what blocked you. A confident, plausible answer with no traceable quote is worse than an honest unverified and will be discarded.

Blogs, SEO pages, content farms, aggregators and document resellers are pointers, not sources. Use them to find the document, then cite the document.

For every row marked unverified, name the single specific next query or document you would try.

Source tier differs by strand, deliberately. For Strands 2 and 3 the organisation's own documentation IS the object of study and is the required source; a third-party summary is a pointer only. For Strands 1, 5 and 6 the original publication or preprint is required and a summary is a pointer. For Strand 4 both tiers are acceptable, and each row must say which it is.

CLOSE WITH THIS CHECK, AND WRITE NOTHING AFTER IT

- ROWS PER STRAND, one line each, then the total. Count the rows in your own tables; do not report a figure you have not counted.
- Strands completed: __ of 6. Name any strand you did not reach. Do not omit a strand silently.
- Rows carrying both a verbatim quote and its hosting URL: __ of __.
- Strand 2: number of DISTINCT organisations reached: __ of the six required. Name them.
- Strand 4: number of rows that are empirical studies: __ of the two required.
- Rows by host class: publisher __, author __, object-of-study __, rehost __, secondary __. THESE COUNTS MUST SUM TO THE ROW TOTAL. If a row could take more than one class, list it once under its primary class.
- Sources I could not open, and what blocked each.
- Any row where my verdict token and my prose disagree, name it, or write "none".

HOW TO DELIVER THE RESULT

Put the ENTIRE ANSWER IN ONE MARKDOWN FILE and offer that file for download. It must contain every table and every section asked for above, in order, with nothing left behind in the chat window. Do not split the answer across several files, and do not deliver a table as a CSV: a CSV export carries one table and silently drops everything else.

If you reference any other file in your answer, deliver that file too. A file named but not delivered is a claim with nothing behind it.

If a separate list, CSV or spreadsheet is also useful, produce it IN ADDITION TO the complete Markdown file, never instead of it.
