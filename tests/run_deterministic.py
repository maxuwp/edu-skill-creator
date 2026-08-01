#!/usr/bin/env python3
"""Deterministic regression suite. Every case here corresponds to a defect that actually shipped.

Usage: python3 tests/run_deterministic.py       Exit 0 = all pass, 1 = a regression.
Works on a throwaway copy; the real tree is never modified.

EVERY SEEDED CASE NAMES THE ERROR IT EXPECTS. The first cut asserted only "the lint exited
nonzero", and two cases passed for the wrong reason: deleting lesson_index.md also orphans
every lesson file, so check 12's 18 errors satisfied fixtures written for check 11 — both
stayed green with check 11's guard deleted. A fixture that accepts any failure proves the
lint can fail, not that THIS guard fires. `expect_tag` is mandatory for that reason.
"""
import hashlib, json, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "skills/scaffold/reference/validator_template.py"
results = []

# --only <substring> runs just the matching cases. Used by release_lint's canary, which
# needs one case rather than the whole file, and useful when iterating on a single guard.
ONLY = (sys.argv[sys.argv.index("--only") + 1]
        if "--only" in sys.argv and len(sys.argv) > sys.argv.index("--only") + 1 else None)


def record(name, ok, detail=""):
    if ONLY and ONLY not in name:
        return
    results.append((name, ok, detail))


def lint(repo, *args):
    # --skip-suite is mandatory here: lint check 13 runs this suite, so without it the
    # suite would invoke a lint that invokes the suite, forever. Cases that must exercise
    # check 13 itself use lint_full() against a STUB suite, which cannot recurse.
    r = subprocess.run([sys.executable, "scripts/release_lint.py", "--skip-suite", *args],
                       cwd=repo, capture_output=True, text=True)
    return r.returncode, r.stdout


def lint_full(repo, *args):
    # Cases that exercise check 13 run the lint WITHOUT --skip-suite. Every one of them
    # first replaces the copy's suite with a STUB, and a stub never invokes the lint, so the
    # chain terminates in one step with no depth counter and no environment variable.
    r = subprocess.run([sys.executable, "scripts/release_lint.py", *args],
                       cwd=repo, capture_output=True, text=True)
    return r.returncode, r.stdout


def _copy(td):
    repo = pathlib.Path(td) / "r"
    shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns(".git"))
    return repo


def seeded(name, mutate, expect_tag, expect_fail=True, full=False):
    """Copy the repo, mutate it, assert the named guard fires. A check that cannot fail is
    worse than no check (L8); a fixture that cannot say WHICH check failed is worse than
    no fixture, because it reads as coverage."""
    if ONLY and ONLY not in name:
        return
    with tempfile.TemporaryDirectory() as td:
        repo = _copy(td)
        try:
            mutate(repo)
        except Exception as e:
            return record(name, False, f"could not seed: {e!r}")
        if full:
            # 1.17 removed the ESC_LINT_DEPTH counter (an environment-controlled off-switch
            # that silently disabled check 13) and replaced the bound with a convention:
            # every full=True case stubs the copy's suite. A convention nothing checks is not
            # a bound — the first violation hangs the lint forever instead of erroring.
            _s = repo / "tests/run_deterministic.py"
            if _s.exists() and "release_lint.py" in _s.read_text():
                return record(name, False, "full=True case left the copy's suite unstubbed — "
                                           "the nested lint would re-enter this suite forever")
        rc, out = (lint_full if full else lint)(repo)
        if expect_fail:
            if not expect_tag:
                # "" is in every string; a case with a blank tag is a case that names no
                # guard, which is the shape this whole file exists to forbid.
                return record(name, False, "expect_tag is empty — the case names no guard")
            ok = rc != 0 and expect_tag in out
            why = "" if ok else (f"exit {rc}, expected nonzero" if rc == 0 else
                                 f"failed, but not with {expect_tag!r}")
        else:
            ok = rc == 0
            why = "" if ok else f"exit {rc}, expected 0"
        record(name, ok, why)


def _json_edit(repo, rel, fn):
    p = repo / rel
    d = json.loads(p.read_text())
    fn(d)
    p.write_text(json.dumps(d, indent=2))


def _sub(repo, rel, old, new, count=1):
    p = repo / rel
    t = p.read_text()
    if old not in t:
        raise AssertionError(f"anchor {old!r} not present in {rel} — fixture is stale")
    p.write_text(t.replace(old, new, count))


# --------------------------------------------------------------------------------------
# 1-3. paths, manifest versions, deprecated URLs
# --------------------------------------------------------------------------------------
def m_path(r):     _sub(r, "skills/intent/SKILL.md", "\n## ", "\nSee ~/.claude/skills/x\n\n## ")
def m_version(r):  _json_edit(r, ".codex-plugin/plugin.json", lambda d: d.update(version="9.9.9"))
def m_vergone(r):  _json_edit(r, ".claude-plugin/plugin.json", lambda d: d.pop("version"))
def m_deprec(r):   (r / "README.md").write_text((r / "README.md").read_text() + "\nsee maxuwp/page\n")

def m_pathwhitelist(r):
    # the whitelist keyed on BASENAME, so any file under skills/ with one of these two names
    # was exempt from the check entirely
    (r / "skills/test/reference").mkdir(parents=True, exist_ok=True)
    (r / "skills/test/reference/harness_adaptation.md").write_text("See ~/.claude/skills/x\n")
def m_deprecpy(r):
    p = r / "scripts/link_dev_dirs.py"
    p.write_text(p.read_text() + "\n# see https://github.com/maxuwp/page\n")

seeded("c1 hardcoded harness path", m_path, "hardcodes a harness path")
seeded("c1 whitelist evaded by reusing a whitelisted basename", m_pathwhitelist,
       "hardcodes a harness path")
seeded("c2 manifest version mismatch", m_version, "[manifest] version mismatch")
seeded("c2 version key deleted (once silenced c2, c5 and c8 at once)", m_vergone,
       "has no usable string 'version'")
seeded("c3 deprecated URL (was dead code)", m_deprec, "references deprecated")
def m_deprecmd(r):
    # 1.18 excluded all of tests/ to spare the suite's deliberate fixture string, dropping
    # coverage of tests/*.md that 1.17 had
    p = r / "tests/evals/E1_cold_start_execution.md"
    p.write_text(p.read_text() + "\nsee maxuwp/page\n")

seeded("c3 deprecated URL in a .py (scan scope)", m_deprecpy, "references deprecated")
seeded("c3 deprecated URL in tests/*.md (scope regressed in 1.18)", m_deprecmd,
       "references deprecated")

