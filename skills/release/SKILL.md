---
name: edu-skill-creator-release
description: Edu Skill Creator Stage 7 — Release hygiene for an educational plugin. Runs the release lint (rule 0), verifies changelog heading and lockstep manifest versions, checks trigger descriptions, applies commit conventions, and gates the actual publish (remote push, marketplace) on the author. Triggers - when the edu-skill-creator umbrella dispatches Stage 7, or the user says "release/ship/publish the plugin".
version: "1.4"
---

# Edu Skill Creator Stage 7: Release

Mechanical, ordered, and strict — every step below exists because skipping it once
shipped a defect (see lessons L7, L8).

**Inputs (exact):** the new plugin's repo with `docs/BUILD_PLAN.md`, `reviews/*.json`,
`tests/results.md` + `test_gate_decision.json`, and both plugin manifests. **Refuses to
run** while anything upstream is stale: unchecked BUILD_PLAN items for this release,
any review below 85 or carrying a critical flag, or GREEN passes invalidated by a
later edit. Releasing over stale state is exactly the critical-severity "governance
bypassed" defect the rubric defines. **Outputs:** the release commit/tag, the CHANGELOG
entry, and `release_gate_decision.json` (below).

## Checklist (in order)

1. **Pull, then verify state before commit.** `git pull` first — the other harness may
   have pushed (dual-harness playbook release rule 2). Confirm every BUILD_PLAN item claimed done is
   actually on disk as described — a mid-session abort once produced a bad partial
   commit because edit-then-commit was chained blindly. Spot-read, don't trust memory.
2. **Semantic-drift grep.** For every rule or schema changed this release, grep the
   whole skills tree for the OLD phrasing. New-rule-on-top with stale text below is the
   one drift class the lint cannot catch; the grep is the defense.
3. **Rule 0.** `python3 scripts/release_lint.py` exits 0. If this release added a lint
   check, demonstrate it failing on a seeded violation first (falsifiability, L8).
   Also verify structural validity beyond the drift-lint: both manifests parse and
   carry the fields plugin-dev's plugin-structure conventions require (a lint-clean
   but structurally invalid manifest must not ship).
4. **Version lockstep.** Bump BOTH plugin manifests identically, and every SKILL.md
   frontmatter `version` to the new major.minor (uniform convention, lint-enforced —
   per-skill history belongs in the changelog, not the frontmatter). Changelog gets a
   real
   `## <x>_skill.X.Y — <date>` heading with: what changed, why (which pilot finding or
   review drove it), and what a user of the previous version should do.
5. **Trigger check.** Re-read each skill's frontmatter description against the intent's
   should/should-not-trigger lists; a skill that would fire on the near-misses gets its
   description tightened now (skill-creator's description-optimization step, done
   manually).
6. **Consent-mode disclosure.** If Stage 6 ran lite or skip, the changelog and README
   state it (L6: the recorded `test.consent_mode` is part of the release record —
   consent to skip testing is the educator's to give, but a future maintainer must be
   able to see that it was skipped).
7. **Commit** with trailer `Found-on: claude-code | codex-desktop | codex-cli |
   user-pilot-review`.
8. **Publish gate — author's call.** Creating a remote repo, pushing, or listing on a
   marketplace is an outward action: present exactly what will be published and wait
   for explicit approval. Never push on the author's behalf.

   | Field | Value |
   |---|---|
   | gate_id | `release_gate` |
   | decision | Publish this release to the named remote/marketplace? |
   | artifact | the release commit (diff summary), CHANGELOG entry, consent-mode disclosure |
   | reviewer | the lint run from step 3 — a deliberate substitution: this stage's artifact is mechanical conformance, so the lint is the right reviewer (inspection vs. judgment, Fagan/IEEE 1028; there is no content judgment here to re-derive) |
   | decision_file | `release_gate_decision.json` — `{decision: publish\|hold, remote, version, guidance}` |
   | owns | `edu-skill-creator-release` re-runs steps 1–7 on hold-with-changes |
   | invalidates | publishing freezes this version; later edits start the next release |
   | consent | n/a — the outward action IS the decision |

   After publishing, re-run the lint in publish mode
   (`python3 scripts/release_lint.py --publish`): it verifies the manifests'
   homepage/repository URLs match the actual git remote, and in this mode a claimed
   repo with **no** origin is an error, not the scaffold-time warning (a manifest
   claiming a repo that origin doesn't point to — or that doesn't exist yet — is
   exactly the drift it catches).

## Cross-harness handoff

After the first release, hand the author a short verification checklist for the OTHER
harness's agent (install the plugin, run the lint, dry-run the umbrella skill's Stage 1,
report divergences). Both agents maintaining the plugin — and finding different issues —
is the intended steady state (L7); AGENTS.md carries their standing rules.

## Exit

Tagged release, lint clean, changelog entry, author-approved publish (or an explicit
decision to stay local). Then schedule `edu-skill-creator-reflect` for after the first pilot.
