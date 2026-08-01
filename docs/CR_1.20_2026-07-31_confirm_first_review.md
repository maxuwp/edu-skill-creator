# CR 1.20 — Make the confirm-first review contract a mechanism, not a sentence

**Prepared by:** Claude (Opus 5), 2026-07-31, at Dr. Ma's direction.
**Revision 2**, 2026-07-31, after independent reviews by Fable (method and evidence lens,
`docs/REVIEW_CR_1.20_fable.md`) and Grok (design and blast-radius lens,
`docs/REVIEW_CR_1.20_grok.md`). Rev 1 is preserved in git history; this file supersedes it.
**Status:** PROPOSED. Nothing here is implemented. Per-row gate required.
**Origin:** not a pilot harvest and not a release-history harvest. The source is a **method defect
observed live**, in this repository's own audit loop and independently in other threads and with
other AI tools. The brief was changed once and then extended once, one round later, so the record
is two treatments rather than one clean intervention — corrected from rev 1, which called it a
single change (Fable F8).
**Already landed, and therefore NOT gated here:** lesson `L19_confirm_first_review.md`, its
`lesson_index.md` row, and two prose wirings — the Stage 5 review dispatch in
`skills/draft/SKILL.md` and the Stage 8 ledger review in `skills/reflect/SKILL.md`. This CR covers
the remainder, which is the part that matters: **L19 is currently doctrine with no enforcement.**

---

## 0. What rev 2 changes, and what it must not

This section exists because a revision that silently re-drafts is the defect this CR is about. Both
reviewers returned a confirm-first pass; those confirmations are this document's protected baseline.

**Confirmed by both reviews, carried forward unchanged.** The defect mechanism in §1 (Fable A1,
Grok A1). "Positive" meaning verified properties rather than praise (Grok A2). §3's argument that
prose-only rules drift in this repository, grounded in its own recorded failures (Fable A5, Grok A3).
The row set's accuracy against the current rubric schema, the fourteen existing critical flags, the
sixteen existing lint checks and the twelve historical review logs (Fable A2, A3; Grok A4, A5) — so
checks 17–18 are free ids and `c5` is arithmetic necessity, not caution. The POSED precedent exists
as shipped, enforced code (Fable A4, Grok A6). Group A alone is incomplete as multi-round memory, so
A and B are one mechanism (Grok A8). `c16` names the right residual risk (Fable A7, Grok A7). `c13`
is the highest-blast-radius row (Grok A9). **Rev 2 changes none of these, and no row below may be
implemented in a way that breaks one.**

**Modified, each traced to the finding that forced it.**

| Finding | Reviewer | Row(s) changed |
|---|---|---|
| Metric mixes denominators and censors the after-period | Fable F1 | §2, `c15` |
| Causal claim is confounded; the repo documents the confounds | Fable F2, Grok B6 | §2, `c15` |
| The brief changed twice, not once | Fable F8 | Origin, §2 |
| Instance C "already solved" overstates what was verified | Fable F7 | §2 |
| Instance D is author testimony carrying the broadest claim | Fable F5 | §2 |
| `how_verified` is unenforced, so the CR's main mitigation is prose | Fable F3, Grok B2, B7 | `c1`, `c4`, `c16` |
| Supersession is load-bearing and shapeless | Fable F4, Grok B3, B8 | `c6`, `c7`, `c16` |
| `c3` forbids an honest `regenerate` with nothing preservable | Grok B4 | `c3` |
| `c5`'s missing-version default is a permanent fail-open | Grok B5 | `c5` |
| `c13` propagates a research-repo contract into every faculty plugin | Grok B1 | `c13`, `c14` |
| Seed data lives only in session context | Fable F6 | `c8`, and the new appendix |
| Wire generators only after A+B are green here | Grok B9 | §6 |

**One correction neither reviewer could have made**, found while closing F6: rev 1's "24 baseline
invariants (7 lint + 17 generated-surface)" added *mutation* counts as though they were *property*
counts. The recovered enumeration is **8 lint-side and 18 generated-surface invariants, 26 rows**.
See `docs/APPENDIX_CR_1.20_baseline_seed.md`. A CR about protected baselines mis-stating the size of
its own baseline is worth recording rather than quietly fixing.

