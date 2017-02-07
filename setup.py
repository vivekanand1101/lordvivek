#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(fname).read()


setup(
    name='lordvivek',
    packages=['lordvivek'],
    version='1.1',
    description='CLI tool for imports to Pagure',
    long_description=read('Readme.md'),
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
    install_requires=read('requirements.txt'),
    zip_safe=False,
)