# --------------------------------------------------------------------------------------
# 4. rubric arithmetic — and the reword that used to disarm it
# --------------------------------------------------------------------------------------
RUBRIC = "skills/edu-skill-creator/reference/skill_quality_rubric.md"
def m_rubric(r):   _sub(r, RUBRIC, "| 25 |", "| 40 |")
def m_rubdis(r):
    # the old check keyed on the phrase "100 points" in the rubric's own prose, so an
    # author could turn the arithmetic off by rewording the sentence announcing it
    _sub(r, RUBRIC, "| 25 |", "| 40 |")
    p = r / RUBRIC
    p.write_text(p.read_text().replace("100 points", "one hundred points").replace("/100", " out of 100"))
def m_rubparse(r):
    p = r / RUBRIC
    p.write_text(re.sub(r"^\|\s*(\d+)\s*\|", r"| x\1 |", p.read_text(), flags=re.M))

seeded("c4 rubric dimensions sum", m_rubric, "dimensions sum to")
seeded("c4 rubric reworded to dodge the check", m_rubdis, "dimensions sum to")
def m_rubelsewhere(r):
    # check 4 identifies rubrics by path, so a scored rubric named outside the convention
    # is invisible to it — the instruction that once taught otherwise sent authors here
    (r / "skills/draft/reference").mkdir(parents=True, exist_ok=True)
    (r / "skills/draft/reference/reviewer_criteria.md").write_text(
        "# Criteria\n\n| # | Dimension | Points |\n|---|---|---|\n| 1 | Grounding | 40 |\n"
        "| 2 | Structure | 50 |\n\nA critical flag blocks approval.\n")

seeded("c4 unparseable rubric (was a warning)", m_rubparse, "no dimension points parsed")
def m_rubheading(r):
    # check 4 parses heading-style rubrics, so the misplacement detector must recognise them
    (r / "skills/draft/reference").mkdir(parents=True, exist_ok=True)
    (r / "skills/draft/reference/reviewer_criteria.md").write_text(
        "# Criteria\n\n### 1. Grounding — 40 points\n\n### 2. Structure — 50 points\n\n"
        "A critical flag blocks approval.\n")

seeded("c4 scored rubric named outside the convention (invisible to the check)",
       m_rubelsewhere, "sits outside skills/*/reference/*rubric*.md")
seeded("c4 heading-style rubric outside the convention", m_rubheading,
       "sits outside skills/*/reference/*rubric*.md")

# --------------------------------------------------------------------------------------
# 5. changelog heading — version-derived, never pinned
# --------------------------------------------------------------------------------------
def _mm(r):
    return ".".join(json.loads((r / ".claude-plugin/plugin.json").read_text())["version"].split(".")[:2])
def m_chlog(r):
    # version-derived, never hardcoded: a suite that pins a release number goes stale the
    # moment the release does, and reports a false failure instead of a real one.
    _sub(r, "CHANGELOG.md", f"## edu_skill_creator.{_mm(r)}", f"## old.{_mm(r)}")
def m_chfence(r):
    # a bare substring test was satisfied by the same heading quoted inside a code fence
    v = _mm(r)
    _sub(r, "CHANGELOG.md", f"## edu_skill_creator.{v}", f"## old.{v}")
    p = r / "CHANGELOG.md"
    p.write_text(p.read_text() + f"\n```\n## edu_skill_creator.{v} — example heading\n```\n")

seeded("c5 changelog heading", m_chlog, "[changelog] no '##")
seeded("c5 heading faked inside a code fence", m_chfence, "[changelog] no '##")

# --------------------------------------------------------------------------------------
# 7. manifest URL vs git origin
# --------------------------------------------------------------------------------------
def m_url(r):
    # the copy has no .git, so check 7 would take its no-origin WARNING branch and prove
    # nothing. Give it a real origin, then mismatch the manifest against it.
    for cmd in (["git", "init", "-q"], ["git", "remote", "add", "origin",
                                        "https://github.com/maxuwp/edu-skill-creator.git"]):
        subprocess.run(cmd, cwd=r, capture_output=True)
    _json_edit(r, ".claude-plugin/plugin.json",
               lambda d: d.update(homepage="https://github.com/maxuwp/WRONG"))
def m_nourl(r):
    _json_edit(r, ".claude-plugin/plugin.json",
               lambda d: [d.pop(k, None) for k in ("homepage", "repository")])

seeded("c7 manifest URL vs origin", m_url, "does not match git origin")
seeded("c7 manifest claims no home at all (was a free skip)", m_nourl,
       "declares neither 'homepage' nor 'repository'")

# --------------------------------------------------------------------------------------
# 8. uniform skill versioning
# --------------------------------------------------------------------------------------
def m_skillver(r):
    # version-derived, never pinned: a fixture that hardcodes a release number breaks on
    # the next bump and reports a false failure. This is the second time.
    p = r / "skills/intent/SKILL.md"
    p.write_text(re.sub(r'^version: "[0-9.]+"$', 'version: "0.1"', p.read_text(), count=1, flags=re.M))
def m_skillnover(r):
    p = r / "skills/intent/SKILL.md"
    p.write_text(re.sub(r'^version: "[0-9.]+"\n', "", p.read_text(), count=1, flags=re.M))

seeded("c8 uniform skill version", m_skillver, "!= plugin")
seeded("c8 version field deleted (was a warning)", m_skillnover, "no frontmatter version")

# --------------------------------------------------------------------------------------
# 9. review evidence — including the empty directory and the rename evasion
# --------------------------------------------------------------------------------------
REV = "reviews/edu-skill-creator-draft_review.json"
def m_revpass(r):  _json_edit(r, REV, lambda d: (d.update(findings=[]), d.pop("resolution_pass", None)))
def m_revstat(r):  _json_edit(r, REV, lambda d: d["findings"][0].pop("status"))
def m_revres(r):   _json_edit(r, REV, lambda d: d["findings"][0].update(resolution="  "))
def m_revgone(r):  [p.unlink() for p in (r / "reviews").glob("*.json")]
def m_revrename(r):
    # the old *_review.json glob let a rename move a file out of enforcement entirely
    p = r / REV
    _json_edit(r, REV, lambda d: d.pop("resolution_pass", None))
    p.rename(r / "reviews/edu-skill-creator-draft.review.json")

