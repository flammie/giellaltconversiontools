#!/usr/bin/env -O python3
"""Global definitions of simple tag maps and configurations for conversions."""

import sys

IGNORED_GENS = [
    "+",
    "+ABBR",
    "+ACR",
    "+Acr",
    "+Arab",
    "+Coll",
    "+Clt/Add",
    "+Clt/aram",
    "+Clt/Cop",
    "+Cmp",
    "+Cmp#",
    "+Cmp/Hyph-Serial",
    "+Der",
    "+Der/AAdv",
    "+Der/adda",
    "+Der/adte",
    "+Der/Adv",
    "+Der/ahtje",
    "+Der/alla",
    "+Der/allash",
    "+Der/amoš",
    "+Der/Car",
    "+Der/Caus",
    "+Der/d",
    "+Der/dahtte",
    "+Der/dalla",
    "+Der/Dimin",
    "+Der/eamoš",
    "+Der/easti",
    "+Der/f",
    "+Der/geahtes",
    "+Der/h",
    "+Der/halla",
    "+Der/ht",
    "+Der/huhtti",
    "+Der/huvva",
    "+Der/im",
    "+Der/InchL",
    "+Der/ist",
    "+Der/ja",
    "+Der/kas",
    "+Der/keahtta",
    "+Der/l",
    "+Der/laagasj",
    "+Der/laakan",
    "+Der/lane",
    "+Der/las",
    "+Der/lasj",
    "+Der/lazh",
    "+Der/lg",
    "+Der/lik",
    "+Der/line",
    "+Der/m",
    "+Der/mas",
    "+Der/mata",
    "+Der/meahttun",
    "+Der/muš",
    "+Der/musj",
    "+Der/MWN",
    "+Der/N2A",
    "+Der/ne",
    "+Der/nna",
    "+Der/NomAct",
    "+Der/NomAg",
    "+Der/OkshnOms",
    "+Der/oollyd",
    "+Der/oottyd",
    "+Der/OvOms",
    "+Der/PassL",
    "+Der/PassS",
    "+Der/Poss",
    "+Der/r",
    "+Der/sazh",
    "+Der/st",
    "+Der/stahtte",
    "+Der/stalla",
    "+Der/stoollyd",
    "+Der/stoovvyd",
    "+Der/stuvva",
    "+Der/t",
    "+Der/tamatu",
    "+Der/ti",
    "+Der/tOin",
    "+Der/toovvyd",
    "+Der/tt",
    "+Der/tu",
    "+Der/tud",
    "+Der/us",
    "+Der/v",
    "+Der/viđá",
    "+Der/viđi",
    "+Der/vuota",
    "+Dim/ke",
    "+Dyn",
    "+Guess",
    "+Err/DerSub",
    "+Err/MissingSpace",
    "+Err/Orth",
    "+Err/Orth-a-á",
    "+Err/Orth-á-a",
    "+Err/Spellrelax",
    "+Num",
    "+Ord",
    "+Prop",
    "+TODO",
    "+Use/Circ",
    "+Use/GC",
    "+Use/NG",
    "+Use/SpellNoSugg",
    "^BlockCap"
]


