# Cumulative regression ledger

**What this is.** Every case any review round has established, with its verdict, kept monotone
across rounds (CR 1.20 `c6`–`c8`, L19). A per-round baseline dies with the round that wrote it; this
file is what makes the baseline cumulative, so a later round cannot fix one case by breaking an
earlier one. Enforced by release lint check 18.

**Verdicts.** `confirmed` · `defect` · `ambiguous` · `present-but-not-a-defect`. The last two are the
ones usually missing, and they are where oscillation lives: a case with nowhere to go gets re-decided
every round. **Status** is a separate axis — `active` or `superseded` — so a lifecycle change never
competes with a truth claim.

**Supersession.** Rows are never deleted. A row is superseded by a record naming: the superseded id,
a demonstration that the original verification was faulty **as a mechanism** (re-run the recorded
`how_verified` against the case it should have caught and show it passing — prove the verification
vacuous rather than re-arguing the property), the round and reviewer, and the human gate that enacted
it. Agents propose a supersession; only the gate enacts one.

**Row floor: 26.** Check 18 fails below it. Lowering the floor is a deliberate act argued in the
changelog, never a side effect of tidying. This is the practical form of "no row disappears": the
lint has no access to history, so the floor is what makes deletion visible.

**Seeded 2026-08-01** from `docs/APPENDIX_CR_1.20_baseline_seed.md`, which recovered the round-4 and
round-5 auditor enumerations. Per that appendix's own rule, no row is marked plainly `confirmed`: the
verdict below is `confirmed` with the qualifier that it records a verification performed against 1.18
and 1.19 **and recovered from transcripts**, not a verification performed today. Re-anchoring is
pending and is tracked as the `re-anchor` note.

---

## Lint-side invariants

| id | verdict | status | round | case established | mechanised by |
|---|---|---|---|---|---|
| `s1` | confirmed (1.19, re-anchor) | active | round 5 | Citation resolution honours four declared forms, and any `..` leaving the citing skill is an error whether or not a placeholder is present | suite cases `c16 …` |
| `s2` | confirmed (1.19, re-anchor) | active | round 5 | The check-13 canary runs regardless of the suite's verdict, and its anchor test is line-anchored so the error message cannot satisfy its own precondition | suite cases `c13 canary: suite stops detecting a disabled guard`, `c13 canary anchor removed (canary cannot run)` |
| `s3` | confirmed (1.19, re-anchor) | active | round 5 | The suite's case count is read from the suite SOURCE, never from what the subprocess prints | suite cases `c13 suite shrunk below its floor`, `c13 a guard neutered and its case padded back to the total` |
| `s4` | confirmed (1.19, re-anchor) | active | round 5 | Numbered enforcement claims resolve to real numbered items, with valid check numbers derived from the lint's own comments; zero parsed index rows is an error | suite cases `c11 …` |
| `s5` | confirmed (1.19, re-anchor) | active | round 5 | The review population is enumerated from skill frontmatter, never globbed, and an empty `reviews/` is an error | suite cases `c9 …` |
| `s6` | confirmed (1.19, re-anchor) | active | round 5 | Review coherence reads fields by meaning, and the dimension arithmetic runs regardless of the recommendation | suite cases `c15 …` |
| `s7` | confirmed (1.19, re-anchor) | active | round 5 | The validator-template runner refuses empty, duplicate, aliased and anonymous CHECKS, binds `_current` itself, and treats no-evidence as NOT RUN | suite cases `template exit 2 on a duplicated CHECKS entry (evidence would cover for itself)`, `template exit 2 on an anonymous CHECKS entry`, `template refuses a check that produced no evidence`, `template binds evidence to the running check, not to a name it passes` |
| `s8` | confirmed (1.19, re-anchor) | active | round 5 | A fixture that cannot name the guard it proves is a failing fixture: `expect_tag` mandatory, `names_check` required for exit-1 probes | not mechanisable from inside the suite, because the guard is the suite's own case constructor; verified by four direct mutations recorded in the round-5 audit |

## Generated-surface invariants

