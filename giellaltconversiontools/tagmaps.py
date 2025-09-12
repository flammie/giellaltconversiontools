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

# simple 1-to-many mappings
GIELLA2UNIMORPH = {
    "Adv": ["ADV"],
    "Num": ["NUM"],
    "Po": ["ADP"],
    "Pr": ["ADP"],
    "A": ["ADJ"],
    "Interj": ["INTJ"],
    "CC": ["CONJ"],
    "CS": ["CONJ"],
    "Pron": ["PRO"],
    "Neu": ["NEUT"],
    "Fem": ["FEM"],
    "Msc": ["MASC"],
    "Common": ["MASC+FEM"],
    "Gen": ["GEN"],
    "Com": ["COM"],
    "Ses": ["ON+ESS"],
    "Ess": ["FRML"],  # XXX: ESS?
    "Inan": ["INAN"],
    "Anim": ["ANIM"],
    "Abe": ["PRIV"],  # XXX: ABE?
    "Par": ["PRT"],
    "Ins": ["INS"],
    "Ine": ["IN+ESS"],
    "Nom": ["NOM"],
    "Sub": ["ON+ALL"],
    "All": ["AT+ALL"],  # XXX: ALL?
    "Loc": ["PRP"],
    "Inst": ["INST"],
    "Tra": ["TRANS"],
    "Del": ["ON+ABL"],
    "Ela": ["IN+ABL"],
    "Ill": ["IN+ALL"],
    "Dat": ["DAT"],
    "Acc": ["ACC"],
    "Ade": ["AT+ESS"],
    "Abl": ["AT+ABL"],
    "Sg": ["SG"],
    "Du": ["DU"],
    "Pl": ["PL"],
    "Indic": ["IND"],
    "Ind": ["IND"],  # XXX: can sometimes be indef?
    "Prs": ["PRS"],
    "Prt": ["PST"],
    "Perf": ["PRF"],
    "Fut": ["FUT"],
    "Sg1": ["1', 'SG"],
    "Sg2": ["2', 'SG"],
    "Sg3": ["3', 'SG"],
    "Du1": ["1', 'DU"],
    "Du2": ["2', 'DU"],
    "Du3": ["3', 'DU"],
    "Pl1": ["1', 'PL"],
    "Pl2": ["2', 'PL"],
    "Pl3": ["3', 'PL"],
    "4": ["4"],
    "Pe4": ["4"],
    "Ips": ["IMPRS"],
    "ScSg1": ["ARGNO1S"],
    "ScSg2": ["ARGNO2S"],
    "ScSg3": ["ARGNO3S"],
    "ScPl1": ["ARGNO1S"],
    "ScPl2": ["ARGNO2S"],
    "ScPl3": ["ARGNO3S"],
    "OcSg1": ["ARGAC1S"],
    "OcSg2": ["ARGAC2S"],
    "OcSg3": ["ARGAC3S"],
    "OcPl1": ["ARGAC1S"],
    "OcPl2": ["ARGAC2S"],
    "OcPl3": ["ARGAC3S"],
    "PxSP3": ["PSS3"],
    "Px3": ["PSS3"],
    "PxSg1": ["PSS1S"],
    "PxSg2": ["PSS2S"],
    "PxSg3": ["PSS3S"],
    "PxDu1": ["PSS1D"],
    "PxDu2": ["PSS2D"],
    "PxDu3": ["PSS3D"],
    "PxPl1": ["PSS1P"],
    "PxPl2": ["PSS2P"],
    "PxPl3": ["PSS3P"],
    "Def": ["DEF"],
    "Indef": ["NDEF"],
    "VGen": ["V.MSDR', 'GEN"],
    "VAbess": ["V.CVB', 'ABE"],
    "NomAg": ["V.MSDR', 'LGSPEC/agent"],
    "AgPrc": ["V.PTCP', 'LGSPEC/agent"],
    "NegPrc": ["V.PTCP', 'NEG"],
    "NomAct": ["V.MSDR"],
    "INF": ["NFIN"],
    "Inf": ["NFIN"],
    "Ger": ["V.CVB', 'LGSPEC/ger"],  # XXX: GER?
    "Actio": ["V.MSDR', 'LGSPEC/actio"],  # XXX: ???
    "Sup": ["V.CVB', 'LGSPEC/sup"],  # Supine, not superlative or superessive
    "InfA": ["NFIN"],  # fin
    "InfE": ["V.CVB"],  # fin
    "Inf3": ["V.CVB"],  # fkv
    "InfMa": ["V.CVB"],  # fin
    "A_Hum": ["ADJ"],  # fin?
    "Adv-": ["ADV"],
    "Actv": ["ACT"],
    "Act": ["ACT"],
    "Pasv": ["PASS"],
    "Pass": ["PASS"],
    "Pss": ["PASS"],
    "Cond": ["COND"],
    "Pot": ["POT"],
    "Imp": ["IMP"],
    "Imprt": ["IMP"],
    "ImprtII": ["IMP"],
    "Cau": ["CAUS"],
    "Subj": ["SBJV"],
    "Opt": ["OPT"],  # Desiderative optative
    "Des": ["OPT"],  # Desiderative optative
    "Oblig": ["OBGLIG"],
    "Interr": ["INT"],  # XXX: ABE?
    "Der/Comp": ["CMPR"],
    "Comp": ["CMPR"],
    "Compar": ["CMPR"],  # fkv
    "Superl": ["SPRL"],
    "Der/Superl": ["SPRL"],
    "Der/PassS": ["PASS"],
    "Attr": ["LGSPEC9/ATTR"],
    "Pred": ["LGSPEC9/PRED"],
    "Aff": ["POS"],
    "Neg": ["NEG"],
    "NegCnd": ["NEG', 'COND"],
    "NegCndSub": ["NEG', 'COND"],
    "Pos": ["POS"],
    "Qu": ["LGSPEC1/?"],
    "Qst": ["LGSPEC1/?"],
    "Use/Rus": ["DIAL"],
    "Use/Circ": ["XXXCIRC"],
    "Use/Dial": ["DIAL"],
    "Guess": ["XXX"],
    "??": ["XXX"],
    "TODO": ["XXX"],
    "Dial": ["DIAL"],
    "South": ["DIAL?"],
    "Orth/Colloq": ["DIAL?"],
    "Conneg": ["NEG"],  # XXX
    "ConNeg": ["NEG"],  # XXX
    "ConNegII": ["NEG"],  # XXX
    "IV": ["INTR"],
    "TV": ["TR"],
    "Impers": ["IMPRS"],
    "Reflex": ["REFL"],
    "Refl": ["REFL"],
    "Recipr": ["RECP"],
    "Distr": ["REM"],
    "Dist": ["REM"],
    "Prox": ["PROXM"],
    "TruncPrefix": ["LGSPEC/prefix-"],
    "Pref": ["LGSPEC/prefix-"],
    "Prefix": ["LGSPEC/prefix-"],
    "PrsPrc": ["PRS"],
    "PrtPrc": ["PST"],
    "PrfPrc": ["PRFV"],
    "Prc/Telic": ["LGSPEC/telic"],  # myv
    "Foc": ["LGSPEC/foc"],
    "Clit": ["LGSPEC/clit"],
    "Clt": ["LGSPEC/clit"],
    "Long": [],
    "Allegro": [],
    "Sh": [],
    "Largo": [],
    "ABBR-": [],
    "ABBR": [],
    "ACRO": [],
    "LEFT": [],
    "RIGHT": [],
    "Dim/ke": [],
    "Dummytag": [],
    "S": [],
    "Quote": [],
    "CLB": [],
    "Bahuvrihi": [],  # myv
    "AssocColl": [],  # myv
    "Adn": [],  # myv
    "Conj": [],  # myv
    "Prec": [],  # myv
    "Quot": [],  # est
    "Prel": [],  # fit
    "Dem": [],  # FIXME
    "Pers": [],  # FIXME
    "Disc": [],
    "ACR": [],
    "Coll": [],
    "Subqst": [],
    "Rel": [],  # is not: Relative case or Relative comparator
    "Ord": [],
    "Prop": [],  # handled elsehwere
    "Der1": [],
    "Der2": [],
    "v1": [],
    "v2": [],
    "v3": [],
    "v4": [],
    "v5": [],
    "v6": [],
    "v7": [],
    "v8": [],
    "v9": [],
    "G1": [],
    "G2": [],
    "G3": [],
    "G4": [],
    "G5": [],
    "G6": [],
    "G7": [],
    "G8": [],
    "G9": [],
}

