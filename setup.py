#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='Deprecant',
      version='0.1',
      description='Python Deprecation Decorator',
      author='Andrew Graham-Yooll',
      author_email='andrewgy8@gmail.com',
      packages=find_packages(),
      test_suite='tests.test_deprecate'
      )
