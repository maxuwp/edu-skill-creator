#!/usr/bin/env python3
"""Release lint for the Edu Skill Creator repo — run before every push (see MAINTAINING.md).

Checks the drift classes that actually bit POSED/p2d releases (see
skills/edu-skill-creator/reference/lessons_learned.md L7/L8):
  1. Hardcoded ~/.claude / ~/.codex paths in shared skill markdown
     (whitelist: harness_adaptation.md and dual_harness_playbook.md, which
     define/spec the path mappings).
  2. The two plugin manifests (.claude-plugin / .codex-plugin) version-match.
  3. Deprecated repo URLs (none yet — placeholder list).
  4. Rubric dimension points sum to 100 in skills/*/reference/*rubric*.md.
  5. CHANGELOG.md has a real '## edu_skill_creator.X.Y ' heading for the current version.
  6. reference/ files cited by skills exist (warning only — heuristic).
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
 12. Registry completeness: every file in reference/lessons/ is referenced by the
     index, so no lesson is unreachable.

Exit 0 = clean (warnings allowed), 1 = errors found.
"""
import hashlib, json, pathlib, re, subprocess, sys

PUBLISH = "--publish" in sys.argv[1:]
ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []

# 1. Hardcoded harness paths in shared skill bodies
WHITELIST = {"harness_adaptation.md", "dual_harness_playbook.md"}
for p in (ROOT / "skills").rglob("*.md"):
    if p.name in WHITELIST:
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
    vers[mp] = json.loads(f.read_text()).get("version")
if len(set(vers.values())) > 1:
    errors.append(f"[manifest] version mismatch: {vers}")
plugin_version = next(iter(vers.values()), None)

# 3. Deprecated repo URLs outside the changelog (none at birth; add as they retire)
DEPRECATED = ("maxuwp/page",)  # pre-rename repo; live check, not a placeholder
for p in list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.json")):
    rel = p.relative_to(ROOT)
    if rel.parts[0] in {".git", "node_modules"} or p.name == "CHANGELOG.md":
        continue
    text = p.read_text(errors="ignore")
    for dep in DEPRECATED:
        if dep in text:
            errors.append(f"[repo] {rel} references deprecated {dep}")

# 4. Rubric dimensions sum to 100 (table style: | n | name | pts | ... ;
#    heading style: '### N. Name — 20 points')
for p in (ROOT / "skills").glob("*/reference/*rubric*.md"):
    text = p.read_text()
    if "100 points" not in text and "/100" not in text:
        continue  # not a scored reviewer rubric
    pts = [int(m.group(1)) for m in
           re.finditer(r"^\|\s*\d+\s*\|[^|]+\|\s*(\d+)\s*\|", text, re.M)]
    if not pts:
        pts = [int(m.group(1)) for m in
               re.finditer(r"^###\s+\d+\..*—\s*(\d+)\s*points", text, re.M)]
    if pts and sum(pts) != 100:
        errors.append(f"[rubric] {p.name}: dimensions sum to {sum(pts)}, expected 100")
    elif not pts:
        warnings.append(f"[rubric] {p.name}: could not parse dimension points")

# 5. Changelog covers the current plugin version (heading required — a
#    teaser mention like '*next → edu_skill_creator.1.1*' does not count)
if plugin_version:
    major_minor = "edu_skill_creator." + ".".join(plugin_version.split(".")[:2])
    clog = ROOT / "CHANGELOG.md"
    clog_text = clog.read_text() if clog.exists() else ""
    if f"## {major_minor} " not in clog_text:
        errors.append(f"[changelog] no '## {major_minor}' entry heading "
                      f"(plugin.json is {plugin_version})")

# 6. Cited reference files exist (heuristic, warning only)
cite = re.compile(r"`(?:<edu-skill-creator-skill-dir>/)?reference/([A-Za-z0-9_\-]+\.md)`")
for p in (ROOT / "skills").rglob("SKILL.md"):
    text = p.read_text()
    for m in cite.finditer(text):
        name = m.group(1)
        candidates = [p.parent / "reference" / name,
                      ROOT / "skills" / "edu-skill-creator" / "reference" / name]
        if not any(c.exists() for c in candidates):
            warnings.append(f"[ref] {p.relative_to(ROOT)} cites reference/{name} — not found")

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
    for key in ("homepage", "repository"):
        v = data.get(key)
        if isinstance(v, str) and "://" in v:
            claimed.add(_norm(v))
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
            warnings.append(f"[skillver] {p.relative_to(ROOT)}: no frontmatter version")
        elif m.group(1) != mm:
            errors.append(f"[skillver] {p.relative_to(ROOT)}: frontmatter version "
                          f"{m.group(1)} != plugin {mm} (uniform convention — bump on release)")

