#!/usr/bin/env python3
"""Release lint for the Edu Skill Creator repo — run before every push (see MAINTAINING.md).

Checks the drift classes that actually bit POSED/p2d releases (see
skills/edu-skill-creator/reference/lessons_learned.md L7/L8):
  1. Hardcoded ~/.claude / ~/.codex paths in shared skill markdown
     (whitelist: harness_adaptation.md and dual_harness_playbook.md, which
     define/spec the path mappings).
  2. The two plugin manifests (.claude-plugin / .codex-plugin) version-match.
  3. Deprecated repo URLs (none yet — placeholder list).
  4. Rubric dimension points sum to 100 in skills/*/reference/*rubric*.md. Rubrics are
     identified by PATH; an unparseable rubric is an error, not an exemption.
  5. CHANGELOG.md has a real '## edu_skill_creator.X.Y ' heading for the current version
     (line-anchored, code fences stripped).
  6. RETIRED — folded into check 16.
  7. Manifest homepage/repository URLs match the configured git remote: a manifest
     that claims a hosted repo while origin points elsewhere is an error; a claimed
     repo with no origin at all is a warning at scaffold time — pass --publish (as
     edu-skill-creator-release step 8 does after the publish gate) and it becomes an error.
  8. Uniform skill versioning: every skills/*/SKILL.md frontmatter `version` equals
     the plugin manifests' major.minor. Skill versions are bumped together on every
     release, so a stale frontmatter is mechanical drift, not history.
  9. Review evidence is mechanically resolved: every reviews/*_review.json finding
     has status fixed|accepted plus a resolution, and every review file carries a
     resolution_pass block (required whether or not it reports findings — a review
     claiming none must still record that it was resolved).
 11. Every numbered enforcement claim in the lesson index resolves to a real numbered
     item in the skill it names, and every lesson id resolves to an existing detail
     file. Fails closed if the index itself is missing. (There is no check 10; the
     numbering follows the order checks were added.)
 12. Registry completeness: every file in reference/lessons/ is referenced by a PARSED
     index row, so no lesson is unreachable.
 13. The deterministic suite passes, reports its own verdict line, and still carries at
     least MIN_SUITE_CHECKS cases — exit 0 alone was satisfied by a zero-byte file.
 14. Approved artifacts have not drifted since their gate decision (sha256 binding).
 15. Review coherence: no review recommends approval against its own record, and its
     dimension scores sum to the total it reports.
 16. Citation resolution: every backticked path in a skill body resolves, and no skill
     reaches a sibling through '..' (which resolves in a checkout and dangles installed).
 17. The confirm-first review contract: a review log written under the 1.20 contract era
     carries a non-empty `verified` baseline whose entries name a classified mechanism, at
     least one of them strong; findings arrive as `modification` and their `preserve` ids
     resolve. Era-gated on `review_contract_version`, and exemption must be declared.

Three outcomes, not two: error, clean, and UNVERIFIABLE — the check ran and could not
tell. An unverifiable result that authorizes a gate is also an error (fail closed); the
separate name keeps "wrong" distinguishable from "not established" in the record.

Every check has a negative fixture in tests/run_deterministic.py that names the error it
expects. Adding a check without one is adding a green light, not a guard (L8).

Exit 0 = clean (warnings allowed), 1 = errors found.
"""
import hashlib, json, pathlib, re, subprocess, sys

PUBLISH = "--publish" in sys.argv[1:]
ROOT = pathlib.Path(__file__).resolve().parent.parent
# Three outcomes, not two. `_unver` is the third: the check ran, and could not tell. Until
# it existed the lint had error and clean only, so "I could not open the evidence" had
# nowhere to go and was recorded as clean. An unverifiable result that is AUTHORIZING a gate
# is also an error — it fails closed — but it is named separately so the record distinguishes
# "this is wrong" from "this could not be established" (CR 1.20 c21).
errors, warnings, _unver = [], [], []

# Floor for check 13. Raise it when the suite grows; lowering it is a deliberate act that
# must be argued in the changelog, never a side effect of deleting cases.
# Counts FALSIFIABLE case sites (seeded/probe). A dead guard could be neutered by turning
# its case into record(name, bool(1)) — not a literal True, so the constant-verdict test
# missed it — and the total held. record() sites still count toward the reported total.
MIN_SUITE_CHECKS = 113

# 1. Hardcoded harness paths in shared skill bodies
#    Whitelisted by repo-relative PATH, not basename: any file anywhere under skills/ that
#    happened to share one of these names was exempt from the whole check.
WHITELIST = {"skills/edu-skill-creator/reference/harness_adaptation.md",
             "skills/edu-skill-creator/reference/dual_harness_playbook.md"}
for p in (ROOT / "skills").rglob("*.md"):
    if str(p.relative_to(ROOT)) in WHITELIST:
        continue
    for i, line in enumerate(p.read_text().splitlines(), 1):
        if "~/.claude/" in line or "~/.codex/" in line:
            errors.append(f"[path] {p.relative_to(ROOT)}:{i} hardcodes a harness path — "
                          f"use <edu-skill-creator-skill-dir>/… or <skills-dir>/…")

# 2. Manifest versions match
vers = {}
for mp in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
    f = ROOT / mp
    if not f.exists():
        errors.append(f"[manifest] missing {mp}"); continue
    v = json.loads(f.read_text()).get("version")
    if not isinstance(v, str) or not v.strip():
        # fail closed: a None version makes set(vers.values()) size 1 and gates checks 5
        # and 8 off, so deleting one key silenced three checks at once.
        errors.append(f"[manifest] {mp} has no usable string 'version' ({v!r}) — "
                      f"an absent version disarms the version-match, changelog and "
                      f"skill-version checks; a vanished input is a failure, not a skip")
    vers[mp] = v
