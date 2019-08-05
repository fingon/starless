#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 13:21:52 2019 mstenber
# Last modified: Mon Aug  5 11:00:27 2019 mstenber
# Edit time:     51 min
#
"""

"""

import importlib
import os
import sys
import tempfile

from pyflakes.api import check
from pyflakes.messages import ImportStarUsage, ImportStarUsed
from pyflakes.reporter import Reporter
from redbaron import RedBaron


class RewriterReporter(Reporter):
    def __init__(self, rewriter):
        super().__init__(sys.stdout, sys.stderr)
        self.rewriter = rewriter

    def flake(self, message):
        if isinstance(message, ImportStarUsed):
            return
        if isinstance(message, ImportStarUsage):
            self.rewriter.add_undefined(message.message_args[0], str(message))
            return
        super().flake(message)


class Rewriter:
    def rewrite_string(self, s, filename='<string>'):
        self.undefined = {}
        self.red = RedBaron(s)
        self.star_imports = self.find_star_imports()
        if not self.star_imports:
            print(' No star imports detected')
            return
        rr = RewriterReporter(self)
        check(s, filename, rr)
        missing = set()
        for name in sorted(list(self.undefined.keys())):
            for _, m, l in self.star_imports.values():
                if hasattr(m, name):
                    l.append(name)
                    break
                # print('Not found', name, m)
            else:
                missing.add(name)
        if missing:
            print('Unable to commit due to inability to find following:')
            for k in sorted(missing):
                print(' ', self.undefined[k])
            return
        # Everything found; stars can go
        rewrote = 0
        for fi, _, l in self.star_imports.values():
            if l:
                rewrote += len(l)
                fi.targets = ', '.join(sorted(l))
        print(f' Rewrote {rewrote} star imports')

    def add_undefined(self, s, msg):
        self.undefined[s] = msg

    def find_star_imports(self):
        d = {}
        for fi in self.red.find_all('FromImportNode'):
            # Only handle star import-only statements for now
            if str(fi.targets[0]) != '*':
                continue
            if len(fi.targets) != 1:
                print(f' Too many imports in {fi}')
                continue
            name = '.'.join([str(x) for x in fi.value])
            d[name] = [fi, importlib.import_module(name), []]
        return d

    # PyChecker reporter API


def rewrite(s):
    r = Rewriter()
    r.rewrite_string(s)
    return r.red.dumps()


def rewrite_file(filename):
    print('Handling', filename)
    s = open(filename, 'r').read()
    r = Rewriter()
    r.rewrite_string(s, filename)
    s2 = r.red.dumps()
    if s == s2:
        print(' No difference in', filename)
        return
    with tempfile.NamedTemporaryFile('w', dir=os.path.dirname(filename), delete=False) as f:
        try:
            f.write(s2)
            f.flush()
            os.rename(f.name, filename)
        except:
            os.unlink(f.name)
            raise
    print()
