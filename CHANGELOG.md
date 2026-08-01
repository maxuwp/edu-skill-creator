# Changelog — Edu Skill Creator

All releases bump both plugin manifests in lockstep. Entry headings follow
`## edu_skill_creator.X.Y — <date>` (the release lint requires the heading, not a mention).

**Numbering rule, adopted 2026-07-31 by the author.** From 1.20 onward a change request's id is the
release number it ships in: CR 1.20 ships as release 1.20, CR 1.21 as release 1.21. Work with no CR
of its own rides the next CR's release rather than minting a minor version. That is why the grounding
corrections below carry no version bump of their own — a version number was deliberately skipped so
the CR and the release could keep matching. The manifests bump when 1.20 gates.

**Open change requests, in gate order.** CR 1.20, confirm-first review as a mechanism, revision 2,
awaiting a per-row gate. CR 1.21, circular evidence, scoped but not drafted. **CR 1.22, terminating
review loops**, revision 0, drafted 2026-08-01 at `docs/CR_1.22_2026-08-01_terminating_review_loops.md`
— it wires L24 through the review brief, the reviewer output schema, one release lint check and one
rubric critical flag, and it takes the ids CR 1.20 does not claim, so 1.20 gates first.

## edu_skill_creator.1.20 — in progress (opened 2026-07-31)

**`c1`–`c5` implemented — the confirm-first contract is now a mechanism.** L19 has said since 1.18
that a review has two halves and that the confirmed half is a protected baseline. Nothing checked it,
which is the state every prose-only rule in this repository has drifted from.

The reviewer output schema now carries `verified: [{id, property, how_verified, how_verified_kind,
location}]`, findings carry `modification` and `preserve` instead of free-prose `fix`, and
`review_contract_version` declares the era. `how_verified_kind` is a closed set, and at least one
entry per log must be `mutation`, `command`, `diff` or `schema` — a baseline made entirely of "read it
and it looked right" is worse than no baseline, because the ledger will defend it. An honest
`regenerate` on an artifact with nothing worth keeping is expressible as verified negative ground, so
the rule does not force fabricated positives. Rubric critical flag 15 makes the omission block.

**New release lint check 17, era-gated, and the gate fails closed.** The CR proposed exempting logs
whose version field is absent. That is the fail-open Grok's review named: every future log would be
exempt by omission. Exemption is now a declaration — a log claims it by recording `pre-1.20` — and the
twelve historical review logs were stamped accordingly. A log written after the era with no version is
non-compliant, not exempt.

Nine new suite cases, seven negative and two positive controls, each starting from a compliant 1.20
log and removing exactly one thing so that every case names the guard it proves: missing version,
empty baseline, an unclassified verification kind, a baseline verified only by reading, a property
with no mechanism, a finding with no modification, a `preserve` id resolving to nothing, plus the
compliant log and the declared pre-era log both accepted. Suite 109 to 118; floor raised to 113.

**`c20` and `c21` implemented — the one live defect in shipped code is closed.** Check 15 authorized
L11's central gate on `computed_checks.<artifact>_validator_pass: true`, a boolean the reviewing
agent wrote about its own conduct. Nothing opened the report it named, confirmed the file existed, or
bound its bytes. A reviewer that wrote `true` without running anything passed, and the prose in the
scaffold skill and the validator template's own header had promised more than the code delivered: the
pass flag travels with a real report path.

The clause now requires the report path, requires the file to exist, and binds its sha256, so a
report that changes after the approval that cites it is caught the way check 14 catches a drifted
gate artifact.

**The lint has a third outcome.** Error, clean, and now UNVERIFIABLE — the check ran and could not
tell. A missing or unreadable report is unverifiable, never a pass; because it is authorizing a gate
it is also an error, so it fails closed, but the record now distinguishes "this is wrong" from "this
could not be established". Before this the lint had two outcomes and "I could not open the evidence"
had nowhere to go except clean.

Five new suite cases, four negative and one positive control: no report path, a path naming a file
that does not exist, a report whose bytes are unbound, a report that changed after the review, and
the fully bound block accepted. The positive control gives every approving review the complete block,
not just one, because the moment a validator exists L11's gate applies to all of them — that is the
contract, not a fixture artefact. Suite 104 to 109 cases, floor raised to 104 falsifiable sites.

**L23 — preserve the need, reconsider the means.** The author's second correction, and it exposed a
defect in the rebase design committed hours earlier. That design protected recorded requirements by
default, so his own example breaks it: a house with small windows carries "many lighting fixtures",
the site changes to one with good daylight, and the fixtures ride across unchanged. The new house
gets a large window and twelve lamps. The requirement was never a requirement; it was a compensating
workaround for a limitation the new foundation removed, and carrying it forward imports the old
foundation's defect into the new one. The same sentence with a decorative reason behind it inverts
the correct action entirely — preserve the fixtures, adapt the structure to carry them. Identical
artifact text, opposite correct migrations, and nothing in the artifact can tell them apart. Only the
person who asked knows, which is why this is solved by asking rather than by better analysis.

Requirements are now recorded on two axes that the first version conflated: semantic role (need,
outcome, preference, constraint, solution, workaround, assumption) and migration disposition
(preserve, adapt, retire_workaround, invalidate, hold_pending_clarification). Reviewer outcomes gain
a fourth, `CLARIFICATION_REQUIRED`, distinct from `REBASE_REQUIRED` because an ambiguous load-bearing
need is not the same state as a foundation known to be wrong. Questions are written with the decision
each answer settles, and a question whose answers change no decision is not asked.

**Two corrections to this thread's own proposals, both against Claude.** "Carry it forward and flag
it" was not sufficient as a tie-break for an ambiguous requirement: carried forward *as active*, it
still gets built, and the twelve-lamp house survives the flag. The disposition is
`hold_pending_clarification` — keep the item in the lineage, commit the design to nothing, and where
work must continue take the most reversible option deliberately. And the proposal to widen L20's
definition of convergence to admit "discovery" as a third category was refused, correctly: it would
have let a descending loop relabel itself as discovery. The three axes — artifact convergence,
requirements resolution, foundation transition — sit beside that definition rather than inside it, so
`silent_descent` remains the pathology while `governed_rebase` is not.

Provenance is mandatory on every lineage entry: an inference must never silently become
`user_confirmed`, and a confirmed status points at the interaction that established it. Without that
field an agent's own guess about what the faculty member wanted is read three rounds later as the
faculty member's stated requirement, which is the circular-evidence failure reserved as L21 arriving
in the requirements layer.

The acceptance test is stated so it can fail: hold the artifact text constant, vary only the human's
answer, and the migration decisions must differ — and must differ only after the clarification, never
before. The lighting pair is the standing fixture. Not mechanised, and the lesson says so.

**CLARIFY / EXECUTE / REBASE — the canonical loop contract, and L22 amended by three reviews.** The
author's objection stood: the scope protocol was human change management, and the agent chain is
different. Four contributions were reconciled into one design record rather than merged silently.
The research run supplied the empirical base — across six vendors' own documentation, four instruct
minimal scope and **none** tells the agent what to do when the correct fix lies outside it. Grok
supplied the move that resolves the conflict architecturally: do not ask the implementer to set aside
minimal scope, stop calling the implementer. Codex supplied the intake assumption audit, the
foundation-first review order, the dependency cone in place of a layer ladder, and selective
invalidation. The author supplied the principle the other three had all missed.

**Rebase, not restart.** When the foundation changes, every prior decision is protected by default
and must carry a recorded disposition — carried forward unchanged, carried forward as a constraint,
adapted because its dependencies moved, or invalidated with the evidence for why it could not
survive. Nothing is regenerated merely because its upstream changed. And the new foundation is chosen
using every requirement gathered so far, including those that only surfaced while building on the
wrong one. This is the part specific to working with an agent: it holds the whole history and can
consume it in one pass, where a human team re-derives it slowly, which is why human change control
treats relocation as expensive and avoids it. Discarding the accumulated design to start clean throws
away the one advantage the medium provides.

