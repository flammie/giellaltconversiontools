#!/usr/bin/env python3
'''CLI program to turn unimorph data to GiellaLT.'''
import sys

from .tagmaps import unimorph2giella


def main():
    '''CLI for unimorph2fst.'''
    lemmas = 0
    tokens = 0
    suspicious = 0
    for line in sys.stdin:
        if not line or line.strip() == '':
            print()
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
        if 'intransitive verb' in surf:
            suspicious += 1
        elif 'subjunctive forms' in surf:
            suspicious += 1
        elif '|' in surf:
            suspicious += 1
        giellatags = unimorph2giella(unimorphs)
        print(surf, '\t', lemma, ''.join(giellatags), sep='')

    print()
    print('# tokens\tlemmas\tsuspicious')
    print('# ', tokens, '\t', lemmas, '\t', suspicious, sep='')
    print('# ', tokens / tokens * 100, '\t',
          lemmas / tokens * 100, '\t',
          suspicious / tokens * 100, '\t', sep='')


if __name__ == '__main__':
    main()
