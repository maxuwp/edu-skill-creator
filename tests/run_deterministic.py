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
import json, pathlib, re, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "skills/scaffold/reference/validator_template.py"
results = []


def record(name, ok, detail=""):
    results.append((name, ok, detail))


def lint(repo, *args):
    # --skip-suite is mandatory here: lint check 13 runs this suite, so without it the
    # suite would invoke a lint that invokes the suite, forever. Cases that must exercise
    # check 13 itself use lint_full() against a STUB suite, which cannot recurse.
    r = subprocess.run([sys.executable, "scripts/release_lint.py", "--skip-suite", *args],
                       cwd=repo, capture_output=True, text=True)
    return r.returncode, r.stdout


def lint_full(repo, *args):
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
    with tempfile.TemporaryDirectory() as td:
        repo = _copy(td)
        try:
            mutate(repo)
        except Exception as e:
            return record(name, False, f"could not seed: {e!r}")
        rc, out = (lint_full if full else lint)(repo)
        if expect_fail:
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

seeded("c1 hardcoded harness path", m_path, "hardcodes a harness path")
seeded("c2 manifest version mismatch", m_version, "[manifest] version mismatch")
seeded("c2 version key deleted (once silenced c2, c5 and c8 at once)", m_vergone,
       "has no usable string 'version'")
seeded("c3 deprecated URL (was dead code)", m_deprec, "references deprecated")

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
seeded("c4 unparseable rubric (was a warning)", m_rubparse, "no dimension points parsed")

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
seeded("c9 reviews/ emptied (a glob with no floor reads clean)", m_revgone, "holds no review JSON")
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
seeded("c12 orphan lesson file", m_orphan, "no lesson_index.md row references it")
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

seeded("c13 suite missing", m_suitegone, "[tests] tests/run_deterministic.py is missing", full=True)
seeded("c13 suite fails (was proven only by hand)", m_suitefail,
       "[tests] deterministic suite failed", full=True)
seeded("c13 zero-byte suite exits 0 and proves nothing", m_suitemute, "verdict line", full=True)
seeded("c13 suite shrunk below its floor", m_suitefloor, "below the floor of", full=True)

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
def m_citeblind(r):
    _sub(r, "scripts/release_lint.py",
         'CITE16 = re.compile(r"`([^`\\s]*/[A-Za-z0-9_<>:.\\-/]*\\.(?:md|py|json|mjs))`")',
         'CITE16 = re.compile(r"`(NEVER_MATCHES_ANYTHING)`")')

seeded("c16 citation that does not resolve", m_citebad, "does not resolve")
seeded("c16 sibling cited through '..' (breaks in the installed layout)", m_citedots,
       "walks out of a skill directory")
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


def probe(name, setup, argv, expect, source=None, names_check=None):
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
            named = names_check in {f["check"] for f in rep["findings"]}
            ok, why = named, "" if named else f"report never names {names_check}"
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
probe("template exit 1 with report on missing record", s_ok, ["s"], 1)

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

# the two ways an author mid-instantiation could ship a validator that validates nothing
probe("template exit 2 when CHECKS is empty", s_pass, ["s"], 2,
      source=re.sub(r"^CHECKS = \[.*\]$", "CHECKS = []", TEMPLATE.read_text(), flags=re.M))
probe("template refuses a check that produced no evidence", s_pass, ["s"], 1,
      source=TEMPLATE.read_text().replace(
          '    checked("check_forbidden_markers", session / "ARTIFACT.json")', "    return"),
      names_check="check_forbidden_markers")

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
record("every lesson file is indexed",
       bool(_lessons) and all(f.name in idx for f in _lessons),
       "no lesson files found" if not _lessons else "")

print(f"{'PASS' if all(o for _, o, _ in results) else 'FAIL'}  "
      f"{sum(1 for _, o, _ in results if o)}/{len(results)} deterministic checks\n")
for name, ok, detail in results:
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{'  — ' + detail if detail else ''}")
sys.exit(0 if all(o for _, o, _ in results) else 1)
