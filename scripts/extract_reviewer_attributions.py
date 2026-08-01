#!/usr/bin/env python3
"""Extract candidate reviewer-attributed concerns from a change-request corpus.

Emits a TSV coding sheet, one row per line that names at least one reviewer, with the set of
reviewers named on that line. A line is a CANDIDATE concern, not a concern: prose that merely
mentions a reviewer is included and must be coded out by hand. The script measures the corpus,
it does not interpret it.

Usage:  extract_reviewer_attributions.py <docs-dir> [<docs-dir> ...]

Why lines and not paragraphs: this corpus records folded findings one per numbered list item, so a
line is the unit that carries an attribution. Where a concern spans two lines the second carries no
attribution and is dropped, which UNDERCOUNTS multi-line concerns. Stated rather than hidden; the
hand-coding pass is where that is repaired.
"""
import pathlib, re, sys, collections

REVIEWERS = ("Grok", "Codex", "Fable", "Opus")
# Word-boundary match: "Codexes" or a path fragment should not count.
PATTERNS = {r: re.compile(rf"\b{r}\b") for r in REVIEWERS}
# A CR id in the filename, when there is one. Files without one still emit rows, marked "-".
CR_ID = re.compile(r"CR_(\d+\.\d+(?:\.\d+)?)")


def scan(paths):
    rows, per_file = [], collections.Counter()
    for d in paths:
        for p in sorted(pathlib.Path(d).rglob("*.md")):
            if ".git" in p.parts or "worktrees" in p.parts:
                continue
            m = CR_ID.search(p.name)
            cr = m.group(1) if m else "-"
            for i, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
                named = sorted(r for r, pat in PATTERNS.items() if pat.search(line))
                if not named:
                    continue
                rows.append((cr, p.name, i, len(named), "+".join(named),
                             " ".join(line.split())[:300]))
                per_file[p.name] += 1
    return rows, per_file


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    rows, per_file = scan(sys.argv[1:])
    print("cr\tfile\tline\tn_reviewers\treviewers\ttext")
    for r in rows:
        print("\t".join(str(x) for x in r))

    multi = [r for r in rows if r[3] >= 2]
    combos = collections.Counter(r[4] for r in multi)
    crs = {r[0] for r in rows if r[0] != "-"}
    sys.stderr.write(
        f"\ncandidate attribution lines : {len(rows)}\n"
        f"  naming one reviewer        : {len(rows) - len(multi)}\n"
        f"  naming two or more         : {len(multi)}\n"
        f"distinct CR ids touched      : {len(crs)}\n"
        f"files with any attribution   : {len(per_file)}\n"
        f"co-attribution combinations  : {dict(combos.most_common())}\n"
        "\nEvery row is a CANDIDATE. Prose mentioning a reviewer is included by design;\n"
        "the hand-coding pass decides which rows are concerns and merges duplicates.\n")


if __name__ == "__main__":
    main()
