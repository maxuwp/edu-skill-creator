# Next moves — Fable's return on the idea-collection handoff

**From:** Claude (Fable 5), 2026-07-31, per `docs/HANDOFF_next_step_ideas_fable_grok.md`.
**What I checked before relying on §1:** read in full `docs/AUDIT_grounding_two_runs_compared.md`,
`docs/HANDOFF_reply_to_posed_circular_evidence.md`, and
`docs/CENSUS_evidence_levels_2026-07-31.md` (including the check-15 clause it quotes); the CR 1.20
findings attributed to me are mine; Grok's review is not in `docs/`, so where I use its findings
(B2/B3/B6/B7, the `c13` critical) I rely on the handoff's summary and say so. Stream A's health
claims match what I verified during the CR 1.20 review and are not re-checked here.

---

## 3.1 — Sequencing: the draft plan is right except for one decoupling

The plan's core instinct — design the provenance schema against a real population, not an imagined
one — is the correct lesson from this repo's history, and I would keep (i), (ii), (v) as drafted.
The correction is that **CR 1.21 is not one unit of work, and treating it as one is what makes the
question "defer or not" feel hard.** `c20` (the check-15 `computed_checks` fix: require the report
path, require the file, bind the hash, missing report = `unverifiable`) is the only row that fixes
a defect in shipped code, and its design depends on nothing in the grounding data — the fix was
fully specified in the POSED reply before the grounding audit existed. Pull `c20` (with `c21`,
which it needs for the third outcome) forward and gate it in the same session as CR 1.20 rev 2.
There is a second, unstated reason to bundle them: both touch the review-log contract, and every
schema change mints a new contract era. Gated a week apart, they produce two eras and double the
era-gate matrix that `c5`-style exemptions must reason over; gated together, the era cost is paid
once. The trade-off named: bundling violates the clean one-CR-one-gate discipline and makes the
rev-2 gate session heavier. I would pay that, because the alternative cost is structural (a
permanent extra era) rather than attentional (a longer afternoon). The rest of CR 1.21 — the
schema and process rows — waits for the grounding data *and* for 3.5's real generation run, which
is a better population than the grounding audit alone. One sequencing constraint the draft plan
implies but does not state: **`c31` (second-model census re-read) must complete before `c22` seeds
from the census.** Seeding a provenance registry from a level-3 self-classification and then
protecting it is precisely the protected-error scenario `c16` was written about; the census's own
§4 says so. Deferring CR 1.21's schema rows is safe *only* because `c20` no longer waits on them.

## 3.2 — Two vocabularies, one table

They are different axes, and the repo already contains the proof they cannot merge: the Mayer
operationalization. A 12-place pronoun substitution is *recomputable* — level 2, mechanically
verifiable, anyone can count the substitutions — and it is scope-invalid, which is why it produced
L14. High evidence level, wrong scope. Conversely, an anchor can be perfectly scope-accurate and
merely asserted (nobody has re-derived it). Check-provenance answers "who authored the operands of
this computation and can it support this conclusion"; anchor-scope answers "is this citation used
within what its source validated, and is that still current." One is a property fixed at authoring
time; the other decays (superseded, contested) and needs re-verification dates. A merged ordinal
scale would force nonsense comparisons — is `scope-too-broad` worse than `cross-checked`? — and
downstream authors will inevitably read one number as summarizing both. What breaks if they stay
fully separate is subtler: a generated rule needs *both* stamps to be trustworthy, and two
unlinked vocabularies let a rule cite a level-2 check resting on a superseded anchor with neither
noticing. So: two vocabularies, joined in one place — the check registry row carries its
provenance level *and*, where the check or rule cites an anchor, that anchor's current scope
verdict with its audit date. The join is a foreign key, not a merged scale. The trade-off: two
fields cost more registry ceremony per row; the alternative costs a category error baked into
every generated plugin.

## 3.3 — Contested anchors: state the license, not the dispute

The missing verdict is real, but a bare "contested" flag is the least useful of the options,
because the downstream author the handoff describes — not an expert in that literature — cannot
adjudicate a dispute; they can only over-weight it (stop trusting CLT entirely) or ignore it. What
they need is which *part* of the anchor is disputed and what may still be load-borne. The three
cases decompose cleanly: CLT's intrinsic/extraneous distinction stands while the germane-load
partition is dropped, so a rule resting on "reduce extraneous load" is safe and one resting on
"optimize germane load" is not; ICAP's category definitions are usable while the strict ordering
is not; Bloom's levels are usable as a vocabulary while claims that require the two dimensions to
be independent are not. So: extend the scope-limit sentence with a dated contested clause in the
affirmative form — *"Contested (2025): safe to load-bear on X; do not load-bear on Y; re-verify by
<date>"* — which is L9's decay discipline applied to frameworks. Costs of the alternatives, named:
a fourth column is signal without guidance; demotion to "suggestive" cascades — the grounding
doctrine flags unanchored stages as invented process, so demoting CLT forces stages into fake
re-anchoring onto weaker frameworks; mandatory fallbacks are mostly fictional (these are anchors
precisely because no equivalent substitute exists); doing nothing means the next audit re-flags
the same three anchors forever. The contested clause costs one sentence of expert judgment per
anchor at audit time — the only option whose cost lands on the person equipped to pay it.