def giella2unimorph(tags):
    unimorphtags = []
    for giella in tags.split('+'):
        if giella == '':
            continue
        elif giella == 'N':
            if 'Prop' in tags:
                unimorphtags += ['PROPN']
            else:
                unimorphtags += ['N']
        elif giella == 'Adv':
            unimorphtags += ['ADV']
        elif giella == 'Num':
            unimorphtags += ['NUM']
        elif giella == 'Po':
            unimorphtags += ['ADP']
        elif giella == 'Pr':
            unimorphtags += ['ADP']
        elif giella == 'A':
            unimorphtags += ['ADJ']
        elif giella == 'Interj':
            unimorphtags += ['INTJ']
        elif giella == 'CC':
            unimorphtags += ['CONJ']
        elif giella == 'CS':
            unimorphtags += ['CONJ']
        elif giella == 'Pron':
            unimorphtags += ['PRO']
        elif giella == 'Neu':
            unimorphtags += ['NEUT']
        elif giella == 'Fem':
            unimorphtags += ['FEM']
        elif giella == 'Msc':
            unimorphtags += ['MASC']
        elif giella == 'Common':
            unimorphtags += ['MASC+FEM']
        elif giella == 'Gen':
            unimorphtags += ['GEN']
        elif giella == 'Com':
            unimorphtags += ['COM']
        elif giella == 'Ses':
            unimorphtags += ['ON+ESS']
        elif giella == 'Ess':
            unimorphtags += ['FRML']  # XXX: ESS?
        elif giella == 'Inan':
            unimorphtags += ['INAN']
        elif giella == 'Anim':
            unimorphtags += ['ANIM']
        elif giella == 'Abe':
            unimorphtags += ['PRIV']  # XXX: ABE?
        elif giella == 'Par':
            unimorphtags += ['PRT']
        elif giella == 'Ins':
            unimorphtags += ['INS']
        elif giella == 'Ine':
            unimorphtags += ['IN+ESS']
        elif giella == 'Nom':
            unimorphtags += ['NOM']
        elif giella == 'Sub':
            unimorphtags += ['ON+ALL']
        elif giella == 'All':
            unimorphtags += ['AT+ALL']  # XXX: ALL?
        elif giella == 'Loc':
            unimorphtags += ['PRP']
        elif giella == 'Inst':
            unimorphtags += ['INST']
        elif giella == 'Tra':
            unimorphtags += ['TRANS']
        elif giella == 'Del':
            unimorphtags += ['ON+ABL']
        elif giella == 'Ela':
            unimorphtags += ['IN+ABL']
        elif giella == 'Ill':
            unimorphtags += ['IN+ALL']
        elif giella == 'Dat':
            unimorphtags += ['DAT']
        elif giella == 'Acc':
            unimorphtags += ['ACC']
        elif giella == 'Ade':
            unimorphtags += ['AT+ESS']
        elif giella == 'Abl':
            unimorphtags += ['AT+ABL']
        elif giella == 'Sg':
            unimorphtags += ['SG']
        elif giella == 'Du':
            unimorphtags += ['DU']
        elif giella == 'Pl':
            unimorphtags += ['PL']
        elif giella == 'Indic':
            unimorphtags += ['IND']
        elif giella == 'Ind':
            unimorphtags += ['IND']  # XXX: can sometimes be indef?
        elif giella == 'Prs':
            unimorphtags += ['PRS']
        elif giella == 'Prt':
            unimorphtags += ['PST']
        elif giella == 'Perf':
            unimorphtags += ['PRF']
        elif giella == 'Fut':
            unimorphtags += ['FUT']
        elif giella == 'Sg1':
            unimorphtags += ['1', 'SG']
        elif giella == 'Sg2':
            unimorphtags += ['2', 'SG']
        elif giella == 'Sg3':
            unimorphtags += ['3', 'SG']
        elif giella == 'Du1':
            unimorphtags += ['1', 'DU']
        elif giella == 'Du2':
            unimorphtags += ['2', 'DU']
        elif giella == 'Du3':
            unimorphtags += ['3', 'DU']
        elif giella == 'Pl1':
            unimorphtags += ['1', 'PL']
        elif giella == 'Pl2':
            unimorphtags += ['2', 'PL']
        elif giella == 'Pl3':
            unimorphtags += ['3', 'PL']
        elif giella == '4':
            unimorphtags += ['4']
        elif giella == 'Pe4':
            unimorphtags += ['4']
        elif giella == 'Ips':
            unimorphtags += ['IMPRS']
        elif giella == 'ScSg1':
            unimorphtags += ['ARGNO1S']
        elif giella == 'ScSg2':
            unimorphtags += ['ARGNO2S']
        elif giella == 'ScSg3':
            unimorphtags += ['ARGNO3S']
        elif giella == 'ScPl1':
            unimorphtags += ['ARGNO1S']
        elif giella == 'ScPl2':
            unimorphtags += ['ARGNO2S']
        elif giella == 'ScPl3':
            unimorphtags += ['ARGNO3S']
        elif giella == 'OcSg1':
            unimorphtags += ['ARGAC1S']
        elif giella == 'OcSg2':
            unimorphtags += ['ARGAC2S']
        elif giella == 'OcSg3':
            unimorphtags += ['ARGAC3S']
        elif giella == 'OcPl1':
            unimorphtags += ['ARGAC1S']
        elif giella == 'OcPl2':
            unimorphtags += ['ARGAC2S']
        elif giella == 'OcPl3':
            unimorphtags += ['ARGAC3S']
        elif giella == 'PxSg1':
            unimorphtags += ['PSS1S']
        elif giella == 'PxSg2':
            unimorphtags += ['PSS2S']
        elif giella == 'PxSg3':
            unimorphtags += ['PSS3S']
        elif giella == 'PxDu1':
            unimorphtags += ['PSS1D']
        elif giella == 'PxDu2':
            unimorphtags += ['PSS2D']
        elif giella == 'PxDu3':
            unimorphtags += ['PSS3D']
        elif giella == 'PxPl1':
            unimorphtags += ['PSS1P']
        elif giella == 'PxPl2':
            unimorphtags += ['PSS2P']
        elif giella == 'PxPl3':
            unimorphtags += ['PSS3P']
        elif giella == 'PxSP3':
            unimorphtags += ['PSS3']
        elif giella == 'Px3':
            unimorphtags += ['PSS3']
        elif giella == 'Def':
            unimorphtags += ['DEF']
        elif giella == 'Indef':
            unimorphtags += ['NDEF']
        elif giella == 'PxSg1':
            unimorphtags += ['PSS1S']
        elif giella == 'PxSg2':
            unimorphtags += ['PSS2S']
        elif giella == 'PxSg3':
            unimorphtags += ['PSS3S']
        elif giella == 'PxDu1':
            unimorphtags += ['PSS1D']
        elif giella == 'PxDu2':
            unimorphtags += ['PSS2D']
        elif giella == 'PxDu3':
            unimorphtags += ['PSS3D']
        elif giella == 'PxPl1':
            unimorphtags += ['PSS1P']
        elif giella == 'PxPl2':
            unimorphtags += ['PSS2P']
        elif giella == 'PxPl3':
            unimorphtags += ['PSS3P']
        elif giella == 'Def':
            unimorphtags += ['DEF']
        elif giella == 'Indef':
            unimorphtags += ['NDEF']
        elif giella == 'V':
            if '+PrsPrc' in tags:
                unimorphtags += ['V.PTCP']
            elif '+PrtPrc' in tags:
                unimorphtags += ['V.PTCP']
            elif '+PrfPrc' in tags:
                unimorphtags += ['V.PTCP']
            else:
                unimorphtags += ['V']
        elif giella == 'PrsPrc':
            unimorphtags += ['PRS']
        elif giella == 'PrtPrc':
            unimorphtags += ['PST']
        elif giella == 'PrfPrc':
            unimorphtags += ['PRFV']
        elif giella == 'Prc/Telic':
            unimorphtags += ['LGSPEC4/telic']  # myv
        elif giella == 'VGen':
            unimorphtags += ['V.MSDR', 'GEN']
        elif giella == 'VAbess':
            unimorphtags += ['V.CVB', 'ABE']
        elif giella == 'NomAg':
            unimorphtags += ['V.MSDR', 'LGSPEC/agent']
        elif giella == 'AgPrc':
            unimorphtags += ['V.PTCP', 'LGSPEC/agent']
        elif giella == 'NegPrc':
            unimorphtags += ['V.PTCP', 'NEG']
        elif giella == 'NomAct':
            unimorphtags += ['V.MSDR']
        elif giella == 'INF':
            unimorphtags += ['NFIN']
        elif giella == 'Inf':
            unimorphtags += ['NFIN']
        elif giella == 'Ger':
            unimorphtags += ['V.CVB', 'LGSPEC/ger']  # XXX: GER?
        elif giella == 'Actio':
            unimorphtags += ['V.MSDR', 'LGSPEC/actio']  # XXX: ???
        elif giella == 'Sup':
            unimorphtags += ['V.CVB', 'LGSPEC/sup']  # Supine, not superlative or superessive
        elif giella == 'InfA':
            unimorphtags += ['NFIN']  # fin
        elif giella == 'InfE':
            unimorphtags += ['V.CVB']  # fin
        elif giella == 'Inf3':
            unimorphtags += ['V.CVB']  # fkv
        elif giella == 'InfMa':
            unimorphtags += ['V.CVB']  # fin
        elif giella == 'A_Hum':
            unimorphtags += ['ADJ']  # fin?
        elif giella == 'Adv-':
            unimorphtags += ['ADV']
        elif giella == 'Actv':
            unimorphtags += ['ACT']
        elif giella == 'Act':
            unimorphtags += ['ACT']
        elif giella == 'Pasv':
            unimorphtags += ['PASS']
        elif giella == 'Pass':
            unimorphtags += ['PASS']
        elif giella == 'Pss':
            unimorphtags += ['PASS']
        elif giella == 'Cond':
            unimorphtags += ['COND']
        elif giella == 'Pot':
            unimorphtags += ['POT']
        elif giella == 'Imp':
            unimorphtags += ['IMP']
        elif giella == 'Imprt':
            unimorphtags += ['IMP']
        elif giella == 'ImprtII':
            unimorphtags += ['IMP']
        elif giella == 'Cau':
            unimorphtags += ['CAUS']
        elif giella == 'Subj':
            unimorphtags += ['SBJV']
        elif giella == 'Opt':
            unimorphtags += ['OPT']  # Desiderative optative
        elif giella == 'Des':
            unimorphtags += ['OPT']  # Desiderative optative
        elif giella == 'Oblig':
            unimorphtags += ['OBGLIG']
        elif giella == 'Interr':
            unimorphtags += ['INT']  # XXX: ABE?
        elif giella in ['Der1', 'Der2']:
            continue
        elif giella == 'Der/Comp':
            unimorphtags += ['CMPR']
        elif giella == 'Comp':
            unimorphtags += ['CMPR']
        elif giella == 'Compar':
            unimorphtags += ['CMPR']  # fkv
        elif giella == 'Superl':
            unimorphtags += ['SPRL']
        elif giella == 'Der/Superl':
            unimorphtags += ['SPRL']
        elif giella == 'Der/PassS':
            unimorphtags += ['PASS']
        elif giella == 'Attr':
            unimorphtags += ['LGSPEC9/ATTR']
        elif giella == 'Pred':
            unimorphtags += ['LGSPEC9/PRED']
        elif giella == 'Aff':
            unimorphtags += ['POS']
        elif giella == 'Neg':
            unimorphtags += ['NEG']
        elif giella == 'NegCnd':
            unimorphtags += ['NEG', 'COND']
        elif giella == 'NegCndSub':
            unimorphtags += ['NEG', 'COND']
        elif giella == 'Pos':
            unimorphtags += ['POS']
        elif giella.startswith('Err/'):
            unimorphtags += ['TYPO']
        elif giella.startswith('Errr/'):
            unimorphtags += ['TYPO']
        elif giella.startswith('Der/'):
            unimorphtags += ['XXXDER' + giella[4:]]
            continue  # NB: handle SOME ders before this
        elif giella == 'Long':
            continue
        elif giella == 'Allegro':
            continue
        elif giella == 'Sh':
            continue
        elif giella == 'Largo':
            continue
        elif giella == 'ABBR-':
            continue
        elif giella == 'ABBR':
            continue
        elif giella == 'ACRO':
            continue
        elif giella == 'ACR':
            continue
        elif giella == 'LEFT':
            continue
        elif giella == 'RIGHT':
            continue
        elif giella == 'Coll':
            continue
        elif giella == 'Qu':
            unimorphtags += ['LGSPEC1/?']
        elif giella == 'Qst':
            unimorphtags += ['LGSPEC1/?']
        elif giella.startswith('Qst/'):
            unimorphtags += ['LGSPEC1/?' + giella[4:]]
        elif giella == 'Subqst':
            continue
        elif giella == 'Rel':
            continue  # is not: Relative case or Relative comparator
        elif giella == 'Dim/ke':
            continue
        elif giella == 'Ord':
            continue
        elif giella in ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']:
            continue
        elif giella in ['G3', 'G7']:
            continue
        elif giella.startswith('Sem'):
            continue
        elif giella == 'Dummytag':
            continue
        elif giella == 'S':
            continue
        elif giella == 'Quote':
            continue
        elif giella == 'CLB':
            continue
        elif giella == 'Prop':
            continue  # handled elsehwere
        elif giella.startswith('Cmp'):
            unimorphtags += ['XXXCOMPOUND']
            continue  # ?
        elif giella == 'Use/Rus':
            unimorphtags += ['DIAL']
        elif giella == 'Use/Circ':
            unimorphtags += ['XXXCIRC']
        elif giella == 'Use/Dial':
            unimorphtags += ['DIAL']
        elif giella.startswith('Use/'):
            unimorphtags += ['XXX' + giella[4:]]
        elif giella.startswith('Usage/'):
            unimorphtags += ['XXX' + giella[6:]]
        elif giella == 'Guess':
            unimorphtags += ['XXX']
        elif giella == '??':
            unimorphtags += ['XXX']
        elif giella == 'TODO':
            unimorphtags += ['XXX']
        elif giella == 'Dial':
            unimorphtags += ['DIAL']
        elif giella == 'South':
            unimorphtags += ['DIAL?']
        elif giella == 'Orth/Colloq':
            unimorphtags += ['DIAL?']
        elif giella == 'Conneg':
            unimorphtags += ['NEG']  # XXX
        elif giella == 'ConNeg':
            unimorphtags += ['NEG']  # XXX
        elif giella == 'ConNegII':
            unimorphtags += ['NEG']  # XXX
        elif giella == 'IV':
            unimorphtags += ['INTR']
        elif giella == 'TV':
            unimorphtags += ['TR']
        elif giella == 'Impers':
            unimorphtags += ['IMPRS']
        elif giella == 'Reflex':
            unimorphtags += ['REFL']
        elif giella == 'Refl':
            unimorphtags += ['REFL']
        elif giella == 'Recipr':
            unimorphtags += ['RECP']
        elif giella == 'Distr':
            unimorphtags += ['REM']
        elif giella == 'Dist':
            unimorphtags += ['REM']
        elif giella == 'Prox':
            unimorphtags += ['PROXM']
        elif giella == 'Bahuvrihi':
            # myv
            continue
        elif giella == 'AssocColl':
            # myv
            continue
        elif giella in ['0,0', '0,1']:
            continue
        elif giella in ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9',
                        'F00', 'F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07',
                        'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F08',
                        'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24',
                        'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 'F09',
                        'F32', 'F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F0',
                        'F39', 'F40', 'F41', 'F42', 'F43', 'F44', 'F45',
                        'F46', 'F47', 'F48', 'F49', 'F50', 'F51', 'F52', 'F53',
                        'F54', 'F55', 'F56', 'F57', 'F58', 'F59', 'F60', 'F61',
                        'F62', 'F63', 'F64', 'F65', 'F66', 'F67', 'F68',
                        'F69', 'F70', 'F71', 'F72', 'F73', 'F74', 'F75', 'F76',
                        'F77', 'F78', 'F79', 'F80', 'F81', 'F82', 'F83', 'F84',
                        'F85', 'F86', 'F87', 'F88', 'F89', 'F90', 'F91', 'F92',
                        'F93', 'F94', 'F95', 'F96', 'F97', 'F98', 'F99',
                        'F100', 'Enter', 'Alt', 'Shift',
                        'B', 'C', 'E', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X',
                        'Y', 'Z',
                        'Š', 'Ž', 'Ä', 'Õ', 'Ö', 'Ü', '0']:
            # est
            continue
        elif giella == 'Adn':
            # myv
            continue
        elif giella == 'Conj':
            # myv
            continue
        elif giella == 'Prec':
            # myv
            continue
        elif giella == 'Quot':
            # est
            continue
        elif giella == 'Prel':
            # fit
            continue
        elif giella == 'Dem':
            continue  # FIXME
        elif giella == 'Pers':
            continue  # FIXME
        elif giella == 'Disc':
            continue
        elif giella == 'Foc':
            unimorphtags += ['LGSPEC1/UnnamedFoc']
        elif giella.startswith('Foc/'):
            unimorphtags += ['LGSPEC1/' + giella[4:]]
        elif giella == 'Clit':
            unimorphtags += ['LGSPEC1/UnnamedClit']
        elif giella.startswith('Clit/'):
            unimorphtags += ['LGSPEC1/' + giella[5:]]
        elif giella == 'Clt':
            unimorphtags += ['LGSPEC2']
        elif giella.startswith('Clt/'):
            unimorphtags += ['LGSPEC2/' + giella[4:]]
        elif giella.startswith('OLang/'):
            continue
        elif giella.startswith('Gram/'):
            continue
        elif giella.startswith('Hom'):
            continue
        elif giella == 'TruncPrefix':
            unimorphtags += ['LGSPEC/prefix-']
        elif giella == 'Pref':
            unimorphtags += ['LGSPEC/prefix-']
        elif giella == 'Prefix':
            unimorphtags += ['LGSPEC/prefix-']
        elif giella.startswith('Pref-'):
            unimorphtags += ['LGSPEC/prefix-']
        elif giella.startswith('Genmiessi'):
            print('SOmething broken here½!', tags)
        elif '@' in giella:
            print('SOmething broken here½!', tags)
        elif giella.startswith('NErr/'):
            print('SOmething broken here½!', tags)
            unimorphtags += ['TYPO']
        elif giella.startswith('AErr/'):
            print('SOmething broken here½!', tags)
            unimorphtags += ['TYPO']
        elif '<cnjcoo>' in giella:
            print('SOmething broken here½!', tags)
        elif '<actv>' in giella:
            print('SOmething broken here½!', tags)
        elif '<gen>' in giella:
            print('SOmething broken here½!', tags)
        elif 'N224-1-9' in giella:
            print('SOmething broken here½!', tags)
        elif '#222-5-19' in giella:
            print('SOmething broken here½!', tags)
        elif '/-' in giella:
            print('SOmething broken here½!', tags)
        elif giella in ['a', 'b', 'i', 't', 'd', 's', 'n', 'ä', 'ö']:
            print('SOmething broken here½!', tags)
        elif giella in ['Ne', 'Ni', 'Nte', 'Ntee', 'Nt', 'Nti', 'Na', 'No',
                        'N-', 'c']:
            print('SOmething broken here½!', tags)
        elif 'elekriski' in giella:
            print('SOmething broken here½!', tags)
        elif giella == 'VGen':
            continue  # FIXME
        elif giella == 'VAbess':
            continue  # FIXME
        elif giella == 'NomAg':
            continue  # FIXME
        elif giella == 'Inf':
            unimorphtags += ['NFIN']
        elif giella == 'Ger':
            unimorphtags += ['NFIN']  # XXX: GER?
        elif giella == 'Actio':
            unimorphtags += ['GER']  # XXX: ???
        elif giella == 'Actv':
            unimorphtags += ['ACT']
        elif giella == 'Pasv':
            unimorphtags += ['PASS']
        elif giella == 'Cond':
            unimorphtags += ['COND']
        elif giella == 'Pot':
            unimorphtags += ['POT']
        elif giella == 'Imprt':
            unimorphtags += ['IMP']
        elif giella == 'Subj':
            unimorphtags += ['SBJV']
        elif giella == 'Interr':
            unimorphtags += ['INT']  # XXX: ABE?
        elif giella == 'Der/Comp':
            unimorphtags += ['CMPR']
        elif giella == 'Comp':
            unimorphtags += ['CMPR']
        elif giella == 'Sup':
            unimorphtags += ['SPRL']
        elif giella == 'Der/Superl':
            unimorphtags += ['SPRL']
        elif giella == 'Der/PassS':
            unimorphtags += ['PASS']
        elif giella == 'Attr':
            unimorphtags += ['ATTR']
        elif giella == 'Neg':
            unimorphtags += ['NEG']
        elif giella == 'Pos':
            unimorphtags += ['POS']
        elif giella.startswith('Err/'):
            unimorphtags += ['TYPO']
        elif giella.startswith('Der/'):
            continue  # NB: handle SOME ders before this
        elif giella == 'Allegro':
            continue
        elif giella == 'ACR':
            continue
        elif giella == 'Coll':
            continue
        elif giella == 'Qst':
            continue
        elif giella == 'Subqst':
            continue
        elif giella == 'Rel':
            continue  # is not: Relative case or Relative comparator
        elif giella == 'Ord':
            continue
        elif giella in ['v1', 'v2', 'v3']:
            continue
        elif giella in ['G3', 'G7']:
            continue
        elif giella.startswith('Sem'):
            continue
        elif giella == 'Prop':
            continue  # handled elsehwere
        elif giella.startswith('Cmp'):
            continue  # ?
        elif giella == 'South':
            unimorphtags += ['DIAL?']
        elif giella == 'ConNeg':
            unimorphtags += ['NEG']  # XXX
        elif giella == 'ConNegII':
            unimorphtags += ['NEG']  # XXX
        elif giella == 'IV':
            continue  # not marked in current unimorph
            # unimorphtags += ['INTR']
        elif giella == 'TV':
            continue  # not marked in current unimorph
            unimorphtags += ['TR']
        elif giella == 'Recipr':
            unimorphtags += ['RECP']
        elif giella == 'Dem':
            continue  #  FIXME
        elif giella == 'Pers':
            continue  #  FIXME
        elif giella.startswith('Foc/'):
            unimorphtags += ['LGSPEC1/' + giella[5:]]
        else:
            print("missing giella mapping for", giella, "in tags")
            sys.exit(2)
    # shuffle and patch
    CASESWITHOUTNUMBERS = ['FRML', 'COM']
    for casetag in CASESWITHOUTNUMBERS:
        if casetag in unimorphtags and 'SG' not in unimorphtags and\
                'PL' not in unimorphtags:
            unimorphtags += ['SG']
    MOODSWITHEXTRATENSE = ['COND', 'POT']
    for mood in MOODSWITHEXTRATENSE:
        if mood in unimorphtags and 'PRS' in unimorphtags:
            unimorphtags.remove('PRS')
        elif mood in unimorphtags and 'PST' in unimorphtags:
            unimorphtags.remove('PST')
    return ';'.join(unimorphtags)


