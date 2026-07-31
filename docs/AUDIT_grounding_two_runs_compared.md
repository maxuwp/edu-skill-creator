# The two Perplexity grounding runs, compared

**Inputs:** `docs/AUDIT_grounding_perplexity_browsing_2026-07-31.md` (agentic browsing) and
`docs/AUDIT_grounding_perplexity_deepresearch_2026-07-31.md` (deep research), both against
`docs/HANDOFF_perplexity_grounding_audit.md`.
**Purpose:** neither run is a baseline on its own. This note records what they agree on, where they
disagree, and what still has to be settled before any anchor text is edited.

---

## 1. Coverage

| | Anchors with a verdict | Anchors marked unverified | Currency half |
|---|---|---|---|
| Browsing | **29 of 29** examinable | 0 (several numeric sub-claims flagged inline) | done, dated, per anchor |
| Deep research | **14** | **15**, listed explicitly | not run |

The deep-research run states plainly that it is "a Half A pass" and that unreached anchors "should
not be treated as validated by omission." That is the handoff's rule followed correctly, and the
honesty is worth more than the missing rows cost. But it means the two runs are not
interchangeable: one is a complete audit, the other is a partial second opinion on half of it.

Note the mode inversion against what the handoff asked for. The handoff assigned Deep Research to
the *currency* half; the deep-research run did *scope* instead, and the browsing run did both. So
the currency sweep as designed was effectively run once, by browsing, not twice.

## 2. Where they disagree — 8 of the 14 anchors both covered

This is the most useful output of having run it twice, and it is a high disagreement rate.

| # | Anchor | Browsing | Deep research |
|---|---|---|---|
| 3 | Bloom (revised) | scope-accurate | scope-too-broad — "calling it purely a classification undersells that the authors still describe it as a hierarchy of complexity" |
| 7 | Cognitive Load Theory | scope-too-broad | superseded — though its own prose then says "contested, not superseded outright", so the verdict and the note disagree with each other |
| 8 | ICAP | scope-accurate | scope-too-broad |
| 16 | Quality Matters | scope-too-narrow (free PDF carries all 44 specific standards) | scope-accurate (free material is the 8 general standards) |
| 18 | Mayer | scope-too-broad | scope-accurate with a correction |
| 21 | Kosslyn | scope-too-narrow (perception **and memory and comprehension**) | scope-accurate (perception) |
| 22 | SIFT + CRAAP | scope-too-broad | scope-accurate, CRAAP flagged |
| 25 | NIST SSDF | scope-accurate + currency caveat | scope-too-narrow |

Two of these are factual, not interpretive, and must be settled before anything is edited:

- **#17 IEEE 1028 status.** Browsing: **"Inactive-Reserved"**, inactivated 2019-11-07 for missing
  its revision window — an administrative lapse, no formal withdrawal. Deep research: **"formally
  withdrawn"**, withdrawn 07-11-2019. Same date, materially different legal status, and the
  deep-research source is a **standards reseller listing**, not IEEE. Resolve against IEEE directly.
- **#23 WCAG 2.2 recommendation date.** Browsing: "this version 12 Dec 2024". Deep research:
  "became a W3C Recommendation in October 2023". Both are probably right about different things
  (original REC vs. latest revision) and the library should say which it means.

And one where the runs are not in conflict but only one looked: **#24 FERPA/PTAC.** Browsing found
a June 2026 interagency agreement routing FERPA complaint review through DOJ, sourced to an ED press
release and corroborated by *Education Week*. Deep research found a re-awarded PTAC support contract
and no DOJ involvement. These are compatible facts; the DOJ change is the material one and only one
run has it.

## 3. Source quality differs, and it matters

The browsing run cites **primary sources** almost throughout: Sweller 1988 itself, Chi & Wylie's own
PDF, Fagan's IBM Systems Journal paper, Mayer's own study, the W3C and NIST and CAST pages.

The deep-research run leans on **secondary and tertiary sources** in several rows: a personal blog
review for Kosslyn and for Doumont, a **standards reseller** for the IEEE 1028 status, an
SEO-farm PDF at `internationalinsurance.org` for Kent Beck's TDD, and `csrc.nist.rip` — a mirror
domain, not `nist.gov` — for NIST.

**One citation does not match its claim.** Row 18 (Mayer, personalization) carries an inline URL of
`EJ944963.pdf` but its footnote `[^10]` resolves to `EJ1347324.pdf`, which is the CRAAP/CCOW paper
cited again at `[^13]`. The quote in that row is about Mayer; the footnote points at
information-literacy scholarship. This is precisely the untraceable-claim failure the handoff was
written to prevent, and it appeared anyway — in the run whose mode is optimised for synthesis.

That is a result, not just a complaint: it is direct evidence for the handoff's own reasoning that
synthesis-oriented modes damage traceability, and it is the reason the mode split should stay.

## 4. What both runs agree on — the safe-to-act list

These carry the same verdict in both, or appear in only the complete run with primary sourcing and
no contradiction:

- **#10 POGIL** — "validated mainly in sciences" holds; chemistry-dominant evidence base.
- **#11 UDL 3.0** — currency confirmed, July 2024, CAST's fifth iteration.
- **#20 Doumont** — non-empirical practitioner guide, unchanged since 2009.
- **#29 TDD** — Beck scopes it to programming; the skills extension is obra's, documented, not ours.
- **#25's addition** — both flag **SP 800-218A** (generative-AI companion profile, 2024) as missing
  from the library. This is the clearest *additive* finding of the whole exercise.
- **#17** — whatever its exact status, IEEE 1028 must stop being cited as an active standard.
- **#18** — Mayer's personalization principle was operationalized narrowly (a pronoun substitution in
  a narrated science animation) and cannot license general prose-level editing judgments. **This is
  the anchor that caused the recorded failure, and both runs independently confirm the diagnosis.**

## 5. Recommendation

1. **Treat the browsing run as the working draft baseline**, not because it is more confident but
   because it is complete and primarily sourced.
2. **Do not edit any of the 8 disputed anchors yet.** Settle #17 and #23 against the issuing bodies
   directly (IEEE, W3C), and treat #3, #7, #8, #16, #18, #21, #22, #25 as needing one tie-break pass
   each — these are scope-judgment calls where two readers of the same sources disagreed, which is
   exactly the case for a third read rather than for picking a winner.
3. **Act now only on the agreed list in §4**, and on the ten anchors the deep-research run never
   reached but the browsing run verified against primary sources with no contradicting reading.
4. **Keep both files.** The disagreement is the evidence, and a later round that sees only the
   winner cannot audit the call.

**What neither run establishes:** whether the pipeline is pedagogically sound. Both say so. That
remains faculty judgment.
