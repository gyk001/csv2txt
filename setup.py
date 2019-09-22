#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
import csv2txt;
import os;

setup(
    name='csv2txt',
    version=csv2txt.getVersion(),
    author='gyk001',
    author_email='gyk001@gmail.com',
    url='https://github.com/gyk001/csv2txt',
    platforms = "any",
    license='MIT',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    description=u'Convert a csv file to token separator txt file\n把csv文件转换为分隔符分隔的文本文件，支持跨行单元格哦',
    keywords='csv txt',
    packages=['csv2txt'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'csv2txt=csv2txt.cmd:convert_by_cmd'
        ]
    }
)