#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 13:17:21 2019 mstenber
# Last modified: Tue Feb 12 14:07:26 2019 mstenber
# Edit time:     5 min
#
"""

"""

import argparse

from .rewriter import rewrite_file


def main(*, args=None):
    p = argparse.ArgumentParser()
    p.add_argument('files', metavar='PYFILE', type=str, nargs='+',
                   help='.py files to eliminate star includes from')
    args = p.parse_args(args=args)
    for filename in args.files:
        rewrite_file(filename)
