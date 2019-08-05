#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 14:03:08 2019 mstenber
# Last modified: Mon Aug  5 11:11:16 2019 mstenber
# Edit time:     7 min
#
"""

"""

import tempfile

from .cli import main
from .test_starless import basic_in, basic_out


def test_main():
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(basic_in)
        f.flush()
        main(args=[f.name])
        with open(f.name) as g:
            assert g.read() == basic_out


diff_text = ''' Rewrote 2 star imports
*** /tmp/tmp_ew7_ab8.old
--- /tmp/tmp_ew7_ab8
***************
*** 1,5 ****

! from sys import *

  stdin.write('whee')
  stdout.read()
--- 1,5 ----

! from sys import stdin, stdout

  stdin.write('whee')
  stdout.read()
'''


def test_diff(capsys):
    with tempfile.NamedTemporaryFile('w') as f:
        f.write(basic_in)
        f.flush()
        main(args=['-t', f.name])
        captured = capsys.readouterr()

        def _string_to_lines(s):
            return [x.rstrip() for x in s.split('\n') if '/tmp/' not in x]
        assert _string_to_lines(captured.out) == _string_to_lines(diff_text)
