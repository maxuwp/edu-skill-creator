# Review handoff — CR 1.20 (confirm-first review contract)

**For:** two independent reviewers, **Fable** and **Grok**, working separately. Do not share
drafts; the value is in the disagreement.
**Subject:** `docs/CR_1.20_2026-07-31_confirm_first_review.md` in
`github.com/maxuwp/edu-skill-creator` (local: `~/Documents/claudecode/edu-skill-creator-plugin`).
**Status of the subject:** PROPOSED. Nothing in it is implemented. Your review feeds a per-row gate
held by Dr. Xiaoguang Ma (UW-Platteville).
**Self-containment:** this document carries everything needed to review without repo access. If you
have the repo, read the CR itself — **where this handoff and the CR differ, the CR governs.**

---

## 0. How to give feedback here — read this first, it is the subject matter

This CR exists because review briefs that ask only "what is wrong" made a five-round loop diverge.
A brief for reviewing *that* CR must not repeat the defect. So:

**Your review has two parts and Part A is not optional.**

- **Part A — CONFIRM.** What in this CR is correct, well-evidenced, and load-bearing, and *how you
  checked*. Not praise. Each entry is a claim the author is then obliged to keep true: it becomes a
  do-not-break baseline for the next revision. State it as "X holds, verified by Y".
- **Part B — DEFECTS, EACH AS THE SMALLEST MODIFICATION.** For each: severity, which row (`c1`…`c18`)
  or section it lands on, what is wrong, **the smallest change that fixes it**, and **which Part A
  items that change must not disturb**. If only a redesign will do, say so and say why a
  modification cannot work — but propose a redesign only then.

If you find yourself writing a new version of a row rather than a modification to it, stop: that is
the exact failure mode under review.

---

## 1. What the CR proposes, in one paragraph

A defects-only review brief produces a *redesign* where a *modification* was needed, because the
author has no record of what the previous round verified as correct. The CR makes the missing record
a mechanism rather than a habit: review logs gain a `verified` array (properties confirmed, with how
they were verified), findings gain `preserve` (which verified items the fix must not break) and
`modification` (the smallest change), `approve` becomes illegal with an empty `verified`, two new
release-lint checks enforce it, and a cumulative regression ledger carries the baseline across
rounds so a later fix cannot silently undo an earlier one. The scaffold then generates all of it
into every plugin the tool builds.

## 2. The evidence the CR rests on

**Instance A — the subject repository, releases 1.14 → 1.19.** Five adversarial audit rounds. The
brief was changed once, after round 3, from defects-only to confirm-first.

| Round | Brief | Outcome |
|---|---|---|
| 1 (→1.15) | defects only | the fix reopened 1.14's citation defect |
| 2 (→1.16) | defects only | the fix (a suite case count) was self-reported: one `print()` satisfied it |
| 3 (→1.17) | defects only | the fix (a recursion bound) was an environment variable that disabled the whole check |
| 4 (→1.18) | confirm-first | 20 findings, none reopening a prior fix |
| 5 (→1.19) | confirm-first + carried-forward baseline | auditors re-broke every baseline mechanism and reported 7/7 and 17/17 still firing; 9 of 10 findings in surfaces 1.18 had just touched; 1 narrow regression |

Reopening rate: **3 of 3** before, **0 of 30** after.

**Instance B — a sibling project (talk-like-a-professor).** Five rounds returned 5, 7, 8, 11, 10
criticals — increasing. One criterion was rewritten wholesale four times. A baseline artifact, once
built, immediately caught two regressions that had already shipped unnoticed.

