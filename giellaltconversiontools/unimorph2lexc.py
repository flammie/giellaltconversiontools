#!/usr/bin/env python3
'''CLI program to turn unimorph data to GiellaLT morph tester yaml.'''
import sys

from .tagmaps import unimorph2giella


def main():
    '''Minimal CLI for unimorph2lexc.'''
    print('Multichar_Symbols')
    print('+N +A +V')
    print('+Sg +Pl +Du')
    print('+Nom +Acc +Dat +Gen +Loc +Ine +Ill +Abl +Lat +Ela')
    print('+Com +Abe +Tra +Ins +Ess')
    print('+Prs +Prt +Ind +Pot +Cond +Imprt')
    print('+Sg1 +Sg2 +Sg3 +Du1 +Du2 +Du3 +Pl1 +Pl2 +Pl3')
    lemmas = 0
    tokens = 0
    suspicious = 0
    prevlemma = None
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
        print(lemma, ''.join(giellatags), ':', surf, sep='')



if __name__ == '__main__':
    main()