**Three parts of L22 did not survive, and the corrections are recorded in place rather than
rewritten.** The one-controlled-descent reserve is withdrawn as unevidenced — it was invented here,
and this project's own research found nobody has measured whether tighter scope constraints raise or
lower resolution rate. The complete-the-breadth-first rule is corrected to foundation first: once a
foundation assumption is demonstrably invalid, reviewing its descendants produces findings that will
be discarded, which is the waste the lesson exists to prevent. The single layer ladder is demoted to
reporting vocabulary, because a control plane such as the release lint is not simply deeper and
defects travel laterally through shared dependencies as often as down. What survived: declaring scope
before starting, separating scope pressure from findings, and grading by impact.

Reviewer outputs become `PASS`, `REVISE_LOCAL` or `REBASE_REQUIRED`, with the harness stop behind the
third. Settlement is converged, rebased, or a design verdict; many rounds and general fatigue is not
settlement. Faculty authority is narrowed to intent, approved decisions, risk and cost rather than
every technical boundary adjustment.

Recorded as unestablished, in the record itself: that any of this saves tokens; that minimal-diff
discipline is what stalled our own loops; and two figures cited for the clarification scaffold that
are not in the paper's abstract. The dual-mode proposal in the POSED repository keeps its analysis
and defers its contract section to this record, so one contract exists rather than two.

**Review Scope Protocol, and lesson L22 — controlled scope escalation.** Three external reviewers
were asked independently how to control a review scope that keeps expanding as the digging goes
deeper. They returned the same structure from three traditions: timeboxed spikes that convert an
over-running fix into a re-scope proposal, one-logical-change commit discipline that files a deeper
defect instead of absorbing it, and incident command re-declaring an incident's type rather than
letting one grow quietly. The shared mechanism is that scope must be a declared artifact with an
owner, so expansion becomes a diff between declared and touched rather than a feeling.

`skills/edu-skill-creator/reference/review_scope_protocol.md` is the runnable procedure, written for
both reviewer populations at once — the fresh-context reviewers this system dispatches, and external
models reviewing this repository's own work. It carries the declaration block (object of record,
layer, breadth, budget, authority), the rule that stops descent (complete the declared breadth at
the declared layer before writing any finding), the scope-pressure record for everything that cannot
be fixed at that layer, the four impact classes with their authorities, and two paste-ready brief
blocks.

**One correction to L20, and it came from a reviewer.** L20 rule 1 said a lower-layer fix means stop
the round. Read strictly that sends a one-line adjacent correction through the same procedure as
rebuilding the foundation, which makes teams either freeze or creep. The amended rule: every
lower-layer change is a re-scope, but not every re-scope is a restart — the response is graded, from
an author-enacted controlled descent (recorded, one per round) to a faculty-authorized relocation.
L20 detects, L22 routes. The rest of L20 is unchanged, and the amendment says so in place.

The bounded reserve is the cap that makes it decidable: one controlled descent per round; a second
converts the round into a major re-scope proposal whatever its size.

Grounded on a primary source rather than on the analogy: NASA's Systems Engineering Handbook
separates a major change (impact on baseline specification, cost, safety, interface compatibility,
training) from a minor one, and routes changes through a board chaired by someone with change
authority. Added to the grounding library with a scope limit that says what it does not license —
our four class names and the reserve are local rules. The incident-command corroboration is recorded
as an illustration, not an anchor, because its primary text could not be fetched in this pass.

Enforcement is prose and procedure only. Nothing reads a declaration block or notices a fix that
landed below the declared layer. Wiring it is scoped as future change-request rows and deliberately
not folded into CR 1.20, which is under gate — amending a document under review is the failure L19
names, and widening a change already out for decision is the failure L22 names.

**CR 1.20 rev 2, after both independent reviews.** Fable took the method and evidence lens, Grok the
design and blast-radius lens; between them, eighteen findings, none rejected. Rev 2 opens with the
confirm-first pass applied to itself: what both reviewers verified is stated as this document's own
protected baseline before any row changes, so the revision is a modification and not a new draft.

The evidence section was the part that did not survive review. Rev 1 claimed "3/3 to 0/30, the only
variable changed was the brief". Both reviewers rejected that independently: the two rates use
different denominators, the after-period censors round 5 (no subsequent round has audited its
fixes), and three things co-varied with the brief — the suite grew from 25 to 78 falsifiable cases
before round 4, round 3 had no external auditors, and three rounds had already swept the older
surfaces. Rev 2 states the per-fix-set rates, names the confounds, and gives the attribution to the
combination while noting that the component this repository's own evidence most directly supports is
the mechanised baseline rather than the brief's wording. That is a weaker claim about the prose and a
stronger one about Groups A and B.

Six rows were tightened where the CR's own mitigation was prose under its own lint: `how_verified`
gains a closed kind and check 17 must reject a log that verified nothing by a runnable mechanism;
supersession gains a required shape, an evidence burden and a human-gate authority, so a wrong
protected row can be demoted without the ledger becoming decorative; `c3` admits negative ground so
an honest regenerate is expressible; `c5` closes the missing-version fail-open that would have made
every future log exempt by omission; `c13` becomes an opt-in module rather than the default shape of
every generated plugin, held behind one internal round.

`c8`'s seed data is now in the repository (`docs/APPENDIX_CR_1.20_baseline_seed.md`), recovered from
the round-4 and round-5 auditor reports: 26 invariants with their breaks-if clauses, which is the
part that survives a rewrite. Recovering it corrected a count rev 1 got wrong — "24 (7 lint + 17
generated-surface)" added mutation counts as though they were property counts; the enumeration is 8
and 18. A CR about protected baselines mis-stating the size of its own baseline is worth recording
rather than quietly fixing.

Rows `c20` and `c21` are pulled forward from the scoped CR 1.21 into this gate. They change the same
contract Group A changes, so gating them apart would mint two contract eras and permanently double
the exemption matrix `c5` reasons over. `c20` is the one live defect in shipped code: check 15
authorizes L11's central gate on a boolean the reviewing agent wrote about its own conduct, and
never opens the report it names.

Grok's review is now filed at `docs/REVIEW_CR_1.20_grok.md`. It had decided rows while living only in
chat, which is the same durability defect as `c8`'s seed data, one level up.

Nothing in the CR is implemented; it awaits the per-row gate.

**Lesson L20 — Foundation Regress.** The author named the pathology behind the audit loops: a fix
that requires changing a layer below the artifact under review is a re-scope, not a fix, so the loop
descends through layers while looking like iteration — house, then foundation, then water table,
then a new location — and the lessons are lost at each relocation because they were written as
repairs to the thing being abandoned. The lesson states both halves, gives three early-detection
signatures, and defines the metric that would make the economic claim falsifiable: rounds against a
declared budget, findings per round, regression share, layer touched per round, cost per round.
Convergence is findings falling while the layer holds; descent is findings falling while the layer
drops, which reads as progress on a findings chart alone.

Recorded honestly in the lesson: this repository logs rounds, findings and reopened-fix counts, and
does not yet log cost or layer per round, so the token-cost claim is a well-founded expectation and
not a measured result. Enforcement is prose and metric definition only; the stage wiring is specified
and not yet mechanized.

The circular-evidence lesson that the POSED handoff proposed for the L20 slot ships as L21. That
handoff carries a numbering note rather than a rewrite, since it was already sent.

**Grounding library corrections, from the first external audit of the anchors themselves.** Thirty
anchors were checked against primary sources twice and independently (Perplexity agentic browsing and
deep research); the comparison is in `docs/AUDIT_grounding_two_runs_compared.md`. The two runs
disagreed on eight anchors, so this release acts only where the evidence is not in dispute, and says
so in the library itself.

**The highest-value single edit is Mayer.** The anchor read "Multimedia materials; not classroom
facilitation," which an author could read as licensing prose-level editing judgments — and one did,
which is the failure L14 records. Both runs independently confirmed the diagnosis: the personalization
principle was operationalized as a 12-place "the"→"your" substitution in a narrated science animation.
The row now states that scope and rules out lexico-grammatical editing at any layer, explicitly.

**Corrected on agreed or uncontradicted evidence:** UbD widened (its own Stage 3 plans instruction);
Mager and ABCD split into separate rows, because ABCD is a different lineage and the library had
conflated the two; Merrill re-pointed from the 2002 synthesis paper to the 2020 AECT revision (2024
reissue); Ausubel narrowed to prose organizers before unfamiliar written expository text; cognitive
apprenticeship widened, since the source includes conceptual knowledge situated in use; Haladyna
narrowed to multiple-choice and selected-response, with the blueprint clause softened; obra's
description rewritten to admit Superpowers is a full agentic-development methodology from which one
skill is borrowed; NIST SP 800-218A added as a companion anchor, the clearest additive finding of the
exercise; Quality Matters' copyright rule extended to the free PDF, which is itself restricted against
duplication.

