#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(fname, 'r').read()


setup(
    name='lordvivek',
    packages=['lordvivek'],
    version='1.3',
    description='See lord in action',
    author='Vivek Anand',
    author_email='vivekanand1101@gmail.com',
    url='https://lookupinthesky.heaven',
    keywords=['lord', 'hell', 'heaven', 'vivek'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2 :: Only',

    ],
    license='GNU General Public License v2.0',
    entry_points={
        'console_scripts': [
            'god = lordvivek.app:app'
        ],
    },
    include_package_data=True,
    install_requires=['click'],
    zip_safe=False,
)
