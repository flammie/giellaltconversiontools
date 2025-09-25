#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert output of hfst-fst2strings of a generator to unimorph.
"""


import sys
from argparse import ArgumentParser, FileType
from sys import stderr, stdin, stdout
from time import perf_counter, process_time

from .unimorph import giella2unimorph


def main():
    """CLI for giella2unimorph converter."""
    a = ArgumentParser()
    a.add_argument('-i', '--input', metavar='INFILE', type=open,
                   dest='infile', help='source of analysis data')
    a.add_argument('-o', '--output', metavar='OUTFILE',
                   type=FileType('w'),
                   dest='outfile', help='log outputs to OUTFILE')
    a.add_argument('-v', '--verbose', action='store_true', default=False,
                   help='Print verbosely while processing')
    a.add_argument('-C', '--no-casing', action='store_true', default=False,
                   help='Do not try to recase input and output when matching')
    a.add_argument('-t', '--threshold', metavar='THOLD', default=99,
                   help='if coverage is less than THOLD exit with error')
    a.add_argument('-I', '--include-specs', metavar='INCSPEC',
                   help='include INCSPEC in generated data',
                   action='append', choices=['lgspec', 'typo', 'xxx', 'dial'])
    options = a.parse_args()
    if not options.infile:
        options.infile = stdin
        print('reading from <stdin>')
    if not options.outfile:
        options.outfile = stdout
    lines = 0
    # for make check target
    realstart = perf_counter()
    cpustart = process_time()
    skip_lgspec = True
    skip_typo = True
    skip_xxx = True
    skip_dial = True
    if options.include_specs:
        for inclusive in options.include_specs:
            if inclusive == 'lgspec':
                skip_lgspec = False
            elif inclusive == 'typo':
                skip_typo = False
            elif inclusive == 'xxx':
                skip_xxx = False
            elif inclusive == 'dial':
                skip_dial = False
    for line in options.infile:
        fields = line.strip().split(':')
        if line.strip() == '':
            continue
        if len(fields) < 2:
            print('ERROR: Skipping line', fields, file=stderr)
            continue
        if ' ' in fields[1] or ' ' in fields[0]:
            continue
        lines += 1
        if options.verbose and lines % 1000 == 0:
            print(lines, '...')
        giella = fields[0]
        lemma = giella.split('+')[0]
        giellatags = giella[giella.find('+'):]
        surf = fields[1]
        unimorph = giella2unimorph(giellatags)
        if skip_lgspec and 'LGSPEC' in unimorph:
            continue
        if skip_typo and 'TYPO' in unimorph:
            continue
        if skip_xxx and 'XXX' in unimorph:
            continue
        if skip_dial and 'DIAL' in unimorph:
            continue
        print(lemma, surf, unimorph, sep='\t', file=options.outfile)
    realend = perf_counter()
    cpuend = process_time()
    print('CPU time:', cpuend - cpustart, 'real time:', realend - realstart)
    sys.exit(0)


if __name__ == '__main__':
    main()