UNIMORPH2GIELLA = {
    "N": ["+N"],
    "PROPN": ["+N", "+Prop"],
    "V": ["+V"],
    "AUX": ["+V", "+Aux"],
    "COP": ["+V", "+Cop"],
    "ADJ": ["+A"],
    "ADV": ["+Adv"],
    "ADP": ["+Adp"],
    "PRO": ["+Pron"],
    "NUM": ["+Num"],
    "CONJ": ["+C"],
    "DET": ["+Det"],
    "ART": ["+Art"],
    "INTJ": ["+Interj"],
    "PART": ["+Part"],
    "Cop": ["+Cop"],
    "NEUT": ["+Neu"],
    "MASC": ["+Msc"],
    "FEM": ["+Fem"],
    "MASC+FEM": ["+Common"],
    "MASC+FEM+NEUT": ["+Common"],
    "MASC+NEUT": ["+Ut"],
    "ERG": ["+Erg"],
    "ABS": ["+Abs"],
    "OBL": ["+Obl"],
    "GEN": ["+Gen"],
    "COM": ["+Com"],
    "ON+ESS": ["+Ses"],
    "FRML": ["+Ess"],
    "ESS": ["+Ess"],
    "BYWAY": ["+Ess"],
    "INAN": ["+Inan"],
    "HUM": ["+Sem/Human"],
    "ANIM": ["+Anim"],
    "PRIV": ["+Abe"],
    "PRT": ["+Par"],
    "INS": ["+Ins"],
    "IN+ESS": ["+Ine"],
    "IN": ["+Ine"],
    "NOM": ["+Nom"],
    "SUP": ["+Super"],
    "SUB": ["+Sub"],
    "ON+ALL": ["+Sub"],
    "AT+ALL": ["+All"],
    "ALL": ["+All"],
    "PRP": ["+Instr"],
    "LOC": ["+Loc"],
    "VOC": ["+Voc"],
    "INST": ["+Inst"],
    "TRANS": ["+Tra"],
    "PROL": ["+Prl"],
    "TERM": ["+Term"],
    "COMPV": ["+Compv"],
    "REL": ["+Relv"],
    "ON+ABL": ["+Del"],
    "IN+ABL": ["+Ela"],
    "IN+ALL": ["+Ill"],
    "DAT": ["+Dat"],
    "ACC": ["+Acc"],
    "AT": ["+Loc"],
    "AT+ESS": ["+Ade"],
    "AT+ABL": ["+Abl"],
    "ABL": ["+Abl"],
    "SG": ["+Sg"],
    "DU": ["+Du"],
    "PL": ["+Pl"],
    "SG+PL": [],  # ["+Sg/Pl"]
    "IND": ["+Ind"],
    "PRS": ["+Prs"],
    "PST": ["+Prt"],
    "RCT": [],
    "PRF": ["+Perf"],
    "FUT": ["+Fut"],
    "NFUT": ["+Prs"],  # usually
    "PROG": ["+Prog"],
    "HOD": ["+Hod"],
    "0": ["+Pe0"],
    "1": ["+1"],
    "2": ["+2"],
    "3": ["+3"],
    "4": ["+Pe4"],
    "INCL": ["+Incl"],
    "EXCL": ["+Excl"],
    "INDF": [],  # unmarked in giellatags
    "GEADJ": ["+Error", "+Gen"],  # bug in fin
    "BEADJ": ["+Error", "+Adj"],
    "DEF": ["+Def"],
    "NDEF": ["+Ind"],
    "REFL": ["+Reflex"],
    "RECP": ["+Recipr"],
    "FIN": [],
    "NFIN": ["+Inf"],
    "TR": ["+TV"],
    "INTR": ["+IV"],
    "ACT": ["+Actv"],
    "PASS": ["+Pasv"],
    "COND": ["+Cond"],
    "OPT": ["+Opt"],
    "POT": ["+Pot"],
    "IMP": ["+Imprt"],
    "FREQ": ["+Freq"],
    "CAUS": ["+Caus"],
    "DEB": ["+Deb"],
    "ADM": ["+Adm"],
    "SBJV": ["+Subj"],
    "V.CVB": ["+V", "+Der/Adv"],
    "V.MSDR": ["+V", "+Der/Noun"],
    "V.PTCP": ["+V", "+Der/Adj"],
    "CMPR": ["+Comp"],
    "SPRL": ["+Sup"],
    "NEG": ["+Neg"],
    "POS": [],  # ["+Pos"]
    "LGSPEC": [],
    "LGSPEC1": [],
    "LGSPEC2": [],
    "LGSPEC3": [],
    "LGSPEC4": [],
    "LGSPEC5": [],
    "LGSPEC6": [],
    "LGSPEC7": [],
    "LGSPEC8": [],
    "LGSPEC9": [],
    "LGSPEC10": [],  # 9 is allowed maximum...
    "LGSPEC0": [],
    "LGSPEC01": [],
    "LGSPEC11": [],
    "LGSPEC12": [],
    "LGSPEC13": [],
    "LGSPEC14": [],
    "LGSPEC15": [],
    "LGSPEC16": [],
    "LGSPEC02": [],
    "LGSPEC03": [],
    "LGSPEC04": [],
    "LGSPEC05": [],
    "LGSPEC06": [],
    "LGSPEC07": [],
    "LGSPEC08": [],
    "LGSPEC09": [],
    "PSSRS": ["+PxSgFIXME"],
    "PSSRP": ["+PxPlFIXME"],
    "PSSB1": ["+PxFIXME1"],
    "PSSB5": ["+PxFIXME1"],
    "PSSD": ["+Px"],
    "PSS0": ["+Px0"],
    "PSS1": ["+Px1"],
    "PSS2": ["+Px2"],
    "PSS1S": ["+PxSg1"],
    "PSS1SM": ["+PxSg1Msc"],
    "PSS1SF": ["+PxSg1Fem"],
    "PSS2S": ["+PxSg2"],
    "PSS2SM": ["+PxSg2Msc"],
    "PSS2SF": ["+PxSg2Fem"],
    "PSS2PF": ["+PxPl2Fem"],
    "PSS3S": ["+PxSg3"],
    "PSS3SM": ["+PxSg3Msc"],
    "PSS3SF": ["+PxSg3Fem"],
    "PSS1D": ["+PxDu1"],
    "PSS2D": ["+PxDu2"],
    "PSS3D": ["+PxDu3"],
    "PSS1P": ["+PxPl1"],
    "PSS1PL": ["+PxPl1"],
    "PSS1I": ["+Px1Incl"],
    "PSS1PE": ["+PxPl1Excl"],
    "PSS1PI": ["+PxPl1Incl"],
    "PSS2P": ["+PxPl2"],
    "PSS2PM": ["+PxPl2Msc"],
    "PSS3P": ["+PxPl3"],
    "PSS3PM": ["+PxPl3Msc"],
    "PSS3PF": ["+PxPl3Fem"],
    "PSS3": ["+Px3"],
    "PSS3M": ["+Px3Msc"],
    "PSS3F": ["+Px3Fem"],
    "PSS4": ["+Px4"],
    "PFV": ["+Pfv"],
    "TOP": ["+Topic"],
    "FOC": ["+Focus"],
    "HAB": ["+Hab"],
    "INFM": ["+Infm"],
    "REAL": ["+Real"],
    "IPFV": ["+Imperf"],
    "POL": ["+Polite"],
    "FORM": ["+Formal"],
    "FOREG": ["+Formal"],
    "COL": ["+Coll"],
    "INV": ["+Inverse"],
    "IRR": ["+Irreal"],
    "PROSP": ["+Prosp"],
    "RMT": ["+Remote"],
    "MED": ["+Med"],
    "PROX": ["+Prox"],
    "IMMED": ["+Immed"],
    "QUOT": ["+Quot"],
    "APPL": ["+Appl"],
    "DECL": ["+Decl"],
    "ARGIOINFM": [],   # ???
    "ARGIOMASC": [],   # ???
    "ARGIO1": [],   # ???
    "ARGIO2": [],   # ???
    "ARGIO3": [],   # ???
    "ARGIOPL": [],   # ???
    "ARGIOSG": [],   # ???
    "ARGNO1S": ["+ScSg1"],
    "ARGNO2S": ["+ScSg2"],
    "ARGNO3S": ["+ScSg3"],
    "ARGNO1P": ["+ScPl1"],
    "ARGNO2P": ["+ScPl2"],
    "ARGNO3P": ["+ScPl3"],
    "ARGABS3": ["+Ac3"],
    "ARGAB3S": ["+AcSg3"],
    "ARG1": ["+Sc1"],
    "ARG2": ["+Sc1"],
    "ARG3": ["+Sc3"],
    "ARGSG": ["+ScSg"],
    "ARGDU": ["+ScDu"],
    "ARGPL": ["+ScPl"],
    "ARGABSSG": ["+AcSg"],
    "ARGAB1S": ["+AcSg1"],
    "ARGAB1P": ["+AcPl1"],
    "ARGAB3P": ["+AcPl3"],
    "ARGAC3SG": ["+AcSg3"],
    "ARGAC3SGHUM": ["+AcSg3Hum"],
    "ARGAC1S": ["+AcSg1"],
    "ARGAC3S": ["+AcSg3"],
    "ARGAC1": ["+Ac1"],
    "ARGAC1P": ["+AcPl1"],
    "ARGAC1PL": ["+AcPl1"],
    "ARGAC2": ["+Ac2"],
    "ARGAC2P": ["+AcPl2"],
    "ARGAC2S": ["+AcSg2"],
    "ARGAC1DU": ["+AcDu1"],
    "ARGAC2DU": ["+AcDu2"],
    "ARGAC3DU": ["+AcDu3"],
    "ARGAC3P": ["+AcPl3"],
    "ARGAC3PL": ["+AcPl3"],
    "ARGER1S": ["+EcSg1"],
    "ARGER3S": ["+EcSg3"],
    "ARGER1P": ["+EcPl1"],
    "ARGBE1S": ["+BcSg1"],
    "ARGBE2P": ["+BcPl2"],
    "ARGEXCL": ["+AcExcl"],
    "ARGINCL": ["+AcIncl"],
    # Unsorted / misspelt / bugs:
    "NO1": [],  # ?
    "NO1P": [],  # ?
    "NO2": [],  # ?
    "NO1S": [],  # ?
    "NO2P": [],  # ?
    "NO2S": [],  # ?
    "NO3P": [],  # ?
    "NO3S": [],  # ?
    "NO3PA": [],  # ?
    "NO3M": [],  # ?
    "NO1PI": [],  # ?
    "NO1PE": [],  # ?
    "NO1PA": [],  # ?
    "NO3SI": [],  # ?
    "AC1S": [],  # ?
    "CAUSV": [],  # ?
    "LIT": [],  # ?
    "BEN": [],  # ?
    "DED": [],  # ?
    "ELEV": [],  # ?
    "FORM2": [],  # ?
    "MPOL": [],  # ?
    "INTER": [],  # ?
    "INDF1": [],  # ?
    "INDF2": [],  # ?
    "DRCT": [],  # ?
    "SIM": [],  # ?
    "ITER": [],  # ?
    "OBLIG": [],  # ?
    "PROPR": ["+Error", "+N", "+Prop"],
    "AUTO": [],  # ?
    "ANTIP": [],  # ?
    "INCH": [],  # ?
    "INT": [],  # ?
    "INF": [],  # ?
    "INFN": [],  # ?
    "REMT": [],  # ?
    "APPRX": [],  # ?
    "CF": [],  # ?
    "PFOC": [],  # ?
    "SL": [],  # ?
    "PC": [],  # ?
    "ER": [],  # ?
    "FH": [],  # ?
    "DIM": [],  # ?
    "PFA": [],  # ?
    "ALN": [],  # ?
    "NALN": [],  # ?
    "RPRT": [],  # ?
    "ACTY": ["+Error", "+Act"],  # ?
    "PRON": ["+Error", "+Pron"],  # ?
    "CVB": ["+Error"],  # ?
    "MSDR": ["+Error"],  # ?
    "V.NFIN": ["+Error"],  # ?
    "V.PCTP": ["+Error"],  # ?
    "V.PTCP.PST": ["+Error"],  # ?
    "V.PTCP.PRS": ["+Error"],  # ?
    "SUBJ": [],  # ?
    "DUR": [],  # ?
    " N": ["+Error"],  # ?
    " PSS1S": ["+Error"],  # ?
    "STAT": [],  # ?
    "WEAK": [],  # ?
    "STRONG": [],  # ?
    "PRES": ["+Error"],  # ?
    "SIMMA": [],  # ?
    "NO3": [],  # ?
    "NO3F": [],  # ?
    "NO3SA": [],  # ?
    "AB": [],  # ?
    "AC1": [],  # ?
    "AC2": [],  # ?
    "AC3": [],  # ?
    "AC2P": [],  # ?
    "AC3P": [],  # ?
    "INDF3": [],  # ?
    "BANTU1": ["+Bantu1"],  # ?
    "BANTU2": ["+Bantu2"],  # ?
    "BANTU3": ["+Bantu3"],  # ?
    "BANTU4": ["+Bantu4"],  # ?
    "BANTU5": ["+Bantu5"],  # ?
    "BANTU6": ["+Bantu6"],  # ?
    "BANTU7": ["+Bantu7"],  # ?
    "BANTU8": ["+Bantu8"],  # ?
    "BANTU9": ["+Bantu9"],  # ?
    "BANTU10": ["+Bantu10"],  # ?
    "BANTU11": ["+Bantu11"],  # ?
    "BANTU12": ["+Bantu12"],  # ?
    "BANTU13": ["+Bantu13"],  # ?
    "BANTU14": ["+Bantu14"],  # ?
    "BANTU15": ["+Bantu15"],  # ?
    "BANTU16": ["+Bantu16"],  # ?
    "BANTU17": ["+Bantu17"],  # ?
    "BANTU18": ["+Bantu18"],  # ?
    "BANTU19": ["+Bantu19"],  # ?
    "BANTU20": ["+Bantu20"],  # ?
    "AGFOC": [],  # ?
    "TEL": [],  # ?
    "INFR": [],  # ?
    "DISTR": [],  # ?
    "AGT": [],  # ?
    "NPST": [],  # ?
    "PTCP": ["+Error", "+Der/Adj"],  # ?
    "NFH": [],  # ?
    "MID": [],  # ?
    "SS": [],  # ?
    "DS": [],  # ?
    "EXCLV": [],  # ?
    "PURP": [],  # ?
    "EQTV": [],  # ?
    "INTEN": [],  # ?
    "MASV": [],  # ?
    "SEMEL": [],  # ?
    "_": [],  # ?
    "": ["+Error"],  # ?
    "LgSPEC8": ["+Error"],  # ?
    "LGSEPC1": ["+Error"],  # ?
    "LSGSPEC1": ["+Error"],  # ?
    "LSGSPEC2": ["+Error"],  # ?
    "LGSEPC2": ["+Error"],  # ?
    "PRS/FUT": [],  # ?
    "PRS/PST": [],  # ?
    "NOM/ACC": [],  # ?
    "NOM/ACC/DAT": [],  # ?
    "DAT/GEN": [],  # ?
    "GEN/DAT": [],  # ?
    "ADJ/GEN": [],  # ?
    "MASC/FEM": [],  # ?
    "PSS3S/PSS3P": [],  # ?
    "LGSPEC1/LGSPEC2": [],  # ?
}