seeded("c9 review without resolution_pass (was bypassable)", m_revpass, "missing resolution_pass block")
seeded("c9 finding with no status", m_revstat, "is not fixed|accepted")
seeded("c9 finding with an empty resolution", m_revres, "missing non-empty resolution")
def m_revoneskill(r):
    # a "non-empty" floor still let ONE skill ship unreviewed
    (r / "reviews/edu-skill-creator-scaffold_review.json").unlink()

seeded("c9 reviews/ emptied (a glob with no floor reads clean)", m_revgone, "holds no review JSON")
def m_revmalformed(r):
    # a non-list findings value crashed the lint: zero findings printed, checks 11-16 skipped
    _json_edit(r, REV, lambda d: d.update(findings={"a": 1}))

seeded("c9 one skill's review deleted (floor was population-blind)", m_revoneskill,
       "no reviews/edu-skill-creator-scaffold_review.json")
seeded("c9 malformed findings value (was a traceback, not a finding)", m_revmalformed,
       "not a list — an unreadable finding list is unresolved")
seeded("c9 review renamed out of the old glob", m_revrename, "missing resolution_pass block")

# --------------------------------------------------------------------------------------
# 11/12. lesson index and registry — each branch, each with its own tag
# --------------------------------------------------------------------------------------
IDX = "skills/edu-skill-creator/reference/lesson_index.md"
LDIR = "skills/edu-skill-creator/reference/lessons"
def m_claim(r):    _sub(r, IDX, "rubric critical flag 13", "rubric critical flag 99")
def m_idxgone(r):  (r / IDX).unlink()
def m_idxrows(r):  (r / IDX).write_text("# Lesson index\n\nno table here\n")
def m_dangle(r):   _sub(r, IDX, "L01_grounding.md", "L01_GONE.md")
def m_orphan(r):   shutil.copy(r / LDIR / "L01_grounding.md", r / LDIR / "L99_orphan.md")
def m_orphancomment(r):
    # membership was a raw substring test over the index, so naming the file in an HTML
    # comment counted as indexed while no row linked it
    m_orphan(r)
    p = r / IDX
    p.write_text(p.read_text() + "\n<!-- TODO: write the row for L99_orphan.md later -->\n")
def m_lintclaim(r): _sub(r, IDX, "release_lint check 13", "release_lint check 99")
def m_ldirgone(r): shutil.rmtree(r / LDIR)
def m_ldirempty(r):
    for f in (r / LDIR).glob("*.md"):
        f.unlink()

seeded("c11 unresolvable enforcement claim", m_claim, "has no numbered item")
seeded("c11 index deleted (fixture once proved c12 instead)", m_idxgone,
       "[ledger] lesson_index.md is missing")
seeded("c11 index parses zero rows", m_idxrows, "parsed zero rows")
seeded("c11 dangling lesson path (fixture once proved c12 instead)", m_dangle,
       "[ledger] L1 points at")
def m_claimbody(r):
    # claims drifted in SKILL bodies for four releases because only index rows were resolved
    _sub(r, "skills/scaffold/SKILL.md", "architecture item 12 computed-validation plan",
         "architecture item 99 computed-validation plan")

seeded("c11 unresolvable release_lint check claim", m_lintclaim,
       "claims 'release_lint check 99'")
def m_claimoutside(r):
    p = r / "docs/BUILD_PLAN.md"
    p.write_text(p.read_text() + "\n\nEnforced at release_lint check 99.\n")
def m_claimrange(r):
    _sub(r, "skills/scaffold/SKILL.md", "## The lint (rule 0)",
         "## The lint (rule 0)\n\nSee release_lint checks 9-11.")

seeded("c11 stale numbered claim in a SKILL body, not an index row", m_claimbody,
       "skills/scaffold/SKILL.md claims 'architecture item 99'")
seeded("c11 claim outside skills/ (scan scope)", m_claimoutside,
       "docs/BUILD_PLAN.md claims 'release_lint check 99'")
seeded("c11 range claim spanning a number that does not exist", m_claimrange,
       "claims 'release_lint check 10'")
seeded("c12 orphan lesson file", m_orphan, "no lesson_index.md row references it")
seeded("c12 orphan named only in an HTML comment", m_orphancomment,
       "no lesson_index.md row references it")
seeded("c12 lessons/ directory deleted", m_ldirgone, "[registry] reference/lessons/ is missing")
seeded("c12 lessons/ emptied", m_ldirempty, "contains no lesson files")

# --------------------------------------------------------------------------------------
# 13. the suite check itself. Seeded with STUB suites, so nothing recurses.
# --------------------------------------------------------------------------------------
SUITE = "tests/run_deterministic.py"
def _stub(r, body):  (r / SUITE).write_text(body)
def m_suitegone(r):  (r / SUITE).unlink()
def m_suitefail(r):  _stub(r, "import sys\nprint('FAIL something')\nsys.exit(1)\n")
def m_suitemute(r):  _stub(r, "")                       # zero bytes, exit 0
def m_suitefloor(r): _stub(r, "print('PASS 3/3 deterministic checks')\n")

def m_suitecount(r):
    # a verdict line that does not describe this file: many case sites, 5 claimed.
    # Padding is seeded(, not record(, so it clears the FALSIFIABLE floor and the case lands
    # on the count-mismatch branch rather than the floor branch.
    _stub(r, 'print("PASS 5/5 deterministic checks")\nraise SystemExit(0)\n'
             + "seeded('x', None, 'tag')\n" * (MIN_FLOOR + 5))
def m_suiteconst(r):
    _stub(r, f'print("PASS {MIN_FLOOR + 5}/{MIN_FLOOR + 5} deterministic checks")\n'
             'raise SystemExit(0)\n' + "seeded('x', None, 'tag')\n" * (MIN_FLOOR + 4)
             + 'record("x", True)\n')
def _passing_stub(n):
    """A suite that reports a full, correctly-counted PASS and detects nothing. Every
    check-13 fixture uses a STUB: a stub never invokes the lint, so lint -> suite -> lint
    cannot recur and no depth counter is needed. The earlier design ran the real suite here
    and needed an ESC_LINT_DEPTH env var to terminate — which let anyone disable check 13
    by exporting that variable. A guard whose off-switch lives in the ambient environment is
    not a guard; deleting the surface beats guarding it."""
    return (f'print("PASS {n}/{n} deterministic checks")\n'
            'raise SystemExit(0)\n' + "seeded('case', None, 'tag')\n" * n)
def m_canaryblind(r):
    # a suite that always says PASS: the shape a self-reported count cannot see
    _stub(r, _passing_stub(MIN_FLOOR))
