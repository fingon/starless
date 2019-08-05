#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Python -*-
#
# Author: Markus Stenberg <fingon@iki.fi>
#
# Copyright (c) 2019 Markus Stenberg
#
# Created:       Tue Feb 12 13:12:42 2019 mstenber
# Last modified: Mon Aug  5 11:14:05 2019 mstenber
# Edit time:     7 min
#
"""

"""

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='starless',
      version='0.3',
      description='Star import eliminator',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/fingon/starless',
      author='Markus Stenberg',
      author_email='markus.stenberg@iki.fi',
      license='GPLv2',
      install_requires=['redbaron', 'pyflakes'],
      entry_points={
          'console_scripts': ['starless=starless.cli:main'],
      },
      packages=['starless'])