**Instance C — POSED (the author's other plugin), where half of this is already shipped.** Audit
review logs carry `strengths` and `preserve_units`, both passed to the reviser, enforced by a
`review_strengths_missing` check. This CR ports that pattern and adds the cumulative ledger.

**Instance D — Dr. Ma reports the same pattern in other threads and with other AI tools.**

## 3. The decidable rows you are reviewing

**Group A — the review log carries the baseline.**
`c1` output schema gains `verified: [{property, how_verified, location}]` ·
`c2` findings gain `preserve: [verified ids]` and `modification`, replacing free-prose `fix` ·
`c3` `approve` illegal with an empty `verified` ·
`c4` new lint check 17 enforcing all of the above, fail-closed, one negative fixture per branch ·
`c5` era-gate check 17 on a `review_contract_version` so twelve compliant historical reviews are
not retroactively condemned.

**Group B — the cumulative regression ledger.**
`c6` create the ledger: one row per case any round established, with verdicts `confirmed` /
`defect` / `ambiguous` / `present-but-not-a-defect` ·
`c7` lint check 18: ledger non-empty, no row vanishes without a recorded supersession, every
`confirmed` row names a test case or an explicit "not mechanisable, because …" ·
`c8` seed it with the 24 invariants rounds 4–5 verified.

**Group C — stage wiring.**
`c9` architecture names a ledger per reviewer pairing · `c10` testing carries the confirmed set
forward, so a passing test that breaks a confirmed property is a regression · `c11` a new rubric
critical flag blocking a defects-only review · `c12` the same for the refresh and release stages.

**Group D — the generated product.**
`c13` scaffold generates the schema, ledger and checks into every new plugin ·
`c14` the shared playbook's review-brief template states both halves verbatim.

**Group E — evidence and honesty.**
`c15` fold Instance A into the lesson and cite POSED as precedent rather than novelty ·
`c16` record what the method does **not** fix: a property confirmed *in error* becomes protected
error, and the ledger will then defend it.

**Deferred (no action proposed):** `c17` machine-diffing consecutive review logs to detect a dropped
`verified` entry; `c18` extending the contract to the human faculty gate.

## 4. Your specific lens

Both reviewers use the Part A / Part B structure above. The lenses differ so the two reviews are not
redundant.

### Fable — method and evidence

Attack the causal claim. The CR asserts the brief change caused the convergence, from n=5 rounds
with one variable deliberately changed.

- Is that supported, or confounded? Other things changed across rounds 4–5: the surface had already
  been hardened by three rounds of fixes; the auditors were different instances; the later briefs
  were longer and more specific in ways beyond the confirm half. Can the effect be attributed?
- Is "reopening rate" the right measure, or does it favour the later rounds by construction?
- Does Instance B support the claim or merely illustrate it? Instance C is a different mechanism
  (`strengths`/`preserve_units`) in a different pipeline — is calling it "the worked precedent" fair?
- Is the CR's own evidence standard (L16: evidence burden scales with specificity and consequence)
  met by the CR itself? It makes a strong, general, cross-tool claim.
- **`c16` is where I most expect a real finding.** The method protects a baseline, so a property
  confirmed in error becomes protected error that the ledger defends. The CR's mitigation is "verify
  by mutation, never by reading". Is that sufficient? What is the escape hatch when a baseline entry
  turns out to be wrong, and does the CR provide one?

### Grok — design and blast radius

Attack the mechanism and its reach.

- `c13` pushes this into every plugin the tool generates, including ones for faculty who never saw
  this discussion. Is the design right to propagate, or is it over-fitted to this repository's
  particular review loop?
- Does the schema change (`c1`, `c2`) buy its cost? It makes every review longer — roughly a third
  of reviewer effort in rounds 4–5 went to Part A. Is there a cheaper mechanism that captures the
  same property?
- `c3` makes `approve` illegal with an empty `verified`. What legitimate review does that block?
  Consider a review that genuinely found the artifact unsalvageable.
- Is `c5`'s era-gate the right shape, or does "pre-1.20 = exempt" create a permanent exempt class?
- `c7` requires the ledger to be monotone. What happens when a `confirmed` property is later
  discovered to be wrong, or when a deliberate design change must break one? Is "recorded
  supersession" enough, and who decides?
- `c6`'s four verdicts include `ambiguous` and `present-but-not-a-defect`. Are those the right two
  additions, are they distinguishable in practice, and is anything still missing from the set?
- Sanity-check the grouping: Group A and B are recommended as one block. Is that right, or is there
  a smaller shippable increment?

## 5. Output format

Return one document:

1. **Part A — confirmed**, as a numbered list. Each: the property, how you checked it, and why it is
   load-bearing.
2. **Part B — findings**, ranked by severity (critical / major / minor). Each: row id or section,
   what is wrong, the smallest modification, and which Part A numbers it must not disturb.
3. **Row-by-row disposition**: for each of `c1`–`c18`, one of `approve` / `approve-with-modification`
   (name it) / `revise` / `reject` / `defer`, one line of reasoning each.
4. **One paragraph**: if you were Dr. Ma, which rows would you gate first and why.

State plainly where you could not verify something rather than assuming. A false finding costs more
than a missed one. If a section is sound, say so in Part A and say what you tried against it — that
is a result, not filler.

## 6. What is already decided and not up for review

Not because it is beyond criticism, but because it has shipped and re-litigating it wastes your pass:

- The lesson file itself (`L19`) and its index row — already committed in release 1.18.
- The two prose wirings already landed: the Stage 5 review dispatch in `skills/draft/SKILL.md` and
  the Stage 8 ledger review in `skills/reflect/SKILL.md`.
- The long-term-memory entry recording the method.
- The framing that "positive feedback" here means verified properties, not praise. Dr. Ma has
  endorsed it explicitly.

If you believe one of these is wrong, say so in Part B marked **out-of-scope**, and it will be
routed separately rather than folded into this gate.