**Two factual disputes settled at their issuing bodies rather than by a third reader.** IEEE's own
record gives 1028-2008 as "Inactive-Reserved" since 2019-11-07 with no successor — the browsing run
was right, and the deep-research run's "formally withdrawn" came from a reseller's sales listing.
W3C's publication history shows both parties were right about different things: WCAG 2.2 became a
Recommendation on 2023-10-05 and its current version is dated 2024-12-12. The library now states both
dates. IEEE 1028 is no longer cited as an active standard anywhere in the skills: the four live
citations that justified binary inspection over scored rubrics now stand on Fagan (1976) alone, which
is where that claim always came from.

**What was deliberately not changed, and why it is recorded.** Bloom, Cognitive Load Theory, ICAP,
Kosslyn and SIFT/CRAAP are disputed between the two runs and are untouched; their scope sentences
carry no more authority now than before the audit, and the library says so in a new audit-status
section. Gagné, POGIL, UDL 3.0, TPI, Biggs, Wiliam, Alley, plugin-dev and TDD were checked and found
sound, and were left alone on purpose — a verified property is a baseline to protect, not an
invitation to re-draft (L19). Two flagged findings needed no edit and were verified as such: no
shipped skill cites a formative-assessment effect size, and no skill cites the moved upstream
`skill-creator/` path. The historical narrative in L01 still reads "Fagan/IEEE 1028" because it
records what POSED did at the time; rewriting it would falsify the record.

## edu_skill_creator.1.19 — 2026-07-31

Round 5, same confirm-first brief, with round 4's verified properties carried forward as a
baseline to RE-VERIFY rather than assume. **The convergence is real.** Both auditors broke every
baseline mechanism on a temp copy and reported it firing: 7 of 7 lint invariants and 17 of 17
generated-surface invariants survived 1.18 intact. Of the ten findings, nine are gaps in surfaces
1.18 itself added or last touched, and exactly one is a regression from an earlier release. After
three rounds where every fix reopened a prior one, that is the shape a converging loop has.

**The one regression, and it was mine.** 1.18 widened check 3 to scan `.py` and excluded all of
`tests/` so the suite's deliberate fixture string would not trip it. Only one file under `tests/`
carries that string, so the exclusion silently dropped coverage of `tests/*.md` and `tests/*.json`
that 1.17 had. Both other exemptions in that loop are file-scoped; this one now is too.

**Both auditors independently found the same two holes**, which is the strongest signal in the
round:

- **The citation rule tested where a path LANDS, not each hop.** A citation of the form
  `../../skills/NAME/…` leaves the skill directory and comes back, so it passed — while the
  installed layout, where siblings are prefixed, still dangles. It is also the natural spelling
  for an author thinking in repo terms. Now checked per hop.
- **The computed-checks gate accepted any non-empty block.** `{"note": "ran it"}` satisfied
  L11's central gate, which 1.18 had just converted from prose to code. Recording the report path
  and renaming or forgetting the pass flag was enough. It now requires an
  `<artifact>_validator_pass` key.

**The runner's own diagnostics were being read as the subject's evidence.** A negative fixture
proved its check by finding a critical carrying that check's name — but the runner stamps its own
CRASHED and NOT-RUN criticals with the check's name too. A fixture that made the check crash, or
that stopped it running at all, therefore read as proof that it ran, and a check with an empty
body shipped certified. Findings whose location is `validator` are now excluded. This is the
same shape as 1.16's self-reported count and 1.17's self-matching anchor, in a new place.

**The prescribed fixture contract closed one of three removal shapes.** Deleting a file was
rejected; blanking it and dropping a manifest record were not, and both make the fail-closed
helpers report under the calling check's name exactly as deletion does. The rule is now stated as
what it always meant: change one value in place, leaving every input present and non-empty.

**The snippet could not be pasted out of the file it lives in.** The docstring stored backslash
escapes, so the block an author copies is a `SyntaxError`; only `__doc__` rendered correctly, and
the instruction says to take it "from the template's docstring". The escapes were unnecessary and
are gone; the suite's parse probe now compiles the text as pasted. A missing positive fixture
also raised instead of reporting, discarding every error the earlier checks had found.

**The generated harness is now tested by this repo's own suite, end to end.** Ten new cases build
a real downstream plugin from the template, transcribe the fixture-runner snippet verbatim, and
require each claimed rejection to fire: blanked input, dropped manifest record, crashing check,
missing positive fixture, byte-identical fixtures, a guard downgraded to `warn()`, surviving
`SAMPLES_PRESENT`, stale `CONTRACT_VERSION`, and an unregistered fixture — plus a control that an
honest plugin is silent. Two audit rounds had to do this by hand; verified-when-someone-remembers
is not verified. Suite 91 → **104 cases** (99 falsifiable), 8s.

**Also:** the era-gate fallback is stated honestly — with no `session_contract_version`,
`contract_era` returns this validator's own floor, which DISARMS era gates rather than arming
them, and is safe only because the runner requires `CONTRACT_VERSION` to track the release. The
instantiation instruction now says to trim the template's authoring preamble, so a shipped
validator stops carrying a second copy of the snippet and citations written for another repo.

**Lessons.** L11 gains the lands-versus-traverses row and the harness-diagnostics-as-evidence row.

Verification: `release_lint: 0 error(s), 0 warning(s)` in both modes; `PASS 104/104 deterministic
checks`.

## edu_skill_creator.1.18 — 2026-07-31

The audit brief changed, and the loop converged. Rounds 1 to 3 asked reviewers only for defects,
so each round returned a redesign, and each redesign carried the next round's bug. Round 4's
brief required a **confirm pass first** — verified properties with the mechanism each rests on,
as a do-not-break contract — and then defects **as the smallest modification that keeps that
contract true**. Two auditors returned 20 findings, and for the first time none of them was a
reopening of a previous fix. The author's diagnosis, recorded as **L19**: *a revision can't be a
new draft, it should be a well informed modification.*

**Confirmed and preserved (the do-not-break contract).** Independently verified by mutation, not
by reading: check 16's `..` rule and its four declared citation forms; check 13's canary and its
source-level case count; check 11's `_lint_checks()` deriving valid numbers from the lint's own
`# N.` comments; check 9's per-skill review enumeration; check 15's read-by-meaning fields;
the validator runner's empty/duplicate/anonymous `CHECKS` refusals, its runner-bound `_current`,
and its NOT-RUN finding; `seeded()`'s mandatory `expect_tag` and `probe()`'s mandatory
`names_check`. Every fix below was checked against this list before landing.

**The case floor counted members that could not fail.** A dead guard could be neutered by
rewriting its case as `record(name, bool(1))` — not a literal `True`, so the constant-verdict
test missed it — and the total held. The floor now counts `seeded`/`probe` sites only; `record`
sites still count toward the reported total, so the verdict-line equality is unchanged.

**Removing the recursion off-switch in 1.17 left no bound at all.** 1.17 was right to delete
`ESC_LINT_DEPTH` (an ambient variable that silently disabled the whole suite check), but its
replacement was a convention — "every `full=True` case stubs its copy's suite" — that nothing
enforced. True for all eight cases today; the first violation hangs the lint forever. `seeded()`
now refuses a `full=True` case whose copy still holds a real suite. The bound is back without
the switch.

