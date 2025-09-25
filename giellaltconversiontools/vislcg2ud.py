#!/usr/bin/env python3
"""Simple converter from giellalt deps to universal deps."""

import sys
from argparse import ArgumentParser, FileType

from .ud import get_dep, get_ufeats, get_upos, get_xpos


def print_sent(sent: list, sent_id: str, orig: str, outfile):
    """Print CONLL-U format for single sentence."""
    print(f"# sent_id = {sent_id}", file=outfile)
    print(f"# text = {orig}", file=outfile)
    for i, token in enumerate(sent):
        for cohort in token:
            print(i+1, cohort["surf"], cohort["lemma"], cohort["upos"],
                  cohort["xpos"], cohort["feats"],
                  cohort["depto"], cohort["dep"], "_", sep="\t", file=outfile)


def main():
    """CLI for giellalt to ud conversion."""
    ap = ArgumentParser()
    ap.add_argument("-i", "--input", metavar="INFILE", type=open,
                    dest="infile", help="read vislcg3 data from INFILE")
    ap.add_argument("-o", "--output", metavar="OUTFILE", type=FileType("w"),
                    dest="outfile", help="write UD to OUTFILE")
    ap.add_argument("-v", "--verbose", action="store_true", default=False,
                    help="print verbosely while processing")
    opts = ap.parse_args()
    if not opts.infile:
        opts.infile = sys.stdin
        print("reading from <stdin>")
    if not opts.outfile:
        opts.outfile = sys.stdout
    sent = []
    cohorts = []
    orig = ""
    sentnum = 1
    sentprinted = True
    for line in opts.infile:
        if line.startswith("\"<") and line.strip().endswith(">\""):
            if "¶" in line:
                continue
            if cohorts:
                sent.append(cohorts)
                cohorts = []
            surf = line[2:-3]
            orig = orig + surf
            sentprinted = False
        elif line.startswith("\t") and line.count("\"") == 2:
            if "¶" in line:
                continue
            if "#1->" in line and not sentprinted:
                if cohorts:
                    sent.append(cohorts)
                    cohorts = []
                orig = orig[:-len(surf)]  # cause we already peeked it
                print_sent(sent, opts.infile.name + "." + str(sentnum), orig,
                           opts.outfile)
                sentnum = sentnum + 1
                sent = []
                orig = surf  # cause we already read one surf
                sentprinted = True
            elif "#1->" in line:
                pass
            elif "#" in line and "->" in line:
                sentprinted = False
            lemstart = line.find("\"")
            lemend = line.find("\"", lemstart+1)
            lemma = line[lemstart+1:lemend]
            tags = line.rstrip()[lemend+1:].split()
            upos = get_upos(tags, lemma, surf)
            xpos = get_xpos(tags, lemma, surf)
            feats = get_ufeats(tags, lemma, surf)
            dep, deptarget = get_dep(tags, lemma, surf)
            cohorts.append({"surf": surf, "lemma": lemma, "tags": tags,
                            "suggested": True, "upos": upos, "xpos": xpos,
                            "feats": feats, "dep": dep,
                            "depto": deptarget})
        elif line.startswith(";\t") and line.count("\"") == 2:
            if "¶" in line:
                continue
            lemstart = line.find("\"")
            lemend = line.find("\"", lemstart+1)
            lemma = line[lemstart+1:lemend]
            tags = line.rstrip()[lemend+1:].split()
            upos = get_upos(tags, lemma, surf)
            xpos = get_xpos(tags, lemma, surf)
            feats = get_ufeats(tags, lemma, surf)
            dep, deptarget = get_dep(tags, lemma, surf)
            cohorts.append({"surf": surf, "lemma": lemma, "tags": tags,
                            "suggested": False, "upos": upos, "xpos": xpos,
                            "feats": feats, "dep": dep,
                            "depto": deptarget})
        elif line.startswith("\t\"\"\""):
            if "¶" in line:
                continue
            lemma = "\""
            tags = line.rstrip()[5:].split()
            upos = get_upos(tags, lemma, surf)
            xpos = get_xpos(tags, lemma, surf)
            feats = get_ufeats(tags, lemma, surf)
            dep, deptarget = get_dep(tags, lemma, surf)
            cohorts.append({"surf": surf, "lemma": lemma, "tags": tags,
                            "suggested": False, "upos": upos, "xpos": xpos,
                            "feats": feats, "dep": dep,
                            "depto": deptarget})
        elif line.startswith(":\\n"):
            if cohorts:
                sent.append(cohorts)
                cohorts = []
            print_sent(sent, opts.infile.name + "." + str(sentnum), orig,
                       opts.outfile)
            sentnum = sentnum + 1
            sent = []
            orig = ""
        elif line.startswith(";\t") and line.count("\"") == 4:
            # FIXME: tokeniser split
            continue
        elif line.startswith(":"):
            orig = orig + line[1:-1]  # or rstrip(\n) like
        elif line.strip() == "":
            continue
        else:
            print(f"some garbage data here: {line}")
    if cohorts:
        sent.append(cohorts)
    print_sent(sent, opts.infile.name + "." + str(sentnum), orig, opts.outfile)


if __name__ == "__main__":
    main()
