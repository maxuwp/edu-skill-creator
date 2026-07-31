# Review of CR 1.20 — Fable, method and evidence lens

**Reviewer:** Claude (Fable 5), 2026-07-31, independent pass per
`docs/HANDOFF_CR_1.20_review_fable_grok.md`. Repo access: yes; the CR governs where it and the
handoff differ (no material differences found).
*Received verbatim; two bare path citations were qualified to repo-root form so the
release lint's citation check passes. No content changed.*

**Scope:** the causal claim, the measure, the four instances, the CR's own evidence standard, and
the `c16` protected-error problem. Design and blast radius are Grok's pass.

---

## Part A — Confirmed

Each entry is a property I verified and how. These are the do-not-break baseline for the next
revision of this CR.

1. **Instance A's round-by-round narrative is corroborated by the repository, in detail.** Each
   table row maps to a specific changelog entry: 1.15 records the vacuous suite cases and that
   1.14's citation fix did not land; 1.16 records the print-satisfiable check-13 floor; 1.17
   records the `ESC_LINT_DEPTH` off-switch reproduced with command output; 1.18 records the brief
   change, the 20 findings, and the confirmed-and-preserved contract; 1.19 records the 7/7 and
   17/17 baseline re-verification, nine of ten findings in 1.18's own surfaces, and exactly one
   regression. Checked by reading `CHANGELOG.md` entries 1.14–1.19 against the CR's table. This is
   load-bearing because the CR's core evidence is real repository history, not reconstruction.

2. **The rows modify what they say they modify.** The current rubric
   (`skills/edu-skill-creator/reference/skill_quality_rubric.md`) carries free-prose `fix` in its
   findings schema (line 70), no `verified` array, fourteen critical flags (so `c11`'s "flag 15"
   is the next slot), and an iteration policy under which `approve` needs no confirmed property.
   Checked against the file directly. Load-bearing: `c1`–`c3` and `c11` describe the current
   state accurately, so the deltas are what they claim to be.

3. **The numbering and the historical-log count are exact.** `release_lint.py` has sixteen
   numbered checks, so checks 17–18 are correctly named; `reviews/` holds exactly twelve
   `*_review.json` files, so `c5`'s "twelve compliant historical reviews" is exact, and check 17
   without the era gate would fail on all of them. Checked by enumerating the lint's check
   comments and counting the directory. Load-bearing: `c5`'s "this row is why `c4` can ship at
   all" is arithmetic, not rhetoric.

4. **The POSED precedent exists as claimed.**
   `posed-plugin/skills/ai-audit/scripts/validate_audit.py:2277` implements
   `review_strengths_missing`: every audit review log must carry a non-empty `strengths` list and
   a `preserve_units` list, fail-closed criticals otherwise. Checked by reading the check body.
   Load-bearing: feasibility of mechanising the confirm half is demonstrated by shipped code, not
   asserted. (One wording caveat, Part B F7.)

5. **"Prose is not enough" is grounded in this repo's own recorded failures.** The 1.15 entry
   records an enforcement claim naming "release_lint check 11" when no such check existed,
   surviving two independent reviews; the 1.18 entry records L11's central gate as "prose in four
   files and code in none". Checked in the changelog. Load-bearing: §3 is the justification for
   `c4` and `c7` being lint checks rather than doctrine, and it holds.

6. **The already-landed wiring already depends on `c1`.** `skills/draft/SKILL.md:76` instructs
   saving "the rubric's output JSON, whose `verified` array holds the confirmed baseline" — and no
   schema defines that array. Checked by diffing the wiring against the rubric's output schema.
   Load-bearing in a direction the CR does not state: if the gate rejects `c1`, a shipped
   instruction cites a nonexistent field, which is exactly the L7 defect class recorded in
   Part A 5. `c1` is not merely desirable; its rejection leaves the repo in a state its own lint
   doctrine condemns.

7. **`c16` names the right residual risk and the qualitative claim behind the CR survives attack.**
   I looked for a rounds-4–5 finding that reopened a prior fix beyond the one the CR itself
   records, and found none; and the shape of the fixes differs visibly across the brief change —
   rounds 1–3 each replaced a mechanism wholesale and each replacement carried the next defect
   (floor → print-satisfiable; bound → off-switch), while 1.19's fixes are narrow in-place
   modifications (per-hop checking, a required key, a file-scoped exclusion). That qualitative
   shift is evidenced by the entries themselves and is what the CR is actually entitled to claim.
   The quantitative form it uses instead is Part B F1.

8. **The verbatim brief language is consistent across its three homes.** L19's "brief language
   that works" block, the landed `skills/draft/SKILL.md` dispatch, and `c14`'s intent match. Checked by
   reading all three. Load-bearing for `c14`: single-source is already true of the prose; `c14`
   extends it to the generated playbook.

**Could not verify, stated plainly:** Instance B — the talk-like-a-professor repository is not in
this workspace; I checked the narrative's internal consistency with L19 only. Instance D — author
testimony, not examinable. The "roughly a third of reviewer effort" figure — no repo artifact
measures effort. Round 5's own fixes — no round 6 has audited them, so their reopening count is
unobserved (this matters; see F1).

