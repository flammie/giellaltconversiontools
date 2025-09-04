#!/usr/bin/env -O python3
"""Handling of lexc stuff."""


def print_lexc_preamble(f):
    """Print lexc stuff that is required in the beginning of the file."""
    print("Multichar_Symbols", file=f)
    for tag in ["+N", "+V", "+A", "+Adv", "+Pcle", "+Adp", "+X", "+CC", "+CS",
                "+Interj", "+Punct", "+Sym", "+Prn", "+Det"]:
        print(tag, file=f)
    print(file=f)
    print("LEXICON Root", file=f)


def lexc_escape(s: str) -> str:
    """Escape lexc reserved symbols."""
    s = s.replace("%", "@PERCENT@")
    s = s.replace(" ", "% ")
    s = s.replace(";", "%;")
    s = s.replace("#", "%#")
    s = s.replace(":", "%:")
    s = s.replace("\"", "%\"")
    s = s.replace("<", "%<")
    s = s.replace(">", "%>")
    s = s.replace("!", "%!")
    s = s.replace("@PERCENT@", "%%")
    return s
