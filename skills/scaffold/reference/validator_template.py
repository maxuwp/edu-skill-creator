#!/usr/bin/env python3
"""validate_ARTIFACT.py — computed structural validator (Edu Skill Creator L11 template).

`edu-skill-creator-scaffold` instantiates ONE copy of this template per artifact named
in the architecture's computed-validation plan (architecture item 11): replace ARTIFACT,
fill in CHECKS, delete the sample bodies. Everything import-free and self-contained on
purpose — a validator with dependencies is a validator someone will skip.

Why this exists (L11, lessons_learned.md): prose contracts rot. A POSED pilot deck
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

FIXTURES (release lint runs these pairs; falsifiability, L8/L11)
  tests/fixtures/ARTIFACT_fail/   — expected exit 1; mirrors a REAL observed failure
  tests/fixtures/ARTIFACT_pass/   — expected exit 0; minimal compliant session
Neutralizing the fail fixture must make the release lint itself fail (prove the proof).
Fixtures NEVER contain student/faculty course content — the data posture (intent A.7)
applies to test data too. The generated release_lint.py gets a check like:

    # check N: validator fixture pairs (fail-expected / pass-expected)
    for name, expect in ((\"ARTIFACT_fail\", 1), (\"ARTIFACT_pass\", 0)):
        rc = subprocess.run([sys.executable, \"skills/<x>/scripts/validate_ARTIFACT.py\",
                             f\"tests/fixtures/{name}\"], capture_output=True).returncode
        if rc != expect:
            errors.append(f\"[fixtures] {name}: exit {rc}, expected {expect}\")
"""
import json, pathlib, re, sys

# Keep equal to the plugin's current release; the generated lint checks the match.
CONTRACT_VERSION = "<x>_skill.0.1"

findings = []


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


def contract_era(manifest):
    """L12: which contract governs this session? Missing or unknown version = checks
    ARMED (fail closed) — a stale value once disarmed a whole release's enforcement."""
    v = (manifest or {}).get("session_contract_version")
    return v if isinstance(v, str) and v else CONTRACT_VERSION


def stamped(rec, check):
    """L12: every artifact carries generated_by; validators use it to tell contract
    upgrades (old artifact, new rules) from quality gaps (bad artifact)."""
    if rec is not None and not rec.get("generated_by"):
        warn(check, "generated_by", "artifact predates contract stamping",
             "possible contract upgrade, not a quality gap — see the amendment path")


# ---------- distribution helper (L11: repetition defeats totals) ----------

def repetition_ratio(text):
    """Share of the most-repeated sentence. One sentence x54 once passed a 98%
    word-count band — check variance, not just sums. Tune the threshold per artifact."""
    sents = [s.strip().lower() for s in re.split(r"[.!?]\s+", text) if len(s.strip()) > 20]
    if len(sents) < 5:
        return 0.0
    return max(sents.count(s) for s in set(sents)) / len(sents)


# ---------- CHECKS — replace samples with the architecture item-11 list ----------
# Each check takes (session: Path, manifest: dict) and calls crit()/warn().
# Write per-id bindings, not count matches: "3 activity slides exist" proves nothing
# about WHICH activities were materialized (posed 1.27.1).

def check_required_structure(session, manifest):
    """SAMPLE: required rows/fields/tags exist in the artifact."""
    text = require_file(session, "ARTIFACT.json", "required_structure")
    if text is None:
        return
    # ... parse; assert required fields per item; cite ids in findings ...


def check_upstream_coverage(session, manifest):
    """SAMPLE: every upstream-contract item is bound BY ID in this artifact
    (e.g. every planned activity id appears as an activity_ref, or carries a
    machine-readable declared exception)."""
    # ... build upstream id set; for each unbound id: crit(..., fix_hint="add
    #     <!-- ..._ref: idN --> or declare an exception; structural gaps route to the
    #     owning upstream step (targeted amendment), never drafter patch-arounds") ...


def check_forbidden_markers(session, manifest):
    """SAMPLE: markers that must never reach this artifact (authoring deixis in
    student-facing text, metadata blocks rendered as content, answer keys in the
    student form...)."""
    # ... scan; each hit is a critical with the exact line ...


CHECKS = [check_required_structure, check_upstream_coverage, check_forbidden_markers]

# ---------- runner (do not edit below when instantiating) ----------


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__.split("\n\n")[0]); sys.exit(2)
    session = pathlib.Path(args[0])
    report_path = (pathlib.Path(args[args.index("--report") + 1]) if "--report" in args
                   else session / "review_logs" / "ARTIFACT_validation.json")
    try:
        manifest = json.loads((session / "manifest.json").read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"validate_ARTIFACT: cannot read manifest ({e}) — fail closed"); sys.exit(2)

    for check in CHECKS:
        try:
            check(session, manifest)
        except Exception as e:  # a crashing check is a failing check, never a skipped one
            crit(check.__name__, "validator", f"check crashed: {e!r}",
                 "fix the validator; a crash must not pass the gate")

    crits = [f for f in findings if f["severity"] == "critical"]
    report = {"validator": "validate_ARTIFACT", "contract_version": contract_era(manifest),
              "session": str(session), "passed": not crits,
              "counts": {"critical": len(crits), "warning": len(findings) - len(crits)},
              "findings": findings}
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n")
    for f in findings:
        print(f"{f['severity'].upper():8} [{f['check']}] {f['location']}: {f['issue']}")
    print(f"\nvalidate_ARTIFACT: {len(crits)} critical(s), "
          f"{len(findings) - len(crits)} warning(s) → {report_path}")
    sys.exit(1 if crits else 0)


if __name__ == "__main__":
    main()