**`require_bool` recorded no evidence**, so a check built the documented way ("the require_*
helpers record for you") was reported NOT RUN on its happy path — a permanent false critical in
every generated plugin using that pattern.

**The era-gate idiom the template prescribes was a string compare.** `"x.1.17" >= "x.1.4"` is
False, and so is `"x.10.0" >= "x.9.0"`. Any generated plugin reaching minor .10 would have
silently disarmed every era-gated rule — the exact failure the same paragraph warns about. Ships
`era_at_least()` instead, and the runner now checks `CONTRACT_VERSION` against the release, a
match the template claimed the lint verified and no lint did.

**A negative fixture that DELETES an input proves the helper, not the check.** `require_file` and
`require_record` report under the *calling* check's name, so a check whose body is a lone
`require_file(...)  # TODO` is named by its own fixture and ships certified. The prescribed
runner now rejects a fixture that removes a file the pass fixture has, rejects byte-identical
fixtures (one bad session copied N times is one proof), and requires the named finding to be
**critical** — a guard downgraded to `warn()` still appeared in `findings` while a cascading
defect from another check supplied the failing exit. Each verified by rebuilding a downstream
plugin and running its generated lint.

**L11's central gate was prose in four files and code in none.** "`approve` is illegal without a
recorded computed pass" is now a clause in check 15: with any `validate_*.py` present, a review
recommending approval must carry `computed_checks.<artifact>_validator_pass = true`. Inert here
until a validator exists, live in every generated plugin from birth.

**Smaller, each with its own fixture:** check 1's whitelist keyed on basename, exempting any file
under `skills/` that reused one of two names; check 3 never scanned `.py`; check 4's misplacement
detector knew only the table shape, not the heading shape check 4 itself parses; check 9 crashed
on a malformed `findings` value, printing zero findings and skipping checks 11 to 16; check 11
resolved claims only inside `skills/`, while a live claim sits in `docs/`, and verified only the
endpoints of a range, so "checks 9-11" asserted a check 10 that does not exist; check 15 skipped
the dimension arithmetic when the scores were a list; check 16's remediation text recommended a
repo-root path for sibling skills; and one suite case still tested lesson reachability by the
substring method check 12 was rewritten to abandon. The prescribed snippet was also cwd-relative
inside a ROOT-anchored lint (`exec_module` raised before `sys.exit`, discarding every earlier
error) and leaked child validator CRITICAL lines into a clean release's stdout.

**Three ambiguities resolved in wording**, each of which two reasonable authors would have built
differently: the fixture directory suffix is the check function's `__name__` verbatim; a negative
fixture is the pass fixture with one field corrupted; `SAMPLES_PRESENT` is disposed of by value,
and the token surviving in the docstring is expected.

**Lessons.** L19 (confirm first; a revision is a modification) arrives from the
talk-like-a-professor rounds and is now wired into the Stage 5 review brief and the Stage 8
ledger review. L11 gains three population rows and the severity-is-part-of-the-claim corollary.

Verification: `release_lint: 0 error(s), 0 warning(s)` in both modes; `PASS 91/91 deterministic
checks` (86 falsifiable); the downstream harness rebuilt and its five new guards each fired.

## edu_skill_creator.1.17 — 2026-07-30

Third audit round. Both external auditors terminated on an account session limit before
producing findings, so this release is what a self-audit of 1.16's own new code found. Both
defects were introduced BY 1.16, and both are the pattern the previous two rounds named: the
machinery added to close a hole became the hole.

**Check 13 had an off-switch in the ambient environment.** 1.16 bounded lint → suite → lint
recursion with an `ESC_LINT_DEPTH` counter read from `os.environ`. Exporting it disabled check
13 entirely — the suite run, the case count and the canary — while the lint printed a warning
and exited 0:

```
ESC_LINT_DEPTH=2 python3 scripts/release_lint.py   ->   0 error(s), 1 warning(s)
```

The variable is gone. Every check-13 fixture now stubs the copy's suite, and a stub never
invokes the lint, so the chain terminates in one step with nothing to configure. Deleting the
surface beats guarding it; a guard configurable from outside the repo is not a guard. Lint
runtime drops from ~16s to ~6s as a side effect.

**The canary vouched for its own anchor.** It refused to run unless it could find
`DEPRECATED = ("maxuwp/page",)` in the lint source — by substring search, and that exact string
appears twice inside the canary's own two lines. The anchor could therefore never be reported
missing. Now line-anchored to the assignment. Its fixture is falsifiable: reverting to the
substring form turns `c13 canary anchor removed` red.

**The generated harness was proven end to end, not asserted.** A downstream plugin was built by
following `skills/scaffold/SKILL.md` literally — template instantiated, fixtures written, the
fixture-runner snippet transcribed verbatim from the template docstring — and the resulting lint
catches all three shapes the template claims it stands behind: a hollow check (`exit 0,
check_upstream_coverage named: False`), a check fixtured but never registered in `CHECKS`, and a
validator that can never approve anything. `SAMPLES_PRESENT` fires on an un-replaced template.
This matters because the template states plainly that it cannot itself detect a check that lies
about its work; the per-check negative fixture is what does, and that is now demonstrated.

**Residual, stated rather than closed.** Three ways remain to make an instantiated validator
report a pass while validating nothing: a check whose body is a bare `checked()` call, a check
that swallows its own exception, and an author who deletes the empty-`CHECKS` guard from the
runner block marked "do not edit". All three are deliberate acts inside the check bodies, all
three are caught by the prescribed fixtures, and none is detectable by the runner. L11 records
them; the alternative is a claim the code cannot keep.

**Lessons.** L11's degenerate-population table gains the ambient-off-switch row and the
guard-anchored-to-its-own-source row.

Verification: `release_lint: 0 error(s), 0 warning(s)` in both modes; `PASS 78/78 deterministic
checks`; `ESC_LINT_DEPTH=9` now changes nothing.

## edu_skill_creator.1.16 — 2026-07-30

Second audit round: two fresh auditors were asked to refute 1.15 and to find what a *second*
adversarial pass would find, on the assumption the easy holes were gone. They found 24 defects
between them, including two that reopened the release's own headline claims.

**Check 16 did not reject `..`; it rejected `..` next to a placeholder.** `<skill-dir>/../scaffold/…`
was caught, plain `` `../scaffold/reference/validator_template.py` `` was not — 1.14's defect,
reopenable by deleting eleven characters. Now any `..` that leaves the citing skill's own
directory is an error, wherever it appears; `..` inside a skill (a lesson file reaching its own
`reference/`) stays legal, because it resolves identically in both layouts.

**"Every one falsifiable" was 58 of 59.** `probe()` never required a names_check, and `s_ok`
produces five criticals from three guards, so one probe's exit-1 was over-determined: it stayed
green with `require_record`'s finding deleted. `probe()` now refuses an exit-1 case that names no
guard, and `issue=` narrows to the specific finding. The same audit showed `stamped`,
`require_file` and `require_record` were claimed "actually exercised" while only `require_bool`
had a probe that could fail; all four now have one.

**Check 13's floor was self-reported.** 1.15 replaced "exit 0" with "exit 0 plus a verdict line
plus a count" — all three printed by the suite under test, so `print("PASS 59/59 …")` satisfied
the gate with the suite deleted. Check 13 now counts case call sites in the SOURCE, requires the
reported number to equal them, rejects any case whose verdict is a literal `True`, and ends with
a **canary**: it breaks check 3 in a copy and requires the suite to notice. The canary runs
whether or not the suite passed. Recursion (lint → suite → lint) is bounded at one nested level
by an explicit depth counter, and the suite gained `--only` so the canary costs one case.

**Check 9 floored an enumerable population at "non-empty".** Deleting one skill's review left the
lint clean. Reviews are now derived from `skills/*/SKILL.md` — every skill needs
`reviews/<name>_review.json` by name.

**Four surfaces cited "architecture item 11" for the computed-validation plan; a 1.11 renumber
moved it to 12.** Item 11 exists (lifecycle stages), so nothing fired, and the wrong number was
baked into the validator template every generated plugin inherits. Corrected, and check 11 now
resolves numbered claims in *every* skill body and script, not only in lesson-index rows — the
audited surface was the one that stayed right.

**`draft/SKILL.md` taught the wrong invariant for check 4**, telling authors to write the phrase
"100 points" so the lint verifies the sum. 1.15 had made the check key on PATH precisely because
the phrase was disarmable. Corrected, and a scored rubric (points table plus critical flags)
sitting outside `skills/*/reference/*rubric*.md` is now an error rather than an invisible pass.

**The validator template — copied into every generated plugin — could still emit `passed: true`
seven ways.** `checked(check, target)` took the check name as a free string, so one check could
vouch for a check that never ran; a duplicated or `lambda` entry in `CHECKS` had the same effect.
The runner now binds the running check itself: `checked(target)` takes no name, `crit()`/`warn()`
take no name, the helpers take no name, and duplicate or anonymous entries exit 2. The require_*
helpers record evidence themselves, so a check built from them proves it ran without extra
ceremony. The one shape no runner can catch — a check that examines something and then swallows
its own exception — is now stated as a limit rather than implied away; the per-check negative
fixture is what stands behind it.

**The fixture harness the template prescribes had four defects**, all in the code downstream
authors copy: `V` was never bound (`NameError` on first run); reports were written into the
fixtures being read; `SAMPLES_PRESENT` promised an enforcement that existed nowhere; and the
runner audited `CHECKS → fixture` but never `fixture → CHECKS`, so a check that was written and
even fixtured but never registered shipped silently unenforced. All four fixed, the last by
mirroring check 12's registry fold into the template.

**Also:** check 16 now scans the whole repo rather than `skills/` only (tests/ excluded — its
fixture strings are deliberately broken citations), covers eleven more file extensions, and takes
its generated-artifact exemptions as exact tokens rather than prefixes, which had exempted
everything under `reviews/`. `MAINTAINING.md` and the lint docstring described check 9 by the
glob 1.15 abandoned. `test/SKILL.md` claimed the suite had 18 cases. An empty `expect_tag` was
accepted, and `"" in out` is always true.

**Lessons.** L11's degenerate-population table gains four rows and three rules (declare the
population; enumerate it where it is enumerable; never let the subject report on itself). L13
gains the sweep-where-the-audit-does-not-reach fold. L14 gains the harness-reads-its-own-subject
fold.

