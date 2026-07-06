#!/usr/bin/env python3
"""Release lint for the PAGE repo — run before every push (see MAINTAINING.md).

Checks the drift classes that actually bit POSED/p2d releases (see
skills/page/reference/lessons_learned.md L7/L8):
  1. Hardcoded ~/.claude / ~/.codex paths in shared skill markdown
     (whitelist: harness_adaptation.md and dual_harness_playbook.md, which
     define/spec the path mappings).
  2. The two plugin manifests (.claude-plugin / .codex-plugin) version-match.
  3. Deprecated repo URLs (none yet — placeholder list).
  4. Rubric dimension points sum to 100 in skills/*/reference/*rubric*.md.
  5. CHANGELOG.md has a real '## page_skill.X.Y ' heading for the current version.
  6. reference/ files cited by skills exist (warning only — heuristic).
  7. Manifest homepage/repository URLs match the configured git remote: a manifest
     that claims a hosted repo while origin points elsewhere is an error; a claimed
     repo with no origin at all is a warning at scaffold time — pass --publish (as
     page-release step 8 does after the publish gate) and it becomes an error.
  8. Uniform skill versioning: every skills/*/SKILL.md frontmatter `version` equals
     the plugin manifests' major.minor. Skill versions are bumped together on every
     release, so a stale frontmatter is mechanical drift, not history.
  9. Review evidence is mechanically resolved: every reviews/*_review.json finding
     has status fixed|accepted plus a resolution, and every review file has a
     resolution_pass block.

Exit 0 = clean (warnings allowed), 1 = errors found.
"""
import json, pathlib, re, subprocess, sys

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
                          f"use <page-skill-dir>/… or <skills-dir>/…")

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
DEPRECATED = ()
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
#    teaser mention like '*next → page_skill.1.1*' does not count)
if plugin_version:
    major_minor = "page_skill." + ".".join(plugin_version.split(".")[:2])
    clog = ROOT / "CHANGELOG.md"
    clog_text = clog.read_text() if clog.exists() else ""
    if f"## {major_minor} " not in clog_text:
        errors.append(f"[changelog] no '## {major_minor}' entry heading "
                      f"(plugin.json is {plugin_version})")

# 6. Cited reference files exist (heuristic, warning only)
cite = re.compile(r"`(?:<page-skill-dir>/)?reference/([A-Za-z0-9_\-]+\.md)`")
for p in (ROOT / "skills").rglob("SKILL.md"):
    text = p.read_text()
    for m in cite.finditer(text):
        name = m.group(1)
        candidates = [p.parent / "reference" / name,
                      ROOT / "skills" / "page" / "reference" / name]
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
    if findings and not isinstance(data.get("resolution_pass"), dict):
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

for w in warnings: print("WARN ", w)
for e in errors:   print("ERROR", e)
print(f"\nrelease_lint: {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
