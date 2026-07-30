#!/usr/bin/env python3
"""validate_ARTIFACT.py — computed structural validator (Edu Skill Creator L11 template).

`edu-skill-creator-scaffold` instantiates ONE copy of this template per artifact named
in the architecture's computed-validation plan (architecture item 11): replace ARTIFACT,
fill in CHECKS, delete the sample bodies. Everything import-free and self-contained on
purpose — a validator with dependencies is a validator someone will skip.

Why this exists (L11, `<edu-skill-creator-skill-dir>/reference/lessons/L11_computed_validators.md`): prose contracts rot. A POSED pilot deck
passed FOUR fresh-context prose reviews at 94/100 while carrying 13 structural
criticals; the computed validator failed it instantly. LLM review establishes judgment;
this script establishes structure. Both layers, always.

ONE IMPLEMENTATION, TWO CALLERS
  1. The drafter skill runs this PRE-GATE as a self-check (fix, re-run, then hand off).
  2. The reviewer skill re-runs the SAME script as a hard gate and records the report:
     its `approve` is illegal unless `passed: true` with a real report path, and the
     orchestrator refuses to open the human gate otherwise.
Never restate any threshold/formula from this file in a SKILL.md or rubric — cite the
script (L7 corollary: restated values diverge; three divergent pacing formulas is the
recorded failure).

USAGE
  python3 validate_ARTIFACT.py <session_dir> [--report <path>]
Exit 0 = pass (warnings allowed) · 1 = criticals found · 2 = could not run.
Exit 2 is FAIL-CLOSED: an unreadable session, missing manifest, or crashing check means
"not validated", never "nothing to check". Callers treat 1 and 2 identically: no gate.

FIXTURES — ONE NEGATIVE PER CHECK, NOT ONE PER VALIDATOR (L8/L11)
  tests/fixtures/ARTIFACT_pass/              — exit 0; minimal compliant session
  tests/fixtures/ARTIFACT_fail_<check_id>/   — exit 1, AND the report must name <check_id>
A single \"bad\" fixture trips whichever check fires first and leaves every other check
unproven forever; that is how a validator with three checks ships with one working.
Neutralizing a fail fixture must make the release lint itself fail (prove the proof).
Fixtures NEVER contain student/faculty course content — the data posture (intent A.7)
applies to test data too. The generated release_lint.py gets a check like:

    # check N: one negative fixture per check, plus the positive control
    import importlib.util
    spec = importlib.util.spec_from_file_location(\"v\", \"skills/<x>/scripts/validate_ARTIFACT.py\")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    rc = subprocess.run([sys.executable, V, \"tests/fixtures/ARTIFACT_pass\"]).returncode
    if rc != 0:
        errors.append(\"[fixtures] ARTIFACT_pass did not pass — the validator can never approve\")
    for fn in (c.__name__ for c in mod.CHECKS):
        d = pathlib.Path(f\"tests/fixtures/ARTIFACT_fail_{fn}\")
        if not d.is_dir():
            errors.append(f\"[fixtures] {fn} has no negative fixture — unproven, not exempt\")
            continue
        rep = d / \"r.json\"
        rc = subprocess.run([sys.executable, V, str(d), \"--report\", str(rep)]).returncode
        named = fn in {f[\"check\"] for f in json.loads(rep.read_text())[\"findings\"]} if rep.exists() else False
        if rc != 1 or not named:
            errors.append(f\"[fixtures] ARTIFACT_fail_{fn}: exit {rc}, {fn} named: {named}\")
"""
import json, pathlib, re, sys

# Keep equal to the plugin's current release; the generated lint checks the match.
CONTRACT_VERSION = "<x>_skill.0.1"

findings = []
evidence = []          # what each check actually examined; see checked() and main()


def checked(check, target):
    """Record that CHECK really examined TARGET. The runner refuses any check that finishes
    with neither evidence nor a finding: an empty CHECKS list, a body an author left as
    comments, or a stub that returns early all produce `passed: true` otherwise, and a
    validator that examined nothing is the most expensive kind of green."""
    evidence.append((check, str(target)))


def crit(check, location, issue, fix_hint=""):
    findings.append({"severity": "critical", "check": check, "location": str(location),
                     "issue": issue, "fix_hint": fix_hint})


def warn(check, location, issue, fix_hint=""):
    findings.append({"severity": "warning", "check": check, "location": str(location),
                     "issue": issue, "fix_hint": fix_hint})


# ---------- fail-closed helpers (L11: missing = refusal, never a skip) ----------

def require_file(session, rel, check):
    """A file the contract promises. Missing/empty/unreadable = critical, return None.
    (The 1.30.1 lesson: a guard that skips what's missing passes what's forged.)"""
    p = session / rel
    try:
        text = p.read_text()
    except OSError:
        crit(check, rel, "required file missing or unreadable",
             "generate it via the owning stage; do not hand-create")
        return None
    if not text.strip():
        crit(check, rel, "required file is empty", "regenerate via the owning stage")
        return None
    return text


