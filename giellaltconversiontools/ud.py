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

GIELLA2UPOS = {
    "A": "ADJ",
    "Adv": "ADV",
    "CC": "CCONJ",
    "CS": "SCONJ",
    "Pron": "PRON",
    "Pr": "ADP",
    "Po": "ADP",
    "Num": "NUM",
    "CLB": "PUNCT",
    "Pcle": "PART",
    "PUNCT": "PUNCT",
    "Interj": "INTJ",
    "URL": "PROPN",  # c.f. standard docu
    "?": "X",
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
        "Gender=Fem,Neut": ["+Ut"],
        "Gender=Fem": ["+Fem"],
        "Gender=Neut": ["+Neut"],
        "Gender[psor]=Fem": ["+PxFem"],
        "Gender[psor]=Masc": ["+PxMasc"],
        "Gender[psor]=Masc,Neut": ["+PxMascNeut"],
        "Gender[abs]=Neut": [],  # ?
        "Gender[obj]=Masc": [],
        "Animacy=Anim": ["+Sem/Animate"],
        "Animacy=Inan": ["+Sem/Inanimate"],
        "Animacy=Hum": ["+Sem/Human"],
        "Animacy=Nhum": ["+Sem/-Human"],
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
        "Aspect=Prosp": [],
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
        "Number=Coll": ["+Pl"],  # XXX
        "Number=Count": [],  # XXX
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
        "Number[abs]=Sing": [],  # c.f. Person[grnd]
        "Number[abs]=Plur": [],  # c.f. Person[grnd]
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
        "AdpType=Voc": [],  # rest AdpType is handled in code
        "AdpType=Comprep": [],  # rest AdpType is handled in code
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
        "PronType=Exc":  [],
        "PronType=Neg":  ["+Neg"],
        "AdjType=Attr":  ["+Attr"],
        "AdjType=Pred":  ["+Pred"],
        "ConjType=Oper":  [],
        "Polarity=Pos": [],
        "Polarity=Neg":  ["+Neg"],
        "Tense=Pres": ["+Prs"],
        "Tense=Past": ["+Prt"],
        "Tense=Imp": ["+Prt"],
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
        "Degree=Equ": [],  # ?
        "Degree=Pos": [],  # ?
        "Degree=Cmp": ["+Comp"],
        "Degree=Sup": ["+Sup"],
        "Degree=Aug": ["+Aug"],
        "Degree=Dim": ["+Dim"],
        "VerbType=Aux": ["+Aux"],
        "VerbType=Cop": ["+Cop"],
        "VerbType=Mod": [],
        "VerbType=Pas": [],
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
        "Deixis[psor]=Prox": [],  # XXX
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
        "NounType=Clf": [],
        "NegationType=Contrastive": [],
        "PunctType=Elip": [],
        "PunctType=Peri": [],
        "PunctType=Comm": [],
        "PunctType=Brck": [],
        "PunctSide=Ini": [],
        "PunctSide=Fin": [],
        "Red=Yes": [],
        "Modality=Proh": [],
        "Modality=Cond": ["+Cond"],
        "Foc=Yes": ["+Foc"],
        "Compound=Yes": [],  # XXX #+cmp should go in the middle?
        "NounBase=Suffixal": [],
        "NounBase=Bound": [],
        "NounBase=Free": [],
        "Subcat=Tran": ["+TV"],
        "Subcat=Intr": ["+IV"],
        "TV=Yes": ["+TV"],
        "Tv=Yes": ["+TV"],
        "Hyph=Yes": ["+Cmp/Hyph"],  # mayge?
        "PrepCase=Pre": [],  # ?
        "PrepCase=Npr": [],  # ?
}

