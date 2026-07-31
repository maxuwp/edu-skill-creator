# Idea-collection handoff — what should edu-skill-creator do next?

**For:** Fable and Grok, independently. **From:** the edu-skill-creator thread, 2026-07-31.
**This is not a review.** The last two handoffs asked you to confirm and correct a document. This
one asks a different question: given four workstreams that have started interacting, **what is the
right next move, and what are we not seeing?** Divergent, not adversarial. Proposals with
trade-offs, not verdicts.

**But keep the confirm-first discipline in one direction:** §2 lists what is settled. Do not spend
your pass reopening it. If you think something in §2 is wrong, say so in one line marked
`challenge-to-settled` and move on — it will be routed separately rather than folded in here.

---

## 1. Where things stand

Four streams, all live, all touching each other.

**A. The repository itself — healthy.** Release 1.19. Release lint 16 checks, 0 errors; 104
deterministic cases, 99 falsifiable; the generated-product harness is tested end to end. Five
adversarial audit rounds are behind it. This is not where the risk is.

**B. CR 1.20 — confirm-first as mechanism.** 18 rows. Both of you reviewed it. Converging findings:
the 3/3 → 0/30 metric mixes denominators and is confounded (Fable F1/F2/F8, Grok B6); `how_verified`
is unenforced prose so the mitigation for the CR's own main risk does not bind (Fable F3, Grok
B2/B7); supersession is shapeless (Fable F4, Grok B3). Grok's critical: `c13` propagates the whole
contract into every generated plugin with no opt-out. Fable's blocker: `c8`'s seed data exists only
in session context and will expire. **Rev 2 is owed and not yet written.**

**C. CR 1.21 — circular evidence.** Scoped, 13 rows, not written. Came from the POSED thread's
handoff: a claim must not be called verified when all its operands share one authoring provenance.
Five evidence levels, grounded → recomputed → cross-checked → independently-reviewed → asserted. A
census of this repo's own lint found one real instance: check 15's `computed_checks` clause
authorizes a gate on a boolean the reviewing agent wrote about its own conduct, and nothing opens
the validator report it names.

**D. The grounding library — just audited for the first time.** 30 anchors, run twice through
Perplexity (agentic browsing, and deep research). Results in
`docs/AUDIT_grounding_two_runs_compared.md`. Headlines:

- **7 anchors need their scope sentence re-scoped**, 3 need their citation repointed, 1 is a
  conflation of two different lineages ("Mager / ABCD" — ABCD is not Mager's), 1 addition is
  clearly missing (NIST SP 800-218A, the generative-AI companion profile).
- **The recorded prior failure is confirmed by both runs.** Mayer's personalization principle was
  operationalized as a 12-place "the"→"your" substitution in a narrated science animation. It
  cannot license prose-level editing judgments. That is the defect that produced lesson L14.
- **Three anchors are contested rather than wrong** — Cognitive Load Theory (germane load formally
  dropped by Kalyuga & Plass 2025), ICAP (ordering not replicating, one reversed result), Bloom
  (two dimensions found non-independent). The library has no vocabulary for "real, cited correctly,
  and actively disputed."
- **The two runs disagree on 8 of the 14 anchors both covered.**

## 2. Settled — do not reopen

- The confirm-first method itself, and that "positive feedback" means verified properties rather
  than praise. Faculty-endorsed.
- Lesson L19 and its index row; the Stage 5 and Stage 8 prose wirings. Shipped in 1.18.
- The five-level evidence scheme as a *concept*. Whether it fits a release lint is open (§3.4).
- That the browsing grounding run is the stronger artifact — complete coverage, primary sources.
  Whether it is *right* on the 8 disputed anchors is open.
- Releases 1.14–1.19 and everything in them.

## 3. The open questions — this is what I want from you

Answer the ones you have something real to say about. Skip the rest; a thin answer to all five is
worth less than a good answer to two.

**3.1 — Sequencing. What order, and what does the wrong order cost?**
My draft plan: (i) ship the uncontested grounding fixes now, since they touch one file and need no
gate machinery; (ii) settle the two factual questions at their issuing bodies; (iii) CR 1.20 rev 2,
then gate; (iv) write CR 1.21 *after* the grounding data exists, so the provenance schema is
designed against a real population rather than an imagined one; (v) census second read.
The reasoning behind (iv) is that this repo's recurring mistake has been building enforcement
before understanding the population it enforces over. **Is that the right read, or does deferring
CR 1.21 leave the one live defect (check 15) open longer than it should be?**

**3.2 — Are anchor-provenance and check-provenance the same scheme, or am I conflating them?**
CR 1.21 proposes a `provenance` field on every *check registry row* — about who authored the
operands of a computation. The grounding audit just produced, empirically, a per-*anchor* verdict:
scope-accurate, scope-too-broad, superseded, unverified. These feel related and I am not sure they
are. One is about evidence for a claim a script makes; the other is about whether a citation is
used within what its source validated. **Should these be one vocabulary or two, and what breaks
either way?**

**3.3 — The library has no verdict for "real but contested." What should it have?**
CLT, ICAP and Bloom are correctly cited, within scope, and under active empirical challenge. Today
the library's only structure is `Framework | Grounds | Scope limit`. Options I can see: a fourth
column for contestation; demote contested anchors to "suggestive, not load-bearing"; require any
rule grounded on a contested anchor to name a fallback; or do nothing and let the scope-limit
sentence carry it. **What would you do, and what does each option cost a downstream plugin author
who is not an expert in that literature?**

**3.4 — 8 of 14 disagreements: whose failure is that?**
Two careful readers of the same primary sources disagreed on more than half the scope sentences
they both examined. The obvious reading is that one reader was sloppier — and the sourcing
evidence supports that. But there is a second reading: **a one-sentence scope limit may be an
under-determined instrument**, and two honest readers will diverge on it no matter how careful they
are. If that is right, a third read is not the fix, and the format is. **Which reading do you hold,
and what is the test that would distinguish them?**

**3.5 — What are we not seeing?**
Four streams, one repository, one faculty member's attention. Name the thing this project is
walking past. Candidates I am aware of and have not prioritised: no plugin has ever actually been
generated by this tool, so the whole generated-product surface is verified only by synthetic
harnesses; the refresh stage has never run; nothing has been tested with a faculty member who is
not Dr. Ma. **You may have better candidates than mine.**

## 4. What to return

1. **One paragraph per question you answer**, with the trade-off named, not just the recommendation.
2. **A proposed sequence** for the four streams, with the cost of getting it wrong.
3. **One thing you would cut.** There are three CRs' worth of proposed work and one repository. If
   something here is not worth doing, saying so is the most valuable thing you can return —
   proposals accumulate and nothing in this project has yet been deliberately dropped.
4. Anything in §2 you think is wrong, one line each, marked `challenge-to-settled`.

No confirm-pass is required this time, because you are not judging an artifact. But if you rely on
a claim in §1, say how you checked it — several are summaries of documents you have not read, and
`docs/` holds all of them.
