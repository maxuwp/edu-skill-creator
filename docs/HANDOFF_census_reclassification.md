# Handoff — re-classify the evidence-level census (independent second reader)

**For:** Fable or Grok — **preferably whichever did NOT review CR 1.20**, since this document's
whole purpose is a second, differently-provenanced reading.
**From:** the edu-skill-creator thread, 2026-07-31, release 1.19.
**Subject:** `docs/CENSUS_evidence_levels_2026-07-31.md` — sixteen lint checks classified by
evidence level.
**Why you and not me:** the census is, by its own §4, a level-3 artifact: one agent classifying its
own code by reading it. Its rows are about to become a protected baseline that later rounds must
preserve, and a wrong row there becomes defended error rather than a passing mistake. This is
`c31` of the sibling CR, and it is invariant 8 (independent semantic review, cold context) applied
to the document that implements invariant 8.

**This is a RE-CLASSIFICATION, not a fresh audit.** Do not look for new defects in the lint; five
rounds have already done that. Judge the classifications.

---

## 1. The scheme

From the POSED thread's circular-evidence handoff. Every check declares what its operands are and
who authored them; the level follows.

| Level | Name | Establishes | Typical instrument |
|---|---|---|---|
| 1 | Grounded | Fact | Source bytes, server-stamped human decisions, authoritative external sources |
| 2 | Recomputed | Fact, derived | Deterministic computation *over grounded evidence* |
| 3 | Cross-checked | Consistency, not truth | Agreement between fields the same author wrote |
| 4 | Independently reviewed | Judgment | Fresh-context reviewer against an explicit rubric |
| 5 | Asserted | Nothing on its own | Author self-report; advisory |

The rule that gives it teeth: **a level-3 or level-5 result may never be reported to a faculty
member as "verified", and may never authorize a gate on its own.** The trap the scheme is built
around: a check can be arithmetic, deterministic and mutation-tested — every hallmark of level 2 —
and still be level 3, because its *operands* were written by the same agent.

## 2. Confirm first, then correct

**Part A — which classifications hold, and how you checked.** Read the check body in
`scripts/release_lint.py`, name its operands, name who authored each, and say whether the assigned
level follows. Verify by reading code, not by reasoning from the census's prose — the census is the
thing under test, and its "who wrote this operand" claims are exactly what could be wrong.

**Part B — which classifications are wrong**, each as the smallest correction: the row, the level
assigned, the level you would assign, the operand that decides it, and which Part A rows your
correction must not disturb.

## 3. Where I expect you to disagree, stated so you can prove me wrong

The census flags two of its own rows as arguable. Judge those first, and treat my reasoning as the
hypothesis, not the context:

- **Check 4 (rubric arithmetic).** Assigned level 2 "about the file". The sum is a genuine fact
  about the bytes; the numbers summed were written by an agent. Is "level 2 about the artifact,
  establishing nothing about the world" a coherent position, or is it the exact rationalization the
  AI-Completability example in §1 warns against? This is the row I am least sure of.
- **Check 9 (review evidence).** Split across two levels in one row — 3 for field contents, 2 for
  the population derived from the filesystem. Is a split row legitimate, or does a check that mixes
  levels need to be reported at its weakest?

Two more worth a hard look:

- **Check 13's canary.** Called "the only experiment in the file" and assigned level 2. It mutates
  code and observes behaviour, which reads as genuinely grounded — but it observes the *suite's*
  output, and the suite is agent-authored. Does the mutation rescue it, or is it level 3 with extra
  steps?
- **Check 7 (manifest URL vs git origin).** Assigned level 2 on the grounds that `git remote
  get-url` is environment state rather than authored. Is environment state under the same author's
  control "grounded"?

## 4. The finding you should try hardest to break

The census's §2 asserts one real defect: check 15's `computed_checks` clause authorizes a gate on a
boolean the reviewing agent wrote about its own conduct, and nothing opens the validator report it
names. If that is wrong — if some path does read a report, or if the clause cannot in fact
authorize anything on its own — it is the most valuable thing you can return, because a sibling CR
row (`c20`) is scoped to fix it and would be wasted work.

The census's claim is falsifiable by search: it says no code in the repository opens a validator
report. Check that directly.

## 5. Also worth your judgment

- **§3, the missing third outcome.** The lint has 47 error sites and no warning sites: error or
  clean, nothing else. The census argues invariant 4 (`unverifiable`, never `pass`) has nowhere to
  live. Is adding a third verdict the right fix, or does it create a category that gets used to
  soften real failures?
- **Is the scheme itself right for a lint?** It was designed for a validator that judges *course
  material*. A release lint judges *a repository*. Does the five-level scheme transfer cleanly, or
  does it need a sixth level or a different level-1 definition here? Say so if it does not fit — the
  scheme is not sacred and this is the first time it has been applied outside its home.

## 6. Output

1. **Part A** — confirmed classifications, numbered, each with how you checked.
2. **Part B** — corrections, each as the smallest change, naming what it must not disturb.
3. **A corrected sixteen-row table**, so the result is directly usable as the baseline.
4. **One paragraph:** is this census fit to become a protected baseline, or does it need a third
   reader first?

State plainly where you could not verify something. A false correction here is worse than a missed
one, because the output becomes the thing later rounds are forbidden to break.