def require_record(manifest, key, check):
    """A manifest record the contract promises. A missing record is UNAPPROVED BY
    DEFINITION — never 'nothing to validate' (the publisher hole, posed 1.30.1)."""
    rec = (manifest or {}).get("artifacts", {}).get(key)
    if not isinstance(rec, dict):
        crit(check, f"manifest.artifacts.{key}", "record missing — unapproved by definition",
             "the owning drafter stamps this record; re-run it")
    return rec if isinstance(rec, dict) else None


def require_bool(container, key, check, location=""):
    """A gate flag must be a JSON boolean. The string "false" is truthy in every naive
    check and has defeated a real independence gate — validate by TYPE, never by truth."""
    v = (container or {}).get(key) if isinstance(container, dict) else None
    if not isinstance(v, bool):
        crit(check, location or key,
             f"{key} is {type(v).__name__} {v!r}, not a JSON boolean",
             'emit true/false unquoted; the string "false" is truthy and passes naive checks')
        return None
    return v


def contract_era(manifest):
    """L12: which contract governs this session? A missing or non-string value falls back to
    THIS validator's CONTRACT_VERSION, so era-gated rules stay ARMED rather than disarmed —
    a stale value once turned off a whole release's enforcement. Gate an era-specific rule
    with `if contract_era(manifest) >= "<x>_skill.1.4":`; never with
    `if manifest.get("session_contract_version") >= ...`, which is None-safe in the wrong
    direction. The value is also written into the report so a reader can tell a contract
    upgrade from a quality gap."""
    v = (manifest or {}).get("session_contract_version")
    return v if isinstance(v, str) and v else CONTRACT_VERSION


def stamped(rec, check):
    """L12: every artifact carries generated_by; validators use it to tell contract
    upgrades (old artifact, new rules) from quality gaps (bad artifact)."""
    if rec is None:
        return
    g = rec.get("generated_by")
    if g is None:
        warn(check, "generated_by", "artifact predates contract stamping",
             "possible contract upgrade, not a quality gap — see the amendment path")
    elif not isinstance(g, str) or not g.strip():
        crit(check, "generated_by", f"generated_by is {type(g).__name__} {g!r}, not a "
             f"non-empty identity string", "stamp it with the drafter name and version")


# ---------- distribution helper (L11: repetition defeats totals) ----------

def repetition_ratio(text):
    """Share of the most-repeated sentence. One sentence x54 once passed a 98%
    word-count band — check variance, not just sums. Tune the threshold per artifact."""
    sents = [s.strip().lower() for s in re.split(r"[.!?]\s+", text) if len(s.strip()) > 20]
    if len(sents) < 5:
        return 0.0
    return max(sents.count(s) for s in set(sents)) / len(sents)


# ---------- CHECKS — replace samples with the architecture item-11 list ----------
# Each check takes (session: Path, manifest: dict), calls checked() for what it examined,
# and crit()/warn() for what it found. Write per-id bindings, not count matches: "3 activity
# slides exist" proves nothing about WHICH activities were materialized (posed 1.27.1).
#
# The samples below are RUNNABLE against the toy schema documented in each docstring, not
# comment sketches — a sketch an author forgets to fill in validates nothing while reporting
# success. Replace them, and delete this marker line as you do:
SAMPLES_PRESENT = True   # the generated lint errors if a shipped validator still sets this

FORBIDDEN = ("ANSWER KEY", "TODO:", "<!-- internal")


def check_required_structure(session, manifest):
    """SAMPLE: the artifact exists, is an object, and every item carries a non-empty id.
    Toy schema: ARTIFACT.json = {"items": [{"id": ..., "upstream_ref": ..., "text": ...}]}"""
    rec = require_record(manifest, "ARTIFACT", "check_required_structure")
    stamped(rec, "check_required_structure")
    require_bool(rec, "reviewed", "check_required_structure", "manifest.artifacts.ARTIFACT.reviewed")
    text = require_file(session, "ARTIFACT.json", "check_required_structure")
    if text is None:
        return
    checked("check_required_structure", session / "ARTIFACT.json")
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return crit("check_required_structure", "ARTIFACT.json", f"unparseable JSON ({e})",
                    "regenerate via the owning stage")
    items = data.get("items") if isinstance(data, dict) else None
    if not isinstance(items, list) or not items:
        return crit("check_required_structure", "ARTIFACT.json", "no non-empty 'items' array",
                    "the drafter emits one row per planned unit")
    for i, it in enumerate(items, 1):
        if not isinstance(it, dict) or not str(it.get("id", "")).strip():
            crit("check_required_structure", f"ARTIFACT.json items[{i}]", "item has no id",
                 "ids are what every downstream binding cites; generate them, never infer")