def m_canaryanchor(r):
    _stub(r, _passing_stub(MIN_FLOOR))
    _sub(r, "scripts/release_lint.py", 'DEPRECATED = ("maxuwp/page",)',
         'DEPRECATED = ("maxuwp/page", )')

MIN_FLOOR = int(re.search(r"^MIN_SUITE_CHECKS = (\d+)",
                          (ROOT / "scripts/release_lint.py").read_text(), re.M).group(1))

seeded("c13 suite missing", m_suitegone, "[tests] tests/run_deterministic.py is missing", full=True)
seeded("c13 suite fails (was proven only by hand)", m_suitefail,
       "[tests] deterministic suite failed", full=True)
seeded("c13 zero-byte suite exits 0 and proves nothing", m_suitemute, "verdict line", full=True)
seeded("c13 suite shrunk below its floor", m_suitefloor, "below the floor of", full=True)
seeded("c13 verdict line does not describe the file it came from", m_suitecount,
       "call sites — the verdict line is not describing this file", full=True)
seeded("c13 cases with a constant verdict", m_suiteconst, "assert a literal True", full=True)
seeded("c13 canary: suite stops detecting a disabled guard", m_canaryblind,
       "the suite is not detecting broken guards", full=True)
def m_suitepad(r):
    # one falsifiable case replaced by a non-literal constant and the TOTAL padded back to
    # the floor. The old floor counted record() sites too, so a guard could go dead while
    # the number held; `bool(1)` is not a literal True, so the constant-verdict test missed
    # it. Stubbed like every other check-13 fixture, per the bound in seeded().
    _stub(r, f'print("PASS {MIN_FLOOR}/{MIN_FLOOR} deterministic checks")\n'
             "raise SystemExit(0)\n"
             + "seeded('case', None, 'tag')\n" * (MIN_FLOOR - 1)
             + 'record("c1 hardcoded harness path", bool(1))\n')

seeded("c13 canary anchor removed (canary cannot run)", m_canaryanchor,
       "canary anchor", full=True)
seeded("c13 a guard neutered and its case padded back to the total", m_suitepad,
       "falsifiable case call sites", full=True)

# --------------------------------------------------------------------------------------
# 14. post-approval drift
# --------------------------------------------------------------------------------------
def m_drift(r):    _sub(r, "reflect_ledger.json", '"prepared_by"', '"prepared_by_"')
def m_gategone(r): (r / "reflect_gate_decision.json").unlink()
def m_nosha(r):    _json_edit(r, "reflect_gate_decision.json",
                              lambda d: d.get("artifact_binding", {}).pop("sha256", None))

seeded("c14 ledger drift after gate", m_drift, "changed after its gate decision")
seeded("c14 gate decision deleted (was a free skip)", m_gategone,
       "[drift] reflect_gate_decision.json is missing")
seeded("c14 binding with no sha256", m_nosha, "records no artifact_binding.sha256")

# --------------------------------------------------------------------------------------
# 15. review coherence — one case per clause, plus the spellings the first cut missed
# --------------------------------------------------------------------------------------
def _incoh(**kv):
    def m(r):
        _json_edit(r, REV, lambda d: d.update(**kv))
    return m

seeded("c15 approve with a critical flag", _incoh(critical_flags=["seeded"]),
       "entry(ies) in critical_flags")
seeded("c15 approve with a blocking finding", _incoh(
    findings=[{"severity": "blocking", "status": "fixed", "resolution": "x"}]),
    "blocking/critical finding(s)")
seeded("c15 severity spelled 'Critical' (case once evaded it)", _incoh(
    findings=[{"severity": "Critical", "status": "fixed", "resolution": "x"}]),
    "blocking/critical finding(s)")
seeded("c15 counts.critical, not counts.blocking", _incoh(counts={"critical": 2}),
       "counts.critical")
seeded("c15 score below threshold", _incoh(score=81, threshold=85, dimension_scores={"a": 81}),
       "below threshold")
seeded("c15 score/threshold as strings (isinstance once skipped them)",
       _incoh(score="81", threshold="85", dimension_scores={"a": "81"}), "below threshold")
seeded("c15 passed false as a string", _incoh(passed="false"), "passed:")
seeded("c15 dimension scores that do not sum to the reported total",
       _incoh(score=95, dimension_scores={"a": 40, "b": 40}), "dimension_scores sum to")
seeded("c15 dimension scores as a list (shape, not meaning)",
       _incoh(score=95, dimension_scores=[40, 40]), "dimension_scores sum to")
def m_nocomputed(r):
    # L11's gate: with a validator present, approval without a recorded computed pass is
    # incoherent. Was prose in four files and code in none.
    (r / "skills/test/scripts").mkdir(parents=True, exist_ok=True)
    (r / "skills/test/scripts/validate_thing.py").write_text("# generated validator\n")
def m_computedfalse(r):
    m_nocomputed(r)
    _json_edit(r, REV, lambda d: d.update(computed_checks={"thing_validator_pass": False}))

seeded("c15 approve with no computed_checks while a validator exists", m_nocomputed,
       "no computed_checks block while a validator exists")
def m_computedkey(r):
    # recording the report path and renaming or forgetting the pass flag satisfied the gate
    m_nocomputed(r)
    _json_edit(r, REV, lambda d: d.update(
        computed_checks={"thing_validator_report": "reviews/thing_validation.json"}))

seeded("c15 approve with a failing computed check", m_computedfalse,
       "computed_checks.thing_validator_pass=False")
seeded("c15 computed_checks block with no _validator_pass key", m_computedkey,
       "names no '<artifact>_validator_pass' entry")

# c20: a true pass flag is the reviewer's testimony about its own conduct. Each case below
# is one way that testimony was accepted with nothing behind it. Every one of them passed
# the lint before this clause existed.
#   The report lives OUTSIDE reviews/ on purpose: check 9 enumerates reviews/*.json as
#   review logs and check 15 rglobs *review*.json, so a validator report parked among them
#   would be linted as a review and the fixture would fail for a reason it never meant.
RPT = "docs/thing_validation.json"
RPT_BODY = b'{"passed": true}\n'
RPT_SHA = hashlib.sha256(RPT_BODY).hexdigest()

def _cc(r, **kv):
    m_nocomputed(r)
    _json_edit(r, REV, lambda d: d.update(computed_checks=kv))
def _report(r):
    (r / RPT).write_bytes(RPT_BODY)

def m_ccnopath(r):
    _cc(r, thing_validator_pass=True)
