#!/usr/bin/env python3
"""Link the personal skill directories to this repo so both harnesses edit one source.

Creates:
    ~/.claude/skills/page-<x>  ->  <repo>/skills/<x>
    ~/.codex/skills/page-<x>   ->  <repo>/skills/<x>

The Claude/Codex personal dirs use the "page-" prefix; the repo drops it for most skills
(the plugin namespace re-adds it). Exception kept as-is: `page` (the umbrella keeps its full name).

Idempotent: an existing correct symlink is left alone. A real directory in the way is moved
to <backup-root>/<tool>/ (default ~/page-prefork-backup-<timestamp>) before linking, so the
operation is always reversible. Run with --dry-run to preview.
"""
import argparse, os, glob, shutil, datetime

KEEP_NAME = {"page"}   # repo dir == personal dir
SKIP = set()                            # stays a real dir (node_modules)


def repo_target(repo_skills, pdir):
    if pdir in KEEP_NAME:
        cand = pdir
    else:
        cand = pdir[len("page-"):] if pdir.startswith("page-") else pdir
    return cand if os.path.isdir(os.path.join(repo_skills, cand)) else None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    default_repo = os.path.dirname(here)  # repo root (scripts/..)
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=default_repo, help="Path to the page repo root")
    ap.add_argument("--trees", nargs="+",
                    default=[os.path.expanduser("~/.claude/skills"),
                             os.path.expanduser("~/.codex/skills")])
    ap.add_argument("--backup-root",
                    default=os.path.expanduser(
                        "~/page-prefork-backup-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    repo_skills = os.path.join(args.repo, "skills")
    if not os.path.isdir(repo_skills):
        ap.error(f"no skills/ under {args.repo}")

    # Every page skill that exists in the repo (so a fresh machine gets them all).
    repo_dirs = sorted(d for d in os.listdir(repo_skills)
                       if os.path.isdir(os.path.join(repo_skills, d)))
    personal_names = sorted({("page" if d == "page" else
                              d if d.startswith("page-") else "page-" + d)
                             for d in repo_dirs})

    for tree in args.trees:
        os.makedirs(tree, exist_ok=True)
        for pdir in personal_names:
            if pdir in SKIP:
                continue
            tgt = repo_target(repo_skills, pdir)
            if not tgt:
                print(f"  [skip] {pdir}: no repo target"); continue
            link = os.path.join(tree, pdir)
            dest = os.path.join(repo_skills, tgt)
            if os.path.islink(link) and os.path.realpath(link) == os.path.realpath(dest):
                continue  # already correct
            if args.dry_run:
                print(f"  [dry] {link} -> {dest}"); continue
            if os.path.exists(link) or os.path.islink(link):
                bk = os.path.join(args.backup_root, os.path.basename(tree.rstrip("/")))
                os.makedirs(bk, exist_ok=True)
                shutil.move(link, os.path.join(bk, pdir))
            os.symlink(dest, link)
            print(f"  linked {link} -> {dest}")
    print("done" + (" (dry run)" if args.dry_run else f"; backups under {args.backup_root}"))


if __name__ == "__main__":
    main()
