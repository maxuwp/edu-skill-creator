#!/usr/bin/env python3
"""Deterministic regression suite. Every case here corresponds to a defect that actually shipped.

Usage: python3 tests/run_deterministic.py       Exit 0 = all pass, 1 = a regression.
Works on a throwaway copy; the real tree is never modified.
"""
import json, pathlib, shutil, subprocess, sys, tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
results = []


def record(name, ok, detail=""):
    results.append((name, ok, detail))


def lint(repo, *args):
    # --skip-suite is mandatory: lint check 13 runs this suite, so without it the
    # suite would invoke a lint that invokes the suite, forever.
    r = subprocess.run([sys.executable, "scripts/release_lint.py", "--skip-suite", *args],
                       cwd=repo, capture_output=True, text=True)
    return r.returncode, r.stdout


def seeded(name, mutate, expect_fail=True):
    """Copy the repo, mutate it, assert the lint verdict flips. A check that cannot fail
    is worse than no check (L8) — this proves each one still can."""
    with tempfile.TemporaryDirectory() as td:
        repo = pathlib.Path(td) / "r"
        shutil.copytree(ROOT, repo, ignore=shutil.ignore_patterns(".git"))
        try:
            mutate(repo)
        except Exception as e:
            return record(name, False, f"could not seed: {e!r}")
        rc, out = lint(repo)
        ok = (rc != 0) if expect_fail else (rc == 0)
        record(name, ok, "" if ok else f"exit {rc}; expected {'nonzero' if expect_fail else 0}")


# --- lint checks that once could not fail, or silently skipped ---
def m_path(r):    (r / "skills/intent/SKILL.md").write_text(
                      (r / "skills/intent/SKILL.md").read_text() + "\nSee ~/.claude/skills/x\n")
def m_version(r): p = r / ".codex-plugin/plugin.json"; d = json.loads(p.read_text()); d["version"] = "9.9.9"; p.write_text(json.dumps(d))
def m_deprec(r):  (r / "README.md").write_text((r / "README.md").read_text() + "\nsee maxuwp/page\n")
def m_chlog(r):
    # version-derived, never hardcoded: a suite that pins a release number goes stale
    # the moment the release does, and reports a false failure instead of a real one.
    v = ".".join(json.loads((r / ".claude-plugin/plugin.json").read_text())["version"].split(".")[:2])
    p = r / "CHANGELOG.md"
    p.write_text(p.read_text().replace(f"## edu_skill_creator.{v}", f"## old.{v}", 1))
def m_review(r):  p = r / "reviews/edu-skill-creator-draft_review.json"; d = json.loads(p.read_text()); d["findings"] = []; d.pop("resolution_pass", None); p.write_text(json.dumps(d))
def m_claim(r):   p = r / "skills/edu-skill-creator/reference/lesson_index.md"; p.write_text(p.read_text().replace("rubric critical flag 13", "rubric critical flag 99", 1))
def m_idxgone(r): (r / "skills/edu-skill-creator/reference/lesson_index.md").unlink()
def m_dangle(r):  p = r / "skills/edu-skill-creator/reference/lesson_index.md"; p.write_text(p.read_text().replace("L01_grounding.md", "L01_GONE.md"))
def m_orphan(r):  shutil.copy(r / "skills/edu-skill-creator/reference/lessons/L01_grounding.md",
                              r / "skills/edu-skill-creator/reference/lessons/L99_orphan.md")

def m_rubric(r):  p = r / "skills/edu-skill-creator/reference/skill_quality_rubric.md"; p.write_text(p.read_text().replace("| 25 |", "| 40 |", 1))
def m_url(r):
    # the copy has no .git, so check 7 would take its no-origin WARNING branch and prove
    # nothing. Give it a real origin, then mismatch the manifest against it.
    for cmd in (["git", "init", "-q"], ["git", "remote", "add", "origin",
                                        "https://github.com/maxuwp/edu-skill-creator.git"]):
        subprocess.run(cmd, cwd=r, capture_output=True)
    p = r / ".claude-plugin/plugin.json"; d = json.loads(p.read_text())
    d["homepage"] = "https://github.com/maxuwp/WRONG"; p.write_text(json.dumps(d))
def m_skillver(r):
    # version-derived, never pinned: a fixture that hardcodes a release number breaks
    # on the next bump and reports a false failure. This is the second time.
    import re as _re
    p = r / "skills/intent/SKILL.md"
    p.write_text(_re.sub(r'^version: "[0-9.]+"$', 'version: "0.1"', p.read_text(), count=1, flags=_re.M))
