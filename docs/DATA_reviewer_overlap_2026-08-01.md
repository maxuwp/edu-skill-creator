# Reviewer overlap — first measurement, and the corpus available for more

**Why this exists.** The 2026-08-01 research return found no published measurement of overlap or
inter-rater agreement between independent LLM reviewers examining the same artifact
(`docs/RESEARCH_review_efficiency_perplexity_2026-08-01.md`, Strand 1, `not-addressed`). This
project has been running two and three independent model reviewers over the same documents for a
week and has never computed it. This file is the first computation and the corpus survey behind it.

---

## 1. Method

**Unit of analysis: the distinct concern, not the finding.** Reviewers number their findings
differently — one writes three findings about one problem, another writes one. Counting raw findings
would make the more granular reviewer look more productive and would inflate apparent disagreement.
A *concern* is a defect claim about the same defect in the same artifact location, however many
numbered findings each reviewer spends on it.

**Matching rule.** Two findings are the same concern when they would be closed by the same
modification. This is the rule that was applied — before this measurement was contemplated — when
CR 1.20 rev 2 was written, and the mapping is recorded in that document's §0 table, so the coding is
auditable against an artifact written for another purpose rather than reconstructed to support a
number.

**Stated limitation.** One coder, who is also one of the reviewed parties. A second coder should
re-derive the mapping from the two review documents without seeing this table. Until then the figure
is a level-3 result under this project's own evidence scheme: recomputable, but single-provenance.

## 2. The measured pair — CR 1.20, reviewed independently by Fable and Grok

Both reviewers received the same document and the same brief, with deliberately different lenses
(method and evidence; design and blast radius). Fable returned 8 findings, Grok returned 10.

| # | concern | Fable | Grok | raised by |
|---|---|---|---|---|
| 1 | The evidence claim is over-stated: mixed denominators, censored after-period, confounds, brief changed twice | F1, F2, F8 | B6 | **both** |
| 2 | `how_verified` is unenforced, so the CR's own mitigation is prose and the field is gameable | F3 | B2, B7 | **both** |
| 3 | Supersession is shapeless; no first-class invalidate path for a wrong protected row | F4 | B3, B8 | **both** |
| 4 | Instance D is uncited author testimony carrying the broadest claim | F5 | — | Fable |
| 5 | `c8`'s seed data exists only in session context and will expire | F6 | — | Fable |
| 6 | Instance C "already solved" overstates what was verified | F7 | — | Fable |
| 7 | `c13` propagates the whole contract into every generated plugin | — | B1 | Grok |
| 8 | `c3` forbids an honest `regenerate` with nothing preservable | — | B4 | Grok |
| 9 | `c5`'s missing-version default is a permanent fail-open | — | B5 | Grok |
| 10 | Group C/D ordering: wire generators only after A+B are green | — | B9 | Grok |
| 11 | `c17`'s deferral should state its dependency | — | B10 | Grok |

**18 findings collapse to 11 distinct concerns. 3 were raised by both reviewers. 8 were raised by
exactly one — 72.7%.**

**The severity distribution is the more striking result.** Grok's single **critical** finding (`c13`)
was raised by Grok alone. Fable's single **blocker** (`c8`'s seed data) was raised by Fable alone.
Neither of the two highest-severity findings in the round would have existed with one reviewer, and
which one you lose depends on which reviewer you drop.

**Direction of the disagreement is not random.** Every Fable-only concern is about evidence and
honesty; every Grok-only concern is about design and blast radius. The reviewers were given different
lenses and produced non-overlapping findings along exactly those lines, which suggests the low
overlap is at least partly *designed* rather than discovered — a confound that any write-up must
carry, and a variable worth manipulating deliberately in a later round.

## 2a. Second measurement — POSED CR 1.71 revision 2.1, three reviewers

Codex, Fable and Grok reviewed the same implementation. The change request records which reviewers
raised each concern, in its own revision-2.1 section, written before any measurement was contemplated.

| # | concern | Codex | Fable | Grok | raised by |
|---|---|---|---|---|---|
| 1 | Vehicle binding table: token to manifest key, student form only | M2 | E26 | ✓ | **three** |
| 2 | `pre_course_quiz` moved to diagnostic-exempt; 4 of 5 origin tags would have fired falsely | — | E25 | — | Fable |
| 3 | Acceptance test 1 softened from "exactly two" to "at minimum two" | — | E5 | ✓ | two |
| 4 | R3 renamed to declared dependency order; the "0 forward references" claim withdrawn as vacuous | C1a | E24 | ✓ | **three** |
| 5 | D2's plan half replaced with a post-assembly validate-and-stamp transaction | C3 | — | critical | two |
| 6 | Census enumerator frozen and shipped, denominator stated | — | — | major | Grok |
| 7 | Test 14 re-derives whenever claim fields are present; P1 and R1b tightened | — | E27 | minors | two |

**7 concerns. 2 raised by exactly one reviewer — 28.6%.** Two of the seven were raised by all three.

**These two numbers do not belong in the same column, and saying so is the point.** CR 1.20 counts
concerns **raised**; CR 1.71's section counts concerns **actioned in a revision**. A concern raised by
one reviewer and rejected never appears in the second frame. Putting 72.7% and 28.6% side by side
without that distinction would repeat exactly the defect Fable caught in CR 1.20 — mixing
denominators and censoring one end of the distribution — in a document written to measure the process
that caught it.

**Two hypotheses fall out, both testable against this corpus.**

1. **Co-raised findings may be preferentially actioned.** If a concern raised by two reviewers is more
   likely to survive triage than one raised by one, the actioned frame will always show higher
   agreement than the raised frame, and the gap between the two frames is itself the measurement.
   Testable by coding raised-and-rejected concerns from the same rounds.
2. **Agreement tracks how mechanical the artifact is.** CR 1.20 was a method and evidence review, and
   the reviewers diverged; CR 1.71 was an implementation review, and they converged. The grounding
   audit is a third instance in the same direction: two independent runs agreed on the factual rows
   and disagreed on eight of fourteen scope judgments. If it holds, the practical rule is that a
   second reviewer buys most where the judgment is interpretive, and least where a check could have
   settled it — which is also the cost argument for pushing mechanical work down to the lint.

## 3. Corpus available for further coding

| source | multi-reviewer artifacts | state |
|---|---|---|
| edu-skill-creator, CR 1.20 | 1 pair, both reviews filed in full | **coded above** |
| edu-skill-creator, L20 and L22 | 3 reviewers (Fable, Codex, Grok) on the scope-escalation design | returns arrived in conversation, not filed as documents; recoverable from the session transcript |
| POSED | 58 change requests mention a named external reviewer; **6** carry per-finding attribution in a codable form | needs manual coding; the other 52 attribute at the document level only |
| p2d, slide-narrator, the codex-side mirrors | 40 review-named files across four repositories | not yet surveyed for multi-reviewer pairs |

**What is missing for a defensible study, in order of cost.** A second coder for the matching rule.
Filed returns for the L20/L22 round, which currently exist only in a transcript. A same-lens control:
two reviewers given the *identical* brief, to separate designed non-overlap from genuine reviewer
variance. And a severity-weighted figure, since the raw overlap percentage understates what a second
reviewer bought here.

## 4. What this does and does not support

It supports, on one pair: a second independent reviewer with a different lens produced eight of
eleven concerns that the first did not raise, including the round's only critical finding. It does
not support any general claim about model heterogeneity, because the lenses differed by design and
n = 1. The honest description is a **case study with a computed figure**, which is more than the
published record currently contains for LLM reviewers, and less than an experiment.
