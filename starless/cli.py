#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 13:17:21 2019 mstenber
# Last modified: Mon Aug  5 11:05:51 2019 mstenber
# Edit time:     10 min
#
"""

"""

import argparse
import difflib

from .rewriter import rewrite, rewrite_file


def diff_file(filename):
    s = open(filename).read()
    s2 = rewrite(s)
    l = s.split('\n')
    l2 = s2.split('\n')
    return difflib.context_diff(l, l2,
                                fromfile=f'{filename}.old', tofile=filename,
                                lineterm='')


def main(*, args=None):
    p = argparse.ArgumentParser()
    p.add_argument('-t', '--test', action='store_true',
                   help='Test only (prints context diff of changes).')
    p.add_argument('files', metavar='PYFILE', type=str, nargs='+',
                   help='.py files to eliminate star includes from')
    args = p.parse_args(args=args)
    for filename in args.files:
        if args.test:
            print('\n'.join(diff_file(filename)))
        else:
            rewrite_file(filename)