GIELLA2UFEATS = {
        "N": [],
        "V": [],
        "A": [],
        "CC": [],
        "CS": [],
        "Adv": [],
        "Pron": [],
        "Prop": [],
        "Punct": [],
        "<aux>": [],
        "CLB": [],
        "Symbol": [],
        "?": [],
        "Num": [],
        "PUNCT": [],
        "Po": [],
        "Pr": [],
        "Pcle": [],
        "Interj": [],
        "CLBfinal": [],
        "URL": [],
         "Imprt":  ["Mood=Imp"],
         "Cond": ["Mood=Cond"],
         "Pot": ["Mood=Pot"],
         "Ind": ["Mood=Ind"],
         "Opt": ["Mood=Opt"],
         "Prs": ["Tense=Pres"],
         "Prt": ["Tense=Past"],
         "Sg": ["Number=Sing"],
         "Pl": ["Number=Plur"],
         "Du": ["Number=Dual"],
         "Nom": ["Case=Nom"],
         "Gen": ["Case=Gen"],
         "Ela": ["Case=Ela"],
         "Ine": ["Case=Ine"],
         "Loc": ["Case=Loc"],
         "Ess": ["Case=Ess"],
         "Ill": ["Case=Ill"],
         "Acc": ["Case=Acc"],
         "Par": ["Case=Par"],
         "Abe": ["Case=Abe"],
         "Com": ["Case=Com"],
         "Sg1": ["Number=Sing", "Person=1"],
         "Sg2": ["Number=Sing", "Person=2"],
         "Sg3": ["Number=Sing", "Person=3"],
         "Du1": ["Number=Dual", "Person=1"],
         "Du2": ["Number=Dual", "Person=2"],
         "Du3": ["Number=Dual", "Person=3"],
         "Pl1": ["Number=Plur", "Person=1"],
         "Pl2": ["Number=Plur", "Person=2"],
         "Pl3": ["Number=Plur", "Person=3"],
         "PxSg1": ["Number[psor]=Sing", "Person[psor]=1"],
         "PxSg2": ["Number[psor]=Sing", "Person[psor]=2"],
         "PxSg3": ["Number[psor]=Sing", "Person[psor]=3"],
         "PxDu1": ["Number[psor]=Dual", "Person[psor]=1"],
         "PxDu2": ["Number[psor]=Dual", "Person[psor]=2"],
         "PxDu3": ["Number[psor]=Dual", "Person[psor]=3"],
         "PxPl1": ["Number[psor]=Plur", "Person[psor]=1"],
         "PxPl2": ["Number[psor]=Plur", "Person[psor]=2"],
         "PxPl3": ["Number[psor]=Plur", "Person[psor]=3"],
         "PrsPrc": ["VerbForm=Part", "Tense=Pres"],
         "PrfPrc": ["VerbForm=Part", "Tense=Past"],
         "Indef": ["PronType=Ind"],
         "Recipr": ["PronType=Rec"],
         "Dem": ["PronType=Dem"],
         "Interr": ["PronType=Int"],
         "Rel": ["PronType=Rel"],
         "Pers": ["PronType=Pers"],
         "Refl": ["Reflex=Yes"],
         "Ord": ["NumType=Ord"],
         "Coll": ["NumType=Sets"],
         "Neg": ["Polarity=Neg"],
         "ConNeg": ["Connegative=Yes"],
         "ABBR": ["Abbr=Yes"],
         "ACR": ["Abbr=Yes"],
         "Err/Orth": ["Typo=Yes"],
         "Err/MissingSpace": ["Typo=Yes"],
         "Err/Lex": [],
         "Qst": [],  # XXX: this should be something
         "Inf": ["VerbForm=Inf"],
         "Actio": ["VerbForm=Inf?"],
         "VAbess": ["VerbForm=Inf?", "Case=Abe"],
         "VGen": ["VerbForm=Inf?", "Case=Gen"],
         "Ger": ["VerbForm=Ger"],
         "Sup": ["VerbForm=Sup"],
         "TV": [],
         "IV": [],
         "Rom": [],
         "Arab": [],
         "Attr": [],  # XXX: check if should be upd in ud standards?
         "Subqst": [],  # FIXME what is this?
         "Logo": [],  # FIXME what is this?
         "ImprtII": [],  # FIXME what is this?
         "Allegro": [],
         "NomAg": [],  # XXX?
         "Known": [],  # ???


}


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
        # things that overwrite things
        elif featstruct == "AdpType=Prep":
            if "+Adp" in giellatags:
                giellatags.remove("+Adp")
            giellatags.insert(0, "+Pr")
        elif featstruct == "AdpType=Post":
            if "+Adp" in giellatags:
                giellatags.remove("+Adp")
            giellatags.insert(0, "+Po")
        elif featstruct == "AdpType=Ambi":
            if "+Adp" in giellatags:
                giellatags.remove("+Adp")
            giellatags.insert(0, "+Po")
            giellatags.insert(0, "+Pr")
        # things that may depend on things
        elif featstruct == "Number=Sing":
            if "Person=" not in feats:
                giellatags.append("+Sg")
        elif featstruct == "Number=Dual":
            if "Person=" not in feats:
                giellatags.append("+Du")
        elif featstruct == "Number=Plur":
            if "Person=" not in feats:
                giellatags.append("+Pl")
        # things that depend on things like always
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
        elif featstruct == "Person[abs]=1":
            if "Number[abs]=Sing" in feats:
                giellatags.append("+a_Sg1")
            elif "Number[abs]=Plur" in feats:
                giellatags.append("+a_Pl1")
        elif featstruct == "Person[abs]=2":
            if "Number[abs]=Sing" in feats:
                giellatags.append("+a_Sg2")
            elif "Number[abs]=Plur" in feats:
                giellatags.append("+a_Pl2")
        elif featstruct == "Person[obj]=3":
            if "Number[abs]=Sing" in feats:
                giellatags.append("+a_Sg3")
            elif "Number[abs]=Plur" in feats:
                giellatags.append("+a_Pl3")
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
        # skippable feats (not relevant)
        elif feat == "Polite":
            continue
        elif feat == "InflClass":
            continue
        elif feat == "VerbClass":
            continue
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
            print(f"Unhandled UFeat {featstruct} in {feats}")
            sys.exit(1)
    return giellatags


def get_upos(tags: list, lemma: str = "", surf: str = ""):
    """Convert giella tags into UPOS."""
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
    for g in GIELLA2UPOS:
        if g in tags:
            return GIELLA2UPOS[g]
    print(f"cannot find upos from {surf} → {lemma} {tags}")
    return "X"


def get_xpos(tags: list, lemma: str = "", surf: str = ""):
    """Convert giella tags int XPOS."""
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
        return "+" + "+".join(rv[:2])
    else:
        return "+" + "+".join(rv)


def get_ufeats(tags: list, lemma: str = "", surf: str = ""):
    """Convert giella tags into universal feature structures."""
    feats = []
    for tag in tags:
        if tag in GIELLA2UFEATS:
            for feat in GIELLA2UFEATS[tag]:
                feats.append(feat)
        elif tag.startswith("Foc/"):
            feats.append("Clitic=" + tag[4:])
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
        elif tag.startswith("Dyn"):
            continue
        elif tag.startswith("Cmp"):
            continue
        elif tag.startswith("<") and tag.endswith(">"):
            continue
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
    """Convert Giella CG annotations to UD dependency annotations."""
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
                sys.exit(1)
    if dep == "dep" and "CLB" in tags or "Punct" in tags:
        dep = "punct"
    return dep, depto