if len(set(vers.values())) > 1:
    errors.append(f"[manifest] version mismatch: {vers}")
plugin_version = next((v for v in vers.values() if isinstance(v, str) and v.strip()), None)
if plugin_version is None:
    errors.append("[manifest] no readable plugin version in either manifest — checks 5 and 8 "
                  "cannot run; treating the release as unverified")

# 3. Deprecated repo URLs outside the changelog (none at birth; add as they retire)
DEPRECATED = ("maxuwp/page",)  # pre-rename repo; live check, not a placeholder
#    .py included: a deprecated URL in a script was invisible. The two exemptions are
#    FILE-scoped, not directory-scoped — 1.18 excluded all of tests/ to spare the suite's
#    deliberate fixture string and silently dropped coverage of tests/*.md and tests/*.json
#    that 1.17 had.
_DEP_EXEMPT = {pathlib.Path(__file__).resolve(), (ROOT / "tests/run_deterministic.py").resolve()}
for p in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.json")) + list(ROOT.rglob("*.py")):
    rel = p.relative_to(ROOT)
    if (rel.parts[0] in {".git", "node_modules"} or p.name == "CHANGELOG.md"
            or p.resolve() in _DEP_EXEMPT):
        continue
    text = p.read_text(errors="ignore")
    for dep in DEPRECATED:
        if dep in text:
            errors.append(f"[repo] {rel} references deprecated {dep}")

# 4. Rubric dimensions sum to 100 (table style: | n | name | pts | ... ;
#    heading style: '### N. Name — 20 points')
#    A rubric is identified by PATH, never by a phrase in its own prose: keying on
#    "100 points" let an author disarm the arithmetic by rewording the sentence that
#    announced it. Unparseable is an error, not a warning — an unchecked rubric is not
#    an exempt one.
for p in (ROOT / "skills").glob("*/reference/*rubric*.md"):
    text = p.read_text()
    pts = [int(m.group(1)) for m in
           re.finditer(r"^\|\s*\d+\s*\|[^|]+\|\s*(\d+)\s*\|", text, re.M)]
    if not pts:
        pts = [int(m.group(1)) for m in
               re.finditer(r"^###\s+\d+\..*—\s*(\d+)\s*points", text, re.M)]
    if not pts:
        errors.append(f"[rubric] {p.name}: no dimension points parsed — an unparseable "
                      f"rubric is unchecked, not exempt; keep the table or heading shape")
    elif sum(pts) != 100:
        errors.append(f"[rubric] {p.name}: dimensions sum to {sum(pts)}, expected 100")
#    Since the check now trusts a filename, the filename must be enforced: a scored rubric
#    written as reviewer_criteria.md, or parked outside reference/, would carry unverified
#    arithmetic while its author believed the lint covered it.
_rubrics = set((ROOT / "skills").glob("*/reference/*rubric*.md"))
for p in (ROOT / "skills").rglob("*.md"):
    if p in _rubrics:
        continue
    text = p.read_text(errors="ignore")
    if "critical flag" in text and (
            re.search(r"^\|\s*\d+\s*\|[^|]+\|\s*\d+\s*\|", text, re.M)
            or re.search(r"^###\s+\d+\..*—\s*\d+\s*points", text, re.M)):
        errors.append(f"[rubric] {p.relative_to(ROOT)} looks like a scored rubric (points "
                      f"table + critical flags) but sits outside skills/*/reference/*rubric*.md, "
                      f"so check 4 never sees it — rename it into the convention")

# 5. Changelog covers the current plugin version (heading required — a
#    teaser mention like '*next → edu_skill_creator.1.1*' does not count)
if plugin_version:
    major_minor = "edu_skill_creator." + ".".join(plugin_version.split(".")[:2])
    clog = ROOT / "CHANGELOG.md"
    clog_text = clog.read_text() if clog.exists() else ""
    # anchored to line start, with fenced blocks stripped: a substring test was satisfied
    # by the same string quoted inside a ``` example, so a real heading could be renamed
    # away while the check stayed green.
    _prose = re.sub(r"^```.*?^```", "", clog_text, flags=re.M | re.S)
    if not re.search(rf"^##\s+{re.escape(major_minor)}\s", _prose, re.M):
        errors.append(f"[changelog] no '## {major_minor}' entry heading "
                      f"(plugin.json is {plugin_version})")

# 6. RETIRED into check 16. It matched only `reference/<name>.md` inside SKILL.md, warned
#    instead of erroring, and — the reason it missed real defects — retried every failed
#    path against the umbrella's reference/ directory, so a citation written from the wrong
#    skill still "resolved". Check 16 does the same job for every file type, from every
#    skill body, at error level, without the fallback. Numbering is stable on purpose: a
#    renumber would silently invalidate every enforcement claim that cites a check by number
#    (there is no check 10 either).

# 7. Manifest homepage/repository URLs match the git remote
def _norm(url):
    url = re.sub(r"^git@([^:]+):", r"https://\1/", url.strip())
    return re.sub(r"\.git$", "", url).rstrip("/").lower()