def giella2unimorph(tags):
    unimorphtags = []
    for giella in tags.split("+"):
        if giella in GIELLA2UNIMORPH:
            unimorphtags += GIELLA2UNIMORPH[giella]
        elif giella == "":
            continue
        elif giella == "N":
            if "Prop" in tags:
                unimorphtags += ["PROPN"]
            else:
                unimorphtags += ["N"]
        elif giella == "V":
            if "+PrsPrc" in tags:
                unimorphtags += ["V.PTCP"]
            elif "+PrtPrc" in tags:
                unimorphtags += ["V.PTCP"]
            elif "+PrfPrc" in tags:
                unimorphtags += ["V.PTCP"]
            else:
                unimorphtags += ["V"]
        elif giella.startswith("Err/"):
            unimorphtags += ["TYPO"]
        elif giella.startswith("Errr/"):
            unimorphtags += ["TYPO"]
        elif giella.startswith("Der/"):  # some der's should be handled before
            unimorphtags += ["XXXDER" + giella[4:]]
            continue
        elif giella.startswith("Pref-"):
            continue
        elif giella.startswith("Qst/"):
            unimorphtags += ["LGSPEC/?" + giella[4:]]
        elif giella.startswith("Sem"):
            continue
        elif giella.startswith("Cmp"):
            unimorphtags += ["XXXCOMPOUND"]
            continue  # ?
        elif giella.startswith("Use/"):
            unimorphtags += ["XXX" + giella[4:]]
        elif giella.startswith("Usage/"):
            unimorphtags += ["XXX" + giella[6:]]
        elif giella in ["0,0", "0,1"]:
            continue
        elif giella in ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9",
                        "F00", "F01", "F02", "F03", "F04", "F05", "F06", "F07",
                        "F10", "F11", "F12", "F13", "F14", "F15", "F16", "F08",
                        "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24",
                        "F25", "F26", "F27", "F28", "F29", "F30", "F31", "F09",
                        "F32", "F33", "F34", "F35", "F36", "F37", "F38", "F0",
                        "F39", "F40", "F41", "F42", "F43", "F44", "F45",
                        "F46", "F47", "F48", "F49", "F50", "F51", "F52", "F53",
                        "F54", "F55", "F56", "F57", "F58", "F59", "F60", "F61",
                        "F62", "F63", "F64", "F65", "F66", "F67", "F68",
                        "F69", "F70", "F71", "F72", "F73", "F74", "F75", "F76",
                        "F77", "F78", "F79", "F80", "F81", "F82", "F83", "F84",
                        "F85", "F86", "F87", "F88", "F89", "F90", "F91", "F92",
                        "F93", "F94", "F95", "F96", "F97", "F98", "F99",
                        "F100", "Enter", "Alt", "Shift",
                        "B", "C", "E", "D", "F", "G", "H", "I", "J", "K", "L",
                        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X",
                        "Y", "Z",
                        "Š", "Ž", "Ä", "Õ", "Ö", "Ü", "0"]:
            # est
            continue
        elif giella.startswith("Foc/"):
            unimorphtags += ["LGSPEC1/" + giella[4:]]
        elif giella.startswith("Clit/"):
            unimorphtags += ["LGSPEC1/" + giella[5:]]
        elif giella.startswith("Clt/"):
            unimorphtags += ["LGSPEC2/" + giella[4:]]
        elif giella.startswith("OLang/"):
            continue
        elif giella.startswith("Gram/"):
            continue
        elif giella.startswith("Hom"):
            continue
        elif giella.startswith("Genmiessi"):
            print("SOmething broken here½!", tags)
        elif "@" in giella:
            print("SOmething broken here½!", tags)
        elif giella.startswith("NErr/"):
            print("SOmething broken here½!", tags)
            unimorphtags += ["TYPO"]
        elif giella.startswith("AErr/"):
            print("SOmething broken here½!", tags)
            unimorphtags += ["TYPO"]
        elif "<cnjcoo>" in giella:
            print("SOmething broken here½!", tags)
        elif "<actv>" in giella:
            print("SOmething broken here½!", tags)
        elif "<gen>" in giella:
            print("SOmething broken here½!", tags)
        elif "N224-1-9" in giella:
            print("SOmething broken here½!", tags)
        elif "#222-5-19" in giella:
            print("SOmething broken here½!", tags)
        elif "/-" in giella:
            print("SOmething broken here½!", tags)
        elif giella in ["a", "b", "i", "t", "d", "s", "n", "ä", "ö"]:
            print("SOmething broken here½!", tags)
        elif giella in ["Ne", "Ni", "Nte", "Ntee", "Nt", "Nti", "Na", "No",
                        "N-", "c"]:
            print("SOmething broken here½!", tags)
        elif "elekriski" in giella:
            print("SOmething broken here½!", tags)
        elif giella.startswith("Err/"):
            unimorphtags += ["TYPO"]
        elif giella.startswith("Der/"):
            continue  # NB: handle SOME ders before this
        elif giella.startswith("Cmp"):
            continue  # ?
        elif giella.startswith("Sem"):
            continue
        elif giella.startswith("Foc/"):
            unimorphtags += ["LGSPEC1/" + giella[5:]]
        else:
            print("missing giella mapping for", giella, "in tags")
            sys.exit(2)
    # shuffle and patch
    CASESWITHOUTNUMBERS = ["FRML", "COM"]
    for casetag in CASESWITHOUTNUMBERS:
        if casetag in unimorphtags and "SG" not in unimorphtags and\
                "PL" not in unimorphtags:
            unimorphtags += ["SG"]
    MOODSWITHEXTRATENSE = ["COND", "POT"]
    for mood in MOODSWITHEXTRATENSE:
        if mood in unimorphtags and "PRS" in unimorphtags:
            unimorphtags.remove("PRS")
        elif mood in unimorphtags and "PST" in unimorphtags:
            unimorphtags.remove("PST")
    return ";".join(unimorphtags)


