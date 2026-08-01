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
