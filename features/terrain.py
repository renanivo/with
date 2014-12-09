# -*- coding: utf-8 -*-
import difflib

from lettuce import world


@world.absorb
def diff(text1, text2):
    differ = difflib.Differ()
    diff_text = differ.compare(text1.splitlines(), text2.splitlines())
    return "\n".join(diff_text)