def check_upstream_coverage(session, manifest):
    """SAMPLE: every upstream id is bound BY ID in this artifact, or carries a declared
    exception. Count matches are not coverage — bind ids, always."""
    up = require_record(manifest, "upstream", "check_upstream_coverage")
    if up is None:
        return
    checked("check_upstream_coverage", "manifest.artifacts.upstream")
    planned = [str(x) for x in up.get("items", []) if str(x).strip()]
    if not planned:
        return crit("check_upstream_coverage", "manifest.artifacts.upstream.items",
                    "upstream record names no items — nothing to bind against",
                    "an empty upstream contract cannot be satisfied; re-run the owning stage")
    try:
        data = json.loads((session / "ARTIFACT.json").read_text())
        bound = {str(it.get("upstream_ref")) for it in data.get("items", [])
                 if isinstance(it, dict)}
        declared = {str(x) for x in data.get("declared_exceptions", [])}
    except (OSError, json.JSONDecodeError):
        return  # check_required_structure already reported this file
    for pid in planned:
        if pid not in bound and pid not in declared:
            crit("check_upstream_coverage", f"upstream:{pid}", "planned item is unbound",
                 "add upstream_ref: %s or a declared exception; structural gaps route to "
                 "the owning upstream step (targeted amendment), never drafter patch-arounds"
                 % pid)


def check_forbidden_markers(session, manifest):
    """SAMPLE: markers that must never reach this artifact (authoring deixis in
    student-facing text, metadata rendered as content, answer keys in the student form)."""
    text = require_file(session, "ARTIFACT.json", "check_forbidden_markers")
    if text is None:
        return
    checked("check_forbidden_markers", session / "ARTIFACT.json")
    for n, line in enumerate(text.splitlines(), 1):
        for marker in FORBIDDEN:
            if marker in line:
                crit("check_forbidden_markers", f"ARTIFACT.json:{n}",
                     f"forbidden marker {marker!r} in a student-facing artifact",
                     "remove it at the drafter, not by post-editing the output")


CHECKS = [check_required_structure, check_upstream_coverage, check_forbidden_markers]

# ---------- runner (do not edit below when instantiating) ----------


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__.split("\n\n")[0]); sys.exit(2)
    session = pathlib.Path(args[0])
    if "--report" in args:
        i = args.index("--report") + 1
        if i >= len(args):
            print("validate_ARTIFACT: --report given with no path — fail closed"); sys.exit(2)
        report_path = pathlib.Path(args[i])
    else:
        report_path = session / "review_logs" / "ARTIFACT_validation.json"
    try:
        manifest = json.loads((session / "manifest.json").read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"validate_ARTIFACT: cannot read manifest ({e}) — fail closed"); sys.exit(2)
    if not isinstance(manifest, dict):
        print(f"validate_ARTIFACT: manifest is {type(manifest).__name__}, not an object — "
              f"fail closed"); sys.exit(2)

    if not CHECKS:
        print("validate_ARTIFACT: CHECKS is empty — nothing was validated, fail closed. "
              "An author mid-instantiation must not be able to emit passed:true.")
        sys.exit(2)

    for check in CHECKS:
        try:
            check(session, manifest)
        except Exception as e:  # a crashing check is a failing check, never a skipped one
            crit(check.__name__, "validator", f"check crashed: {e!r}",
                 "fix the validator; a crash must not pass the gate")

    # A check that finished with neither evidence nor a finding did not run. This is what
    # catches a comment-only body, an early `return` before any work, and a check whose own
    # try/except swallowed everything — all of which otherwise report a clean pass.
    _ran = {c for c, _ in evidence} | {f["check"] for f in findings}
    for check in CHECKS:
        if check.__name__ not in _ran:
            crit(check.__name__, "validator", "check produced no evidence and no finding — "
                 "treated as NOT RUN", "call checked(<name>, <what you examined>) in the "
                 "body, or delete the check; an unrun check must never read as a pass")

    crits = [f for f in findings if f["severity"] == "critical"]
    report = {"validator": "validate_ARTIFACT", "contract_version": contract_era(manifest),
              "session": str(session), "passed": not crits,
              "counts": {"critical": len(crits), "warning": len(findings) - len(crits)},
              "checks_run": sorted(_ran), "evidence": [list(e) for e in evidence],
              "findings": findings}
    try:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n")
    except OSError as e:
        print(f"validate_ARTIFACT: cannot write report to {report_path} ({e}) — fail closed. "
              f"Findings were computed but are unpersisted, so this run did not validate.")
        sys.exit(2)
    for f in findings:
        print(f"{f['severity'].upper():8} [{f['check']}] {f['location']}: {f['issue']}")
    print(f"\nvalidate_ARTIFACT: {len(crits)} critical(s), "
          f"{len(findings) - len(crits)} warning(s) → {report_path}")
    sys.exit(1 if crits else 0)


if __name__ == "__main__":
    main()
