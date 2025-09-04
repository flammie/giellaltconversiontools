#!/usr/bin/env -O python3
import re

import pyhfst


def remove_flags(s):
    return re.sub('@[^@]*@', '', s)

def load_hfst(f):
    his = pyhfst.HfstInputStream(f)
    return his.read()
