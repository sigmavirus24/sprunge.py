#!/usr/bin/env python

import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] in ("submit", "publish"):
    os.system("python setup.py sdist upload")
    sys.exit()

packages = []
requires = ['requests>=0.12.1']

setup(
    name="sprunge.py",
    version="0.1",
    description="A small python script to post files to http://sprunge.us",
    long_description="\n\n".join([open("README.rst").read(), 
        open("HISTORY.rst").read()]),
    author="Ian Cordasco",
    author_email="graffatcolmingov@gmail.com",
    url="https://github.com/sigmavirus24/sprunge.py",
    package_data={'': ['LICENSE']},
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
        ),
    scripts=["sprunge.py"]
    )