def m_ccghost(r):
    _cc(r, thing_validator_pass=True, thing_validator_report=RPT)   # never written
def m_ccunbound(r):
    _report(r)
    _cc(r, thing_validator_pass=True, thing_validator_report=RPT)
def m_ccdrift(r):
    _report(r)
    _cc(r, thing_validator_pass=True, thing_validator_report=RPT,
        thing_validator_report_sha256="0" * 64)

seeded("c20 pass flag true with no report path", m_ccnopath,
       "names no report path")
seeded("c20 report path naming a file that does not exist", m_ccghost,
       "a missing report is UNVERIFIABLE")
seeded("c20 report exists but its bytes are not bound", m_ccunbound,
       "is unbound")
seeded("c20 report changed after the review that cited it", m_ccdrift,
       "changed after the review")

def m_ccbound(r):
    # The positive control. Without it the four cases above prove only that the clause can
    # FAIL, never that it can pass — a guard nothing can satisfy is as dead as a guard
    # nothing can trip, and it would be satisfied here by a clause that rejected everything.
    # Every approving review needs the block, not just one: the moment a validator exists,
    # L11's gate applies to all of them, which is the contract, not a fixture artefact.
    _report(r)
    m_nocomputed(r)
    for p in sorted((r / "reviews").glob("*.json")):
        _json_edit(r, f"reviews/{p.name}", lambda d: d.update(computed_checks={
            "thing_validator_pass": True,
            "thing_validator_report": RPT,
            "thing_validator_report_sha256": RPT_SHA}))
seeded("c20 fully bound computed pass is accepted", m_ccbound, "", expect_fail=False)

# --------------------------------------------------------------------------------------
# 17. the confirm-first contract (CR 1.20 c1-c5). Every case starts from a COMPLIANT
#     1.20 log and removes exactly one thing, so each case names the guard it proves
#     rather than passing because the log was malformed in some other way.
# --------------------------------------------------------------------------------------
def _era(d, **over):
    d.update(review_contract_version="1.20",
             verified=[{"id": "v1", "property": "check 3 scans .py files",
                        "how_verified": "deleted the guard on a copy; c3 case failed",
                        "how_verified_kind": "mutation",
                        "location": "scripts/release_lint.py:109"}])
    for f in d.get("findings") or []:
        f["modification"] = "narrow the exemption to the one file that needs it"
    d.update(**over)
def m_eraok(r):     _json_edit(r, REV, lambda d: _era(d))
def m_eranover(r):  _json_edit(r, REV, lambda d: (_era(d), d.pop("review_contract_version")))
def m_eraempty(r):  _json_edit(r, REV, lambda d: _era(d, verified=[]))
def m_erakind(r):
    _json_edit(r, REV, lambda d: (_era(d), d["verified"][0].update(how_verified_kind="vibes")))
def m_eraweak(r):
    _json_edit(r, REV, lambda d: (_era(d), d["verified"][0].update(how_verified_kind="other")))
def m_erahow(r):
    _json_edit(r, REV, lambda d: (_era(d), d["verified"][0].update(how_verified="  ")))
def m_eramod(r):
    _json_edit(r, REV, lambda d: (_era(d), d["findings"][0].pop("modification")))
def m_erapres(r):
    _json_edit(r, REV, lambda d: (_era(d), d["findings"][0].update(preserve=["v99"])))

seeded("c17 log written after the era with no contract version", m_eranover,
       "no review_contract_version")
seeded("c17 approve with an empty verified baseline", m_eraempty,
       "empty or missing 'verified'")
seeded("c17 how_verified_kind outside the closed set", m_erakind,
       "is not one of")
seeded("c17 baseline verified only by reading (no strong kind)", m_eraweak,
       "no 'verified' entry of kind")
seeded("c17 verified property with no mechanism recorded", m_erahow,
       "records no how_verified")
seeded("c17 finding with no modification (free prose fix retired)", m_eramod,
       "carries no 'modification'")
seeded("c17 preserve id that resolves to nothing", m_erapres,
       "not a verified id in this file")
seeded("c17 a compliant 1.20 log is accepted", m_eraok, "", expect_fail=False)
def m_eraprefix(r):
    # the era gate itself: a log that declares the pre-era exemption is exempt, and the
    # exemption must be DECLARED — a missing version is non-compliant, not exempt (c5).
    _json_edit(r, REV, lambda d: d.update(review_contract_version="pre-1.20", verified=[]))
seeded("c17 declared pre-era log stays exempt", m_eraprefix, "", expect_fail=False)

# --------------------------------------------------------------------------------------
# 16. citation resolution — the class check behind "reference not landing"
# --------------------------------------------------------------------------------------
def m_citebad(r):
    p = r / "skills/test/SKILL.md"
    p.write_text(p.read_text() + "\n\nSee `reference/nope/missing.md`.\n")
def m_citedots(r):
    _sub(r, "skills/architecture/SKILL.md",
         "`<edu-skill-creator-skill-dir:scaffold>/reference/validator_template.py`",
         "`<edu-skill-creator-skill-dir>/../scaffold/reference/validator_template.py`")
def m_citeplain(r):
    # the placeholder-free form: the first cut required the placeholder to be present, so
    # deleting eleven characters reopened the whole defect
    p = r / "skills/test/SKILL.md"
    p.write_text(p.read_text() + "\n\nSee `../scaffold/reference/validator_template.py`.\n")
def m_citeext(r):
    # the extension whitelist once stopped at .md/.py/.json/.mjs
    p = r / "skills/test/SKILL.md"
    p.write_text(p.read_text() + "\n\nRun `reference/ghost_helper.sh`.\n")
def m_citeoutside(r):
    # only skills/ was scanned; a repo-root doc could cite anything
    p = r / "MAINTAINING.md"
    p.write_text(p.read_text() + "\n\nSee `docs/never_written.md`.\n")
def m_citegen(r):
    # GENERATED was a prefix list, so everything under reviews/ was exempt wholesale
    p = r / "skills/test/SKILL.md"
    p.write_text(p.read_text() + "\n\nSee `reviews/not_a_real_review.json`.\n")
def m_citeblind(r):
    p = r / "scripts/release_lint.py"
    src = p.read_text()
    out = re.sub(r"^CITE16 = re\.compile\((?:.|\n)*?\)\n",
                 'CITE16 = re.compile(r"`(NEVER_MATCHES_ANYTHING)`")\n', src, count=1, flags=re.M)
    if out == src:
        raise AssertionError("CITE16 assignment not found — fixture is stale")
    p.write_text(out)

