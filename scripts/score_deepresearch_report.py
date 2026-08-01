#!/usr/bin/env python3
"""Score a returned Deep Research report against the run contract.

Perplexity's own Search-as-Code pipeline rejects aggregator URLs with a host predicate in code
rather than by asking the model to prefer good sources
(https://research.perplexity.ai/articles/rethinking-search-as-code-generation). This script is the
same move at our layer: the host test, the verdict-token test and the citation-resolution test run
as code over the returned markdown, so the scorecard in
docs/METHOD_deep_research_orchestration_v1.md is computed rather than judged.

    python3 scripts/score_deepresearch_report.py docs/deepresearch_runs/RETURN_A.md --profile academic

What it CANNOT check, and never claims to: whether the quoted sentence actually appears on the page
at the reported URL. That requires fetching the page and is a human or agent step. The scorecard
reports it as an open item rather than passing it silently.
"""
import argparse
import pathlib
import re
import sys
from urllib.parse import urlparse

SCOPE_VERDICTS = {"scope-accurate", "scope-too-broad", "scope-too-narrow",
                  "superseded", "contested", "unverified"}
STATUS_VERDICTS = {"current", "not-current", "unverified"}

# Positive predicates, one per run profile: the analogue of official_vendor_advisory(url, vendor).
# A host matches if it equals an entry or ends with "." + entry.
ALLOW = {
    "academic": [
        "eric.ed.gov", "files.eric.ed.gov", "ncbi.nlm.nih.gov", "pmc.ncbi.nlm.nih.gov",
        "arxiv.org", "doi.org", "jstor.org", "nature.com", "science.org", "apa.org",
        "psycnet.apa.org", "springer.com", "link.springer.com", "wiley.com",
        "onlinelibrary.wiley.com", "sciencedirect.com", "tandfonline.com", "sagepub.com",
        "journals.sagepub.com", "frontiersin.org", "plos.org", "journals.plos.org",
        "acs.org", "pubs.acs.org", "acm.org", "dl.acm.org", "ieee.org", "ieeexplore.ieee.org",
        "edu", "ac.uk", "edu.au", "oup.com", "academic.oup.com", "cambridge.org", "routledge.com",
        "herdsa.org.au", "ascd.org", "files.ascd.org", "cast.org", "udlguidelines.cast.org",
    ],
    "tooling": [
        "github.com", "raw.githubusercontent.com", "githubusercontent.com",
        "docs.claude.com", "anthropic.com", "claude.com", "npmjs.com", "pypi.org",
    ],
    "standards": [
        "ieee.org", "standards.ieee.org", "ieeexplore.ieee.org", "w3.org", "www.w3.org",
        "nist.gov", "csrc.nist.gov", "iso.org", "ansi.org",
    ],
}

# Named failure classes from the 2026-07-31 deep-research return. Naming the specific error a guard
# expects is lesson L8; "use good sources" is not testable, these are.
DENY = {
    "intertekinform.com": "document reseller product listing, not the issuing body",
    "techstreet.com": "document reseller",
    "scispace.com": "paper aggregator, not the publisher",
    "researchgate.net": "upload aggregator",
    "academia.edu": "upload aggregator",
    "semanticscholar.org": "index, acceptable only for an abstract and only if said so",
    "internationalinsurance.org": "unrelated SEO-farm PDF host",
    "orangeslices.ai": "contract-award trade blog",
    "speakingppt.com": "personal blog review",
    "andrewpwheeler.com": "personal blog review",
    "accesstive.com": "accessibility-vendor marketing blog",
    "a11yflow.dev": "vendor blog",
    "bettera.co": "vendor blog",
}
DENY_SUFFIX = {".rip": "mirror domain, not the issuing agency"}

URL_RE = re.compile(r"https?://[^\s)\]<>\"|]+")
FOOTREF_RE = re.compile(r"\[\^([A-Za-z0-9_-]+)\]")
FOOTDEF_RE = re.compile(r"^\[\^([A-Za-z0-9_-]+)\]:\s*(.+)$", re.M)
# Titles routinely contain brackets ("[PDF] Journal of ..."), so match the first URL on the line
# rather than a well-formed link; a strict link pattern silently drops those references, which
# reads as "no mismatch found" when the truth is "the reference was never parsed".
NUMREF_RE = re.compile(r"^\s*(\d+)\.\s+.*?\((https?://[^)\s]+)\)", re.M)


def host_of(url):
    h = (urlparse(url).hostname or "").lower()
    return h[4:] if h.startswith("www.") else h


def norm(url):
    """Compare URLs by identity of the document, not by host: the observed failure was a footnote
    pointing at a different PDF on the same host."""
    u = url.strip().rstrip(".,;)").lower()
    return re.sub(r"^https?://(www\.)?", "", u).rstrip("/")


