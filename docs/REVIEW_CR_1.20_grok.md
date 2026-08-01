# Review of CR 1.20 — Grok, design and blast-radius lens

**Reviewer:** Grok 4.5, 2026-07-31, independent pass per
`docs/HANDOFF_CR_1.20_review_fable_grok.md`. Filed to the repository on 2026-07-31 while writing
rev 2: it had been returned in chat only, while Fable's pass had a file. A review that decides rows
and lives nowhere is the same durability defect as `c8`'s seed data (F6), one level up.

*Received verbatim. Nothing edited; the box-drawn tables are the reviewer's own formatting.*

---

Grok review — CR 1.20 (confirm-first as mechanism)

Reviewer: Grok 4.5 · Lens: design and blast radius (per handoff §4) · Confirm-first.
Repo access used for schema/lint/review-log spot-checks; causal claims on rounds 1–5 are judged from the CR’s table plus local structure, not re-audit of 1.14–1.19 transcripts.
Where handoff and CR differ, CR governs.

───

Part A — confirmed (protected baseline, not praise)

1. Defect mechanism is correctly named.
   Holds: defects-only briefs yield redesigns without a durable record of what was already verified.
   Checked by: CR §1; matches multi-round CR thrash elsewhere (including POSED/CR loops).
   Load-bearing: this is the problem the CR is allowed to solve.

2. “Positive” = verified properties, not praise.
   Holds as product framing (out-of-scope to re-litigate; also endorsed).
   Checked by: CR §1; handoff §6; consistent with Grok long-term review method.

