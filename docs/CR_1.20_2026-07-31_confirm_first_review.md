# CR 1.20 — Make the confirm-first review contract a mechanism, not a sentence

**Prepared by:** Claude (Opus 5), 2026-07-31, at Dr. Ma's direction.
**Status:** PROPOSED. Nothing here is implemented. Per-row gate required.
**Origin:** not a pilot harvest and not a release-history harvest. The source is a **method defect
observed live**, in this repository's own audit loop and independently in at least two other
threads and with other AI tools. The evidence is reproduced below and is unusually clean, because
the same loop was run five times with the brief changed once, in the middle.
**Already landed, and therefore NOT gated here:** lesson `L19_confirm_first_review.md` (authored in
the talk-like-a-professor thread, committed here in 1.18 with its cross-repo citations qualified),
its `lesson_index.md` row, and two prose wirings — the Stage 5 review dispatch in
`skills/draft/SKILL.md` and the Stage 8 ledger review in `skills/reflect/SKILL.md`. This CR covers
the remainder, which is the part that matters: **L19 is currently doctrine with no enforcement.**

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

## 2. The evidence

**Instance A — this repository, releases 1.14 to 1.19.** Five adversarial audit rounds, the brief
changed after round 3.

| Round | Brief | Outcome |
|---|---|---|
| 1 (→1.15) | defects only | fix reopened 1.14's citation defect |
| 2 (→1.16) | defects only | fix (suite case count) was self-reported and satisfiable by one `print()` |
| 3 (→1.17) | defects only | fix (recursion bound) was an environment-controlled off-switch that disabled the whole check |
| 4 (→1.18) | **confirm-first** | 20 findings, **none reopening a prior fix** |
| 5 (→1.19) | **confirm-first + carried-forward baseline** | auditors re-broke every baseline mechanism and reported 7/7 and 17/17 still firing; 9 of 10 findings in surfaces 1.18 had just touched; 1 regression, narrow, two-line fix |

Rounds 1–3 have a 3/3 reopening rate. Rounds 4–5 have 0/30. The only variable changed was the
brief.

**Instance B — the talk-like-a-professor thread.** Five rounds returned 5, 7, 8, 11 and 10
criticals, *increasing*. The same lexical criterion was rewritten wholesale four times. The round-5
reviewer diagnosed the criterion's architecture; the correct diagnosis was the method. When a
baseline artifact was finally built, it immediately caught two regressions that had already shipped
unnoticed.

**Instance C — POSED, where the reviser half is already solved.** Every audit review log carries
`strengths` and `preserve_units`, both passed to the reviser, enforced by the
`review_strengths_missing` check (CR 1.74 I-18, umbrella A14), so a regenerate cannot silently
discard what was working. The audit family's cumulative baseline lives in its own floor regression
ledger. **POSED is the worked precedent; this CR ports the pattern to Edu Skill Creator and, through
the scaffold, to every plugin Edu Skill Creator generates.**

**Instance D — reported by Dr. Ma across other threads and other AI tools.** Treat "give me
feedback" as *systematically* read to mean "list the violations", and correct for it in the brief
rather than hoping the reviewer infers it.

## 3. Why prose is not enough here

L19 says the right thing and nothing checks it. Every lesson in this repo that stayed prose-only has
drifted: L7's registry fold claimed enforcement by a lint check that did not exist and survived two
independent reviews; L11's central gate ("`approve` illegal without a recorded computed pass") was
asserted in four files and implemented in none until 1.18. This repo's own doctrine (L11, L13) says
any requirement code can check, code must check. A review contract is checkable: the review log is
a JSON file this repo already lints.

---

## 4. Decidable rows

Each row is independently decidable. Ids are stable and never recycled.

### Group A — the review log carries the baseline (the load-bearing change)

| id | change | why |
|---|---|---|
| `c1` | `skill_quality_rubric.md` output schema gains **`verified: [{property, how_verified, location}]`** — what the reviewer checked and found correct, with the mechanism and file:line. Not praise; each entry is a claim another round must keep true. | Without a durable record, the baseline dies with the reviewer's context. |
| `c2` | Same schema gains **`preserve: [<verified ids>]`** on each finding, plus **`modification`** — the smallest change that fixes it. `fix` (free prose) is replaced by these two. | Forces the finding to arrive as a modification and to name what it must not disturb. |
| `c3` | Iteration policy: **`approve` is illegal with an empty `verified`.** A review that confirmed nothing has not reviewed. | Mirrors POSED's `review_strengths_missing`. |
| `c4` | New **release lint check 17**: every `reviews/*.json` carries a non-empty `verified`, every finding carries `modification`, and every id in `preserve` resolves to a `verified` entry in the same file. Fail-closed; one negative fixture per branch. | L11: the requirement is checkable, so code checks it. |
| `c5` | **Era-gate `c4`** on a `review_contract_version` field, defaulting to "pre-1.20 = exempt". | L12. The 12 existing review logs predate the rule; a retroactive rule that condemns compliant history is the B2 defect recorded in POSED's own audit. **This row is why `c4` can ship at all.** |