**Also pulled forward into this gate:** rows `c20` and `c21` from the scoped CR 1.21, for the reason
in §7.

---

## 1. The defect

Dr. Ma, on being shown a fifth non-converging review round:

> when you provide feedback, did you just list the violations? did you confirm what is right? a
> revision can't be a new draft, it should be a well informed modification.

And on the mechanism:

> Seems when i say provide feedback, it's always negative feedback. so the loop keeps continuing.

The failure is not that reviewers are wrong. It is that a **defects-only brief produces a redesign
where a modification was needed.** With no record of what the previous round verified as correct,
the author has no protected baseline, so each fix rewrites a surface that was already sound and
silently discards properties an earlier round had established. That is the mechanism by which one
round's fix becomes the next round's defect.

Codex's framing, which Dr. Ma endorsed and which this CR adopts as the definition:

> positive feedback here should not mean praise, it should mean **verified properties that become a
> protected baseline**.

## 2. The evidence, corrected

Rev 1 stated this as "3/3 → 0/30, the only variable changed was the brief". Both reviewers rejected
that form, independently and for the same reasons. It is restated here as what the record actually
supports. The mechanism is unaffected; only the evidence claim changes.

**Instance A — this repository, releases 1.14 to 1.19.** Five adversarial audit rounds.

| Round | Brief | Outcome |
|---|---|---|
| 1 (→1.15) | defects only | fix reopened 1.14's citation defect |
| 2 (→1.16) | defects only | fix (suite case count) was self-reported and satisfiable by one `print()` |
| 3 (→1.17) | defects only, and self-audited — both external auditors terminated on session limits | fix (recursion bound) was an environment-controlled off-switch that disabled the whole check |
| 4 (→1.18) | **confirm-first** | 20 findings; the fix-set produced one narrow regression, found in round 5 |
| 5 (→1.19) | **confirm-first + carried-forward baseline** | auditors re-broke every baseline mechanism and reported all of them still firing; 9 of 10 findings in surfaces 1.18 had just touched; 1 regression, narrow, two-line fix; **this fix-set has had no subsequent round, so its reopening count is unobserved** |

Measured consistently, per fix-set, which is how rounds 1–3 were counted: **rounds 1–3 reopened a
prior property three times out of three, wholesale; round 4 produced one narrow regression, caught
by the baseline re-verification; round 5 is not yet observable.** The qualitative shift is the
sturdier claim and survives attack: rounds 1–3 each replaced a mechanism wholesale and each
replacement carried the next defect (floor → print-satisfiable; bound → off-switch), while round 5's
fixes are narrow in-place modifications.

**Confounds, named rather than absorbed.** The brief was the deliberately changed variable, and
three things changed with it: the deterministic suite grew from 25 to 78 falsifiable cases *before*
round 4, so by then prior fixes were mechanically pinned and a reopening would trip the suite
regardless of brief; round 3 had no external auditors, so auditor identity changed too; and by round
4 three rounds had already swept the older surfaces, which is consistent with 1.19 reporting nine of
ten findings in surfaces 1.18 had just touched. Attribution is therefore to the combination, and
**the component this repository's own evidence most directly supports is the mechanised baseline**,
not the brief's prose. That direction argues *for* Groups A and B, which are the mechanisation, and
it weakens only the rows that rest on wording.

**Instance B — the talk-like-a-professor thread.** Five rounds returned 5, 7, 8, 11 and 10
criticals, *increasing*. The same lexical criterion was rewritten wholesale four times. When a
baseline artifact was finally built, it immediately caught two regressions that had already shipped
unnoticed. Note the same direction as the confounds above: the convergence event was the *artifact*
existing, not a rewording. Not independently examinable from this workspace; the narrative was
checked for internal consistency with L19 only.

**Instance C — POSED, where the reviser half is shipped and enforced.** Every audit review log
carries `strengths` and `preserve_units`, both passed to the reviser, enforced fail-closed by the
`review_strengths_missing` check, so a regenerate cannot silently discard what was working. This is
precedent for **feasibility**, verified in shipped code. It is not evidence of outcome: no
measurement of reopening rates in POSED exists, and POSED's check permits an empty `preserve_units`,
a weaker contract than this CR proposes. This CR strengthens the pattern rather than porting it
unchanged.