3. Prose-only L19 is under-enforced relative to this repo’s L11 habit.
   Holds: draft SKILL already demands confirm-first wording; skill_quality_rubric.md output schema still has findings with free-prose fix only, no verified / preserve / modification.
   Checked by: reading skills/draft/SKILL.md (~L67–76) vs rubric schema (~L61–72); 12 reviews/*.json sampled have no verified key.
   Load-bearing: justifies Group A (schema + lint), not more lesson prose.

4. Historical reviews would break a non–era-gated check 17.
   Holds: existing reviews are the old schema; fail-closed check 17 without c5 condemns compliant history.
   Checked by: 12 review files present, old shape.
   Load-bearing: c5 is required if c4 ships (CR §5).

5. Lint check numbers 17–18 are free on the current lint surface.
   Holds: release_lint.py references checks through 16 (max seen 16).
   Checked by: grep of check numbers.
   Load-bearing: ids 17–18 do not collide today.

6. POSED is a fair partial precedent for Group A, not for the full CR.
   Holds: POSED has strengths / preserve_units / strengths-missing style enforcement for revisers.
   Checked by: CR Instance C claim + prior POSED work (not re-read every path this pass).
   Load-bearing: ports “don’t discard what worked”; cumulative ledger + scaffold emission are extensions, not copies.

7. c16 correctly states the main risk.
   Holds: a wrong baseline becomes defended error.
   Checked by: CR §4 Group E + §5.
   Load-bearing: any approve of A/B must retain this limit and strengthen escape hatches (Part B).

8. Group A alone is incomplete as a multi-round memory.
   Holds: per-review verified dies when the next log is written; cumulative ledger (B) is the monotone store.
   Checked by: design of c1–c3 vs c6–c8.
   Load-bearing: supports shipping A+B as one mechanism, with staging only if B is stubbed carefully (see dispositions).

9. c13 is correctly identified as highest blast radius.
   Holds: scaffold propagates schema, ledger, and checks 17–18 into every new plugin.
   Checked by: CR Group D text.
   Load-bearing: this is the faculty-facing product decision, not a local-repo hygiene tweak.

───

Part B — findings (smallest modifications)

Critical

B1. c13 over-propagates a research-repo review contract into every generated plugin.
Row: c13 (also c14).
Wrong: Faculty plugins that never run multi-round adversarial audits still pay full schema + ledger + lint surface. Risk of cargo-cult empty verified lists that satisfy lint without doing the method (same family as “print() suite count”).
Keep: A1–A5, A7–A8 (local mechanism + honesty).
Fix (smallest): Scaffold emits the contract as a named optional module default on for multi-stage authoring plugins with independent reviewers; off for single-skill or no-reviewer pipelines, with one playbook sentence: “turn on when you have a review loop.” Lint checks 17–18 generate only when the flag is on. Do not remove c13; scope it.

B2. how_verified is under-specified for authorizing baselines (c16 is text, not mechanism).
Row: c1, c4, c16.
Wrong: Lint can require non-empty verified while accepting how_verified: "read it". That produces protected false baselines — the failure mode c16 names but does not block.
Keep: A3, A7.
Fix: Schema enum or closed prefixes for how_verified_kind: mutation | command | diff | schema | human_gate | other with detail required; lint rejects missing kind; other requires non-empty because. Document that mutation/command preferred for guard-like claims. Escape hatch for wrong baseline: ledger verdict → superseded with reason + optional reopened_as_defect (ties to B3).

Major

B3. Monotone ledger lacks a first-class invalidate path when a confirmed property is wrong or design deliberately breaks it.
Row: c6, c7.
Wrong: “Recorded supersession” is mentioned in lint goals but not as an authoring workflow (who may supersede, required fields, whether supersession needs a review id). Without that, teams either freeze wrong truths or delete rows (lint fails) or soft-fork the ledger.
Keep: A8.
Fix: Add ledger columns: status includes superseded; required superseded_by (row id or decision id), reason, changed_in_round. Lint: no silent delete; supersession keeps history. Human gate or release owner may supersede; agents may only propose.

B4. c3 blocks legitimate “unsalvageable / regenerate” outcomes if verified must be non-empty only as “good properties.”
Row: c3.
Wrong: An artifact can be fully reviewed and still deserve regenerate with zero preservable units. Empty verified then forbids honest close-out, or forces fake positives.
Keep: A1, A3.
Fix: Allow verified entries that are negative ground: e.g. property = “no unit meets threshold X”, how_verified = command/mutation. Clarify: empty array illegal; zero preservable strengths is expressible as verified negative facts. Optionally allow recommendation: regenerate with verified only of type absence/failure.

B5. c5 “pre-1.20 = exempt” can become a permanent exempt class if new logs omit the version field.
Row: c5.
Wrong: Defaulting missing version to exempt recreates fail-open for any file that never sets review_contract_version.
Keep: A4 (historical twelve need exemption).
Fix: Exempt only if review_contract_version absent and reviewed_at / file mtime / release tag predates 1.20 or explicit review_contract_version: "pre-1.20". New reviews written after ship must set version ≥ 1.20; missing version on post-era files fails check 17.

B6. Instance A’s 3/3 → 0/30 is over-claimed as pure causal proof; CR should not overfit mechanism strength to that n.
Row: §2 Instance A; c15.
Wrong: Rounds 4–5 also differ in surface hardness, brief length, auditor instances, and accumulated fixes. Reopening rate can favour later rounds. Mechanism can still be right; evidence strength for a universal claim is moderate.
Keep: A1 (mechanism).
Fix: In c15 / L19: state as strong before/after in one repo under a deliberate brief change, not as proof of unique causation; list confounders in one sentence. Do not weaken c1–c4 for this — only the evidence claim.

B7. Scaffold + lint without a “no fake verified” fitness invites gaming.
Row: c4, c13.
Wrong: Non-empty verified is satisfiable by boilerplate. Rounds 2–3 of Instance A were exactly this family of self-satisfied checks.
Keep: A3, A5.
Fix: Check 17 requires ≥1 verified entry with how_verified_kind in {mutation, command, diff, schema} or links to a suite case id (same spirit as c7 for ledger). Reject pure “looked good” for critical-flag-related properties.

Minor

B8. Four ledger verdicts are usable; add superseded as status, not a fifth parallel of confirmed.
Row: c6.
Keep: A8.
Fix: Keep confirmed / defect / ambiguous / present-but-not-a-defect; put lifecycle in status (active | superseded).

B9. Group C/D ordering: wire generators after A+B green on this repo.
Row: c9–c14.
Fix: Gate recommends A+B first implement; C then D so scaffold does not freeze a wrong schema. Not a redesign of rows — sequence only.

B10. c17 defer is correct; state dependency on two rounds of new schema.
Already deferred. Confirm; no change.

───

Row-by-row disposition

┌─────┬───────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ Row │ Disposition               │ One-line reason                                                                                 │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c1  │ approve-with-modification │ Add closed how_verified_kind (B2).                                                              │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c2  │ approve                   │ preserve + modification is the right finding shape; keeps A1.                                   │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c3  │ approve-with-modification │ Empty illegal, but allow verified negative ground for regenerate (B4).                          │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c4  │ approve-with-modification │ Fail-closed good; raise bar on verification kind / suite link (B7).                             │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c5  │ approve-with-modification │ Era-gate required (A4); close missing-version fail-open (B5).                                   │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c6  │ approve-with-modification │ Four content verdicts good; add supersession lifecycle fields (B3, B8).                         │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c7  │ approve-with-modification │ Monotone + suite-or-reason good; define supersession rules (B3).                                │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c8  │ approve                   │ Seeding from already-verified 24 is the point of a ledger; re-list sources in implement record. │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c9  │ approve                   │ Ledger belongs at pairing design; after A+B (B9).                                               │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c10 │ approve                   │ GREEN that breaks confirmed property = regression is correct for test loops.                    │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c11 │ approve                   │ Critical flag closes the “defects-only = pass rubric” hole; aligns L11.                         │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c12 │ approve                   │ Class sweep (L13); same contract as draft.                                                      │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c13 │ approve-with-modification │ Emit under opt-in/default-for-reviewer-pipelines only (B1).                                     │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c14 │ approve-with-modification │ Template both halves; only when review loop enabled (B1).                                       │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c15 │ approve-with-modification │ Fold Instance A; soften unique-causation claim (B6).                                            │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c16 │ approve-with-modification │ Keep limit; bind escape hatch + verification kinds into c1/c4/c6 (B2, B3).                      │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c17 │ defer                     │ Needs two rounds of new schema; correct.                                                        │
├─────┼───────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ c18 │ defer                     │ Gate load / L4; faculty call.                                                                   │
└─────┴───────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────┘

───

If I were holding the per-row gate

Gate first as one block: Group A (c1–c5) + Group B (c6–c8), with the modifications above on verification kind, era fail-open, supersession, and negative verified entries — that is the whole mechanism (durable baseline + monotone memory). Then C on this repo. Then D (c13–c14) only after A+B have run on real reviews here, and only with the scaffold scope flag so every generated faculty plugin is not forced into a full adversarial-audit operating system. Approve E with the evidence-tone fix. Defer c17/c18. Do not ship bare c4 without c5.

───

Regression ledger for this review (for the next CR revision)

┌──────────────────────────────────────┬───────────────────┬─────────────────────────────────────────────────┬───────────┐
│ Case                                 │ Verdict           │ Proof                                           │ Source    │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ Defects-only → redesign mechanism    │ holds             │ CR §1; method literature + multi-round practice │ this pass │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ L19 prose without schema enforcement │ holds             │ draft vs rubric schema; reviews lack verified   │ this pass │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ Era-gate needed for check 17         │ holds             │ 12 old review JSONs                             │ this pass │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ Checks 17–18 free                    │ holds             │ lint check numbers ≤16                          │ this pass │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ Instance A pure causation 3/3→0/30   │ open / confounded │ n=5, multiple covariates                        │ B6        │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ c13 full propagate to all plugins    │ defect as written │ blast radius without opt-out                    │ B1        │
├──────────────────────────────────────┼───────────────────┼─────────────────────────────────────────────────┼───────────┤
│ how_verified mutation-only in prose  │ defect            │ schema allows empty quality                     │ B2        │
└──────────────────────────────────────┴───────────────────┴─────────────────────────────────────────────────┴───────────┘

Faculty one-liner: CR 1.20 mechanism is sound; approve A+B with verification-kind, era, and supersession fixes; scope c13 before it becomes every plugin’s default.
