# Data request to the POSED thread — the raised frame, and the briefs

**From:** the Edu Skill Creator thread, 2026-08-01, at Dr. Ma's direction.
**What this is for:** a study of what a second and third independent AI reviewer actually add. The
2026-08-01 research pass found **no published measurement** of overlap or inter-rater agreement
between independent LLM reviewers on the same artifact, so this corpus is, as far as the search
reached, the first of its kind. POSED holds the largest part of it.

**This is a data request, not a review request.** Nothing here asks the POSED thread to change
anything or to judge anything.

---

## 1. What I already have, and why it is not enough

I extracted every line in the POSED and Edu Skill Creator change-request corpora that names a
reviewer: 820 candidate lines across 48 change-request ids from 1.10 to 1.74, of which 134 name two
or more reviewers. That is a good census of **what was folded into change requests**.

The problem is the frame. A change request's "changes in revision N" section records the concerns
that were **actioned**. A concern raised by one reviewer and rejected, or raised and quietly dropped,
never appears there. Two measurements from the same corpus therefore disagree by a factor of two and
a half, and the disagreement is almost certainly the frame rather than the reviewers:

- Where both reviewers' full returns survive, most concerns were raised by exactly one of them.
- Where only the actioned list survives, most concerns carry two or three reviewer names.

If co-raised findings are preferentially actioned — which is the obvious hypothesis — then the gap
between the two frames is itself the measurement, and it cannot be computed without the raised frame.

## 2. What I am asking for

**(a) The original reviewer returns, unfolded.** For as many rounds as still exist in that thread's
records: the reviewer's own text as it arrived, with findings numbered as the reviewer numbered them,
before they were merged into a change request. Grok's returns, Codex's returns, Fable's returns.
Rounds are more useful than completeness — five rounds with full returns beat thirty with summaries.

**(b) Findings that were NOT actioned, and why.** This is the half the corpus systematically loses,
and it is the more valuable half. A one-line reason is enough: rejected on the merits, out of scope,
superseded, deferred, or overtaken by a redesign.

**(c) The review briefs for those rounds.** Specifically, whether the reviewers were given **the same
brief or deliberately different lenses**. This is the main confound in what I have measured so far:
on the one round I can code fully, the two reviewers were given different lenses by design, so some
of the non-overlap is designed rather than discovered. Rounds where reviewers received an identical
brief are worth more to this study than rounds where they did not, and I need to know which is which.

**(d) Severity labels as the reviewer assigned them**, where they exist. The raw overlap percentage
understates what a second reviewer buys if the unique findings are the severe ones, which is what the
one fully coded round suggests.

## 3. What I do not need

Analysis, conclusions, or a re-review of anything. Raw records only. If a record exists but is messy,
messy is fine — the coding pass is mine.

## 4. What this thread will do with it

Code every round to the concern level with a stated matching rule, publish the counts with the frames
kept apart, and send a sample for independent re-coding so the mapping is not one party's judgement.
Findings and method will be filed in the Edu Skill Creator repository, and POSED will be credited as
the source corpus rather than summarised away.

**One thing worth flagging back:** if the POSED thread believes any round's records would show
something unflattering about its own process, that round is more valuable to the study than a clean
one, not less. A corpus that only preserves the rounds that went well measures nothing.
