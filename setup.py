#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
import versioneer

setup(name='skeleton',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      author="Richard Lu",
      author_email="ddcien.lu@gmail.com",
      url="https://github.com/ddcien/skeleton",
      packages=["skeleton"],
      package_dir={"": "src"},
      license="WTFPL")
