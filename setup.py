#!/usr/bin/env python

import os
from setuptools import setup

LICENSE = open(
    os.path.join(os.path.dirname(__file__), 'LICENSE')).read().strip()

DESCRIPTION = open(
    os.path.join(os.path.dirname(__file__), 'README.md')).read().strip()

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Software Development",
]

setup(
    name='forwardable.py',
    version='0.0.1',
    description='pythoniac port forwardable from Ruby',
    author='OGURA_Daiki',
    author_email='8hachibee125@gmail.com',
    url='https://github.com/hachibeeDI/forwardable.py',
    py_modules=['forwardable'],
    keywords=['forwardable', 'delegate', ],
    classifiers=classifiers,
    install_requires=[''],
    license=LICENSE,
    long_description=DESCRIPTION,
    test_suite='')
