#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
import csv2txt;

setup(
    name='csv2txt',
    version=csv2txt.getVersion(),
    author='gyk001',
    author_email='gyk001@gmail.com',
    url='https://github.com/gyk001/csv2txt',
    description=u'Convert a csv file to token separator txt file\n',
    packages=['csv2txt'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'csv2txt=csv2txt.cmd:convert_by_cmd'
        ]
    }
)