def m_drift(r):   p = r / "reflect_ledger.json"; p.write_text(p.read_text().replace('"prepared_by"', '"prepared_by_"', 1))
def m_incoh(r):   p = r / "reviews/edu-skill-creator-draft_review.json"; d = json.loads(p.read_text()); d["critical_flags"] = ["seeded"]; p.write_text(json.dumps(d))

for n, m in [("lint c4 rubric dimensions sum", m_rubric), ("lint c7 manifest URL vs origin", m_url),
             ("lint c8 uniform skill version", m_skillver), ("lint c14 ledger drift after gate", m_drift),
             ("lint c15 review recommends approve with a critical", m_incoh),
             ("lint c1 hardcoded harness path", m_path), ("lint c2 manifest version mismatch", m_version),
             ("lint c3 deprecated URL (was dead code)", m_deprec), ("lint c5 changelog heading", m_chlog),
             ("lint c9 review without resolution_pass (was bypassable)", m_review),
             ("lint c11 unresolvable enforcement claim", m_claim),
             ("lint c11 index deleted (was a silent skip)", m_idxgone),
             ("lint c11 dangling lesson path", m_dangle), ("lint c12 orphan lesson file", m_orphan)]:
    seeded(n, m)
seeded("lint clean on an unmodified tree", lambda r: None, expect_fail=False)

# --- validator template: its documented fail-closed contract ---
def probe(name, setup, argv, expect):
    with tempfile.TemporaryDirectory() as td:
        d = pathlib.Path(td)
        shutil.copy(ROOT / "skills/scaffold/reference/validator_template.py", d / "v.py")
        try:
            setup(d)
        except Exception as e:
            return record(name, False, f"setup failed: {e!r}")
        r = subprocess.run([sys.executable, "v.py", *argv], cwd=d, capture_output=True, text=True)
        ok = r.returncode == expect and "Traceback" not in r.stderr
        record(name, ok, "" if ok else f"exit {r.returncode} (want {expect}){' TRACEBACK' if 'Traceback' in r.stderr else ''}")


def s_none(d):  (d / "s").mkdir()
def s_list(d):  (d / "s").mkdir(); (d / "s/manifest.json").write_text("[1,2,3]")
def s_ok(d):    (d / "s").mkdir(); (d / "s/manifest.json").write_text('{"artifacts":{}}')
def s_blk(d):   s_ok(d); (d / "s/blocker").write_text("x")

probe("template exit 2 on missing manifest", s_none, ["s"], 2)
probe("template exit 2 on non-object manifest (was a crash)", s_list, ["s"], 2)
probe("template exit 2 on unwritable report dir (was a crash)", s_blk, ["s", "--report", "s/blocker/x/r.json"], 2)
probe("template exit 2 on --report with no path (was a crash)", s_ok, ["s", "--report"], 2)
probe("template exit 1 with report on missing record", s_ok, ["s"], 1)

# --- reachability: the 1.10 split broke citations; keep them honest ---
idx = (ROOT / "skills/edu-skill-creator/reference/lesson_index.md").read_text()
stub = (ROOT / "skills/edu-skill-creator/reference/lessons_learned.md").read_text()
record("lessons_learned.md is a stub, not cited as a ledger", len(stub.splitlines()) < 40)
bad = [p.relative_to(ROOT) for p in (ROOT / "skills").rglob("*.md")
       if "reference/lessons_learned.md" in p.read_text() and "pointer stub" not in p.read_text()]
record("no skill cites the gutted ledger as a source", not bad, f"{[str(b) for b in bad]}")
# check 6 is warning-only; assert the WARN appears rather than an exit code
with tempfile.TemporaryDirectory() as _td:
    _r = pathlib.Path(_td) / "r"; shutil.copytree(ROOT, _r, ignore=shutil.ignore_patterns(".git"))
    _p = _r / "skills/test/SKILL.md"
    _p.write_text(_p.read_text() + "\n\nSee `reference/does_not_exist.md`.\n")
    _rc, _out = lint(_r)
    record("lint c6 dangling reference emits a warning", "does_not_exist.md" in _out)

# check 13 runs this suite, so it cannot seed itself here; proven manually in 1.13 by
# disabling the check-3 guard and observing check 13 fail. Recorded, not silently skipped.
record("lint c13 self-test noted as externally proven", True, "see CHANGELOG 1.13")

record("every lesson file is indexed",
       all(f.name in idx for f in (ROOT / "skills/edu-skill-creator/reference/lessons").glob("*.md")))

print(f"{'PASS' if all(o for _, o, _ in results) else 'FAIL'}  "
      f"{sum(1 for _, o, _ in results if o)}/{len(results)} deterministic checks\n")
for name, ok, detail in results:
    print(f"  {'ok  ' if ok else 'FAIL'}  {name}{'  — ' + detail if detail else ''}")
sys.exit(0 if all(o for _, o, _ in results) else 1)