### Group B — the cumulative regression ledger

| id | change | why |
|---|---|---|
| `c6` | Create a cumulative regression ledger at docs/REGRESSION_LEDGER.md (unbackticked: the file does not exist yet, and a CR must not cite a path as though it did — check 16 caught exactly that): one row per case any round has established — case, verdict, round that established it, why it is on the list. Verdict set is `confirmed` / `defect` / **`ambiguous`** / **`present-but-not-a-defect`**. | The last two verdicts are the ones usually missing, and they are where oscillation lives: a case with nowhere to go gets re-decided every round. |
| `c7` | **Lint check 18**: the ledger is non-empty; no row disappears without a recorded supersession; every `confirmed` row names either a suite case id or an explicit "not mechanisable, because …". | Makes the baseline monotone. A later round cannot fix one case by breaking an earlier one. |
| `c8` | Seed the ledger with the 24 baseline invariants rounds 4 and 5 verified (7 lint + 17 generated-surface), each already carrying its file:line. | The data exists in this session's audit records; not re-deriving it is the point of a ledger. |

### Group C — stage wiring beyond the two already landed

| id | change | why |
|---|---|---|
| `c9` | `edu-skill-creator-architecture`: every reviewer pairing names its regression ledger alongside its rubric. | The ledger is per-review-relationship, so it belongs where the relationship is designed. |
| `c10` | `edu-skill-creator-test`: RED/GREEN findings carry the confirmed set forward; a GREEN that breaks a confirmed property is a **regression, not a pass**. | Testing is a review loop too and has the same failure. |
| `c11` | `skill_quality_rubric.md` gains **critical flag 15**: "a review reports defects with no verified baseline, or a revision rewrites a unit the previous round verified without recording the trade". | Critical flags are how this repo makes a rule block rather than advise. |
| `c12` | `edu-skill-creator-refresh` and `edu-skill-creator-release` review dispatches get the confirm half. | Completes the sweep (L13: fix the class, not the instance). |

### Group D — the generated product

| id | change | why |
|---|---|---|
| `c13` | `edu-skill-creator-scaffold` generates, for every new plugin: the `verified`/`preserve`/`modification` schema fields, the ledger file, and checks 17–18 in the generated lint. | Highest blast radius. Every plugin this tool builds inherits either the defect or the fix. |
| `c14` | `dual_harness_playbook.md` review-brief template states the two halves verbatim, so a generated plugin's briefs are born correct. | Single source (L7). |

### Group E — evidence and honesty

| id | change | why |
|---|---|---|
| `c15` | L19 gains Instance A (the 3/3 → 0/30 table above) as a second independent instance, and cites POSED's shipped mechanisation as the precedent rather than describing it as new. | L16: the claim is now strong, so the evidence should be. |
| `c16` | Record in L19 what this method does **not** fix: it does not make a wrong baseline right. A property confirmed in error becomes protected error, and the ledger will defend it. Mitigation: `how_verified` must be a re-runnable mechanism, never "read it and it looked right". | Stating the limit is the L13 discipline. Flagged as the main risk of this CR. |

### Deferred, no action

| id | item | why deferred |
|---|---|---|
| `c17` | Machine-diffing consecutive review logs to auto-detect a dropped `verified` entry | Needs two rounds of the new schema to exist before the shape is knowable. Revisit after the first plugin builds under it. |
| `c18` | Extending the contract to the human gate (asking faculty what to preserve) | Adds gate load against the intent's budget (L4). Dr. Ma's call, not mine, and not urgent. |

---

## 5. Costs and risks, stated

**Reviewer cost rises.** A confirm pass makes each review longer — in rounds 4 and 5 the auditors
spent roughly a third of their effort on Part A. That is the price of the 3/3 → 0/30 change and it
is worth it, but L6 says name it rather than absorb it silently.

**`c16` is the real risk.** A protected baseline is only as good as its verification. In rounds 4
and 5 every baseline item was verified by mutation — break the mechanism, watch the guard fire —
and that standard is what makes the ledger trustworthy. A baseline of assertions would be worse
than no baseline, because it would be defended.

**`c5` is load-bearing.** Without the era gate, check 17 fails on twelve compliant historical
reviews the moment it ships.

## 6. Gate

Per-row, on the table above. Recommended: **approve A and B as a block** (they are one mechanism
split for reviewability, and A without B keeps the baseline per-round instead of cumulative);
**approve C and D**; **approve E**; **defer `c17`, `c18`**. `c5` is not optional if `c4` ships.

Nothing in this document is faculty approval, and nothing here is implemented.
