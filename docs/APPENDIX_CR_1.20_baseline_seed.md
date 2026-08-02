# Appendix to CR 1.20 — the seed rows for the cumulative regression ledger (`c8`)

**Why this file exists.** Fable's review, finding F6: `c8` proposed seeding the ledger with the
baseline invariants that rounds 4 and 5 verified, but those enumerations existed only in session
context, which expires. A ledger whose stated purpose is "do not re-derive what was already
verified" cannot have its seed data live somewhere that disappears. The enumerations below were
recovered from the round-4 and round-5 auditor reports and are now repository-durable.

**Provenance and its limits, stated.** Recovered on 2026-07-31 from the audit reports of the two
independent auditors of round 5 and one of round 4, against releases 1.18 and 1.19. Each row was
verified **by mutation** — break the mechanism on a copy, observe the guard fire — not by reading.
Two limits that the implementation of `c8` must respect:

1. **Line numbers are as-audited and have drifted.** The round-5 lint audit ran against 1.18's
   `scripts/release_lint.py` before 1.19's fixes landed, so its line ranges no longer point where
   they did. The invariant text is durable; the anchors are not. Re-anchor at implementation time
   and record the re-anchoring, rather than copying stale ranges into a ledger that then certifies
   them.
2. **The count in CR rev 1 was wrong.** Rev 1 said "24 baseline invariants (7 lint + 17
   generated-surface)". The enumeration is **8 lint-side invariants and 18 generated-surface
   invariants, 26 rows.** The "7/7 and 17/17" figures in the 1.19 changelog are *mutation* counts,
   not property counts, and rev 1 added them as though they were properties. Corrected here and in
   rev 2.

The **"breaks if"** column is the most valuable part and is why this is a ledger rather than a list:
it states what a later round must not do, which is the form a lesson has to take to survive a
rewrite (L20).

---

## Part 1 — lint-side invariants (round 5, auditor 1; verified against 1.18)

| id | surface | invariant | breaks if |
|---|---|---|---|
| `s1` | citation resolver, check 16 | Every backticked token containing `/` and a known extension, in every `.md`/`.py` outside `tests/` and the changelog, resolves from the citing file under exactly four declared forms; any `..` segment leaving the citing skill's own directory is an error whether or not a placeholder is present. Verified by 8 mutations, including the two that must be *allowed*. | the `..` rule is keyed on the placeholder again (an 11-character bypass that already shipped once); `_owner` is computed from the citing file's directory instead of the skill root; the retired check-6 fallback retry against the umbrella `reference/` returns; `GENERATED` reverts to prefixes |
| `s2` | check 13's canary | Independent of the suite's own verdict, the lint copies the tree, disables check 3, and requires the suite's `c3 deprecated URL` case to fail. It runs unconditionally, and the anchor test is line-anchored to the assignment so the error message cannot satisfy its own precondition. | the anchor test returns to a substring test; the anchor literal is quoted in the error string again; the canary moves inside the "suite passed" branch |
| `s3` | source-level case count | The denominator of the child's `PASS n/n` line must equal the number of column-0 case call sites counted in the suite **source**, and that source count must clear `MIN_SUITE_CHECKS`. The count is read from the file, never from what the subprocess claims. | the count is taken from the child's output; indented call sites are counted; the floor is lowered as a side effect of deleting cases |
| `s4` | check 11, numbered-claim resolution | Any declared label followed by a number, anywhere in the lesson index or in `skills/**`, must resolve to a real numbered item in the named file; valid check numbers are derived from the lint's own `# N.` comments, so retired 6 is unresolvable and there is no 10. Zero parsed index rows is an error, not a vacuous pass. | sources are restricted back to index rows; the number set is read from the module docstring instead of the comments; the retired-check filter is dropped; checks are renumbered |
| `s5` | check 9, per-skill review derivation | The review population is **enumerated** from `skills/*/SKILL.md` frontmatter, never globbed; every JSON in `reviews/` needs a `resolution_pass`, and every finding needs `status ∈ {fixed, accepted}` with a non-empty resolution. An empty `reviews/` is an error. | the population reverts to a glob (rename evasion) or to a count floor; a missing `name:` is treated as exempt |
| `s6` | check 15, review coherence | Fields are read by meaning: case, spaces and underscores normalized; numeric strings accepted and booleans rejected; the dimension-sum arithmetic runs **regardless** of the recommendation; five independent contradiction sources are checked. | type gates return early on score or threshold; severity matching becomes lowercase-only; the arithmetic moves behind the approving early-continue; the file set narrows again |
| `s7` | validator-template runner | Empty `CHECKS` exits 2; a duplicate, aliased, anonymous or `partial` entry exits 2; `_current` is bound by the runner and `checked()` takes no name, so no check can vouch for another; a check ending with neither evidence nor finding is a critical NOT RUN. The declared limit is honest: a check that swallows its own exception exits 0, backstopped by the per-check negative fixture. | `checked()` takes a name argument again; "ran" is computed from `CHECKS` instead of from evidence and findings; duplicates are silently deduped; NOT RUN becomes a warning |
| `s8` | suite falsifiability guards | A fixture that cannot name the guard it proves is a failing fixture: `seeded()` requires a non-empty `expect_tag` that matches the real error, and `probe()` requires `names_check` for exit-1 cases, asserted against the JSON report's `check` field rather than stdout. Verified by four mutations, each recording FAIL. | `expect_tag` gains a default; assertions move to stdout; `names_check` becomes optional for exit-1 |