seeded("c16 citation that does not resolve", m_citebad, "does not resolve")
seeded("c16 sibling cited through '..' with the placeholder", m_citedots, "traverses out of")
def m_citereturn(r):
    # leaves the skill directory and comes back: a destination-only test passed it, while the
    # installed layout (siblings prefixed) still dangles
    p = r / "skills/test/SKILL.md"
    p.write_text(p.read_text() + "\n\nSee `../../skills/scaffold/SKILL.md`.\n")

seeded("c16 sibling cited through a bare '..' (no placeholder to key on)", m_citeplain,
       "traverses out of")
seeded("c16 '..' that leaves the skill and returns", m_citereturn, "traverses out of")
seeded("c16 non-whitelisted extension", m_citeext, "does not resolve")
seeded("c16 citation outside skills/ (scan scope)", m_citeoutside, "does not resolve")
seeded("c16 nonexistent file under a generated-artifact prefix", m_citegen, "does not resolve")
seeded("c16 extractor blinded (a resolver with nothing to resolve)", m_citeblind, "matched only")

# --------------------------------------------------------------------------------------
# the clean tree still passes — the control that keeps every case above honest
# --------------------------------------------------------------------------------------
seeded("lint clean on an unmodified tree", lambda r: None, "", expect_fail=False)

# --------------------------------------------------------------------------------------
# validator template: the contract every generated plugin inherits
# --------------------------------------------------------------------------------------
PASS_MANIFEST = {"session_contract_version": "toy.1.0",
                 "artifacts": {"ARTIFACT": {"generated_by": "drafter.1.0", "reviewed": False},
                               "upstream": {"generated_by": "planner.1.0", "items": ["a1", "a2"]}}}
PASS_ARTIFACT = {"items": [{"id": "i1", "upstream_ref": "a1", "text": "one"},
                           {"id": "i2", "upstream_ref": "a2", "text": "two"}]}


def probe(name, setup, argv, expect, source=None, names_check=None, issue=None):
    """An exit-1 probe MUST name the finding it expects. `s_ok` alone produces five
    criticals from three guards, so exit 1 was over-determined: one probe stayed green with
    its named guard deleted — the same passing-for-the-wrong-reason shape seeded() forbids.
    `issue` narrows further, to a substring of the finding text, when one check can fail in
    several ways."""
    if ONLY and ONLY not in name:
        return
    if expect == 1 and not names_check:
        return record(name, False, "exit-1 probe with no names_check — names no guard")
    with tempfile.TemporaryDirectory() as td:
        d = pathlib.Path(td)
        (d / "v.py").write_text(source if source else TEMPLATE.read_text())
        try:
            setup(d)
        except Exception as e:
            return record(name, False, f"setup failed: {e!r}")
        r = subprocess.run([sys.executable, "v.py", *argv], cwd=d, capture_output=True, text=True)
        ok = r.returncode == expect and "Traceback" not in r.stderr
        why = "" if ok else f"exit {r.returncode} (want {expect})" + \
                            (" TRACEBACK" if "Traceback" in r.stderr else "")
        if ok and names_check:
            rep = json.loads((d / "s/review_logs/ARTIFACT_validation.json").read_text())
            hits = [f for f in rep["findings"] if f["check"] == names_check
                    and (issue is None or issue in f["issue"])]
            ok = bool(hits)
            why = "" if ok else f"report never names {names_check}" + \
                                (f" with issue ~{issue!r}" if issue else "")
        record(name, ok, why)


def s_none(d):  (d / "s").mkdir()
def s_list(d):  (d / "s").mkdir(); (d / "s/manifest.json").write_text("[1,2,3]")
def s_ok(d):    (d / "s").mkdir(); (d / "s/manifest.json").write_text('{"artifacts":{}}')
def s_blk(d):   s_ok(d); (d / "s/blocker").write_text("x")


def s_pass(d, artifact=None, manifest=None):
    (d / "s").mkdir()
    (d / "s/manifest.json").write_text(json.dumps(manifest or PASS_MANIFEST))
    (d / "s/ARTIFACT.json").write_text(json.dumps(artifact or PASS_ARTIFACT, indent=1))


probe("template exit 2 on missing manifest", s_none, ["s"], 2)
probe("template exit 2 on non-object manifest (was a crash)", s_list, ["s"], 2)
probe("template exit 2 on unwritable report dir (was a crash)", s_blk,
      ["s", "--report", "s/blocker/x/r.json"], 2)
probe("template exit 2 on --report with no path (was a crash)", s_ok, ["s", "--report"], 2)

# the fail-closed helpers, each proven by the finding it alone produces. All three were
# claimed "actually exercised" while only require_bool had a probe that could fail.
probe("template require_record fires on a missing manifest record", s_ok, ["s"], 1,
      names_check="check_required_structure", issue="record missing")
probe("template require_file fires on a missing artifact file",
      lambda d: (d / "s").mkdir() or (d / "s/manifest.json").write_text(json.dumps(PASS_MANIFEST)),
      ["s"], 1, names_check="check_required_structure", issue="required file missing")
probe("template require_file fires on an empty artifact file",
      lambda d: s_pass(d) or (d / "s/ARTIFACT.json").write_text("   \n"),
      ["s"], 1, names_check="check_required_structure", issue="required file is empty")
probe("template stamped() fires on a non-string generated_by",
      lambda d: s_pass(d, None, json.loads(json.dumps(PASS_MANIFEST).replace('"drafter.1.0"', "17"))),
      ["s"], 1, names_check="check_required_structure", issue="non-empty identity string")

# positive control: without it, a template that can NEVER approve looks identical to a
# correct one, and every negative probe above would still be green.
probe("template exit 0 on a compliant session (positive control)", s_pass, ["s"], 0)

# one negative per check, each asserting the report names ITS OWN check — a single "bad"
# fixture trips whichever check runs first and leaves the rest unproven forever.
probe("template names check_required_structure on an id-less item",
      lambda d: s_pass(d, {"items": [{"upstream_ref": "a1"}, {"id": "i2", "upstream_ref": "a2"}]}),
      ["s"], 1, names_check="check_required_structure")
probe("template names check_upstream_coverage on an unbound upstream id",
      lambda d: s_pass(d, {"items": [{"id": "i1", "upstream_ref": "a1"}]}),
      ["s"], 1, names_check="check_upstream_coverage")