## 3.4 — 8 of 14: both readings are true, on different rows, and there is a cheap test

The disagreements are not one population. Rows like #16 (what the free QM PDF contains) and the
two factual splits (#17, #23) are checkable facts, and there the sourcing evidence points one way:
the deep-research run disagreed while citing a reseller, a mirror domain, and a footnote that
resolves to the wrong paper. Reader failure, resolved at issuing bodies, no third opinion needed.
But rows #3 (Bloom: "purely a classification" vs "still described as a hierarchy") and #8 (ICAP)
are disagreements between two *true* sentences with different emphasis — and no amount of reader
care converges emphasis. For those rows I hold the second reading: a one-sentence descriptive
scope limit is an under-determined instrument, and a third read is a third sample from the same
under-determined instrument. The fix is the format: state the scope limit as a **decidable
license** — "this anchor licenses rules of form X and does not license rules of form Y" — because
two readers who diverge on how to *describe* Bloom will agree far more often on whether a
*specific rule* is licensed by it. That is also the instrument's actual job: its consumer is a
rule-author asking "may I ground this here," not a reviewer paraphrasing a framework. The
distinguishing test is direct and cheap: rewrite two or three disputed scope sentences in license
form, hand both readers the same candidate downstream rules, and ask licensed-or-not. If
agreement jumps, the instrument was the problem; if they still split, it was the readers, and a
third read regains its point. One afternoon, and it measures the format rather than buying
another opinion. Trade-off: license form is more work to author than a descriptive sentence and
can under-generalize (a rule form nobody anticipated is neither licensed nor forbidden) — accept
that, and let unanticipated forms route to the human gate, which is where genuinely novel
groundings belong anyway.

## 3.5 — What the project is walking past: the object level has never run

All four streams are meta. The repository lints itself, reviews its reviews, audits its grounding,
and designs contracts for a generated product that has never existed — the handoff's own candidate
list says it, and I think it is not one candidate among three but the dominant one, because it is
upstream of the other two open questions. **Generate one real plugin, for a real (small)
educational task, before any more enforcement ships.** Three returns, each currently
unobtainable any other way: it converts a large class of synthetic-harness claims into grounded
ones (the 1.19 suite builds a toy end-to-end, so the marginal cost of a real run is one session);
it produces the real check population CR 1.21's schema rows should be designed against — better
data than the grounding audit, which covers anchors, not checks; and it is the only way to observe
the *cost* side of the contract this project keeps growing — Grok's `c13` critical (per the
handoff's summary) worries that the full contract propagates into every generated plugin, and
today that worry is unmeasurable because no author, human or agent, has ever paid the contract's
price on a real task. The second thing being walked past, related: heterogeneity of evidence
sources. The Perplexity audit was the first genuinely external reader this project has used, and
it immediately produced the densest findings of any round — while `c26` (different-model review)
sits deferred. The lesson of stream D is that the marginal value of one *different kind* of reader
now exceeds the marginal value of another round from the same kind. The trade-off of the
generation run: it spends a session on object-level work while three CRs sit open, and its
findings will themselves demand triage. That is the point — it is the cheapest experiment that can
falsify assumptions all three CRs currently share.

## Proposed sequence, and the cost of the wrong order

1. Ship the uncontested grounding fixes (§4 safe-to-act list + the ten browsing-only,
   primary-sourced anchors). One file, no gate machinery.
2. Settle #17 and #23 at IEEE and W3C; fold in with (1).
3. CR 1.20 rev 2, incorporating both reviews; gate it together with `c20`+`c21` pulled forward
   from CR 1.21. One gate session, one new contract era.
4. **Generate one real plugin** (3.5). Harvest its findings.
5. Run the license-form test on two or three disputed anchors (3.4); reformat or third-read per
   its outcome; add contested clauses (3.3).
6. `c31` second-model census re-read; then write the remainder of CR 1.21 against the census, the
   grounding data, and the generation run's real population; gate.
7. Census second read of the grounding library folds into the next refresh cycle.

Costs of the wrong order, concretely: gating `c20` separately from rev 2 mints an avoidable
contract era (permanent, compounding); writing CR 1.21's schema rows before steps 4–6 repeats the
build-enforcement-before-knowing-the-population mistake the draft plan itself names, and seeding
`c22` before `c31` creates a protected level-3 baseline — the `c16` failure with a ledger to
defend it; running a third anchor read before the license-form test risks paying for a third
sample from a broken instrument and then still having to fix the instrument.

## The cut

**Cut the third tie-break read on the interpretive disputed anchors as currently designed.** The
comparison doc's recommendation 2 sends all eight disputed anchors to "one tie-break pass each."
For the factual rows the tie-break is the issuing body, already planned, and cheaper than a third
reader. For the interpretive rows (#3, #8, and the scope-judgment half of the rest), a third
descriptive read is a third opinion from an instrument the disagreement itself indicts; it
produces a 2-1 vote that settles the text without settling the license, and the next audit
re-opens it. The license-form test replaces it at similar cost with a falsifiable outcome. This is
a genuine cut, not a deferral: if the test shows agreement jumps under license form, the third
read never happens for those rows.

## Challenge-to-settled

None. I looked for one, specifically at "the browsing run is the stronger artifact" (verified: the
comparison doc's coverage table and sourcing section support it) and at the five-level scheme's
level 3, and found nothing worth the line.