| id | verdict | status | round | case established | mechanised by |
|---|---|---|---|---|---|
| `g1` | confirmed (1.19, re-anchor) | active | rounds 4–5 | An empty `CHECKS` exits 2 rather than emitting `passed: true` | not mechanisable, because no suite case seeds an empty registry yet — round-4 and round-5 probes did, on scratch copies |
| `g2` | confirmed (1.19, re-anchor) | active | rounds 4–5 | A duplicate or anonymous `CHECKS` entry exits 2 | suite cases `template exit 2 on a duplicated CHECKS entry (evidence would cover for itself)`, `template exit 2 on an anonymous CHECKS entry` |
| `g3` | confirmed (1.19, re-anchor) | active | rounds 4–5 | `checked()` takes only a target; the runner binds the current check | suite case `template binds evidence to the running check, not to a name it passes` |
| `g4` | confirmed (1.19, re-anchor) | active | rounds 4–5 | A check ending with neither evidence nor finding is a critical NOT RUN | suite case `template refuses a check that produced no evidence` |
| `g5` | confirmed (1.19, re-anchor) | active | rounds 4–5 | A missing, unreadable or empty required file is a critical refusal | suite cases `template require_file fires on a missing artifact file`, `template require_file fires on an empty artifact file`, `template require_record fires on a missing manifest record` |
| `g6` | confirmed (1.19, re-anchor) | active | rounds 4–5 | A gate flag is validated by type, so the string `"false"` crits | suite case `template names check_required_structure on a non-boolean gate flag` |
| `g7` | confirmed (1.19, re-anchor) | active | rounds 4–5 | A half-instantiated template cannot reach a green lint while the sample marker survives | suite case `downstream: template samples still present` |
| `g8` | confirmed (1.19, re-anchor) | active | rounds 4–5 | The positive control separates "correct" from "can never approve" | suite case `downstream: positive fixture missing (was a traceback)` |
| `g9` | confirmed (1.19, re-anchor) | active | rounds 4–5 | Every registered check needs its own negative fixture directory | not mechanisable yet, because the suite's downstream plugin registers exactly its fixtured checks; the missing-fixture shape was probed on a scratch copy |
| `g10` | confirmed (1.19, re-anchor) | active | rounds 4–5 | A fixture naming a check absent from `CHECKS` is an error | suite case `downstream: a fixture for a check absent from CHECKS` |
| `g11` | confirmed (1.19, re-anchor) | active | round 5 | `era_at_least` compares integer lists, not strings, and an empty manifest falls back to the contract version | not mechanisable from the suite, because the comparison is a template-internal helper; verified by direct probe with 1.17≥1.4, 10.0≥9.0, 1.2≥1.4 |
| `g12` | confirmed (1.19, re-anchor) | active | round 5 | `CONTRACT_VERSION` must end with the manifest's major.minor | suite case `downstream: CONTRACT_VERSION trailing the release` |
| `g13` | confirmed (1.19, re-anchor) | active | round 5 | A negative fixture that REMOVES an input is rejected — removing an input proves the helper, not the check | suite cases `downstream: fixture that BLANKS an input (proves the helper, not the check)`, `downstream: fixture that DROPS a manifest record` |
| `g14` | confirmed (1.19, re-anchor) | active | round 5 | Byte-identical negative fixtures are rejected | suite case `downstream: two byte-identical negative fixtures` |
| `g15` | confirmed (1.19, re-anchor) | active | round 5 | The named finding must be a critical; a guard downgraded to a warning still errors | suite case `downstream: a guard downgraded from crit to warn` |
| `g16` | confirmed (1.19, re-anchor) | active | round 5 | `require_bool` records evidence, so a check built only from it is not falsely NOT RUN | not mechanisable yet, because the suite's downstream checks all record other evidence; probed directly in round 5 |
| `g17` | confirmed (1.19, re-anchor) | active | round 5 | ROOT-anchored paths work from an unrelated working directory | not mechanisable in-suite, because the suite runs from the copy root; verified in round 5 by running the generated lint from `/` |
| `g18` | confirmed (1.19, re-anchor) | active | round 5 | No child validator output leaks into a clean run | not mechanisable in-suite without asserting on stdout of a nested process; verified in round 5 by inspection of both call sites |

## Superseded rows

None. When the first one arrives it carries the full record described above, and this section stops
being an empty statement about the ledger's integrity and starts being evidence for it.