def unimorph2giella(unimorphs: str) -> list:
    giellatags = []
    for unimorph in unimorphs.split(';'):
        if unimorph == 'N':
            giellatags += ['+N']
        elif unimorph == 'V':
            giellatags += ['+V']
        elif unimorph == 'ADJ':
            giellatags += ['+A']
        elif unimorph == 'NEUT':
            giellatags += ['+Neu']
        elif unimorph == 'MASC':
            giellatags += ['+Msc']
        elif unimorph == 'FEM':
            giellatags += ['+Fem']
        elif unimorph == 'MASC+FEM':
            giellatags += ['+Common']
        elif unimorph == 'GEN':
            giellatags += ['+Gen']
        elif unimorph == 'COM':
            giellatags += ['+Com']
        elif unimorph == 'ON+ESS':
            giellatags += ['+Ses']
        elif unimorph == 'FRML':
            giellatags += ['+Ess']
        elif unimorph == 'ESS':
            giellatags += ['+Ess']
        elif unimorph == 'INAN':
            giellatags += ['+Inan']
        elif unimorph == 'ANIM':
            giellatags += ['+Anim']
        elif unimorph == 'PRIV':
            giellatags += ['+Abe']
        elif unimorph == 'PRT':
            giellatags += ['+Par']
        elif unimorph == 'INS':
            giellatags += ['+Ins']
        elif unimorph == 'IN+ESS':
            giellatags += ['+Ine']
        elif unimorph == 'NOM':
            giellatags += ['+Nom']
        elif unimorph == 'ON+ALL':
            giellatags += ['+Sub']
        elif unimorph == 'AT+ALL':
            giellatags += ['+All']
        elif unimorph == 'PRP':
            giellatags += ['+Loc']
        elif unimorph == 'INST':
            giellatags += ['+Inst']
        elif unimorph == 'TRANS':
            giellatags += ['+Tra']
        elif unimorph == 'TERM':
            giellatags += ['+Term']
        elif unimorph == 'ON+ABL':
            giellatags += ['+Del']
        elif unimorph == 'IN+ABL':
            giellatags += ['+Ela']
        elif unimorph == 'IN+ALL':
            giellatags += ['+Ill']
        elif unimorph == 'DAT':
            giellatags += ['+Dat']
        elif unimorph == 'ACC':
            giellatags += ['+Acc']
        elif unimorph == 'AT+ESS':
            giellatags += ['+Ade']
        elif unimorph == 'AT+ABL':
            giellatags += ['+Abl']
        elif unimorph == 'SG':
            giellatags += ['+Sg']
        elif unimorph == 'DU':
            giellatags += ['+Du']
        elif unimorph == 'PL':
            giellatags += ['+Pl']
        elif unimorph == 'SG+PL':
            # giellatags += ['+Sg/Pl']
            pass
        elif unimorph == 'IND':
            giellatags += ['+Ind']
        elif unimorph == 'PRS':
            giellatags += ['+Prs']
        elif unimorph == 'PST':
            giellatags += ['+Prt']
        elif unimorph == 'PRF':
            giellatags += ['+Perf']
        elif unimorph == 'FUT':
            giellatags += ['+Fut']
        elif unimorph == '1':
            giellatags += ['+1']
        elif unimorph == '2':
            giellatags += ['+2']
        elif unimorph == '3':
            giellatags += ['+3']
        elif unimorph == 'INDF':
            pass  # unmarked in giellatags
        elif unimorph == 'GEADJ':
            giellatags += ['+Gen']
        elif unimorph == 'DEF':
            giellatags += ['+Def']
        elif unimorph == 'NDEF':
            giellatags += ['+Ind']
        elif unimorph == 'V.PTCP':
            giellatags += ['+V']
            if 'PRS' in unimorphs:
                giellatags += ['+PrsPrc']
            elif 'PST' in unimorphs:
                giellatags += ['+PrtPrc']
            elif 'FUT' in unimorphs:
                giellatags += ['+Fut']
            else:
                giellatags += ['+Drv/Ptcp']
        elif unimorph == 'NFIN':
            giellatags += '+Ger'
        elif unimorph == 'ACT':
            giellatags += ['+Actv']
        elif unimorph == 'PASS':
            giellatags += ['+Pasv']
        elif unimorph == 'COND':
            giellatags += ['+Cond']
        elif unimorph == 'POT':
            giellatags += ['+Pot']
        elif unimorph == 'IMP':
            giellatags += ['+Imprt']
        elif unimorph == 'SBJV':
            giellatags += ['+Subj']
        elif unimorph == 'V.CVB':
            giellatags += ['+V']
            giellatags += ['+Der/Adv']
        elif unimorph == 'CMPR':
            giellatags += ['+Comp']
        elif unimorph == 'SPRL':
            giellatags += ['+Sup']
        elif unimorph == 'NEG':
            giellatags += ['+Neg']
        elif unimorph == 'POS':
            # giellatags += ['+Pos']
            pass
        elif unimorph == 'LGSPEC':
            pass
        elif unimorph == 'LGSPEC1':
            pass
        else:
            print('missing unimorph mapping for:', unimorph)
            sys.exit(2)
    reorg = list()
    for ape in giellatags:
        if ape in ['+N', '+V', '+A']:
            reorg += [ape]
            break
    if reorg == ['+N']:
        for ape in giellatags:
            if ape in ['+Sg', '+Pl', '+Du']:
                reorg += [ape]
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ['+V']:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
        if '+1' in reorg and '+Sg' in reorg:
            reorg += ['+Sg1']
            reorg.remove('+1')
            reorg.remove('+Sg')
        elif '+2' in reorg and '+Sg' in reorg:
            reorg += ['+Sg2']
            reorg.remove('+2')
            reorg.remove('+Sg')
        elif '+3' in reorg and '+Sg' in reorg:
            reorg += ['+Sg3']
            reorg.remove('+3')
            reorg.remove('+Sg')
        elif '+1' in reorg and '+Du' in reorg:
            reorg += ['+Du1']
            reorg.remove('+1')
            reorg.remove('+Du')
        elif '+2' in reorg and '+Du' in reorg:
            reorg += ['+Du2']
            reorg.remove('+2')
            reorg.remove('+Du')
        elif '+3' in reorg and '+Du' in reorg:
            reorg += ['+Du3']
            reorg.remove('+3')
            reorg.remove('+Du')
        elif '+1' in reorg and '+Pl' in reorg:
            reorg += ['+Pl1']
            reorg.remove('+1')
            reorg.remove('+Pl')
        elif '+2' in reorg and '+Pl' in reorg:
            reorg += ['+Pl2']
            reorg.remove('+2')
            reorg.remove('+Pl')
        elif '+3' in reorg and '+Pl' in reorg:
            reorg += ['+Pl3']
            reorg.remove('+3')
            reorg.remove('+Pl')
    elif reorg == ['+A']:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    else:
        print('REORG FAIL', reorg)
        sys.exit(1)
    return reorg


