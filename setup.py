#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name="platformer",
      version="1.0-dev",
      description="A cross-platform way to compile and run C files",
      author=u"The PyPy team, maintained by Maciej Fijałkowski",
      author_email='fijall@gmail.com',
      url='http://github.com/fijal/platformer',
      packages=['platformer'],
      scripts=[],
      install_requires=['py'],
      zip_safe=True)
