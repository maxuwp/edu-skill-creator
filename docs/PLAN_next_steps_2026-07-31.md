# Decided plan — next steps, after Fable's and Grok's idea passes

**Date:** 2026-07-31, release 1.19. **Inputs:** `docs/IDEAS_next_steps_fable.md`, Grok's return
(reproduced in this thread), `docs/AUDIT_grounding_two_runs_compared.md`, both CR 1.20 reviews.
**Status:** a plan, not an approval. Steps 1–2 are edits to one reference file and need Dr. Ma's
go-ahead; steps 3 onward each carry their own gate.

**Why this document exists:** two idea passes agreed on all five open questions. Leaving two files
and no decision would recreate the accumulation problem the brief was written to name.

---

## 1. Where the two passes agreed, and what decided each fork

| Question | Both said | What decided it |
|---|---|---|
| 3.1 sequencing | Do **not** wait for a full CR 1.21 before fixing check 15 | Fable's **contract-era** argument: `c20`/`c21` and CR 1.20 rev 2 both change the review-log contract, so gating them apart mints two eras and permanently doubles the era-gate matrix. Grok reached the same place by a different route (a surgical patch), but did not consider era cost. **Bundle, per Fable.** |
| 3.2 one scheme or two | **Two vocabularies, joined by a foreign key in one registry row** | Fable's proof, which is genuinely decisive: the Mayer case is *level-2 recomputable* — anyone can count the 12 pronoun substitutions — **and** scope-invalid. High evidence level, wrong scope. The axes are orthogonal, so a merged ordinal scale would ask whether `scope-too-broad` is worse than `cross-checked`. |
| 3.3 contested anchors | A bare "contested" flag is the **weakest** option | Fable's affirmative dated clause — *"Contested (2025): safe to load-bear on X; not on Y; re-verify by ⟨date⟩"* — **plus** Grok's behavioural rule that a contested anchor may not sole-authorize a fail-closed student-facing gate. These are complementary: one states the license, the other constrains authorization. **Take both.** |
| 3.4 the 8 disagreements | The population **splits**: factual rows are reader failure, interpretive rows are instrument failure | Fable's license-form test, which is falsifiable and doubles as the fix. |
| 3.5 what we walk past | **Generate one real plugin** | Both ranked it first. Fable's addition: it is *upstream* of 3.2 and 3.4, because it produces the real check population CR 1.21's schema needs, and it is the only way to measure the cost side of the contract `c13` propagates. |

## 2. The three cuts — taken, and recorded as cuts

My own complaint in the brief was that nothing in this project has ever been deliberately dropped.
All three proposed cuts are compatible; all three are taken.

1. **Cut the third tie-break read on the interpretive disputed anchors** (Fable). The comparison
   doc sent all eight to "one tie-break pass each." For the factual rows the tie-break is the
   issuing body, cheaper and already planned. For the interpretive rows a third *descriptive* read
   is a third sample from the instrument the disagreement indicts — it buys a 2-1 vote that settles
   the text without settling the license, and the next audit reopens it. **Replaced by the
   license-form test.** Not a deferral: if agreement jumps under license form, it never happens.
2. **Cut "the next deliverable is another complete CR"** (Grok). The repository is healthy. The
   next integrity win is one clause in check 15 plus a durable rev 2, not more unfixed surface.
3. **Cut `c13`-by-default** (Grok, and Fable's cost argument). The confirm-first contract propagates
   into every generated plugin under an **opt-in flag** until one real plugin has been generated
   under it. Nobody — human or agent — has yet paid this contract's price on a real task, so its
   cost is currently unmeasured.

## 3. The sequence

**Step 1 — ship the uncontested grounding fixes.** One file, no gate machinery, breaks nothing.
The §4 safe-to-act list plus the ten anchors the browsing run verified against primary sources with
no contradicting reading. Highest-value single edit: **#18 Mayer**, rewritten so it cannot be read
as licensing prose-level editing — the anchor that caused the failure L14 records, confirmed
independently by both audit runs. Also: the **Mager/ABCD conflation** split (ABCD is not Mager's),
**NIST SP 800-218A** added as a companion anchor, and **IEEE 1028** stops being cited as active
whatever its exact status turns out to be.

**Step 2 — settle the two factual splits at their issuing bodies.** IEEE on 1028's status
(inactive-reserved vs. formally withdrawn — the deep-research claim rests on a standards reseller),
W3C on WCAG 2.2's recommendation date. Folds into step 1's release.

**Step 3 — CR 1.20 rev 2, gated together with `c20` and `c21` pulled forward from CR 1.21.**
Rev 2 folds in: the corrected metric and named confounds (Fable F1/F2/F8, Grok B6); `how_verified`
must name a runnable mechanism, so the CR's own main mitigation binds (Fable F3, Grok B2/B7);
supersession gets a required shape and an authority (Fable F4, Grok B3); `c8`'s seed enumeration
lands in the repository before the gate rather than expiring with this session (Fable F6); `c3`
admits negative ground so an honest `regenerate` is expressible (Grok B4); `c5` closes the
missing-version fail-open (Grok B5); `c13` becomes opt-in (cut 3). One gate session, one new
contract era.

**Step 4 — generate one real plugin, for a real small educational task.** The object level has
never run. Every claim about the generated-product surface currently rests on a synthetic harness
this repo also wrote. Harvest its findings before designing more schema.

**Step 5 — the license-form test.** Rewrite two or three disputed scope sentences as decidable
licenses, hand both readers the same candidate downstream rules, ask licensed-or-not. Agreement
jumps → the instrument was the problem, reformat the library. Still split → the readers were, and
the third read regains its point. Then add the contested clauses from §1.

**Step 6 — `c31` second-model census re-read, then the remainder of CR 1.21.** Ordering constraint
Fable identified and the draft plan missed: **`c31` must complete before `c22` seeds a provenance
registry from the census.** Seeding a protected baseline from a level-3 self-classification and
then defending it is exactly the `c16` failure, with a ledger to enforce it.

## 4. Costs of the wrong order

- Gating `c20` apart from rev 2 mints an avoidable contract era — permanent and compounding, where
  the alternative cost is one longer gate session.
- Writing CR 1.21's schema rows before steps 4–6 repeats this repo's recurring mistake: building
  enforcement before understanding the population it enforces over.
- Seeding `c22` before `c31` creates a protected level-3 baseline.
- A third anchor read before the license-form test buys a third sample from a possibly broken
  instrument, and the instrument still needs fixing afterwards.
- Deferring the check-15 fix for a complete CR leaves the one live authorizing hole open: any review
  writing `computed_checks.*_validator_pass: true` can launder L11's central gate.

## 5. Carried forward, not settled

- **Grok's narrow challenge**, accepted as open: the five-level scheme is settled *as a concept*,
  but whether it fits a release lint without a lint-specific definition of level 1 (repo bytes) is
  not. This is already the last question in `docs/HANDOFF_census_reclassification.md`; it now has a
  second voice behind it.
- **Numbering collision.** CR 1.20 is named for a release that does not exist yet, and step 1 would
  naturally ship as release 1.20. Either the grounding release takes a different number or CR ids
  and release numbers are formally decoupled. Small, but it will confuse the changelog if left.
- **Heterogeneity as a finding in its own right** (Fable). The Perplexity audit was this project's
  first genuinely external reader and produced the densest findings of any round, while `c26`
  (prefer a different model for independent review) sits deferred. The marginal value of a
  *different kind* of reader now exceeds another round from the same kind.
