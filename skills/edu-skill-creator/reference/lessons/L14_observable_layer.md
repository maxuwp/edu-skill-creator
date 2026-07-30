<!-- Detail for L14. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L14 — Check at the layer the claim is about

**Rule.** For every criterion, name the observable layer where the claim lives, and verify at that
layer. Evidence drawn from a proxy layer cannot satisfy the claim unless the mapping from proxy to
target is justified and tested. This is a caveat to L1: grounding is necessary and not sufficient,
because a real framework can describe a different layer than the criterion judges.

**Failures that taught it.** Five observed instances.

An oral-review rubric was correctly grounded, citing the AAC&U Oral Communication VALUE rubric and
Mayer's multimedia principles, both legitimate and properly attributed. It passed a 7,557-word
narration script that was not speech. Neither anchor could catch it: VALUE assesses live student
presentations at the level of delivery and organisation, and Mayer's personalization principle was
operationalized in its source experiments as pronoun substitution. The defects sat at the
lexico-grammatical layer, which neither framework reaches. Zero verbal contractions was one observed
symptom of that, not a universal failure condition.

A module entered its gate with two independent AI approvals and clean validator output and was
rejected by faculty, because required content sat in comments that render as nothing — the pipeline
had been drafting for the validator's audience rather than the room. POSED's own phrasing: the floors
verify what the room sees, never what the file declares. A deck of 41 flattened raster slides with
zero extractable text satisfied a format check. A hash-checked directive ledger was blind to an
omitted approved chart, because its probes were text-only and the omission was an image. And earlier,
a whole renderer was built after nine pilot defects proved invisible at every gate and obvious the
moment the deck rendered, because review ran on markdown source while the faculty's real review unit
was the slide as experienced.

**Fold added 1.15 — the repo checkout is a proxy for the installed harness.** A citation was
repaired to a skill-dir placeholder followed by "/../scaffold/reference/validator_template.py"
(written unbackticked here so lint check 16 does not read a counterexample as a defect) and
verified by resolving it on disk, where it resolved. It resolves only in a git checkout: the
installed layout prefixes every sibling skill (`edu-skill-creator-scaffold`), so the same path
dangles for the agent that actually follows it, which is the only reader that matters. The
verification ran at the authoring layer while the claim lived at the deployment layer, and the
two agree often enough to be trusted and differ exactly where the defect is. The general form:
when a path, name, or identifier is resolved differently by the environment that runs it,
verify against that environment's layout or make the citation layout-independent. Here the fix
was a parameterized placeholder (`<edu-skill-creator-skill-dir:NAME>`) that maps correctly in
all three layouts, plus lint check 16, which rejects `..` traversal outright rather than
resolving it.

**Diagnostic value.** The first diagnosis in the oral case was "the rubric is ungrounded," and
checking the file disproved it. The true diagnosis — grounded in frameworks that do not reach the
layer — is both more accurate and harder to find, which is why the grounding stage should ask the
question mechanically rather than leaving it to notice.

**Enforcement.** `edu-skill-creator-grounding` asks, for every anchor, which observable layer the
framework describes and whether the criterion lives in it; `skill_quality_rubric` critical flag 13
blocks a criterion verified at a proxy layer with no justified mapping. Mechanism examples in
`../implementation_patterns.md` P4.
