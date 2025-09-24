#!/usr/bin/env python3
'''CLI program to turn unimorph data to lexc format with giellalt tags.'''
import sys
from argparse import ArgumentParser, FileType

from .lexc import print_lexc_preamble
from .tagmaps import unimorph2giella


def main():
    '''Minimal CLI for unimorph2lexc.'''
    ap = ArgumentParser()
    ap.add_argument("-i", "--input", metavar="INFILE", type=open,
                    dest="infile", help="read unimorph data from INFILE")
    ap.add_argument("-L", "--lexc", metavar="LEXCFILE", type=FileType("w"),
                    dest="lexcfile", help="write lexc to LEXCFILE")
    ap.add_argument("-v", "--verbose", action="store_true", default=False,
                    help="print verbosely while processing")
    opts = ap.parse_args()
    if not opts.lexcfile:
        opts.lexcfile = sys.stdout
        print("Writing to <stdout>", file=sys.stderr)
    if not opts.infile:
        opts.infile = sys.stdin
        print("Reading from <stdin>", file=sys.stderr)
    print_lexc_preamble(opts.lexcfile)
    lemmas = 0
    tokens = 0
    suspicious = 0
    prevlemma = None
    for line in opts.infile:
        if not line or line.strip() == '':
            print(file=opts.lexcfile)
            continue
        # gravitáció      gravitáción     N;ON+ESS;SG
        fields = line.strip().split('\t')
        tokens += 1
        if len(fields) != 3:
            print('Datoissa virhe!', fields)
            sys.exit(1)
        elif fields[0] == '----' and fields[1] == '----' and\
                fields[2] == '----':
            # this is the kind bs that unimorph is full of
            suspicious += 1
            continue
        lemma = fields[0]
        surf = fields[1]
        unimorphs = fields[2]
        if lemma != prevlemma:
            prevlemma = lemma
            print()
            lemmas += 1
        if 'intransitive verb' in surf:
            suspicious += 1
        elif 'subjunctive forms' in surf:
            suspicious += 1
        elif '|' in surf:
            suspicious += 1
        giellatags = unimorph2giella(unimorphs)
        print(lemma, ''.join(giellatags), ':', surf,
              "\t#\t;", sep='', file=opts.lexcfile)


if __name__ == '__main__':
    main()