Verification: `release_lint: 0 error(s), 0 warning(s)` in both modes; `PASS 78/78 deterministic
checks`; 73 path citations resolved from the citing file.

## edu_skill_creator.1.15 — 2026-07-30

Two independent auditors, given no prior context, were asked to refute 1.14's claims and to hunt
fail-open holes. Both found real defects, and both converged on the same root: **the suite asserted
that the lint failed, never which guard fired.** Everything below follows from that.

**Three of the twenty-five suite cases were vacuous.** `lint c13 self-test noted as externally
proven` was the literal constant `True` — it could not fail, and it occupied a slot in the advertised
count. The two check-11 cases (`index deleted`, `dangling lesson path`) passed for the wrong reason:
each mutation also orphans lesson files, so **check 12** failed the lint and the fixtures went green;
with check 11's guard deleted, both still passed. 1.14's headline was vacuous green, and it shipped
three instances of it in the file it was editing.

- `seeded()` now **requires** an `expect_tag` and asserts that exact error text. A case that cannot
  name its guard cannot be written.
- Fixtures are per BRANCH, not per check. Nine fail-closed branches had no fixture at all.
- Check 13 is now genuinely tested, against stub suites (no recursion): missing, failing, zero-byte,
  and shrunk below its case floor.
- Suite: 25 → **59 cases**, every one falsifiable.

**The 1.14 reference fix did not land.** `<edu-skill-creator-skill-dir>/../scaffold/…` resolves in a
git checkout and dangles in the installed harness, where the sibling is `edu-skill-creator-scaffold`.
It was verified at the authoring layer while the claim lived at the deployment layer — L14's own
error, committed while writing L14's enforcement. Fixed with a parameterized placeholder
`<edu-skill-creator-skill-dir:NAME>`, correct in all three layouts, and with **check 16**, which
rejects `..` traversal outright and resolves all 52 path citations in the corpus from the citing
file. Three further unresolvable citations the 1.14 sweep missed are corrected (`L12`,
`reflect/SKILL.md`, the validator template's own header).

**Eleven fail-open holes in the lint, all reproduced before fixing.** The pattern behind them: a
check whose *population* can be emptied is as dead as a check whose input was deleted.

- deleting one `version` key silenced checks 2, 5 and 8 at once → absent version is now an error
- `reviews/` empty, or a review renamed off the `*_review.json` glob → every JSON in `reviews/` is a
  review, and an empty directory is an error
- a zero-byte `run_deterministic.py` satisfied check 13 → the suite must emit its own verdict line
  and meet `MIN_SUITE_CHECKS`
- deleting `reflect_gate_decision.json` defeated drift detection → missing gate record is an error
- rewording "100 points" disarmed the rubric arithmetic → rubrics are identified by path; an
  unparseable rubric is an error
- a missing skill `version:` was a warning while a wrong one was an error → both are errors
- manifests claiming no `homepage`/`repository` skipped the origin comparison → both manifests must
  claim a home
- the changelog heading was a substring test, satisfiable from inside a code fence → line-anchored,
  fences stripped
- check 12 counted a filename mentioned in an HTML comment as indexed → membership is tested against
  check 11's parsed rows
- check 15 matched only lowercase `"blocking"` and rejected string-typed numbers via `isinstance`, so
  `severity: "Critical"`, `counts.critical`, and `score: "81"` all sailed through the check written
  for them → every field is read by meaning; dimension scores must also sum to the reported total
- check 6 warned instead of erroring and retried failed paths against the umbrella's `reference/`,
  so a citation written from the wrong skill still "resolved" → retired into check 16

**The validator template could report a pass it never earned.** This is the highest-blast-radius
finding, because scaffold copies the template into every plugin this tool generates. An empty
`CHECKS` list, or the three sample bodies left as comment sketches, produced `passed: true` on a
session with no artifact at all — and `passed: true` plus a report path is what makes a reviewer's
`approve` legal. Now: empty `CHECKS` exits 2; every check records what it examined via `checked()`,
and one finishing with neither evidence nor a finding is reported as NOT RUN; the samples are
runnable code against a documented toy schema rather than sketches; `require_record`, `require_bool`
and `stamped` are actually exercised. The prescribed fixture contract changes from one pair per
*validator* to **one negative per check** — a single "bad" fixture trips whichever check runs first
and leaves the rest unproven forever — plus a positive control, without which a template hardwired to
fail is indistinguishable from a correct one.

**Enforcement claims are now checkable.** Check 11 verifies `release_lint check N` claims in the
lesson index against the numbered checks in `release_lint.py`. The 1.11 ledger claimed enforcement by
"release_lint check 11" when no such check existed, and that claim survived two independent review
rounds; prose about code is exactly what code should check.

**Lessons.** L8 gains the fixture-naming fold (passing for the wrong reason, branch granularity, the
missing positive control). L11 gains the degenerate-population corollary with the five shapes
tabulated. L14 gains the checkout-as-proxy-for-harness fold.

**Corrections to 1.14's own entry.** It said six of thirteen checks lacked a fixture, listing 4, 6,
7, 8, 13, 14 — check 14 did not exist before 1.14, so the figure was five of thirteen plus one new
check. It also said check 14 "asks on every push"; there is no pre-push hook, so it asks whenever the
lint is run, which `MAINTAINING.md` requires but does not enforce.

Verification: `release_lint: 0 error(s), 0 warning(s)` in both normal and `--publish` modes;
`PASS 59/59 deterministic checks`.

## edu_skill_creator.1.14 — 2026-07-30

Audited this repo against the failure patterns from the sibling POSED project's live test run
(`FINDINGS_posed_multi_model_review_2026-07-29`, `SELFTEST_posed_session_audit_2026-07-29`). Twelve
generalizable patterns were extracted; four were present here.

- **Reference not landing** (their A7). `skills/architecture/SKILL.md` cited
  `reference/validator_template.py`, which does not resolve from that skill — the file is under
  `scaffold/`. A cold agent following that pointer fails. Corrected to the placeholder-qualified path.
  Nine other candidate paths were checked and are outputs a *generated* plugin creates, not defects.
- **Post-approval drift was undetectable** (their A1, the most serious finding in their audit: three
  approved artifacts were edited afterwards and nothing noticed for sixteen days). Our gate decision
  named its artifact by the version *string* `"reflect_ledger.json rev 3.1"` with no hash, so the
  ledger could change under an approval and nothing would ask. Now hash-bound, with **check 14**
  asking on every push rather than waiting to be asked — which is the fix their audit recommends and
  does not yet have.
- **A gate that authenticates a signal, not the record it signs** (their most cross-confirmed
  finding: a review recording `total 81`, `threshold 85`, `passed false` and `recommendation approve`
  simultaneously). Nothing here cross-checked a recommendation against its own evidence. All twelve
  of our reviews are in fact coherent — the hole was latent, not fired. **Check 15** now blocks any
  review recommending approval while carrying critical flags, blocking findings, a sub-threshold
  score, or `passed:false`.
- **Vacuous green** (their pattern: a zero-finding run may mean the check never engaged). Six of
  thirteen lint checks had no failing fixture — 4, 6, 7, 8, 13, 14 — so their clean results carried
  no information. Fixtures added for all; check 6 asserts its warning text since it is warning-only,
  and check 13 runs the suite so it cannot seed itself and is recorded as externally proven in 1.13
  rather than silently skipped. Suite is now 25 checks. The c7 fixture initially passed for the wrong
  reason (the temp copy has no git remote, so the check took its no-origin branch); it now creates a
  real origin and mismatches against it.

Also noted, not yet acted on: 26 ledger fields no script reads (their pattern 9, a self-assessment
with no consumer), and derived counts propagating by citation rather than recomputation (their
pattern 3). Both are recorded for the next harvest rather than half-fixed.

## edu_skill_creator.1.13 — 2026-07-28

Ledger row `f14`: the one-off testers become a suite. The plugin prescribed fixture pairs and TDD for
every plugin it generates and had no tests of its own.

- **`tests/run_deterministic.py`** — 18 checks, seconds, no model calls. Every case corresponds to a
  defect that actually shipped: nine seeded lint violations (including the three fail-open holes fixed
  in 1.12 — dead `DEPRECATED` tuple, silent skip on a deleted index, `findings: []` bypass), five
  validator-template probes covering its three former crash paths, and three reachability checks that
  would have caught 1.10's broken reviewer allowlist. Runs on a throwaway copy; never touches the tree.
- **`tests/evals/E1`, `E2`** — the two behavioural prompts that cannot be scripted: cold-start
  execution, and the semantic enforcement audit that caught a false "implemented as check 11" claim
  two review rounds had passed. Reported separately from deterministic results, never overwriting them.
- **Lint check 13** runs the deterministic suite before every push, so a guard that stops firing is
  caught at release rather than discovered by a tester months later. Proven by disabling the check-3
  guard and watching check 13 fail. `--skip-suite` breaks the recursion when the suite calls the lint.

The suite is not proof of correctness. It is proof that specific known failures stay fixed.

## edu_skill_creator.1.12 — 2026-07-28

**Everything here was found by testing the shipped code, not by review.** Three independent agents
were pointed at 0c09837: one executed the skills cold on a real request, one audited every
enforcement claim against its cited target, one ran the scripts. All three found defects that three
prior review rounds and a passing lint had missed.

### The serious one: 1.10 broke the fresh-context reviewer

`lessons_learned.md` became an 18-line pointer stub in 1.10, but **fifteen citations across nine
files still treated it as the substantive ledger** — including `skill_quality_rubric.md` and
`draft/SKILL.md`, which define the independent reviewer's **input allowlist**. `lesson_index.md` and
`reference/lessons/` were not on that allowlist. A Stage 5 reviewer following the documented inputs
exactly would open an empty file and be unable to interpret the numbered critical flags it exists to
enforce. The plugin's central quality gate, operating rule 3, was wired to nothing for two releases.
All fifteen citations swept; Stage 8's write side now targets a new `lessons/` file plus its index row.

### A false enforcement claim that survived two review rounds

L7's fold stated registry completeness was "implemented as release_lint check 11." Check 11 resolves
numbered enforcement claims; **no registry-completeness check existed anywhere.** The claim originated
in ledger row `f21` and passed both independent reviews, because reviewers verified that cited numbers
resolve rather than that claimed implementations exist. New **check 12** now does what was claimed
(every `lessons/` file is referenced by the index), and the lesson records how the false claim survived.

### Three fail-open holes in the lint that polices fail-open holes

- **Check 3 was dead code.** `DEPRECATED = ()` — an empty tuple no content could ever trigger. The
  repo does have a deprecated URL (the pre-rename `maxuwp/page`); populated, and it now fires.
- **Check 11 silently skipped** when `lesson_index.md` was deleted: `if LL.exists()` bypassed its own
  fail-closed guard, so deleting the entire enforcement ledger produced exit 0. Now an error.
- **Check 9 was bypassable** via `findings: []`, which skipped the `resolution_pass` requirement
  entirely. Now required unconditionally.
Each fixed check was seeded with a violation and observed firing; all four proofs recorded.

### The validator template violated its own doctrine

Three uncaught crashes outside the CHECKS loop, each breaking the documented exit-2 contract: a
manifest that is valid JSON but not an object, an unwritable report directory, and `--report` given
with no path. All now exit 2 with a stated reason. And `stamped()` used truthiness where the template's
own lesson says gate flags are validated by type — fixed, plus the `require_bool` helper that lesson
demanded and the template never had.

### Honest enforcement accounting

Eight of the nine 1.11 folds shipped as prose with no mechanical check — the failure L11 and L13 name,
committed in the release that refined L11 and L13. Rather than imply coverage, each now carries an
explicit *Enforcement status* line stating it is guidance only, so a future release adds the mechanism
or withdraws the corollary. Also fixed: L12's detail file cited `architecture item 11` (now Lifecycle
stages) and `scenarios 12–14` (14 is unrelated); `implementation_patterns.md` declared everything in it
an example while P3's mechanism stayed a live mandate in two files; the umbrella claimed "nine lessons"
in one place and "thirteen" in another against an actual eighteen; rubric flags ran 1–10, 13, 14, 11, 12;
and the umbrella never explained that `edu-skill-creator-<stage>` lives at `skills/<stage>/`.

