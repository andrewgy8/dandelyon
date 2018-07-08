#!/usr/bin/env python

"""The setup.py file for Python Fire."""

import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install


class VerifyVersionCommand(install):
    """Custom command to verify that 
    the git tag matches our version"""

    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

LONG_DESCRIPTION = """
Dandelyon is a library for handling deprecation events that occur
naturally in software's lifecycle.  
With the help of some decorators, you can gracefully manage your API's 
deprecations without user interference. 
""".strip()

SHORT_DESCRIPTION = """
A library for handling deprecation warnings and events.
""".strip()

DEPENDENCIES = []

TEST_DEPENDENCIES = [
    'coverage',
]

VERSION = '0.2.5'
URL = 'https://github.com/andrewgy8/dandelyon'


setup(name='Dandelyon',
      version=VERSION,
      description=SHORT_DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      url=URL,
      author='Andrew Graham-Yooll',
      author_email='andrewgy8@gmail.com',
      packages=find_packages(),
      test_suite='tests.test_deprecate',
      install_requires=DEPENDENCIES,
      tests_require=TEST_DEPENDENCIES,
      keywords='deprecate deprecation decorator',
      python_requires='>=3',
      cmdclass={
          'verify': VerifyVersionCommand,
          }
      )

