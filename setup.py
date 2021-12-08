#!/usr/bin/env python

# Copyright (c) 2011 Pavel T
# Copyright (c) 2021 Pheme Pte Ltd
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from setuptools import setup, Extension

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('LICENSE', 'r') as f:
    license_ = f.read()

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='sql_validator',
    version='1.0.0',
    description='SQL Validation script',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Sophia Hale',
    author_email='support@currentsapi.services',
    url='https://github.com/currentsapi/sql_syntax_validator',
    keywords='language detection library',
    packages=['sql_validator'],
    package_data={'sql_validator': ['sql_validator/*']},
    include_package_data=True,
    install_requires=['fasttext'],
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)