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
    long_description_content_type='text/markdown',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    description=u'Convert a csv file to token separator txt file(把csv文件转换为分隔符分隔的文本文件，支持跨行单元格哦)',
    keywords='csv txt convert',
    packages=['csv2txt'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux'
    ],
     project_urls={
        'Documentation': 'https://github.com/gyk001/csv2txt',
        'Source': 'https://github.com/gyk001/csv2txt',
        'Tracker': 'https://github.com/gyk001/csv2txt/issues',
    },
    install_requires=[],
    entry_points={
        'console_scripts': [
            'csv2txt=csv2txt.cmd:convert_by_cmd'
        ]
    }
)