## edu_skill_creator.1.11 — 2026-07-28

The doctrine release. Gate rows f2–f7, f9(partial), f19–f22, f24–f27, f31 as decided in
`reflect_gate_decision.json`. Ledger goes from thirteen lessons to eighteen.

- **Five new lessons.** **L14** check at the layer the claim is about (five observed instances;
  a correctly grounded oral rubric passed a script that was not speech, because neither anchor
  reached the lexico-grammatical layer). **L15** explicit user decisions are authoritative
  constraints. **L16** evidence burden scales with specificity, consequence and volatility, and no
  precision claim is laundered through a category tag. **L17** when the subject taught is a process,
  its structure is content. **L18** make the compliant path cheaper than the workaround.
- **L18 was the conditional row (f4)** and its grounding investigation resolved positively:
  Beautement, Sasse & Wonham (2008) *The Compliance Budget* (NSPW), with Saltzer & Schroeder's
  psychological acceptability. The scope limit is stated in the lesson per L1's corollary — both are
  validated for human users, and the extension to agent behaviour is analogical, carried by the
  observed incidents rather than by the frameworks.
- **Nine folds** into L1 (corpus provenance), L4 (never derive identity from position), L6 (a silent
  substitution is an unconsented change), L7 (registry completeness), L9 (world-dependent examples
  decay), L10 (anti-tell rules checked against the genre; declared language of instruction) and L11
  (verification reports are self-interested; operational criteria; motivating artifact in the
  acceptance suite; independent threshold re-derivation; measure your own exemplars; detectors need
  a domain model of legitimate variation).
- **`reference/implementation_patterns.md` created (f31)**, in this same release, carrying the four
  mechanisms the lessons no longer mandate — hash-bound decision ledger, locked process graph,
  server-stamped decisions, rendered-surface probes — each with the capability it satisfies, the
  product type it suits, portability, a simpler fallback, and where it was actually run. Shipping it
  later would have made the relocation a deletion.
- **Enforcement added, not merely claimed**: rubric critical flags 13–14, grounding step 2 (the
  layer question), architecture item 6, intent item 8, test scenarios 16–17.
- **Two defects caught in this build.** Inserting numbered items duplicated `3.` in grounding and
  `7.` in architecture, and shifted the computed-validation plan from item 11 to 12, silently
  invalidating L11's enforcement claim. Renumbered, claim corrected. Lint check 11 also silently
  ignored `grounding step`/`intent item`/`draft step` claims because those patterns were not in its
  target table; extended and proven with a seeded `grounding step 99`.
- The L14–L23 proposal document is marked SUPERSEDED with an explicit mapping, since its numbering
  does not match the shipped lessons (L13: mark historical, never leave a superseded instruction live).

## edu_skill_creator.1.10 — 2026-07-28

Gate row `f1` only: the lessons ledger becomes an always-read card plus detail files. No doctrine
changes; the approved lessons and folds land in 1.11.