def matches(host, entries):
    return any(host == e or host.endswith("." + e) for e in entries)


def classify(url, profile):
    host = host_of(url)
    if not host:
        return "malformed", "not a parseable URL"
    for suffix, why in DENY_SUFFIX.items():
        if host.endswith(suffix):
            return "rejected", why
    for bad, why in DENY.items():
        if host == bad or host.endswith("." + bad):
            return "rejected", why
    if matches(host, ALLOW.get(profile, [])):
        return "allowed", ""
    return "unlisted", "not on the profile allowlist — needs a human call"


def table_rows(text):
    """Body rows of pipe tables, minus header and separator lines."""
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if not (s.startswith("|") and s.count("|") >= 3):
            continue
        if re.fullmatch(r"\|[\s:|-]+\|", s):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if cells and cells[0].lower() in {"#", "no", "item"}:
            continue
        rows.append((s, cells))
    return rows


def footnote_map(text):
    m = {k: v for k, v in FOOTDEF_RE.findall(text)}
    for num, url in NUMREF_RE.findall(text):
        m.setdefault(num, url)
    return m


def main():
    p = argparse.ArgumentParser()
    p.add_argument("report", type=pathlib.Path)
    p.add_argument("--profile", choices=sorted(ALLOW), default="academic")
    p.add_argument("--expect-rows", type=int, default=0,
                   help="number of items assigned to this run; 0 skips the coverage test")
    p.add_argument("--status-run", action="store_true",
                   help="score against the status verdict set instead of the scope set")
    args = p.parse_args()

    if not args.report.exists():
        sys.exit(f"no such report: {args.report}")
    text = args.report.read_text(encoding="utf-8")
    rows = table_rows(text)
    notes = footnote_map(text)
    legal = STATUS_VERDICTS if args.status_run else SCOPE_VERDICTS

    failures, unlisted, bad_tokens, unresolved = [], [], [], []
    row_urls = 0

    for raw, cells in rows:
        urls = URL_RE.findall(raw)
        row_urls += len(urls)
        for u in urls:
            verdict, why = classify(u, args.profile)
            if verdict == "rejected":
                failures.append((host_of(u), why))
            elif verdict == "unlisted":
                unlisted.append((host_of(u), why))

        # Verdict token: the closed set, nothing appended.
        if not any(c.strip().strip("`*").lower() in legal for c in cells):
            found = [c for c in cells if any(v in c.lower() for v in legal)]
            bad_tokens.append(found[0][:70] if found else raw[:70])

        # Citation resolution. A row may legitimately carry an extra corroborating footnote, so the
        # test is not "every footnote matches" but "at least one footnote target is the document the
        # row itself cites". A row where none of them agree is the D4/D5 failure: the visible URL and
        # the reference apparatus point at different documents, and the reader cannot tell which
        # carries the quote.
        refs = FOOTREF_RE.findall(raw)
        if refs and urls:
            targets, missing = [], []
            for ref in refs:
                target = notes.get(ref)
                if target is None:
                    missing.append(ref)
                else:
                    targets.extend(URL_RE.findall(target))
            for ref in missing:
                unresolved.append(f"[^{ref}] has no definition")
            if targets and not ({norm(t) for t in targets} & {norm(u) for u in urls}):
                unresolved.append(
                    f"row cites {urls[0]} but its footnote(s) resolve to {targets[0]}"
                    + (f" (+{len(targets) - 1} more)" if len(targets) > 1 else ""))

    print(f"report            : {args.report}")
    print(f"profile           : {args.profile}")
    print(f"rows parsed       : {len(rows)}"
          + (f" of {args.expect_rows} expected" if args.expect_rows else ""))
    print(f"URLs in rows      : {row_urls}")
    print(f"rejected hosts    : {len(failures)}")
    for h, why in sorted(set(failures)):
        print(f"    REJECT {h} — {why}")
    print(f"unlisted hosts    : {len(set(unlisted))}")
    for h, why in sorted(set(unlisted)):
        print(f"    CHECK  {h} — {why}")
    print(f"illegal verdicts  : {len(bad_tokens)}")
    for t in bad_tokens:
        print(f"    TOKEN  {t}")
    print(f"citation mismatch : {len(unresolved)}")
    for t in unresolved:
        print(f"    CITE   {t}")
    print("open item         : quote-hosted-at-URL is NOT checked here; verify by hand on a sample")

    short = args.expect_rows and len(rows) < args.expect_rows
    fail = bool(failures or bad_tokens or unresolved or short)
    if short:
        print(f"\nFAIL: {args.expect_rows - len(rows)} row(s) missing")
    print("\nRESULT:", "FAIL" if fail else "PASS (mechanical checks only)")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
