---
name: page-release
description: PAGE Stage 7 — Release hygiene for an educational plugin. Runs the release lint (rule 0), verifies changelog heading and lockstep manifest versions, checks trigger descriptions, applies commit conventions, and gates the actual publish (remote push, marketplace) on the author. Triggers - when the page umbrella dispatches Stage 7, or the user says "release/ship/publish the plugin".
version: "1.0"
---

# PAGE Stage 7: Release

Mechanical, ordered, and strict — every step below exists because skipping it once
shipped a defect (see lessons L7, L8).

## Checklist (in order)

1. **State verification before commit.** Confirm every BUILD_PLAN item claimed done is
   actually on disk as described — a mid-session abort once produced a bad partial
   commit because edit-then-commit was chained blindly. Spot-read, don't trust memory.
2. **Semantic-drift grep.** For every rule or schema changed this release, grep the
   whole skills tree for the OLD phrasing. New-rule-on-top with stale text below is the
   one drift class the lint cannot catch; the grep is the defense.
3. **Rule 0.** `python3 scripts/release_lint.py` exits 0. If this release added a lint
   check, demonstrate it failing on a seeded violation first (falsifiability, L8).
4. **Version lockstep.** Bump BOTH plugin manifests identically. Changelog gets a real
   `## <x>_skill.X.Y — <date>` heading with: what changed, why (which pilot finding or
   review drove it), and what a user of the previous version should do.
5. **Trigger check.** Re-read each skill's frontmatter description against the intent's
   should/should-not-trigger lists; a skill that would fire on the near-misses gets its
   description tightened now (skill-creator's description-optimization step, done
   manually).
6. **Consent-mode disclosure.** If Stage 6 ran lite or skip, the changelog and README
   state it.
7. **Commit** with trailer `Found-on: claude-code | codex-desktop | codex-cli |
   user-pilot-review`.
8. **Publish — author's call.** Creating a remote repo, pushing, or listing on a
   marketplace is an outward action: present exactly what will be published and wait
   for explicit approval. Never push on the author's behalf. After publishing, re-run
   the lint: its publish check verifies the manifests' homepage/repository URLs match
   the actual git remote (a manifest claiming a repo that origin doesn't point to —
   or that doesn't exist yet — is exactly the drift it catches).

## Cross-harness handoff

After the first release, hand the author a short verification checklist for the OTHER
harness's agent (install the plugin, run the lint, dry-run the umbrella skill's Stage 1,
report divergences). Both agents maintaining the plugin — and finding different issues —
is the intended steady state (L7); AGENTS.md carries their standing rules.

## Exit

Tagged release, lint clean, changelog entry, author-approved publish (or an explicit
decision to stay local). Then schedule `page-reflect` for after the first pilot.