probe("template names check_forbidden_markers on a leaked answer key",
      lambda d: s_pass(d, {"items": [{"id": "i1", "upstream_ref": "a1", "text": "ANSWER KEY: 1c"},
                                     {"id": "i2", "upstream_ref": "a2"}]}),
      ["s"], 1, names_check="check_forbidden_markers")
probe("template names check_required_structure on a non-boolean gate flag",
      lambda d: s_pass(d, None, json.loads(json.dumps(PASS_MANIFEST).replace("false", '"false"'))),
      ["s"], 1, names_check="check_required_structure")

# the ways an author mid-instantiation could ship a validator that validates nothing
def _checks_line(replacement):
    src = TEMPLATE.read_text()
    out = re.sub(r"^CHECKS = \[.*\]$", replacement, src, flags=re.M)
    assert out != src, "CHECKS assignment line not found — probe is stale"
    return out


def _gut(fn):
    """Replace a sample check's whole body with `return`, leaving the def intact."""
    src = TEMPLATE.read_text()
    anchor = f"def {fn}(session, manifest):"
    i = src.index(anchor) + len(anchor)
    j = src.index("\n\n\n", i)
    return src[:i] + "\n    return" + src[j:]


probe("template exit 2 when CHECKS is empty", s_pass, ["s"], 2, source=_checks_line("CHECKS = []"))
probe("template exit 2 on a duplicated CHECKS entry (evidence would cover for itself)",
      s_pass, ["s"], 2,
      source=_checks_line("CHECKS = [check_forbidden_markers, check_forbidden_markers]"))
probe("template exit 2 on an anonymous CHECKS entry", s_pass, ["s"], 2,
      source=_checks_line("CHECKS = [lambda s, m: checked(s)]"))
probe("template refuses a check that produced no evidence", s_pass, ["s"], 1,
      source=_gut("check_forbidden_markers"), names_check="check_forbidden_markers",
      issue="NOT RUN")
probe("template binds evidence to the running check, not to a name it passes",
      s_pass, ["s"], 1, names_check="check_upstream_coverage", issue="NOT RUN",
      # a check trying to vouch for another: checked() takes no name, so this records
      # evidence for check_forbidden_markers only, and upstream_coverage is still NOT RUN
      source=_gut("check_upstream_coverage").replace(
          '    text = require_file(session, "ARTIFACT.json")',
          '    checked("check_upstream_coverage")\n    text = require_file(session, "ARTIFACT.json")'))

# the template's own helper contract: the docstring promises the require_* helpers record
# evidence, so a check built only from them must not be reported NOT RUN on its happy path.
def _one_check(body):
    src = TEMPLATE.read_text()
    src = src.replace("def check_required_structure(session, manifest):",
                      f"def check_probe(session, manifest):\n{body}\n\n\n"
                      "def check_required_structure(session, manifest):", 1)
    return re.sub(r"^CHECKS = \[.*\]$", "CHECKS = [check_probe]", src, flags=re.M)


probe("template require_bool alone counts as evidence (helpers record for you)", s_pass,
      ["s"], 0, source=_one_check('    rec = require_record(manifest, "ARTIFACT")\n'
                                  '    require_bool(rec, "reviewed",\n'
                                  '                 "manifest.artifacts.ARTIFACT.reviewed")'))

# era_at_least compares NUMBERS: the prescribed `>=` on version strings said 1.17 < 1.4.
def _era_probe():
    with tempfile.TemporaryDirectory() as td:
        v = pathlib.Path(td) / "v.py"; v.write_text(TEMPLATE.read_text())
        return subprocess.run([sys.executable, "-c",
            "import importlib.util,sys;s=importlib.util.spec_from_file_location('v',sys.argv[1]);"
            "m=importlib.util.module_from_spec(s);s.loader.exec_module(m);"
            "print(m.era_at_least({'session_contract_version':'x.1.17'},'x.1.4'),"
            "m.era_at_least({'session_contract_version':'x.10.0'},'x.9.0'),"
            "m.era_at_least({'session_contract_version':'x.1.2'},'x.1.4'))", str(v)],
            capture_output=True, text=True).stdout.strip()


_era = _era_probe()
record("template era_at_least compares numbers, not strings", _era == "True True False", _era)


# the fixture-runner snippet is the code every downstream author copies: it must parse.
def _snippet_parses():
    import textwrap
    s = TEMPLATE.read_text().split("release_lint.py gets a check like:\n\n")[1]
    s = s.split("\n\nThe reviewer")[0]
    try:
        # compiled AS PASTED: the docstring no longer stores backslash escapes, because a
        # block an author copies out of the file has to be valid where they paste it
        compile(textwrap.dedent(s), "<snippet>", "exec")
        return True, ""
    except SyntaxError as e:
        return False, str(e)[:70]


_snip_ok, _snip_why = _snippet_parses()
record("template's prescribed lint snippet parses as Python", _snip_ok, _snip_why)

# --------------------------------------------------------------------------------------
# the GENERATED harness, end to end. The template's docstring prescribes a fixture runner
# that every downstream plugin copies; until now it was verified by hand, which means it was
# verified when someone remembered. This builds a real downstream plugin from the template,
# transcribes the snippet verbatim, and requires each claimed rejection to fire.
# --------------------------------------------------------------------------------------
def _downstream(td, mutate=None):
    """Instantiate the template, write the prescribed fixtures and the prescribed lint, run it."""
    import textwrap
    d = pathlib.Path(td)
    (d / ".claude-plugin").mkdir(parents=True)
    (d / ".claude-plugin/plugin.json").write_text(json.dumps({"version": "0.1.0"}))
    src = TEMPLATE.read_text().replace("SAMPLES_PRESENT = True", "SAMPLES_PRESENT = False", 1)
    src = src.replace('CONTRACT_VERSION = "<x>_skill.0.1"', 'CONTRACT_VERSION = "d_skill.0.1"', 1)
    (d / "validate_ARTIFACT.py").write_text(src)
    snip = TEMPLATE.read_text().split("release_lint.py gets a check like:\n\n")[1]
    snip = textwrap.dedent(snip.split("\n\nThe reviewer")[0])
    snip = snip.replace("skills/<x>/scripts/validate_ARTIFACT.py", "validate_ARTIFACT.py")
    (d / "gen_lint.py").write_text(
        "import hashlib, json, pathlib, subprocess, sys\n"
        "ROOT = pathlib.Path(__file__).resolve().parent\nerrors = []\n" + snip +
        '\nfor e in errors: print("ERROR", e)\nsys.exit(1 if errors else 0)\n')
    fx = d / "tests/fixtures"
    def fixture(name, artifact=None, manifest=None):
        q = fx / name; q.mkdir(parents=True, exist_ok=True)
        (q / "manifest.json").write_text(json.dumps(manifest or PASS_MANIFEST))
        (q / "ARTIFACT.json").write_text(json.dumps(artifact or PASS_ARTIFACT, indent=1))
    fixture("ARTIFACT_pass")
    fixture("ARTIFACT_fail_check_required_structure",
            {"items": [{"upstream_ref": "a1"}, PASS_ARTIFACT["items"][1]]})
    fixture("ARTIFACT_fail_check_upstream_coverage", {"items": [PASS_ARTIFACT["items"][0]]})
    fixture("ARTIFACT_fail_check_forbidden_markers",
            {"items": [{"id": "i1", "upstream_ref": "a1", "text": "ANSWER KEY: 1c"},
                       PASS_ARTIFACT["items"][1]]})
    if mutate:
        mutate(d)
    r = subprocess.run([sys.executable, str(d / "gen_lint.py")], capture_output=True, text=True,
                       cwd="/")   # ROOT-anchored: must not depend on the working directory
    return r.returncode, r.stdout