claimed = set()
for mp in (".claude-plugin/plugin.json", ".codex-plugin/plugin.json"):
    f = ROOT / mp
    if not f.exists():
        continue
    data = json.loads(f.read_text())
    _here = {_norm(v) for key in ("homepage", "repository")
             for v in [data.get(key)] if isinstance(v, str) and "://" in v}
    if not _here:
        # claiming nothing was the cheapest way to skip the origin comparison entirely
        errors.append(f"[publish] {mp} declares neither 'homepage' nor 'repository' — "
                      f"a manifest that claims no home cannot be compared to git origin")
    claimed |= _here
if claimed:
    r = subprocess.run(["git", "-C", str(ROOT), "remote", "get-url", "origin"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        msg = (f"[publish] manifests claim {sorted(claimed)} but no git remote "
               f"'origin' is configured — fine pre-publish, wrong after")
        (errors if PUBLISH else warnings).append(msg)
    else:
        remote = _norm(r.stdout)
        for c in claimed:
            if c != remote:
                errors.append(f"[publish] manifest URL {c} does not match "
                              f"git origin {remote}")

# 8. Uniform skill versioning: SKILL frontmatter version == plugin major.minor
if plugin_version:
    mm = ".".join(plugin_version.split(".")[:2])
    fm_ver = re.compile(r'^version:\s*"?([0-9.]+)"?\s*$', re.M)
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        head = "\n".join(p.read_text().splitlines()[:12])
        m = fm_ver.search(head)
        if not m:
            # absent was a warning while wrong was an error, so deleting the field from
            # every skill bought a clean lint and dissolved the uniform-version guarantee
            errors.append(f"[skillver] {p.relative_to(ROOT)}: no frontmatter version — "
                          f"an absent version is not an exempt one")
        elif m.group(1) != mm:
            errors.append(f"[skillver] {p.relative_to(ROOT)}: frontmatter version "
                          f"{m.group(1)} != plugin {mm} (uniform convention — bump on release)")

# 9. Review evidence: no status-less findings, no unrecorded resolution pass
#    Every JSON in reviews/ is a review: the old `*_review.json` glob both missed
#    reflect_ledger_rereview.json and let a rename move a file out of enforcement, and a
#    glob with no floor reports clean when the directory is empty.
_revs = sorted((ROOT / "reviews").glob("*.json"))
if not _revs:
    errors.append("[review] reviews/ holds no review JSON — a release with no review evidence "
                  "is unreviewed, not exempt")
#    The population is ENUMERABLE, so enumerate it. A "non-empty" floor still let any single
#    skill ship unreviewed: deleting one review file left the lint clean. L3 says every
#    content stage has an independent reviewer; this is where that becomes evidence.
for _sk in sorted((ROOT / "skills").glob("*/SKILL.md")):
    _m = re.search(r"^name:\s*(\S+)\s*$", "\n".join(_sk.read_text().splitlines()[:12]), re.M)
    if not _m:
        continue   # check 8 owns malformed frontmatter
    if not (ROOT / "reviews" / f"{_m.group(1)}_review.json").exists():
        errors.append(f"[review] no reviews/{_m.group(1)}_review.json for "
                      f"{_sk.relative_to(ROOT)} — an unreviewed skill, not an exempt one")
for p in _revs:
    try:
        data = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"[review] {p.relative_to(ROOT)}: invalid JSON ({e})")
        continue
    findings = data.get("findings") if isinstance(data, dict) else None
    if not isinstance(findings, list):
        # a traceback here printed ZERO findings and skipped checks 11-16 entirely
        errors.append(f"[review] {p.relative_to(ROOT)}: 'findings' is {type(findings).__name__}, "
                      f"not a list — an unreadable finding list is unresolved, not exempt")
        findings = []
    if not isinstance(data, dict) or not isinstance(data.get("resolution_pass"), dict):
        errors.append(f"[review] {p.relative_to(ROOT)}: missing resolution_pass block")
    for i, finding in enumerate(findings, 1):
        if not isinstance(finding, dict):
            errors.append(f"[review] {p.relative_to(ROOT)} finding {i}: "
                          f"{type(finding).__name__}, not an object")
            continue
        status = finding.get("status")
        if status not in {"fixed", "accepted"}:
            errors.append(f"[review] {p.relative_to(ROOT)} finding {i}: "
                          f"status {status!r} is not fixed|accepted")
        resolution = finding.get("resolution")
        if not isinstance(resolution, str) or not resolution.strip():
            errors.append(f"[review] {p.relative_to(ROOT)} finding {i}: "
                          "missing non-empty resolution")

# 11. Every numbered enforcement claim in the lessons quick-reference table resolves
#     (L13: an instructional surface must not promise enforcement the repo lacks; the
#     ledger's own "Enforced at" column is such a surface). Only NUMBERED claims are
#     checkable — that is why the convention is to cite numbered units.
LL = ROOT / "skills" / "edu-skill-creator" / "reference" / "lesson_index.md"
_rows = []          # (lesson id, enforcement claim, detail-file link) — check 12 reads this too
if not LL.exists():
    errors.append("[ledger] lesson_index.md is missing — the enforcement ledger cannot be checked; "
                  "a vanished input is a failure, not a skip")
else:
    def _numbered(path):
        f = ROOT / path
        return ({int(n) for n in re.findall(r"^\s*(\d+)\.\s", f.read_text(), re.M)}
                if f.exists() else set())

    def _lint_checks():
        """Numbered checks in this file, so 'release_lint check N' in the ledger is
        verifiable rather than decorative. The 1.11 ledger claimed enforcement by
        'release_lint check 11' when no such check existed, and the claim survived two
        independent review rounds — prose about code is exactly what code should check."""
        return {int(m.group(1)) for m in
                re.finditer(r"^#\s*(\d+)\.\s+(?!RETIRED)", pathlib.Path(__file__).read_text(), re.M)}
    targets = {
        "release_lint check":   ("scripts/release_lint.py", _lint_checks()),
        "rubric critical flag": ("skills/edu-skill-creator/reference/skill_quality_rubric.md",
                                 _numbered("skills/edu-skill-creator/reference/skill_quality_rubric.md")),
        "test scenario":        ("skills/test/SKILL.md", _numbered("skills/test/SKILL.md")),
        "architecture item":    ("skills/architecture/SKILL.md", _numbered("skills/architecture/SKILL.md")),
        "release step":         ("skills/release/SKILL.md", _numbered("skills/release/SKILL.md")),
        "grounding step":       ("skills/grounding/SKILL.md", _numbered("skills/grounding/SKILL.md")),
        "intent item":          ("skills/intent/SKILL.md", _numbered("skills/intent/SKILL.md")),
        "draft step":           ("skills/draft/SKILL.md", _numbered("skills/draft/SKILL.md")),
    }
    _idx = LL.read_text()
    _rows = re.findall(r"^\| (L\d+) \| [^|]+ \| ([^|]+) \| \[`([^`]+)`\][^|]*\|$", _idx, re.M)
    if not _rows:  # fail closed: a check that silently checks nothing is worse than no check
        errors.append("[ledger] lesson_index.md parsed zero rows — check 11 would pass vacuously")
    for _lid, _claim, _path in _rows:  # f1: dangling lesson detail files
        if not (LL.parent / _path).exists():
            errors.append(f"[ledger] {_lid} points at {_path}, which does not exist")
    #  Claims resolve EVERYWHERE they are written, not only in index rows. Restricting the
    #  resolver to lesson_index.md kept the one audited surface correct while unaudited ones
    #  drifted: four places cited "architecture item 11" for the computed-validation plan
    #  after a 1.11 renumber moved it to 12 - and item 11 exists (lifecycle stages), so
    #  nothing fired and the wrong number reached every generated plugin.
    _claim_sources = [("lesson_index.md " + a, b) for a, b, _ in _rows]
    #  Whole repo, not just skills/: check 16 already learned this scope lesson and a live
    #  "release_lint check 7" claim sits in docs/. tests/ and CHANGELOG.md stay excluded and
    #  the exclusions are load-bearing, not cosmetic — the suite holds deliberate "99"
    #  fixture strings, and the changelog records a pre-renumber "architecture item 11".
    _claim_sources += [(str(f.relative_to(ROOT)), f.read_text(errors="ignore"))
                       for f in sorted(ROOT.rglob("*"))
                       if f.suffix in {".md", ".py"} and ".git" not in f.parts
                       and f.relative_to(ROOT).parts[0] != "tests"
                       and f.name != "CHANGELOG.md"]
    for lesson, claim in _claim_sources:
        for label, (where, present) in targets.items():
            for m in re.finditer(label.replace(" ", r"\s") + r"s?\s+(\d+)(?:\s*[\u2013-]\s*(\d+))?", claim):
                # a range asserts every number it spans: "checks 9-11" claims 10, which does
                # not exist, and endpoint-only checking passed it
                _lo, _hi = int(m.group(1)), int(m.group(2) or m.group(1))
                for n in (range(_lo, _hi + 1) if _hi >= _lo else [_lo, _hi]):
                    if n not in present:
                        errors.append(f"[ledger] {lesson} claims '{label} {n}' but {where} "
                                      f"has no numbered item {n} — L13: the claim or the "
                                      f"enforcement must change, not neither")

# 12. Registry completeness (L7 fold): every lesson detail file appears in the index.
#     Check 11 verifies index->file; this verifies file->index. An orphan lesson is a
#     rule nobody will ever read. This is the check L7's fold previously mis-attributed
#     to check 11, which does something else entirely.
#     Membership is tested against check 11's PARSED row targets, not the index text: a
#     raw substring test counted a filename mentioned in an HTML comment as indexed.
_ldir = ROOT / "skills" / "edu-skill-creator" / "reference" / "lessons"
if not _ldir.is_dir():
    errors.append("[registry] reference/lessons/ is missing — the lesson corpus cannot be "
                  "checked for reachability; a vanished input is a failure, not a skip")
elif not list(_ldir.glob("*.md")):
    errors.append("[registry] reference/lessons/ contains no lesson files — fail closed")
elif _rows:   # a missing/unparseable index is check 11's failure; do not cascade it here
    _linked = {pathlib.PurePosixPath(t).name for _, _, t in _rows}
    for _o in [f.name for f in sorted(_ldir.glob("*.md")) if f.name not in _linked]:
        errors.append(f"[registry] lessons/{_o} exists but no lesson_index.md row references it — "
                      f"an unreachable lesson (L7: every unit appears in the registry that governs it)")

# 13. The deterministic regression suite passes. Every case in it corresponds to a
#     defect that actually shipped; if one stops firing, a guard has gone dead.
_suite = ROOT / "tests" / "run_deterministic.py"
if not _suite.exists():
    errors.append("[tests] tests/run_deterministic.py is missing — the regression suite is the "
                  "only thing proving the other checks still fire; a vanished suite is a failure")
elif "--skip-suite" not in sys.argv[1:]:
    # No re-entrancy guard is needed and none is wanted: every suite case that runs this lint
    # without --skip-suite first stubs the copy's suite, and a stub never invokes the lint.
    # The earlier design ran the real suite there and needed an ESC_LINT_DEPTH env var to
    # terminate, which meant exporting that variable disabled check 13 — suite, count and
    # canary — while the lint still exited 0. An off-switch in the ambient environment is
    # worse than the recursion it prevents.
    _r = subprocess.run([sys.executable, str(_suite)], capture_output=True, text=True)
    if _r.returncode != 0:
        _fails = [l.strip() for l in _r.stdout.splitlines() if l.strip().startswith("FAIL")]
        errors.append(f"[tests] deterministic suite failed: {'; '.join(_fails) or 'see output'}")
    else:
        # exit 0 alone was satisfiable by a zero-byte file. The next cut demanded a verdict
        # line and a count — both printed by the subprocess under test, so a one-line
        # `print("PASS 59/59 …")` satisfied it (L14: that is verification at a proxy layer).
        # So: count the cases in the SOURCE, require the reported number to equal them, and
        # finish with a canary that proves the suite still detects a broken guard.
        _src = _suite.read_text()
        _sites = len(re.findall(r"^(?:seeded|probe|downstream|record)\(", _src, re.M))
        _falsifiable = len(re.findall(r"^(?:seeded|probe|downstream)\(", _src, re.M))
        _const = re.findall(r"^record\([^\n]*?,\s*True\s*[,)]", _src, re.M)
        _m = re.search(r"^PASS\s+(\d+)/(\d+)\s+deterministic checks", _r.stdout, re.M)
        if not _m:
            errors.append("[tests] deterministic suite exited 0 without its 'PASS n/n "
                          "deterministic checks' verdict line — a silent suite is not a "
                          "passing suite")
        elif _falsifiable < MIN_SUITE_CHECKS:
            errors.append(f"[tests] the suite SOURCE contains {_falsifiable} falsifiable case "
                          f"call sites, "
                          f"below the floor of {MIN_SUITE_CHECKS} — cases were removed, not "
                          f"fixed; raise the floor deliberately when the suite shrinks")
        elif int(_m.group(2)) != _sites:
            errors.append(f"[tests] the suite reports {_m.group(2)} cases but its source has "
                          f"{_sites} call sites — the verdict line is not describing this file")
        if _const:
            errors.append(f"[tests] {len(_const)} case(s) assert a literal True "
                          f"({_const[0].strip()[:60]}…) — a case with a constant verdict "
                          f"cannot fail and still occupies a slot in the count")
    # canary: break one guard in a copy and require the suite to notice. This is the only
    # check here made at the right layer — it tests the suite's detection, not its output.
    # It runs whether or not the suite passed: independent evidence that short-circuits on a
    # failing suite is evidence you only get when you already believe the answer.
    if True:
        import shutil, tempfile
        with tempfile.TemporaryDirectory() as _td:
            _c = pathlib.Path(_td) / "canary"
            shutil.copytree(ROOT, _c, ignore=shutil.ignore_patterns(".git"))
            _lp = _c / "scripts" / "release_lint.py"
            _lt = _lp.read_text()
            # line-anchored to the ASSIGNMENT. A plain substring test matched the same text
            # quoted in these two lines, so the canary vouched for its own anchor and the
            # "anchor gone" branch could never fire — the check reading itself as evidence.
            _anchor = re.compile(r'^DEPRECATED = \("maxuwp/page",\)', re.M)
            if not _anchor.search(_lt):
                errors.append("[tests] canary anchor (the DEPRECATED assignment) is gone — "
                              "the canary cannot run, so the suite is unproven")
            else:
                _lp.write_text(_anchor.sub("DEPRECATED = ()", _lt, count=1))
                _cr = subprocess.run([sys.executable, str(_c / "tests/run_deterministic.py"),
                                      "--only", "c3 deprecated URL"],
                                     capture_output=True, text=True)
                if _cr.returncode == 0 or "c3 deprecated URL" not in "".join(
                        l for l in _cr.stdout.splitlines() if l.strip().startswith("FAIL")):
                    errors.append("[tests] canary: check 3 was disabled and the suite still "
                                  "passed (or failed elsewhere) — the suite is not detecting "
                                  "broken guards, whatever its verdict line says")

# 14. Approved artifacts have not drifted since their gate decision. A decision that
#     names its artifact by version string cannot notice the artifact changing; this
#     asks every push, instead of waiting for someone to ask.
_gate = ROOT / "reflect_gate_decision.json"
if not _gate.exists():
    # deleting the approval record was the cheapest way to defeat drift detection
    errors.append("[drift] reflect_gate_decision.json is missing — the approval that binds the "
                  "ledger cannot be checked; a vanished record is a failure, not a skip")
else:
    try:
        _g = json.loads(_gate.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"[drift] reflect_gate_decision.json is unreadable ({e}) — fail closed")
        _g = None
    if _g is not None:
        _b = _g.get("artifact_binding")
        if not isinstance(_b, dict) or not _b.get("sha256"):
            errors.append("[drift] reflect_gate_decision.json records no artifact_binding.sha256 — "
                          "an approval that cannot detect drift in what it approved")
        else:
            _sub = ROOT / _b.get("artifact", "")
            if not _sub.exists():
                errors.append(f"[drift] gate decision binds {_b.get('artifact')!r}, which does not exist")
            else:
                _now = hashlib.sha256(_sub.read_bytes()).hexdigest()
                if _now != _b["sha256"]:
                    errors.append(f"[drift] {_b['artifact']} changed after its gate decision "
                                  f"({_b['sha256'][:12]}… -> {_now[:12]}…). Re-gate the affected rows "
                                  f"or record an amendment; do not silently re-stamp the hash.")

# 15. Review coherence: a review may not recommend approval while its own evidence
#     says otherwise. The sibling POSED audit's most cross-confirmed finding was a
#     review recording total 81 against threshold 85, passed:false, and
#     recommendation:approve simultaneously — the gate tested that a recommendation
#     existed, never that it agreed with the record it signed.
#     Read every field by MEANING, not by one exact spelling: the first cut matched only
#     lowercase "blocking" and rejected string-typed numbers via isinstance, so a review
#     writing severity "Critical", counts.critical, or score "81" sailed through the very
#     check written for it.
APPROVING = {"approve", "approved", "approve-with-acknowledged-majors", "open-the-gate",
             "pass", "passed", "accept", "accepted", "ship", "go"}
BLOCKING_SEV = {"blocking", "blocker", "critical", "fatal"}


def _slug(v):
    return re.sub(r"[\s_]+", "-", str(v).strip().lower()) if v is not None else ""


def _num(v):
    """Numeric value of an int/float or a numeric string; None otherwise. A review that
    records "81" means eighty-one, and a check that silently skips it enforces nothing."""
    if isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return None


_review_files = sorted((ROOT / "reviews").glob("*.json"))
_review_files += [p for p in ROOT.rglob("*review*.json")
                  if ".git" not in p.parts and p not in _review_files]
for _rf in sorted(set(_review_files)):
    try:
        _d = json.loads(_rf.read_text())
    except json.JSONDecodeError:
        continue  # check 9 already reports unreadable review files
    if not isinstance(_d, dict):
        continue
    _rel = _rf.relative_to(ROOT)
    _why = []
    # arithmetic coherence holds whatever the recommendation says
    _sc = _num(_d.get("score") if _d.get("score") is not None else _d.get("total"))
    _ds = _d.get("dimension_scores")
    if isinstance(_ds, (dict, list)) and _sc is not None:
        _vals = _ds.values() if isinstance(_ds, dict) else _ds
        _parts = [_num(v.get("score", v.get("points")) if isinstance(v, dict) else v)
                  for v in _vals]
        if all(p is not None for p in _parts) and _parts and abs(sum(_parts) - _sc) > 1e-6:
            errors.append(f"[coherence] {_rel}: dimension_scores sum to {sum(_parts):g} but "
                          f"score records {_sc:g} — the total must be the sum it reports")
    _rec = _d.get("recommendation") or _d.get("gate_recommendation") or _d.get("verdict")
    if _slug(_rec) not in APPROVING:
        continue
    for _k in ("critical_flags", "criticals", "critical_findings", "blockers"):
        if _d.get(_k):
            _why.append(f"{len(_d[_k])} entry(ies) in {_k}")
    _blk = [f for lst in _d.values() if isinstance(lst, list) for f in lst
            if isinstance(f, dict) and _slug(f.get("severity")) in BLOCKING_SEV]
    if _blk:
        _why.append(f"{len(_blk)} blocking/critical finding(s)")
    _counts = _d.get("counts") if isinstance(_d.get("counts"), dict) else {}
    for _k, _v in _counts.items():
        if _slug(_k) in BLOCKING_SEV and (_num(_v) or 0) > 0:
            _why.append(f"counts.{_k}={_v}")
    _th = _num(_d.get("threshold") if _d.get("threshold") is not None
               else _d.get("pass_threshold"))
    if _sc is not None and _th is not None and _sc < _th:
        _why.append(f"score {_sc:g} below threshold {_th:g}")
    if _slug(_d.get("passed")) in {"false", "no"}:
        _why.append(f"passed:{_d.get('passed')!r}")
    # L11's central gate — "approve is illegal without a recorded computed pass" — was prose
    # in four files and code in none. Inert while no validator exists; live the moment one
    # does, and the generated lint inherits it working rather than as an instruction.
    if any((ROOT / "skills").glob("*/scripts/validate_*.py")):
        _cc = _d.get("computed_checks")
        if not isinstance(_cc, dict) or not _cc:
            _why.append("no computed_checks block while a validator exists")
        elif not any(k.endswith("_validator_pass") for k in _cc):
            # a block of any shape satisfied the gate: recording the report path and
            # renaming or forgetting the pass flag was enough
            _why.append("computed_checks names no '<artifact>_validator_pass' entry while a "
                        "validator exists")
        else:
            _why += [f"computed_checks.{k}={v!r}" for k, v in _cc.items()
                     if k.endswith("_validator_pass") and v is not True]
            # c20: a True pass flag is the reviewing agent's own testimony about its own
            # conduct. Until this clause, nothing opened the report it names, confirmed the
            # file existed, or bound its bytes — level 5 authorizing L11's central gate, in
            # the newest code in the file. The prose promised more than the code delivered:
            # skills/scaffold/SKILL.md and the validator template's header both say the pass
            # flag travels WITH a real report path.
            for _k, _v in sorted(_cc.items()):
                if not _k.endswith("_validator_pass") or _v is not True:
                    continue
                _art = _k[: -len("_validator_pass")]
                _rep = _cc.get(f"{_art}_validator_report")
                _sha = _cc.get(f"{_art}_validator_report_sha256")
                if not isinstance(_rep, str) or not _rep.strip():
                    _unver.append(f"[unverifiable] {_rel}: computed_checks.{_k} is true with no "
                                  f"'{_art}_validator_report' path — the pass is the reviewer's "
                                  f"own testimony and nothing can open what it refers to")
                    _why.append(f"computed_checks.{_k} names no report path")
                    continue
                _rp = ROOT / _rep
                if not _rp.exists():
                    _unver.append(f"[unverifiable] {_rel}: computed_checks.{_art}_validator_report "
                                  f"names {_rep!r}, which does not exist — a missing report is "
                                  f"UNVERIFIABLE, never a pass")
                    _why.append(f"computed_checks.{_art}_validator_report {_rep!r} does not exist")
                    continue
                try:
                    _now = hashlib.sha256(_rp.read_bytes()).hexdigest()
                except OSError as _e:
                    _unver.append(f"[unverifiable] {_rel}: {_rep} is unreadable ({_e}) — "
                                  f"UNVERIFIABLE, never a pass")
                    _why.append(f"computed_checks.{_art}_validator_report is unreadable")
                    continue
                if not isinstance(_sha, str) or not _sha.strip():
                    _why.append(f"computed_checks.{_art}_validator_report is unbound — no "
                                f"'{_art}_validator_report_sha256', so the report may change "
                                f"under the approval that cites it")
                elif _sha.strip().lower() != _now:
                    _why.append(f"computed_checks.{_art}_validator_report changed after the "
                                f"review ({_sha.strip()[:12]}… -> {_now[:12]}…)")
    if _why:
        errors.append(f"[coherence] {_rel} recommends {_rec!r} while its own record shows "
                      f"{', '.join(_why)} — a recommendation must agree with the evidence it signs")

# 16. Citation resolution (the class check behind check 6). Every backticked file path in a
#     skill body or reference file must resolve from the citing file, honouring the
#     placeholder table. Two failure shapes this closes, both shipped:
#       - a relative `<skill-dir>/../scaffold/…`, which resolves in a git checkout and
#         dangles in the installed harness, where the sibling is `edu-skill-creator-scaffold`;
#       - a bare reference/<name>.md written in a file whose own directory has no such file,
#         which check 6 forgave because it silently retried against the umbrella dir.
#     Paths a generated plugin or a build session creates are declared, not guessed.
#     Exact tokens, never prefixes: a `reviews/` prefix exempted every path under it, so
#     a nonexistent file under reviews/ was silently forgiven. Each entry below is a file a
#     BUILD SESSION creates and this repo therefore cannot contain.
GENERATED = {"reviews/architecture_review.json", "reviews/grounding_map_review.json",
             "tests/results.md", "tests/loop_log.md"}
FOREIGN = ("skills/posed/",)          # POSED's repo, cited with its URL alongside
#     A repo-root-relative citation means the repository being worked in (this one while
#     maintaining Edu Skill Creator; the generated plugin's while building one — the layouts
#     are identical because scaffold generates this shape). Declared, not inferred from
#     whatever directories happen to exist.
REPO_DIRS = {"scripts", "tests", "docs", "reviews", "skills"}
#     SCOPE, stated so the check is not read as more than it is: only backticked tokens
#     containing a '/' are path assertions and therefore resolvable. A bare `intent.md` is
#     a name, not a location.
TEMPLATE = re.compile(r"<(?!edu-skill-creator-skill-dir|skills-dir|repo)[^>]*>")
CITE16 = re.compile(r"`([^`\s]*/[A-Za-z0-9_<>:.\-/]*"
                    r"\.(?:md|py|json|mjs|js|ts|sh|ya?ml|txt|html|css|toml|cfg))`")
_cited = 0
#     tests/ is excluded: its fixture strings are deliberately broken citations, which is
#     data under test, not documentation. Everything else in the repo is in scope.
_scan = [p for p in ROOT.rglob("*")
         if p.suffix in {".md", ".py"} and ".git" not in p.parts
         and p.relative_to(ROOT).parts[0] != "tests"
         and p.name != "CHANGELOG.md"]     # the changelog cites paths as they were, not as they are
for p in sorted(_scan):
    rel_p = p.relative_to(ROOT)
    _owner = ROOT / "skills" / rel_p.parts[1] if rel_p.parts[0] == "skills" else ROOT
    for m in CITE16.finditer(p.read_text(errors="ignore")):
        tok = m.group(1)
        if TEMPLATE.search(tok) or tok.startswith(("http", "<skills-dir>")) or "*" in tok:
            continue
        if tok in GENERATED or tok.startswith(FOREIGN):
            continue
        _cited += 1
        sub = re.match(r"<edu-skill-creator-skill-dir:([A-Za-z0-9_\-]+)>/(.*)", tok)
        if sub:
            target = ROOT / "skills" / sub.group(1) / sub.group(2)
        elif tok.startswith("<edu-skill-creator-skill-dir>/"):
            target = ROOT / "skills" / "edu-skill-creator" / tok.split("/", 1)[1]
        elif tok.startswith("<repo>/") or tok.split("/", 1)[0] in REPO_DIRS:
            target = ROOT / tok.replace("<repo>/", "", 1)
        else:
            target = p.parent / tok
        if ".." in tok.split("/"):
            # '..' is legal only while it stays inside the citing skill: crossing OUT of a
            # skill directory resolves in a checkout (siblings are bare names) and dangles
            # installed (siblings are prefixed). The first cut keyed on the placeholder being
            # present, so a plain `../scaffold/…` reopened the defect in eleven characters.
            # PER HOP, not just the destination: a citation of the form ../../skills/NAME/…
            # (unbackticked here so this comment is not itself a citation) leaves the skill
            # directory and comes back, so a destination-only test passed it while the installed
            # layout (where siblings are prefixed) still dangles.
            _owner_r = _owner.resolve()
            _cur, _escaped = pathlib.Path(target.parts[0]), False
            for _seg in target.parts[1:]:
                _cur = _cur.parent if _seg == ".." else _cur / _seg
                if _seg == ".." and _cur != _owner_r and _owner_r not in _cur.parents:
                    _escaped = True
                    break
            try:
                if _escaped:
                    raise ValueError
                target.resolve().relative_to(_owner_r)
            except ValueError:
                errors.append(f"[cite] {rel_p}: `{tok}` traverses out of "
                              f"{_owner.relative_to(ROOT) if _owner != ROOT else 'the repo'} "
                              f"with '..' — the installed layout prefixes sibling skills, so "
                              f"this resolves only in a checkout; use "
                              f"<edu-skill-creator-skill-dir:NAME>/… for a sibling skill, or a "
                              f"repo-root path (scripts/, tests/, docs/, reviews/) for a repo "
                              f"artifact")
                continue
        if not target.exists():
            errors.append(f"[cite] {rel_p}: `{tok}` does not resolve "
                          f"(tried {target.relative_to(ROOT) if ROOT in target.parents else target})")
if _cited < 50:   # the real corpus is far larger; a collapsed count means the extractor
    errors.append(f"[cite] citation extractor matched only {_cited} path(s) — it has stopped "
                  f"seeing the corpus; a resolver with nothing to resolve proves nothing")

# 17. The confirm-first review contract, mechanised (CR 1.20 c1-c5). L19 said a review has two
#     halves and nothing checked it, which is the state every prose-only rule in this repo has
#     drifted from. The review log is JSON this lint already reads, so the contract is checkable.
#     ERA GATE, and it fails CLOSED: exemption requires the log to SAY "pre-1.20". Defaulting a
#     MISSING version to exempt would have made every future log exempt by omission — the
#     fail-open Grok's review named. Historical logs carry the marker explicitly.
REVIEW_ERA = "1.20"
STRONG_KINDS = {"mutation", "command", "diff", "schema"}
VERIFIED_KINDS = STRONG_KINDS | {"human_gate", "other"}


def _era_ge(v, floor):
    """Integer-list comparison, never string comparison: '1.9' < '1.10' is only true if the
    parts are compared as numbers, and the era gate is the thing that decides whether a check
    applies at all."""
    def parts(s):
        return [int(n) for n in re.findall(r"\d+", str(s))]
    return parts(v) >= parts(floor)


for _rf in sorted(set(_review_files)):
    try:
        _d = json.loads(_rf.read_text())
    except json.JSONDecodeError:
        continue                      # check 9 already reports unreadable review files
    if not isinstance(_d, dict):
        continue
    _rel = _rf.relative_to(ROOT)
    _ver = _d.get("review_contract_version")
    if _slug(_ver) == "pre-1.20":
        continue                      # declared pre-era, exempt by its own statement
    if _ver is None:
        errors.append(f"[contract] {_rel}: no review_contract_version. A log written after the "
                      f"{REVIEW_ERA} contract must declare its era; write 'pre-1.20' to claim the "
                      f"exemption explicitly. A missing version is non-compliant, not exempt")
        continue
    if not _era_ge(_ver, REVIEW_ERA):
        continue                      # an older era it declared honestly
    _vf = _d.get("verified")
    if not isinstance(_vf, list) or not _vf:
        errors.append(f"[contract] {_rel}: empty or missing 'verified' — a review that confirmed "
                      f"nothing has not reviewed (L19). An artifact with nothing worth keeping is "
                      f"expressible as verified negative ground, not as an empty array")
        continue
    _ids = set()
    _strong = False
    for _i, _v in enumerate(_vf):
        if not isinstance(_v, dict):
            errors.append(f"[contract] {_rel}: verified[{_i}] is not an object")
            continue
        _ids.add(_v.get("id"))
        _kind = _slug(_v.get("how_verified_kind"))
        if _kind not in VERIFIED_KINDS:
            errors.append(f"[contract] {_rel}: verified[{_i}] how_verified_kind "
                          f"{_v.get('how_verified_kind')!r} is not one of "
                          f"{sorted(VERIFIED_KINDS)} — an unclassified verification cannot be "
                          f"weighed, and this baseline will be defended by the ledger")
        elif _kind in STRONG_KINDS:
            _strong = True
        if not str(_v.get("how_verified") or "").strip():
            errors.append(f"[contract] {_rel}: verified[{_i}] records no how_verified — a "
                          f"property with no mechanism behind it is an assertion")
    if not _strong:
        errors.append(f"[contract] {_rel}: no 'verified' entry of kind {sorted(STRONG_KINDS)} — "
                      f"a baseline made entirely of reading is worse than no baseline, because "
                      f"the ledger will protect it (c16)")
    for _i, _f in enumerate(_d.get("findings") or []):
        if not isinstance(_f, dict):
            continue
        if not str(_f.get("modification") or "").strip():
            errors.append(f"[contract] {_rel}: findings[{_i}] carries no 'modification' — a "
                          f"finding must arrive as the smallest change that fixes it, not as "
                          f"free prose; a revision is a modification, never a new draft (L19)")
        for _p in _f.get("preserve") or []:
            if _p not in _ids:
                errors.append(f"[contract] {_rel}: findings[{_i}].preserve names {_p!r}, which is "
                              f"not a verified id in this file — the do-not-break list must "
                              f"resolve, or it protects nothing")

for w in warnings: print("WARN ", w)
for u in _unver:   print("UNVER", u)
for e in errors:   print("ERROR", e)
print(f"\nrelease_lint: {len(errors)} error(s), {len(warnings)} warning(s), "
      f"{len(_unver)} unverifiable")
sys.exit(1 if errors else 0)