## Part B — Findings

### Major

**F1 — §2 and `c15`: the "3/3 → 0/30" measure mixes units and censors the after-period.**
The before-number counts *fix-sets that were later reopened, per fix-set*, discovered by the next
round. The after-number counts *reopenings per finding* — a different denominator, inflated by
rounds 4–5 returning many findings — and reopenings caused by a round's fixes are only observable
in the *next* round: round 4's fix-set did produce one regression (1.18's check-3 `tests/`
exclusion dropping 1.17 coverage, found in round 5), and round 5's fix-set has had no subsequent
round at all. Measured the way rounds 1–3 were measured, the record is: rounds 1–3, three of three
fix-sets reopened a prior property, wholesale; round 4, one narrow regression, caught by the
baseline re-verification; round 5, not yet observable. That is a strong result — the CR does not
need the inflated form, and its own table row 5 already contradicts "0/30" by recording the
regression.
*Smallest modification:* in §2 and in `c15`'s proposed lesson text, replace the two rates with the
per-fix-set statement above, and mark round 5 "unobserved, no subsequent round". Must not disturb
A1, A7.

**F2 — §2 "the only variable changed was the brief": confounded, and the repo documents the
confounds.** Three things co-varied with the brief: (i) the deterministic suite grew 25 → 59 → 78
falsifiable cases *before* round 4 (1.15 made every case name its guard), so by round 4 prior
fixes were mechanically pinned and a reopening would trip the suite regardless of brief; (ii)
round 3 had no external auditors — both terminated on session limits and 1.17 is a self-audit —
so auditor identity and process changed alongside the brief; (iii) 1.19 itself reports nine of ten
findings in surfaces 1.18 had just touched, consistent with older surfaces having been swept
clean by three prior rounds. Note the direction of (i): it *supports* Group B — a mechanised,
cumulative, falsifiable baseline is precisely what the growing suite already was — while weakening
attribution to the brief prose specifically (`c11`, `c14`). Instance B's strongest datum has the
same shape: the convergence event was the *baseline artifact* existing, not a brief rewording.
The evidence, read strictly, supports "mechanically pinned baselines stop reopenings" more
directly than "confirm-first prose stops reopenings".
*Smallest modification:* in §2 (and `c15`), replace the single-variable sentence with: the brief
was the deliberately changed variable; the suite's growth in falsifiable cases, the absence of
external auditors in round 3, and surface hardening changed concurrently; the attribution is to
the combination, and the component the repository's own evidence most directly supports is the
mechanised baseline. Must not disturb A1, A7. No row's *design* changes — this is an evidence-
honesty fix, and it strengthens Groups A/B's rationale rather than weakening it.

**F3 — `c4`/`c16`: the CR's stated mitigation for its main risk is prose-only under its own
lint.** `c16`'s mitigation is "`how_verified` must be a re-runnable mechanism, never 'read it and
it looked right'" — but check 17 as specified in `c4` verifies only non-emptiness of `verified`,
presence of `modification`, and `preserve`-id resolution. A `verified` entry whose `how_verified`
is "read it and it looked right" passes the very check this CR adds, and §3 of this CR is an
argument that exactly this arrangement drifts. The asymmetry is sharp because `c7` *does* impose
the standard on the ledger: every `confirmed` row names a suite case id or an explicit "not
mechanisable, because …". The review log is where baseline entries are born; it has the weaker
rule.
*Smallest modification:* extend `c4`'s check 17 with `c7`'s clause — each `verified[].how_verified`
must name a runnable case/command or state "not mechanisable, because …" — plus one negative
fixture for that branch. `c13` then inherits the strengthened form automatically. Must not disturb
A2, A3, A4.

**F4 — `c7`/`c16`: the escape hatch for a wrong `confirmed` row is load-bearing and shapeless.**
The handoff asks what happens when a baseline entry turns out to be wrong; the CR's only exit is
"a recorded supersession", with no required content, no evidence burden, and no authority named.
Because monotonicity is the point of `c7`, an undefined supersession degenerates one of two ways:
too easy (any round writes one and the ledger is decorative) or too socially hard (no one dares
demote a protected row and the error is defended — the exact `c16` failure). Which way it goes
gets decided ad hoc by the first reviewer under pressure.
*Smallest modification:* `c7` specifies the supersession record's minimum shape: the superseded
row id; a demonstration that the original verification was faulty *as a mechanism* (re-run the
recorded `how_verified` against the case it should have caught and show it passing — prove the
verification vacuous rather than re-arguing the property); the round and reviewer; and routing to
the human gate for the demotion itself. Additionally fold into `c16`'s lesson text: protected
error's likeliest home is the `present-but-not-a-defect` verdict, which certifies an absence and
is the hardest verdict to verify by mutation. Must not disturb A4, A7.

### Minor

