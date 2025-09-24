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

UPOS2GIELLA = {
    "NOUN": ["+N"],
    "VERB": ["+V"],
    "ADJ": ["+A"],
    "ADV": ["+Adv"],
    "ADP": ["+Adp"],
    "CCONJ": ["+CC"],
    "SCONJ": ["+CS"],
    "PUNCT": ["+Punct"],
    "SYM": ["+Sym"],
    "PRON": ["+Prn"],
    "DET": ["+Det"],
    "NUM": ["+Num"],
    "INTJ": ["+Interj"],
    "PROPN": ["+N", "+Prop"],
    "AUX": ["+V", "+Aux"],
    "PART": ["+Pcle"],
    "X": ["+X"],
}

UFEATS2GIELLA = {
        "Case=Nom": ["+Nom"],
        "Case=Gen": ["+Gen"],
        "Case=Dat": ["+Dat"],
        "Case=Par": ["+Par"],
        "Case=Ins": ["+Ins"],
        "Case=Ill": ["+Ill"],
        "Case=Abl": ["+Abl"],
        "Case=Tra": ["+Tra"],
        "Case=All": ["+All"],
        "Case=Abe": ["+Abe"],
        "Case=Ade": ["+Ade"],
        "Case=Ine": ["+Ine"],
        "Case=Ela": ["+Ela"],
        "Case=Loc": ["+Loc"],
        "Case=Ess": ["+Ess"],
        "Case=Com": ["+Com"],
        "Case=Voc": ["+Voc"],
        "Case=Del": ["+Del"],
        "Case=Sbl": ["+Sub"],
        "Case=Sup": ["+Super"],
        "Case=Cau": ["+Cau"],
        "Case=Lat": ["+Lat"],
        "Case=Dis": ["+Dis"],
        "Case=Abs": ["+Abs"],
        "Case=Tem": ["+Tem"],
        "Case=Ter": ["+Ter"],
        "Case=Acc": ["+Acc"],
        "Case=Prl": ["+Prl"],
        "Case=Ben": ["+Ben"],
        "Case=Mal": ["+Mal"],
        "Case=Cmp": ["+Compv"],
        "Case=Acc,Nom": ["+Acc", "+Nom"],
        "Case=Gen,Nom": ["+Gen", "+Nom"],
        "Gender=Masc": ["+Msc"],
        "Gender=Fem,Masc": ["+Common"],
        "Gender=Masc,Neut": ["+Ut"],
        "Gender=Fem": ["+Fem"],
        "Gender=Neut": ["+Neut"],
        "Gender[psor]=Fem": ["+PxFem"],
        "Gender[psor]=Masc": ["+PxMasc"],
        "Gender[abs]=Neut": [],  # ?
        "Gender[obj]=Masc": [],
        "Animacy=Anim": ["+Sem/Animate"],
        "Animacy=Inan": ["+Sem/Inanimate"],
        "Animacy=Hum": ["+Sem/Human"],
        "Mood=Ind": ["+Ind"],
        "Mood=Imp": ["+Imp"],
        "Mood=Cnd": ["+Cond"],
        "Mood=Pot": ["+Pot"],
        "Mood=CndSub": ["+CndSubj"],
        "Mood=Sub": ["+Subj"],
        "Mood=Opt": ["+Opt"],
        "Mood=Jus": ["+Jus"],
        "Mood=Proh": ["+Proh"],
        "Mood=Prec": ["+Prec"],
        "Mood=Nec": ["+Nec"],
        "Mood=Des": ["+Des"],
        "Mood=Imp,Ind": ["+Imp", "+Ind"],
        "Mood=Imp,Pot": ["+Imp", "+Pot"],
        "Mood=Cnd,Pot": ["+Eve"],
        "Aspect=Compl": [],
        "Aspect=Frus": [],
        "Aspect=Freq": ["+Freq"],
        "Aspect=Aor": ["+Past"],
        "Aspect=Imp": ["+Imp"],
        "Aspect=Hab": ["+Hab"],
        "Aspect=Prog": ["+Prog"],
        "Aspect=ProgNeg": ["+Prog", "+Neg"],
        "Aspect=ProgBkg": ["+Prog"],  # XXX
        "Aspect=ProgLocBkg": ["+Prog"],  # XXX
        "Aspect=PerfNeg": ["+Perf", "+Neg"],
        "Aspect=Perf": ["+Perf"],
        "Aspect=PerfBkg": ["+Perf"],  # XXX
        "Aspect=Iter": ["+Iter"],
        "Number=Ptan": ["+Pl"],  # XXX
        "Number=Plur,Sing": [],  # ???
        "Number[psor]=Sing": [],  # c.f. Person[psor]
        "Number[psor]=Dual": [],  # c.f. Person[psor]
        "Number[psor]=Plur": [],  # c.f. Person[psor]
        "Number[psed]=Sing": ["+Der/PxSg"],
        "Number[psed]=Plur": ["+Der/PxPl"],
        "Number[subj]=Sing": [],  # c.f. Person[subj]
        "Number[subj]=Plur": [],  # c.f. Person[subj]
        "Number[subj]=Plur,Sing": [],  # c.f. Person[subj]
        "Number[obj]=Sing": [],  # c.f. Person[obj]
        "Number[obj]=Plur": [],  # c.f. Person[obj]
        "Number[grnd]=Sing": [],  # c.f. Person[grnd]
        "NumType=Card": ["+Card"],
        "NumType=Ord": ["+Ord"],
        "NumType=OrdSets": [],
        "NumType=OrdMult": [],
        "NumType=Mult": [],
        "NumType=Frac": [],
        "NumType=Dist": [],
        "NumType=Appr": [],
        "NumType=Coll": [],
        "NumType=Sets": [],
        "AdvType=Cau": [],
        "AdvType=Con": [],
        "AdvType=Sta": [],
        "AdvType=Mod": [],
        "AdvType=Loc": [],
        "AdvType=Deg": [],
        "AdvType=Tim": [],
        "AdvType=Man": [],
        "AdvType=Ideoph": [],
        "Person=4": ["+Impersonal"],  # FIXME
        "Person=0": ["+Impersonal"],  # FIXME
        "PronType=Ind,Prs": ["+Indef", "+Pers"],
        "PronType=Ind": ["+Indef"],
        "PronType=Prs": ["+Pers"],
        "PronType=Prs,Tot": ["+Pers"],
        "PronType=Rel": ["+Rel"],
        "PronType=Dem": ["+Dem"],
        "PronType=Dem,Ind": ["+Dem", "+Ind"],
        "PronType=Int": ["+Interr"],
        "PronType=Int,Rel": ["+Interr", "+Rel"],
        "PronType=Rcp": ["+Recipr"],
        "PronType=Art": ["+Art"],
        "PronType=Art,Prs": ["+Art", "+Pers"],
        "PronType=Tot":  [],
        "PronType=Emp":  [],
        "PronType=Neg":  ["+Neg"],
        "AdjType=Attr":  ["+Attr"],
        "Polarity=Pos": [],
        "Polarity=Neg":  ["+Neg"],
        "Tense=Pres": ["+Prs"],
        "Tense=Past": ["+Prt"],
        "Tense=Pqp": ["+Pqp"],
        "Tense=Fut": ["+Fut"],
        "Tense=Pred": ["+Pred"],
        "Voice=Act": ["+Act"],
        "Voice=Pass": ["+Pass"],
        "Voice=Rcp": ["+Rcp"],
        "Voice=Cau": ["+Cau"],
        "Voice=Mid": ["+Mid"],
        "Voice=Mid,Pass": ["+Mid", "+Pass"],
        "Voice=Stat": ["+Stat"],
        "Voice=Trans": ["+Trans"],
        "Degree=Pos": [],  # ?
        "Degree=Cmp": ["+Comp"],
        "Degree=Sup": ["+Sup"],
        "Degree=Aug": ["+Aug"],
        "Degree=Dim": ["+Dim"],
        "VerbType=Aux": ["+Aux"],
        "VerbType=Cop": ["+Cop"],
        "PartForm=Pres": ["+PrsPrc"],
        "PartForm=Past": ["+PrtPrc"],
        "PartForm=Agt": ["+AgPrc"],
        "PartForm=Neg": ["+NegPrc"],
        "PartForm=NegConvPrc": ["+NegConvPrc"],
        "PartForm=PastDyn": [],
        "PartForm=PrsDet": [],
        "PartForm=PrsTra": [],
        "Definite=Ind": ["+Indef"],
        "Definite=2": ["+Def2"],
        "Definite=Def": ["+Def"],
        "Definite=Spec": ["+Spec"],  # XXX
        "Definite=Cons": ["+Cons"],  # XXX
        "Definite=Com": ["+Com"],  # XXX
        "Definite=Def,Ind": [],  # ???
        "Deixis=Prox": ["+Prox"],
        "Deixis=Remt": ["+Dist"],
        "Valency=1": ["+IV"],
        "Valency=2": ["+TV"],
        "Abbr=Yes": ["+Abbr"],
        "Poss=Yes": ["+Poss"],
        "Reflex=Yes": ["+Reflex"],
        "Connegative=Yes": ["+ConNeg"],
        "Typo=Yes": ["+Err/Orth"],
        "Style=Slng": ["+Use/Nonstd"],
        "Style=Coll": ["+Use/Nonstd"],
        "Style=Vrnc": ["+Use/Nonstd"],
        "Style=Rare": ["+Use/Nonstd"],
        "Style=Expr": ["+Use/Nonstd"],
        "Style=Arch": ["+Use/Arch"],
        "Rel=Abs": [],
        "Rel=NCont": [],
        "Rel=Cont": [],
        "NumForm=Word": [],
        "NumForm=Combi": [],  # XXX
        "NumForm=Roman": ["+Roman"],
        "NumForm=Digit": ["+Arab"],
        "PartType=Prs": ["+PrsPrc"],
        "PartType=Neg": ["+NegPrc"],
        "PartType=Emp": ["+Foc"],
        "PartType=Int": ["+Interr"],
        "PartType=Mod": [],
        "PartType=Exs": [],
        "PartType=Inf": ["+Inf"],  # doesnt make sense
        "Foreign=Yes": ["+Lang/Und"],
        "Variant=Short": ["+Allegro"],
        "Variant=Long": ["+Adagio"],
        "Evident=Nfh": [],
        "Evident=Fh": [],
        "NounType=Relat": [],
        "NounType=Het": [],
        "NegationType=Contrastive": [],
        "PunctType=Elip": [],
        "PunctSide=Ini": [],
        "PunctSide=Fin": [],
        "Red=Yes": [],
        "Modality=Proh": [],
        "Modality=Cond": ["+Cond"],
        "Foc=Yes": ["+Foc"],
        "Compound=Yes": [],  # XXX #+cmp should go in the middle?
        "NounBase=Bound": [],
        "NounBase=Free": [],
        "Subcat=Tran": ["+TV"],
        "Subcat=Intr": ["+IV"],
        "TV=Yes": ["+TV"],
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
    if upos in UPOS2GIELLA:
        giellatags += UPOS2GIELLA[upos]
    elif upos == "_":
        pass
    else:
        print(f"Unhandled upos {upos}")
        sys.exit(1)
    for featstruct in feats.split("|"):
        if featstruct == "_":
            continue
        feat, val = featstruct.split("=")
        if featstruct in UFEATS2GIELLA:
            giellatags += UFEATS2GIELLA[featstruct]
        elif featstruct == "AdpType=Prep":
            giellatags.remove("+Adp")
            giellatags.insert(0, "+Pr")
        elif featstruct == "AdpType=Post":
            giellatags.remove("+Adp")
            giellatags.insert(0, "+Po")
        elif featstruct == "Number=Sing":
            if "Person=" not in feats:
                giellatags.append("+Sg")
        elif featstruct == "Number=Dual":
            if "Person=" not in feats:
                giellatags.append("+Du")
        elif featstruct == "Number=Plur":
            if "Person=" not in feats:
                giellatags.append("+Pl")
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
        # hacks that use feat and val separately
        elif feat == "InfForm":
            giellatags.append("+Inf" + val)
        elif feat == "Clitic":
            giellatags.append("+Foc/" + val)
        elif feat == "HebBinyan":
            continue
        elif feat == "NumValue":
            continue  # ?
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


def get_upos(tags: list, lemma: str = "", surf: str = ""):
    if "N" in tags:
        if "Prop" in tags:
            return "PROPN"
        elif "Symbol" in tags:
            return "SYM"
        else:
            return "NOUN"
    elif "V" in tags:
        if "<aux>" in tags:
            return "AUX"
        else:
            return "VERB"
    elif "A" in tags:
        return "ADJ"
    elif "Adv" in tags:
        return "ADV"
    elif "CC" in tags:
        return "CCONJ"
    elif "CS" in tags:
        return "SCONJ"
    elif "Pron" in tags:
        return "PRON"
    elif "Pr" in tags:
        return "ADP"
    elif "Po" in tags:
        return "ADP"
    elif "Num" in tags:
        return "NUM"
    elif "CLB" in tags:
        return "PUNCT"
    elif "Pcle" in tags:
        return "PART"
    elif "PUNCT" in tags:
        return "PUNCT"
    elif "Interj" in tags:
        return "INTJ"
    elif "URL" in tags:
        return "PROPN"  # c.f. standard docu
    elif "?" in tags:
        return "X"
    else:
        print(f"cannot find upos from {surf} → {lemma} {tags}")
        return "X"


def get_xpos(tags: list, lemma: str = "", surf: str = ""):
    rv = []
    for tag in tags:
        if tag.startswith("<"):
            continue
        elif ":" in tag:
            continue
        elif "@" in tag:
            continue
        elif "#" in tag:
            continue
        else:
            rv.append(tag)
    if len(rv) > 2:
        return " ".join(rv[:2])
    else:
        return " ".join(rv)


def get_ufeats(tags: list, lemma: str = "", surf: str = ""):
    feats = []
    for tag in tags:
        if tag in ["N", "V", "A", "CC", "CS", "Adv", "Pron", "Prop", "Punct",
                   "<aux>", "CLB", "Symbol", "?", "Num", "PUNCT", "Po", "Pr",
                   "Pcle", "Interj", "CLBfinal", "URL"]:
            continue
        elif tag == "Imprt":
            feats.append("Mood=Imp")
        elif tag == "Cond":
            feats.append("Mood=Cond")
        elif tag == "Pot":
            feats.append("Mood=Pot")
        elif tag == "Ind":
            feats.append("Mood=Ind")
        elif tag == "Opt":
            feats.append("Mood=Opt")
        elif tag == "Prs":
            feats.append("Tense=Pres")
        elif tag == "Prt":
            feats.append("Tense=Past")
        elif tag == "Sg":
            feats.append("Number=Sing")
        elif tag == "Pl":
            feats.append("Number=Plur")
        elif tag == "Du":
            feats.append("Number=Dual")
        elif tag == "Nom":
            feats.append("Case=Nom")
        elif tag == "Gen":
            feats.append("Case=Gen")
        elif tag == "Ela":
            feats.append("Case=Ela")
        elif tag == "Ine":
            feats.append("Case=Ine")
        elif tag == "Loc":
            feats.append("Case=Loc")
        elif tag == "Ess":
            feats.append("Case=Ess")
        elif tag == "Ill":
            feats.append("Case=Ill")
        elif tag == "Acc":
            feats.append("Case=Acc")
        elif tag == "Par":
            feats.append("Case=Par")
        elif tag == "Abe":
            feats.append("Case=Abe")
        elif tag == "Com":
            feats.append("Case=Com")
        elif tag == "Sg1":
            feats.append("Number=Sing")
            feats.append("Person=1")
        elif tag == "Sg2":
            feats.append("Number=Sing")
            feats.append("Person=2")
        elif tag == "Sg3":
            feats.append("Number=Sing")
            feats.append("Person=3")
        elif tag == "Du1":
            feats.append("Number=Dual")
            feats.append("Person=1")
        elif tag == "Du2":
            feats.append("Number=Dual")
            feats.append("Person=2")
        elif tag == "Du3":
            feats.append("Number=Dual")
            feats.append("Person=3")
        elif tag == "Pl1":
            feats.append("Number=Plur")
            feats.append("Person=1")
        elif tag == "Pl2":
            feats.append("Number=Plur")
            feats.append("Person=2")
        elif tag == "Pl3":
            feats.append("Number=Plur")
            feats.append("Person=3")
        elif tag == "PxSg1":
            feats.append("Number[psor]=Sing")
            feats.append("Person[psor]=1")
        elif tag == "PxSg2":
            feats.append("Number[psor]=Sing")
            feats.append("Person[psor]=2")
        elif tag == "PxSg3":
            feats.append("Number[psor]=Sing")
            feats.append("Person[psor]=3")
        elif tag == "PxDu1":
            feats.append("Number[psor]=Dual")
            feats.append("Person[psor]=1")
        elif tag == "PxDu2":
            feats.append("Number[psor]=Dual")
            feats.append("Person[psor]=2")
        elif tag == "PxDu3":
            feats.append("Number[psor]=Dual")
            feats.append("Person[psor]=3")
        elif tag == "PxPl1":
            feats.append("Number[psor]=Plur")
            feats.append("Person[psor]=1")
        elif tag == "PxPl2":
            feats.append("Number[psor]=Plur")
            feats.append("Person[psor]=2")
        elif tag == "PxPl3":
            feats.append("Number[psor]=Plur")
            feats.append("Person[psor]=3")
        elif tag == "PrsPrc":
            feats.append("VerbForm=Part")
            feats.append("Tense=Pres")
        elif tag == "PrfPrc":
            feats.append("VerbForm=Part")
            feats.append("Tense=Past")
        elif tag == "Indef":
            feats.append("PronType=Ind")
        elif tag == "Recipr":
            feats.append("PronType=Rec")
        elif tag == "Dem":
            feats.append("PronType=Dem")
        elif tag == "Interr":
            feats.append("PronType=Int")
        elif tag == "Rel":
            feats.append("PronType=Rel")
        elif tag == "Pers":
            feats.append("PronType=Pers")
        elif tag == "Refl":
            feats.append("Reflex=Yes")
        elif tag == "Ord":
            feats.append("NumType=Ord")
        elif tag == "Coll":
            feats.append("NumType=Sets")
        elif tag == "Neg":
            feats.append("Polarity=Neg")
        elif tag == "ConNeg":
            feats.append("Connegative=Yes")
        elif tag == "ABBR":
            feats.append("Abbr=Yes")
        elif tag == "ACR":
            feats.append("Abbr=Yes")
        elif tag == "Err/Orth":
            feats.append("Typo=Yes")
        elif tag == "Err/MissingSpace":
            feats.append("Typo=Yes")
        elif tag == "Err/Lex":
            continue
        elif tag.startswith("Foc/"):
            feats.append("Clitic=" + tag[4:])
        elif tag == "Qst":
            continue  # XXX: this should be something
        elif tag == "Inf":
            feats.append("VerbForm=Inf")
        elif tag == "Actio":
            feats.append("VerbForm=Inf?")
        elif tag == "VAbess":
            feats.append("VerbForm=Inf?")
            feats.append("Case=Abe")
        elif tag == "VGen":
            feats.append("VerbForm=Inf?")
            feats.append("Case=Gen")
        elif tag == "Ger":
            feats.append("VerbForm=Ger")
        elif tag == "Sup":
            feats.append("VerbForm=Sup")
        elif tag.startswith("Gram/TAbbr"):
            continue
        elif tag.startswith("Cmp"):
            continue
        elif tag.startswith("<") and tag.endswith(">"):
            continue
        elif tag in ["TV", "IV"]:
            continue
        elif tag.startswith("Ex/"):
            continue
        elif tag.startswith("Der/"):
            continue
        elif tag.startswith("Sem/"):
            continue
        elif tag.startswith("Gram/"):
            continue
        elif tag.startswith("LEFT"):
            continue  # XXX
        elif tag.startswith("RIGHT"):
            continue  # XXX
        elif tag in ["Rom", "Arab"]:
            continue
        elif tag.startswith("Dyn"):
            continue
        elif tag == "Attr":
            continue  # XXX: check if should be upd in ud standards?
        elif tag == "Sg1":
            feats.append("Number=Sing")
            feats.append("Person=1")
        elif tag == "Sg2":
            feats.append("Number=Sing")
            feats.append("Person=2")
        elif tag == "Sg3":
            feats.append("Number=Sing")
            feats.append("Person=3")
        elif tag == "Subqst":
            continue  # FIXME what is this?
        elif tag == "Logo":
            continue  # FIXME what is this?
        elif tag == "ImprtII":
            continue  # FIXME what is this?
        elif tag == "Allegro":
            continue
        elif tag == "NomAg":
            continue
        elif tag == "Known":
            continue  # ???
        elif tag.startswith("@"):
            continue
        elif tag.startswith("SUBSTITUTE:") or tag.startswith("REMOVE:") or \
                tag.startswith("MAP:") or tag.startswith("SETPARENT:") or \
                tag.startswith("SELECT:") or tag.startswith("IFF:") or \
                tag.startswith("ADD:"):
            continue
        elif tag.startswith("#") and "->" in tag:
            continue
        elif tag.startswith("<W:"):
            continue
        else:
            print(f"Unhandled giella tag! {tag} in {surf} → {lemma} {tags}")
            exit(1)
    return "|".join(sorted(feats))


def get_dep(tags: list, lemma: str="", surf: str=""):
    depfrom = 0
    depto = 0
    dep = "dep"
    for tag in tags:
        if tag.startswith("#") and "->" in tag:
            arrow = tag.find("->")
            depfrom = int(tag[1:arrow])
            depto = int(tag[arrow+2:])
        elif tag.startswith("@"):
            if tag == "@>N" and "Pron" in tags and "Dem" in tags:
                dep = "det"
            elif tag == "@>N" and "Pron" in tags and "Indef" in tags:
                dep = "det"
            elif tag == "@>N" and "A" in tags:
                dep = "amod"
            elif tag == "@>N" and "PrsPrc" in tags:
                dep = "amod"
            elif tag == "@>N" and "PrfPrc" in tags:
                dep = "amod"
            elif tag == "@>N" and "Num" in tags:
                dep = "nummod"
            elif tag == "@>N" and "Gen" in tags:
                dep = "nmod:poss"
            elif tag == "@>N":
                dep = "obl"
            elif tag == "@N<" and "jieš" == lemma:
                dep = "advmod"
            elif tag == "@N<":
                dep = "obl"
            elif tag == "@>Num" and "N" in tags:
                dep = "nmod"
            elif tag == "@Num<" and "N" in tags:
                dep = "nmod"
            elif tag == "@>Num":
                dep = "amod"
            elif tag == "@Num<":
                dep = "amod?"
            elif tag == "@>A" and "Num" in tags:
                dep = "nummod"
            elif tag == "@>A":
                dep = "amod?"  # XXX
            elif tag == "@A<" and "V" in tags:
                dep = "xcomp"
            elif tag == "@SUBJ>":
                dep = "nsubj"
            elif tag == "@<SUBJ":
                dep = "nsubj"
            elif tag == "@OBJ>":
                dep = "obj"
            elif tag == "@<OBJ":
                dep = "obj"
            elif tag == "@-FSUBJ>":
                dep = "nsubj"
            elif tag == "@-F<SUBJ":
                dep = "nsubj"
            elif tag == "@ICLOBJ":
                dep = "ccomp"
            elif tag == "@-F<OBJ":
                dep = "obj"
            elif tag == "@-FOBJ>":
                dep = "obj"
            elif tag == "@FMV":
                dep = "root"
            elif tag == "@FMVdic":
                dep = "parataxis"
            elif tag == "@IMV":
                dep = "root?"
            elif tag == "@+FMAINV":
                dep = "root"
            elif tag == "@-FMAINV":
                dep = "root?"
            elif tag == "@FS-VFIN<":
                dep = "aux"
            elif tag == "@FS-OBJ":
                dep = "ccomp"
            elif tag == "@FS-N<":
                dep = "aux?"
            elif tag == "@FS-IMV":
                dep = "ccomp"
            elif tag == "@FS-N<IAUX":
                dep = "xcomp"
            elif tag == "@FS-N<IMV":
                dep = "xcomp"
            elif tag == "@S<":
                dep = "conj??"
            elif tag == "@ICL-OBJ":
                dep = "obj?"
            elif tag == "@FS-ADVL>":
                dep = "acl?"
            elif tag == "@P<":
                dep = "case"
            elif tag == "@>P":
                dep = "case"
            elif tag == "@ADVL":
                dep = "obl"
            elif tag == "@ADVL>":
                dep = "obl"
            elif tag == "@ADVL<":
                dep = "obl"
            elif tag == "@<ADVL":
                dep = "obl"
            elif tag == "@>ADVL":
                dep = "obl"
            elif tag == "@ADVL-ine>":
                dep = "obl"
            elif tag == "@<ADVL-ine":
                dep = "obl"
            elif tag == "@<ADVL-ela":
                dep = "obl"
            elif tag == "@-FADVL>":
                dep = "obl"
            elif tag == "@>N" and "Gen" in tags:
                dep = "nmod:poss"
            elif tag == "@>Num" and "Gen" in tags:
                dep = "nmod:poss"
            elif tag == "@>N" and "Prop" in tags:
                dep = "flat"
            elif tag == "@>N" and "N" in tags:
                dep = "compound"
            elif tag == "@>Pron":
                dep = "obl?"
            elif tag == "@Pron<":
                dep = "obl?"
            elif tag == "@APP-ADVL<":
                dep = "appos"
            elif tag == "@APP-Pron<":
                dep = "appos"
            elif tag == "@APP-N<":
                dep = "appos"
            elif tag in ["@CVP", "@CNP"]:
                dep = "cc"
            elif tag == "@FAUX":
                dep = "aux"
            elif tag == "@+FAUXV":
                dep = "aux"
            elif tag == "@-FAUXV":
                dep = "aux"
            elif tag == "@IAUX":
                dep = "aux"
            elif tag == "@FS-IAUX":
                dep = "aux?"
            elif tag == "@FS-<ADVL":
                dep = "acl"
            elif tag == "@SPRED>":
                dep = "obl"
            elif tag == "@OPRED>":
                dep = "obl?"
            elif tag == "@<OPRED":
                dep = "obl?"
            elif tag == "@-F<OPRED":
                dep = "obl?"
            elif tag == "@<SPRED":
                dep = "ccomp?"
            elif tag == "@HNOUN":
                dep = "nmod?"
            elif tag == "@ADVL>CS":
                dep = "advcl"
            elif tag == "@COMP-CS<":
                dep = "mark"
            elif tag == "@>CC":
                dep = "conj"
            elif tag == "@INTERJ":
                dep = "discourse"
            elif tag == "@VOC":
                dep = "vocative"
            elif tag == "@PCLE":
                dep = "discourse"
            elif tag == "@X":
                dep = "dep"
            else:
                print(f"Unhandled dep tag {tag} in {surf} → {lemma} {tags}")
                exit(1)
    if dep == "dep" and "CLB" in tags or "Punct" in tags:
        dep = "punct"
    return dep, depto




