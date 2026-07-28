<!-- Detail for L7. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L7 — One source of truth; automate drift detection

**Rule.** One repo per plugin serving all harnesses: both plugin manifests version-locked,
shared tool-agnostic SKILL bodies (neutral `<x-skill-dir>/…` placeholders; harness
specifics only in a scoped, whitelisted reference file), personal skill dirs symlinked
into the repo, and a `release_lint.py` run before every push. Lint the drift classes that
actually bit: hardcoded harness paths, manifest version mismatch, deprecated repo URLs,
rubric sums ≠ 100, missing changelog heading, dangling reference citations.

**Failure that taught it.** Four repos (claude/codex × posed/p2d) drifted immediately.
Even after merging, a shared variable containing a literal home-directory harness path
leaked into 17 files — caught by the other harness, then made lintable.

**Corollary — one canonical implementation INSIDE the plugin too.** A formula, constant,
threshold, or key vocabulary that appears in two places will diverge: POSED shipped three
different pacing formulas (drafter script, drafter prose, reviewer inline) and two key
vocabularies for the same corpus-recommendation concept. Rule: one canonical
implementation (a script or a named reference section); every other mention CITES it,
never restates the value; near-miss keys hard-fail with "did you mean" rather than being
silently ignored (posed_skill.1.27/1.30 F7).

**Edu Skill Creator enforcement.** `edu-skill-creator-scaffold` generates this layout from day one, including the
parameterized lint; `dual_harness_playbook.md` is the specification.