**F5 — §2 Instance D: fails the CR's own L16 standard as used.** Uncited author testimony carries
the CR's broadest claim ("systematically", "other AI tools"). L16: the burden scales with the
claim. *Smallest modification:* label Instance D "author-reported, not independently examinable
here" and scope the systematic-misreading sentence to what Instances A–C support. Must not
disturb A1.

**F6 — `c8`: the seed data is not in the repository.** The 24 invariants "each already carrying
its file:line" exist only as summary counts (7/7, 17/17) in the 1.19 changelog entry; the
enumeration lives in session context, which expires. As written, `c8` is executable only while
this conversation survives — for a ledger whose stated point is "not re-deriving it".
*Smallest modification:* attach the 24-row enumeration as an appendix to this CR (or a `docs/`
file) before the gate, so `c8`'s input is repo-durable. Must not disturb A1, A3.

**F7 — §2 Instance C: "already solved" overstates what was verified.** POSED's mechanism is
shipped and enforced (A4), but the CR offers no outcome evidence that it reduced reopenings
there; and POSED's check explicitly permits an empty `preserve_units` list, a softer contract
than this CR proposes. Precedent for feasibility, yes; "solved", not shown.
*Smallest modification:* "already shipped and enforced" for "already solved", plus one clause
noting this CR strengthens the POSED contract rather than porting it unchanged. Must not disturb
A4.

**F8 — §Origin: "the brief changed once" — it changed twice.** Round 4 introduced confirm-first;
round 5 added the carried-forward baseline, which is itself the ledger treatment under review.
Two treatments, one round apart, is the honest description, and it also bears on F2 (the round-5
result cannot be attributed to the brief alone). *Smallest modification:* "changed once, then
extended once with the carried-forward baseline", and qualify "unusually clean" accordingly. Must
not disturb A1.

## Row-by-row disposition

| Row | Disposition | Reasoning |
|---|---|---|
| `c1` | approve | Field is accurately scoped against the current schema (A2), and the landed draft wiring already cites it (A6) — rejection leaves a shipped false claim. |
| `c2` | approve | The modification-plus-preserve pair is the operative half of L19; replacing free-prose `fix` is what makes findings arrive as modifications. |
| `c3` | approve | Accurate about the current iteration policy; the POSED mirror is fair at this row's level (the strengths half of A4). |
| `c4` | approve-with-modification (F3) | Add the `how_verified`-names-a-mechanism clause; without it the CR's own §5 risk statement is unenforced prose. |
| `c5` | approve | The twelve-log count is exact (A3); the era gate is arithmetic necessity, not caution. |
| `c6` | approve | The two added verdicts answer a failure mode L19/Instance B documents (oscillation of cases with nowhere to go); path spelled unbackticked correctly. |
| `c7` | approve-with-modification (F4) | Monotonicity needs a defined supersession shape and authority, or it is decorative or despotic. |
| `c8` | approve-with-modification (F6) | Seed list must land in the repository before the gate; today it exists only in session context. |
| `c9` | approve | Wiring row; per-relationship placement follows from `c6`'s design. |
| `c10` | approve | The row the evidence most directly supports: the growing falsifiable suite is what demonstrably pinned prior fixes (F2, direction (i)). |
| `c11` | approve | Flag numbering verified (A2); a blocking flag is this repo's established way to make a rule bind. |
| `c12` | approve | L13 sweep-the-class, correctly applied to the two undispatched stages. |
| `c13` | approve-with-modification (inherits F3) | Propagate only the strengthened check 17, or every generated plugin inherits the prose-only mitigation. Blast-radius design itself is Grok's pass. |
| `c14` | approve | Verbatim consistency across the three homes verified (A8). |
| `c15` | approve-with-modification (F1, F2, F8) | Fold the corrected measure and named confounds into L19; the current "3/3 → 0/30" form would bake a confounded attribution into doctrine. |
| `c16` | approve-with-modification (F3, F4) | The row is right to exist (A7); its mitigation must be enforced (F3) and its escape hatch defined (F4), with the `present-but-not-a-defect` caveat recorded. |
| `c17` | defer | Agree with the CR: the diff's shape is unknowable before two rounds of the new schema exist. |
| `c18` | defer | Agree: gate-load cost against L4's budget is Dr. Ma's call and nothing here forces it now. |

## If I were Dr. Ma

Gate `c15` and `c16` first, amended per F1/F2/F8 and F3/F4, because they are the CR's claims about
itself: every other row will be cited against this evidence record, and the current quantitative
form is the one part of the CR that would not survive the confirm-first standard it proposes. Then
`c1`–`c5` as a block (with F3's clause), since the landed draft wiring already references the
`verified` array and the repo is in an L7-violating state until `c1` ships, and `c4` without `c5`
breaks twelve compliant logs. Then `c6`–`c8` (with F4's supersession shape and F6's appendix),
which is the mechanism the evidence most directly supports. `c9`–`c12` and `c14` follow
mechanically. Hold `c13` until one internal round has run under the new schema — propagating to
every generated plugin is the one decision here that is expensive to walk back, and nothing in the
evidence requires it to ship simultaneously.