- **The defect.** `skills/draft/SKILL.md` tells authors that depth belongs in references "loaded on
  demand", while the umbrella ordered `lessons_learned.md` read "before doing anything". That file
  was 346 lines and 3,297 words with its index at line 325, so an agent reading top-down consumed
  the whole evidence corpus before reaching the summary.
- **The split.** `reference/lesson_index.md` is now the always-read card: 25 lines, one row per
  lesson, carrying the single authoritative applicability map. Each lesson's full entry moved to
  `reference/lessons/L01…L13_*.md`, pulled when a stage appears in its Applies-to column.
  `lessons_learned.md` remains as a pointer only. Stage skills cite lesson ids; they do not restate
  the rules, because a second map would drift from the first (L7).
- **Lint check 11 hardened.** It previously parsed the quick-reference table inside
  `lessons_learned.md`. After the split it found no table and passed vacuously — a check that
  silently checks nothing. It now reads the card, **fails closed when it parses zero rows**, and
  additionally verifies that every lesson id resolves to an existing detail file (the dangling-id
  requirement in `f1`). Proven both directions: a seeded `L01_MISSING.md` path fails, restore passes.
- Decided at the gate recorded in `reflect_gate_decision.json` (28 rows, 8 grouped calls).

## edu_skill_creator.1.9 — 2026-07-28

L13 applied to L13: the lesson that forbids promising enforcement the code refuses had
shipped promising two enforcement points that did not exist.

- **The defect.** L13's "Enforced at" column claimed `edu-skill-creator-release sweep`
  and `edu-skill-creator-test scenario 15`. The release skill carried only the older,
  narrower "semantic-drift grep" (scoped to rules changed *this* release, no count
  requirement), and the test suite ended at scenario 14. Only `rubric critical flag 12`
  was real. L13 was also the sole lesson with no enforcement paragraph (L11's is
  deliberately shared with L12).