def downstream(name, mutate, expect_tag, expect_fail=True):
    if ONLY and ONLY not in name:
        return
    with tempfile.TemporaryDirectory() as td:
        try:
            rc, out = _downstream(td, mutate)
        except Exception as e:
            return record(name, False, f"could not build: {e!r}")
        if expect_fail:
            ok = rc != 0 and expect_tag in out
            why = "" if ok else (f"exit {rc}, expected nonzero" if rc == 0
                                 else f"failed, but not with {expect_tag!r}")
        else:
            ok = rc == 0 and not out.strip()
            why = "" if ok else f"exit {rc}, output {out.strip()[:60]!r}"
        record(name, ok, why)


def _edit(rel, old, new):
    def m(d):
        q = d / rel
        s = q.read_text()
        if old not in s:
            raise AssertionError(f"anchor {old[:40]!r} missing in {rel} — probe is stale")
        q.write_text(s.replace(old, new, 1))
    return m


downstream("downstream harness: an honest plugin is silent", None, "", expect_fail=False)
downstream("downstream: fixture that BLANKS an input (proves the helper, not the check)",
           lambda d: (d / "tests/fixtures/ARTIFACT_fail_check_forbidden_markers/ARTIFACT.json")
           .write_text("   \n"), "REMOVES")
downstream("downstream: fixture that DROPS a manifest record",
           lambda d: (d / "tests/fixtures/ARTIFACT_fail_check_upstream_coverage/manifest.json")
           .write_text(json.dumps({"session_contract_version": "toy.1.0",
                                   "artifacts": {"ARTIFACT": PASS_MANIFEST["artifacts"]["ARTIFACT"]}})),
           "REMOVES")
downstream("downstream: a check that CRASHES (runner diagnostics are not proof it ran)",
           _edit("validate_ARTIFACT.py", "    for n, line in enumerate(text.splitlines(), 1):",
                 '    raise ValueError("boom")\n    for n, line in enumerate(text.splitlines(), 1):'),
           "crit: False")
downstream("downstream: positive fixture missing (was a traceback)",
           lambda d: shutil.rmtree(d / "tests/fixtures/ARTIFACT_pass"), "ARTIFACT_pass is missing")
downstream("downstream: two byte-identical negative fixtures",
           lambda d: (d / "tests/fixtures/ARTIFACT_fail_check_forbidden_markers/ARTIFACT.json")
           .write_text((d / "tests/fixtures/ARTIFACT_fail_check_required_structure/ARTIFACT.json")
                       .read_text()), "byte-identical")
downstream("downstream: a guard downgraded from crit to warn",
           _edit("validate_ARTIFACT.py", '                crit(f"ARTIFACT.json:{n}",',
                 '                warn(f"ARTIFACT.json:{n}",'), "crit: False")
downstream("downstream: template samples still present",
           _edit("validate_ARTIFACT.py", "SAMPLES_PRESENT = False", "SAMPLES_PRESENT = True"),
           "SAMPLES_PRESENT")
downstream("downstream: CONTRACT_VERSION trailing the release",
           _edit("validate_ARTIFACT.py", '"d_skill.0.1"', '"d_skill.0.0"'), "trails the release")
downstream("downstream: a fixture for a check absent from CHECKS",
           lambda d: shutil.copytree(d / "tests/fixtures/ARTIFACT_fail_check_forbidden_markers",
                                     d / "tests/fixtures/ARTIFACT_fail_check_never_registered"),
           "absent from CHECKS")

# --------------------------------------------------------------------------------------
# reachability: the 1.10 split broke citations; keep them honest
# --------------------------------------------------------------------------------------
idx = (ROOT / IDX).read_text()
stub = (ROOT / "skills/edu-skill-creator/reference/lessons_learned.md").read_text()
record("lessons_learned.md is a stub, not cited as a ledger", len(stub.splitlines()) < 40)
_scanned = [p for p in (ROOT / "skills").rglob("*.md")]
bad = [p.relative_to(ROOT) for p in _scanned
       if "reference/lessons_learned.md" in p.read_text() and "pointer stub" not in p.read_text()]
record("no skill cites the gutted ledger as a source",
       bool(_scanned) and not bad, f"{[str(b) for b in bad]}" if bad else "")
_lessons = list((ROOT / LDIR).glob("*.md"))
# membership against PARSED row targets, exactly as check 12 does. A raw substring test over
# the index counted an HTML-comment mention as indexed — the defect check 12 was rewritten to
# catch, still living in the case that shadows it.
_linked = {pathlib.PurePosixPath(m).name for m in
           re.findall(r"^\| L\d+ \| [^|]+ \| [^|]+ \| \[`([^`]+)`\]", idx, re.M)}
record("every lesson file is indexed by a parsed row",
       bool(_lessons) and all(f.name in _linked for f in _lessons),
       "no lesson files found" if not _lessons else "")

# A --only run prints SELECTED, never PASS: release_lint check 13 keys on the PASS line and
# compares its count to the number of case call sites, so a filtered run must not look like
# a full one.
_verdict = ("SELECTED" if ONLY else "PASS") if all(o for _, o, _ in results) else "FAIL"
print(f"{_verdict}  {sum(1 for _, o, _ in results if o)}/{len(results)} deterministic checks\n")
for name, ok, detail in results:
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{'  — ' + detail if detail else ''}")
sys.exit(0 if all(o for _, o, _ in results) else 1)
