#!/usr/bin/env -o python3
"""Script to convert ud to giellalt stuffs."""

import sys
from argparse import ArgumentParser, FileType

from .lexc import lexc_escape, print_lexc_preamble
from .tagmaps import ud2giella


def main():
    """CLI for UD to gielalt confersion."""
    ap = ArgumentParser()
    ap.add_argument("-i", "--input", metavar="INFILE", type=open,
                    dest="infile", help="read CONLL-U data from INFILE")
    ap.add_argument("-L", "--lexc", metavar="LEXCFILE", type=FileType("w"),
                    dest="lexcfile", help="write lexc to LEXCFILE",
                    required=True)
    ap.add_argument("-v", "--verbose", action="store_true", default=False,
                    help="print verbosely while processing")
    opts = ap.parse_args()
    if not opts.infile:
        opts.infile = sys.stdin
        print("reading from <stdin>")
    print_lexc_preamble(opts.lexcfile)
    for line in opts.infile:
        if line.startswith("#"):
            continue
        elif line.strip() == "":
            continue
        fields = line.rstrip("\n").split("\t")
        if len(fields) != 10:
            print("Datoissa virhe {len(fields)} != 10:", fields)
            continue
        position = fields[0]
        surf = fields[1]
        lemma = fields[2]
        upos = fields[3]
        xpos = fields[4]
        feats = fields[5]
        deptarget = fields[6]
        depname = fields[7]
        endeps = fields[8]
        misc = fields[9]
        giellatags = ud2giella(lemma, upos, xpos, feats)
        lexclemma = lexc_escape(lemma)
        lexctags = lexc_escape("".join(giellatags))
        lexcsurf = lexc_escape(surf)
        print(f"{lexclemma}{lexctags}:{lexcsurf}  # ;", file=opts.lexcfile)



if __name__ == "__main__":
    main()