**Instance D — author-reported, not independently examinable here.** Dr. Ma reports the same
defects-only reading across other threads and other AI tools. The systematic-misreading claim is
scoped to what Instances A–C support, plus this testimony named as testimony.

## 3. Why prose is not enough here

L19 says the right thing and nothing checks it. Every lesson in this repo that stayed prose-only has
drifted: L7's registry fold claimed enforcement by a lint check that did not exist and survived two
independent reviews; L11's central gate ("`approve` illegal without a recorded computed pass") was
asserted in four files and implemented in none until 1.18 — and, as `c20` below records, the
implementation it finally got does not read the evidence it names. This repo's own doctrine (L11,
L13) says any requirement code can check, code must check. A review contract is checkable: the
review log is a JSON file this repo already lints.

---

## 4. Decidable rows

Each row is independently decidable. Ids are stable and never recycled. **Bold text marks what rev 2
changed.**

### Group A — the review log carries the baseline (the load-bearing change)

| id | change | why |
|---|---|---|
| `c1` | `skill_quality_rubric.md` output schema gains **`verified: [{property, how_verified, how_verified_kind, location}]`** — what the reviewer checked and found correct, with the mechanism and file:line. **`how_verified_kind` is a closed set: `mutation` \| `command` \| `diff` \| `schema` \| `human_gate` \| `other`, and `other` requires a non-empty reason.** Not praise; each entry is a claim another round must keep true. | Without a durable record, the baseline dies with the reviewer's context. The closed kind is what makes the next row's check possible at all (Grok B2). |
| `c2` | Same schema gains **`preserve: [<verified ids>]`** on each finding, plus **`modification`** — the smallest change that fixes it. `fix` (free prose) is replaced by these two. | Forces the finding to arrive as a modification and to name what it must not disturb. |
| `c3` | Iteration policy: **`approve` is illegal with an empty `verified`.** **An entry may record negative ground — "no unit meets threshold X", verified by command or mutation — so an honest `regenerate` with nothing preservable is expressible without fabricating positives.** | Mirrors POSED's `review_strengths_missing`. The negative-ground clause stops the rule from forcing fake positives on a genuinely unsalvageable artifact (Grok B4). |
| `c4` | New **release lint check 17**: every `reviews/*.json` carries a non-empty `verified`, every finding carries `modification`, and every id in `preserve` resolves to a `verified` entry in the same file. **Each `verified` entry must name a runnable mechanism — a suite case id, a command, or an explicit "not mechanisable, because …" — and at least one entry must be of kind `mutation`, `command`, `diff` or `schema`, so a log of "read it and it looked right" cannot pass.** Fail-closed; one negative fixture per branch. | L11: the requirement is checkable, so code checks it. Without the added clause the CR's own §5 risk statement is unenforced prose, and non-emptiness is satisfiable by boilerplate — the same family as the `print()`-satisfiable count of round 2 (Fable F3, Grok B7). |
| `c5` | **Era-gate `c4`** on a `review_contract_version` field. **Exempt only if the field is absent AND the file predates the 1.20 release (by recorded review date or release tag), or the field explicitly reads `pre-1.20`. A post-era log with no version fails check 17.** | L12, and the fix for the fail-open: defaulting *missing* to *exempt* would make every future log exempt by omission (Grok B5). **This row is why `c4` can ship at all.** |

### Group B — the cumulative regression ledger

