#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 13:12:42 2019 mstenber
# Last modified: Tue Feb 12 13:33:50 2019 mstenber
# Edit time:     5 min
#
"""

"""

from setuptools import setup

setup(name='starless',
      version='0.1',
      description='Star import eliminator',
      url='http://github.com/fingon/starless',
      author='Markus Stenberg',
      author_email='markus.stenberg@iki.fi',
      license='GPLv2',
      install_requires=['redbaron', 'pyflakes'],
      entry_points={
          'console_scripts': ['starless=starless.cli:main'],
      },
      packages=['starless'])
