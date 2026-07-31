# Evidence-level census — release_lint 1.19, and the validator template it ships

**Run:** 2026-07-31, at release 1.19 (`6cd39f9`), answering open question 1 of the POSED thread's
circular-evidence handoff: *does edu-skill-creator's own generated lint have this defect?*
**Method:** for each check, name its operands, name who authored each operand, and assign the
evidence level the POSED handoff defines. Levels: 1 grounded · 2 recomputed over grounded ·
3 cross-checked (same authoring provenance) · 4 independently reviewed · 5 asserted.
**Standing artifact.** This is a baseline, not a one-off. A check that changes level, in either
direction, changes what may be said about it.

**Answer: yes, in one place, and it is the newest code.** Fifteen of sixteen checks are level 2 over
source bytes or filesystem state, or are level 3 and named as such. One clause — the
`computed_checks` gate added in 1.18 — authorizes a gate on an agent-asserted boolean and never
opens the artifact that boolean refers to. Details in §2.

---

## 1. The census

| Check | What it concludes | Operands, and who wrote them | Level |
|---|---|---|---|
| 1 harness paths | no shared skill body hardcodes a harness path | repository source bytes | 2 |
| 2 manifest versions | the two manifests agree | two JSON files, both agent-authored | **3**, and the check is named "version mismatch" — consistency is the whole claim |
| 3 deprecated URLs | no file references a retired repo | source bytes vs a literal declared in the lint | 2 |
| 4 rubric arithmetic | dimension points sum to 100 | numbers in an agent-authored rubric | 2 *about the file*; establishes nothing about rubric quality, and claims nothing |
| 5 changelog heading | a real heading exists for this version | file bytes, fences stripped, line-anchored | 2 |
| 7 manifest URL vs origin | the claimed home matches the configured remote | manifest (agent) vs `git remote get-url` (environment) | **2** — one grounded operand; the strongest of the comparison checks |
| 8 uniform skill versions | frontmatter matches the manifest | both agent-authored | **3**, named as a convention check |
| 9 review evidence | every review carries resolution structure, and every skill has a review | review JSONs (subagent-authored) + the skills directory listing | 3 for the field contents, 2 for the population (derived from the filesystem) |
| 11 numbered claims | prose citing "item N" resolves to a real item N | prose (agent) vs numbered items (agent) | **3** — and the conclusion is exactly consistency: it does not claim item N is correct |
| 12 registry completeness | every lesson file is reachable from a parsed index row | directory listing (filesystem) vs parsed rows | 2 |
| 13 suite + count + canary | the suite runs, describes itself honestly, and still detects a broken guard | **the canary mutates code and observes behaviour** | **2**, and the canary is the only experiment in the file — it does not ask, it breaks something and watches |
| 14 artifact drift | the gated artifact is byte-identical to what was approved | sha256 over file bytes vs a recorded hash | **2** over grounded bytes |
| 15 review coherence | a recommendation does not contradict its own record | fields within one agent-authored review | **3**, and correctly named "coherence" — except the `computed_checks` clause, §2 |
| 16 citation resolution | every cited path resolves | citation text vs the filesystem | 2 |

**Nothing in this lint is level 4.** Independent review happens in this project, and its output lands
in the review JSONs, but no *check* consumes a level-4 result. That is a description gap rather than
a defect: the lint does not claim otherwise.

**Nothing in this lint can return level 5 as a pass.** There is no self-report the lint accepts as
authority — with the single exception in §2.

## 2. The defect

`scripts/release_lint.py`, check 15, the clause added in 1.18:

```
if any((ROOT / "skills").glob("*/scripts/validate_*.py")):
    _cc = _d.get("computed_checks")
    ...
    _why += [f"computed_checks.{k}={v!r}" for k, v in _cc.items()
             if k.endswith("_validator_pass") and v is not True]
```

The gate it implements is L11's central one: *`approve` is illegal without a recorded computed
pass.* The operand is a boolean the reviewing agent wrote about its own conduct. The check never
opens the validator report, never confirms the report exists, never re-runs the validator, never
binds a hash. A reviewer that writes `true` without running anything passes.

Level 5 authorizing a gate. Invariants 1 and 2 of the POSED handoff, violated in the newest code in
the file — and violated in the act of converting a prose rule into a mechanism, which is the move
this repository's own L11 and L13 recommend. Converting prose to code does not by itself raise the
evidence level; it only makes the level explicit enough to audit.

**Aggravating: the prose already promised more than the code delivers.** `skills/scaffold/SKILL.md`
says the reviewer's schema carries `computed_checks.<artifact>_validator_pass` **+ report path**,
and the validator template's own header says `approve` is illegal unless `passed: true` *"with a
real report path"*. Nothing in this repository reads a report path. The stricter contract was
written first and the weaker check was built later under the same name.

**Not aggravating, and worth stating:** no plugin has yet been generated by this tool, so no faculty
member has been shown a level-5 result described as verification. The defect is latent. That is why
it is worth fixing now rather than after.

## 3. The structural gap

The lint has two outcomes: error and clean. Forty-seven error sites, zero warning sites remaining
after 1.16 converted the last of them. There is no third outcome.

Invariant 4 of the handoff — *missing independent evidence produces `unverifiable`, never `pass`* —
therefore has nowhere to live. Today that is harmless, because every check either computes over
grounded operands or names itself a consistency check. It stops being harmless the moment a check
wants to say "I could not establish this." With only error and clean available, such a check must
choose between blocking a release it has no grounds to block, and passing silently. Both are wrong,
and the second is the one that gets chosen.

## 4. What this census does not establish

It is itself a level-3 artifact: one agent classifying its own code by reading it. Two of the
assignments are genuinely arguable — check 4 (arithmetic over agent-authored numbers: level 2 about
the file, but the operands are level 3) and check 9 (mixed, split across two rows above). A second
reader, preferably a different model, should re-run the census before its rows are treated as a
baseline. That is invariant 8 applied to this document.

The one finding in §2 does not depend on those judgment calls. It is verifiable directly: grep the
repository for any code that opens a validator report. There is none.