| id | change | why |
|---|---|---|
| `c6` | Create a cumulative regression ledger at docs/REGRESSION_LEDGER.md (unbackticked: the file does not exist yet, and a CR must not cite a path as though it did): one row per case any round has established — case, verdict, round that established it, why it is on the list. Verdict set is `confirmed` / `defect` / **`ambiguous`** / **`present-but-not-a-defect`**. **Lifecycle is a separate `status` column (`active` \| `superseded`), not a fifth verdict, with `superseded_by`, `reason` and `changed_in_round`.** | The two extra verdicts are where oscillation lives: a case with nowhere to go gets re-decided every round. Keeping lifecycle out of the verdict set stops "superseded" from competing with "confirmed" as a truth claim (Grok B8). |
| `c7` | **Lint check 18**: the ledger is non-empty; no row disappears without a recorded supersession; every `confirmed` row names either a suite case id or an explicit "not mechanisable, because …". **A supersession record must carry: the superseded row id; a demonstration that the original verification was faulty *as a mechanism* — re-run the recorded `how_verified` against the case it should have caught and show it passing — the round and reviewer; and routing to the human gate for the demotion itself. Agents may propose a supersession; only the human gate may enact one. Silent deletion is an error.** | Makes the baseline monotone without making it despotic. An undefined escape hatch degenerates one of two ways — too easy and the ledger is decorative, too hard and a wrong row is defended, which is exactly the `c16` failure (Fable F4, Grok B3). |
| `c8` | Seed the ledger from **`docs/APPENDIX_CR_1.20_baseline_seed.md`** — **26 rows now in the repository** (8 lint-side, 18 generated-surface), each with its invariant text and its breaks-if clause. **Seeding must re-anchor line numbers to current code and record the re-anchoring, and must not mark a row `confirmed` on the appendix alone: the honest initial verdict is "confirmed as of 1.19, by mutation, re-verification pending".** | Rev 1's seed data existed only in session context, for a ledger whose stated point is not re-deriving (Fable F6). Now closed. The appendix also corrects rev 1's count. |

### Group C — stage wiring beyond the two already landed

| id | change | why |
|---|---|---|
| `c9` | `edu-skill-creator-architecture`: every reviewer pairing names its regression ledger alongside its rubric. | The ledger is per-review-relationship, so it belongs where the relationship is designed. |
| `c10` | `edu-skill-creator-test`: RED/GREEN findings carry the confirmed set forward; a GREEN that breaks a confirmed property is a **regression, not a pass**. | Testing is a review loop too and has the same failure. This is the row §2's confounds most directly support. |
| `c11` | `skill_quality_rubric.md` gains **critical flag 15**: "a review reports defects with no verified baseline, or a revision rewrites a unit the previous round verified without recording the trade". | Critical flags are how this repo makes a rule block rather than advise. |
| `c12` | `edu-skill-creator-refresh` and `edu-skill-creator-release` review dispatches get the confirm half. | Completes the sweep (L13: fix the class, not the instance). |

### Group D — the generated product

| id | change | why |
|---|---|---|
| `c13` | `edu-skill-creator-scaffold` generates the `verified`/`preserve`/`modification` schema, the ledger file and checks 17–18 **as a named optional module, not as the default shape of every plugin. Default ON for multi-stage authoring plugins that have independent reviewers; OFF for single-skill or no-reviewer pipelines. The generated lint emits checks 17–18 only when the flag is on. Held until the contract has run one full internal round here.** | Highest blast radius. A faculty plugin that never runs a multi-round adversarial audit would otherwise pay the full schema, ledger and lint surface, and the likeliest result is empty `verified` lists that satisfy the lint without doing the method (Grok B1). Scoped, not removed. |
| `c14` | `dual_harness_playbook.md` review-brief template states the two halves verbatim, **and states the one-sentence rule for when to enable the module: turn it on when you have a review loop.** | Single source (L7). |

### Group E — evidence and honesty

| id | change | why |
|---|---|---|
| `c15` | L19 gains Instance A **in the corrected form of §2** — per-fix-set rates, round 5 marked unobserved, the three confounds named in one sentence, and the attribution given to the combination with the mechanised baseline as the best-supported component. POSED is cited as shipped and enforced, not as solved. | L16: the burden scales with the claim. Baking rev 1's form into doctrine would put a confounded attribution into the lesson every future plugin inherits (Fable F1/F2/F7/F8, Grok B6). |
| `c16` | Record in L19 what this method does **not** fix: a property confirmed in error becomes protected error, and the ledger will defend it. **The mitigation is no longer prose — it is `c4`'s runnable-mechanism clause and `c7`'s supersession shape. Add the caveat that protected error's likeliest home is the `present-but-not-a-defect` verdict, which certifies an absence and is the hardest verdict to falsify by mutation.** | Stating the limit is the L13 discipline; binding it is the L11 discipline. Rev 1 did the first only (Fable F3/F4). |