def unimorph2giella(unimorphs: str) -> list:
    giellatags = []
    for unimorph in unimorphs.split(";"):
        if unimorph in UNIMORPH2GIELLA:
            giellatags += UNIMORPH2GIELLA[unimorph]
        elif unimorph.startswith("non{") and unimorph.endswith("}"):
            # we don't have such negated tags...
            # should just print multiple lines or so
            continue
        elif unimorph.startswith("non(") and unimorph.endswith(")"):
            # typoed {}
            giellatags += ["+Error"]
        elif unimorph.startswith("(non)"):
            # typoed non()
            giellatags += ["+Error"]
        elif unimorph.startswith("not{") and unimorph.endswith("}"):
            # typoed non
            giellatags += ["+Error"]
        elif unimorph.startswith("not(") and unimorph.endswith(")"):
            # typoed non
            giellatags += ["+Error"]
        elif "+" in unimorph:
            for subtag in unimorph.split("+"):
                if subtag in UNIMORPH2GIELLA:
                    giellatags += UNIMORPH2GIELLA[subtag]
                else:
                    print(f"missing unimorph {subtag} in {unimorph} "
                          f"in {unimorphs}")
                    sys.exit(1)
        elif "/" in unimorph:
            # FIXME: or tags should possibly print multiple lines
            for subtag in unimorph.split("/"):
                if subtag in UNIMORPH2GIELLA:
                    giellatags += UNIMORPH2GIELLA[subtag]
                else:
                    print(f"missing unimorph {subtag} in {unimorph} "
                          f"in {unimorphs}")
                    sys.exit(1)
        elif "," in unimorph:
            # usually , instead of ;
            giellatags += ["+Error"]
        elif ":" in unimorph:
            # usually : instead of ;
            giellatags += ["+Error"]
        elif unimorph == "V.PTCP":
            giellatags += ["+V"]
            if "PRS" in unimorphs:
                giellatags += ["+PrsPrc"]
            elif "PST" in unimorphs:
                giellatags += ["+PrtPrc"]
            elif "FUT" in unimorphs:
                giellatags += ["+Fut"]
            else:
                giellatags += ["+Drv/Ptcp"]
        else:
            print(f"missing unimorph mapping for {unimorph} in {unimorphs}")
            sys.exit(2)
    reorg = []
    # pos
    for ape in giellatags:
        if ape in ["+N", "+V", "+A", "+Adv", "+Part", "+Num", "+Pron",
                   "+Interj", "+Adp", "+C", "+Det", "+Error"]:
            reorg += [ape]
            break
    if reorg == ["+N"]:
        for ape in giellatags:
            if ape in ["+Sg", "+Pl", "+Du"]:
                reorg += [ape]
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+V"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
        if "+1" in reorg and "+Sg" in reorg:
            reorg += ["+Sg1"]
            reorg.remove("+1")
            reorg.remove("+Sg")
        elif "+2" in reorg and "+Sg" in reorg:
            reorg += ["+Sg2"]
            reorg.remove("+2")
            reorg.remove("+Sg")
        elif "+3" in reorg and "+Sg" in reorg:
            reorg += ["+Sg3"]
            reorg.remove("+3")
            reorg.remove("+Sg")
        elif "+1" in reorg and "+Du" in reorg:
            reorg += ["+Du1"]
            reorg.remove("+1")
            reorg.remove("+Du")
        elif "+2" in reorg and "+Du" in reorg:
            reorg += ["+Du2"]
            reorg.remove("+2")
            reorg.remove("+Du")
        elif "+3" in reorg and "+Du" in reorg:
            reorg += ["+Du3"]
            reorg.remove("+3")
            reorg.remove("+Du")
        elif "+1" in reorg and "+Pl" in reorg:
            reorg += ["+Pl1"]
            reorg.remove("+1")
            reorg.remove("+Pl")
        elif "+2" in reorg and "+Pl" in reorg:
            reorg += ["+Pl2"]
            reorg.remove("+2")
            reorg.remove("+Pl")
        elif "+3" in reorg and "+Pl" in reorg:
            reorg += ["+Pl3"]
            reorg.remove("+3")
            reorg.remove("+Pl")
    elif reorg == ["+A"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Adv"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Pron"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Part"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Adp"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Num"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Det"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+C"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Interj"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    elif reorg == ["+Error"]:
        for ape in giellatags:
            if ape not in reorg:
                reorg += [ape]
    else:
        print(f"REORG FAIL {reorg} for {giellatags}")
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

