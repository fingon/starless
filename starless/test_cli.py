#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 14:03:08 2019 mstenber
# Last modified: Tue Feb 12 14:05:53 2019 mstenber
# Edit time:     2 min
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
