<!-- Detail for L12. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L12 — Live sessions outlive releases: version the contract, route upgrades to targeted amendments

**Rule.** A plugin's artifact schemas WILL change while faculty sessions are in flight.
Every artifact carries `generated_by` (drafter + skill version) and the session carries a
server-owned `session_contract_version`; validators distinguish **contract upgrades**
(old artifact, new rules) from **quality gaps** (bad artifact); a schema change marks
in-flight artifacts contract-stale and routes faculty to a TARGETED amendment of the
owning step, seeded with proposed fixes — never a full regeneration, never a downstream
stage patching around a doomed upstream artifact. Unknown or missing contract versions
fail closed (treated as current-era, checks armed).

**Failure that taught it.** A live POSED session carried contract version "1.13", which
disarmed every ≥1.29 enforcement check at once; drafters were re-running against
approved-but-now-invalid outlines; reflect couldn't tell upgrade findings from quality
findings (posed_skill.1.28–1.30, F10). L4's stale-state model covers *content* edits;
this covers *schema* evolution — a different axis that bites exactly when the plugin
improves fastest.

**Edu Skill Creator enforcement (L11 + L12).** `edu-skill-creator-architecture` items 5
and 11 require the contract-version fields and a computed-validation plan;
`edu-skill-creator-scaffold` instantiates each planned validator from
`scaffold/reference/validator_template.py` (fail-closed helpers, per-id coverage,
distribution checks, fixture pairs — generated, not just required);
`skill_quality_rubric` critical flag 11 blocks prose-only structural enforcement and
fail-open guards; `edu-skill-creator-test` scenarios 12–14 attack exactly these surfaces.