# 9. Review evidence: no status-less findings, no unrecorded resolution pass
for p in sorted((ROOT / "reviews").glob("*_review.json")):
    try:
        data = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        errors.append(f"[review] {p.relative_to(ROOT)}: invalid JSON ({e})")
        continue
    findings = data.get("findings", [])
    if not isinstance(data.get("resolution_pass"), dict):
        errors.append(f"[review] {p.relative_to(ROOT)}: missing resolution_pass block")
    for i, finding in enumerate(findings, 1):
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
if not LL.exists():
    errors.append("[ledger] lesson_index.md is missing — the enforcement ledger cannot be checked; "
                  "a vanished input is a failure, not a skip")
else:
    def _numbered(path):
        f = ROOT / path
        return ({int(n) for n in re.findall(r"^\s*(\d+)\.\s", f.read_text(), re.M)}
                if f.exists() else set())
    targets = {
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
    for lesson, claim in [(a, b) for a, b, _ in _rows]:
        for label, (where, present) in targets.items():
            for m in re.finditer(label.replace(" ", r"\s") + r"s?\s+(\d+)(?:\s*[\u2013-]\s*(\d+))?", claim):
                for n in [int(m.group(1))] + ([int(m.group(2))] if m.group(2) else []):
                    if n not in present:
                        errors.append(f"[ledger] {lesson} claims '{label} {n}' but {where} "
                                      f"has no numbered item {n} — L13: the claim or the "
                                      f"enforcement must change, not neither")

# 12. Registry completeness (L7 fold): every lesson detail file appears in the index.
#     Check 11 verifies index->file; this verifies file->index. An orphan lesson is a
#     rule nobody will ever read. This is the check L7's fold previously mis-attributed
#     to check 11, which does something else entirely.
_ldir = ROOT / "skills" / "edu-skill-creator" / "reference" / "lessons"
if _ldir.is_dir():
    _idx_text = LL.read_text() if LL.exists() else ""
    _orphans = [f.name for f in sorted(_ldir.glob("*.md")) if f.name not in _idx_text]
    for _o in _orphans:
        errors.append(f"[registry] lessons/{_o} exists but no lesson_index.md row references it — "
                      f"an unreachable lesson (L7: every unit appears in the registry that governs it)")
    if not list(_ldir.glob("*.md")):
        errors.append("[registry] reference/lessons/ contains no lesson files — fail closed")

# 13. The deterministic regression suite passes. Every case in it corresponds to a
#     defect that actually shipped; if one stops firing, a guard has gone dead.
_suite = ROOT / "tests" / "run_deterministic.py"
if not _suite.exists():
    errors.append("[tests] tests/run_deterministic.py is missing — the regression suite is the "
                  "only thing proving the other checks still fire; a vanished suite is a failure")
elif "--skip-suite" not in sys.argv[1:]:
    _r = subprocess.run([sys.executable, str(_suite)], capture_output=True, text=True)
    if _r.returncode != 0:
        _fails = [l.strip() for l in _r.stdout.splitlines() if l.strip().startswith("FAIL")]
        errors.append(f"[tests] deterministic suite failed: {'; '.join(_fails) or 'see output'}")

# 14. Approved artifacts have not drifted since their gate decision. A decision that
#     names its artifact by version string cannot notice the artifact changing; this
#     asks every push, instead of waiting for someone to ask.
_gate = ROOT / "reflect_gate_decision.json"
if _gate.exists():
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
for _rf in sorted((ROOT / "reviews").glob("*.json")):
    try:
        _d = json.loads(_rf.read_text())
    except json.JSONDecodeError:
        continue  # check 9 already reports unreadable review files
    _rec = _d.get("recommendation") or _d.get("gate_recommendation")
    if _rec not in ("approve", "open-the-gate", "approve-with-acknowledged-majors"):
        continue
    _why = []
    if _d.get("critical_flags"):
        _why.append(f"{len(_d['critical_flags'])} critical flag(s)")
    _blk = [f for f in _d.get("findings", []) if f.get("severity") == "blocking"]
    if _blk:
        _why.append(f"{len(_blk)} blocking finding(s)")
    if _d.get("counts", {}).get("blocking"):
        _why.append(f"counts.blocking={_d['counts']['blocking']}")
    _sc, _th = _d.get("score"), _d.get("threshold")
    if isinstance(_sc, (int, float)) and isinstance(_th, (int, float)) and _sc < _th:
        _why.append(f"score {_sc} below threshold {_th}")
    if _d.get("passed") is False:
        _why.append("passed:false")
    if _why:
        errors.append(f"[coherence] {_rf.name} recommends {_rec!r} while its own record shows "
                      f"{', '.join(_why)} — a recommendation must agree with the evidence it signs")

for w in warnings: print("WARN ", w)
for e in errors:   print("ERROR", e)
print(f"\nrelease_lint: {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