- **Swept the class, reporting the count** (L13's own rule): all 13 rows audited, 29
  resolvable claims checked, **1 unresolved** — plus one claim ("release sweep") that
  proved *unverifiable as written*, because a bare skill name plus a noun cannot be
  checked. Claims now cite numbered units for exactly that reason.
- **`release_lint` check 11** resolves every numbered enforcement claim in the ledger's
  quick-reference table against the numbered items actually present in the rubric, test,
  architecture and release skills. Falsifiability came free and in the honest direction:
  the check FAILED on the real shipped defect before any fix, and a seeded `architecture
  item 99` fails on restore. This makes the ledger's enforcement column computed rather
  than asserted, which is L11 applied to L13.
- **The enforcement now exists.** `edu-skill-creator-release` step 2 is rewritten as the
  **class sweep**: two triggers (rules changed this release; any review finding citing a
  file:line), one pass, report the count rather than "fixed as suggested", delete or
  move superseded instructions rather than annotate them, table cells whose value is the
  instruction named explicitly, and the wrong-layer signal when a second round finds
  another instance. `edu-skill-creator-test` scenario 15 plants one instruction in four
  surfaces and cites one, with the table-cell variant. `edu-skill-creator-draft` step 3
  carries the same rule at the layer where review findings are actually handled.
- L13 gains its enforcement paragraph.

No stage, gate, schema or product-behaviour changes.

## edu_skill_creator.1.8 — 2026-07-27

L13 — the authoring half of L11: once a skill ships both prose and enforcement, the prose
can teach what the code refuses.

- New `lessons_learned.md` L13, harvested from posed_skill.1.64–1.66. The evidence is
  POSED's six-round 1.66 review: `hitl_protocol.md` listed `approved: true` as the manifest
  effect of a terminal approval that `approval_provenance.py` refuses in every contract era,
  and the same instruction had four more homes (orchestrator step 4, the README, the
  harness-adaptation note, and the outline skill's "Upload an override" path, which saved
  pasted content *as the approved outline*). Each round fixed the cited line and found the
  next home. The rule: sweep the class in one pass and report the count.
- **Annotation is not repair.** The four-option table survived a round with an explicit
  non-approval warning above it. A Manifest-effect column reading `approved: true` is an
  instruction; prose above it is commentary. Superseded procedure is deleted or moved to a
  marked historical section — Anthropic's "old patterns" rule applied to procedure, not
  only to time-sensitive facts.
- Corollaries also recorded: when each round finds a new instance the fix is at the wrong
  layer (the 1.64 CSP precedent); a contradiction inside one instruction set is one defect
  with two locations, so deferring half is a scheduled regression; measure the region, not
  the file; a dispute between two competent reviewers usually indicts your own rule rather
  than either reviewer.
- `skill_quality_rubric.md` gains **critical flag 12** so L13 blocks rather than advises.
- Quick-reference table and the umbrella's stale "nine lessons" pointer updated (thirteen).

No stage, gate, schema or validator behaviour changes: this release adds a lesson, a
critical flag, and their citations.

## edu_skill_creator.1.7 — 2026-07-10

L11 becomes generated, not just required: scaffold ships a validator template.

- New `skills/scaffold/reference/validator_template.py` — self-contained,
  import-free skeleton embodying every L11 corollary: fail-closed helpers
  (`require_file`/`require_record` — missing = critical, never a skip; crashing check =
  failing check; exit 2 when the session can't even be read), L12 contract-era +
  `generated_by` helpers, per-id upstream-coverage pattern (never count matches), a
  repetition/distribution helper, report JSON with `passed`/counts/findings, and the
  fixture-runner lint check in its docstring. Behavior-proven before shipping: exit 2 on
  bare/unreadable sessions, exit 1 with a written report on missing records, exit 0 on a
  compliant sample.
- `edu-skill-creator-scaffold`: new "Validator scaffolding (L11)" section — one
  instantiation per architecture item-11 artifact; both callers wired into the generated
  drafter/reviewer/umbrella stubs; `tests/fixtures/<artifact>_{fail,pass}/` in the
  generated tree; the generated lint gains the fixture-runner check with both-direction
  falsifiability ("neutralize the negative fixture and watch the LINT fail"); exit check
  extended (each validator compiles + exits 2 on a bare directory before any session
  exists).
- Cross-refs: architecture item 11 notes the plan only names artifacts + requirements
  (scaffold designs nothing ad hoc); L12's enforcement paragraph records that the
  template is generated. POSED's `validate_stage5_slides.py`/`validate_outline.py`
  cited as worked examples.

## edu_skill_creator.1.6 — 2026-07-10

Reflect harvest from the POSED 1.15–1.30.1 release run (16 releases, 4 days, the
three-model review loop): two new lessons, one corollary, and gate-pattern hardening.

- **L11 — prose contracts rot; computed, fail-closed validators.** The defining pilot
  fact: a deck passed FOUR fresh-context reviews at 94/100 while carrying 13 structural
  criticals, and its approved outline scored 97/100 with 5 more. LLM review establishes
  judgment, not structure. Rule: one validator implementation, two callers (drafter
  pre-gate + reviewer hard gate); `approve` illegal without recorded computed passes.
  Corollaries: fail closed (missing record/artifact/contract = refusal — six fail-open
  holes found by adversarial review in 1.30.1); prove by attack, not only by fixture;
  falsifiability against real failing artifacts + synthetic fixtures (never course
  content); distribution checks (one sentence ×54 passed a 98% word-count band);
  anti-softener rubric language; server-stamped decisions (mechanical L5).
- **L12 — live sessions outlive releases.** `generated_by` + server-owned
  `session_contract_version` on every artifact; contract upgrades distinguished from
  quality gaps; schema changes route to TARGETED amendments of the owning step, never
  full regeneration; unknown contract versions fail closed (a live session carrying
  "1.13" had disarmed every ≥1.29 check).
- **L7 corollary — one canonical implementation inside the plugin**: POSED shipped three
  divergent pacing formulas and two key vocabularies for one concept; prose cites the
  canonical script, never restates values; near-miss keys hard-fail with "did you mean".
- **gate_design_patterns 8–11**: AI pre-fills recommend but hard gates still block
  (`faculty_overrode` audit trail); blank-gate guard + server-stamped decisions; agent
  silence during human review; gate links never navigate away.
- **architecture**: item 5 gains the contract axis (L12); new item 11 computed-validation
  plan (L11). **rubric**: critical flag 11 (prose-only structural enforcement / fail-open
  guards / approve-without-computed-checks); flag 6 extended to contract staleness.
  **test**: scenarios 12 (rationalizing reviewer), 13 (fail-open forgery), 14
  (authoring-context/deixis leakage — students must never see the scaffolding
  conversation). **draft**: no softener language; rubrics cite validators, never restate.

## edu_skill_creator.1.5 — 2026-07-09

Lesson L10 promoted from the POSED pilot (the reflect pattern, run live): educational
content is heterogeneous — templates must be content-type-aware.

- **lessons_learned.md L10** (+ quick-reference row, provenance updated to include
  posed_skill.1.24–1.25): any stage drafting/transforming/rendering teaching artifacts
  works from an explicit content-type registry (definition, equation, derivation,
  procedure, worked example, comparison, code, data figure, …), each type with its own
  body grammar, budgets, and reviewer checks. Corollary: precision blocks are atomic
  end-to-end, and the registry must be wired into EVERY downstream transformer — a rule
  that lives only in the drafter dies in the next stage (POSED 1.24 → 1.25 demonstrated
  both halves).
- **edu-skill-creator-intent**: A.1 now also asks what content TYPES the artifacts carry.
- **edu-skill-creator-architecture**: step 1 requires the content-type registry for
  artifact-producing stages, with the precision-block rule wired into all transformers.
- **skill_quality_rubric**: critical flag 10 — one-size template on heterogeneous
  content, or precision content trimmable/paraphrasable anywhere in the pipeline.
- **edu-skill-creator-test**: pressure scenario 11 — seed a cited definition, equation,
  and code block; verify wording/notation intact through every transform stage.
- **edu_grounding_library**: Alley scope limit sharpened — the visual-evidence body
  applies to data/figure content; precision text is its own evidence.
- Fixed three 1.4 rename casualties where the common noun "page" had become
  "edu-skill-creator" ("HITL page", 2× "gate/human page renders").

## edu_skill_creator.1.4 — 2026-07-06

Rename release: PAGE is now **Edu Skill Creator**.

- Renamed the plugin id, umbrella skill, subskill frontmatter names, placeholders,
  README/maintenance docs, release lint prefix, and dev-link script from generic
  `page` / `PAGE` naming to `edu-skill-creator` / `Edu Skill Creator`.
- Updated both manifests to `edu-skill-creator` 1.4.0 and pointed homepage/repository
  metadata at `https://github.com/maxuwp/edu-skill-creator`.
- Future release headings use `edu_skill_creator.X.Y`; older entries below retain the
  old `page_skill.*` tag prefix for historical accuracy.

## page_skill.1.3 — 2026-07-06

Tiny Codex release-evidence cleanup.

- Corrected the page_skill.1.2 review-evidence tally to match the machine-readable
  review logs: 36 findings total, 16 fixed and 20 accepted.
- Added release_lint check 9: every `reviews/*_review.json` finding must carry
  `status: fixed|accepted` plus a non-empty `resolution`, and every review file with
  findings must carry a `resolution_pass` block. The check was falsifiability-tested
  by deleting a finding status in a temp copy and confirming lint failed.

## page_skill.1.2 — 2026-07-06

Release-evidence hygiene (second Codex review round). No workflow changes.

- **Review logs are now mechanical evidence**: every finding in `reviews/*.json`
  carries `status: fixed|accepted` + a one-line `resolution`, and each file a
  `resolution_pass` block naming the release it was resolved against (36 findings:
  16 fixed, 20 accepted). A status-less finding = open; there are none.
- **Uniform skill versioning**: every SKILL.md frontmatter `version` now tracks the
  plugin major.minor and is bumped together on release. New lint check 8 enforces it
  (falsifiability-tested: failed on all 10 stale files before the bump). Per-skill
  history lives in this changelog.
- **`release_lint.py --publish`**: after the publish gate, the "manifests claim a
  hosted repo but no origin exists" case escalates from warning to error
  (falsifiability-tested with origin removed). `edu-skill-creator-release` step 8 and
  MAINTAINING.md now call for publish mode post-publish.
- edu-skill-creator-refresh: Part B (grounding-library judgment) scoped INTO the independent
  review alongside Part C, per the round-3 reviewer's finding; only Part A's pure
  fact-reporting keeps the L3 waiver.

## page_skill.1.1 — 2026-07-06

Codex review round: privacy/security/accessibility hardening + Edu Skill Creator reviewed by its own
instrument.

- **Stage 1 intent**: new interview questions A.7 (student data/PII, FERPA/PPRA +
  institutional constraints, retention/deletion, de-identification, external
  API/vendor exposure, logging/redaction, permissions) and A.8 (accessibility, incl.
  the plugin's own HITL pages); three new contested postures (accessibility,
  student-data handling, external-service); persisted `intent_gate_decision.json`.
- **Grounding library**: new privacy/security/accessibility section — W3C WCAG 2.2,
  CAST UDL 3.0, FERPA/PPRA + Dept. of Education PTAC, NIST SP 800-218 (consolidated).
- **Architecture**: mandatory data-flow & security model for plugins touching student
  data, external services, or generated UI; exact inputs + refusal conditions;
  independent design review + full gate spec.
- **skill_quality_rubric**: critical flags 7–9 (ungoverned student data, undisclosed
  external services, inaccessible HITL pages).
- **edu-skill-creator-test**: pressure scenarios 7–10 (student-data leakage, undisclosed external
  call, log/redaction failure, gate keyboard/screen-reader operability); fresh-context
  GREEN judges; exit gate spec (`test_gate`).
- **release_lint check 7**: manifests' homepage/repository URLs must match the git
  origin (mismatch = error, missing origin = warning). Falsifiability-tested in both
  directions before landing. Lint also hardened against a missing CHANGELOG.
- **Edu Skill Creator reviewed by Edu Skill Creator's rubric** (durable evidence in `reviews/`): all 10 skills
  cold-reviewed by fresh-context subagents, findings fixed, revised skills
  re-reviewed to a green board — final scores 88–98, zero critical flags. The round
  caught real defects in its own author: no self stale-state at the umbrella (fixed:
  operating rules 7–8), grounding/reflect/draft/refresh shipping without the
  independent-review or invalidation discipline they preach (all fixed), and — outside
  the repo entirely — POSED's `posed-refresh` symlinks missing from both harness trees
  (relinked).
- Every stage gate now carries the full gate-spec table (gate_id, decision_file,
  owns, invalidates, consent); binary inspections are explicitly distinguished from
  scored rubrics (Fagan/IEEE 1028).

## page_skill.1.0 — 2026-07-06

Initial release: the full authoring pipeline, built to the plan in `docs/BUILD_PLAN.md`.

- **Umbrella + 9 stage skills**: `edu-skill-creator` (dispatcher), `edu-skill-creator-intent` (interview +
  contested-choices inventory), `edu-skill-creator-grounding` (framework map before design),
  `edu-skill-creator-architecture` (stages, gates, dependency model, BUILD_PLAN output),
  `edu-skill-creator-scaffold` (dual-harness repo generation), `edu-skill-creator-draft` (skills + rubrics with
  fresh-context review), `edu-skill-creator-test` (RED/GREEN/REFACTOR + education-specific pressure
  suite, consent-gated), `edu-skill-creator-release` (lint, lockstep, semantic-drift grep,
  author-gated publish), `edu-skill-creator-reflect` (post-pilot harvest, approve-per-item),
  `edu-skill-creator-refresh` (~90-day source refresh).
- **Reference set**: `lessons_learned.md` (the nine POSED/p2d lessons as design
  requirements), `edu_grounding_library.md` (starter framework menu with scope limits),
  `gate_design_patterns.md` (gate spec + decision JSON + stale-state model),
  `dual_harness_playbook.md` (repo/symlink/lint specification),
  `skill_quality_rubric.md` (/100 reviewer instrument, threshold 85, 6 critical flags),
  `harness_adaptation.md` (placeholder mappings).
- **Scripts**: `release_lint.py` (6 checks, falsifiability-tested during this build —
  the path and changelog checks were observed failing before their fixes landed),
  `link_dev_dirs.py`.
- Sources synthesized: Anthropic skill-creator, official plugin-dev plugin, obra
  writing-skills (TDD for skills), POSED posed_skill.1.4–1.14, p2d p2d_skill.1.4–1.6.