def ud2giella(lemma, upos, xpos, feats):
    """Convert UD to giellalt tags for morphosyntax."""
    giellatags = []
    if upos == "NOUN":
        giellatags.append("+N")
    elif upos == "VERB":
        giellatags.append("+V")
    elif upos == "ADJ":
        giellatags.append("+A")
    elif upos == "ADV":
        giellatags.append("+Adv")
    elif upos == "ADP":
        giellatags.append("+Adp")
    elif upos == "CCONJ":
        giellatags.append("+CC")
    elif upos == "SCONJ":
        giellatags.append("+CS")
    elif upos == "PUNCT":
        giellatags.append("+Punct")
    elif upos == "SYM":
        giellatags.append("+Sym")
    elif upos == "PRON":
        giellatags.append("+Prn")
    elif upos == "DET":
        giellatags.append("+Det")
    elif upos == "NUM":
        giellatags.append("+Num")
    elif upos == "INTJ":
        giellatags.append("+Interj")
    elif upos == "PROPN":
        giellatags.append("+N")
        giellatags.append("+Prop")
    elif upos == "AUX":
        giellatags.append("+V")
        giellatags.append("+Aux")
    elif upos == "PART":
        giellatags.append("+Pcle")
    elif upos == "X":
        giellatags.append("+X")
    elif upos == "_":
        pass
    else:
        print(f"Unhandled upos {upos}")
        sys.exit(1)
    for featstruct in feats.split("|"):
        if featstruct == "_":
            continue
        feat, val = featstruct.split("=")
        if featstruct == "Case=Nom":
            giellatags.append("+Nom")
        elif featstruct == "Case=Gen":
            giellatags.append("+Gen")
        elif featstruct == "Case=Dat":
            giellatags.append("+Dat")
        elif featstruct == "Case=Par":
            giellatags.append("+Par")
        elif featstruct == "Case=Ins":
            giellatags.append("+Ins")
        elif featstruct == "Case=Ill":
            giellatags.append("+Ill")
        elif featstruct == "Case=Abl":
            giellatags.append("+Abl")
        elif featstruct == "Case=Tra":
            giellatags.append("+Tra")
        elif featstruct == "Case=All":
            giellatags.append("+All")
        elif featstruct == "Case=Abe":
            giellatags.append("+Abe")
        elif featstruct == "Case=Ade":
            giellatags.append("+Ade")
        elif featstruct == "Case=Ine":
            giellatags.append("+Ine")
        elif featstruct == "Case=Ela":
            giellatags.append("+Ela")
        elif featstruct == "Case=Loc":
            giellatags.append("+Loc")
        elif featstruct == "Case=Ess":
            giellatags.append("+Ess")
        elif featstruct == "Case=Com":
            giellatags.append("+Com")
        elif featstruct == "Case=Voc":
            giellatags.append("+Voc")
        elif featstruct == "Case=Del":
            giellatags.append("+Del")
        elif featstruct == "Case=Sbl":
            giellatags.append("+Sub")
        elif featstruct == "Case=Sup":
            giellatags.append("+Super")
        elif featstruct == "Case=Cau":
            giellatags.append("+Cau")
        elif featstruct == "Case=Lat":
            giellatags.append("+Lat")
        elif featstruct == "Case=Dis":
            giellatags.append("+Dis")
        elif featstruct == "Case=Abs":
            giellatags.append("+Abs")
        elif featstruct == "Case=Tem":
            giellatags.append("+Tem")
        elif featstruct == "Case=Ter":
            giellatags.append("+Ter")
        elif featstruct == "Case=Acc":
            giellatags.append("+Acc")
        elif featstruct == "Case=Prl":
            giellatags.append("+Prl")
        elif featstruct == "Case=Ben":
            giellatags.append("+Ben")
        elif featstruct == "Case=Cmp":
            giellatags.append("+Compa")
        elif featstruct == "Case=Acc,Nom":
            giellatags.append("+AccNom")
        elif featstruct == "Case=Gen,Nom":
            giellatags.append("+GenNom")
        elif featstruct == "Gender=Masc":
            giellatags.append("+Masc")
        elif featstruct == "Gender=Fem,Masc":
            giellatags.append("+Ut")
        elif featstruct == "Gender=Fem":
            giellatags.append("+Fem")
        elif featstruct == "Gender=Neut":
            giellatags.append("+Neut")
        elif featstruct == "Gender[psor]=Fem":
            giellatags.append("+Fem")
        elif featstruct == "Gender[psor]=Masc":
            giellatags.append("+Masc")
        elif featstruct == "Animacy=Anim":
            giellatags.append("+Sem/Animate")
        elif featstruct == "Animacy=Inan":
            giellatags.append("+Sem/Inanimate")
        elif featstruct == "Animacy=Hum":
            giellatags.append("+Sem/Hum")
        elif featstruct == "Mood=Ind":
            giellatags.append("+Ind")
        elif featstruct == "Mood=Imp":
            giellatags.append("+Imp")
        elif featstruct == "Mood=Cnd":
            giellatags.append("+Cond")
        elif featstruct == "Mood=Pot":
            giellatags.append("+Pot")
        elif featstruct == "Mood=CndSub":
            giellatags.append("+CndSubj")
        elif featstruct == "Mood=Sub":
            giellatags.append("+Subj")
        elif featstruct == "Mood=Opt":
            giellatags.append("+Opt")
        elif featstruct == "Mood=Jus":
            giellatags.append("+Jus")
        elif featstruct == "Mood=Proh":
            giellatags.append("+Proh")
        elif featstruct == "Mood=Prec":
            giellatags.append("+Prec")
        elif featstruct == "Mood=Nec":
            giellatags.append("+Nec")
        elif featstruct == "Mood=Des":
            giellatags.append("+Des")
        elif featstruct == "Mood=Imp,Ind":
            giellatags.append("+Imp")
            giellatags.append("+Ind")
        elif featstruct == "Mood=Imp,Pot":
            giellatags.append("+Imp")
            giellatags.append("+Pot")
        elif featstruct == "Mood=Cnd,Pot":
            giellatags.append("+Eve")
        elif featstruct == "Aspect=Compl":
            continue
        elif featstruct == "Aspect=Frus":
            continue
        elif featstruct == "Aspect=Freq":
            giellatags.append("+Freq")
        elif featstruct == "Aspect=Aor":
            giellatags.append("+Past")
        elif featstruct == "Aspect=Imp":
            giellatags.append("+Imp")
        elif featstruct == "Aspect=Hab":
            giellatags.append("+Hab")
        elif featstruct == "Aspect=Prog":
            giellatags.append("+Prog")
        elif featstruct == "Aspect=ProgNeg":
            giellatags.append("+Prog")
            giellatags.append("+Neg")
        elif featstruct == "Aspect=ProgBkg":
            giellatags.append("+Prog")  # XXX
        elif featstruct == "Aspect=ProgLocBkg":
            giellatags.append("+Prog")  # XXX
        elif featstruct == "Aspect=PerfNeg":
            giellatags.append("+Perf")
            giellatags.append("+Neg")
        elif featstruct == "Aspect=Perf":
            giellatags.append("+Perf")
        elif featstruct == "Aspect=PerfBkg":
            giellatags.append("+Perf")  # XXX
        elif featstruct == "Aspect=Iter":
            giellatags.append("+Iter")
        elif featstruct == "Number=Sing":
            if "Person=" not in feats:
                giellatags.append("+Sg")
        elif featstruct == "Number=Dual":
            if "Person=" not in feats:
                giellatags.append("+Du")
        elif featstruct == "Number=Plur":
            if "Person=" not in feats:
                giellatags.append("+Pl")
        elif featstruct == "Number=Ptan":
            giellatags.append("+Pl")  # XXX
        elif featstruct == "Number=Plur,Sing":
            continue  # ???
        elif featstruct == "Number[psor]=Sing":
            continue  # c.f. Person[psor]
        elif featstruct == "Number[psor]=Dual":
            continue  # c.f. Person[psor]
        elif featstruct == "Number[psor]=Plur":
            continue  # c.f. Person[psor]
        elif featstruct == "Number[psed]=Sing":
            giellatags.append("+Der/PxSg")
        elif featstruct == "Number[psed]=Plur":
            giellatags.append("+Der/PxPl")
        elif featstruct == "Number[subj]=Sing":
            continue  # c.f. Person[subj]
        elif featstruct == "Number[subj]=Plur":
            continue  # c.f. Person[subj]
        elif featstruct == "Number[subj]=Plur,Sing":
            continue  # c.f. Person[subj]
        elif featstruct == "Number[obj]=Sing":
            continue  # c.f. Person[obj]
        elif featstruct == "Number[obj]=Plur":
            continue  # c.f. Person[obj]
        elif featstruct == "Number[grnd]=Sing":
            continue  # c.f. Person[grnd]
        elif featstruct == "NumType=Card":
            giellatags.append("+Card")
        elif featstruct == "NumType=Ord":
            giellatags.append("+Ord")
        elif featstruct == "NumType=OrdSets":
            continue
        elif featstruct == "NumType=OrdMult":
            continue
        elif featstruct == "NumType=Mult":
            continue
        elif featstruct == "NumType=Frac":
            continue
        elif featstruct == "NumType=Dist":
            continue
        elif featstruct == "NumType=Appr":
            continue
        elif featstruct == "NumType=Coll":
            continue
        elif featstruct == "NumType=Sets":
            continue
        elif featstruct == "AdvType=Cau":
            continue
        elif featstruct == "AdvType=Con":
            continue
        elif featstruct == "AdvType=Sta":
            continue
        elif featstruct == "AdvType=Mod":
            continue
        elif featstruct == "AdvType=Loc":
            continue
        elif featstruct == "AdvType=Deg":
            continue
        elif featstruct == "AdvType=Tim":
            continue
        elif featstruct == "AdvType=Man":
            continue
        elif featstruct == "AdvType=Ideoph":
            continue
        elif featstruct == "Person=1":
            if "Number=Sing" in feats:
                giellatags.append("+Sg1")
            elif "Number=Plur" in feats:
                giellatags.append("+Pl1")
            elif "Number=Dual" in feats:
                giellatags.append("+Du1")
            else:
                giellatags.append("+1")
        elif featstruct == "Person=2":
            if "Number=Sing" in feats:
                giellatags.append("+Sg2")
            elif "Number=Plur" in feats:
                giellatags.append("+Pl2")
            elif "Number=Dual" in feats:
                giellatags.append("+Du2")
            else:
                giellatags.append("+2")
        elif featstruct == "Person=3":
            if "Number=Sing" in feats:
                giellatags.append("+Sg3")
            elif "Number=Plur" in feats:
                giellatags.append("+Pl3")
            elif "Number=Dual" in feats:
                giellatags.append("+Du3")
            else:
                giellatags.append("+3")
        elif featstruct == "Person=4":
            giellatags.append("+Impersonal")  # FIXME
        elif featstruct == "Person=0":
            giellatags.append("+Impersonal")  # FIXME
        elif featstruct == "Person[psor]=1":
            if "Number[psor]=Sing" in feats:
                giellatags.append("+PxSg1")
            elif "Number[psor]=Plur" in feats:
                giellatags.append("+PxPl1")
            elif "Number[psor]=Dual" in feats:
                giellatags.append("+PxDu1")
            else:
                giellatags.append("+Px1")
        elif featstruct == "Person[psor]=2":
            if "Number[psor]=Sing" in feats:
                giellatags.append("+PxSg2")
            elif "Number[psor]=Plur" in feats:
                giellatags.append("+PxPl2")
            elif "Number[psor]=Dual" in feats:
                giellatags.append("+PxDu2")
            else:
                giellatags.append("+Px2")
        elif featstruct == "Person[psor]=3":
            if "Number[psor]=Sing" in feats:
                giellatags.append("+PxSg3")
            elif "Number[psor]=Plur" in feats:
                giellatags.append("+PxPl3")
            elif "Number[psor]=Dual" in feats:
                giellatags.append("+PxDu3")
            else:
                giellatags.append("+Px3")
        elif featstruct == "Person[subj]=1":
            if "Number[subj]=Sing" in feats:
                giellatags.append("+Sg1")
            elif "Number[subj]=Plur" in feats:
                giellatags.append("+Pl1")
        elif featstruct == "Person[subj]=2":
            if "Number[subj]=Sing" in feats:
                giellatags.append("+Sg2")
            elif "Number[subj]=Plur" in feats:
                giellatags.append("+Pl2")
        elif featstruct == "Person[subj]=3":
            if "Number[subj]=Sing" in feats:
                giellatags.append("+Sg3")
            elif "Number[subj]=Plur" in feats:
                giellatags.append("+Pl3")
            else:
                giellatags.append("+3")
        elif featstruct == "Person[obj]=1":
            if "Number[obj]=Sing" in feats:
                giellatags.append("+o_Sg1")
            elif "Number[obj]=Plur" in feats:
                giellatags.append("+o_Pl1")
        elif featstruct == "Person[obj]=2":
            if "Number[obj]=Sing" in feats:
                giellatags.append("+o_Sg2")
            elif "Number[obj]=Plur" in feats:
                giellatags.append("+o_Pl2")
        elif featstruct == "Person[obj]=3":
            if "Number[obj]=Sing" in feats:
                giellatags.append("+o_Sg3")
            elif "Number[obj]=Plur" in feats:
                giellatags.append("+o_Pl3")
        elif featstruct == "Person[grnd]=3":
            if "Number[grnd]=Sing" in feats:
                giellatags.append("+g_Sg3")
            elif "Number[grnd]=Plur" in feats:
                giellatags.append("+g_Pl3")
        elif featstruct == "PronType=Ind,Prs":
            giellatags.append("+Indef")
            giellatags.append("+Pers")
        elif featstruct == "PronType=Ind":
            giellatags.append("+Indef")
        elif featstruct == "PronType=Prs":
            giellatags.append("+Pers")
        elif featstruct == "PronType=Prs,Tot":
            giellatags.append("+Pers")
        elif featstruct == "PronType=Rel":
            giellatags.append("+Rel")
        elif featstruct == "PronType=Dem":
            giellatags.append("+Dem")
        elif featstruct == "PronType=Dem,Ind":
            giellatags.append("+Dem")
            giellatags.append("+Ind")
        elif featstruct == "PronType=Int":
            giellatags.append("+Interr")
        elif featstruct == "PronType=Int,Rel":
            giellatags.append("+Interr")
            giellatags.append("+Rel")
        elif featstruct == "PronType=Rcp":
            giellatags.append("+Recipr")
        elif featstruct == "PronType=Art":
            giellatags.append("+Art")
        elif featstruct == "PronType=Art,Prs":
            giellatags.append("+Art")
            giellatags.append("+Pers")
        elif featstruct == "PronType=Tot":
            continue
        elif featstruct == "PronType=Emp":
            continue
        elif featstruct == "PronType=Neg":
            giellatags.append("+Neg")
        elif featstruct == "AdpType=Prep":
            giellatags.remove("+Adp")
            giellatags.insert(0, "+Pr")
        elif featstruct == "AdpType=Post":
            giellatags.remove("+Adp")
            giellatags.insert(0, "+Po")
        elif featstruct == "Polarity=Pos":
            continue
        elif featstruct == "Polarity=Neg":
            giellatags.append("+Neg")
        elif featstruct == "Tense=Pres":
            giellatags.append("+Prs")
        elif featstruct == "Tense=Past":
            giellatags.append("+Prt")
        elif featstruct == "Tense=Fut":
            giellatags.append("+Fut")
        elif featstruct == "Tense=Pred":
            giellatags.append("+Pred")
        elif featstruct == "Voice=Act":
            giellatags.append("+Act")
        elif featstruct == "Voice=Pass":
            giellatags.append("+Pass")
        elif featstruct == "Voice=Rcp":
            giellatags.append("+Rcp")
        elif featstruct == "Voice=Cau":
            giellatags.append("+Cau")
        elif featstruct == "Voice=Mid":
            giellatags.append("+Mid")
        elif featstruct == "Voice=Mid,Pass":
            giellatags.append("+Mid")
            giellatags.append("+Pass")
        elif featstruct == "Voice=Stat":
            giellatags.append("+Stat")
        elif featstruct == "Degree=Pos":
            continue  # ?
        elif featstruct == "Degree=Cmp":
            giellatags.append("+Comp")
        elif featstruct == "Degree=Sup":
            giellatags.append("+Sup")
        elif featstruct == "Degree=Aug":
            giellatags.append("+Aug")
        elif featstruct == "Degree=Dim":
            giellatags.append("+Dim")
        elif featstruct == "VerbType=Aux":
            giellatags.append("+Aux")
        elif featstruct == "PartForm=Pres":
            giellatags.append("+PrsPrc")
        elif featstruct == "PartForm=Past":
            giellatags.append("+PrtPrc")
        elif featstruct == "PartForm=Agt":
            giellatags.append("+AgPrc")
        elif featstruct == "PartForm=Neg":
            giellatags.append("+NegPrc")
        elif featstruct == "PartForm=NegConvPrc":
            giellatags.append("+NegConvPrc")
        elif featstruct == "PartForm=PastDyn":
            continue
        elif featstruct == "PartForm=PrsDet":
            continue
        elif featstruct == "PartForm=PrsTra":
            continue
        elif featstruct == "Definite=Ind":
            giellatags.append("+Indef")
        elif featstruct == "Definite=2":
            giellatags.append("+Def2")
        elif featstruct == "Definite=Def":
            giellatags.append("+Def")
        elif featstruct == "Definite=Spec":
            giellatags.append("+Spec")  # XXX
        elif featstruct == "Definite=Cons":
            giellatags.append("+Cons")  # XXX
        elif featstruct == "Definite=Def,Ind":
            continue  # ???
        elif featstruct == "Deixis=Prox":
            giellatags.append("+Prox")
        elif featstruct == "Deixis=Remt":
            giellatags.append("+Dist")
        elif featstruct == "Valency=1":
            giellatags.append("+IV")
        elif featstruct == "Valency=2":
            giellatags.append("+TV")
        elif featstruct == "Abbr=Yes":
            giellatags.append("+Abbr")
        elif featstruct == "Poss=Yes":
            giellatags.append("+Poss")
        elif featstruct == "Reflex=Yes":
            giellatags.append("+Reflex")
        elif featstruct == "Connegative=Yes":
            giellatags.append("+ConNeg")
        elif featstruct == "Typo=Yes":
            giellatags.append("+Err/Orth")
        elif featstruct == "Style=Slng":
            giellatags.append("+Use/Nonstd")
        elif featstruct == "Style=Coll":
            giellatags.append("+Use/Nonstd")
        elif featstruct == "Style=Vrnc":
            giellatags.append("+Use/Nonstd")
        elif featstruct == "Style=Rare":
            giellatags.append("+Use/Nonstd")
        elif featstruct == "Style=Expr":
            giellatags.append("+Use/Nonstd")
        elif featstruct == "Style=Arch":
            giellatags.append("+Use/Arch")
        elif featstruct == "Rel=Abs":
            continue
        elif featstruct == "Rel=NCont":
            continue
        elif featstruct == "Rel=Cont":
            continue
        elif featstruct == "NumForm=Word":
            continue
        elif featstruct == "NumForm=Combi":
            continue  # XXX
        elif featstruct == "NumForm=Roman":
            giellatags.append("+Roman")
        elif featstruct == "NumForm=Digit":
            giellatags.append("+Arab")
        elif featstruct == "PartType=Prs":
            giellatags.append("+PrsPrc")
        elif featstruct == "PartType=Neg":
            giellatags.append("+NegPrc")
        elif featstruct == "PartType=Emp":
            giellatags.append("+Foc")
        elif featstruct == "PartType=Int":
            giellatags.append("+Interr")
        elif featstruct == "PartType=Mod":
            continue
        elif featstruct == "PartType=Exs":
            continue
        elif featstruct == "Foreign=Yes":
            giellatags.append("+Lang/Und")
        elif featstruct == "Variant=Short":
            giellatags.append("+Allegro")
        elif featstruct == "Variant=Long":
            giellatags.append("+Adagio")
        elif featstruct == "Evident=Nfh":
            continue
        elif featstruct == "Evident=Fh":
            continue
        elif featstruct == "NounType=Relat":
            continue
        elif featstruct == "NegationType=Contrastive":
            continue
        elif featstruct == "PunctType=Elip":
            continue
        elif featstruct == "PunctSide=Ini":
            continue
        elif featstruct == "PunctSide=Fin":
            continue
        elif featstruct == "Red=Yes":
            continue
        elif featstruct == "Modality=Proh":
            continue
        elif featstruct == "Modality=Cond":
            giellatags.append("+Cond")
        elif featstruct == "Foc=Yes":
            giellatags.append("+Foc")
        elif featstruct == "Compound=Yes":
            continue  # XXX #+cmp should go in the middle?
        # hacks that use feat and val separately
        elif feat == "InfForm":
            giellatags.append("+Inf" + val)
        elif feat == "Clitic":
            giellatags.append("+Foc/" + val)
        elif feat == "NameType":
            continue  # ?
        elif feat == "VerbForm":
            continue  # ?
        elif feat == "ExtPos":
            continue
        elif feat == "Derivation":
            giellatags.append("+Drv/" + val)
        else:
            print(f"Unhandled UFeat {featstruct}")
            sys.exit(1)
    return giellatags

