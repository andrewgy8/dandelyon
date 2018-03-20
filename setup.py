#!/usr/bin/env python

"""The setup.py file for Python Fire."""

from setuptools import setup, find_packages


LONG_DESCRIPTION = """
Dandelion is a library for handling deprecation events that occur
naturally in software's lifecycle.  
With the help of some decorators, you can gracefully manage your API's 
deprecations without user interference. 
""".strip()

SHORT_DESCRIPTION = """
A library for handling deprecation warnings and events.
""".strip()

DEPENDENCIES = [
    'six',
]

TEST_DEPENDENCIES = [
    'coverage',
]

VERSION = '0.1.0'
URL = 'https://github.com/andrewgy8/dandelion'


setup(name='Dandelion',
      version=VERSION,
      description=SHORT_DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url=URL,
      author='Andrew Graham-Yooll',
      author_email='andrewgy8@gmail.com',
      packages=find_packages(),
      test_suite='tests.test_deprecate',
      install_requires=DEPENDENCIES,
      tests_require=TEST_DEPENDENCIES
      )