### Pulled forward from CR 1.21 — the one live defect in shipped code

| id | change | why |
|---|---|---|
| `c20` | Fix check 15's `computed_checks` clause: **require the report path, require the file to exist, bind its hash, and treat a missing or unreadable report as `unverifiable` rather than as a pass.** | L11's central gate currently authorizes `approve` on a boolean the reviewing agent wrote about its own conduct. Nothing opens the report it names. The prose in `skills/scaffold/SKILL.md` and the validator template's own header already promise the stricter contract; the code delivered less under the same name. |
| `c21` | Add the third outcome (**`unverifiable`**) to the lint's vocabulary, and to the generated lint the scaffold emits. | The lint has two outcomes, error and clean, so "I could not tell" has nowhere to go and becomes clean. `c20` needs the third outcome to express its failure honestly. |

**Why these two are in this gate and the rest of CR 1.21 is not.** They change the same contract
Group A changes — what a review log must carry for a gate to trust it. Gated a week apart they mint
two contract eras and permanently double the exemption matrix `c5` must reason over; gated together
the era cost is paid once. The rest of CR 1.21 waits for a real population to design against.
`c19`'s lesson ships as **L21**, since L20 went to Foundation Regress.

### Deferred, no action

| id | item | why deferred |
|---|---|---|
| `c17` | Machine-diffing consecutive review logs to auto-detect a dropped `verified` entry | Needs two rounds of the new schema to exist before the shape is knowable. Both reviewers agree. |
| `c18` | Extending the contract to the human gate (asking faculty what to preserve) | Adds gate load against the intent's budget (L4). Dr. Ma's call, not mine, and not urgent. |

---

## 5. Costs and risks, stated

**Reviewer cost rises.** A confirm pass makes each review longer — in rounds 4 and 5 the auditors
spent a substantial share of their effort on Part A, though no repository artifact measures effort,
so that share is an impression and is labelled as one. L6 says name the cost rather than absorb it.

**`c16` is still the real risk, and it is now bound rather than described.** A protected baseline is
only as good as its verification. In rounds 4 and 5 every baseline item was verified by mutation, and
`c4` now requires that standard of at least one entry per log rather than recommending it.

**`c5` is load-bearing in both directions.** Without the era gate, check 17 fails on twelve compliant
historical reviews the moment it ships. Without rev 2's tightening, every future log is exempt by
forgetting a field.

**The `c13` decision is the expensive one to walk back.** It is the only row that reaches faculty who
will never see this repository, and rev 2 scopes it to a flag and holds it behind one internal round.

## 6. Gate

Per-row, on the tables above. Recommended sequence, on which both reviewers converged:

1. **Group A (`c1`–`c5`) plus Group B (`c6`–`c8`) as one block**, with rev 2's modifications. They
   are one mechanism split for reviewability: A without B keeps the baseline per-round instead of
   cumulative. `c4` does not ship without `c5`.
2. **`c20` and `c21` in the same gate session**, for the contract-era reason in §4.
3. **Group C (`c9`–`c12`)** once A and B are green on this repository's own reviews.
4. **Group D (`c13`, `c14`) last**, behind the scope flag, and only after one internal round has run
   under the new schema.
5. **Group E (`c15`, `c16`)** with the corrected evidence; Fable would gate these first, since every
   other row is cited against this evidence record, and that ordering is compatible with the above.
6. **Defer `c17` and `c18`.**

Nothing in this document is faculty approval, and nothing here is implemented.

## 7. What rev 2 does not settle

- Whether the mechanised baseline or the brief's prose is doing the work. §2 now says the evidence
  favours the mechanism; distinguishing them would need a round with the brief reverted and the
  suite held constant, which nobody has run.
- Whether `c13`'s flag defaults are right. They are a judgment about faculty plugins that have never
  been built; the first real plugin is the test.
- Whether the appendix's recovered rows are still true. They record a verification performed against
  1.18 and 1.19 and recovered from transcripts, and `c8` requires re-anchoring rather than trust.