**Recorded as slack, not as invariants** (the auditor's own distinction, preserved because a ledger
that silently promotes caveats to guarantees is the `c16` failure): narrowing the citation
extractor's extension list to `.md` alone still clears the `_cited` floor, so *partial* blinding of
the extractor is undetected; and check 15's blocking scan walks only top-level list values, so a
finding nested one level deeper is missed. Both were true when audited and neither was fixed.

## Part 2 — generated-surface invariants (round 5, auditor 2; 17 mutations, 17 fired)

Carried forward from round 4 and re-verified independently in round 5. All anchors are in
`skills/scaffold/reference/validator_template.py` unless stated.

| id | invariant |
|---|---|
| `g1` | An empty `CHECKS` exits 2 instead of emitting `passed: true`. |
| `g2` | A duplicate or anonymous (`<lambda>`) `CHECKS` entry exits 2. |
| `g3` | `checked()` takes only `target`; the runner binds `_current` from the check's own name. |
| `g4` | A check ending with neither evidence nor finding is a critical "treated as NOT RUN". |
| `g5` | A missing, unreadable or empty required file is a critical refusal. |
| `g6` | A gate flag is validated by type, so the string `"false"` crits rather than passing. |
| `g7` | A truthy `SAMPLES_PRESENT` makes the generated lint error — a half-instantiated template cannot reach green. |
| `g8` | The positive control separates "correct" from "can never approve", catching comment-only bodies, unconditional crits and all three degenerate `CHECKS` shapes. |
| `g9` | Every registered check needs its own negative fixture directory. |
| `g10` | A fixture naming a check absent from `CHECKS` is an error, so a written-but-unregistered check cannot hide. |
| `g11` | `era_at_least` compares integer lists, not strings: 1.17 ≥ 1.4 is true, 10.0 ≥ 9.0 is true, 1.2 ≥ 1.4 is false, and an empty manifest falls back to the contract version and stays below a high floor. |
| `g12` | `CONTRACT_VERSION` must end with the manifest's major.minor; bumping the manifest alone errors. |
| `g13` | A negative fixture missing a top-level file that the pass fixture has is rejected — removing an input proves the helper, not the check. |
| `g14` | Byte-identical negative fixtures are rejected. |
| `g15` | The named finding must be `severity == "critical"`; downgrading a guard to a warning while another check supplies exit 1 still errors. |
| `g16` | `require_bool` records evidence, so a check built only from it is not falsely reported NOT RUN. |
| `g17` | ROOT-anchored paths work from an unrelated working directory; the generated lint runs clean from `/`. |
| `g18` | No child validator output leaks into a clean run. |

## Part 3 — round 4's independently verified set (12 mechanisms, 17 attacks)

Round 4's auditor built a different downstream plugin and verified twelve mechanisms by attack.
Every one of them is covered by a row above (`g1`–`g12` map onto it item for item), which is itself
the useful finding: **two auditors, two different generated plugins, one week apart, converged on the
same invariant set.** That convergence is the argument for seeding rather than re-deriving, and it
is recorded here as one row rather than duplicated as twelve.

---

## How the implementation of `c8` must use this file

1. Re-anchor every row to current line numbers, and record the re-anchoring as part of the seeding
   act — a ledger that inherits stale anchors certifies them.
2. Map each row to a suite case id where one exists, or record the explicit "not mechanisable,
   because …" that `c7` requires. Rows `s1`–`s8` and `g1`–`g18` were verified by mutation, so most
   should map; any that does not is the interesting case and must say why.
3. Carry the **breaks-if** text into the ledger verbatim. It is the part that survives a rewrite,
   and it is the reason this is a seed for a regression ledger rather than a summary of two audits.
4. Do not mark any row `confirmed` in the ledger on the strength of this appendix alone. These are
   recovered records of a past verification, not a present one; the honest initial verdict is
   `confirmed (as of 1.19, by mutation, re-verification pending)`.

**Status, 2026-08-02.** Steps 1 to 4 are done; the ledger carries the outcome per row and check 18
resolves every named case against the suite source. Step 2's "any that does not map is the interesting
case" was the productive half: four of this appendix's own mechanisation claims were wrong. `g17` and
`g18` were recorded here as unmechanisable and had in fact been covered by the downstream harness since
1.19, and `g1` and `g9` were one line each from a case. Read this file as the seed record it is, not as
a current statement of coverage — for that, read the ledger.
