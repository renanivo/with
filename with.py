#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import subprocess
import sys

try:
    import __builtin__
    input = getattr(__builtin__, 'raw_input')
except (ImportError, AttributeError):
    pass

cmd = sys.argv[1]

while True:
    try:
        sub = input('{}> '.format(cmd))
        call = '{cmd} {sub}'.format(cmd=cmd, sub=sub)
        subprocess.check_call(call, shell=True)

    except KeyboardInterrupt, EOFError:
        sys.exit()

    except subprocess.CalledProcessError, e:
        pass
