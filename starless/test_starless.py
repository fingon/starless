#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 13:20:08 2019 mstenber
# Last modified: Mon Aug  5 10:42:10 2019 mstenber
# Edit time:     5 min
#
"""

"""

import pytest

import starless

basic_in = '''
from sys import *

stdin.write('whee')
stdout.read()
'''

basic_out = '''
from sys import stdin, stdout

stdin.write('whee')
stdout.read()
'''

nested_in = '''
from urllib.response import *

addbase('whee')
'''

nested_out = '''
from urllib.response import addbase

addbase('whee')
'''


@pytest.mark.parametrize('i,o', [
    (basic_in, basic_out),
    (nested_in, nested_out),
])
def test_basic(i, o):
    s = starless.rewrite(i)
    assert s == o
